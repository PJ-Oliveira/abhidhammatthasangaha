#!/usr/bin/env python3
"""
Gera o dicionário offline 100% autônomo e de alta fidelidade para o Abhidhammatthasaṅgaha.
Extrai todos os vocábulos e compostos dos 9 capítulos e consulta o Digital Pāli Dictionary (dpd-mobile.db).
Traduz integralmente para Português e Espanhol com léxico estritamente Abhidhammika Theravāda.
"""

import json
import sqlite3
import re
import unicodedata
import os
import glob

DB_PATH = '/Users/pauloo/Desktop/abhidhamma-ai-agente and book translations/_NAO_SUBIR_bancos_originais/dpd-mobile.db'
CHAPTERS_DIR = 'src/data/chapters'
OUTPUT_DICT_PATH = 'src/data/paliDictionary.json'

# Termos técnicos Abhidhamma e Theravāda (EN -> PT, ES)
PHRASE_MAP = {
    "cognitive series": ("processo cognitivo; curso mental", "proceso cognitivo; curso mental"),
    "mental sequence": ("sequência mental; processo mental", "secuencia mental; proceso mental"),
    "mental process": ("processo mental", "proceso mental"),
    "cognitive process": ("processo cognitivo", "proceso cognitivo"),
    "related to the realm of sense desire": ("pertencente à esfera sensorial", "perteneciente a la esfera de los sentidos"),
    "realm of sense desire": ("esfera dos sentidos; reino sensorial", "esfera de los sentidos; reino sensorial"),
    "realm of sensual desire": ("esfera sensorial; reino do desejo", "esfera sensorial; reino del deseo"),
    "sensual realm": ("esfera sensorial; reino do desejo", "esfera sensorial; reino del deseo"),
    "sensual desire": ("desejo sensorial; apego aos sentidos", "deseo sensorial; apego a los sentidos"),
    "sense desire": ("desejo dos sentidos", "deseo de los sentidos"),
    "fine material realm": ("esfera da matéria sutil", "esfera de la materia sutil"),
    "fine-material realm": ("esfera da matéria sutil", "esfera de la materia sutil"),
    "immaterial realm": ("esfera imaterial", "esfera inmaterial"),
    "supramundane": ("supramundano; transcendente", "supramundano; trascendente"),
    "mental concomitant": ("fator mental associado; concomitante mental", "factor mental asociado; concomitante mental"),
    "mental factor": ("fator mental; cetasika", "factor mental; cetasika"),
    "mental factors": ("fatores mentais", "factores mentales"),
    "mental state": ("estado mental", "estado mental"),
    "mental states": ("estados mentais", "estados mentales"),
    "material phenomenon": ("fenômeno material; rūpa", "fenómeno material; rūpa"),
    "material phenomena": ("fenômenos materiais", "fenómenos materiales"),
    "physical phenomenon": ("fenômeno físico", "fenómeno físico"),
    "physical phenomena": ("fenômenos físicos", "fenómenos físicos"),
    "primary element": ("grande elemento primário; mahābhūta", "gran elemento primario; mahābhūta"),
    "four great elements": ("quatro grandes elementos", "cuatro grandes elementos"),
    "water element": ("elemento água; coesão", "elemento agua; cohesión"),
    "earth element": ("elemento terra; solidez", "elemento tierra; solidez"),
    "fire element": ("elemento fogo; temperatura", "elemento fuego; temperatura"),
    "air element": ("elemento ar; movimento", "elemento aire; movimiento"),
    "wind element": ("elemento vento; mobilidade", "elemento viento; movilidad"),
    "sense door": ("porta sensorial", "puerta sensorial"),
    "mind door": ("porta mental", "puerta mental"),
    "eye door": ("porta visual", "puerta visual"),
    "ear door": ("porta auditiva", "puerta auditiva"),
    "nose door": ("porta olfativa", "puerta olfativa"),
    "tongue door": ("porta gustativa", "puerta gustativa"),
    "body door": ("porta corporal", "puerta corporal"),
    "life continuum": ("fluxo da existência passiva; bhavaṅga", "continuo de la existencia; bhavaṅga"),
    "subconscious life-continuum": ("fluxo subliminar da existência; bhavaṅga", "flujo subliminal de la existencia; bhavaṅga"),
    "passive consciousness": ("consciência passiva; bhavaṅga", "conciencia pasiva; bhavaṅga"),
    "active consciousness": ("consciência ativa; javana", "conciencia activa; javana"),
    "registration consciousness": ("consciência de retenção; tadārammaṇa", "conciencia de retención; tadārammaṇa"),
    "determining consciousness": ("consciência determinante; voṭṭhabbana", "conciencia determinante; voṭṭhabbana"),
    "investigating consciousness": ("consciência investigadora; santīraṇa", "conciencia investigadora; santīraṇa"),
    "receiving consciousness": ("consciência receptora; sampaṭicchana", "conciencia receptora; sampaṭicchana"),
    "adverting consciousness": ("consciência de advertência; āvajjana", "conciencia de advertencia; āvajjana"),
    "death consciousness": ("consciência de morte; cuticitta", "conciencia de muerte; cuticitta"),
    "rebirth-linking consciousness": ("consciência de renascimento; paṭisandhicitta", "conciencia de renacimiento; paṭisandhicitta"),
    "heart base": ("base cardíaca; sede física da mente", "base cardíaca; sede física de la mente"),
    "heart-base": ("base cardíaca; sede física da mente", "base cardíaca; sede física de la mente"),
    "physical seat of consciousness": ("sede física da consciência", "sede física de la conciencia"),
    "sensitive matter": ("matéria sensível; órgão sutil", "materia sensible; órgano sutil"),
    "nutritive essence": ("essência nutritiva; alimento material", "esencia nutritiva; alimento material"),
    "applied thought": ("pensamento aplicado; vitakka", "pensamiento aplicado; vitakka"),
    "sustained thought": ("pensamento sustentado; vicāra", "pensamiento sostenido; vicāra"),
    "one-pointedness of mind": ("unidirecionalidade da mente; concentração", "unidireccionalidad de la mente; concentración"),
    "desire to act": ("desejo de agir; intenção saudável; chanda", "deseo de actuar; intención saludable; chanda"),
    "loving-kindness": ("amor-bondade; benevolência; mettā", "amor bondoso; benevolencia; mettā"),
    "sympathetic joy": ("alegria altruísta; muditā", "alegría empática; muditā"),
    "moral shame": ("pudor moral; vergonha do mal; hiri", "pudor moral; vergüenza del mal; hiri"),
    "moral dread": ("temor moral; receio do mal; ottappa", "temor moral; recelo del mal; ottappa"),
    "fear of wrongdoing": ("temor de agir mal; receio moral", "temor de obrar mal; recelo moral"),
    "fearlessness of wrongdoing": ("ausência de temor moral; desfaçatez", "ausencia de temor moral; desfachatez"),
    "unwholesome root": ("raiz prejudicial; raiz não hábil", "raíz perjudicial; raíz no hábil"),
    "wholesome root": ("raiz salutar; raiz hábil", "raíz saludable; raíz hábil"),
    "indeterminate": ("indeterminado; neutro", "indeterminado; neutro"),
    "inoperative": ("funcional; sem fruto kármico", "inoperante; funcional; sin fruto"),
    "kamma result": ("resultado kármico; fruto da ação", "resultado kármico; fruto de la acción"),
    "latent tendency": ("tendência latente; anusaya", "tendencia latente; anusaya"),
    "mental hindrance": ("obstáculo mental; nīvaraṇa", "obstáculo mental; nīvaraṇa"),
    "cycle of rebirth": ("ciclo de renascimentos; saṃsāra", "ciclo de renacimientos; saṃsāra"),
    "round of rebirth": ("ciclo de renascimentos; saṃsāra", "ciclo de renacimientos; saṃsāra"),
    "four noble truths": ("quatro nobres verdades", "cuatro nobles verdades"),
    "noble eightfold path": ("nobre caminho óctuplo", "noble óctuple sendero"),
    "root of evil": ("raiz do mal; raiz prejudicial", "raíz del mal; raíz perjudicial"),
    "wrong view": ("visão incorreta; diṭṭhi", "visión errónea; diṭṭhi"),
    "unprompted": ("não induzido; espontâneo; asaṅkhārika", "no instigado; espontáneo; asaṅkhārika"),
    "prompted": ("induzido; instigado; sasaṅkhārika", "instigado; inducido; sasaṅkhārika"),
    "accompanied by joy": ("acompanhado de alegria", "acompañado de alegría"),
    "accompanied by equanimity": ("acompanhado de equanimidade", "acompañado de ecuanimidad"),
    "accompanied by displeasure": ("acompanhado de desprazer", "acompañado de desagrado"),
    "accompanied by pain": ("acompanhado de dor", "acompañado de dolor"),
    "accompanied by pleasure": ("acompanhado de prazer", "acompañado de placer"),
    "accompanied by": ("acompanhado de", "acompañado de"),
    "associated with": ("associado a", "asociado con"),
    "dissociated from": ("dissociado de", "disociado de"),
    "connected with": ("conectado com", "conectado con"),
    "consciousness accompanied by": ("consciência acompanhada de", "conciencia acompañada de"),
    "rooted in": ("enraizado em; com raiz em", "enraizado en; con raíz en"),
}

WORD_MAP = {
    "mind": ("mente", "mente"),
    "consciousness": ("consciência", "conciencia"),
    "thought": ("pensamento", "pensamiento"),
    "matter": ("matéria", "materia"),
    "materiality": ("materialidade", "materialidad"),
    "form": ("forma", "forma"),
    "feeling": ("sensação", "sensación"),
    "sensation": ("sensação", "sensación"),
    "perception": ("percepção", "percepción"),
    "volition": ("volição", "volición"),
    "intention": ("intenção", "intención"),
    "aggregate": ("agregado", "agregado"),
    "aggregates": ("agregados", "agregados"),
    "element": ("elemento", "elemento"),
    "elements": ("elementos", "elementos"),
    "faculty": ("faculdade", "facultad"),
    "faculties": ("faculdades", "facultades"),
    "base": ("base", "base"),
    "bases": ("bases", "bases"),
    "sphere": ("esfera", "esfera"),
    "spheres": ("esferas", "esferas"),
    "object": ("objeto", "objeto"),
    "objects": ("objetos", "objetos"),
    "door": ("porta", "puerta"),
    "doors": ("portas", "puertas"),
    "eye": ("olho", "ojo"),
    "ear": ("ouvido", "oído"),
    "nose": ("nariz", "nariz"),
    "tongue": ("língua", "lengua"),
    "body": ("corpo", "cuerpo"),
    "sound": ("som", "sonido"),
    "smell": ("odor; cheiro", "olor"),
    "taste": ("sabor", "sabor"),
    "phenomenon": ("fenômeno", "fenómeno"),
    "phenomena": ("fenômenos", "fenómenos"),
    "quality": ("qualidade", "cualidad"),
    "qualities": ("qualidades", "cualidades"),
    "teaching": ("ensinamento", "enseñanza"),
    "teachings": ("ensinamentos", "enseñanzas"),
    "nature": ("natureza", "naturaleza"),
    "characteristic": ("característica", "característica"),
    "characteristics": ("características", "características"),
    "cause": ("causa", "causa"),
    "causes": ("causas", "causas"),
    "condition": ("condição", "condición"),
    "conditions": ("condições", "condiciones"),
    "root": ("raiz", "raíz"),
    "roots": ("raízes", "raíces"),
    "origin": ("origem", "origen"),
    "cessation": ("cessação", "cesación"),
    "extinction": ("extinção", "extinción"),
    "liberation": ("libertação", "liberación"),
    "suffering": ("sofrimento", "sufrimiento"),
    "pain": ("dor; sofrimento", "dolor; sufrimiento"),
    "pleasure": ("prazer", "placer"),
    "happiness": ("felicidade", "felicidad"),
    "joy": ("alegria", "alegría"),
    "rapture": ("júbilo", "júbilo"),
    "equanimity": ("equanimidade", "ecuanimidad"),
    "grief": ("pesar; dor", "pesar; dolor"),
    "greed": ("cobiça; apego", "codicia; apego"),
    "attachment": ("apego", "apego"),
    "craving": ("desejo ardente; taṇhā", "ansia; sed; taṇhā"),
    "hatred": ("aversão; ódio; dosa", "aversión; odio; dosa"),
    "aversion": ("aversão", "aversión"),
    "delusion": ("delusão; ilusão; moha", "delusión; ilusión; moha"),
    "ignorance": ("ignorância; avijjā", "ignorancia; avijjā"),
    "sloth": ("preguiça; torpor", "pereza; torpor"),
    "torpor": ("torpor mental", "torpor mental"),
    "restlessness": ("inquietação; agitação", "inquietud; agitación"),
    "worry": ("remorso; preocupação", "remordimiento; preocupación"),
    "doubt": ("dúvida cética; vicikicchā", "duda escéptica; vicikicchā"),
    "faith": ("confiança; fé; saddhā", "confianza; fe; saddhā"),
    "mindfulness": ("atenção plena; sati", "atención plena; sati"),
    "concentration": ("concentração mental; samādhi", "concentración mental; samādhi"),
    "wisdom": ("sabedoria; compreensão; paññā", "sabiduría; comprensión; paññā"),
    "insight": ("visão analítica profunda; vipassanā", "visión profunda; vipassanā"),
    "calm": ("tranquilidade; samatha", "tranquilidad; samatha"),
    "absorption": ("absorção meditativa; jhāna", "absorción meditativa; jhāna"),
    "path": ("nobre caminho; magga", "noble sendero; magga"),
    "fruition": ("fruição espiritual; phala", "fructificación espiritual; phala"),
    "unbinding": ("desatar; libertação; nibbāna", "liberación; desapego; nibbāna"),
    "rebirth": ("renascimento", "renacimiento"),
    "action": ("ação intencional; kamma", "acción intencional; kamma"),
    "result": ("resultado; fruto", "resultado; fruto"),
    "wholesome": ("salutar; benéfico; hábil; kusala", "saludable; hábil; kusala"),
    "unwholesome": ("prejudicial; não hábil; akusala", "perjudicial; no hábil; akusala"),
    "indeterminate": ("indeterminado; neutro; abyākata", "indeterminado; neutro; abyākata"),
    "beautiful": ("belo; nobre; sobhana", "bello; noble; sobhana"),
    "rootless": ("sem raízes; ahetuka", "sin raíces; ahetuka"),
    "unprompted": ("não induzido; asaṅkhārika", "no inducido; asaṅkhārika"),
    "prompted": ("induzido; instigado; sasaṅkhārika", "inducido; instigado; sasaṅkhārika"),
    "accompanied": ("acompanhado", "acompañado"),
    "associated": ("associado", "asociado"),
    "dissociated": ("dissociado", "disociado"),
    "wrong": ("incorreto; errôneo", "erróneo; incorrecto"),
    "view": ("visão; entendimento", "visión; visión"),
    "eight": ("oito", "ocho"),
    "twelve": ("doze", "doce"),
    "two": ("dois", "dos"),
    "one": ("um", "uno"),
    "four": ("quatro", "cuatro"),
    "fourteen": ("quatorze", "catorce"),
    "twenty": ("vinte", "veinte"),
    "twenty-eight": ("vinte e oito", "veintiocho"),
    "eighty-nine": ("oitenta e nove", "ochenta y nueve"),
    "one hundred and twenty-one": ("cento e vinte e um", "ciento veintiuno"),
    "called": ("chamado; conhecido como", "llamado; conocido como"),
    "known": ("conhecido", "conocido"),
    "named": ("chamado; de nome", "nombrado; llamado"),
    "among": ("entre; dentre", "entre; de entre"),
    "these": ("estes; estas", "estos; estas"),
    "which": ("qual; o qual", "cuál; el cual"),
    "what": ("o que; que", "qué; lo que"),
    "how": ("como", "cómo"),
    "thus": ("assim; deste modo", "así; de este modo"),
    "there": ("lá; nisso; ali", "allí; en eso"),
    "here": ("aqui", "aquí"),
    "now": ("agora", "ahora"),
    "then": ("então", "entonces"),
    "also": ("também", "también"),
    "and": ("e", "y"),
    "or": ("ou", "o"),
    "not": ("não", "no"),
    "all": ("todo; todos; tudo", "todo; todos"),
    "only": ("apenas; somente", "solo; solamente"),
    "desire": ("desejo", "deseo"),
    "power": ("poder", "poder"),
    "taken": ("tomado", "tomado"),
    "born": ("nascido", "nacido"),
    "reason": ("razão; motivo", "razón; motivo"),
    "fact": ("fato", "hecho"),
    "case": ("caso", "caso"),
}

POS_MAP = {
    'adj': 'adj.',
    'noun': 'subst.',
    'masc': 'm.',
    'fem': 'f.',
    'nt': 'nt.',
    'verb': 'v.',
    'pr': 'v. pres.',
    'aor': 'v. aor.',
    'fut': 'v. fut.',
    'opt': 'v. opt.',
    'imp': 'v. imp.',
    'pp': 'part. pass.',
    'prp': 'part. pres.',
    'ptp': 'gerundivo',
    'grd': 'gerundivo',
    'ger': 'gerúndio',
    'ind': 'indecl.',
    'adv': 'adv.',
    'pron': 'pron.',
    'num': 'num.',
    'comp': 'comp.',
    'sandhi': 'sandhi',
}

def translate_dpd(text: str, lang: str = 'pt') -> str:
    if not text:
        return ""
    idx = 0 if lang == 'pt' else 1
    t = text
    # 1. Frases completas (ordenadas por comprimento decrescente)
    for phrase, trans in sorted(PHRASE_MAP.items(), key=lambda x: len(x[0]), reverse=True):
        pattern = re.compile(re.escape(phrase), re.IGNORECASE)
        t = pattern.sub(trans[idx], t)
    # 2. Palavras individuais
    words = t.split()
    res = []
    for w in words:
        w_clean = re.sub(r'^[^\w]+|[^\w]+$', '', w).lower()
        if w_clean in WORD_MAP:
            replacement = WORD_MAP[w_clean][idx]
            res.append(w.replace(w_clean, replacement))
        else:
            # Sufixos comuns seguros
            if w_clean.endswith('tion'):
                suf = 'ção' if lang == 'pt' else 'ción'
                res.append(w.replace(w_clean, w_clean[:-4] + suf))
            elif w_clean.endswith('ity'):
                suf = 'idade' if lang == 'pt' else 'idad'
                res.append(w.replace(w_clean, w_clean[:-3] + suf))
            elif w_clean.endswith('ble'):
                suf = 'vel' if lang == 'pt' else 'ble'
                res.append(w.replace(w_clean, w_clean[:-3] + suf))
            else:
                res.append(w)
    return " ".join(res)

def translate_meaning(meaning_en: str) -> tuple[str, str]:
    if not meaning_en:
        return "", ""
    subs = [s.strip() for s in meaning_en.split(';') if s.strip()]
    pt_list = []
    es_list = []
    for sub in subs:
        pt_t = translate_dpd(sub, 'pt')
        es_t = translate_dpd(sub, 'es')
        if pt_t and pt_t not in pt_list:
            pt_list.append(pt_t)
        if es_t and es_t not in es_list:
            es_list.append(es_t)
    pt_final = "; ".join(pt_list) if pt_list else meaning_en
    es_final = "; ".join(es_list) if es_list else meaning_en
    return pt_final, es_final

def format_grammar(pos_raw: str, grammar_raw: str) -> str:
    parts = []
    if pos_raw:
        for p in pos_raw.split(','):
            p_strip = p.strip()
            parts.append(POS_MAP.get(p_strip, p_strip))
    if grammar_raw and grammar_raw not in parts:
        parts.append(grammar_raw)
    return ", ".join(parts) if parts else "termo"

def main():
    print(f"Lendo capítulos em {CHAPTERS_DIR}...")
    token_counts = {}
    tokens_ordered = []
    
    for fpath in sorted(glob.glob(f"{CHAPTERS_DIR}/ch*.json")):
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for seg in data:
                pali = seg.get('pali', '')
                clean_pali = re.sub(r'<[^>]+>', ' ', pali)
                toks = re.findall(r'[a-zA-ZāīūñṅṭḍṇḷṃĀĪŪÑṄṬḌṆḶṂ]+', clean_pali)
                for t in toks:
                    tl = t.lower()
                    if tl not in token_counts:
                        tokens_ordered.append(tl)
                    token_counts[tl] = token_counts.get(tl, 0) + 1

    print(f"Total de tokens únicos no Abhidhammatthasaṅgaha: {len(token_counts)}")

    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Banco DPD não encontrado em: {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Dicionário final: { pali_key: entry_obj }
    entries_map = {}
    seen_hw_ids = set()

    def add_headword_entry(hid: int):
        if hid in seen_hw_ids:
            return
        seen_hw_ids.add(hid)
        
        cur.execute('SELECT id, lemma_1, pos, grammar, meaning_1, root_key, construction FROM dpd_headwords WHERE id = ?', (hid,))
        row = cur.fetchone()
        if not row or not row[4]:
            return
            
        hid, lemma_1, pos, grammar, meaning_1, root_key, construction = row
        clean_lemma = re.sub(r'\s+\d+(\.\d+)?$', '', lemma_1).strip()
        if not clean_lemma or len(clean_lemma) < 2:
            return
            
        pt_m, es_m = translate_meaning(meaning_1)
        root_info = construction if construction else (root_key if root_key else None)
        gram = format_grammar(pos, grammar)
        
        entry = {
            "pali": clean_lemma,
            "meaning": {
                "en": meaning_1,
                "pt": pt_m,
                "es": es_m
            },
            "grammar": gram,
        }
        if root_info:
            entry["root"] = root_info
            
        if clean_lemma.lower() in entries_map:
            existing = entries_map[clean_lemma.lower()]
            if meaning_1 not in existing["meaning"]["en"]:
                existing["meaning"]["en"] += f"; {meaning_1}"
                if pt_m and pt_m not in existing["meaning"]["pt"]:
                    existing["meaning"]["pt"] += f"; {pt_m}"
                if es_m and es_m not in existing["meaning"]["es"]:
                    existing["meaning"]["es"] += f"; {es_m}"
        else:
            entries_map[clean_lemma.lower()] = entry

    # Processa cada token do texto
    print("Mapeando vocábulos e lemas através do DPD...")
    matched_tokens = 0

    for tok in tokens_ordered:
        cur.execute('SELECT headwords, deconstructor, grammar FROM lookup WHERE lookup_key = ?', (tok,))
        row = cur.fetchone()
        hw_ids = []
        decon = []
        gram_info = ""
        
        if row:
            if row[0]:
                try: hw_ids = json.loads(row[0])
                except: pass
            if row[1]:
                try: decon = json.loads(row[1])
                except: pass
            if row[2]:
                try:
                    g_list = json.loads(row[2])
                    if g_list and isinstance(g_list, list) and len(g_list) > 0:
                        first = g_list[0]
                        if isinstance(first, list) and len(first) >= 3:
                            gram_info = f"{first[1]}, {first[2]}"
                except: pass
                
        # Adiciona headwords encontrados
        if hw_ids:
            matched_tokens += 1
            for hid in hw_ids:
                add_headword_entry(hid)
                
            # Se o token é uma forma flexionada (ex: kāmāvacaraṃ != kāmāvacara),
            # cria também a entrada da forma flexionada apontando diretamente para o significado!
            if tok not in entries_map:
                cur.execute('SELECT lemma_1, meaning_1, construction FROM dpd_headwords WHERE id = ?', (hw_ids[0],))
                hrow = cur.fetchone()
                if hrow and hrow[1]:
                    base_lemma = re.sub(r'\s+\d+(\.\d+)?$', '', hrow[0]).strip()
                    pt_m, es_m = translate_meaning(hrow[1])
                    gram_str = gram_info if gram_info else f"flexão de {base_lemma}"
                    surface_entry = {
                        "pali": tok,
                        "meaning": {
                            "en": f"{hrow[1]} (inflected form of {base_lemma})",
                            "pt": f"{pt_m} (forma flexionada de {base_lemma})",
                            "es": f"{es_m} (forma flexionada de {base_lemma})"
                        },
                        "grammar": gram_str,
                    }
                    if hrow[2]:
                        surface_entry["root"] = hrow[2]
                    entries_map[tok] = surface_entry
            continue
            
        # Se não teve headword direto, testa deconstructor
        if decon:
            matched_tokens += 1
            parts = [p.strip() for p in decon[0].split('+')]
            sub_meanings_en = []
            sub_meanings_pt = []
            sub_meanings_es = []
            
            for part in parts:
                cur.execute('SELECT headwords FROM lookup WHERE lookup_key = ?', (part,))
                prow = cur.fetchone()
                if prow and prow[0]:
                    try:
                        phw = json.loads(prow[0])
                        for h in phw:
                            add_headword_entry(h)
                            cur.execute('SELECT lemma_1, meaning_1 FROM dpd_headwords WHERE id = ?', (h,))
                            dhrow = cur.fetchone()
                            if dhrow and dhrow[1]:
                                pt_dm, es_dm = translate_meaning(dhrow[1])
                                sub_meanings_en.append(dhrow[1].split(';')[0])
                                sub_meanings_pt.append(pt_dm.split(';')[0])
                                sub_meanings_es.append(es_dm.split(';')[0])
                    except: pass
                    
            if sub_meanings_en and tok not in entries_map:
                entries_map[tok] = {
                    "pali": tok,
                    "meaning": {
                        "en": f"Compound: {' + '.join(parts)} ({'; '.join(sub_meanings_en[:3])})",
                        "pt": f"Composto: {' + '.join(parts)} ({'; '.join(sub_meanings_pt[:3])})",
                        "es": f"Compuesto: {' + '.join(parts)} ({'; '.join(sub_meanings_es[:3])})"
                    },
                    "grammar": "composto (sandhi)",
                    "root": " + ".join(parts)
                }
            continue
            
        # Sandhi strip (ti, nti, pi, ca, eva)
        for sfx in ['nti', 'ti', 'pi', 'ca', 'eva', 'miva']:
            if tok.endswith(sfx) and len(tok) > len(sfx) + 2:
                base = tok[:-len(sfx)]
                cur.execute('SELECT headwords FROM lookup WHERE lookup_key = ?', (base,))
                brow = cur.fetchone()
                bhw = []
                if brow and brow[0]:
                    try: bhw = json.loads(brow[0])
                    except: pass
                if not bhw:
                    cur.execute('SELECT headwords FROM lookup WHERE lookup_key = ?', (base + 'ṃ',))
                    brow2 = cur.fetchone()
                    if brow2 and brow2[0]:
                        try: bhw = json.loads(brow2[0])
                        except: pass
                        
                if bhw:
                    matched_tokens += 1
                    for h in bhw: add_headword_entry(h)
                    cur.execute('SELECT lemma_1, meaning_1 FROM dpd_headwords WHERE id = ?', (bhw[0],))
                    bhrow = cur.fetchone()
                    if bhrow and bhrow[1] and tok not in entries_map:
                        pt_bm, es_bm = translate_meaning(bhrow[1])
                        base_lem = re.sub(r'\s+\d+(\.\d+)?$', '', bhrow[0]).strip()
                        entries_map[tok] = {
                            "pali": tok,
                            "meaning": {
                                "en": f"{bhrow[1]} [{base_lem} + {sfx}]",
                                "pt": f"{pt_bm} [{base_lem} + {sfx}]",
                                "es": f"{es_bm} [{base_lem} + {sfx}]"
                            },
                            "grammar": f"sandhi ({sfx})",
                            "root": f"{base_lem} + {sfx}"
                        }
                    break

    print(f"Tokens mapeados: {matched_tokens} / {len(token_counts)} ({matched_tokens*100/len(token_counts):.1f}%)")
    print(f"Total de verbetes no dicionário gerado: {len(entries_map)}")

    # Ordena alfabeticamente para renderização previsível
    final_dict = sorted(entries_map.values(), key=lambda e: e['pali'].lower())

    with open(OUTPUT_DICT_PATH, 'w', encoding='utf-8') as f:
        json.dump(final_dict, f, ensure_ascii=False, indent=2)

    print(f"Dicionário offline salvo com sucesso em: {OUTPUT_DICT_PATH} ({len(final_dict)} verbetes)")

if __name__ == '__main__':
    main()

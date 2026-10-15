#!/usr/bin/env python3
"""Gera src/data/ankiAtomicCards.ts: deck de cartões atômicos (1 fato por cartão).

O deck mestre (ankiCards.ts, 63 cartões) NÃO é alterado. Os cartões atômicos têm
`layer` (1 fundamental, 2 intermediária, 3 síntese) e `requires` (pré-requisitos
que precisam estar consolidados antes de o cartão ser liberado no modo Estudo).

Camadas: 1 = fundamental, 2 = intermediária, 3 = avançada (síntese).
Uso:  python3 scripts/build_atomic_cards.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TS_PATH = ROOT / "src/data/ankiAtomicCards.ts"

CHAPTER_NAMES = {
    1: {"pali": "Cittaparicchedo", "en": "Chapter 1: Consciousness",
        "pt": "Capítulo 1: Consciência", "es": "Capítulo 1: Conciencia"},
    3: {"pali": "Pakiṇṇakasaṅgahavibhāgo", "en": "Chapter 3: Miscellaneous Categories",
        "pt": "Capítulo 3: Categorias Diversas", "es": "Capítulo 3: Categorías Diversas"},
}

# (id, cap, categoria, seção, termo pāli, camada, requer, tags, {pt,en,es: (pergunta, resposta)})
C = []


def add(id_, ch, cat, sec, pali, layer, req, tags, pt, en, es, enrichment=None):
    C.append((id_, ch, cat, sec, pali, layer, req, tags, {"pt": pt, "en": en, "es": es}, enrichment or {}))


def AT(id_, ch, cat, sec, pali, req, tags, pt, en, es, enrichment=None):
    """Atalho: o campo legado `layer` é ignorado; o nível vem do grafo de requisitos."""
    add(id_, ch, cat, sec, pali, 0, req, tags, pt, en, es, enrichment)


P = "Paramattha Dhammas"
V = "Vedanā"
J = "Jāti"
B = "Bhūmi"
# ── Termos fundamentais (raízes do grafo: não dependem de nada) ───────────────
AT("at-t01", 1, "quantities", P, "Catudhā Paramatthato", [], ["paramattha"],
  ("Quantas e quais são as realidades últimas (paramattha dhamma)?", "4: citta, cetasika, rūpa e nibbāna."),
  ("How many and which are the ultimate realities (paramattha dhamma)?", "4: citta, cetasika, rūpa and nibbāna."),
  ("¿Cuántas y cuáles son las realidades últimas (paramattha dhamma)?", "4: citta, cetasika, rūpa y nibbāna."),
  enrichment={
    "pt": {"breakdown": ["Citta = consciência — 89 ou 121 tipos", "Cetasika = fatores mentais — 52 tipos", "Rūpa = matéria — 28 tipos", "Nibbāna = o incondicionado — único não produzido por causas"], "explanation": "Paramattha ('realidade última'): dhammas que existem por natureza intrínseca própria (sabhāva), irredutíveis. Realidades convencionais (sammuti) — 'pessoa', 'ser', 'eu' — são construtos mentais. Os 3 primeiros são condicionados (saṅkhata); somente Nibbāna é incondicionado (asaṅkhata).", "mnemonic": "C-C-R-N. Pegadinha de prova: Nibbāna é o ÚNICO paramattha incondicionado. 'Pessoa' e 'eu' NÃO são paramattha — são sammuti (convencionais)."},
    "en": {"breakdown": ["Citta = consciousness — 89 or 121 types", "Cetasika = mental factors — 52 types", "Rūpa = matter — 28 types", "Nibbāna = the unconditioned — the only one not produced by causes"], "explanation": "Paramattha ('ultimate reality'): dhammas that exist by their own intrinsic nature (sabhāva), irreducible. Conventional realities (sammuti) — 'person', 'being', 'self' — are mental constructs. The first 3 are conditioned (saṅkhata); Nibbāna alone is unconditioned (asaṅkhata).", "mnemonic": "C-C-R-N. Exam trap: Nibbāna is the ONLY unconditioned paramattha. 'Person' and 'self' are NOT paramattha — they are sammuti (conventional)."},
    "es": {"breakdown": ["Citta = conciencia — 89 o 121 tipos", "Cetasika = factores mentales — 52 tipos", "Rūpa = materia — 28 tipos", "Nibbāna = lo incondicionado — el único no producido por causas"], "explanation": "Paramattha ('realidad última'): dhammas que existen por su propia naturaleza intrínseca (sabhāva). Las realidades convencionales (sammuti) — 'persona', 'ser', 'yo' — son constructos mentales. Los primeros 3 son condicionados (saṅkhata); solo Nibbāna es incondicionado (asaṅkhata).", "mnemonic": "C-C-R-N. Trampa de examen: Nibbāna es el ÚNICO paramattha incondicionado. 'Persona' y 'yo' NO son paramattha — son sammuti (convencionales)."}
  })
AT("at-t02", 1, "philosophy", P, "Citta", ["at-t01"], ["citta"],
  ("O que é *citta*?", "Consciência: o que conhece (vijānana) o objeto."),
  ("What is *citta*?", "Consciousness: that which knows (vijānana) the object."),
  ("¿Qué es *citta*?", "Conciencia: lo que conoce (vijānana) el objeto."),
  enrichment={
    "pt": {"breakdown": ["Característica: conhecer um objeto (vijānana)", "Função: ser guia dos cetasikas (pubbangama)", "Manifestação: continuum de processos (sandhāna)", "Causa próxima: nāmarūpa (mente-e-matéria)"], "explanation": "Citta (de 'citi', conhecer) é definido de 3 formas: (1) como agente — o que conhece; (2) como instrumento — pelo qual os cetasikas conhecem; (3) como atividade — o próprio ato de conhecer. A 3ª é a mais precisa: citta não é um 'eu', mas o momento de conhecer que surge e cessa.", "mnemonic": "89 (ou 121) tipos. Não é alma ou eu — é o ato momentâneo de conhecer. Função = pubbangama (guia)."},
    "en": {"breakdown": ["Characteristic: knowing an object (vijānana)", "Function: forerunner of cetasikas (pubbangama)", "Manifestation: continuity of process (sandhāna)", "Proximate cause: nāmarūpa (mind-and-matter)"], "explanation": "Citta (from 'citi', to cognize) is defined 3 ways: (1) as agent — that which cognizes; (2) as instrument — that by which cetasikas cognize; (3) as activity — the act of cognizing itself. The 3rd is most accurate: citta is not a 'self' but a momentary flash of knowing that arises and ceases.", "mnemonic": "89 (or 121) types. Not self or soul — it is the momentary act of knowing. Function = pubbangama (forerunner)."},
    "es": {"breakdown": ["Característica: conocer un objeto (vijānana)", "Función: guía de los cetasikas (pubbangama)", "Manifestación: continuum de procesos (sandhāna)", "Causa próxima: nāmarūpa (mente-y-materia)"], "explanation": "Citta (de 'citi', conocer) se define de 3 formas: (1) como agente — lo que conoce; (2) como instrumento — por el cual los cetasikas conocen; (3) como actividad — el acto mismo de conocer. La 3ª es la más precisa: el citta no es un 'yo', sino el acto momentáneo de conocer.", "mnemonic": "89 (o 121) tipos. No es alma ni yo — es el acto momentáneo de conocer. Función = pubbangama (guía)."}
  })
AT("at-t03", 1, "philosophy", P, "Cetasika", ["at-t01"], ["cetasika"],
  ("O que é *cetasika*?", "Fator mental: surge e cessa junto com o citta, toma o mesmo objeto e tem a mesma base."),
  ("What is *cetasika*?", "Mental factor: arises and ceases together with the citta, takes the same object and has the same base."),
  ("¿Qué es *cetasika*?", "Factor mental: surge y cesa junto con el citta, toma el mismo objeto y tiene la misma base."),
  enrichment={
    "pt": {"breakdown": ["4 marcas: ekuppāda (mesmo surgimento), ekanirodha (mesma cessação), ekālambaṇa (mesmo objeto), ekavatthuka (mesma base física)", "52 tipos: 13 aññasamāna + 14 akusala + 25 sobhana", "Vedanā e saññā são cetasikas no Abhidhamma"], "explanation": "Cetasika ('pertencente à mente') nunca surge sozinho — sempre junto com o citta. Os 4 'eka-' expressam sua inseparabilidade. Vedanā (sensação) e saññā (percepção), que no Sutta são agregados separados, são aqui classificadas como cetasikas.", "mnemonic": "52 cetasikas = 13 + 14 + 25. Os 4 eka-: uppāda, nirodha, ālambaṇa, vatthuka. Pegadinha: vedanā e saññā são cetasikas no Abhidhamma."},
    "en": {"breakdown": ["4 marks: ekuppāda (same arising), ekanirodha (same cessation), ekālambaṇa (same object), ekavatthuka (same base)", "52 types: 13 aññasamāna + 14 akusala + 25 sobhana", "Vedanā and saññā are cetasikas in the Abhidhamma"], "explanation": "Cetasika ('belonging to the mind') never arises alone — always together with citta. The 4 'eka-' prefixes express their inseparability. Vedanā (feeling) and saññā (perception), separate aggregates in the Suttas, are classified here as cetasikas.", "mnemonic": "52 cetasikas = 13 + 14 + 25. The 4 eka-: uppāda, nirodha, ālambaṇa, vatthuka. Exam trap: vedanā and saññā are cetasikas in the Abhidhamma."},
    "es": {"breakdown": ["4 marcas: ekuppāda (mismo surgimiento), ekanirodha (misma cesación), ekālambaṇa (mismo objeto), ekavatthuka (misma base)", "52 tipos: 13 aññasamāna + 14 akusala + 25 sobhana", "Vedanā y saññā son cetasikas en el Abhidhamma"], "explanation": "Cetasika ('perteneciente a la mente') nunca surge solo — siempre junto con el citta. Los 4 'eka-' expresan su inseparabilidad. Vedanā (sensación) y saññā (percepción), agregados separados en los Suttas, se clasifican aquí como cetasikas.", "mnemonic": "52 cetasikas = 13 + 14 + 25. Los 4 eka-: uppāda, nirodha, ālambaṇa, vatthuka. Trampa: vedanā y saññā son cetasikas en el Abhidhamma."}
  })
AT("at-t04", 1, "philosophy", P, "Rūpa", ["at-t01"], ["rupa"],
  ("O que é *rūpa*?", "Matéria: fenômeno material, sujeito a mudança e deterioração (ruppana)."),
  ("What is *rūpa*?", "Matter: material phenomenon, subject to change and deterioration (ruppana)."),
  ("¿Qué es *rūpa*?", "Materia: fenómeno material, sujeto a cambio y deterioro (ruppana)."),
  enrichment={
    "pt": {"breakdown": ["28 tipos de rūpa: 4 grandes elementos (mahābhūta) + 24 derivados (upādārūpa)", "4 mahābhūta: terra (pṭhavī), água (āpo), fogo (tejo), ar (vāyo)", "Rūpa = único paramattha sem cognição — não conhece nada"], "explanation": "Rūpa (de 'ruppana', mudança/deterioração) é a 3ª realidade última. No Abhidhamma, matéria se analisa em 28 tipos irredutíveis. Os 4 elementos fundamentais estão sempre juntos e são a base de todo fenômeno material. Rūpa é condicionado e impermanente.", "mnemonic": "28 rūpas = 4 mahābhūta + 24 upādārūpa. Pegadinha: rūpa não tem cognição — só citta e cetasika conhecem. A palavra 'rūpa' no Abhidhamma = matéria, não 'forma visual'."},
    "en": {"breakdown": ["28 types of rūpa: 4 great elements (mahābhūta) + 24 derived (upādārūpa)", "4 mahābhūta: earth (pṭhavī), water (āpo), fire (tejo), air (vāyo)", "Rūpa = the only paramattha without cognition — it knows nothing"], "explanation": "Rūpa (from 'ruppana', change/deterioration) is the 3rd ultimate reality. In the Abhidhamma, matter is analyzed into 28 irreducible types. The 4 primary elements are always found together and are the basis of all material phenomena. Rūpa is conditioned and impermanent.", "mnemonic": "28 rūpas = 4 mahābhūta + 24 upādārūpa. Exam trap: rūpa has no cognition — only citta and cetasika know. 'Rūpa' in Abhidhamma = matter, not 'visual form'."},
    "es": {"breakdown": ["28 tipos de rūpa: 4 grandes elementos (mahābhūta) + 24 derivados (upādārūpa)", "4 mahābhūta: tierra (pṭhavī), agua (āpo), fuego (tejo), aire (vāyo)", "Rūpa = el único paramattha sin cognición — no conoce nada"], "explanation": "Rūpa (de 'ruppana', cambio/deterioro) es la 3ª realidad última. En el Abhidhamma, la materia se analiza en 28 tipos irreducibles. Los 4 grandes elementos siempre coexisten y son la base de todo fenómeno material. Rūpa es condicionado e impermanente.", "mnemonic": "28 rūpas = 4 mahābhūta + 24 upādārūpa. Trampa: rūpa no tiene cognición — solo el citta y cetasika conocen. 'Rūpa' en Abhidhamma = materia, no 'forma visual'."}
  })
AT("at-t05", 1, "philosophy", P, "Nibbāna", ["at-t01"], ["nibbana"],
  ("O que é *nibbāna* entre as realidades últimas?", "A realidade incondicionada (asaṅkhata): a única que não é produzida por causas."),
  ("What is *nibbāna* among the ultimate realities?", "The unconditioned reality (asaṅkhata): the only one not produced by causes."),
  ("¿Qué es *nibbāna* entre las realidades últimas?", "La realidad incondicionada (asaṅkhata): la única que no es producida por causas."),
  enrichment={
    "pt": {"breakdown": ["Asaṅkhata: não produzido, não condicionado, não composto", "Lokuttara: supramundano — transcende os 3 mundos (kāma, rūpa, arūpa)", "Tem 2 aspectos: sa-upādisesa (com base residual) e anupādisesa (sem base residual)", "Objeto de todo citta lokuttara (magga e phala)"], "explanation": "Nibbāna é a única realidade última sem origem causal. Não é aniquilação nem existência eterna — é a cessação do anseio (taṇhā) e do sofrimento (dukkha). No Abhidhamma, é o único paramattha sem características de surgimento e cessação.", "mnemonic": "Nibbāna = ÚNICO asaṅkhata (incondicionado) dentre os 4 paramattha. Pegadinha: Nibbāna NÃO é 'nada' — é uma realidade positiva, o objeto do magga-citta."},
    "en": {"breakdown": ["Asaṅkhata: unproduced, unconditioned, uncompounded", "Lokuttara: supramundane — transcends the 3 worlds (kāma, rūpa, arūpa)", "2 aspects: sa-upādisesa (with residual clinging-base) and anupādisesa (without residual base)", "Object of all lokuttara cittas (magga and phala)"], "explanation": "Nibbāna is the only ultimate reality without a causal origin. It is not annihilation nor eternal existence — it is the cessation of craving (taṇhā) and suffering (dukkha). In the Abhidhamma, it is the only paramattha without characteristics of arising and ceasing.", "mnemonic": "Nibbāna = ONLY asaṅkhata (unconditioned) among the 4 paramattha. Exam trap: Nibbāna is NOT 'nothing' — it is a positive reality, the object of the magga-citta."},
    "es": {"breakdown": ["Asaṅkhata: no producido, no condicionado, no compuesto", "Lokuttara: supramundano — trasciende los 3 mundos (kāma, rūpa, arūpa)", "2 aspectos: sa-upādisesa (con base residual) y anupādisesa (sin base residual)", "Objeto de todos los cittas lokuttara (magga y phala)"], "explanation": "Nibbāna es la única realidad última sin origen causal. No es aniquilación ni existencia eterna — es la cesación del ansia (taṇhā) y el sufrimiento (dukkha). En el Abhidhamma, es el único paramattha sin características de surgimiento y cesación.", "mnemonic": "Nibbāna = ÚNICO asaṅkhata (incondicionado) entre los 4 paramattha. Trampa: Nibbāna NO es 'nada' — es una realidad positiva, el objeto del magga-citta."}
  })
AT("at-t06", 1, "philosophy", P, "Sampayutta / Vippayutta", ["at-t03"], ["sampayutta"],
  ("O que significam *sampayutta* e *vippayutta*?", "Sampayutta: associado (surge junto com o fator em questão). Vippayutta: dissociado (surge sem ele)."),
  ("What do *sampayutta* and *vippayutta* mean?", "Sampayutta: associated (arises together with the factor in question). Vippayutta: dissociated (arises without it)."),
  ("¿Qué significan *sampayutta* y *vippayutta*?", "Sampayutta: asociado (surge junto con el factor en cuestión). Vippayutta: disociado (surge sin él)."),
  enrichment={
    "pt": {"breakdown": ["Sampayutta = co-surgente: o cetasika em questão ESTÁ presente naquele citta", "Vippayutta = não co-surgente: o cetasika NÃO está presente", "Ex.: lobha-mūla-citta é sampayutta com lobha, vippayutta com adosa", "Usado nas tabelas de co-presença (sampayoga)"], "explanation": "Estes termos descrevem a relação de associação entre cittas e cetasikas. Quando uma tabela diz 'vedanā-sampayutta', significa que o citta surge com vedanā como cetasika presente. O oposto, vippayutta, indica ausência do fator naquele momento.", "mnemonic": "Sampayutta = 'aparece junto'. Vippayutta = 'fica de fora'. Dica: sam- (junto) → sampayutta; vi- (separação) → vippayutta."},
    "en": {"breakdown": ["Sampayutta = co-arisen: the cetasika in question IS present in that citta", "Vippayutta = not co-arisen: the cetasika is NOT present", "E.g.: lobha-mūla-citta is sampayutta with lobha, vippayutta with adosa", "Used in co-presence tables (sampayoga)"], "explanation": "These terms describe the association relationship between cittas and cetasikas. When a table says 'vedanā-sampayutta', it means the citta arises with vedanā as a present cetasika. The opposite, vippayutta, indicates absence of the factor in that moment.", "mnemonic": "Sampayutta = 'arises with'. Vippayutta = 'left out'. Hint: sam- (together) → sampayutta; vi- (separation) → vippayutta."},
    "es": {"breakdown": ["Sampayutta = co-surgente: el cetasika en cuestión ESTÁ presente en ese citta", "Vippayutta = no co-surgente: el cetasika NO está presente", "Ej.: el lobha-mūla-citta es sampayutta con lobha, vippayutta con adosa", "Usado en tablas de co-presencia (sampayoga)"], "explanation": "Estos términos describen la relación de asociación entre cittas y cetasikas. Cuando una tabla dice 'vedanā-sampayutta', significa que el citta surge con vedanā como cetasika presente. Lo contrario, vippayutta, indica ausencia del factor en ese momento.", "mnemonic": "Sampayutta = 'surge con'. Vippayutta = 'queda fuera'. Pista: sam- (junto) → sampayutta; vi- (separación) → vippayutta."}
  })
AT("at-v01", 1, "quantities", V, "Pañca Vedanā", ["at-t03"], ["vedana"],
  ("Quais são as 5 vedanās (sensações)?", "Sukha, dukkha, somanassa, domanassa e upekkhā."),
  ("What are the 5 vedanās (feelings)?", "Sukha, dukkha, somanassa, domanassa and upekkhā."),
  ("¿Cuáles son las 5 vedanās (sensaciones)?", "Sukha, dukkha, somanassa, domanassa y upekkhā."),
  enrichment={
    "pt": {"breakdown": ["3 corporais: sukha (prazer), dukkha (dor), upekkhā (neutra)", "2 mentais: somanassa (alegria), domanassa (desgosto)", "Upekkhā pode ser corporal OU mental — única vedanā em ambos os tipos", "Nos Suttas = 3 vedanās; no Abhidhamma = 5 vedanās (subdivisão mais precisa)"], "explanation": "Vedanā é o segundo dos 5 khandhas e também um cetasika universal (sabbacittasādhāraṇa). No Abhidhamma, distinguem-se 5 qualidades afetivas: as corporais (corpo físico como base) e as mentais (mente como base). Upekkhā neutra existe nos dois domínios.", "mnemonic": "5 vedanās: 2 corporais (sukha/dukkha) + 2 mentais (somanassa/domanassa) + 1 neutra (upekkhā). Pegadinha: nos Suttas = 3 vedanās; no Abhidhamma = 5."},
    "en": {"breakdown": ["3 bodily: sukha (pleasure), dukkha (pain), upekkhā (neutral)", "2 mental: somanassa (joy), domanassa (displeasure)", "Upekkhā can be bodily OR mental — the only feeling in both types", "In the Suttas = 3 feelings; in the Abhidhamma = 5 feelings (more precise subdivision)"], "explanation": "Vedanā is the second of the 5 khandhas and also a universal cetasika (sabbacittasādhāraṇa). The Abhidhamma distinguishes 5 affective qualities: bodily (physical body as base) and mental (mind as base). Neutral upekkhā exists in both domains.", "mnemonic": "5 vedanās: 2 bodily (sukha/dukkha) + 2 mental (somanassa/domanassa) + 1 neutral (upekkhā). Exam trap: Suttas = 3 feelings; Abhidhamma = 5."},
    "es": {"breakdown": ["3 corporales: sukha (placer), dukkha (dolor), upekkhā (neutra)", "2 mentales: somanassa (alegría), domanassa (disgusto)", "Upekkhā puede ser corporal O mental — la única sensación de ambos tipos", "En los Suttas = 3 vedanās; en el Abhidhamma = 5 vedanās (subdivisión más precisa)"], "explanation": "Vedanā es el segundo de los 5 khandhas y también un cetasika universal (sabbacittasādhāraṇa). El Abhidhamma distingue 5 cualidades afectivas: corporales (cuerpo físico como base) y mentales (mente como base). La upekkhā neutra existe en ambos dominios.", "mnemonic": "5 vedanās: 2 corporales (sukha/dukkha) + 2 mentales (somanassa/domanassa) + 1 neutra (upekkhā). Trampa: Suttas = 3 sensaciones; Abhidhamma = 5."}
  })
AT("at-v02", 1, "philosophy", V, "Sukha / Dukkha", ["at-v01"], ["vedana"],
  ("O que são *sukha* e *dukkha* como vedanā?", "Sensação corporal agradável (sukha) e sensação corporal dolorosa (dukkha)."),
  ("What are *sukha* and *dukkha* as vedanā?", "Pleasant bodily feeling (sukha) and painful bodily feeling (dukkha)."),
  ("¿Qué son *sukha* y *dukkha* como vedanā?", "Sensación corporal agradable (sukha) y sensación corporal dolorosa (dukkha)."),
  enrichment={
    "pt": {"breakdown": ["Sukha/dukkha = vedanā CORPORAL: base = corpo (kāya)", "Surgem apenas nos 2 cittas do kāyaviññāṇa (consciência do toque)", "Sukha: kāyaviññāṇa vipāka kusala; Dukkha: kāyaviññāṇa vipāka akusala", "Distinto de somanassa/domanassa, que são MENTAIS"], "explanation": "No Abhidhamma, sukha e dukkha como vedanā referem-se exclusivamente à sensação física — o prazer ou dor corporal ao tocar um objeto tangível. São únicas nesse domínio: apenas 2 cittas (kāyaviññāṇa) podem tê-las como tonalidade afetiva.", "mnemonic": "Sukha/dukkha = CORPO. Somanassa/domanassa = MENTE. Regra: kāyaviññāṇa kusala → sukha; kāyaviññāṇa akusala → dukkha."},
    "en": {"breakdown": ["Sukha/dukkha = BODILY vedanā: base = body (kāya)", "Arise only in the 2 kāyaviññāṇa cittas (body-consciousness)", "Sukha: kusala kāyaviññāṇa vipāka; Dukkha: akusala kāyaviññāṇa vipāka", "Distinct from somanassa/domanassa, which are MENTAL"], "explanation": "In the Abhidhamma, sukha and dukkha as vedanā refer exclusively to physical sensation — bodily pleasure or pain when contacting a tangible object. They are unique in this domain: only 2 cittas (kāyaviññāṇa) can have them as the affective tone.", "mnemonic": "Sukha/dukkha = BODY. Somanassa/domanassa = MIND. Rule: kusala kāyaviññāṇa → sukha; akusala kāyaviññāṇa → dukkha."},
    "es": {"breakdown": ["Sukha/dukkha = vedanā CORPORAL: base = cuerpo (kāya)", "Surgen solo en los 2 cittas del kāyaviññāṇa (conciencia del tacto)", "Sukha: kāyaviññāṇa vipāka kusala; Dukkha: kāyaviññāṇa vipāka akusala", "Distinto de somanassa/domanassa, que son MENTALES"], "explanation": "En el Abhidhamma, sukha y dukkha como vedanā se refieren exclusivamente a la sensación física — el placer o dolor corporal al contactar un objeto tangible. Son únicos en este dominio: solo 2 cittas (kāyaviññāṇa) pueden tenerlos como tonalidad afectiva.", "mnemonic": "Sukha/dukkha = CUERPO. Somanassa/domanassa = MENTE. Regla: kāyaviññāṇa kusala → sukha; kāyaviññāṇa akusala → dukkha."}
  })
AT("at-v03", 1, "philosophy", V, "Somanassa / Domanassa", ["at-v01"], ["vedana"],
  ("O que são *somanassa* e *domanassa*?", "Sensação mental agradável, alegria (somanassa) e sensação mental desagradável, desagrado (domanassa)."),
  ("What are *somanassa* and *domanassa*?", "Pleasant mental feeling, joy (somanassa) and unpleasant mental feeling, displeasure (domanassa)."),
  ("¿Qué son *somanassa* y *domanassa*?", "Sensación mental agradable, alegría (somanassa) y sensación mental desagradable, desagrado (domanassa)."),
  enrichment={
    "pt": {"breakdown": ["Somanassa = alegria mental, felicidade (base = mente)", "Domanassa = desagrado mental, desgosto (base = mente)", "Domanassa associado SOMENTE com dosa-mūla-cittas (2 cittas)", "Somanassa pode surgir em cittas kusala, akusala (lobha) e vipāka"], "explanation": "Somanassa e domanassa são vedanās mentais — baseadas na mente (mano), não no corpo. Domanassa é a vedanā mais restrita: surge exclusivamente nos 2 dosa-mūla-cittas. Somanassa é mais versátil: acompanha lobha-mūla, muitos kusala e vipāka sobhana.", "mnemonic": "Domanassa = exclusivo de dosa (ódio). Somanassa = 'sentir-se bem' mentalmente. Pegadinha: domanassa NUNCA surge com kusala."},
    "en": {"breakdown": ["Somanassa = mental joy, happiness (base = mind)", "Domanassa = mental displeasure, grief (base = mind)", "Domanassa associated ONLY with dosa-mūla-cittas (2 cittas)", "Somanassa can arise in kusala, akusala (lobha) and vipāka cittas"], "explanation": "Somanassa and domanassa are mental feelings — based in the mind (mano), not the body. Domanassa is the most restricted vedanā: it arises exclusively in the 2 dosa-mūla-cittas. Somanassa is more versatile: it accompanies lobha-mūla, many kusala and sobhana vipāka.", "mnemonic": "Domanassa = exclusive to dosa (hatred). Somanassa = 'feeling good' mentally. Exam trap: domanassa NEVER arises with kusala."},
    "es": {"breakdown": ["Somanassa = alegría mental, felicidad (base = mente)", "Domanassa = disgusto mental, tristeza (base = mente)", "Domanassa asociado SOLO con dosa-mūla-cittas (2 cittas)", "Somanassa puede surgir en cittas kusala, akusala (lobha) y vipāka"], "explanation": "Somanassa y domanassa son vedanās mentales — basadas en la mente (mano), no en el cuerpo. Domanassa es la vedanā más restringida: surge exclusivamente en los 2 dosa-mūla-cittas. Somanassa es más versátil: acompaña a lobha-mūla, muchos kusala y vipāka sobhana.", "mnemonic": "Domanassa = exclusivo de dosa (odio). Somanassa = 'sentirse bien' mentalmente. Trampa: domanassa NUNCA surge con kusala."}
  })
AT("at-v04", 1, "philosophy", V, "Upekkhā", ["at-v01"], ["vedana"],
  ("O que é *upekkhā* como vedanā?", "Sensação neutra: nem agradável nem desagradável."),
  ("What is *upekkhā* as vedanā?", "Neutral feeling: neither pleasant nor unpleasant."),
  ("¿Qué es *upekkhā* como vedanā?", "Sensación neutra: ni agradable ni desagradable."),
  enrichment={
    "pt": {"breakdown": ["Upekkhā vedanā = tonalidade afetiva neutra (adukkhamasukha)", "É a vedanā mais frequente — acompanha a maioria dos cittas", "Presente em: 55 dos 89 cittas mundanos + cittas lokuttara", "Distinta da upekkhā como brahmavihāra (equanimidade = cetasika tatramajjhattatā)"], "explanation": "Upekkhā como vedanā é simplesmente a ausência de tonalidade agradável ou desagradável — não é indiferença, mas neutralidade afetiva. É a tonalidade padrão: a maioria dos cittas ahetuka e muitos kusala operam com upekkhā-vedanā. Atenção: 'upekkhā' tem múltiplos significados no cânone.", "mnemonic": "Upekkhā vedanā = neutro (55+ cittas). NÃO confundir com upekkhā brahmavihāra (equanimidade moral). A vedanā é uma das 5; a brahmavihāra é um cetasika sobhana separado."},
    "en": {"breakdown": ["Upekkhā vedanā = neutral affective tone (adukkhamasukha)", "Most frequent vedanā — accompanies the majority of cittas", "Present in: 55 of the 89 mundane cittas + lokuttara cittas", "Distinct from upekkhā as brahmavihāra (equanimity = cetasika tatramajjhattatā)"], "explanation": "Upekkhā as vedanā is simply the absence of pleasant or unpleasant tone — not indifference, but affective neutrality. It is the default tone: most ahetuka cittas and many kusala operate with upekkhā-vedanā. Note: 'upekkhā' has multiple meanings in the canon.", "mnemonic": "Upekkhā vedanā = neutral (55+ cittas). Do NOT confuse with upekkhā brahmavihāra (moral equanimity). The vedanā is one of 5; the brahmavihāra is a separate sobhana cetasika."},
    "es": {"breakdown": ["Upekkhā vedanā = tonalidad afectiva neutra (adukkhamasukha)", "La vedanā más frecuente — acompaña a la mayoría de los cittas", "Presente en: 55 de los 89 cittas mundanos + cittas lokuttara", "Distinta de la upekkhā como brahmavihāra (ecuanimidad = cetasika tatramajjhattatā)"], "explanation": "La upekkhā como vedanā es simplemente la ausencia de tonalidad agradable o desagradable — no es indiferencia, sino neutralidad afectiva. Es la tonalidad predeterminada: la mayoría de los cittas ahetuka y muchos kusala operan con upekkhā-vedanā. Nota: 'upekkhā' tiene múltiples significados en el canon.", "mnemonic": "Upekkhā vedanā = neutra (55+ cittas). NO confundir con upekkhā brahmavihāra (ecuanimidad moral). La vedanā es una de las 5; la brahmavihāra es un cetasika sobhana separado."}
  })
AT("at-j01", 1, "quantities", J, "Catasso Jāti", ["at-t02"], ["jati"],
  ("Quais são as 4 jāti (naturezas) dos cittas?", "Kusala, akusala, vipāka e kiriya."),
  ("What are the 4 jāti (natures) of cittas?", "Kusala, akusala, vipāka and kiriya."),
  ("¿Cuáles son las 4 jāti (naturalezas) de los cittas?", "Kusala, akusala, vipāka y kiriya."),
  enrichment={
    "pt": {"breakdown": ["Kusala: saudável — produz resultado agradável (kamma)", "Akusala: não-saudável — produz resultado desagradável (kamma)", "Vipāka: resultado — maturação de kamma passado, não produz novo kamma", "Kiriya: funcional — nem kamma nem resultado; apenas função"], "explanation": "As 4 jāti classificam cada citta por sua natureza moral e kármica. Todo citta tem exatamente uma jāti. Esta classificação é fundamental: kusala e akusala constroem o samsāra; vipāka é o fruto colhido; kiriya pertence somente a Arahants e Budas para atos mundanos.", "mnemonic": "4 jāti: K-A-V-K (Kusala, Akusala, Vipāka, Kiriya). Kamma = kusala+akusala. Vipāka = fruto. Kiriya = ato sem consequência kármica."},
    "en": {"breakdown": ["Kusala: wholesome — produces pleasant result (kamma)", "Akusala: unwholesome — produces unpleasant result (kamma)", "Vipāka: result — ripening of past kamma, produces no new kamma", "Kiriya: functional — neither kamma nor result; merely function"], "explanation": "The 4 jāti classify each citta by its moral and karmic nature. Every citta has exactly one jāti. This classification is fundamental: kusala and akusala build samsāra; vipāka is the fruit reaped; kiriya belongs only to Arahants and Buddhas for mundane acts.", "mnemonic": "4 jāti: K-A-V-K (Kusala, Akusala, Vipāka, Kiriya). Kamma = kusala+akusala. Vipāka = fruit. Kiriya = act with no karmic consequence."},
    "es": {"breakdown": ["Kusala: saludable — produce resultado agradable (kamma)", "Akusala: no saludable — produce resultado desagradable (kamma)", "Vipāka: resultado — maduración de kamma pasado, no produce nuevo kamma", "Kiriya: funcional — ni kamma ni resultado; solo función"], "explanation": "Las 4 jāti clasifican cada citta por su naturaleza moral y kármica. Todo citta tiene exactamente una jāti. Esta clasificación es fundamental: kusala y akusala construyen el samsāra; vipāka es el fruto cosechado; kiriya pertenece solo a Arahants y Budas para actos mundanos.", "mnemonic": "4 jāti: K-A-V-K (Kusala, Akusala, Vipāka, Kiriya). Kamma = kusala+akusala. Vipāka = fruto. Kiriya = acto sin consecuencia kármica."}
  })
AT("at-j02", 1, "philosophy", J, "Kusala / Akusala", ["at-j01"], ["jati"],
  ("O que são citta *kusala* e *akusala*?", "Kusala: saudável, kamma que dá resultado agradável. Akusala: não-saudável, kamma que dá resultado desagradável."),
  ("What are *kusala* and *akusala* cittas?", "Kusala: wholesome, kamma that gives pleasant results. Akusala: unwholesome, kamma that gives unpleasant results."),
  ("¿Qué son los cittas *kusala* y *akusala*?", "Kusala: saludable, kamma que da resultado agradable. Akusala: no saludable, kamma que da resultado desagradable."),
  enrichment={
    "pt": {"breakdown": ["Kusala (de 'kusa', erva auspiciosa): hábil, saudável, benéfico", "Akusala (a- + kusala): não-saudável, prejudicial, baseado em raízes akusala", "Kusala produz vipāka agradável (sukha, somanassa); akusala produz vipāka desagradável", "12 akusala cittas vs. 24 kāmāvacara-kusala-cittas (+ mahaggata + lokuttara)"], "explanation": "Kusala e akusala definem a qualidade moral de um ato de consciência. O Abhidhamma é preciso: kusala não é apenas 'bom por convenção', mas um citta que tem raiz em alobha, adosa e/ou amoha. Akusala tem raiz em lobha, dosa e/ou moha.", "mnemonic": "Kusala = raízes belas (alobha, adosa, amoha). Akusala = raízes não-saudáveis (lobha, dosa, moha). Moha está em TODO akusala."},
    "en": {"breakdown": ["Kusala (from 'kusa', auspicious grass): skillful, wholesome, beneficial", "Akusala (a- + kusala): unwholesome, harmful, rooted in akusala roots", "Kusala produces pleasant vipāka (sukha, somanassa); akusala produces unpleasant vipāka", "12 akusala cittas vs. 24 kāmāvacara-kusala-cittas (+ mahaggata + lokuttara)"], "explanation": "Kusala and akusala define the moral quality of a conscious act. The Abhidhamma is precise: kusala is not just 'conventionally good' but a citta rooted in alobha, adosa and/or amoha. Akusala is rooted in lobha, dosa and/or moha.", "mnemonic": "Kusala = beautiful roots (alobha, adosa, amoha). Akusala = unwholesome roots (lobha, dosa, moha). Moha is in EVERY akusala."},
    "es": {"breakdown": ["Kusala (de 'kusa', hierba auspiciosa): hábil, saludable, beneficioso", "Akusala (a- + kusala): no saludable, dañino, enraizado en raíces akusala", "Kusala produce vipāka agradable (sukha, somanassa); akusala produce vipāka desagradable", "12 akusala cittas vs. 24 kāmāvacara-kusala-cittas (+ mahaggata + lokuttara)"], "explanation": "Kusala y akusala definen la calidad moral de un acto de conciencia. El Abhidhamma es preciso: kusala no es solo 'convencionalmente bueno', sino un citta enraizado en alobha, adosa y/o amoha. Akusala está enraizado en lobha, dosa y/o moha.", "mnemonic": "Kusala = raíces bellas (alobha, adosa, amoha). Akusala = raíces no saludables (lobha, dosa, moha). Moha está en TODO akusala."}
  })
AT("at-j03", 1, "philosophy", J, "Vipāka", ["at-j01", "at-j02"], ["jati", "vipaka"],
  ("O que é um citta *vipāka*?", "O resultado (maturação) de kamma kusala ou akusala passado; não produz novo kamma."),
  ("What is a *vipāka* citta?", "The result (ripening) of past kusala or akusala kamma; it does not produce new kamma."),
  ("¿Qué es un citta *vipāka*?", "El resultado (maduración) de kamma kusala o akusala pasado; no produce nuevo kamma."),
  enrichment={
    "pt": {"breakdown": ["Vipāka = maturação de kamma; não é um novo ato de vontade (cetanā)", "Kusala-kamma → kusala-vipāka; akusala-kamma → akusala-vipāka", "Vipāka cittas: 36 (kāmāvacara: 23, rūpāvacara: 5, arūpāvacara: 4, lokuttara: 4)", "Na vida cotidiana: as 5 consciências sensoriais (pañca-viññāṇa) são vipāka"], "explanation": "Vipāka é o princípio de que todo kamma tem consequências. A consciência do resultado não tem potencial de gerar novo kamma — é passiva, como a maçã que cai, não a que a empurra. Os cittas vipāka predominam nos processos mentais do dia a dia (processos dos 5 sentidos).", "mnemonic": "Vipāka = fruto colhido, não semeado agora. Passivo: sem nova cetanā geradora de kamma. Ex. diário: ver, ouvir, cheirar, saborear, tocar = vipāka."},
    "en": {"breakdown": ["Vipāka = ripening of kamma; not a new volitional act (cetanā)", "Kusala-kamma → kusala-vipāka; akusala-kamma → akusala-vipāka", "Vipāka cittas: 36 (kāmāvacara: 23, rūpāvacara: 5, arūpāvacara: 4, lokuttara: 4)", "In daily life: the 5 sense-consciousnesses (pañca-viññāṇa) are vipāka"], "explanation": "Vipāka is the principle that all kamma has consequences. Result-consciousness has no potential to generate new kamma — it is passive, like the fallen apple, not the one that pushed it. Vipāka cittas predominate in everyday mental processes (five-sense processes).", "mnemonic": "Vipāka = fruit harvested, not sown now. Passive: no new kamma-generating cetanā. Daily example: seeing, hearing, smelling, tasting, touching = vipāka."},
    "es": {"breakdown": ["Vipāka = maduración de kamma; no es un nuevo acto volitivo (cetanā)", "Kusala-kamma → kusala-vipāka; akusala-kamma → akusala-vipāka", "Cittas vipāka: 36 (kāmāvacara: 23, rūpāvacara: 5, arūpāvacara: 4, lokuttara: 4)", "En la vida diaria: las 5 conciencias sensoriales (pañca-viññāṇa) son vipāka"], "explanation": "Vipāka es el principio de que todo kamma tiene consecuencias. La conciencia del resultado no tiene potencial para generar nuevo kamma — es pasiva, como la manzana que cae, no la que la empujó. Los cittas vipāka predominan en los procesos mentales cotidianos (procesos de los 5 sentidos).", "mnemonic": "Vipāka = fruto cosechado, no sembrado ahora. Pasivo: sin nueva cetanā generadora de kamma. Ejemplo diario: ver, oír, oler, gustar, tocar = vipāka."}
  })
AT("at-j04", 1, "philosophy", J, "Kiriya", ["at-j01"], ["jati", "kiriya"],
  ("O que é um citta *kiriya*?", "Funcional: não é kamma nem resultado de kamma; apenas exerce uma função (ex.: atenção, sorriso do Arahant)."),
  ("What is a *kiriya* citta?", "Functional: neither kamma nor the result of kamma; it merely performs a function (e.g. adverting, the Arahant's smile)."),
  ("¿Qué es un citta *kiriya*?", "Funcional: ni kamma ni resultado de kamma; solo ejerce una función (p. ej. atención, sonrisa del Arahant)."),
  enrichment={
    "pt": {"breakdown": ["Kiriya = 'ação pura' sem consequência kármica", "2 categorias: (1) ahetuka kiriya (3) — funções básicas de todos os seres; (2) sobhana kiriya (20) — apenas Arahants/Budas", "Ahetuka kiriya: manodvārāvajjana, hasituppāda, pañcadvārāvajjana", "Sobhana kiriya: equivalente funcional dos cittas kusala mahaggata e lokuttara do Arahant"], "explanation": "Kiriya é a jāti dos cittas que operam sem criar nem receber kamma. Na vida cotidiana, alguns processos funcionais (como o 'advertir') são kiriya para todos. Para o Arahant, os cittas que seriam kusala em um não-Arahant tornam-se kiriya — eles agem sem semear futuros resultados.", "mnemonic": "Kiriya = ação sem kamma. Arahant age com kiriya onde comum usa kusala. Hasituppāda (sorriso do Buda) = kiriya. 20 sobhana kiriya = apenas Arahants/Budas."},
    "en": {"breakdown": ["Kiriya = 'pure action' without karmic consequence", "2 categories: (1) ahetuka kiriya (3) — basic functions of all beings; (2) sobhana kiriya (20) — Arahants/Buddhas only", "Ahetuka kiriya: manodvārāvajjana, hasituppāda, pañcadvārāvajjana", "Sobhana kiriya: functional equivalent of the Arahant's mahaggata and lokuttara kusala cittas"], "explanation": "Kiriya is the jāti of cittas that operate without creating or receiving kamma. In daily life, some functional processes (like 'adverting') are kiriya for all. For the Arahant, cittas that would be kusala in a non-Arahant become kiriya — they act without sowing future results.", "mnemonic": "Kiriya = action without kamma. Arahant acts with kiriya where ordinary beings use kusala. Hasituppāda (Buddha's smile) = kiriya. 20 sobhana kiriya = Arahants/Buddhas only."},
    "es": {"breakdown": ["Kiriya = 'acción pura' sin consecuencia kármica", "2 categorías: (1) ahetuka kiriya (3) — funciones básicas de todos los seres; (2) sobhana kiriya (20) — solo Arahants/Budas", "Ahetuka kiriya: manodvārāvajjana, hasituppāda, pañcadvārāvajjana", "Sobhana kiriya: equivalente funcional de los cittas kusala mahaggata y lokuttara del Arahant"], "explanation": "Kiriya es la jāti de los cittas que operan sin crear ni recibir kamma. En la vida cotidiana, algunos procesos funcionales (como 'advertir') son kiriya para todos. Para el Arahant, los cittas que serían kusala en un no-Arahant se convierten en kiriya — actúan sin sembrar resultados futuros.", "mnemonic": "Kiriya = acción sin kamma. El Arahant actúa con kiriya donde los seres ordinarios usan kusala. Hasituppāda (sonrisa del Buda) = kiriya. 20 sobhana kiriya = solo Arahants/Budas."}
  })
AT("at-p01", 1, "quantities", B, "Catasso Bhūmi", ["at-t02"], ["bhumi"],
  ("Quais são as 4 esferas (bhūmi) de consciência?", "Kāmāvacara, rūpāvacara, arūpāvacara e lokuttara."),
  ("What are the 4 spheres (bhūmi) of consciousness?", "Kāmāvacara, rūpāvacara, arūpāvacara and lokuttara."),
  ("¿Cuáles son las 4 esferas (bhūmi) de conciencia?", "Kāmāvacara, rūpāvacara, arūpāvacara y lokuttara."),
  enrichment={
    "pt": {"breakdown": ["Kāmāvacara: 54 cittas — esfera do desejo sensorial", "Rūpāvacara: 15 cittas — esfera da forma sutil (jhāna 1-4 ou 1-5)", "Arūpāvacara: 12 cittas — esfera sem forma (jhāna 5-8)", "Lokuttara: 8 ou 40 cittas — supramundanos, objeto = Nibbāna", "Total mundano: 81 (54+15+12); total com lokuttara: 89 ou 121"], "explanation": "Bhūmi classifica cada citta por sua 'terra' ou domínio de operação. Os 3 primeiros são mundanos (lokiya): operam no samsāra. Apenas lokuttara transcende. A diferença entre 89 e 121 cittas vem dos lokuttara: 8 básicos × 5 jhāna-associações = 40.", "mnemonic": "4 bhūmi = KĀ-RŪ-ARŪ-LO. Números: 54+15+12+8(ou 40) = 89 ou 121. Dica: lokuttara = somente Nibbāna como objeto."},
    "en": {"breakdown": ["Kāmāvacara: 54 cittas — sense-desire sphere", "Rūpāvacara: 15 cittas — fine-material sphere (jhāna 1-4 or 1-5)", "Arūpāvacara: 12 cittas — immaterial sphere (jhāna 5-8)", "Lokuttara: 8 or 40 cittas — supramundane, object = Nibbāna", "Mundane total: 81 (54+15+12); with lokuttara: 89 or 121"], "explanation": "Bhūmi classifies each citta by its 'ground' or domain of operation. The first 3 are mundane (lokiya): they operate within samsāra. Only lokuttara transcends. The difference between 89 and 121 cittas comes from the lokuttara: 8 basic × 5 jhāna-associations = 40.", "mnemonic": "4 bhūmi = KĀ-RŪ-ARŪ-LO. Numbers: 54+15+12+8(or 40) = 89 or 121. Tip: lokuttara = only Nibbāna as object."},
    "es": {"breakdown": ["Kāmāvacara: 54 cittas — esfera del deseo sensorial", "Rūpāvacara: 15 cittas — esfera de la forma sutil (jhāna 1-4 o 1-5)", "Arūpāvacara: 12 cittas — esfera inmaterial (jhāna 5-8)", "Lokuttara: 8 o 40 cittas — supramundanos, objeto = Nibbāna", "Total mundano: 81 (54+15+12); con lokuttara: 89 o 121"], "explanation": "Bhūmi clasifica cada citta por su 'tierra' o dominio de operación. Los 3 primeros son mundanos (lokiya): operan dentro del samsāra. Solo el lokuttara trasciende. La diferencia entre 89 y 121 cittas proviene de los lokuttara: 8 básicos × 5 asociaciones-jhāna = 40.", "mnemonic": "4 bhūmi = KĀ-RŪ-ARŪ-LO. Números: 54+15+12+8(o 40) = 89 o 121. Pista: lokuttara = solo Nibbāna como objeto."}
  })
AT("at-p02", 1, "philosophy", B, "Kāmāvacara", ["at-p01"], ["bhumi"],
  ("O que são os cittas *kāmāvacara*?", "Cittas da esfera dos sentidos (kāma): operam sobretudo no plano do desejo sensorial."),
  ("What are *kāmāvacara* cittas?", "Cittas of the sense sphere (kāma): they operate mainly in the plane of sensual desire."),
  ("¿Qué son los cittas *kāmāvacara*?", "Cittas de la esfera sensorial (kāma): operan sobre todo en el plano del deseo sensorial."),
  enrichment={
    "pt": {"breakdown": ["54 cittas kāmāvacara: 12 akusala + 18 ahetuka + 24 sobhana", "24 sobhana: 8 kusala + 8 vipāka + 8 kiriya", "São os cittas mais comuns — operam em todos os seres dos 11 planos kāma (4 apāya + 7 sugati)", "Os 18 ahetuka incluem os 10 dvipañcaviññāṇa + 2 sampaṭicchana + 3 santīraṇa + 2 pañcadvārāvajjana + 1 manodvārāvajjana + 1 hasituppāda"], "explanation": "Os 54 cittas kāmāvacara são o conjunto mais fundamental — operam desde animais e seres infernais até devas dos céus Cātumaharājika. Qualquer ser sensiente não em jhāna usa apenas esses cittas. São a base de todo o sistema Abhidhamma.", "mnemonic": "54 kāmāvacara = 12+18+24. Mnêmico: 12 'ruins' + 18 'neutros' + 24 'bons'. Todo ser não-jhāna usa apenas esses 54."},
    "en": {"breakdown": ["54 kāmāvacara cittas: 12 akusala + 18 ahetuka + 24 sobhana", "24 sobhana: 8 kusala + 8 vipāka + 8 kiriya", "Most common cittas — operate in all beings of the 11 kāma planes (4 apāya + 7 sugati)", "The 18 ahetuka include the 10 dvipañcaviññāṇa + 2 sampaṭicchana + 3 santīraṇa + 2 pañcadvārāvajjana + 1 manodvārāvajjana + 1 hasituppāda"], "explanation": "The 54 kāmāvacara cittas are the most fundamental set — they operate from animals and hell-beings up to the Cātumaharājika devas. Any sentient being not in jhāna uses only these cittas. They are the foundation of the entire Abhidhamma system.", "mnemonic": "54 kāmāvacara = 12+18+24. Mnemonic: 12 'bad' + 18 'neutral' + 24 'good'. Every non-jhāna being uses only these 54."},
    "es": {"breakdown": ["54 cittas kāmāvacara: 12 akusala + 18 ahetuka + 24 sobhana", "24 sobhana: 8 kusala + 8 vipāka + 8 kiriya", "Los cittas más comunes — operan en todos los seres de los 11 planos kāma (4 apāya + 7 sugati)", "Los 18 ahetuka incluyen los 10 dvipañcaviññāṇa + 2 sampaṭicchana + 3 santīraṇa + 2 pañcadvārāvajjana + 1 manodvārāvajjana + 1 hasituppāda"], "explanation": "Los 54 cittas kāmāvacara son el conjunto más fundamental — operan desde animales y seres del infierno hasta los devas de los Cātumaharājika. Cualquier ser sintiente que no esté en jhāna usa solo estos cittas. Son la base de todo el sistema Abhidhamma.", "mnemonic": "54 kāmāvacara = 12+18+24. Mnemónico: 12 'malos' + 18 'neutros' + 24 'buenos'. Todo ser no-jhāna usa solo estos 54."}
  })
AT("at-p03", 1, "philosophy", B, "Rūpāvacara", ["at-p01"], ["bhumi"],
  ("O que são os cittas *rūpāvacara*?", "Cittas da esfera da forma sutil: os jhānas de forma (rūpa-jhāna)."),
  ("What are *rūpāvacara* cittas?", "Cittas of the fine-material sphere: the form jhānas (rūpa-jhāna)."),
  ("¿Qué son los cittas *rūpāvacara*?", "Cittas de la esfera de la forma sutil: los jhānas de forma (rūpa-jhāna)."),
  enrichment={
    "pt": {"breakdown": ["15 cittas rūpāvacara = 5 kusala + 5 vipāka + 5 kiriya", "Correspondem aos 5 jhānas de forma (pañcaka-naya): vitarka, vicāra, pīti, sukha, ekaggatā", "Surgem mediante o desenvolvimento da meditação samatha com kasiṇa ou outros objetos adequados", "Renascem nos 16 planos rūpa-brahma (exceto Asaññasatta)"], "explanation": "Os cittas rūpāvacara emergem quando a mente entra em jhāna de forma — um estado de profunda concentração que vai além dos sentidos mas ainda tem suporte na forma. Cada jhāna é definido pela presença/ausência dos 5 fatores (aṅga). No sistema fivefold, são 5 jhānas progressivamente depurados.", "mnemonic": "15 rūpāvacara = 5×3 (kusala/vipāka/kiriya). 5 jhānas de forma. Fatores: vitarka → vicāra → pīti → sukha → ekaggatā. Cada jhāna abandona um fator."},
    "en": {"breakdown": ["15 rūpāvacara cittas = 5 kusala + 5 vipāka + 5 kiriya", "Correspond to the 5 form jhānas (pañcaka-naya): vitarka, vicāra, pīti, sukha, ekaggatā", "Arise through samatha meditation development with kasiṇa or other suitable objects", "Rebirth in the 16 rūpa-brahma planes (except Asaññasatta)"], "explanation": "Rūpāvacara cittas emerge when the mind enters form jhāna — a state of deep concentration that transcends the senses but still has form as support. Each jhāna is defined by the presence/absence of the 5 factors (aṅga). In the fivefold system, there are 5 progressively refined jhānas.", "mnemonic": "15 rūpāvacara = 5×3 (kusala/vipāka/kiriya). 5 form jhānas. Factors: vitarka → vicāra → pīti → sukha → ekaggatā. Each jhāna abandons one factor."},
    "es": {"breakdown": ["15 cittas rūpāvacara = 5 kusala + 5 vipāka + 5 kiriya", "Corresponden a los 5 jhānas de forma (pañcaka-naya): vitarka, vicāra, pīti, sukha, ekaggatā", "Surgen mediante el desarrollo de meditación samatha con kasiṇa u otros objetos adecuados", "Renacimiento en los 16 planos rūpa-brahma (excepto Asaññasatta)"], "explanation": "Los cittas rūpāvacara emergen cuando la mente entra en jhāna de forma — un estado de profunda concentración que trasciende los sentidos pero aún tiene soporte en la forma. Cada jhāna se define por la presencia/ausencia de los 5 factores (aṅga). En el sistema quíntuple, hay 5 jhānas progresivamente purificados.", "mnemonic": "15 rūpāvacara = 5×3 (kusala/vipāka/kiriya). 5 jhānas de forma. Factores: vitarka → vicāra → pīti → sukha → ekaggatā. Cada jhāna abandona un factor."}
  })
AT("at-p04", 1, "philosophy", B, "Arūpāvacara", ["at-p01"], ["bhumi"],
  ("O que são os cittas *arūpāvacara*?", "Cittas da esfera sem forma: os jhānas imateriais (arūpa-jhāna)."),
  ("What are *arūpāvacara* cittas?", "Cittas of the immaterial sphere: the formless jhānas (arūpa-jhāna)."),
  ("¿Qué son los cittas *arūpāvacara*?", "Cittas de la esfera inmaterial: los jhānas inmateriales (arūpa-jhāna)."),
  enrichment={
    "pt": {"breakdown": ["12 cittas arūpāvacara = 4 kusala + 4 vipāka + 4 kiriya", "4 arūpa-jhānas: (1) ākāsānañcāyatana, (2) viññāṇañcāyatana, (3) ākiñcaññāyatana, (4) nevasaññānāsaññāyatana", "Base para renascer nos 4 planos arūpa-brahma (os mais elevados do samsāra)", "Não há rūpa nesses seres — somente nāma (mente)"], "explanation": "Os arūpa-jhānas são a meditação imaterial mais profunda — a mente transcende completamente o domínio da forma. Os 4 estados progridem do 'espaço infinito' até a fronteira do ser-e-não-ser. São os estados mais elevados do samsāra, mas ainda condicionados.", "mnemonic": "12 arūpāvacara = 4×3. 4 jhānas imateriais: ESPAÇO → CONSCIÊNCIA → NADA → NEM-SER-NEM-NÃO-SER. Ainda samsāra — mais refinados, não liberados."},
    "en": {"breakdown": ["12 arūpāvacara cittas = 4 kusala + 4 vipāka + 4 kiriya", "4 arūpa-jhānas: (1) ākāsānañcāyatana, (2) viññāṇañcāyatana, (3) ākiñcaññāyatana, (4) nevasaññānāsaññāyatana", "Basis for rebirth in the 4 arūpa-brahma planes (the highest in samsāra)", "No rūpa in these beings — only nāma (mind)"], "explanation": "The arūpa-jhānas are the deepest immaterial meditation — the mind completely transcends the domain of form. The 4 states progress from 'infinite space' to the boundary of being-and-non-being. They are the highest states of samsāra, but still conditioned.", "mnemonic": "12 arūpāvacara = 4×3. 4 immaterial jhānas: SPACE → CONSCIOUSNESS → NOTHINGNESS → NEITHER-BEING-NOR-NON-BEING. Still samsāra — more refined, not liberated."},
    "es": {"breakdown": ["12 cittas arūpāvacara = 4 kusala + 4 vipāka + 4 kiriya", "4 arūpa-jhānas: (1) ākāsānañcāyatana, (2) viññāṇañcāyatana, (3) ākiñcaññāyatana, (4) nevasaññānāsaññāyatana", "Base para renacer en los 4 planos arūpa-brahma (los más elevados del samsāra)", "No hay rūpa en estos seres — solo nāma (mente)"], "explanation": "Los arūpa-jhānas son la meditación inmaterial más profunda — la mente trasciende completamente el dominio de la forma. Los 4 estados progresan desde el 'espacio infinito' hasta la frontera del ser-y-no-ser. Son los estados más elevados del samsāra, pero aún condicionados.", "mnemonic": "12 arūpāvacara = 4×3. 4 jhānas inmateriales: ESPACIO → CONSCIENCIA → NADA → NI-SER-NI-NO-SER. Aún samsāra — más refinados, no liberados."}
  })
AT("at-p05", 1, "philosophy", B, "Lokuttara", ["at-p01"], ["bhumi"],
  ("O que são os cittas *lokuttara*?", "Supramundanos: transcendem o mundo e têm Nibbāna como objeto."),
  ("What are *lokuttara* cittas?", "Supramundane: they transcend the world and take Nibbāna as object."),
  ("¿Qué son los cittas *lokuttara*?", "Supramundanos: trascienden el mundo y tienen Nibbāna como objeto."),
  enrichment={
    "pt": {"breakdown": ["8 cittas básicos (ou 40 com associação de jhāna): 4 magga + 4 phala", "4 pares magga-phala: sotāpatti, sakadāgāmi, anāgāmi, arahatta", "Magga-citta: ÚNICO momento de citta que erradica um nível de defilements (kilesa)", "Phala-citta: resultado imediato do magga, surge logo depois, tem Nibbāna como objeto", "Não acumulam kamma — não produzem resultado futuro no samsāra"], "explanation": "Os cittas lokuttara são os únicos que saem do circuito do samsāra. O magga-citta 'corta' (chinati) as defilements correspondentes ao seu estágio. O phala-citta é o seu fruto imediato. Nos 40 (sistema expandido), cada estágio é associado com os 5 jhānas — o resultado é o mesmo, mas o sabor experiencial varia.", "mnemonic": "8 lokuttara = 4 magga + 4 phala. Nikāyas dos estágios: Sotāpanna → Sakadāgāmi → Anāgāmi → Arahant. Magga ERRADICA; Phala FRUI. Nibbāna = único objeto."},
    "en": {"breakdown": ["8 basic cittas (or 40 with jhāna association): 4 magga + 4 phala", "4 magga-phala pairs: sotāpatti, sakadāgāmi, anāgāmi, arahatta", "Magga-citta: the ONLY citta-moment that eradicates a level of defilements (kilesa)", "Phala-citta: immediate result of magga, arises right after, has Nibbāna as object", "Do not accumulate kamma — produce no future result in samsāra"], "explanation": "Lokuttara cittas are the only ones that exit the samsāra circuit. The magga-citta 'cuts' (chinati) the defilements corresponding to its stage. The phala-citta is its immediate fruit. In the 40 (expanded system), each stage is associated with the 5 jhānas — the result is the same but the experiential quality varies.", "mnemonic": "8 lokuttara = 4 magga + 4 phala. Path-stages: Sotāpanna → Sakadāgāmi → Anāgāmi → Arahant. Magga ERADICATES; Phala ENJOYS. Nibbāna = only object."},
    "es": {"breakdown": ["8 cittas básicos (o 40 con asociación de jhāna): 4 magga + 4 phala", "4 pares magga-phala: sotāpatti, sakadāgāmi, anāgāmi, arahatta", "Magga-citta: el ÚNICO momento de citta que erradica un nivel de corrupciones (kilesa)", "Phala-citta: resultado inmediato del magga, surge justo después, tiene Nibbāna como objeto", "No acumulan kamma — no producen resultado futuro en el samsāra"], "explanation": "Los cittas lokuttara son los únicos que salen del circuito del samsāra. El magga-citta 'corta' (chinati) las corrupciones correspondientes a su etapa. El phala-citta es su fruto inmediato. En los 40 (sistema expandido), cada etapa se asocia con los 5 jhānas — el resultado es el mismo, pero la calidad experiencial varía.", "mnemonic": "8 lokuttara = 4 magga + 4 phala. Etapas: Sotāpanna → Sakadāgāmi → Anāgāmi → Arahant. Magga ERRADICA; Phala GOZA. Nibbāna = único objeto."}
  })

H = "Hetusaṅgaha"
# ── Hetu ────────────────────────────────────────────────────────────────────
add("at-h01", 3, "philosophy", H, "Hetu / Mūla", 1, ["at-t03"], ["hetu", "mula"],
    ("O que é *hetu* (*mūla*, raiz) no Abhidhamma?",
     "Fator mental (*cetasika*) que atua como raiz: dá firmeza e estabilidade ao citta e aos cetasikas associados, como as raízes de uma árvore."),
    ("What is *hetu* (*mūla*, root) in the Abhidhamma?",
     "A mental factor (*cetasika*) acting as a root: it gives firmness and stability to the citta and its associated cetasikas, like the roots of a tree."),
    ("¿Qué es *hetu* (*mūla*, raíz) en el Abhidhamma?",
     "Factor mental (*cetasika*) que actúa como raíz: da firmeza y estabilidad al citta y a los cetasikas asociados, como las raíces de un árbol."),
    enrichment={
      "pt": {"breakdown": ["Hetu (raiz) = cetasika que 'ancora' o citta, como raízes de uma árvore", "6 hetus: 3 akusala (lobha, dosa, moha) + 3 sobhana/kusala (alobha, adosa, amoha)", "Classificam os cittas como: sahetuka (com raiz) ou ahetuka (sem raiz)", "Número de raízes por citta: 1, 2 ou 3"], "explanation": "No Abhidhamma, 'hetu' no sentido de 'raiz moral' é diferente de 'hetu' no Paṭṭhāna (como uma das 24 condições). Aqui, hetu = mūla: as 6 raízes que determinam a qualidade moral e o potencial da consciência. Um citta com mais raízes tem mais potencial resultante.", "mnemonic": "6 hetus = 3 ruins + 3 bons. Cittas ahetuka = sem nenhuma raiz. Sahetuka = 1-3 raízes. Pegadinha: 'hetu' tem dois sentidos no Abhidhamma!"},
      "en": {"breakdown": ["Hetu (root) = cetasika that 'anchors' the citta, like a tree's roots", "6 hetus: 3 akusala (lobha, dosa, moha) + 3 sobhana/kusala (alobha, adosa, amoha)", "Classify cittas as: sahetuka (with root) or ahetuka (rootless)", "Number of roots per citta: 1, 2 or 3"], "explanation": "In the Abhidhamma, 'hetu' meaning 'moral root' is different from 'hetu' in the Paṭṭhāna (as one of 24 conditions). Here, hetu = mūla: the 6 roots that determine the moral quality and potential of consciousness. A citta with more roots has greater resultant potential.", "mnemonic": "6 hetus = 3 bad + 3 good. Ahetuka cittas = no root at all. Sahetuka = 1-3 roots. Exam trap: 'hetu' has two meanings in the Abhidhamma!"},
      "es": {"breakdown": ["Hetu (raíz) = cetasika que 'ancla' el citta, como las raíces de un árbol", "6 hetus: 3 akusala (lobha, dosa, moha) + 3 sobhana/kusala (alobha, adosa, amoha)", "Clasifican los cittas como: sahetuka (con raíz) o ahetuka (sin raíz)", "Número de raíces por citta: 1, 2 o 3"], "explanation": "En el Abhidhamma, 'hetu' en el sentido de 'raíz moral' es diferente de 'hetu' en el Paṭṭhāna (como una de las 24 condiciones). Aquí, hetu = mūla: las 6 raíces que determinan la calidad moral y el potencial de la conciencia. Un citta con más raíces tiene mayor potencial resultante.", "mnemonic": "6 hetus = 3 malos + 3 buenos. Cittas ahetuka = sin ninguna raíz. Sahetuka = 1-3 raíces. Trampa: ¡'hetu' tiene dos significados en el Abhidhamma!"}
    })
add("at-h02", 3, "quantities", H, "Cha Hetū", 1, ["at-h01"], ["hetu"],
    ("Quantos hetus existem no total?", "Seis: 3 não-saudáveis (akusala) e 3 belos (sobhana)."),
    ("How many hetus are there in total?", "Six: 3 unwholesome (akusala) and 3 beautiful (sobhana)."),
    ("¿Cuántos hetus hay en total?", "Seis: 3 no saludables (akusala) y 3 bellos (sobhana)."),
    enrichment={
      "pt": {"breakdown": ["3 akusala: lobha (cobiça), dosa (aversão), moha (delusão)", "3 sobhana: alobha (desapego), adosa (benevolência), amoha (sabedoria/paññā)", "Cada par é oposto moral: lobha↔alobha, dosa↔adosa, moha↔amoha", "Moha é a raiz mais fundamental — presente em todos os 12 akusala cittas"], "explanation": "Os 6 hetus formam o eixo moral do Abhidhamma. As 3 raízes akusala mantêm os seres presos no samsāra; as 3 sobhana conduzem à libertação. A parelha moha/amoha é especialmente crítica: moha obscurece a realidade; amoha (= paññā) a revela.", "mnemonic": "6 = 3+3. Akusala: LO-DO-MO (Lobha-Dosa-Moha). Sobhana: A-A-A (Alobha-Adosa-Amoha). Espelho moral: cada sobhana é o antídoto da sua akusala parceira."},
      "en": {"breakdown": ["3 akusala: lobha (greed), dosa (aversion), moha (delusion)", "3 sobhana: alobha (non-attachment), adosa (goodwill), amoha (wisdom/paññā)", "Each pair is moral opposites: lobha↔alobha, dosa↔adosa, moha↔amoha", "Moha is the most fundamental root — present in all 12 akusala cittas"], "explanation": "The 6 hetus form the moral axis of the Abhidhamma. The 3 akusala roots keep beings bound in samsāra; the 3 sobhana lead to liberation. The moha/amoha pair is especially critical: moha obscures reality; amoha (= paññā) reveals it.", "mnemonic": "6 = 3+3. Akusala: L-D-M (Lobha-Dosa-Moha). Sobhana: A-A-A (Alobha-Adosa-Amoha). Moral mirror: each sobhana is the antidote to its akusala partner."},
      "es": {"breakdown": ["3 akusala: lobha (codicia), dosa (aversión), moha (ilusión)", "3 sobhana: alobha (desapego), adosa (benevolencia), amoha (sabiduría/paññā)", "Cada par es opuesto moral: lobha↔alobha, dosa↔adosa, moha↔amoha", "Moha es la raíz más fundamental — presente en todos los 12 akusala cittas"], "explanation": "Los 6 hetus forman el eje moral del Abhidhamma. Las 3 raíces akusala mantienen a los seres atrapados en el samsāra; las 3 sobhana conducen a la liberación. El par moha/amoha es especialmente crítico: moha oscurece la realidad; amoha (= paññā) la revela.", "mnemonic": "6 = 3+3. Akusala: L-D-M (Lobha-Dosa-Moha). Sobhana: A-A-A (Alobha-Adosa-Amoha). Espejo moral: cada sobhana es el antídoto de su pareja akusala."}
    })
add("at-h03", 3, "structures", H, "Akusala-hetu", 1, ["at-h02"], ["hetu", "akusala"],
    ("Quais são as 3 raízes não-saudáveis (akusala-hetu)?", "Lobha, dosa e moha."),
    ("What are the 3 unwholesome roots (akusala-hetu)?", "Lobha, dosa and moha."),
    ("¿Cuáles son las 3 raíces no saludables (akusala-hetu)?", "Lobha, dosa y moha."))
add("at-h04", 3, "philosophy", H, "Lobha", 1, ["at-h03"], ["hetu", "lobha"],
    ("O que é *lobha*?", "Cobiça, apego, avidez."),
    ("What is *lobha*?", "Greed, attachment, craving."),
    ("¿Qué es *lobha*?", "Codicia, apego, avidez."))
add("at-h05", 3, "philosophy", H, "Dosa", 1, ["at-h03"], ["hetu", "dosa"],
    ("O que é *dosa*?", "Aversão, ódio, raiva."),
    ("What is *dosa*?", "Aversion, hatred, anger."),
    ("¿Qué es *dosa*?", "Aversión, odio, ira."))
add("at-h06", 3, "philosophy", H, "Moha", 1, ["at-h03"], ["hetu", "moha"],
    ("O que é *moha*?", "Delusão, ignorância: obscurece a natureza real do objeto."),
    ("What is *moha*?", "Delusion, ignorance: it obscures the real nature of the object."),
    ("¿Qué es *moha*?", "Delusión, ignorancia: oscurece la naturaleza real del objeto."))
add("at-h07", 3, "structures", H, "Sobhana-hetu", 1, ["at-h02"], ["hetu", "sobhana"],
    ("Quais são as 3 raízes belas (sobhana-hetu)?", "Alobha, adosa e amoha."),
    ("What are the 3 beautiful roots (sobhana-hetu)?", "Alobha, adosa and amoha."),
    ("¿Cuáles son las 3 raíces bellas (sobhana-hetu)?", "Alobha, adosa y amoha."))
add("at-h08", 3, "philosophy", H, "Alobha", 1, ["at-h07"], ["hetu", "alobha"],
    ("O que é *alobha*?", "Não-cobiça, desapego, generosidade."),
    ("What is *alobha*?", "Non-greed, non-attachment, generosity."),
    ("¿Qué es *alobha*?", "No-codicia, desapego, generosidad."))
add("at-h09", 3, "philosophy", H, "Adosa", 1, ["at-h07"], ["hetu", "adosa"],
    ("O que é *adosa*?", "Não-aversão, benevolência (mettā)."),
    ("What is *adosa*?", "Non-aversion, goodwill (mettā)."),
    ("¿Qué es *adosa*?", "No-aversión, benevolencia (mettā)."))
add("at-h10", 3, "philosophy", H, "Amoha / Paññā", 1, ["at-h07"], ["hetu", "amoha"],
    ("O que é *amoha*?", "Não-delusão, sabedoria (paññā)."),
    ("What is *amoha*?", "Non-delusion, wisdom (paññā)."),
    ("¿Qué es *amoha*?", "No-delusión, sabiduría (paññā)."))
add("at-h11", 3, "exam_traps", H, "Moha", 1, ["at-h06"], ["hetu", "moha", "akusala"],
    ("Qual raiz está presente em TODO akusala citta?", "Moha."),
    ("Which root is present in EVERY akusala citta?", "Moha."),
    ("¿Qué raíz está presente en TODO akusala citta?", "Moha."),
    enrichment={
      "pt": {"breakdown": ["Todos os 12 akusala cittas têm moha", "8 lobha-mūla: moha + lobha (às vezes + diṭṭhi ou māna)", "2 dosa-mūla: moha + dosa (às vezes + issā/macchariya/kukkucca)", "2 moha-mūla: apenas moha (vicikicchā e uddhacca)", "Sem moha, não há akusala — moha é a 'escuridão de fundo'"], "explanation": "Moha (delusão) é a raiz primordial de todo akusala. Mesmo nos cittas de lobha ou dosa, moha está presente — sem ignorância sobre a natureza da realidade, lobha e dosa não poderiam surgir. Os 2 cittas moha-mūla têm APENAS moha.", "mnemonic": "MOHA em TODOS os 12 akusala. Fórmula: lobha-mūla = lobha + moha; dosa-mūla = dosa + moha; moha-mūla = moha apenas. Nunca há akusala sem moha."},
      "en": {"breakdown": ["All 12 akusala cittas have moha", "8 lobha-mūla: moha + lobha (sometimes + diṭṭhi or māna)", "2 dosa-mūla: moha + dosa (sometimes + issā/macchariya/kukkucca)", "2 moha-mūla: moha only (vicikicchā and uddhacca)", "Without moha, no akusala — moha is the 'background darkness'"], "explanation": "Moha (delusion) is the primordial root of all akusala. Even in cittas of lobha or dosa, moha is present — without ignorance about the nature of reality, lobha and dosa could not arise. The 2 moha-mūla cittas have moha ALONE.", "mnemonic": "MOHA in ALL 12 akusala. Formula: lobha-mūla = lobha + moha; dosa-mūla = dosa + moha; moha-mūla = moha only. Never akusala without moha."},
      "es": {"breakdown": ["Los 12 akusala cittas tienen moha", "8 lobha-mūla: moha + lobha (a veces + diṭṭhi o māna)", "2 dosa-mūla: moha + dosa (a veces + issā/macchariya/kukkucca)", "2 moha-mūla: solo moha (vicikicchā y uddhacca)", "Sin moha, no hay akusala — moha es la 'oscuridad de fondo'"], "explanation": "Moha (ilusión) es la raíz primordial de todo akusala. Incluso en los cittas de lobha o dosa, moha está presente — sin ignorancia sobre la naturaleza de la realidad, lobha y dosa no podrían surgir. Los 2 cittas moha-mūla tienen SOLO moha.", "mnemonic": "MOHA en TODOS los 12 akusala. Fórmula: lobha-mūla = lobha + moha; dosa-mūla = dosa + moha; moha-mūla = solo moha. Nunca hay akusala sin moha."}
    })
add("at-h12", 3, "philosophy", H, "Ahetuka", 1, ["at-h02"], ["hetu", "ahetuka"],
    ("O que significa *ahetuka*?", "\"Sem raiz\": consciência sem nenhum dos 6 hetus."),
    ("What does *ahetuka* mean?", "\"Rootless\": consciousness without any of the 6 hetus."),
    ("¿Qué significa *ahetuka*?", "\"Sin raíz\": conciencia sin ninguno de los 6 hetus."),
    enrichment={
      "pt": {"breakdown": ["18 cittas ahetuka: 7 akusala-vipāka + 8 kusala-vipāka (ahetuka) + 3 kiriya", "Os 18 ahetuka incluem as 10 dvipañcaviññāṇa (5 pares dos 5 sentidos)", "Ahetuka NÃO significa 'neutro moralmente' — vipāka akusala ainda é resultado de kamma ruim", "Cittas ahetuka produzem renascimento apenas nos planos inferiores (apāya) se vipāka akusala"], "explanation": "Ahetuka descreve a estrutura do citta, não sua tonalidade moral. Esses cittas não têm raiz (hetu) como cetasika associado — são mais simples. Os 10 cittas sensoriais básicos (pañcaviññāṇa) e os processos de recepção/investigação são todos ahetuka.", "mnemonic": "18 ahetuka = 7+8+3 (akusala-vipāka + kusala-vipāka + kiriya). Ver, ouvir, cheirar, saborear, tocar = todos ahetuka. Sem hetu = mais simples, não neutro."},
      "en": {"breakdown": ["18 ahetuka cittas: 7 akusala-vipāka + 8 kusala-vipāka (ahetuka) + 3 kiriya", "The 18 ahetuka include the 10 dvipañcaviññāṇa (5 pairs of the 5 senses)", "Ahetuka does NOT mean 'morally neutral' — akusala vipāka is still the result of bad kamma", "Ahetuka cittas produce rebirth only in lower planes (apāya) if akusala vipāka"], "explanation": "Ahetuka describes the citta's structure, not its moral tone. These cittas have no root (hetu) as an associated cetasika — they are simpler. The 10 basic sensory cittas (pañcaviññāṇa) and receiving/investigating processes are all ahetuka.", "mnemonic": "18 ahetuka = 7+8+3 (akusala-vipāka + kusala-vipāka + kiriya). Seeing, hearing, smelling, tasting, touching = all ahetuka. No hetu = simpler, not neutral."},
      "es": {"breakdown": ["18 cittas ahetuka: 7 akusala-vipāka + 8 kusala-vipāka (ahetuka) + 3 kiriya", "Los 18 ahetuka incluyen los 10 dvipañcaviññāṇa (5 pares de los 5 sentidos)", "Ahetuka NO significa 'moralmente neutro' — el vipāka akusala sigue siendo resultado de mal kamma", "Los cittas ahetuka producen renacimiento solo en planos inferiores (apāya) si son vipāka akusala"], "explanation": "Ahetuka describe la estructura del citta, no su tono moral. Estos cittas no tienen raíz (hetu) como cetasika asociado — son más simples. Los 10 cittas sensoriales básicos (pañcaviññāṇa) y los procesos de recepción/investigación son todos ahetuka.", "mnemonic": "18 ahetuka = 7+8+3 (akusala-vipāka + kusala-vipāka + kiriya). Ver, oír, oler, saborear, tocar = todos ahetuka. Sin hetu = más simple, no neutro."}
    })

A = "Akusalacitta"
# ── Akusala cittas ──────────────────────────────────────────────────────────
add("at-a01", 1, "quantities", A, "Dvādasākusalacittāni", 2, ["at-h03", "at-j01"], ["akusala"],
    ("Quantos akusala cittas existem?", "12."),
    ("How many akusala cittas are there?", "12."),
    ("¿Cuántos akusala cittas hay?", "12."),
    enrichment={
      "pt": {"breakdown": ["12 = 8 lobha-mūla + 2 dosa-mūla + 2 moha-mūla", "8 lobha-mūla: somanassa/upekkhā × diṭṭhigata/sem-diṭṭhi × sasaṅkhārika/asaṅkhārika", "2 dosa-mūla: domanassa × sasaṅkhārika/asaṅkhārika", "2 moha-mūla: vicikicchā (dúvida) e uddhacca (inquietação)", "Todos têm moha; lobha-mūla NUNCA têm domanassa"], "explanation": "Os 12 akusala cittas cobrem todas as formas de consciência não-saudável. A divisão 8+2+2 segue as raízes principais. Os 8 lobha-mūla variam em 3 dimensões: tonalidade afetiva, presença de visão-errada e se são espontâneos ou induzidos. Memorizar essa estrutura é essencial.", "mnemonic": "12 akusala = 8+2+2. Lobha=8 (somanassa ou upekkhā; com ou sem diṭṭhi; asaṅkhārika ou sasaṅkhārika). Dosa=2 (domanassa, asaṅ/saṅ). Moha=2 (vicikicchā + uddhacca). Todos têm MOHA."},
      "en": {"breakdown": ["12 = 8 lobha-mūla + 2 dosa-mūla + 2 moha-mūla", "8 lobha-mūla: somanassa/upekkhā × diṭṭhigata/no-diṭṭhi × sasaṅkhārika/asaṅkhārika", "2 dosa-mūla: domanassa × sasaṅkhārika/asaṅkhārika", "2 moha-mūla: vicikicchā (doubt) and uddhacca (restlessness)", "All have moha; lobha-mūla NEVER have domanassa"], "explanation": "The 12 akusala cittas cover all forms of unwholesome consciousness. The 8+2+2 division follows the primary roots. The 8 lobha-mūla vary along 3 dimensions: affective tone, presence of wrong-view, and whether spontaneous or prompted. Memorizing this structure is essential.", "mnemonic": "12 akusala = 8+2+2. Lobha=8 (somanassa or upekkhā; with or without diṭṭhi; asaṅkhārika or sasaṅkhārika). Dosa=2 (domanassa, asaṅ/saṅ). Moha=2 (vicikicchā + uddhacca). All have MOHA."},
      "es": {"breakdown": ["12 = 8 lobha-mūla + 2 dosa-mūla + 2 moha-mūla", "8 lobha-mūla: somanassa/upekkhā × diṭṭhigata/sin-diṭṭhi × sasaṅkhārika/asaṅkhārika", "2 dosa-mūla: domanassa × sasaṅkhārika/asaṅkhārika", "2 moha-mūla: vicikicchā (duda) y uddhacca (inquietud)", "Todos tienen moha; los lobha-mūla NUNCA tienen domanassa"], "explanation": "Los 12 akusala cittas cubren todas las formas de conciencia no saludable. La división 8+2+2 sigue las raíces principales. Los 8 lobha-mūla varían en 3 dimensiones: tonalidad afectiva, presencia de visión-errónea y si son espontáneos o inducidos. Memorizar esta estructura es esencial.", "mnemonic": "12 akusala = 8+2+2. Lobha=8 (somanassa o upekkhā; con o sin diṭṭhi; asaṅkhārika o sasaṅkhārika). Dosa=2 (domanassa, asaṅ/saṅ). Moha=2 (vicikicchā + uddhacca). Todos tienen MOHA."}
    })
add("at-a02", 1, "structures", A, "Akusala-mūla", 2, ["at-a01"], ["akusala", "mula"],
    ("Em quais 3 grupos, segundo a raiz, se dividem os 12 akusala cittas?",
     "Lobha-mūla, dosa-mūla e moha-mūla."),
    ("Into which 3 groups, by root, are the 12 akusala cittas divided?",
     "Lobha-mūla, dosa-mūla and moha-mūla."),
    ("¿En qué 3 grupos, según la raíz, se dividen los 12 akusala cittas?",
     "Lobha-mūla, dosa-mūla y moha-mūla."),
    enrichment={
      "pt": {"breakdown": ["Lobha-mūla (8): raízes = lobha + moha (± diṭṭhi/māna)", "Dosa-mūla (2): raízes = dosa + moha", "Moha-mūla (2): raiz = apenas moha", "A raiz dominante dá o nome ao grupo, mas moha está em TODOS"], "explanation": "A classificação por mūla é a divisão primária dos akusala cittas. O nome indica a raiz DOMINANTE, não a única. Todos têm moha como base. Os grupos diferem nos cetasikas associados: só lobha-mūla pode ter diṭṭhi; só dosa-mūla tem sempre domanassa-vedanā.", "mnemonic": "3 grupos: L-D-M (8-2-2). Lobha = cobiça domina. Dosa = aversão domina. Moha = apenas delusão. Todos = moha presente."},
      "en": {"breakdown": ["Lobha-mūla (8): roots = lobha + moha (± diṭṭhi/māna)", "Dosa-mūla (2): roots = dosa + moha", "Moha-mūla (2): root = moha alone", "The dominant root names the group, but moha is in ALL"], "explanation": "Classification by mūla is the primary division of akusala cittas. The name indicates the DOMINANT root, not the only one. All have moha as base. The groups differ in associated cetasikas: only lobha-mūla can have diṭṭhi; only dosa-mūla always has domanassa-vedanā.", "mnemonic": "3 groups: L-D-M (8-2-2). Lobha = greed dominates. Dosa = aversion dominates. Moha = delusion alone. All = moha present."},
      "es": {"breakdown": ["Lobha-mūla (8): raíces = lobha + moha (± diṭṭhi/māna)", "Dosa-mūla (2): raíces = dosa + moha", "Moha-mūla (2): raíz = solo moha", "La raíz dominante da nombre al grupo, pero moha está en TODOS"], "explanation": "La clasificación por mūla es la división primaria de los akusala cittas. El nombre indica la raíz DOMINANTE, no la única. Todos tienen moha como base. Los grupos difieren en los cetasikas asociados: solo los lobha-mūla pueden tener diṭṭhi; solo los dosa-mūla siempre tienen domanassa-vedanā.", "mnemonic": "3 grupos: L-D-M (8-2-2). Lobha = codicia domina. Dosa = aversión domina. Moha = solo ilusión. Todos = moha presente."}
    })
add("at-a03", 1, "quantities", A, "Lobhamūlacittāni", 2, ["at-a02", "at-h04"], ["akusala", "lobha"],
    ("Quantos lobha-mūla-cittas existem?", "8."),
    ("How many lobha-mūla-cittas are there?", "8."),
    ("¿Cuántos lobha-mūla-cittas hay?", "8."))
add("at-a04", 1, "quantities", A, "Dosamūlacittāni", 2, ["at-a02", "at-h05"], ["akusala", "dosa"],
    ("Quantos dosa-mūla-cittas existem?", "2."),
    ("How many dosa-mūla-cittas are there?", "2."),
    ("¿Cuántos dosa-mūla-cittas hay?", "2."))
add("at-a05", 1, "quantities", A, "Mohamūlacittāni", 2, ["at-a02", "at-h06"], ["akusala", "moha"],
    ("Quantos moha-mūla-cittas existem?", "2."),
    ("How many moha-mūla-cittas are there?", "2."),
    ("¿Cuántos moha-mūla-cittas hay?", "2."))
add("at-a06", 1, "structures", A, "Vicikicchā / Uddhacca", 2, ["at-a05"], ["akusala", "moha"],
    ("Quais são os 2 moha-mūla-cittas?",
     "Upekkhā-sahagata associado à dúvida (vicikicchā-sampayutta) e upekkhā-sahagata associado à inquietação (uddhacca-sampayutta)."),
    ("What are the 2 moha-mūla-cittas?",
     "Upekkhā-sahagata associated with doubt (vicikicchā-sampayutta) and upekkhā-sahagata associated with restlessness (uddhacca-sampayutta)."),
    ("¿Cuáles son los 2 moha-mūla-cittas?",
     "Upekkhā-sahagata asociado a la duda (vicikicchā-sampayutta) y upekkhā-sahagata asociado a la inquietud (uddhacca-sampayutta)."))
add("at-a07", 1, "structures", A, "Paṭigha-sampayutta", 2, ["at-a04"], ["akusala", "dosa"],
    ("Quais são os 2 dosa-mūla-cittas?",
     "Domanassa-sahagata paṭigha-sampayutta, em duas formas: asaṅkhārika e sasaṅkhārika."),
    ("What are the 2 dosa-mūla-cittas?",
     "Domanassa-sahagata paṭigha-sampayutta, in two forms: asaṅkhārika and sasaṅkhārika."),
    ("¿Cuáles son los 2 dosa-mūla-cittas?",
     "Domanassa-sahagata paṭigha-sampayutta, en dos formas: asaṅkhārika y sasaṅkhārika."))
add("at-a08", 1, "relations", A, "Lobha-mūla: hetu", 2, ["at-a03", "at-h11"], ["akusala", "lobha", "hetu"],
    ("Quais raízes estão presentes em um lobha-mūla-citta?", "Duas: lobha e moha."),
    ("Which roots are present in a lobha-mūla-citta?", "Two: lobha and moha."),
    ("¿Qué raíces están presentes en un lobha-mūla-citta?", "Dos: lobha y moha."))
add("at-a09", 1, "relations", A, "Dosa-mūla: hetu", 2, ["at-a04", "at-h11"], ["akusala", "dosa", "hetu"],
    ("Quais raízes estão presentes em um dosa-mūla-citta?", "Duas: dosa e moha."),
    ("Which roots are present in a dosa-mūla-citta?", "Two: dosa and moha."),
    ("¿Qué raíces están presentes en un dosa-mūla-citta?", "Dos: dosa y moha."))
add("at-a10", 1, "relations", A, "Moha-mūla: hetu", 2, ["at-a05", "at-h11"], ["akusala", "moha", "hetu"],
    ("Quais raízes estão presentes em um moha-mūla-citta?", "Somente moha."),
    ("Which roots are present in a moha-mūla-citta?", "Only moha."),
    ("¿Qué raíces están presentes en un moha-mūla-citta?", "Solo moha."))
add("at-a11", 1, "relations", A, "Domanassa", 2, ["at-a04"], ["akusala", "vedana"],
    ("Qual a vedanā dos 2 dosa-mūla-cittas?", "Domanassa (sensação mental desagradável)."),
    ("What is the vedanā of the 2 dosa-mūla-cittas?", "Domanassa (unpleasant mental feeling)."),
    ("¿Cuál es la vedanā de los 2 dosa-mūla-cittas?", "Domanassa (sensación mental desagradable)."))
add("at-a12", 1, "relations", A, "Upekkhā", 2, ["at-a05"], ["akusala", "vedana"],
    ("Qual a vedanā dos 2 moha-mūla-cittas?", "Upekkhā (neutra)."),
    ("What is the vedanā of the 2 moha-mūla-cittas?", "Upekkhā (neutral)."),
    ("¿Cuál es la vedanā de los 2 moha-mūla-cittas?", "Upekkhā (neutra)."))
add("at-a13", 1, "relations", A, "Somanassa / Upekkhā", 2, ["at-a03"], ["akusala", "lobha", "vedana"],
    ("Como os 8 lobha-mūla-cittas se dividem quanto à vedanā?",
     "4 com somanassa (alegria) e 4 com upekkhā (neutra)."),
    ("How do the 8 lobha-mūla-cittas divide by vedanā?",
     "4 with somanassa (joy) and 4 with upekkhā (neutral)."),
    ("¿Cómo se dividen los 8 lobha-mūla-cittas según la vedanā?",
     "4 con somanassa (alegría) y 4 con upekkhā (neutra)."))
add("at-a14", 1, "relations", A, "Diṭṭhigata", 2, ["at-a03"], ["akusala", "lobha", "ditthi"],
    ("Como os 8 lobha-mūla-cittas se dividem quanto à visão (diṭṭhi)?",
     "4 associados à visão errada (diṭṭhigata-sampayutta) e 4 dissociados (diṭṭhigata-vippayutta)."),
    ("How do the 8 lobha-mūla-cittas divide by view (diṭṭhi)?",
     "4 associated with wrong view (diṭṭhigata-sampayutta) and 4 dissociated (diṭṭhigata-vippayutta)."),
    ("¿Cómo se dividen los 8 lobha-mūla-cittas según la visión (diṭṭhi)?",
     "4 asociados a la visión errónea (diṭṭhigata-sampayutta) y 4 disociados (diṭṭhigata-vippayutta)."))
add("at-a15", 1, "philosophy", A, "Asaṅkhārika / Sasaṅkhārika", 2, ["at-t02"], ["akusala", "sankharika"],
    ("O que distingue asaṅkhārika de sasaṅkhārika?",
     "Asaṅkhārika: surge espontaneamente, sem estímulo. Sasaṅkhārika: surge com estímulo (próprio ou de outrem)."),
    ("What distinguishes asaṅkhārika from sasaṅkhārika?",
     "Asaṅkhārika: arises spontaneously, without prompting. Sasaṅkhārika: arises with prompting (self or other)."),
    ("¿Qué distingue asaṅkhārika de sasaṅkhārika?",
     "Asaṅkhārika: surge espontáneamente, sin estímulo. Sasaṅkhārika: surge con estímulo (propio o ajeno)."))
add("at-a16", 1, "structures", A, "8 = 2×2×2", 3, ["at-a13", "at-a14", "at-a15"], ["akusala", "lobha"],
    ("Os 8 lobha-mūla-cittas resultam de que combinação de fatores?",
     "2 vedanās (somanassa/upekkhā) × 2 (diṭṭhi associada/dissociada) × 2 (asaṅkhārika/sasaṅkhārika) = 8."),
    ("The 8 lobha-mūla-cittas result from which combination of factors?",
     "2 vedanās (somanassa/upekkhā) × 2 (diṭṭhi associated/dissociated) × 2 (asaṅkhārika/sasaṅkhārika) = 8."),
    ("¿Los 8 lobha-mūla-cittas resultan de qué combinación de factores?",
     "2 vedanās (somanassa/upekkhā) × 2 (diṭṭhi asociada/disociada) × 2 (asaṅkhārika/sasaṅkhārika) = 8."),
    enrichment={
      "pt": {"breakdown": ["Dimensão 1 — vedanā: somanassa (alegria) ou upekkhā (neutra)", "Dimensão 2 — diṭṭhi: sampayutta (com visão-errada) ou vippayutta (sem visão-errada)", "Dimensão 3 — impulso: asaṅkhārika (espontâneo) ou sasaṅkhārika (induzido)", "2×2×2 = 8 combinações únicas → 8 lobha-mūla-cittas"], "explanation": "Este cartão sintetiza a lógica combinatória dos lobha-mūla. Cada citta resulta de uma posição única nas 3 dimensões. Ex.: citta 1 = somanassa + diṭṭhi + asaṅkhārika; citta 8 = upekkhā + vippayutta + sasaṅkhārika. Conhecer a matriz 2×2×2 permite reconstruir os 8 cittas a partir de princípios.", "mnemonic": "2×2×2 = 8. DIMENSÕES: Sentimento (S/U) × Visão (D/V) × Impulso (A/S). Prioridade de memorização: primeiro a vedanā, depois diṭṭhi, depois sankharika."},
      "en": {"breakdown": ["Dimension 1 — vedanā: somanassa (joy) or upekkhā (neutral)", "Dimension 2 — diṭṭhi: sampayutta (with wrong-view) or vippayutta (without wrong-view)", "Dimension 3 — impetus: asaṅkhārika (spontaneous) or sasaṅkhārika (prompted)", "2×2×2 = 8 unique combinations → 8 lobha-mūla-cittas"], "explanation": "This card synthesizes the combinatorial logic of lobha-mūla. Each citta results from a unique position along 3 dimensions. E.g.: citta 1 = somanassa + diṭṭhi + asaṅkhārika; citta 8 = upekkhā + vippayutta + sasaṅkhārika. Knowing the 2×2×2 matrix lets you reconstruct all 8 cittas from principles.", "mnemonic": "2×2×2 = 8. DIMENSIONS: Feeling (S/U) × View (D/V) × Impetus (A/S). Memorization priority: feeling first, then diṭṭhi, then sankharika."},
      "es": {"breakdown": ["Dimensión 1 — vedanā: somanassa (alegría) o upekkhā (neutra)", "Dimensión 2 — diṭṭhi: sampayutta (con visión-errónea) o vippayutta (sin visión-errónea)", "Dimensión 3 — impulso: asaṅkhārika (espontáneo) o sasaṅkhārika (inducido)", "2×2×2 = 8 combinaciones únicas → 8 lobha-mūla-cittas"], "explanation": "Este cartón sintetiza la lógica combinatoria de los lobha-mūla. Cada citta resulta de una posición única en 3 dimensiones. Ej.: citta 1 = somanassa + diṭṭhi + asaṅkhārika; citta 8 = upekkhā + vippayutta + sasaṅkhārika. Conocer la matriz 2×2×2 permite reconstruir los 8 cittas desde principios.", "mnemonic": "2×2×2 = 8. DIMENSIONES: Sensación (S/U) × Visión (D/V) × Impulso (A/S). Prioridad de memorización: primero la vedanā, luego diṭṭhi, luego sankharika."}
    })
add("at-a17", 1, "quantities", A, "8 + 2 + 2 = 12", 3, ["at-a03", "at-a04", "at-a05"], ["akusala"],
    ("Como se compõem os 12 akusala cittas por raiz?", "8 lobha-mūla + 2 dosa-mūla + 2 moha-mūla = 12."),
    ("How are the 12 akusala cittas composed by root?", "8 lobha-mūla + 2 dosa-mūla + 2 moha-mūla = 12."),
    ("¿Cómo se componen los 12 akusala cittas por raíz?", "8 lobha-mūla + 2 dosa-mūla + 2 moha-mūla = 12."),
    enrichment={
      "pt": {"breakdown": ["8 lobha-mūla (cobiça): a maior família — 8 = 2×2×2", "2 dosa-mūla (aversão): todos com domanassa e paṭigha", "2 moha-mūla (delusão): vicikicchā + uddhacca, todos com upekkhā", "Soma: 8+2+2 = 12 akusala cittas (kāmāvacara, nunca mahaggata)"], "explanation": "Este é o cartão-síntese dos 12 akusala cittas. A fórmula 8+2+2 deve ser memorizada como uma das equações fundamentais do Abhidhamma. Note que NUNCA há citta akusala mahaggata ou lokuttara — os akusala são exclusivamente kāmāvacara.", "mnemonic": "12 = 8+2+2. LOBHA domina (8). DOSA e MOHA têm 2 cada. Ekuação: oito mais dois mais dois = doze. Akusala = SEMPRE kāmāvacara."},
      "en": {"breakdown": ["8 lobha-mūla (greed): the largest family — 8 = 2×2×2", "2 dosa-mūla (aversion): all with domanassa and paṭigha", "2 moha-mūla (delusion): vicikicchā + uddhacca, all with upekkhā", "Sum: 8+2+2 = 12 akusala cittas (kāmāvacara only, never mahaggata)"], "explanation": "This is the synthesis card for the 12 akusala cittas. The formula 8+2+2 must be memorized as one of the fundamental equations of the Abhidhamma. Note that there is NEVER a mahaggata or lokuttara akusala citta — akusala is exclusively kāmāvacara.", "mnemonic": "12 = 8+2+2. LOBHA dominates (8). DOSA and MOHA have 2 each. Equation: eight plus two plus two equals twelve. Akusala = ALWAYS kāmāvacara."},
      "es": {"breakdown": ["8 lobha-mūla (codicia): la familia más grande — 8 = 2×2×2", "2 dosa-mūla (aversión): todos con domanassa y paṭigha", "2 moha-mūla (ilusión): vicikicchā + uddhacca, todos con upekkhā", "Suma: 8+2+2 = 12 akusala cittas (solo kāmāvacara, nunca mahaggata)"], "explanation": "Este es el cartón-síntesis de los 12 akusala cittas. La fórmula 8+2+2 debe memorizarse como una de las ecuaciones fundamentales del Abhidhamma. Nótese que NUNCA hay un citta akusala mahaggata o lokuttara — los akusala son exclusivamente kāmāvacara.", "mnemonic": "12 = 8+2+2. LOBHA domina (8). DOSA y MOHA tienen 2 cada uno. Ecuación: ocho más dos más dos igual doce. Akusala = SIEMPRE kāmāvacara."}
    })

K = "Ahetukacitta"
# ── Ahetuka cittas ──────────────────────────────────────────────────────────
add("at-k01", 1, "philosophy", K, "Ahetukacitta", 1, ["at-h12"], ["ahetuka"],
    ("O que define um ahetuka citta?",
     "É um citta sem nenhum dos seis hetus (nem lobha/dosa/moha, nem alobha/adosa/amoha)."),
    ("What defines an ahetuka citta?",
     "A citta without any of the six hetus (neither lobha/dosa/moha nor alobha/adosa/amoha)."),
    ("¿Qué define un ahetuka citta?",
     "Un citta sin ninguno de los seis hetus (ni lobha/dosa/moha, ni alobha/adosa/amoha)."))
add("at-k02", 1, "quantities", K, "Aṭṭhārasa Ahetukacittāni", 2, ["at-k01"], ["ahetuka"],
    ("Quantos ahetuka cittas existem?", "18."),
    ("How many ahetuka cittas are there?", "18."),
    ("¿Cuántos ahetuka cittas hay?", "18."))
add("at-k03", 1, "structures", K, "Vipāka / Kiriya", 2, ["at-k02", "at-j03", "at-j04"], ["ahetuka"],
    ("Em quais categorias funcionais se dividem os 18 ahetuka cittas?",
     "Ahetuka-vipāka (15) e ahetuka-kiriya (3)."),
    ("Into which functional categories are the 18 ahetuka cittas divided?",
     "Ahetuka-vipāka (15) and ahetuka-kiriya (3)."),
    ("¿En qué categorías funcionales se dividen los 18 ahetuka cittas?",
     "Ahetuka-vipāka (15) y ahetuka-kiriya (3)."))
add("at-k04", 1, "structures", K, "Pañca-viññāṇa", 2, ["at-k01"], ["ahetuka", "vinnana"],
    ("Quais são as 5 consciências sensoriais?",
     "Cakkhu-, sota-, ghāna-, jivhā- e kāya-viññāṇa."),
    ("What are the 5 sense-consciousnesses?",
     "Cakkhu-, sota-, ghāna-, jivhā- and kāya-viññāṇa."),
    ("¿Cuáles son las 5 conciencias sensoriales?",
     "Cakkhu-, sota-, ghāna-, jivhā- y kāya-viññāṇa."))
add("at-k05", 1, "quantities", K, "Dvipañcaviññāṇa", 2, ["at-k04", "at-k03"], ["ahetuka", "vinnana"],
    ("O que é o dvipañcaviññāṇa e quantos cittas tem?",
     "Os dois conjuntos de cinco viññāṇas: 5 kusala-vipāka + 5 akusala-vipāka = 10."),
    ("What is the dvipañcaviññāṇa and how many cittas does it have?",
     "The two sets of five viññāṇas: 5 kusala-vipāka + 5 akusala-vipāka = 10."),
    ("¿Qué es el dvipañcaviññāṇa y cuántos cittas tiene?",
     "Los dos conjuntos de cinco viññāṇas: 5 kusala-vipāka + 5 akusala-vipāka = 10."))
add("at-k06", 1, "relations", K, "Vedanā dos viññāṇas", 2, ["at-k05"], ["ahetuka", "vedana"],
    ("Qual a vedanā dos viññāṇas sensoriais?",
     "Upekkhā, exceto o kāya-viññāṇa: sukha (kusala-vipāka) ou dukkha (akusala-vipāka)."),
    ("What is the vedanā of the sense-viññāṇas?",
     "Upekkhā, except kāya-viññāṇa: sukha (kusala-vipāka) or dukkha (akusala-vipāka)."),
    ("¿Cuál es la vedanā de los viññāṇas sensoriales?",
     "Upekkhā, excepto kāya-viññāṇa: sukha (kusala-vipāka) o dukkha (akusala-vipāka)."))
add("at-k07", 1, "quantities", K, "Sampaṭicchana", 2, ["at-k03"], ["ahetuka", "sampaticchana"],
    ("Quantos sampaṭicchana cittas existem e qual sua vedanā?",
     "2 (um kusala-vipāka e um akusala-vipāka), ambos com upekkhā."),
    ("How many sampaṭicchana cittas are there and what is their vedanā?",
     "2 (one kusala-vipāka and one akusala-vipāka), both with upekkhā."),
    ("¿Cuántos sampaṭicchana cittas hay y cuál es su vedanā?",
     "2 (uno kusala-vipāka y uno akusala-vipāka), ambos con upekkhā."))
add("at-k08", 1, "quantities", K, "Santīraṇa", 2, ["at-k03"], ["ahetuka", "santirana"],
    ("Quantos santīraṇa cittas existem?",
     "3: akusala-vipāka upekkhā, kusala-vipāka somanassa e kusala-vipāka upekkhā."),
    ("How many santīraṇa cittas are there?",
     "3: akusala-vipāka upekkhā, kusala-vipāka somanassa and kusala-vipāka upekkhā."),
    ("¿Cuántos santīraṇa cittas hay?",
     "3: akusala-vipāka upekkhā, kusala-vipāka somanassa y kusala-vipāka upekkhā."))
add("at-k09", 1, "quantities", K, "Akusala-vipāka ahetuka (7)", 2, ["at-k05", "at-k07", "at-k08"], ["ahetuka", "vipaka"],
    ("Como se compõem os 7 ahetuka akusala-vipāka cittas?", "5 viññāṇas + 1 sampaṭicchana + 1 santīraṇa."),
    ("How are the 7 ahetuka akusala-vipāka cittas composed?", "5 viññāṇas + 1 sampaṭicchana + 1 santīraṇa."),
    ("¿Cómo se componen los 7 ahetuka akusala-vipāka cittas?", "5 viññāṇas + 1 sampaṭicchana + 1 santīraṇa."))
add("at-k10", 1, "quantities", K, "Kusala-vipāka ahetuka (8)", 2, ["at-k05", "at-k07", "at-k08"], ["ahetuka", "vipaka"],
    ("Como se compõem os 8 ahetuka kusala-vipāka cittas?", "5 viññāṇas + 1 sampaṭicchana + 2 santīraṇas."),
    ("How are the 8 ahetuka kusala-vipāka cittas composed?", "5 viññāṇas + 1 sampaṭicchana + 2 santīraṇas."),
    ("¿Cómo se componen los 8 ahetuka kusala-vipāka cittas?", "5 viññāṇas + 1 sampaṭicchana + 2 santīraṇas."))
add("at-k11", 1, "quantities", K, "Ahetuka-vipāka (15)", 3, ["at-k09", "at-k10"], ["ahetuka", "vipaka"],
    ("Como se compõem os 15 ahetuka-vipāka cittas?",
     "10 dvipañcaviññāṇa + 2 sampaṭicchana + 3 santīraṇa (= 7 + 8)."),
    ("How are the 15 ahetuka-vipāka cittas composed?",
     "10 dvipañcaviññāṇa + 2 sampaṭicchana + 3 santīraṇa (= 7 + 8)."),
    ("¿Cómo se componen los 15 ahetuka-vipāka cittas?",
     "10 dvipañcaviññāṇa + 2 sampaṭicchana + 3 santīraṇa (= 7 + 8)."))
add("at-k12", 1, "structures", K, "Ahetuka-kiriya", 2, ["at-k03"], ["ahetuka", "kiriya"],
    ("Quais são os 3 ahetuka-kiriya cittas?",
     "Pañcadvārāvajjana, manodvārāvajjana e hasituppāda."),
    ("What are the 3 ahetuka-kiriya cittas?",
     "Pañcadvārāvajjana, manodvārāvajjana and hasituppāda."),
    ("¿Cuáles son los 3 ahetuka-kiriya cittas?",
     "Pañcadvārāvajjana, manodvārāvajjana y hasituppāda."))
add("at-k13", 1, "philosophy", K, "Pañcadvārāvajjana", 2, ["at-k12"], ["ahetuka", "kiriya"],
    ("Qual a função do pañcadvārāvajjana?",
     "Voltar a atenção ao objeto que surge em uma das cinco portas sensoriais."),
    ("What is the function of the pañcadvārāvajjana?",
     "To advert to the object arising at one of the five sense doors."),
    ("¿Cuál es la función del pañcadvārāvajjana?",
     "Dirigir la atención al objeto que surge en una de las cinco puertas sensoriales."))
add("at-k14", 1, "philosophy", K, "Manodvārāvajjana", 2, ["at-k12"], ["ahetuka", "kiriya"],
    ("Qual a função do manodvārāvajjana?",
     "Voltar a atenção ao objeto da porta mental; nas portas sensoriais exerce também a função de determinação (voṭṭhapana)."),
    ("What is the function of the manodvārāvajjana?",
     "To advert to the object at the mind door; at the sense doors it also performs determining (voṭṭhapana)."),
    ("¿Cuál es la función del manodvārāvajjana?",
     "Dirigir la atención al objeto de la puerta mental; en las puertas sensoriales también ejerce la determinación (voṭṭhapana)."))
add("at-k15", 1, "philosophy", K, "Hasituppāda", 2, ["at-k12"], ["ahetuka", "kiriya"],
    ("O que é o hasituppāda citta?",
     "Citta funcional com somanassa que gera o sorriso do Arahant."),
    ("What is the hasituppāda citta?",
     "A functional citta with somanassa that produces the smile of the Arahant."),
    ("¿Qué es el hasituppāda citta?",
     "Citta funcional con somanassa que produce la sonrisa del Arahant."))
add("at-k16", 1, "quantities", K, "7 + 8 + 3 = 18", 3, ["at-k09", "at-k10", "at-k12"], ["ahetuka"],
    ("Como se compõem os 18 ahetuka cittas?", "7 akusala-vipāka + 8 kusala-vipāka + 3 kiriya = 18."),
    ("How are the 18 ahetuka cittas composed?", "7 akusala-vipāka + 8 kusala-vipāka + 3 kiriya = 18."),
    ("¿Cómo se componen los 18 ahetuka cittas?", "7 akusala-vipāka + 8 kusala-vipāka + 3 kiriya = 18."),
    enrichment={
      "pt": {"breakdown": ["7 akusala-vipāka: 5 pañcaviññāṇa + 1 sampaṭicchana + 1 santīraṇa (todos upekkhā)", "8 kusala-vipāka: 5 pañcaviññāṇa + 1 sampaṭicchana + 2 santīraṇa (1 somanassa + 1 upekkhā)", "3 kiriya: pañcadvārāvajjana + manodvārāvajjana + hasituppāda", "Total: 7+8+3 = 18 ahetuka = segunda família dos 54 kāmāvacara"], "explanation": "Este cartão sintetiza toda a família ahetuka (sem raiz). Os 18 operam sem nenhum hetu associado. São os cittas mais simples — puras funções. A distinção kusala-vipāka (8) vs. akusala-vipāka (7) reflete o karma passado. Os 3 kiriya são funcionais universais (pañcadvārāvajjana e manodvārāvajjana) + 1 exclusivo do Arahant (hasituppāda).", "mnemonic": "18 = 7+8+3. Dica: akusala tem 7 (menos 1 no santīraṇa — o de somanassa é só kusala). Kiriya = 3 (pañca + mano + hasita). Total geral: 12+18+24 = 54 kāmāvacara."},
      "en": {"breakdown": ["7 akusala-vipāka: 5 pañcaviññāṇa + 1 sampaṭicchana + 1 santīraṇa (all upekkhā)", "8 kusala-vipāka: 5 pañcaviññāṇa + 1 sampaṭicchana + 2 santīraṇa (1 somanassa + 1 upekkhā)", "3 kiriya: pañcadvārāvajjana + manodvārāvajjana + hasituppāda", "Total: 7+8+3 = 18 ahetuka = second family of the 54 kāmāvacara"], "explanation": "This card synthesizes the entire ahetuka (rootless) family. The 18 operate without any associated hetu. They are the simplest cittas — pure functions. The distinction kusala-vipāka (8) vs. akusala-vipāka (7) reflects past kamma. The 3 kiriya are universal functionals (pañcadvārāvajjana and manodvārāvajjana) + 1 Arahant-exclusive (hasituppāda).", "mnemonic": "18 = 7+8+3. Tip: akusala has 7 (one less in santīraṇa — the somanassa one is kusala only). Kiriya = 3 (pañca + mano + hasita). Grand total: 12+18+24 = 54 kāmāvacara."},
      "es": {"breakdown": ["7 akusala-vipāka: 5 pañcaviññāṇa + 1 sampaṭicchana + 1 santīraṇa (todos upekkhā)", "8 kusala-vipāka: 5 pañcaviññāṇa + 1 sampaṭicchana + 2 santīraṇa (1 somanassa + 1 upekkhā)", "3 kiriya: pañcadvārāvajjana + manodvārāvajjana + hasituppāda", "Total: 7+8+3 = 18 ahetuka = segunda familia de los 54 kāmāvacara"], "explanation": "Este cartón sintetiza toda la familia ahetuka (sin raíz). Los 18 operan sin ningún hetu asociado. Son los cittas más simples — funciones puras. La distinción kusala-vipāka (8) vs. akusala-vipāka (7) refleja el kamma pasado. Los 3 kiriya son funcionales universales (pañcadvārāvajjana y manodvārāvajjana) + 1 exclusivo del Arahant (hasituppāda).", "mnemonic": "18 = 7+8+3. Pista: akusala tiene 7 (uno menos en santīraṇa — el de somanassa es solo kusala). Kiriya = 3 (pañca + mano + hasita). Total general: 12+18+24 = 54 kāmāvacara."}
    })


# ── Esfera dos sentidos: akusala/ahetuka pertencem a ela ─────────────────────
AT("at-a18", 1, "relations", A, "Akusala: Kāmāvacara", ["at-a01", "at-p02"], ["akusala", "bhumi"],
   ("Os akusala cittas pertencem a qual esfera?", "Kāmāvacara."),
   ("Which sphere do the akusala cittas belong to?", "Kāmāvacara."),
   ("¿A qué esfera pertenecen los akusala cittas?", "Kāmāvacara."))
AT("at-k17", 1, "relations", K, "Ahetuka: Kāmāvacara", ["at-k02", "at-p02"], ["ahetuka", "bhumi"],
   ("Os ahetuka cittas pertencem a qual esfera?", "Kāmāvacara."),
   ("Which sphere do the ahetuka cittas belong to?", "Kāmāvacara."),
   ("¿A qué esfera pertenecen los ahetuka cittas?", "Kāmāvacara."))

S = "Kāmāvacara Sobhana"
AT("at-x02", 1, "philosophy", S, "Ñāṇa-sampayutta", ["at-h10", "at-t06"], ["nana"],
   ("O que significa *ñāṇa-sampayutta*?", "Associado ao conhecimento (ñāṇa = paññā = amoha): tem a raiz da sabedoria."),
   ("What does *ñāṇa-sampayutta* mean?", "Associated with knowledge (ñāṇa = paññā = amoha): it has the root of wisdom."),
   ("¿Qué significa *ñāṇa-sampayutta*?", "Asociado al conocimiento (ñāṇa = paññā = amoha): tiene la raíz de la sabiduría."))
# ── Sobhana kāmāvacara (24) ──────────────────────────────────────────────────
AT("at-s01", 1, "quantities", S, "Mahākusalacittāni", ["at-h07", "at-p02", "at-j02"], ["sobhana", "mahakusala"],
   ("Quantos mahākusala cittas (kusala belos da esfera dos sentidos) existem?", "8."),
   ("How many mahākusala cittas (beautiful kusala of the sense sphere) are there?", "8."),
   ("¿Cuántos mahākusala cittas (kusala bellos de la esfera sensorial) hay?", "8."))
AT("at-s02", 1, "relations", S, "Mahākusala: vedanā", ["at-s01", "at-v03", "at-v04"], ["sobhana", "vedana"],
   ("Como os 8 mahākusala se dividem quanto à vedanā?", "4 com somanassa e 4 com upekkhā."),
   ("How do the 8 mahākusala divide by vedanā?", "4 with somanassa and 4 with upekkhā."),
   ("¿Cómo se dividen los 8 mahākusala según la vedanā?", "4 con somanassa y 4 con upekkhā."))
AT("at-s03", 1, "relations", S, "Mahākusala: ñāṇa", ["at-s01", "at-x02"], ["sobhana", "nana"],
   ("Como os 8 mahākusala se dividem quanto ao ñāṇa?", "4 ñāṇa-sampayutta e 4 ñāṇa-vippayutta."),
   ("How do the 8 mahākusala divide by ñāṇa?", "4 ñāṇa-sampayutta and 4 ñāṇa-vippayutta."),
   ("¿Cómo se dividen los 8 mahākusala según el ñāṇa?", "4 ñāṇa-sampayutta y 4 ñāṇa-vippayutta."))
AT("at-s04", 1, "relations", S, "Mahākusala: saṅkhārika", ["at-s01", "at-a15"], ["sobhana", "sankharika"],
   ("Como os 8 mahākusala se dividem quanto ao estímulo?", "4 asaṅkhārika e 4 sasaṅkhārika."),
   ("How do the 8 mahākusala divide by prompting?", "4 asaṅkhārika and 4 sasaṅkhārika."),
   ("¿Cómo se dividen los 8 mahākusala según el estímulo?", "4 asaṅkhārika y 4 sasaṅkhārika."))
AT("at-s05", 1, "structures", S, "8 = 2×2×2", ["at-s02", "at-s03", "at-s04"], ["sobhana"],
   ("Os 8 mahākusala resultam de que combinação de fatores?", "2 vedanās (somanassa/upekkhā) × 2 (ñāṇa associado/dissociado) × 2 (asaṅkhārika/sasaṅkhārika) = 8."),
   ("The 8 mahākusala result from which combination of factors?", "2 vedanās (somanassa/upekkhā) × 2 (ñāṇa associated/dissociated) × 2 (asaṅkhārika/sasaṅkhārika) = 8."),
   ("¿Los 8 mahākusala resultan de qué combinación de factores?", "2 vedanās (somanassa/upekkhā) × 2 (ñāṇa asociado/disociado) × 2 (asaṅkhārika/sasaṅkhārika) = 8."))
AT("at-s06", 1, "relations", S, "Tihetuka (sobhana)", ["at-s03", "at-h07"], ["sobhana", "hetu"],
   ("Quais raízes têm os mahākusala ñāṇa-sampayutta?", "Três: alobha, adosa e amoha."),
   ("Which roots do the ñāṇa-sampayutta mahākusala have?", "Three: alobha, adosa and amoha."),
   ("¿Qué raíces tienen los mahākusala ñāṇa-sampayutta?", "Tres: alobha, adosa y amoha."))
AT("at-s07", 1, "relations", S, "Dvihetuka (sobhana)", ["at-s03", "at-h07"], ["sobhana", "hetu"],
   ("Quais raízes têm os mahākusala ñāṇa-vippayutta?", "Duas: alobha e adosa."),
   ("Which roots do the ñāṇa-vippayutta mahākusala have?", "Two: alobha and adosa."),
   ("¿Qué raíces tienen los mahākusala ñāṇa-vippayutta?", "Dos: alobha y adosa."))
AT("at-s08", 1, "quantities", S, "Mahāvipākacittāni", ["at-s05", "at-j03"], ["sobhana", "mahavipaka"],
   ("Quantos mahāvipāka cittas existem e como se estruturam?", "8, com a mesma estrutura 2×2×2 dos mahākusala, dos quais são o resultado."),
   ("How many mahāvipāka cittas are there and how are they structured?", "8, with the same 2×2×2 structure as the mahākusala, of which they are the result."),
   ("¿Cuántos mahāvipāka cittas hay y cómo se estructuran?", "8, con la misma estructura 2×2×2 de los mahākusala, de los cuales son el resultado."))
AT("at-s09", 1, "quantities", S, "Mahākiriyacittāni", ["at-s05", "at-j04"], ["sobhana", "mahakiriya"],
   ("Quantos mahākiriya cittas existem e em quem surgem?", "8, com a mesma estrutura 2×2×2; surgem apenas nos Arahants."),
   ("How many mahākiriya cittas are there and in whom do they arise?", "8, with the same 2×2×2 structure; they arise only in Arahants."),
   ("¿Cuántos mahākiriya cittas hay y en quién surgen?", "8, con la misma estructura 2×2×2; surgen solo en los Arahants."))
AT("at-s10", 1, "quantities", S, "Catuvīsati Sobhana", ["at-s05", "at-s08", "at-s09"], ["sobhana"],
   ("Quantos sobhana cittas kāmāvacara existem e como se compõem?", "24 = 8 mahākusala + 8 mahāvipāka + 8 mahākiriya."),
   ("How many kāmāvacara sobhana cittas are there and how are they composed?", "24 = 8 mahākusala + 8 mahāvipāka + 8 mahākiriya."),
   ("¿Cuántos sobhana cittas kāmāvacara hay y cómo se componen?", "24 = 8 mahākusala + 8 mahāvipāka + 8 mahākiriya."),
   enrichment={
     "pt": {"breakdown": ["24 = 8 mahākusala + 8 mahāvipāka + 8 mahākiriya", "Todos têm a mesma estrutura 2×2×2 (vedanā × ñāṇa × saṅkhārika)", "Mahākusala: atos morais belos dos seres comuns e aprendizes", "Mahāvipāka: frutos dos mahākusala — determinam o renascimento sobhana", "Mahākiriya: equivalente funcional no Arahant"], "explanation": "Os 24 sobhana kāmāvacara são a terceira família dos 54. São chamados 'mahā' ('grandes') porque têm raízes belas (alobha, adosa e às vezes amoha). A estrutura 2×2×2 é paralela às dos 8 lobha-mūla, mas com fatores belos. Mahāvipāka determinam o tipo de renascimento: tihetuka (3 raízes) → renascimento tihetuka.", "mnemonic": "24 sobhana = 8+8+8. Todos mahā (= belos). Estrutura 2×2×2 = mesma dos 8 lobha-mūla mas com fatores opostos. Total: 12+18+24 = 54 kāmāvacara."},
     "en": {"breakdown": ["24 = 8 mahākusala + 8 mahāvipāka + 8 mahākiriya", "All share the same 2×2×2 structure (vedanā × ñāṇa × saṅkhārika)", "Mahākusala: beautiful moral acts of ordinary beings and trainees", "Mahāvipāka: fruits of mahākusala — determine the sobhana rebirth", "Mahākiriya: functional equivalent in the Arahant"], "explanation": "The 24 kāmāvacara sobhana are the third family of the 54. They are called 'mahā' ('great') because they have beautiful roots (alobha, adosa and sometimes amoha). The 2×2×2 structure mirrors the 8 lobha-mūla, but with beautiful factors. Mahāvipāka determine the type of rebirth: tihetuka (3 roots) → tihetuka rebirth.", "mnemonic": "24 sobhana = 8+8+8. All mahā (= beautiful). Structure 2×2×2 = same as 8 lobha-mūla but with opposite factors. Total: 12+18+24 = 54 kāmāvacara."},
     "es": {"breakdown": ["24 = 8 mahākusala + 8 mahāvipāka + 8 mahākiriya", "Todos comparten la misma estructura 2×2×2 (vedanā × ñāṇa × saṅkhārika)", "Mahākusala: actos morales bellos de seres ordinarios y aprendices", "Mahāvipāka: frutos de los mahākusala — determinan el renacimiento sobhana", "Mahākiriya: equivalente funcional en el Arahant"], "explanation": "Los 24 sobhana kāmāvacara son la tercera familia de los 54. Se llaman 'mahā' ('grandes') porque tienen raíces bellas (alobha, adosa y a veces amoha). La estructura 2×2×2 es paralela a la de los 8 lobha-mūla, pero con factores bellos. Los mahāvipāka determinan el tipo de renacimiento: tihetuka (3 raíces) → renacimiento tihetuka.", "mnemonic": "24 sobhana = 8+8+8. Todos mahā (= bellos). Estructura 2×2×2 = igual a la de los 8 lobha-mūla pero con factores opuestos. Total: 12+18+24 = 54 kāmāvacara."}
   })
AT("at-s14", 1, "quantities", S, "Sobhana ñāṇa-vippayutta", ["at-s03", "at-s10"], ["sobhana", "nana"],
   ("Quantos sobhana kāmāvacara são ñāṇa-vippayutta?", "12 (4 kusala + 4 vipāka + 4 kiriya)."),
   ("How many kāmāvacara sobhana are ñāṇa-vippayutta?", "12 (4 kusala + 4 vipāka + 4 kiriya)."),
   ("¿Cuántos sobhana kāmāvacara son ñāṇa-vippayutta?", "12 (4 kusala + 4 vipāka + 4 kiriya)."))
AT("at-s15", 1, "quantities", S, "Sobhana ñāṇa-sampayutta", ["at-s03", "at-s10"], ["sobhana", "nana"],
   ("Quantos sobhana kāmāvacara são ñāṇa-sampayutta?", "12 (4 kusala + 4 vipāka + 4 kiriya)."),
   ("How many kāmāvacara sobhana are ñāṇa-sampayutta?", "12 (4 kusala + 4 vipāka + 4 kiriya)."),
   ("¿Cuántos sobhana kāmāvacara son ñāṇa-sampayutta?", "12 (4 kusala + 4 vipāka + 4 kiriya)."))
AT("at-s12", 1, "quantities", "Kāmāvacara 54", "Catupaññāsa Kāmāvacara", ["at-a17", "at-k16", "at-s10"], ["kamavacara"],
   ("Quantos cittas kāmāvacara existem e como se compõem?", "54 = 12 akusala + 18 ahetuka + 24 sobhana."),
   ("How many kāmāvacara cittas are there and how are they composed?", "54 = 12 akusala + 18 ahetuka + 24 sobhana."),
   ("¿Cuántos cittas kāmāvacara hay y cómo se componen?", "54 = 12 akusala + 18 ahetuka + 24 sobhana."))

# ── Rūpāvacara (15) ──────────────────────────────────────────────────────────
R = "Rūpāvacara"
AT("at-r01", 1, "quantities", R, "Pañca Jhānaṅga", ["at-t03"], ["jhana"],
   ("Quais são os 5 fatores do jhāna (jhānaṅga)?", "Vitakka, vicāra, pīti, sukha e ekaggatā."),
   ("What are the 5 jhāna factors (jhānaṅga)?", "Vitakka, vicāra, pīti, sukha and ekaggatā."),
   ("¿Cuáles son los 5 factores del jhāna (jhānaṅga)?", "Vitakka, vicāra, pīti, sukha y ekaggatā."))
AT("at-r02", 1, "philosophy", R, "Vitakka", ["at-r01"], ["jhana"],
   ("O que é *vitakka*?", "Aplicação inicial da mente ao objeto."),
   ("What is *vitakka*?", "Initial application of the mind to the object."),
   ("¿Qué es *vitakka*?", "Aplicación inicial de la mente al objeto."))
AT("at-r03", 1, "philosophy", R, "Vicāra", ["at-r01"], ["jhana"],
   ("O que é *vicāra*?", "Sustentação contínua da mente sobre o objeto."),
   ("What is *vicāra*?", "Sustained application of the mind on the object."),
   ("¿Qué es *vicāra*?", "Sostenimiento continuo de la mente sobre el objeto."))
AT("at-r04", 1, "philosophy", R, "Pīti", ["at-r01"], ["jhana"],
   ("O que é *pīti*?", "Alegria, êxtase: interesse prazeroso pelo objeto."),
   ("What is *pīti*?", "Joy, rapture: pleasurable interest in the object."),
   ("¿Qué es *pīti*?", "Alegría, éxtasis: interés placentero por el objeto."))
AT("at-r05", 1, "philosophy", R, "Sukha (jhānaṅga)", ["at-r01", "at-v01"], ["jhana"],
   ("O que é *sukha* como fator do jhāna?", "Felicidade mental (não a sensação corporal de sukha-vedanā)."),
   ("What is *sukha* as a jhāna factor?", "Mental happiness (not the bodily feeling of sukha-vedanā)."),
   ("¿Qué es *sukha* como factor del jhāna?", "Felicidad mental (no la sensación corporal de sukha-vedanā)."))
AT("at-r06", 1, "philosophy", R, "Ekaggatā", ["at-r01"], ["jhana"],
   ("O que é *ekaggatā*?", "Unificação da mente em um único objeto (samādhi)."),
   ("What is *ekaggatā*?", "One-pointedness of mind on a single object (samādhi)."),
   ("¿Qué es *ekaggatā*?", "Unificación de la mente en un solo objeto (samādhi)."))
AT("at-r07", 1, "quantities", R, "Pañca Rūpajhāna", ["at-r01", "at-p03"], ["jhana"],
   ("Quantos jhānas de forma (rūpa-jhāna) existem e quais são?", "5: paṭhama, dutiya, tatiya, catuttha e pañcama jhāna."),
   ("How many form jhānas (rūpa-jhāna) are there and which?", "5: paṭhama, dutiya, tatiya, catuttha and pañcama jhāna."),
   ("¿Cuántos jhānas de forma (rūpa-jhāna) hay y cuáles son?", "5: paṭhama, dutiya, tatiya, catuttha y pañcama jhāna."))
AT("at-r08", 1, "structures", R, "1º Jhāna", ["at-r07", "at-r02", "at-r03", "at-r04", "at-r05", "at-r06"], ["jhana"],
   ("Quais fatores tem o 1º jhāna?", "Os 5: vitakka, vicāra, pīti, sukha e ekaggatā."),
   ("Which factors does the 1st jhāna have?", "All 5: vitakka, vicāra, pīti, sukha and ekaggatā."),
   ("¿Qué factores tiene el 1.er jhāna?", "Los 5: vitakka, vicāra, pīti, sukha y ekaggatā."))
AT("at-r09", 1, "structures", R, "2º Jhāna", ["at-r08"], ["jhana"],
   ("Quais fatores tem o 2º jhāna?", "4: vicāra, pīti, sukha e ekaggatā (abandona vitakka)."),
   ("Which factors does the 2nd jhāna have?", "4: vicāra, pīti, sukha and ekaggatā (vitakka is abandoned)."),
   ("¿Qué factores tiene el 2.º jhāna?", "4: vicāra, pīti, sukha y ekaggatā (abandona vitakka)."))
AT("at-r10", 1, "structures", R, "3º Jhāna", ["at-r09"], ["jhana"],
   ("Quais fatores tem o 3º jhāna?", "3: pīti, sukha e ekaggatā (abandona vicāra)."),
   ("Which factors does the 3rd jhāna have?", "3: pīti, sukha and ekaggatā (vicāra is abandoned)."),
   ("¿Qué factores tiene el 3.er jhāna?", "3: pīti, sukha y ekaggatā (abandona vicāra)."))
AT("at-r11", 1, "structures", R, "4º Jhāna", ["at-r10"], ["jhana"],
   ("Quais fatores tem o 4º jhāna?", "2: sukha e ekaggatā (abandona pīti)."),
   ("Which factors does the 4th jhāna have?", "2: sukha and ekaggatā (pīti is abandoned)."),
   ("¿Qué factores tiene el 4.º jhāna?", "2: sukha y ekaggatā (abandona pīti)."))
AT("at-r12", 1, "structures", R, "5º Jhāna", ["at-r11", "at-v04"], ["jhana"],
   ("Quais fatores tem o 5º jhāna?", "2: upekkhā e ekaggatā (sukha é substituído por upekkhā)."),
   ("Which factors does the 5th jhāna have?", "2: upekkhā and ekaggatā (sukha is replaced by upekkhā)."),
   ("¿Qué factores tiene el 5.º jhāna?", "2: upekkhā y ekaggatā (sukha es sustituido por upekkhā)."))
AT("at-r13", 1, "quantities", R, "Rūpāvacara-kusala", ["at-r07", "at-j02"], ["rupavacara"],
   ("Quantos rūpāvacara kusala cittas existem?", "5, um por jhāna."),
   ("How many rūpāvacara kusala cittas are there?", "5, one per jhāna."),
   ("¿Cuántos rūpāvacara kusala cittas hay?", "5, uno por jhāna."))
AT("at-r14", 1, "quantities", R, "Rūpāvacara-vipāka", ["at-r13", "at-j03"], ["rupavacara"],
   ("Quantos rūpāvacara vipāka cittas existem?", "5, o resultado dos 5 kusala."),
   ("How many rūpāvacara vipāka cittas are there?", "5, the result of the 5 kusala."),
   ("¿Cuántos rūpāvacara vipāka cittas hay?", "5, el resultado de los 5 kusala."))
AT("at-r15", 1, "quantities", R, "Rūpāvacara-kiriya", ["at-r13", "at-j04"], ["rupavacara"],
   ("Quantos rūpāvacara kiriya cittas existem e em quem surgem?", "5; surgem apenas nos Arahants."),
   ("How many rūpāvacara kiriya cittas are there and in whom do they arise?", "5; they arise only in Arahants."),
   ("¿Cuántos rūpāvacara kiriya cittas hay y en quién surgen?", "5; surgen solo en los Arahants."))
AT("at-r16", 1, "quantities", R, "Pannarasa Rūpāvacara", ["at-r13", "at-r14", "at-r15"], ["rupavacara"],
   ("Quantos rūpāvacara cittas existem e como se compõem?", "15 = 5 kusala + 5 vipāka + 5 kiriya."),
   ("How many rūpāvacara cittas are there and how are they composed?", "15 = 5 kusala + 5 vipāka + 5 kiriya."),
   ("¿Cuántos rūpāvacara cittas hay y cómo se componen?", "15 = 5 kusala + 5 vipāka + 5 kiriya."))

# ── Arūpāvacara (12) ─────────────────────────────────────────────────────────
U = "Arūpāvacara"
AT("at-u01", 1, "quantities", U, "Cattāro Arūpa", ["at-p04"], ["arupa"],
   ("Quais são as 4 esferas imateriais (arūpa)?", "Ākāsānañcāyatana, viññāṇañcāyatana, ākiñcaññāyatana e nevasaññānāsaññāyatana."),
   ("What are the 4 immaterial spheres (arūpa)?", "Ākāsānañcāyatana, viññāṇañcāyatana, ākiñcaññāyatana and nevasaññānāsaññāyatana."),
   ("¿Cuáles son las 4 esferas inmateriales (arūpa)?", "Ākāsānañcāyatana, viññāṇañcāyatana, ākiñcaññāyatana y nevasaññānāsaññāyatana."))
AT("at-u02", 1, "structures", U, "Arūpa: aṅga", ["at-u01", "at-r12"], ["arupa", "jhana"],
   ("Quais fatores tem todo jhāna arūpa?", "2: upekkhā e ekaggatā (como o 5º jhāna)."),
   ("Which factors does every arūpa jhāna have?", "2: upekkhā and ekaggatā (as the 5th jhāna)."),
   ("¿Qué factores tiene todo jhāna arūpa?", "2: upekkhā y ekaggatā (como el 5.º jhāna)."))
AT("at-u03", 1, "quantities", U, "Arūpa-kusala", ["at-u01", "at-j02"], ["arupa"],
   ("Quantos arūpāvacara kusala cittas existem?", "4, um por esfera."),
   ("How many arūpāvacara kusala cittas are there?", "4, one per sphere."),
   ("¿Cuántos arūpāvacara kusala cittas hay?", "4, uno por esfera."))
AT("at-u04", 1, "quantities", U, "Arūpa-vipāka", ["at-u03", "at-j03"], ["arupa"],
   ("Quantos arūpāvacara vipāka cittas existem?", "4, o resultado dos 4 kusala."),
   ("How many arūpāvacara vipāka cittas are there?", "4, the result of the 4 kusala."),
   ("¿Cuántos arūpāvacara vipāka cittas hay?", "4, el resultado de los 4 kusala."))
AT("at-u05", 1, "quantities", U, "Arūpa-kiriya", ["at-u03", "at-j04"], ["arupa"],
   ("Quantos arūpāvacara kiriya cittas existem e em quem surgem?", "4; surgem apenas nos Arahants."),
   ("How many arūpāvacara kiriya cittas are there and in whom do they arise?", "4; they arise only in Arahants."),
   ("¿Cuántos arūpāvacara kiriya cittas hay y en quién surgen?", "4; surgen solo en los Arahants."))
AT("at-u06", 1, "quantities", U, "Dvādasa Arūpāvacara", ["at-u03", "at-u04", "at-u05"], ["arupa"],
   ("Quantos arūpāvacara cittas existem e como se compõem?", "12 = 4 kusala + 4 vipāka + 4 kiriya."),
   ("How many arūpāvacara cittas are there and how are they composed?", "12 = 4 kusala + 4 vipāka + 4 kiriya."),
   ("¿Cuántos arūpāvacara cittas hay y cómo se componen?", "12 = 4 kusala + 4 vipāka + 4 kiriya."))
AT("at-u07", 1, "quantities", "Mahaggata", "Sattavīsati Mahaggata", ["at-r16", "at-u06"], ["mahaggata"],
   ("Quantos cittas mahaggata (sublimes) existem e como se compõem?", "27 = 15 rūpāvacara + 12 arūpāvacara."),
   ("How many mahaggata (sublime) cittas are there and how are they composed?", "27 = 15 rūpāvacara + 12 arūpāvacara."),
   ("¿Cuántos cittas mahaggata (sublimes) hay y cómo se componen?", "27 = 15 rūpāvacara + 12 arūpāvacara."))

# ── Lokuttara (8 / 40) ───────────────────────────────────────────────────────
L = "Lokuttara"
AT("at-l01", 1, "structures", L, "Cattāro Magga", ["at-p05", "at-j02"], ["lokuttara", "magga"],
   ("Quais são os 4 magga cittas (cittas do caminho)?", "Sotāpatti-, sakadāgāmi-, anāgāmi- e arahatta-magga."),
   ("What are the 4 magga cittas (path cittas)?", "Sotāpatti-, sakadāgāmi-, anāgāmi- and arahatta-magga."),
   ("¿Cuáles son los 4 magga cittas (cittas del camino)?", "Sotāpatti-, sakadāgāmi-, anāgāmi- y arahatta-magga."))
AT("at-l02", 1, "structures", L, "Cattāri Phala", ["at-l01", "at-j03"], ["lokuttara", "phala"],
   ("Quais são os 4 phala cittas (cittas do fruto)?", "Sotāpatti-, sakadāgāmi-, anāgāmi- e arahatta-phala, resultado imediato do magga correspondente."),
   ("What are the 4 phala cittas (fruition cittas)?", "Sotāpatti-, sakadāgāmi-, anāgāmi- and arahatta-phala, the immediate result of the corresponding magga."),
   ("¿Cuáles son los 4 phala cittas (cittas del fruto)?", "Sotāpatti-, sakadāgāmi-, anāgāmi- y arahatta-phala, resultado inmediato del magga correspondiente."))
AT("at-l03", 1, "quantities", L, "Aṭṭha Lokuttara", ["at-l01", "at-l02"], ["lokuttara"],
   ("Quantos cittas lokuttara existem na forma básica?", "8 = 4 magga + 4 phala."),
   ("How many lokuttara cittas are there in the basic form?", "8 = 4 magga + 4 phala."),
   ("¿Cuántos cittas lokuttara hay en la forma básica?", "8 = 4 magga + 4 phala."))
AT("at-l04", 1, "quantities", L, "Cattārīsa Lokuttara", ["at-l03", "at-r07"], ["lokuttara", "jhana"],
   ("Como os 8 lokuttara se expandem para 40?", "Cada um pode surgir com cada um dos 5 jhānas: 8 × 5 = 40."),
   ("How do the 8 lokuttara expand to 40?", "Each can arise with each of the 5 jhānas: 8 × 5 = 40."),
   ("¿Cómo se expanden los 8 lokuttara a 40?", "Cada uno puede surgir con cada uno de los 5 jhānas: 8 × 5 = 40."))
AT("at-l05", 1, "quantities", "Lokiya", "Ekāsīti Lokiya", ["at-s12", "at-u07"], ["lokiya"],
   ("Quantos cittas lokiya (mundanos) existem?", "81 = 54 kāmāvacara + 27 mahaggata."),
   ("How many lokiya (mundane) cittas are there?", "81 = 54 kāmāvacara + 27 mahaggata."),
   ("¿Cuántos cittas lokiya (mundanos) hay?", "81 = 54 kāmāvacara + 27 mahaggata."))
AT("at-l06", 1, "quantities", "Total 89 / 121", "Ekūnanavuti Citta", ["at-l05", "at-l03"], ["total"],
   ("Quantos cittas existem no total na forma básica?", "89 = 81 lokiya + 8 lokuttara."),
   ("How many cittas are there in total in the basic form?", "89 = 81 lokiya + 8 lokuttara."),
   ("¿Cuántos cittas hay en total en la forma básica?", "89 = 81 lokiya + 8 lokuttara."),
   enrichment={
     "pt": {"breakdown": ["81 lokiya = 54 kāmāvacara + 27 mahaggata", "8 lokuttara = 4 magga + 4 phala (forma básica)", "54 kāmāvacara = 12 akusala + 18 ahetuka + 24 sobhana", "27 mahaggata = 15 rūpāvacara + 12 arūpāvacara", "89 é o número canônico do Abhidhammatthasaṅgaha (forma padrão)"], "explanation": "O número 89 é a classificação fundamental dos cittas no Abhidhammattha. Deve ser memorizado com sua decomposição: 81 mundanos + 8 supramundanos. Este número é citado no próprio texto do Abhidhammatthasaṅgaha como o total padrão.", "mnemonic": "89 = 81+8. 81 = 54+27. 54 = 12+18+24. 27 = 15+12. 8 = 4+4. Memorize de baixo para cima: akusala→ahetuka→sobhana→rūpa→arūpa→lokuttara."},
     "en": {"breakdown": ["81 lokiya = 54 kāmāvacara + 27 mahaggata", "8 lokuttara = 4 magga + 4 phala (basic form)", "54 kāmāvacara = 12 akusala + 18 ahetuka + 24 sobhana", "27 mahaggata = 15 rūpāvacara + 12 arūpāvacara", "89 is the canonical number from the Abhidhammatthasaṅgaha (standard form)"], "explanation": "The number 89 is the fundamental classification of cittas in the Abhidhammattha. It must be memorized with its decomposition: 81 mundane + 8 supramundane. This number is cited in the Abhidhammatthasaṅgaha text itself as the standard total.", "mnemonic": "89 = 81+8. 81 = 54+27. 54 = 12+18+24. 27 = 15+12. 8 = 4+4. Memorize bottom-up: akusala→ahetuka→sobhana→rūpa→arūpa→lokuttara."},
     "es": {"breakdown": ["81 lokiya = 54 kāmāvacara + 27 mahaggata", "8 lokuttara = 4 magga + 4 phala (forma básica)", "54 kāmāvacara = 12 akusala + 18 ahetuka + 24 sobhana", "27 mahaggata = 15 rūpāvacara + 12 arūpāvacara", "89 es el número canónico del Abhidhammatthasaṅgaha (forma estándar)"], "explanation": "El número 89 es la clasificación fundamental de los cittas en el Abhidhammattha. Debe memorizarse con su descomposición: 81 mundanos + 8 supramundanos. Este número se cita en el propio texto del Abhidhammatthasaṅgaha como el total estándar.", "mnemonic": "89 = 81+8. 81 = 54+27. 54 = 12+18+24. 27 = 15+12. 8 = 4+4. Memorizar de abajo hacia arriba: akusala→ahetuka→sobhana→rūpa→arūpa→lokuttara."}
   })
AT("at-l07", 1, "quantities", "Total 89 / 121", "Ekavīsasatā Citta", ["at-l05", "at-l04"], ["total"],
   ("Quantos cittas existem no total na forma expandida?", "121 = 81 lokiya + 40 lokuttara."),
   ("How many cittas are there in total in the expanded form?", "121 = 81 lokiya + 40 lokuttara."),
   ("¿Cuántos cittas hay en total en la forma expandida?", "121 = 81 lokiya + 40 lokuttara."),
   enrichment={
     "pt": {"breakdown": ["121 = 81 lokiya + 40 lokuttara", "40 lokuttara = 8 cittas × 5 jhānas (associação)", "Expansão: cada um dos 8 lokuttara pode surgir com qualquer um dos 5 jhānas", "81 lokiya = mesmo número da forma básica (sem mudança)", "Ambas as formas (89 e 121) são canônicas — o Abhidhammatthasaṅgaha as menciona"], "explanation": "O número 121 surge ao expandir os 8 lokuttara básicos por sua associação com os 5 jhānas de forma — resultando em 40 lokuttara. O resultado (phala) e o nível do caminho são os mesmos; o que muda é a qualidade jhānica do citta. Esta distinção é importante para entender por que diferentes fontes citam 89 ou 121.", "mnemonic": "121 = 81+40. 40 = 8×5. Diferença entre 89 e 121: apenas os lokuttara (8 vs. 40). Pegadinha: 121 e 89 diferem em EXATAMENTE 32 cittas (40-8=32)."},
     "en": {"breakdown": ["121 = 81 lokiya + 40 lokuttara", "40 lokuttara = 8 cittas × 5 jhānas (association)", "Expansion: each of the 8 lokuttara can arise with any of the 5 jhānas", "81 lokiya = same number as the basic form (unchanged)", "Both forms (89 and 121) are canonical — the Abhidhammatthasaṅgaha mentions both"], "explanation": "The number 121 arises by expanding the 8 basic lokuttara by their association with the 5 form jhānas — yielding 40 lokuttara. The result (phala) and path level are the same; what changes is the jhānic quality of the citta. This distinction is important for understanding why different sources cite 89 or 121.", "mnemonic": "121 = 81+40. 40 = 8×5. Difference between 89 and 121: only the lokuttara (8 vs. 40). Exam trap: 121 and 89 differ by EXACTLY 32 cittas (40-8=32)."},
     "es": {"breakdown": ["121 = 81 lokiya + 40 lokuttara", "40 lokuttara = 8 cittas × 5 jhānas (asociación)", "Expansión: cada uno de los 8 lokuttara puede surgir con cualquiera de los 5 jhānas", "81 lokiya = mismo número que la forma básica (sin cambio)", "Ambas formas (89 y 121) son canónicas — el Abhidhammatthasaṅgaha las menciona"], "explanation": "El número 121 surge al expandir los 8 lokuttara básicos por su asociación con los 5 jhānas de forma — resultando en 40 lokuttara. El resultado (phala) y el nivel del camino son los mismos; lo que cambia es la calidad jhānica del citta. Esta distinción es importante para entender por qué diferentes fuentes citan 89 o 121.", "mnemonic": "121 = 81+40. 40 = 8×5. Diferencia entre 89 y 121: solo los lokuttara (8 vs. 40). Trampa: 121 y 89 difieren en EXACTAMENTE 32 cittas (40-8=32)."}
   })

# ── Classificação por raízes (hetubheda) ─────────────────────────────────────
Hb = "Hetubheda"
AT("at-c01", 1, "quantities", Hb, "Ekahetuka", ["at-a05", "at-h06"], ["hetu"],
   ("Quantos cittas ekahetuka (uma raiz) existem?", "2: os moha-mūla-cittas (somente moha)."),
   ("How many ekahetuka (one-root) cittas are there?", "2: the moha-mūla-cittas (moha only)."),
   ("¿Cuántos cittas ekahetuka (una raíz) hay?", "2: los moha-mūla-cittas (solo moha)."))
AT("at-c02", 1, "quantities", Hb, "Dvihetuka", ["at-a03", "at-a04", "at-s14", "at-s07"], ["hetu"],
   ("Quantos cittas dvihetuka (duas raízes) existem e como se compõem?", "22 = 8 lobha-mūla + 2 dosa-mūla + 12 sobhana ñāṇa-vippayutta."),
   ("How many dvihetuka (two-root) cittas are there and how are they composed?", "22 = 8 lobha-mūla + 2 dosa-mūla + 12 sobhana ñāṇa-vippayutta."),
   ("¿Cuántos cittas dvihetuka (dos raíces) hay y cómo se componen?", "22 = 8 lobha-mūla + 2 dosa-mūla + 12 sobhana ñāṇa-vippayutta."))
AT("at-c03", 1, "quantities", Hb, "Tihetuka", ["at-s15", "at-u07", "at-l03", "at-s06"], ["hetu"],
   ("Quantos cittas tihetuka (três raízes) existem e como se compõem?", "47 = 12 sobhana ñāṇa-sampayutta + 27 mahaggata + 8 lokuttara."),
   ("How many tihetuka (three-root) cittas are there and how are they composed?", "47 = 12 sobhana ñāṇa-sampayutta + 27 mahaggata + 8 lokuttara."),
   ("¿Cuántos cittas tihetuka (tres raíces) hay y cómo se componen?", "47 = 12 sobhana ñāṇa-sampayutta + 27 mahaggata + 8 lokuttara."))
AT("at-c04", 1, "quantities", Hb, "Sahetuka", ["at-c01", "at-c02", "at-c03"], ["hetu"],
   ("Quantos cittas sahetuka (com raiz) existem, na forma de 89?", "71 = 2 ekahetuka + 22 dvihetuka + 47 tihetuka."),
   ("How many sahetuka (rooted) cittas are there, counting 89?", "71 = 2 ekahetuka + 22 dvihetuka + 47 tihetuka."),
   ("¿Cuántos cittas sahetuka (con raíz) hay, en la forma de 89?", "71 = 2 ekahetuka + 22 dvihetuka + 47 tihetuka."))
AT("at-c05", 1, "quantities", Hb, "89 = 18 + 71", ["at-k16", "at-c04", "at-l06"], ["hetu", "total"],
   ("Como os 89 cittas se dividem pela presença de raízes?", "89 = 18 ahetuka + 71 sahetuka."),
   ("How do the 89 cittas divide by presence of roots?", "89 = 18 ahetuka + 71 sahetuka."),
   ("¿Cómo se dividen los 89 cittas según la presencia de raíces?", "89 = 18 ahetuka + 71 sahetuka."))

# ── Cartões de síntese (os 63 antigos, ricos) inseridos no grafo ─────────────
# id -> (requisitos, inserir depois de). Cada síntese fica no ponto do currículo em
# que todos os seus alicerces já foram consolidados.
CAPSTONE_PLAN = {
    "ch1-01": (["at-t01", "at-t02", "at-t03", "at-t04", "at-t05"], "at-t05"),
    "ch1-03": (["at-a17", "at-a16", "at-a06", "at-a07"], "at-a17"),
    "ch1-13": (["at-a16", "at-a03"], "at-a17"),
    "ch1-14": (["at-a06", "at-a07"], "at-a17"),
    "ch1-12": (["at-k08"], "at-k08"),
    "ch1-11": (["at-k12", "at-k13", "at-k14", "at-k15"], "at-k15"),
    "ch1-04": (["at-k16", "at-k11", "at-k12"], "at-k16"),
    "ch1-05": (["at-s10", "at-s05"], "at-s10"),
    "ch1-06": (["at-r16", "at-r12"], "at-r16"),
    "ch1-07": (["at-u06", "at-u02"], "at-u06"),
    "ch1-08": (["at-l04"], "at-l04"),
    "ch1-02": (["at-l06", "at-l07"], "at-l07"),
    "ch1-09": (["at-l07", "at-v01"], "at-l07"),
    "ch1-15": (["at-l07", "at-v03", "at-a13"], "at-l07"),
    "ch1-10": (["at-c04", "at-c05"], "at-c05"),
}


def main() -> None:
    legacy = json.loads((ROOT / "src/data/ankiCards.json").read_text(encoding="utf-8"))
    chapter_of = {c["id"]: c["chapter"] for c in legacy}
    legacy_ids = [c["id"] for c in legacy]

    atom_ids = {c[0] for c in C}
    assert len(atom_ids) == len(C), "ids duplicados"
    atom_pos = {c[0]: i for i, c in enumerate(C)}
    for c in C:
        assert c[0].startswith("at-")
        for r in c[6]:
            assert r in atom_ids and atom_pos[r] < atom_pos[c[0]], f"requisito inválido {c[0]}->{r}"
        chapter_of[c[0]] = c[1]

    # Currículo: átomos na ordem de autoria; cada síntese logo após o seu alicerce final.
    curriculum: list[str] = []
    for c in C:
        curriculum.append(c[0])
        for cap, (_req, after) in CAPSTONE_PLAN.items():
            if after == c[0]:
                curriculum.append(cap)
    placed = set(curriculum)
    for cap, (req, _after) in CAPSTONE_PLAN.items():
        assert cap in placed and cap in chapter_of, cap
        for r in req:
            assert r in atom_ids and curriculum.index(r) < curriculum.index(cap), f"{cap} -> {r}"

    capstone_requires = {cap: req for cap, (req, _a) in CAPSTONE_PLAN.items()}

    # Capítulos 2–9 ainda não atomizados: cada um só abre depois do capítulo anterior.
    rest = sorted((i for i in legacy_ids if i not in placed),
                  key=lambda i: (chapter_of[i], legacy_ids.index(i)))
    assert all(chapter_of[i] >= 2 for i in rest), "sobrou cartão do capítulo 1 sem plano"
    for cid in rest:
        k = chapter_of[cid]
        gate = [i for i in curriculum if chapter_of[i] == k - 1 and not i.startswith("at-")][-1]
        capstone_requires[cid] = [gate]
        curriculum.append(cid)
    assert set(curriculum) == atom_ids | set(legacy_ids) and len(curriculum) == len(set(curriculum))

    cards = []
    for id_, ch, cat, sec, pali, _layer, req, tags, langs, enrichment in C:
        card = {"id": id_, "chapter": ch, "chapterName": CHAPTER_NAMES[ch], "section": sec,
                "category": cat, "paliTerm": pali, "tags": tags, "requires": req}
        for lg, (q, a) in langs.items():
            enrich = enrichment.get(lg, {})
            card[lg] = {"question": q, "answer": a,
                        "breakdown": enrich.get("breakdown", []),
                        "explanation": enrich.get("explanation", ""),
                        "mnemonicOrExamTip": enrich.get("mnemonic", ""),
                        "examQuestionType": {"pt": "Atômico", "es": "Atómico"}.get(lg, "Atomic")}
        cards.append(card)

    TS_PATH.write_text(
        "// src/data/ankiAtomicCards.ts\n"
        "// GERADO por scripts/build_atomic_cards.py — não edite à mão.\n"
        "import type { AnkiCard } from './ankiCards';\n\n"
        "/** Cartões atômicos (1 fato cada). `requires` = alicerces que formam o cartão. */\n"
        "export const ATOMIC_CARDS: AnkiCard[] = " + json.dumps(cards, ensure_ascii=False, indent=2) + ";\n\n"
        "/** Pré-requisitos dos cartões de síntese (os 63 cartões antigos). */\n"
        "export const CAPSTONE_REQUIRES: Record<string, string[]> = "
        + json.dumps(capstone_requires, ensure_ascii=False, indent=2) + ";\n\n"
        "/** Ordem do currículo: do mais básico ao mais composto. */\n"
        "export const CURRICULUM_ORDER: string[] = " + json.dumps(curriculum, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )
    print(f"{len(cards)} atômicos + {len(legacy_ids)} sínteses = {len(curriculum)} cartões")


if __name__ == "__main__":
    main()

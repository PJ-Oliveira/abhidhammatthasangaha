#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the enriched, canonical Abhidhamma Pāli Dictionary (`src/data/paliDictionary.json`)
by merging:
  1. PART1_ENTRIES (Ontology, 4 Paramatthas, Ch. I Citta classifications & formulas)
  2. PART2_ENTRIES (Ch. II: All 52 Cetasikas & groups with Lakkhaṇādi-catukka)
  3. PART3_ENTRIES (Ch. VI: All 28 Rūpas, Kalāpas & origins with Lakkhaṇādi-catukka)
  4. PART4A_ENTRIES (Chs. III, IV, V: 14 Kiccas, Dvāra, Ārammaṇa, Vatthu, Vīthi, Vīthimutta)
  5. PART4B_ENTRIES (Chs. V, VII, VIII, IX: Bhūmi, Kamma, Vedanā, Āsava, Nīvaraṇa, Kilesa, Paccaya, Paṭṭhāna, Paṭiccasamuppāda, Samatha, Vipassanā, Kammaṭṭhāna, Visuddhi)
  6. PART4C_ENTRIES & PART4D_ENTRIES (Dhamma, Nāma, Hetu, Magga, Phala, Khandha, Āyatana, Dhātu, Sacca, Indriya, Upādāna, Anusaya, Saṃyojana, Bodhipakkhiya, Avijjā, Taṇhā, Nimitta, Tilakkhaṇa)
  7. Additional Sangaha compound terms, the 24 Paṭṭhāna conditions, insight knowledges, and chapter tokens.
"""

import json
import glob
import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from abhidhamma_lexicon_part1 import PART1_ENTRIES
from abhidhamma_lexicon_part2 import PART2_ENTRIES
from abhidhamma_lexicon_part3 import PART3_ENTRIES
from abhidhamma_lexicon_part4a import PART4A_ENTRIES
from abhidhamma_lexicon_part4b import PART4B_ENTRIES
from abhidhamma_lexicon_part4c import PART4C_ENTRIES
from abhidhamma_lexicon_part4d import PART4D_ENTRIES

DICT_PATH = "src/data/paliDictionary.json"
CHAPTERS_DIR = "src/data/chapters"

# 24 Paṭṭhāna Conditions (CMA VIII §§17–27, pp. 308–322)
PATTHANA_24 = [
    ("hetupaccaya", "hetu", "Condição-raiz (Hetu-paccaya): 1ª das 24 condições do Paṭṭhāna, pela qual as 6 raízes (lobha, dosa, moha, alobha, adosa, amoha) conferem firmeza e estabilidade aos estados mentais e materiais co-nascidos.", "Root condition (Hetu-paccaya): 1st of the 24 Paṭṭhāna conditions, whereby the 6 roots impart firmness and stability to conascent mental and material states.", "Condición-raíz (Hetu-paccaya): 1ª de las 24 condiciones del Paṭṭhāna, por la cual las 6 raíces confieren firmeza y estabilidad a los estados co-nacidos.", "CMA VIII §17 (p. 308)"),
    ("ārammaṇapaccaya", "ārammaṇa", "Condição-objeto (Ārammaṇa-paccaya): 2ª das 24 condições do Paṭṭhāna, pela qual qualquer realidade ou conceito serve de suporte objetivo para o surgimento de citta e cetasikas.", "Object condition (Ārammaṇa-paccaya): 2nd of the 24 Paṭṭhāna conditions, whereby any reality or concept serves as the objective support for the arising of citta and cetasikas.", "Condición-objeto (Ārammaṇa-paccaya): 2ª de las 24 condiciones del Paṭṭhāna, por la cual un objeto sostiene el surgimiento de citta y cetasikas.", "CMA VIII §18 (p. 309)"),
    ("adhipatipaccaya", "adhipati", "Condição de predominância (Adhipati-paccaya): 3ª das 24 condições do Paṭṭhāna, operando como predominância de objeto (ārammaṇādhipati) ou co-nascida (sahajātādhipati: chanda, vīriya, citta, vīmaṃsā).", "Predominance condition (Adhipati-paccaya): 3rd of the 24 Paṭṭhāna conditions, operating as object-predominance or conascence-predominance (chanda, vīriya, citta, vīmaṃsā).", "Condición de predominancia (Adhipati-paccaya): 3ª de las 24 condiciones del Paṭṭhāna, operando como predominancia de objeto o co-nacida.", "CMA VIII §19 (p. 310)"),
    ("anantarapaccaya", "anantara", "Condição de proximidade (Anantara-paccaya): 4ª das 24 condições do Paṭṭhāna, pela qual cada citta que cessa condiciona o surgimento imediato da citta seguinte no fluxo mental sem intervalo.", "Proximity condition (Anantara-paccaya): 4th of the 24 Paṭṭhāna conditions, whereby each ceasing citta conditions the immediate arising of the next citta in the mental stream without gap.", "Condición de proximidad (Anantara-paccaya): 4ª de las 24 condiciones del Paṭṭhāna, por la cual cada citta que cesa condiciona la siguiente sin intervalo.", "CMA VIII §13 (p. 305)"),
    ("samanantarapaccaya", "samanantara", "Condição de contiguidade (Samanantara-paccaya): 5ª das 24 condições do Paṭṭhāna, idêntica em referentes à condição de proximidade, enfatizando a continuidade perfeita da sucessão mental.", "Contiguity condition (Samanantara-paccaya): 5th of the 24 Paṭṭhāna conditions, identical in referents to proximity condition, emphasizing seamless mental succession.", "Condición de contigüidad (Samanantara-paccaya): 5ª de las 24 condiciones del Paṭṭhāna, que enfatiza la sucesión continua de la mente.", "CMA VIII §13 (p. 305)"),
    ("sahajātapaccaya", "sahajāta", "Condição de co-nascença (Sahajāta-paccaya): 6ª das 24 condições do Paṭṭhāna, pela qual um fenômeno, ao surgir, faz surgir simultaneamente consigo os fenômenos dependentes (como uma lâmpada e sua luz).", "Conascence condition (Sahajāta-paccaya): 6th of the 24 Paṭṭhāna conditions, whereby a phenomenon, in arising, causes dependent phenomena to arise simultaneously with itself.", "Condición de co-nacencia (Sahajāta-paccaya): 6ª de las 24 condiciones del Paṭṭhāna, por la cual un fenómeno hace surgir simultáneamente consigo a otros.", "CMA VIII §15 (p. 306)"),
    ("aññamaññapaccaya", "aññamañña", "Condição de reciprocidade ou mutualidade (Aññamañña-paccaya): 7ª das 24 condições do Paṭṭhāna, pela qual estados co-nascidos sustentam-se mutuamente como um tripé (ex.: os 4 agregados mentais ou os 4 mahābhūtas).", "Mutuality condition (Aññamañña-paccaya): 7th of the 24 Paṭṭhāna conditions, whereby conascent states mutually support one another like a tripod (e.g., the 4 mental aggregates or 4 mahābhūtas).", "Condición de reciprocidad o mutualidad (Aññamañña-paccaya): 7ª de las 24 condiciones del Paṭṭhāna, por la cual los estados co-nacidos se sostienen mutuamente como un trípode.", "CMA VIII §15 (p. 306)"),
    ("nissayapaccaya", "nissaya", "Condição de suporte (Nissaya-paccaya): 8ª das 24 condições do Paṭṭhāna, pela qual um estado serve de base ou fundação para outro (seja por co-nascença ou por pré-nascença da base física).", "Support condition (Nissaya-paccaya): 8th of the 24 Paṭṭhāna conditions, whereby one state serves as foundation or support for another (by conascence or base-prenascence).", "Condición de soporte (Nissaya-paccaya): 8ª de las 24 condiciones del Paṭṭhāna, por la cual un estado sirve de base o fundamento para otro.", "CMA VIII §15–16 (pp. 306–307)"),
    ("upanissayapaccaya", "upanissaya", "Condição de suporte decisivo (Upanissaya-paccaya): 9ª das 24 condições do Paṭṭhāna, abrangendo o suporte decisivo de objeto, de proximidade e natural (pakatūpanissaya).", "Decisive support condition (Upanissaya-paccaya): 9th of the 24 Paṭṭhāna conditions, comprising object-decisive, proximity-decisive, and natural decisive support (pakatūpanissaya).", "Condición de soporte decisivo (Upanissaya-paccaya): 9ª de las 24 condiciones del Paṭṭhāna (de objeto, de proximidad y natural).", "CMA VIII §18 (pp. 309–310)"),
    ("purejātapaccaya", "purejāta", "Condição de pré-nascença (Purejāta-paccaya): 10ª das 24 condições do Paṭṭhāna, pela qual um fenômeno material surgido antes (as 6 bases físicas ou os 5 objetos sensoriais presentes) condiciona a consciência subsequente.", "Prenascence condition (Purejāta-paccaya): 10th of the 24 Paṭṭhāna conditions, whereby pre-arisen material phenomena (the 6 physical bases or 5 present sense objects) condition subsequent mentality.", "Condición de pre-nacencia (Purejāta-paccaya): 10ª de las 24 condiciones del Paṭṭhāna, por la cual la materia surgida antes condiciona la mente posterior.", "CMA VIII §16 (p. 307)"),
    ("pacchājātapaccaya", "pacchājāta", "Condição de pós-nascença (Pacchājāta-paccaya): 11ª das 24 condições do Paṭṭhāna, pela qual citta e cetasikas surgidos posteriormente sustentam e preservam os fenômenos materiais do corpo surgidos antes.", "Postnascence condition (Pacchājāta-paccaya): 11th of the 24 Paṭṭhāna conditions, whereby subsequently arisen citta and cetasikas support and preserve previously arisen bodily material phenomena.", "Condición de pos-nacencia (Pacchājāta-paccaya): 11ª de las 24 condiciones del Paṭṭhāna, por la cual la mente surgida después sostiene la materia corporal previa.", "CMA VIII §14 (p. 306)"),
    ("āsevanapaccaya", "āsevana", "Condição de repetição (Āsevana-paccaya): 12ª das 24 condições do Paṭṭhāna, pela qual cada momento de javana mundano fortalece e infunde perícia no momento de javana seguinte da mesma qualidade ética.", "Repetition condition (Āsevana-paccaya): 12th of the 24 Paṭṭhāna conditions, whereby each mundane javana moment strengthens and imparts proficiency to the succeeding javana of the same ethical quality.", "Condición de repetición (Āsevana-paccaya): 12ª de las 24 condiciones del Paṭṭhāna, por la cual cada momento de javana mundano fortalece al siguiente.", "CMA VIII §13 (p. 305)"),
    ("kammapaccaya", "kamma", "Condição de kamma (Kamma-paccaya): 13ª das 24 condições do Paṭṭhāna, operando como volição co-nascida (sahajāta-kamma) ou como kamma assíncrono passado (nānākkhaṇika-kamma) que produz vipāka e katattārūpa.", "Kamma condition (Kamma-paccaya): 13th of the 24 Paṭṭhāna conditions, operating as conascent volition (sahajāta-kamma) or asynchronous past kamma (nānākkhaṇika-kamma) producing vipāka and katattārūpa.", "Condición de kamma (Kamma-paccaya): 13ª de las 24 condiciones del Paṭṭhāna, operando como volición co-nacida o como kamma pasado asíncrono.", "CMA VIII §20 (p. 312)"),
    ("vipākapaccaya", "vipāka", "Condição de resultante (Vipāka-paccaya): 14ª das 24 condições do Paṭṭhāna, pela qual cittas e cetasikas resultantes (vipāka), por sua quietude passiva e sem esforço, tranquilizam uns aos outros.", "Resultant condition (Vipāka-paccaya): 14th of the 24 Paṭṭhāna conditions, whereby resultant cittas and cetasikas, through their effortless passive quietude, mutually tranquillize one another.", "Condición de resultante (Vipāka-paccaya): 14ª de las 24 condiciones del Paṭṭhāna, por la cual los estados resultantes se apaciguan mutuamente sin esfuerzo.", "CMA VIII §15 (p. 307)"),
    ("āhārapaccaya", "āhāra", "Condição de nutrimento (Āhāra-paccaya): 15ª das 24 condições do Paṭṭhāna, abrangendo o nutrimento material (ojā) e os 3 nutrimentos mentais (phassa, manosañcetanā e viññāṇa).", "Nutriment condition (Āhāra-paccaya): 15th of the 24 Paṭṭhāna conditions, comprising material nutriment (ojā) and the 3 mental nutriments (phassa, manosañcetanā, and viññāṇa).", "Condición de nutrimento (Āhāra-paccaya): 15ª de las 24 condiciones del Paṭṭhāna, que abarca el nutrimento material (ojā) y los 3 nutrimentos mentales.", "CMA VIII §21 (p. 313)"),
    ("indriyapaccaya", "indriya", "Condição de faculdade (Indriya-paccaya): 16ª das 24 condições do Paṭṭhāna, pela qual as faculdades governantes exercem controle soberano sobre os estados associados e materiais.", "Faculty condition (Indriya-paccaya): 16th of the 24 Paṭṭhāna conditions, whereby governing faculties exercise sovereign control over associated and material states.", "Condición de facultad (Indriya-paccaya): 16ª de las 24 condiciones del Paṭṭhāna, por la cual las facultades ejercen control soberano.", "CMA VIII §22 (p. 314)"),
    ("jhānapaccaya", "jhāna", "Condição de jhāna (Jhāna-paccaya): 17ª das 24 condições do Paṭṭhāna, pela qual os 5 fatores de jhāna (vitakka, vicāra, pīti, vedanā, ekaggatā) capacitam a mente a contemplar intimamente o objeto.", "Jhāna condition (Jhāna-paccaya): 17th of the 24 Paṭṭhāna conditions, whereby the 5 jhāna factors (vitakka, vicāra, pīti, vedanā, ekaggatā) enable the mind to closely examine its object.", "Condición de jhāna (Jhāna-paccaya): 17ª de las 24 condiciones del Paṭṭhāna, por la cual los 5 factores de jhāna fijan la mente en el objeto.", "CMA VIII §23 (p. 315)"),
    ("maggapaccaya", "magga", "Condição de caminho (Magga-paccaya): 18ª das 24 condições do Paṭṭhāna, pela qual os 12 fatores de caminho (8 corretos e 4 incorretos) conduzem a um destino específico (saṃsāra ou Nibbāna).", "Path condition (Magga-paccaya): 18th of the 24 Paṭṭhāna conditions, whereby the 12 path factors (8 right and 4 wrong) lead toward a specific destination.", "Condición de sendero (Magga-paccaya): 18ª de las 24 condiciones del Paṭṭhāna, por la cual los 12 factores de sendero conducen a su destino.", "CMA VIII §24 (p. 315)"),
    ("sampayuttapaccaya", "sampayutta", "Condição de associação (Sampayutta-paccaya): 19ª das 24 condições do Paṭṭhāna, pela qual citta e cetasikas associam-se intimamente compartilhando mesma base, mesmo objeto, surgimento e cessação simultâneos.", "Association condition (Sampayutta-paccaya): 19th of the 24 Paṭṭhāna conditions, whereby citta and cetasikas intimately associate by sharing the same base, same object, simultaneous arising, and simultaneous cessation.", "Condición de asociación (Sampayutta-paccaya): 19ª de las 24 condiciones del Paṭṭhāna, por la cual citta y cetasikas comparten base, objeto, surgimiento y cesación.", "CMA VIII §15 (p. 307)"),
    ("vippayuttapaccaya", "vippayutta", "Condição de dissociação (Vippayutta-paccaya): 20ª das 24 condições do Paṭṭhāna, pela qual fenômenos mentais (nāma) e materiais (rūpa) assistem-se mutuamente mantendo suas naturezas distintas sem se fundirem.", "Dissociation condition (Vippayutta-paccaya): 20th of the 24 Paṭṭhāna conditions, whereby mental (nāma) and material (rūpa) phenomena assist one another while remaining distinct in nature.", "Condición de disociación (Vippayutta-paccaya): 20ª de las 24 condiciones del Paṭṭhāna, por la cual nāma y rūpa se asisten sin mezclarse.", "CMA VIII §25 (p. 316)"),
    ("atthipaccaya", "atthi", "Condição de presença (Atthi-paccaya): 21ª das 24 condições do Paṭṭhāna, pela qual um fenômeno condiciona outro enquanto ambos estão presentes simultaneamente (por co-nascença, pré-nascença, pós-nascença, nutrimento ou faculdade).", "Presence condition (Atthi-paccaya): 21st of the 24 Paṭṭhāna conditions, whereby a phenomenon conditions another while remaining present simultaneously.", "Condición de presencia (Atthi-paccaya): 21ª de las 24 condiciones del Paṭṭhāna, por la cual un fenómeno condiciona a otro mediante su presencia actual.", "CMA VIII §26 (p. 317)"),
    ("natthipaccaya", "natthi", "Condição de ausência (Natthi-paccaya): 22ª das 24 condições do Paṭṭhāna, pela qual uma citta, ao cessar e tornar-se ausente, abre espaço para o surgimento imediato da citta seguinte.", "Absence condition (Natthi-paccaya): 22nd of the 24 Paṭṭhāna conditions, whereby a citta, by ceasing and becoming absent, makes room for the immediate arising of the next citta.", "Condición de ausencia (Natthi-paccaya): 22ª de las 24 condiciones del Paṭṭhāna, por la cual una citta al cesar abre paso a la siguiente.", "CMA VIII §13 (p. 305)"),
    ("vigatapaccaya", "vigata", "Condição de desaparecimento (Vigata-paccaya): 23ª das 24 condições do Paṭṭhāna, idêntica em referentes à condição de ausência, enfatizando o desaparecimento completo da citta precedente.", "Disappearance condition (Vigata-paccaya): 23rd of the 24 Paṭṭhāna conditions, identical in referents to absence condition, emphasizing the complete disappearance of the preceding citta.", "Condición de desaparición (Vigata-paccaya): 23ª de las 24 condiciones del Paṭṭhāna, idéntica a la condición de ausencia.", "CMA VIII §13 (p. 305)"),
    ("avigatapaccaya", "avigata", "Condição de não-desaparecimento (Avigata-paccaya): 24ª das 24 condições do Paṭṭhāna, idêntica em referentes à condição de presença (atthipaccaya), encerrando a grande matriz condicional.", "Non-disappearance condition (Avigata-paccaya): 24th of the 24 Paṭṭhāna conditions, identical in referents to presence condition (atthipaccaya), concluding the great conditional matrix.", "Condición de no-desaparición (Avigata-paccaya): 24ª de las 24 condiciones del Paṭṭhāna, idéntica a la condición de presencia.", "CMA VIII §26 (p. 317)"),
]

def build_patthana_entries():
    entries = {}
    for key, first_part, pt_def, en_def, es_def, ref in PATTHANA_24:
        entry = {
            "pali": key,
            "tier": 1,
            "meaning": {"pt": pt_def, "en": en_def, "es": es_def},
            "grammar": "masc. (composto tappurisa / kammadhāraya)",
            "grammarLocalized": {
                "pt": f"Substantivo masculino composto ({first_part} + paccaya)",
                "en": f"Masculine compound noun ({first_part} + paccaya)",
                "es": f"Sustantivo masculino compuesto ({first_part} + paccaya)"
            },
            "root": f"{first_part} + paṭi + √i + a (paccaya)",
            "samasa": {
                "type": {
                    "pt": "Composto Determinativo (Kammadhāraya / Tappurisa)",
                    "en": "Determinative Compound (Kammadhāraya / Tappurisa)",
                    "es": "Compuesto Determinativo (Kammadhāraya / Tappurisa)"
                },
                "viggaha": f"{first_part} ca so paccayo cā ti {key}o",
                "literal": {
                    "pt": f"Condição (paccaya) que opera pelo modo de {first_part}.",
                    "en": f"Condition (paccaya) operating by way of {first_part}.",
                    "es": f"Condición (paccaya) que opera a modo de {first_part}."
                },
                "parts": [
                    {"part": first_part, "gloss": {"pt": first_part, "en": first_part, "es": first_part}},
                    {"part": "paccaya", "gloss": {"pt": "condição / suporte causal", "en": "condition / causal support", "es": "condición / soporte causal"}}
                ]
            },
            "abhidhamma": {
                "ontology": {
                    "pt": "Força Condicionante do Paṭṭhāna (Paccayasatti — Cap. VIII)",
                    "en": "Conditioning Force of the Paṭṭhāna (Paccayasatti — Ch. VIII)",
                    "es": "Fuerza Condicionante del Paṭṭhāna (Paccayasatti — Cap. VIII)"
                },
                "category": {
                    "pt": "As 24 Condições do Método Paṭṭhāna (Cap. VIII, §§11–27)",
                    "en": "The 24 Conditions of the Paṭṭhāna Method (Ch. VIII, §§11–27)",
                    "es": "Las 24 Condiciones del Método Paṭṭhāna (Cap. VIII, §§11–27)"
                },
                "philosophy": {"pt": pt_def, "en": en_def, "es": es_def},
                "bodhiRef": ref
            },
            "seeAlso": ["paccaya", "paṭṭhāna", "paṭiccasamuppāda"]
        }
        entries[key] = entry
    return entries

# Additional high-frequency Sangaha compounds and technical terms
EXTRA_SANGAHA_ENTRIES = {
    "saṅgaha": {
        "meaning": {
            "pt": "Compêndio, síntese, compilação ou agrupamento sistemático; no Abhidhammattha Saṅgaha, a reunião metódica das realidades últimas em grupos categóricos",
            "en": "Compendium, synthesis, compilation, or systematic grouping; in the Abhidhammattha Saṅgaha, the methodical gathering of ultimate realities into categorical groups",
            "es": "Compendio, síntesis, compilación o agrupación sistemática; en el Abhidhammattha Saṅgaha, la reunión metódica de las realidades últimas en grupos categoriales"
        },
        "grammar": "masc. (saṃ + √gah + a)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (saṃ 'junto' + √gah 'tomar, reunir, compendiar')",
            "en": "Masculine noun (saṃ 'together' + √gah 'to hold, gather, compile')",
            "es": "Sustantivo masculino (saṃ 'junto' + √gah 'tomar, reunir, compendiar')"
        },
        "root": "saṃ + √gah (reunir, abarcar) + -a",
        "abhidhamma": {
            "ontology": {"pt": "Método Taxonômico Exegético (Saṅgahanaya)", "en": "Exegetical Taxonomic Method (Saṅgahanaya)", "es": "Método Taxonómico Exegético (Saṅgahanaya)"},
            "category": {"pt": "Estrutura dos 9 Capítulos do Abhidhammattha Saṅgaha", "en": "Structure of the 9 Chapters of the Abhidhammattha Saṅgaha", "es": "Estructura de los 9 Capítulos del Abhidhammattha Saṅgaha"},
            "philosophy": {
                "pt": "Cada um dos 9 capítulos do tratado de Ācariya Anuruddha é intitulado um 'Saṅgaha-vibhāga' (Divisão do Compêndio): (1) Citta, (2) Cetasika, (3) Pakiṇṇaka, (4) Vīthi, (5) Vīthimutta, (6) Rūpa, (7) Samuccaya, (8) Paccaya e (9) Kammaṭṭhāna.",
                "en": "Each of the 9 chapters of Ācariya Anuruddha's treatise is titled a 'Saṅgaha-vibhāga' (Compendium Division): (1) Citta, (2) Cetasika, (3) Pakiṇṇaka, (4) Vīthi, (5) Vīthimutta, (6) Rūpa, (7) Samuccaya, (8) Paccaya, and (9) Kammaṭṭhāna.",
                "es": "Cada uno de los 9 capítulos del tratado de Ācariya Anuruddha se titula 'Saṅgaha-vibhāga' (División del Compendio)."
            },
            "bodhiRef": "CMA I §1 (p. 25)"
        },
        "seeAlso": ["abhidhammatthasaṅgaha", "paramattha", "citta", "cetasika", "rūpa", "nibbāna"]
    },
    "cittacetasika": {
        "meaning": {
            "pt": "Consciência e fatores mentais; a totalidade dos estados mentais condicionados (nāma condicionado), que surgem e cessam inseparavelmente juntos (ekuppādanirodhā)",
            "en": "Consciousness and mental factors; the totality of conditioned mental states (conditioned nāma), which arise and cease inseparably together (ekuppādanirodhā)",
            "es": "Conciencia y factores mentales; la totalidad de los estados mentales condicionados (nāma condicionado), que surgen y cesan inseparablemente juntos (ekuppādanirodhā)"
        },
        "grammar": "masc. pl. (composto dvanda: citta + cetasika)",
        "grammarLocalized": {
            "pt": "Composto Coordenativo Copulativo (Itaritara-Dvanda: citta + cetasika)",
            "en": "Copulative Coordinative Compound (Itaritara-Dvanda: citta + cetasika)",
            "es": "Compuesto Coordinativo Copulativo (Itaritara-Dvanda: citta + cetasika)"
        },
        "root": "√cit (conhecer) + ta + cetas + ika",
        "samasa": {
            "type": {"pt": "Composto Coordenativo (Itaritara-Dvanda)", "en": "Coordinative Compound (Itaritara-Dvanda)", "es": "Compuesto Coordinativo (Itaritara-Dvanda)"},
            "viggaha": "cittañ ca cetasikā ca = cittacetasikā",
            "literal": {"pt": "consciência (citta) e fatores mentais (cetasikas)", "en": "consciousness (citta) and mental factors (cetasikas)", "es": "conciencia (citta) y factores mentales (cetasikas)"},
            "parts": [
                {"part": "citta", "gloss": {"pt": "consciência (89/121)", "en": "consciousness (89/121)", "es": "conciencia (89/121)"}},
                {"part": "cetasika", "gloss": {"pt": "fatores mentais (52)", "en": "mental factors (52)", "es": "factores mentales (52)"}}
            ]
        },
        "abhidhamma": {
            "ontology": {"pt": "1ª e 2ª Realidades Últimas (Citta 89/121 + Cetasika 52)", "en": "1st & 2nd Ultimate Realities (Citta 89/121 + Cetasika 52)", "es": "1ª y 2ª Realidades Últimas (Citta 89/121 + Cetasika 52)"},
            "category": {"pt": "Os 4 Agregados Mentais (Nāmakkhandhā — Cap. II, §1)", "en": "The 4 Mental Aggregates (Nāmakkhandhā — Ch. II, §1)", "es": "Los 4 Agregados Mentales (Nāmakkhandhā — Cap. II, §1)"},
            "philosophy": {
                "pt": "Citta e cetasikas jamais ocorrem isolados um do outro: pela abertura do Cap. II ('Ekuppādanirodhā ca ekālambanavatthukā'), compartilham 4 marcas de associação (sampayutta): (1) surgimento simultâneo, (2) cessação simultânea, (3) mesmo objeto e (4) mesma base física.",
                "en": "Citta and cetasikas never occur in isolation from one another: per the opening verse of Ch. II ('Ekuppādanirodhā ca ekālambanavatthukā'), they share 4 marks of association (sampayutta): (1) simultaneous arising, (2) simultaneous cessation, (3) same object, and (4) same physical base.",
                "es": "Citta y cetasikas jamás ocurren aislados: según el verso inicial del Cap. II ('Ekuppādanirodhā ca ekālambanavatthukā'), comparten 4 marcas de asociación (sampayutta): mismo surgimiento, misma cesación, mismo objeto y misma base física."
            },
            "bodhiRef": "CMA II §1 (pp. 76–77); VIII §15 (p. 307)"
        },
        "seeAlso": ["citta", "cetasika", "nāma", "khandha"]
    },
    "udayabbayañāṇa": {
        "meaning": {
            "pt": "Conhecimento da contemplação do surgimento e cessação; o 1º dos 9 conhecimentos superiores de insight (vipassanā-ñāṇa) na Purificação pelo Conhecimento e Visão do Caminho e Não-Caminho e do Progresso (Cap. IX, §§33–34)",
            "en": "Knowledge of contemplation of rise and fall; the 1st of the 9 higher insight knowledges (vipassanā-ñāṇa) in the Purification by Knowledge and Vision of the Course of Practice (Ch. IX, §§33–34)",
            "es": "Conocimiento de la contemplación del surgimiento y la cesación; el 1º de los 9 conocimientos superiores de insight (vipassanā-ñāṇa) (Cap. IX, §§33–34)"
        },
        "grammar": "nt. (udaya + vaya + ñāṇa)",
        "grammarLocalized": {
            "pt": "Substantivo neutro composto (udaya 'surgimento' + vaya 'cessação' + ñāṇa 'conhecimento')",
            "en": "Neuter compound noun (udaya 'rise' + vaya 'fall' + ñāṇa 'knowledge')",
            "es": "Sustantivo neutro compuesto (udaya 'surgimiento' + vaya 'cesación' + ñāṇa 'conocimiento')"
        },
        "root": "ud + √i (udaya) + vi + √i (vaya) + √ñā (ñāṇa)",
        "samasa": {
            "type": {"pt": "Dvanda + Chaṭṭhī-Tappurisa", "en": "Dvanda + Genitive Tappurisa", "es": "Dvanda + Tappurisa Genitivo"},
            "viggaha": "udayo ca vayo ca = udayabbayaṃ; udayabbayassa ñāṇaṃ = udayabbayañāṇaṃ",
            "literal": {"pt": "conhecimento (ñāṇa) da ascensão/surgimento (udaya) e queda/cessação (vaya)", "en": "knowledge (ñāṇa) of rise/arising (udaya) and fall/passing away (vaya)", "es": "conocimiento (ñāṇa) del surgimiento (udaya) y la caída/cesación (vaya)"},
            "parts": [
                {"part": "udaya", "gloss": {"pt": "surgimento / ascensão", "en": "arising / rise", "es": "surgimiento / ascenso"}},
                {"part": "vaya", "gloss": {"pt": "cessação / declínio", "en": "passing away / fall", "es": "cesación / caída"}},
                {"part": "ñāṇa", "gloss": {"pt": "conhecimento de insight", "en": "insight knowledge", "es": "conocimiento de insight"}}
            ]
        },
        "abhidhamma": {
            "ontology": {"pt": "Realidade Última (Cetasika: Paññindriya)", "en": "Ultimate Reality (Cetasika: Paññindriya)", "es": "Realidad Última (Cetasika: Paññindriya)"},
            "category": {"pt": "10 Conhecimentos de Insight (Vipassanāñāṇa — Cap. IX, §§24 & 33–34)", "en": "10 Insight Knowledges (Vipassanāñāṇa — Ch. IX, §§24 & 33–34)", "es": "10 Conocimientos de Insight (Vipassanāñāṇa — Cap. IX, §§24 y 33–34)"},
            "philosophy": {
                "pt": "Em sua fase terna, pode fazer surgir as 10 imperfeições do insight (vipassanūpakkilesa: obhāsa/luz, pīti, passaddhi, etc.). Quando o meditador discerne que essas imperfeições não são o caminho (5ª visuddhi), retoma udayabbayañāṇa em sua fase madura, ingressando na 6ª purificação (paṭipadāñāṇadassanavisuddhi).",
                "en": "In its tender phase, it may give rise to the 10 imperfections of insight (vipassanūpakkilesa: illumination/obhāsa, zest, tranquillity, etc.). When the meditator discerns that these are not the path (5th visuddhi), mature udayabbayañāṇa is resumed, entering the 6th purification (paṭipadāñāṇadassanavisuddhi).",
                "es": "En su fase tierna puede suscitar las 10 imperfecciones del insight (vipassanūpakkilesa). Al superarlas (5ª visuddhi), retoma udayabbayañāṇa maduro en la 6ª purificación."
            },
            "bodhiRef": "CMA IX §§24, 33–34 (pp. 346, 352–354)"
        },
        "seeAlso": ["vipassanā", "visuddhi", "ñāṇa", "tilakkhaṇa"]
    },
    "saṅkhārupekkhāñāṇa": {
        "meaning": {
            "pt": "Conhecimento de equanimidade em relação às formações; o ápice dos conhecimentos mundanos de insight (Cap. IX, §34), imediatamente anterior à emergência do Caminho Supramundano",
            "en": "Knowledge of equanimity toward formations; the culmination of mundane insight knowledges (Ch. IX, §34), immediately preceding the emergence of the Supramundane Path",
            "es": "Conocimiento de ecuanimidad respecto a las formaciones; la culminación de los conocimientos mundanos de insight (Cap. IX, §34), inmediatamente anterior al Sendero Supramundano"
        },
        "grammar": "nt. (saṅkhāra + upekkhā + ñāṇa)",
        "grammarLocalized": {
            "pt": "Substantivo neutro composto (saṅkhāra + upekkhā + ñāṇa)",
            "en": "Neuter compound noun (saṅkhāra + upekkhā + ñāṇa)",
            "es": "Sustantivo neutro compuesto (saṅkhāra + upekkhā + ñāṇa)"
        },
        "root": "saṃ + √kar + upa + √ikkh + √ñā",
        "samasa": {
            "type": {"pt": "Sattamī-Tappurisa + Kammadhāraya", "en": "Locative Tappurisa + Kammadhāraya", "es": "Tappurisa Locativo + Kammadhāraya"},
            "viggaha": "saṅkhāresu upekkhā = saṅkhārupekkhā; saṅkhārupekkhāya ñāṇaṃ = saṅkhārupekkhāñāṇaṃ",
            "literal": {"pt": "conhecimento (ñāṇa) de equanimidade imparcial (upekkhā) perante todas as formações condicionadas (saṅkhārā)", "en": "knowledge (ñāṇa) of impartial equanimity (upekkhā) toward all conditioned formations (saṅkhārā)", "es": "conocimiento (ñāṇa) de ecuanimidad imparcial (upekkhā) ante todas las formaciones condicionadas (saṅkhārā)"},
            "parts": [
                {"part": "saṅkhāra", "gloss": {"pt": "formações condicionadas", "en": "conditioned formations", "es": "formaciones condicionadas"}},
                {"part": "upekkhā", "gloss": {"pt": "equanimidade / neutralidade", "en": "equanimity / neutrality", "es": "ecuanimidad / neutralidad"}},
                {"part": "ñāṇa", "gloss": {"pt": "conhecimento de insight", "en": "insight knowledge", "es": "conocimiento de insight"}}
            ]
        },
        "abhidhamma": {
            "ontology": {"pt": "Realidade Última (Cetasika: Paññindriya)", "en": "Ultimate Reality (Cetasika: Paññindriya)", "es": "Realidad Última (Cetasika: Paññindriya)"},
            "category": {"pt": "Ápice do Insight Mundano (Vuṭṭhānagāminī-vipassanā — Cap. IX, §§34–36)", "en": "Culmination of Mundane Insight (Vuṭṭhānagāminī-vipassanā — Ch. IX, §§34–36)", "es": "Culminación del Insight Mundano (Vuṭṭhānagāminī-vipassanā — Cap. IX, §§34–36)"},
            "philosophy": {
                "pt": "Livre tanto do medo quanto do deleite em relação a todas as formações condicionadas, contempla nāma e rūpa com equilíbrio sereno através de uma das três portas de libertação (vimokkhamukha: animitta, appaṇihita ou suññata), culminando no conhecimento de conformidade (anulomañāṇa), mudança de linhagem (gotrabhū) e Caminho Supramundano (magga).",
                "en": "Free from both fear and delight regarding all conditioned formations, it contemplates nāma and rūpa with serene balance through one of the three doors of emancipation (vimokkhamukha: animitta, appaṇihita, or suññata), culminating in conformity knowledge (anulomañāṇa), change-of-lineage (gotrabhū), and the Supramundane Path (magga).",
                "es": "Libre de temor y deleite ante las formaciones condicionadas, contempla nāma y rūpa con equilibrio sereno a través de una de las tres puertas de liberación (vimokkhamukha), culminando en el Sendero Supramundano (magga)."
            },
            "bodhiRef": "CMA IX §§34–36 (pp. 355–358)"
        },
        "seeAlso": ["vipassanā", "visuddhi", "upekkhā", "magga", "tilakkhaṇa"]
    }
}

def normalize_samasa(samasa_obj):
    if not samasa_obj or not isinstance(samasa_obj, dict):
        return None
    norm = {
        "type": samasa_obj.get("type", {"pt": "Composto (Samāsa)", "en": "Compound (Samāsa)", "es": "Compuesto (Samāsa)"}),
        "literal": samasa_obj.get("literal", {"pt": "", "en": "", "es": ""}),
        "parts": []
    }
    if isinstance(norm["type"], str):
        norm["type"] = {"pt": norm["type"], "en": norm["type"], "es": norm["type"]}
    if isinstance(norm["literal"], str):
        norm["literal"] = {"pt": norm["literal"], "en": norm["literal"], "es": norm["literal"]}
    if samasa_obj.get("viggaha"):
        norm["viggaha"] = samasa_obj["viggaha"]
    for p in samasa_obj.get("parts", []):
        part_str = p.get("part") or p.get("pali") or ""
        gloss = p.get("gloss") or p.get("meaning") or {"pt": "", "en": "", "es": ""}
        if isinstance(gloss, str):
            gloss = {"pt": gloss, "en": gloss, "es": gloss}
        item = {"part": part_str, "gloss": gloss}
        if p.get("grammar"):
            g = p["grammar"]
            item["grammar"] = g if isinstance(g, dict) else {"pt": str(g), "en": str(g), "es": str(g)}
        norm["parts"].append(item)
    return norm

def localize_grammar_string(gram: str) -> dict:
    if not gram:
        return {"pt": "Termo Pāli", "en": "Pāli term", "es": "Término Pāli"}
    g_pt = gram
    g_en = (
        gram.replace("subst.", "noun")
        .replace("flexão de ", "inflected form of ")
        .replace("composto (sandhi)", "compound (sandhi)")
        .replace("part. pass.", "past part.")
        .replace("part. pres.", "pres. part.")
        .replace("gerundivo", "gerundive")
        .replace("gerúndio", "gerund")
        .replace("indecl.", "indecl.")
    )
    g_es = (
        gram.replace("subst.", "sust.")
        .replace("flexão de ", "forma flexionada de ")
        .replace("composto (sandhi)", "compuesto (sandhi)")
        .replace("part. pass.", "part. pas.")
        .replace("part. pres.", "part. pres.")
        .replace("gerúndio", "gerundio")
    )
    return {"pt": g_pt, "en": g_en, "es": g_es}

def clean_mixed_translation(text: str, lang: str, fallback_en: str) -> str:
    """Fix mixed English/PT/ES strings generated by older regex scripts."""
    if not text:
        return fallback_en
    # Fix common broken tokens
    fixes_pt = {
        "without intenção": "sem intenção",
        "mente; heart": "mente; coração; consciência",
        "não keeping vows": "sem observar votos",
        "(pleasant, unpleasant ou neutral) felt experience": "experiência sentida (agradável, desagradável ou neutra)",
        "sensação tone": "tom hedônico da sensação",
        "second of the five agregados": "segundo dos cinco agregados",
        "inflected forma de": "forma flexionada de",
    }
    fixes_es = {
        "without intención": "sin intención",
        "mente; heart": "mente; corazón; conciencia",
        "no keeping vows": "sin observar votos",
        "(pleasant, unpleasant o neutral) felt experience": "experiencia sentida (agradable, desagradable o neutra)",
        "sensación tone": "tono hedónico de la sensación",
        "second of the five agregados": "segundo de los cinco agregados",
    }
    fixes = fixes_pt if lang == "pt" else fixes_es
    for bad, good in fixes.items():
        text = text.replace(bad, good)
    return text

def strip_pali_inflection(word: str, canonical_map: dict):
    """Find if `word` is an inflected surface form of a canonical entry."""
    w = word.lower().strip()
    if w in canonical_map:
        return w
    suffixes = [
        ("mekaṃ", "a"), ("mekaṃ", ""),
        ("ñceti", "a"), ("ñceti", ""),
        ("ñca", "a"), ("ñca", ""),
        ("neva", "a"), ("neva", ""),
        ("yeva", "a"), ("yeva", ""),
        ("mpi", "a"), ("mpi", ""),
        ("mpī", "a"), ("mpī", ""),
        ("supi", ""), ("nampi", "a"),
        ("vasena", "a"), ("vasena", ""),
        ("bhāvato", "a"), ("bhāvato", ""),
        ("lakkhaṇa", ""),
        ("assa", "a"), ("assa", ""),
        ("ānaṃ", "a"), ("ānaṃ", "i"), ("ānaṃ", "u"), ("ānaṃ", ""),
        ("esu", "a"), ("esu", "i"), ("esu", ""),
        ("āni", "a"), ("āni", ""),
        ("ānī", "a"), ("ānī", ""),
        ("āya", "a"), ("āya", "ā"),
        ("ena", "a"), ("ena", ""),
        ("ehi", "a"), ("ehi", ""),
        ("ato", "a"), ("to", "a"), ("to", ""),
        ("aṃ", "a"), ("aṃ", ""),
        ("o", "a"), ("o", ""),
        ("ā", "a"), ("ā", ""),
        ("e", "a"), ("e", ""),
        ("i", "a"), ("ī", "i"), ("ū", "u"),
    ]
    for sfx, repl in suffixes:
        if w.endswith(sfx) and len(w) > len(sfx) + 2:
            cand = w[:-len(sfx)] + repl
            if cand in canonical_map:
                return cand
    return None

def decompose_canonical_compound(word: str, canonical_map: dict):
    """Decompose a compound token into canonical lemmas if possible."""
    w = word.lower().strip()
    # Strip trailing case endings first
    base = w
    for sfx in ["cittāni", "cittānī", "cittaṃ", "cittesu", "cittānaṃ", "cittañca", "cittāneva"]:
        if w.endswith(sfx) and len(w) > len(sfx) + 2:
            prefix = w[:-len(sfx)]
            cand_prefix = strip_pali_inflection(prefix, canonical_map) or (prefix if prefix in canonical_map else None)
            if cand_prefix and cand_prefix in canonical_map:
                return [cand_prefix, "citta"]
    for sfx in ["rūpaṃ", "rūpāni", "dhammā", "dhammesu", "dhammānaṃ", "saṅgaho", "saṅgahe", "ñāṇaṃ", "ñāṇena", "nimittaṃ", "nimitte", "bhūmi", "bhūmiyaṃ", "caritā", "caritassa"]:
        if w.endswith(sfx) and len(w) > len(sfx) + 2:
            prefix = w[:-len(sfx)]
            head_lemma = strip_pali_inflection(sfx, canonical_map) or sfx.rstrip("ṃāoeyiu")
            for h_cand in [head_lemma, head_lemma + "a", head_lemma + "ā", head_lemma + "i"]:
                if h_cand in canonical_map:
                    head_lemma = h_cand
                    break
            cand_prefix = strip_pali_inflection(prefix, canonical_map) or (prefix if prefix in canonical_map else None)
            if cand_prefix and cand_prefix in canonical_map and head_lemma in canonical_map:
                return [cand_prefix, head_lemma]
    return None

def main():
    # 1. Assemble all canonical curated entries
    canonical = {}
    for part_dict in (
        PART1_ENTRIES,
        PART2_ENTRIES,
        PART3_ENTRIES,
        PART4A_ENTRIES,
        PART4B_ENTRIES,
        PART4C_ENTRIES,
        PART4D_ENTRIES,
        EXTRA_SANGAHA_ENTRIES,
        build_patthana_entries(),
    ):
        for k, v in part_dict.items():
            key_lower = k.lower().strip()
            entry = dict(v)
            entry["pali"] = key_lower
            entry["tier"] = 1
            if "samasa" in entry:
                entry["samasa"] = normalize_samasa(entry["samasa"])
            if "grammarLocalized" not in entry and "grammar" in entry:
                entry["grammarLocalized"] = localize_grammar_string(entry["grammar"])
            canonical[key_lower] = entry

    print(f"Total curated canonical Tier-1 entries assembled: {len(canonical)}")

    # 2. Load existing paliDictionary.json
    with open(DICT_PATH, "r", encoding="utf-8") as f:
        existing_list = json.load(f)

    entries_by_key = {}
    for item in existing_list:
        k = item["pali"].lower().strip()
        entries_by_key[k] = item

    # 3. Override / insert all canonical entries
    for k, c_entry in canonical.items():
        entries_by_key[k] = c_entry

    # 4. Scan all tokens in chapters to ensure 100% coverage of chapter compounds/inflections
    chapter_tokens = set()
    for fpath in sorted(glob.glob(f"{CHAPTERS_DIR}/ch*.json")):
        with open(fpath, "r", encoding="utf-8") as f:
            for seg in json.load(f):
                pali = re.sub(r"<[^>]+>", " ", seg.get("pali", ""))
                for tok in re.findall(r"[a-zA-ZāīūñṅṭḍṇḷṃĀĪŪÑṄṬḌṆḶṂ]+", pali):
                    chapter_tokens.add(tok.lower())

    for tok in chapter_tokens:
        if tok not in entries_by_key:
            base_cand = strip_pali_inflection(tok, canonical)
            if base_cand:
                entries_by_key[tok] = {
                    "pali": tok,
                    "baseLemma": base_cand,
                    "grammar": f"flexão de {base_cand}",
                    "meaning": {
                        "pt": f"{canonical[base_cand]['meaning']['pt']} (forma flexionada de {base_cand})",
                        "en": f"{canonical[base_cand]['meaning']['en']} (inflected form of {base_cand})",
                        "es": f"{canonical[base_cand]['meaning']['es']} (forma flexionada de {base_cand})",
                    }
                }
            else:
                comp_parts = decompose_canonical_compound(tok, canonical)
                if comp_parts and len(comp_parts) == 2:
                    p1, p2 = comp_parts[0], comp_parts[1]
                    c1, c2 = canonical[p1], canonical[p2]
                    entries_by_key[tok] = {
                        "pali": tok,
                        "tier": 1,
                        "grammar": f"composto ({p1} + {p2})",
                        "grammarLocalized": {
                            "pt": f"Composto nominal flexionado ({p1} + {p2})",
                            "en": f"Inflected compound noun ({p1} + {p2})",
                            "es": f"Compuesto nominal flexionado ({p1} + {p2})",
                        },
                        "root": f"{c1.get('root', p1)} + {c2.get('root', p2)}",
                        "meaning": {
                            "pt": f"{c2['meaning']['pt'].split(';')[0]} qualificado por {p1} ({c1['meaning']['pt'].split(';')[0]}).",
                            "en": f"{c2['meaning']['en'].split(';')[0]} qualified by {p1} ({c1['meaning']['en'].split(';')[0]}).",
                            "es": f"{c2['meaning']['es'].split(';')[0]} calificado por {p1} ({c1['meaning']['es'].split(';')[0]}).",
                        },
                        "samasa": {
                            "type": {
                                "pt": "Composto Determinativo (Kammadhāraya / Tappurisa)",
                                "en": "Determinative Compound (Kammadhāraya / Tappurisa)",
                                "es": "Compuesto Determinativo (Kammadhāraya / Tappurisa)",
                            },
                            "literal": {
                                "pt": f"{p1} + {p2}",
                                "en": f"{p1} + {p2}",
                                "es": f"{p1} + {p2}",
                            },
                            "parts": [
                                {"part": p1, "gloss": {"pt": c1["meaning"]["pt"].split(";")[0], "en": c1["meaning"]["en"].split(";")[0], "es": c1["meaning"]["es"].split(";")[0]}},
                                {"part": p2, "gloss": {"pt": c2["meaning"]["pt"].split(";")[0], "en": c2["meaning"]["en"].split(";")[0], "es": c2["meaning"]["es"].split(";")[0]}},
                            ],
                        },
                        "abhidhamma": c1.get("abhidhamma") or c2.get("abhidhamma"),
                        "seeAlso": [p1, p2],
                    }

    # 5. Propagate canonical Abhidhamma & Samāsa metadata to all inflected forms of canonical lemmas
    inherited_count = 0
    for k, entry in list(entries_by_key.items()):
        if k in canonical:
            continue

        # Detect baseLemma from "(inflected form of X)" or morphological stripping
        base_lemma = entry.get("baseLemma")
        if not base_lemma:
            en_m = entry.get("meaning", {}).get("en", "")
            m = re.search(r"\(inflected form of ([^)]+)\)", en_m)
            if m:
                cand = m.group(1).strip().lower()
                if cand in canonical:
                    base_lemma = cand
        if not base_lemma:
            cand = strip_pali_inflection(k, canonical)
            if cand and cand in canonical:
                base_lemma = cand

        if base_lemma and base_lemma in canonical:
            c_base = canonical[base_lemma]
            entry["baseLemma"] = base_lemma
            entry["tier"] = 1
            entry["meaning"] = {
                "pt": f"{c_base['meaning']['pt']} [Forma flexionada de {base_lemma}]",
                "en": f"{c_base['meaning']['en']} [Inflected form of {base_lemma}]",
                "es": f"{c_base['meaning']['es']} [Forma flexionada de {base_lemma}]",
            }
            if c_base.get("root"):
                entry["root"] = c_base["root"]
            if c_base.get("etymology"):
                entry["etymology"] = c_base["etymology"]
            if c_base.get("samasa"):
                entry["samasa"] = c_base["samasa"]
            if c_base.get("abhidhamma"):
                entry["abhidhamma"] = c_base["abhidhamma"]
            if c_base.get("seeAlso"):
                entry["seeAlso"] = [base_lemma] + [x for x in c_base["seeAlso"] if x != base_lemma][:5]
            else:
                entry["seeAlso"] = [base_lemma]
            gram_raw = entry.get("grammar", f"flexão de {base_lemma}")
            entry["grammarLocalized"] = {
                "pt": f"Forma flexionada de {base_lemma} ({gram_raw})",
                "en": f"Inflected form of {base_lemma} ({gram_raw})",
                "es": f"Forma flexionada de {base_lemma} ({gram_raw})",
            }
            inherited_count += 1
        else:
            # Clean any mixed translation & ensure grammarLocalized exists
            m_obj = entry.get("meaning", {})
            en_txt = m_obj.get("en", "")
            m_obj["pt"] = clean_mixed_translation(m_obj.get("pt", ""), "pt", en_txt)
            m_obj["es"] = clean_mixed_translation(m_obj.get("es", ""), "es", en_txt)
            if "grammarLocalized" not in entry:
                entry["grammarLocalized"] = localize_grammar_string(entry.get("grammar", ""))

    # Special case: asaṅkhārikamekaṃ / sasaṅkhārikamekaṃ (very common in Ch. I)
    for prefix_lemma, surface_tok in [("asaṅkhārika", "asaṅkhārikamekaṃ"), ("sasaṅkhārika", "sasaṅkhārikamekaṃ")]:
        if prefix_lemma in canonical:
            c_base = canonical[prefix_lemma]
            entries_by_key[surface_tok] = {
                "pali": surface_tok,
                "baseLemma": prefix_lemma,
                "tier": 1,
                "grammar": f"sandhi ({prefix_lemma}ṃ + ekaṃ)",
                "grammarLocalized": {
                    "pt": f"Composto de sandhi ({prefix_lemma}ṃ [nom. sg. nt.] + ekaṃ [uma])",
                    "en": f"Sandhi compound ({prefix_lemma}ṃ [nt. nom. sg.] + ekaṃ [one])",
                    "es": f"Compuesto de sandhi ({prefix_lemma}ṃ [nom. sg. nt.] + ekaṃ [una])",
                },
                "root": c_base.get("root", ""),
                "meaning": {
                    "pt": f"Uma (ekaṃ) consciência { 'não induzida / espontânea' if prefix_lemma == 'asaṅkhārika' else 'induzida / instigada' } ({prefix_lemma}ṃ). {c_base['meaning']['pt']}",
                    "en": f"One (ekaṃ) { 'unprompted / spontaneous' if prefix_lemma == 'asaṅkhārika' else 'prompted / induced' } ({prefix_lemma}ṃ) consciousness. {c_base['meaning']['en']}",
                    "es": f"Una (ekaṃ) conciencia { 'no instigada / espontánea' if prefix_lemma == 'asaṅkhārika' else 'instigada / inducida' } ({prefix_lemma}ṃ). {c_base['meaning']['es']}",
                },
                "samasa": c_base.get("samasa"),
                "abhidhamma": c_base.get("abhidhamma"),
                "seeAlso": [prefix_lemma, "citta"] + c_base.get("seeAlso", [])[:3],
            }

    print(f"Total inflected/surface entries enriched with canonical inheritance: {inherited_count}")

    final_list = sorted(entries_by_key.values(), key=lambda x: x["pali"].lower())
    with open(DICT_PATH, "w", encoding="utf-8") as f:
        json.dump(final_list, f, ensure_ascii=False, indent=2)

    tier1_count = sum(1 for x in final_list if x.get("tier") == 1)
    print(f"Saved {len(final_list)} entries to {DICT_PATH} ({tier1_count} Tier-1 canonical entries & inflections).")

if __name__ == "__main__":
    main()

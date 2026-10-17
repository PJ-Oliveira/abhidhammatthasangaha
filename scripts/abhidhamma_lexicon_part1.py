# -*- coding: utf-8 -*-
"""
Parte 1 do Léxico Filosófico do Abhidhammattha Saṅgaha (Baseado em Bhikkhu Bodhi, CMA):
- Fundamentos Ontológicos e Realidades Últimas (Paramattha Dhammas, Paññatti, Sabhāva)
- Classificações de Citta (Planos / Bhūmi, Naturezas / Jāti, Raízes / Hetu)
- Compostos e Fórmulas Técnicas do Capítulo I (Somanassasahagata, Diṭṭhigatasampayutta, Asaṅkhārika, etc.)
- Classes das 89 / 121 Consciências (Akusala, Ahetuka, Kāmāvacara Sobhana, Mahaggata, Lokuttara)
"""

PART1_ENTRIES = {
    "abhidhammatthasaṅgaha": {
        "meaning": {
            "pt": "Compêndio das Matérias Contidas no Abhidhamma; tratado clássico do séc. XI/XII composto por Ācariya Anuruddha que sintetiza toda a arquitetura filosófica, psicológica e ontológica do Abhidhamma Theravāda.",
            "en": "A Compendium of the Things Contained in the Abhidhamma; the classical 11th/12th-century manual composed by Ācariya Anuruddha synthesizing the entire philosophical, psychological, and ontological system of Theravāda Abhidhamma.",
            "es": "Compendio de las Materias Contenidas en el Abhidhamma; tratado clásico del siglo XI/XII compuesto por Ācariya Anuruddha que sintetiza toda la arquitectura filosófica, psicológica y ontológica del Abhidhamma Theravāda."
        },
        "grammar": "masc. nom. sg. (título do tratado; composto tappurisa)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (composto determinativo genitivo — Chaṭṭhī-Tappurisa)",
            "en": "Masculine noun (genitive determinative compound — Chaṭṭhī-Tappurisa)",
            "es": "Sustantivo masculino (compuesto determinativo genitivo — Chaṭṭhī-Tappurisa)"
        },
        "root": "abhi + √dhar + ma + attha + saṃ + √gah + a",
        "etymology": {
            "pt": "Formado por abhidhamma (abhi [superior, distinto, supremo] + dhamma [ensinamento/fenômeno, de √dhar 'sustentar']) + attha (matéria, significado, realidade objetiva, de √ar 'alcançar') + saṅgaha (compêndio, síntese, reunião, de saṃ [junto] + √gah [tomar, abarcar]).",
            "en": "Formed from abhidhamma (abhi [higher, special, distinguished] + dhamma [teaching/phenomenon, from √dhar 'to hold/bear']) + attha (thing, matter, meaning, from √ar 'to reach') + saṅgaha (compendium, synthesis, holding together, from saṃ [together] + √gah [to grasp/hold]).",
            "es": "Formado por abhidhamma (abhi [superior, distinguido] + dhamma [enseñanza/fenómeno, de √dhar 'sostener']) + attha (materia, significado, realidad, de √ar 'alcanzar') + saṅgaha (compendio, síntesis, de saṃ [junto] + √gah [tomar, abarcar])."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Genitivo Duplo (Chaṭṭhī-Tappurisa)",
                "en": "Double Genitive Determinative Compound (Chaṭṭhī-Tappurisa)",
                "es": "Compuesto Determinativo Genitivo Doble (Chaṭṭhī-Tappurisa)"
            },
            "viggaha": "abhidhammassa atthā = abhidhammatthā; abhidhammatthānaṃ saṅgaho = abhidhammatthasaṅgaho",
            "literal": {
                "pt": "O compêndio (saṅgaha) das matérias ou realidades (attha) pertencentes ao ensinamento superior (abhidhamma).",
                "en": "The compendium (saṅgaha) of the things or realities (attha) contained in the higher teaching (abhidhamma).",
                "es": "El compendio (saṅgaha) de las materias o realidades (attha) pertenecientes a la enseñanza superior (abhidhamma)."
            },
            "parts": [
                {
                    "part": "abhidhamma",
                    "gloss": {"pt": "ensinamento superior / distinto", "en": "higher / distinguished teaching", "es": "enseñanza superior / distinguida"},
                    "grammar": {"pt": "abhi (pref.) + dhamma (m.)", "en": "abhi (pref.) + dhamma (m.)", "es": "abhi (pref.) + dhamma (m.)"}
                },
                {
                    "part": "attha",
                    "gloss": {"pt": "matéria, realidade, sentido", "en": "thing, matter, meaning", "es": "materia, realidad, significado"},
                    "grammar": {"pt": "subst. masc.", "en": "masc. noun", "es": "sust. masc."}
                },
                {
                    "part": "saṅgaha",
                    "gloss": {"pt": "compêndio, síntese, compilação", "en": "compendium, synthesis", "es": "compendio, síntesis"},
                    "grammar": {"pt": "saṃ + √gah + a (m.)", "en": "saṃ + √gah + a (m.)", "es": "saṃ + √gah + a (m.)"}
                }
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Designação Textual Canônica (Saddapaññatti / Pakaraṇa)",
                "en": "Canonical Textual Designation (Saddapaññatti / Pakaraṇa)",
                "es": "Designación Textual Canónica (Saddapaññatti / Pakaraṇa)"
            },
            "category": {
                "pt": "Manual Exegético Fundamental (Saṅgahapakaraṇa)",
                "en": "Fundamental Exegetical Manual (Saṅgahapakaraṇa)",
                "es": "Manual Exegético Fundamental (Saṅgahapakaraṇa)"
            },
            "philosophy": {
                "pt": "Segundo Bhikkhu Bodhi, o Abhidhammattha Saṅgaha organiza todo o universo da experiência em quatro realidades últimas (citta, cetasika, rūpa, nibbāna) nos Caps. I–VI, e em seguida articula suas sínteses categóricas (Cap. VII), suas relações condicionais (Cap. VIII) e sua aplicação prática na meditação de serenidade e insight (Cap. IX). Seus dois principais subcomentários (ṭīkā) são a Abhidhammatthavibhāvinī-Ṭīkā (de Ācariya Sumaṅgalasāmi) e a Paramatthadīpanī-Ṭīkā (de Ledi Sayadaw).",
                "en": "According to Bhikkhu Bodhi, the Abhidhammattha Saṅgaha organizes the entire universe of experience into four ultimate realities (citta, cetasika, rūpa, nibbāna) in Chs. I–VI, followed by their categorical syntheses (Ch. VII), conditional relations (Ch. VIII), and meditative praxis in calm and insight (Ch. IX). Its two foremost subcommentaries (ṭīkā) are the Abhidhammatthavibhāvinī-Ṭīkā (by Ācariya Sumaṅgalasāmi) and the Paramatthadīpanī-Ṭīkā (by Ledi Sayadaw).",
                "es": "Según Bhikkhu Bodhi, el Abhidhammattha Saṅgaha organiza todo el universo de la experiencia en cuatro realidades últimas (citta, cetasika, rūpa, nibbāna) en los Caps. I–VI, seguido de sus síntesis categoriales (Cap. VII), relaciones condicionales (Cap. VIII) y aplicación meditativa en calma e insight (Cap. IX)."
            },
            "bodhiRef": "CMA Intro & I, §1 (Guide, pp. 1–20, 25–27)"
        },
        "seeAlso": ["paramattha", "citta", "cetasika", "rūpa", "nibbāna"]
    },

    "paramattha": {
        "meaning": {
            "pt": "Realidade última; verdade última; fenômeno irredutível que existe por sua própria natureza intrínseca (sabhāva), independentemente de construção conceitual da mente.",
            "en": "Ultimate reality; ultimate truth; an irreducible phenomenon existing by reason of its own intrinsic nature (sabhāva), independent of conceptual mental construction.",
            "es": "Realidad última; verdad última; fenómeno irreducible que existe por su propia naturaleza intrínseca (sabhāva), independientemente de la construcción conceptual de la mente."
        },
        "grammar": "masc./adj. (parama + attha)",
        "grammarLocalized": {
            "pt": "Substantivo masculino / Adjetivo (composto Kammadhāraya)",
            "en": "Masculine noun / Adjective (Kammadhāraya compound)",
            "es": "Sustantivo masculino / Adjetivo (compuesto Kammadhāraya)"
        },
        "root": "parama + attha (√ar + tha)",
        "etymology": {
            "pt": "De parama (supremo, último, mais elevado, final) + attha (realidade, coisa existente, sentido objetivo). Na Vibhāvinī-Ṭīkā: 'paramassa uttamassa ñāṇassa attho gocaro' — aquilo que é o objeto próprio do conhecimento supremo.",
            "en": "From parama (supreme, ultimate, highest, final) + attha (reality, existent thing, objective meaning). Explained in the Vibhāvinī-Ṭīkā as 'paramassa uttamassa ñāṇassa attho gocaro' — that which is the objective domain of supreme knowledge.",
            "es": "De parama (supremo, último, final) + attha (realidad, ente existente, sentido objetivo). En la Vibhāvinī-Ṭīkā: 'paramassa uttamassa ñāṇassa attho gocaro' — aquello que constituye el dominio objetivo del conocimiento supremo."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Descritivo (Kammadhāraya)",
                "en": "Descriptive Determinative Compound (Kammadhāraya)",
                "es": "Compuesto Determinativo Descriptivo (Kammadhāraya)"
            },
            "viggaha": "paramo ca so attho cā'ti = paramattho (ou: paramassa ñāṇassa attho = paramattho)",
            "literal": {
                "pt": "A realidade (attha) que é última/suprema (parama), ou o objeto próprio da sabedoria suprema.",
                "en": "The reality/thing (attha) that is ultimate/supreme (parama), or the object of supreme knowledge.",
                "es": "La realidad (attha) que es última/suprema (parama), o el objeto del conocimiento supremo."
            },
            "parts": [
                {
                    "part": "parama",
                    "gloss": {"pt": "último, supremo, irredutível", "en": "ultimate, supreme, final", "es": "último, supremo, final"},
                    "grammar": {"pt": "adjetivo superlativo", "en": "superlative adjective", "es": "adjetivo superlativo"}
                },
                {
                    "part": "attha",
                    "gloss": {"pt": "realidade, entidade, objeto", "en": "reality, entity, object", "es": "realidad, entidad, objeto"},
                    "grammar": {"pt": "substantivo masculino", "en": "masculine noun", "es": "sustantivo masculino"}
                }
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "As 4 Realidades Últimas (Catudhā Paramattha)",
                "en": "The 4 Ultimate Realities (Catudhā Paramattha)",
                "es": "Las 4 Realidades Últimas (Catudhā Paramattha)"
            },
            "category": {
                "pt": "Citta (89/121), Cetasika (52), Rūpa (18 nipphanna / 28 total) e Nibbāna (1)",
                "en": "Citta (89/121), Cetasika (52), Rūpa (18 concrete / 28 total), and Nibbāna (1)",
                "es": "Citta (89/121), Cetasika (52), Rūpa (18 concretas / 28 total) y Nibbāna (1)"
            },
            "philosophy": {
                "pt": "O Abhidhamma distingue duas dimensões de realidade: a convencional (sammuti / paññatti) e a última (paramattha). Enquanto 'ser', 'pessoa', 'homem' ou 'carro' são construtos mentais (parikappanā) sobre agregados impermanentes, os paramattha dhammas são os constituintes últimos e irredutíveis da experiência, dotados de natureza intrínseca própria (sabhāva). As três primeiras realidades últimas (citta, cetasika, rūpa) são condicionadas (saṅkhata) e abrangem os cinco agregados (pañcakkhandhā); a quarta (Nibbāna) é a única realidade última incondicionada (asaṅkhata). Somente os 72 dhammas dotados de natureza intrínseca (1 citta + 52 cetasikas + 18 nipphannarūpas + 1 nibbāna = 72 vatthudhammā salakkhaṇā) são paramattha estrito.",
                "en": "The Abhidhamma distinguishes two dimensions of reality: conventional (sammuti / paññatti) and ultimate (paramattha). Whereas 'being', 'person', 'man', or 'chariot' are conceptual constructs (parikappanā) superimposed on impermanent processes, paramattha dhammas are the final, irreducible components of existence possessing their own intrinsic nature (sabhāva). The first three ultimate realities (citta, cetasika, rūpa) are conditioned (saṅkhata) and encompass the five aggregates (pañcakkhandhā); the fourth (Nibbāna) is the sole unconditioned (asaṅkhata) ultimate reality. Strictly speaking, there are 72 realities possessing intrinsic nature (1 citta + 52 cetasikas + 18 concretely produced rūpas + 1 Nibbāna = 72 vatthudhammā salakkhaṇā).",
                "es": "El Abhidhamma distingue dos dimensiones de la realidad: convencional (sammuti / paññatti) y última (paramattha). Mientras que 'ser', 'persona' o 'carro' son construcciones conceptuales (parikappanā), los paramattha dhammas son los componentes últimos e irreducibles de la existencia dotados de naturaleza intrínseca (sabhāva). Las tres primeras realidades (citta, cetasika, rūpa) son condicionadas (saṅkhata); la cuarta (Nibbāna) es la única realidad última incondicionada (asaṅkhata)."
            },
            "bodhiRef": "CMA I, §2 (Guide, pp. 27–29); VII, §1 (p. 265)"
        },
        "seeAlso": ["sabhāva", "paññatti", "sammuti", "citta", "cetasika", "rūpa", "nibbāna"]
    },

    "sabhāva": {
        "meaning": {
            "pt": "Natureza intrínseca; característica própria; modo de ser irredutível que define um dhamma último (ex.: a dureza na terra, o sentir em vedanā, o conhecer em citta).",
            "en": "Intrinsic nature; own-nature; the irreducible defining mode of being of an ultimate dhamma (e.g., hardness in earth, feeling in vedanā, cognizing in citta).",
            "es": "Naturaleza intrínseca; naturaleza propia; modo de ser irreducible que define un dhamma último (ej., la dureza en la tierra, el sentir en vedanā, el conocer en citta)."
        },
        "grammar": "masc. (sa + bhāva)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (composto Kammadhāraya)",
            "en": "Masculine noun (Kammadhāraya compound)",
            "es": "Sustantivo masculino (compuesto Kammadhāraya)"
        },
        "root": "sa (próprio) + √bhū (ser/tornar-se) + *a",
        "etymology": {
            "pt": "Formado pelo prefixo reflexivo sa- (próprio, de si mesmo, sânsc. sva-) + bhāva (estado, natureza, modo de ser, da raiz √bhū 'ser, existir'). Os dhammas são chamados assim porque 'sustentam sua própria natureza intrínseca' (attano sabhāvaṃ dhārentī'ti dhammā).",
            "en": "Formed from the reflexive prefix sa- (own, self, Skt. sva-) + bhāva (state, nature, mode of being, from √bhū 'to be'). Dhammas are so called because 'they bear their own intrinsic nature' (attano sabhāvaṃ dhārentī'ti dhammā).",
            "es": "Formado por el prefijo reflexivo sa- (propio, Skt. sva-) + bhāva (estado, naturaleza, de √bhū 'ser, existir'). Los dhammas se llaman así porque 'sostienen su propia naturaleza intrínseca' (attano sabhāvaṃ dhārentī'ti dhammā)."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Descritivo (Kammadhāraya)",
                "en": "Descriptive Determinative Compound (Kammadhāraya)",
                "es": "Compuesto Determinativo Descriptivo (Kammadhāraya)"
            },
            "viggaha": "sako bhāvo = sabhāvo",
            "literal": {
                "pt": "O estado ou natureza (bhāva) que lhe é próprio (sa).",
                "en": "One's own (sa) state or nature (bhāva).",
                "es": "El estado o naturaleza (bhāva) que le es propio (sa)."
            },
            "parts": [
                {"part": "sa", "gloss": {"pt": "próprio, intrínseco", "en": "own, intrinsic", "es": "propio, intrínseco"}},
                {"part": "bhāva", "gloss": {"pt": "natureza, modo de ser", "en": "nature, state of being", "es": "naturaleza, modo de ser"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Critério Ontológico de Paramattha Dhamma",
                "en": "Ontological Criterion of Paramattha Dhamma",
                "es": "Criterio Ontológico de Paramattha Dhamma"
            },
            "category": {
                "pt": "Lakkhaṇa Individual (Salakkhaṇa) vs. Universal (Sāmaññalakkhaṇa)",
                "en": "Individual Characteristic (Salakkhaṇa) vs. Universal (Sāmaññalakkhaṇa)",
                "es": "Característica Individual (Salakkhaṇa) vs. Universal (Sāmaññalakkhaṇa)"
            },
            "philosophy": {
                "pt": "No Abhidhamma Theravāda clássico, sabhāva NÃO significa uma substância eterna ou autônoma (como o svabhāva criticado por Nāgārjuna contra os Sarvāstivādins), mas sim a função ou característica fenomênica específica (salakkhaṇa) que é diretamente observável na atenção plena (yoniso manasikāra) quando os conceitos são dissolvidos. Todo dhamma condicionado com sabhāva surge e cessa instantaneamente em dependência de condições.",
                "en": "In classical Theravāda Abhidhamma, sabhāva does NOT signify an eternal or self-existent substance (like the Sarvāstivādin svabhāva critiqued by Nāgārjuna), but rather the specific phenomenal characteristic or function (salakkhaṇa) directly observable by wise attention (yoniso manasikāra) when conceptual overlays are dissolved. Every conditioned dhamma possessing sabhāva arises and ceases momentarily in dependence on conditions.",
                "es": "En el Abhidhamma Theravāda clásico, sabhāva NO significa una sustancia eterna o autónoma, sino la característica o función fenoménica específica (salakkhaṇa) directamente observable mediante la atención sabia (yoniso manasikāra). Todo dhamma condicionado dotado de sabhāva surge y cesa instantáneamente en dependencia de condiciones."
            },
            "bodhiRef": "CMA Intro & I, §2 (Guide, pp. 3–6, 27–28); VI, §3 (p. 238)"
        },
        "seeAlso": ["paramattha", "dhamma", "lakkhaṇa", "paññatti"]
    },

    "citta": {
        "meaning": {
            "pt": "Consciência; mente; o ato ou processo momentâneo de conhecer (vijānana) um objeto. Primeira das quatro realidades últimas (paramattha dhammas), classificada em 89 ou 121 tipos.",
            "en": "Consciousness; mind; the momentary act or process of cognizing (vijānana) an object. The first of the four ultimate realities (paramattha dhammas), classified into 89 or 121 types.",
            "es": "Conciencia; mente; el acto o proceso momentáneo de conocer (vijānana) un objeto. Primera de las cuatro realidades últimas (paramattha dhammas), clasificada en 89 o 121 tipos."
        },
        "grammar": "nt. (de √cit + ta)",
        "grammarLocalized": {
            "pt": "Substantivo neutro (derivado da raiz √cit 'conhecer, pensar')",
            "en": "Neuter noun (derived from the root √cit 'to cognize, to know')",
            "es": "Sustantivo neutro (derivado de la raíz √cit 'conocer, pensar')"
        },
        "root": "√cit (conhecer / pensar) + ta",
        "etymology": {
            "pt": "Derivado da raiz verbal √cit (citi = conhecer, discernir). Os Comentários definem citta por três vias gramaticais (sādhana): (1) Agente (kattu-sādhana): 'ārammaṇaṃ cintetī'ti cittaṃ' (aquilo que conhece o objeto); (2) Instrumento (karaṇa-sādhana): 'etena cintentī'ti cittaṃ' (aquilo por meio do qual os fatores mentais associados conhecem o objeto); (3) Atividade pura (bhāva-sādhana): 'cintanamattaṃ cittaṃ' (o mero ato ou processo de conhecer o objeto) — sendo esta terceira definição a mais rigorosa filosoficamente.",
            "en": "Derived from the verbal root √cit (citi = to cognize, to know). The Commentaries define citta in three ways (sādhana): (1) As agent (kattu-sādhana): 'ārammaṇaṃ cintetī'ti cittaṃ' (that which cognizes an object); (2) As instrument (karaṇa-sādhana): 'etena cintentī'ti cittaṃ' (that by means of which the accompanying mental factors cognize the object); (3) As sheer activity (bhāva-sādhana): 'cintanamattaṃ cittaṃ' (nothing other than the process of cognizing the object) — this third definition being regarded as the most philosophically rigorous.",
            "es": "Derivado de la raíz verbal √cit (citi = conocer, discernir). Los Comentarios definen citta de tres modos (sādhana): (1) Como agente (kattu-sādhana): 'ārammaṇaṃ cintetī'ti cittaṃ' (lo que conoce el objeto); (2) Como instrumento (karaṇa-sādhana): 'etena cintentī'ti cittaṃ' (aquello por medio de lo cual los factores mentales asociados conocen el objeto); (3) Como pura actividad (bhāva-sādhana): 'cintanamattaṃ cittaṃ' (el mero proceso de conocer el objeto), siendo esta tercera definición la más rigurosa filosóficamente."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última Condicionada (Saṅkhata Paramattha Dhamma — 1ª de 4)",
                "en": "Conditioned Ultimate Reality (Saṅkhata Paramattha Dhamma — 1st of 4)",
                "es": "Realidad Última Condicionada (Saṅkhata Paramattha Dhamma — 1ª de 4)"
            },
            "category": {
                "pt": "89 Cittas (ou 121): 54 Kāmāvacara, 15 Rūpāvacara, 12 Arūpāvacara, 8 (ou 40) Lokuttara",
                "en": "89 Cittas (or 121): 54 Kāmāvacara, 15 Rūpāvacara, 12 Arūpāvacara, 8 (or 40) Lokuttara",
                "es": "89 Cittas (o 121): 54 Kāmāvacara, 15 Rūpāvacara, 12 Arūpāvacara, 8 (o 40) Lokuttara"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Conhecer um objeto (vijānana-lakkhaṇa) — a apreensão cognitiva nua da presença de um objeto.",
                    "en": "The knowing or cognizing of an object (vijānana-lakkhaṇa) — the bare cognitive awareness of an object.",
                    "es": "El conocer o discernir un objeto (vijānana-lakkhaṇa) — la aprehensión cognitiva desnuda de un objeto."
                },
                "rasa": {
                    "pt": "Ser o precursor ou líder (pubbaṅgama-rasa) dos fatores mentais (cetasikas), presidindo sobre eles e sendo sempre acompanhado por eles.",
                    "en": "To be a forerunner or leader (pubbaṅgama-rasa) of the mental factors (cetasikas), presiding over them and always accompanied by them.",
                    "es": "Ser el precursor o guía (pubbaṅgama-rasa) de los factores mentales (cetasikas), presidiéndolos y estando siempre acompañado por ellos."
                },
                "paccupatthana": {
                    "pt": "Continuidade de processos (sandhāna-paccupaṭṭhāna) — apresenta-se na experiência do meditador como um fluxo contínuo de atos mentais sucessivos.",
                    "en": "Continuity of processes (sandhāna-paccupaṭṭhāna) — presenting itself in the meditator's experience as a continuous stream of successive mental acts.",
                    "es": "Continuidad de procesos (sandhāna-paccupaṭṭhāna) — se presenta en la experiencia del meditador como un flujo continuo de actos mentales sucesivos."
                },
                "padatthana": {
                    "pt": "Mente-e-matéria (nāmarūpa-padaṭṭhāna) — pois a consciência jamais pode surgir isolada, na ausência completa de fatores mentais e fenômenos materiais (nos planos com matéria).",
                    "en": "Mind-and-matter (nāmarūpa-padaṭṭhāna) — because consciousness can never arise alone, in the complete absence of mental factors and material phenomena.",
                    "es": "Mente-y-materia (nāmarūpa-padaṭṭhāna) — porque la conciencia jamás puede surgir aislada, en ausencia completa de factores mentales y fenómenos materiales."
                }
            },
            "philosophy": {
                "pt": "Embora toda consciência tenha uma única característica intrínseca — o conhecer de um objeto —, o Abhidhamma diferencia 89 (ou 121) tipos de citta conforme a comitiva de fatores mentais (cetasikas) que a acompanham. Os 121 cittas resultam de desdobrar os 8 cittas supramundanos (4 caminhos e 4 frutos) pelos 5 níveis de jhāna (8 × 5 = 40, somados aos 81 mundanos = 121). Citta corresponde ao agregado da consciência (viññāṇakkhandha) nos Suttas.",
                "en": "While all consciousness shares a single intrinsic characteristic — the cognizing of an object — the Abhidhamma differentiates 89 (or 121) types of citta according to the retinue of mental factors (cetasikas) accompanying it. The 121-fold reckoning expands the 8 supramundane cittas (4 paths and 4 fruits) across the 5 jhāna levels (8 × 5 = 40, plus 81 mundane = 121). Citta corresponds to the aggregate of consciousness (viññāṇakkhandha) in the Suttas.",
                "es": "Aunque toda conciencia comparte una única característica intrínseca — el conocer un objeto —, el Abhidhamma distingue 89 (o 121) tipos de citta según el séquito de factores mentales (cetasikas) que la acompañan. El cómputo de 121 despliega los 8 cittas supramundanos a través de los 5 niveles de jhāna (8 × 5 = 40, más 81 mundanos = 121)."
            },
            "bodhiRef": "CMA I, §3 (Guide, pp. 29–34)"
        },
        "seeAlso": ["cetasika", "viññāṇa", "mano", "paramattha", "kāmāvacara", "lokuttara"]
    },

    "cetasika": {
        "meaning": {
            "pt": "Fator mental; concomitante mental; cada um dos 52 fenômenos mentais que surgem em conjunção imediata com a consciência (citta), auxiliando-a com tarefas cognitivas, afetivas, volitivas e éticas específicas.",
            "en": "Mental factor; mental concomitant; each of the 52 mental phenomena occurring in immediate conjunction with consciousness (citta), assisting it by performing specific cognitive, affective, volitional, and ethical tasks.",
            "es": "Factor mental; concomitante mental; cada uno de los 52 fenómenos mentales que ocurren en conjunción inmediata con la conciencia (citta), asistiéndola con funciones cognitivas, afectivas, volitivas y éticas específicas."
        },
        "grammar": "masc./nt. (de cetas + ika)",
        "grammarLocalized": {
            "pt": "Substantivo masculino / Adjetivo derivado (Taddhita: cetas + -ika)",
            "en": "Masculine noun / Secondary derivative adjective (Taddhita: cetas + -ika)",
            "es": "Sustantivo masculino / Adjetivo derivado secundario (Taddhita: cetas + -ika)"
        },
        "root": "√cit > cetas (mente) + ika (pertencente a)",
        "etymology": {
            "pt": "Derivado secundário (taddhita) de cetas (mente, consciência, de √cit) + sufixo -ika ('pertencente a, associado a'). Na Vibhāvinī-Ṭīkā e Dhammasaṅgaṇī-Ṭīkā: 'cetasi bhavā, cetasā saṃsaṭṭhā vā cetasikā' — aqueles que ocorrem na mente e estão inseparavelmente mesclados a ela.",
            "en": "Secondary derivative (taddhita) from cetas (mind, consciousness, from √cit) + suffix -ika ('belonging to, associated with'). Defined in the commentaries as 'cetasi bhavā, cetasā saṃsaṭṭhā vā cetasikā' — those that occur in the mind and are inextricably conjoined with it.",
            "es": "Derivado secundario (taddhita) de cetas (mente, conciencia, de √cit) + sufijo -ika ('perteneciente a, asociado con'). Definido en los comentarios como 'cetasi bhavā, cetasā saṃsaṭṭhā vā cetasikā' — aquellos que ocurren en la mente y están inseparablemente unidos a ella."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última Condicionada (Saṅkhata Paramattha Dhamma — 2ª de 4)",
                "en": "Conditioned Ultimate Reality (Saṅkhata Paramattha Dhamma — 2nd of 4)",
                "es": "Realidad Última Condicionada (Saṅkhata Paramattha Dhamma — 2ª de 4)"
            },
            "category": {
                "pt": "52 Cetasikas: 13 Aññasamāna (7 Universais + 6 Ocasionais), 14 Akusala, 25 Sobhana",
                "en": "52 Cetasikas: 13 Aññasamāna (7 Universals + 6 Occasionals), 14 Akusala, 25 Sobhana",
                "es": "52 Cetasikas: 13 Aññasamāna (7 Universales + 6 Ocasionales), 14 Akusala, 25 Sobhana"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Possuir as 4 marcas de inseparabilidade com citta: (1) surgir junto (ekuppāda), (2) cessar junto (ekanirodha), (3) ter o mesmo objeto (ekālambana) e (4) ter a mesma base física (ekavatthuka).",
                    "en": "Possessing the 4 marks of inseparability with citta: (1) arising together (ekuppāda), (2) ceasing together (ekanirodha), (3) having the same object (ekālambana), and (4) having the same physical base (ekavatthuka).",
                    "es": "Poseer las 4 marcas de inseparabilidad con citta: (1) surgir juntos (ekuppāda), (2) cesar juntos (ekanirodha), (3) tener el mismo objeto (ekālambana) y (4) tener la misma base física (ekavatthuka)."
                },
                "rasa": {
                    "pt": "Auxiliar a consciência desempenhando funções específicas (sentir, perceber, decidir, aplicar, etc.) no ato total da cognição, como ministros que acompanham um rei.",
                    "en": "Assisting consciousness by performing specialized tasks (feeling, perceiving, willing, applying, etc.) in the total act of cognition, like a retinue accompanying a king.",
                    "es": "Asistir a la conciencia desempeñando tareas específicas (sentir, percibir, decidir, aplicar, etc.) en el acto total de la cognición, como el séquito que acompaña a un rey."
                },
                "paccupatthana": {
                    "pt": "Concomitância inseparável (sampayoga) com a consciência na experiência do objeto.",
                    "en": "Inseparable association (sampayoga) with consciousness in experiencing the object.",
                    "es": "Asociación inseparable (sampayoga) con la conciencia en la experiencia del objeto."
                },
                "padatthana": {
                    "pt": "A consciência (citta) e os demais fatores mentais co-surgentes, além do objeto e da base.",
                    "en": "Consciousness (citta) and the other co-arisen mental factors, along with the object and base.",
                    "es": "La conciencia (citta) y los demás factores mentales co-surgentes, junto con el objeto y la base."
                }
            },
            "philosophy": {
                "pt": "No Capítulo II (§1), Ācariya Anuruddha define os 52 cetasikas pelas quatro condições 'eka-': (1) ekuppāda exclui estados passados/futuros; (2) ekanirodha exclui a matéria produzida pela mente e pelo kamma (que surge com citta, mas dura 17 momentos mentais); (3) ekālambana exclui as duas intimações materiais (kāyaviññatti e vacīviññatti), que surgem e cessam com citta, mas não tomam objeto; (4) ekavatthuka estabelece a base física comum nos planos com matéria. Os 52 cetasikas compreendem três dos cinco agregados: vedanākkhandha (vedanā), saññākkhandha (saññā) e saṅkhārakkhandha (os outros 50 cetasikas). São analisados por dois métodos complementares: sampayoganaya (com quais cittas cada cetasika se associa) e saṅgahanaya (quais cetasikas entram na composição de cada citta).",
                "en": "In Chapter II (§1), Ācariya Anuruddha defines the 52 cetasikas by the four 'eka-' conditions: (1) ekuppāda excludes non-simultaneous states; (2) ekanirodha excludes mind-born and kamma-born matter (which arise with citta but endure for 17 mind-moments); (3) ekālambana excludes bodily and vocal intimation (kāyaviññatti, vacīviññatti), which arise and cease with citta but do not take an object; (4) ekavatthuka establishes their common physical base in realms with matter. The 52 cetasikas comprise three of the five aggregates: vedanākkhandha (vedanā), saññākkhandha (saññā), and saṅkhārakkhandha (the remaining 50 cetasikas). They are investigated via two complementary methods: sampayoganaya (method of association) and saṅgahanaya (method of combination).",
                "es": "En el Capítulo II (§1), Ācariya Anuruddha define los 52 cetasikas mediante las cuatro condiciones 'eka-': (1) ekuppāda, (2) ekanirodha (excluye la materia nacida de la mente, que dura 17 momentos mentales), (3) ekālambana (excluye las dos intimaciones materiales, que surgen y cesan con citta pero no toman objeto) y (4) ekavatthuka (misma base física). Los 52 cetasikas abarcan tres de los cinco agregados: vedanākkhandha, saññākkhandha y saṅkhārakkhandha (los otros 50 cetasikas)."
            },
            "bodhiRef": "CMA II, §1 (Guide, pp. 76–77)"
        },
        "seeAlso": ["citta", "aññasamāna", "sabbacittasādhāraṇa", "pakiṇṇaka", "akusala", "sobhana", "sampayoga"]
    },

    "rūpa": {
        "meaning": {
            "pt": "Matéria; fenômeno material (sentido geral no Abhidhamma, compreendendo 28 tipos); ou forma visível / cor (sentido restrito como 1 dos 28 fenômenos materiais, rūpāyatana).",
            "en": "Matter; material phenomenon (general sense in Abhidhamma, comprising 28 types); or visible form / colour (restricted sense as 1 of the 28 material phenomena, rūpāyatana).",
            "es": "Materia; fenómeno material (sentido general en el Abhidhamma, que comprende 28 tipos); o forma visible / color (sentido restringido como 1 de los 28 fenómenos materiales, rūpāyatana)."
        },
        "grammar": "nt. (de √rup + a)",
        "grammarLocalized": {
            "pt": "Substantivo neutro (derivado da raiz √rup 'ser deformado, alterado, afligido')",
            "en": "Neuter noun (derived from the root √rup 'to be deformed, disturbed, broken')",
            "es": "Sustantivo neutro (derivado de la raíz √rup 'ser deformado, alterado, quebrantado')"
        },
        "root": "√rup (ser deformado / perturbado) + a",
        "etymology": {
            "pt": "Derivado exegeticamente do verbo ruppati ('ser deformado, perturbado, golpeado, oprimido, quebrado' — Mahāniddesa: ruppati, kuppati, ghaṭṭīyati, pīḷīyati, bhijjati). Na Vibhāvinī-Ṭīkā: 'sītoṇhādi-virodhippaccayehi vikāraṃ āpajjati' — sofre alteração devido a condições físicas adversas como frio e calor.",
            "en": "Derived exegetically from the verb ruppati ('to be deformed, disturbed, knocked about, oppressed, broken' — Mahāniddesa: ruppati, kuppati, ghaṭṭīyati, pīḷīyati, bhijjati). In the Vibhāvinī-Ṭīkā: 'sītoṇhādi-virodhippaccayehi vikāraṃ āpajjati' — it undergoes alteration owing to adverse physical conditions such as cold and heat.",
            "es": "Derivado exegéticamente del verbo ruppati ('ser deformado, perturbado, golpeado, oprimido, quebrantado'). En la Vibhāvinī-Ṭīkā: 'sītoṇhādi-virodhippaccayehi vikāraṃ āpajjati' — sufre alteración debido a condiciones físicas adversas como el frío y el calor."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última Condicionada Não-Cognitiva (Saṅkhata Anārammaṇa Paramattha Dhamma — 3ª de 4)",
                "en": "Non-Cognitive Conditioned Ultimate Reality (Saṅkhata Anārammaṇa Paramattha Dhamma — 3rd of 4)",
                "es": "Realidad Última Condicionada No Cognitiva (Saṅkhata Anārammaṇa Paramattha Dhamma — 3ª de 4)"
            },
            "category": {
                "pt": "28 Fenômenos Materiais: 4 Grandes Elementos (Mahābhūta) + 24 Derivados (Upādārūpa); ou 18 Concretos (Nipphanna) + 10 Não-Concretos (Anipphanna)",
                "en": "28 Material Phenomena: 4 Great Essentials (Mahābhūta) + 24 Derived (Upādārūpa); or 18 Concrete (Nipphanna) + 10 Non-Concrete (Anipphanna)",
                "es": "28 Fenómenos Materiales: 4 Grandes Elementos (Mahābhūta) + 24 Derivados (Upādārūpa); o 18 Concretos (Nipphanna) + 10 No Concretos (Anipphanna)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Sofrer deformação ou alteração (ruppana-lakkhaṇa) sob o impacto de condições físicas opostas como frio, calor, fome e sede.",
                    "en": "Undergoing deformation or alteration (ruppana-lakkhaṇa) owing to adverse physical conditions such as cold, heat, hunger, and thirst.",
                    "es": "Sufrir deformación o alteración (ruppana-lakkhaṇa) debido a condiciones físicas adversas como el frío, el calor, el hambre y la sed."
                },
                "rasa": {
                    "pt": "Dispersar-se ou transformar-se sem possuir faculdade cognitiva (anārammaṇa — não conhece objeto algum).",
                    "en": "Dispersing or transforming without possessing any cognitive faculty (anārammaṇa — it does not cognize any object).",
                    "es": "Dispersarse o transformarse sin poseer facultad cognitiva alguna (anārammaṇa — no conoce ningún objeto)."
                },
                "paccupatthana": {
                    "pt": "Instabilidade física e mutabilidade material contínua.",
                    "en": "Physical instability and continuous material mutability.",
                    "es": "Inestabilidad física y mutabilidad material continua."
                },
                "padatthana": {
                    "pt": "As quatro causas originadoras da matéria (rūpasamuṭṭhāna): kamma, consciência (citta), temperatura (utu) e nutrimento (āhāra).",
                    "en": "The four causes of matter's origination (rūpasamuṭṭhāna): kamma, consciousness (citta), temperature (utu), and nutriment (āhāra).",
                    "es": "Las cuatro causas originadoras de la materia (rūpasamuṭṭhāna): kamma, conciencia (citta), temperatura (utu) y alimento (āhāra)."
                }
            },
            "philosophy": {
                "pt": "Toda matéria compartilha oito qualificações universais (CMA VI, §6): é sem raiz (ahetuka), condicionada (sappaccaya), sujeita às impurezas como objeto (sāsava), produzida (saṅkhata), mundana (lokiya), pertencente à esfera sensorial (kāmāvacara), desprovida de objeto cognitivo (anārammaṇa — ao contrário de nāma, a matéria nunca conhece um objeto) e não passível de ser erradicada pelos caminhos supramundanos (appahātabba). Divide-se em 18 nipphannarūpa (matéria concretamente produzida, dotada de sabhāva próprio e apta à contemplação de insight) e 10 anipphannarūpa (modalidades, limites e características abstratas da matéria concreta).",
                "en": "All matter shares eight universal qualifications (CMA VI, §6): it is rootless (ahetuka), with conditions (sappaccaya), subject to taints as object (sāsava), conditioned (saṅkhata), mundane (lokiya), pertaining to the sense sphere (kāmāvacara), objectless (anārammaṇa — unlike nāma, matter never cognizes an object), and not to be abandoned by the supramundane paths (appahātabba). It divides into 18 nipphannarūpa (concretely produced matter possessing intrinsic nature and suitable for insight contemplation) and 10 anipphannarūpa (modalities, limits, and characteristics of concrete matter).",
                "es": "Toda materia comparte ocho calificaciones universales (CMA VI, §6): es sin raíz (ahetuka), con condiciones (sappaccaya), sujeta a las impurezas (sāsava), condicionada (saṅkhata), mundana (lokiya), perteneciente a la esfera sensorial (kāmāvacara), sin objeto cognitivo (anārammaṇa — no conoce ningún objeto) y no abandonable por los caminos supramundanos (appahātabba)."
            },
            "bodhiRef": "CMA VI, §§1–6 (Guide, pp. 234–245)"
        },
        "seeAlso": ["mahābhūta", "upādārūpa", "nipphannarūpa", "anipphannarūpa", "rūpakalāpa", "paramattha"]
    },

    "nibbāna": {
        "meaning": {
            "pt": "Nibbāna; a quarta realidade última; o elemento incondicionado (asaṅkhata dhātu), imortal e supramundano, que constitui a cessação definitiva do anseio (taṇhā) e do ciclo de renascimentos (saṃsāra).",
            "en": "Nibbāna; the fourth ultimate reality; the unconditioned (asaṅkhata dhātu), deathless, and supramundane element constituting the final cessation of craving (taṇhā) and the round of rebirths (saṃsāra).",
            "es": "Nibbāna; la cuarta realidad última; el elemento incondicionado (asaṅkhata dhātu), inmortal y supramundano, que constituye la cesación definitiva del anhelo (taṇhā) y del ciclo de renacimientos (saṃsāra)."
        },
        "grammar": "nt. (ni + √vā + ana, ou ni + vāna)",
        "grammarLocalized": {
            "pt": "Substantivo neutro (ni [fora / sem] + vāna [entrelaçamento do desejo] ou √vā [soprar / extinguir])",
            "en": "Neuter noun (ni [out / away from] + vāna [entanglement of craving] or √vā [to blow out / extinguish])",
            "es": "Sustantivo neutro (ni [fuera / sin] + vāna [enredo del deseo] o √vā [soplar / extinguir])"
        },
        "root": "ni (fora de) + vāna (desejo/costura) / ni + √vā (extinguir) + ana",
        "etymology": {
            "pt": "Filologicamente derivado de nibbāti (ni + √vā, 'ser soprado, ser extinto', referindo-se à extinção dos três fogos da cobiça, ódio e delusão). Na exegese canônica do Abhidhammattha Saṅgaha (VI, §30), porém, é explicado como 'vānasaṅkhātāya taṇhāya nikkhantattā nibbānaṃ' — a saída ou partida (nikkhantatta = ni-) daquilo que é chamado vāna ('costura' ou 'entrelaçamento'), isto é, o anseio (taṇhā) que costura uma existência à outra.",
            "en": "Philologically derived from nibbāti (ni + √vā, 'to be blown out or extinguished', signifying the extinguishing of the fires of greed, hatred, and delusion). In the canonical exegesis of the Abhidhammattha Saṅgaha (VI, §30), however, it is explained as 'vānasaṅkhātāya taṇhāya nikkhantattā nibbānaṃ' — the departure from (nikkhantatta = ni-) the entanglement (vāna) of craving (taṇhā) which stitches life to life.",
            "es": "Filológicamente derivado de nibbāti (ni + √vā, 'ser extinguido'). En la exégesis del Abhidhammattha Saṅgaha (VI, §30) se explica como 'vānasaṅkhātāya taṇhāya nikkhantattā nibbānaṃ' — la salida o partida (nikkhantatta = ni-) del enredo (vāna) del anhelo (taṇhā) que cose una existencia a otra."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última Incondicionada (Asaṅkhata Paramattha Dhamma — 4ª de 4)",
                "en": "Unconditioned Ultimate Reality (Asaṅkhata Paramattha Dhamma — 4th of 4)",
                "es": "Realidad Última Incondicionada (Asaṅkhata Paramattha Dhamma — 4ª de 4)"
            },
            "category": {
                "pt": "1 por natureza intrínseca (sabhāvato ekavidhaṃ); 2 por base de distinção (sa-upādisesa / anupādisesa); 3 por aspecto (suññata / animitta / appaṇihita)",
                "en": "1 by intrinsic nature (sabhāvato ekavidhaṃ); 2 by basis of distinction (sa-upādisesa / anupādisesa); 3 by aspect (suññata / animitta / appaṇihita)",
                "es": "1 por naturaleza intrínseca (sabhāvato ekavidhaṃ); 2 por base de distinción (sa-upādisesa / anupādisesa); 3 por aspecto (suññata / animitta / appaṇihita)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Paz (santi-lakkhaṇa) — a ausência completa de surgimento, envelhecimento e dissolução.",
                    "en": "Peace (santi-lakkhaṇa) — the complete absence of arising, aging, and dissolution.",
                    "es": "Paz (santi-lakkhaṇa) — la ausencia completa de surgimiento, envejecimiento y disolución."
                },
                "rasa": {
                    "pt": "Não morrer / imortalidade (accuta-rasa) ou proporcionar consolo e libertação do sofrimento (assāsakaraṇa-rasa).",
                    "en": "Not dying / deathlessness (accuta-rasa), or comforting and releasing from suffering (assāsakaraṇa-rasa).",
                    "es": "No morir / inmortalidad (accuta-rasa), o brindar consuelo y liberación del sufrimiento (assāsakaraṇa-rasa)."
                },
                "paccupatthana": {
                    "pt": "Ausência de sinais condicionados (animitta-paccupaṭṭhāna) ou ausência de proliferação e impedimento (nippapañca-paccupaṭṭhāna).",
                    "en": "Signlessness (animitta-paccupaṭṭhāna), i.e., absence of the signs of conditioned things, or non-diversification (nippapañca-paccupaṭṭhāna).",
                    "es": "Ausencia de signos condicionados (animitta-paccupaṭṭhāna) o ausencia de proliferación (nippapañca-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Por ser incondicionado (asaṅkhata), Nibbāna não possui causa produtora; contudo, o Nobre Caminho Óctuplo é a condição para sua realização cognitiva direta (sacchikiriyā).",
                    "en": "Being unconditioned (asaṅkhata), Nibbāna has no productive cause; however, the Noble Eightfold Path is the condition for its direct cognitive realization (sacchikiriyā).",
                    "es": "Al ser incondicionado (asaṅkhata), Nibbāna no tiene causa productora; sin embargo, el Noble Óctuple Sendero es la condición para su realización cognitiva directa (sacchikiriyā)."
                }
            },
            "philosophy": {
                "pt": "No Abhidhamma Theravāda, Nibbāna não é mera inexistência ou aniquilação, mas uma realidade última positiva, supramundana (lokuttara), apreendida como objeto direto (ārammaṇa) pelas consciências de caminho (maggacitta) e fruto (phalacitta), além de gotrabhū e vodāna. Embora único em sua natureza intrínseca (sabhāva), divide-se conceitualmente em dois elementos: (1) sa-upādisesa-nibbānadhātu (com resíduo restante — extinção das impurezas enquanto os 5 agregados do Arahant ainda vivem) e (2) anupādisesa-nibbānadhātu (sem resíduo restante — cessação final dos agregados no parinibbāna). Possui três aspectos contemplativos: vazio (suññata), sem sinal (animitta) e sem desejo (appaṇihita).",
                "en": "In Theravāda Abhidhamma, Nibbāna is not mere nothingness or annihilation, but a positive, supramundane (lokuttara) ultimate reality apprehended as the direct object (ārammaṇa) of the path (maggacitta) and fruition (phalacitta) consciousnesses, as well as gotrabhū and vodāna. Though single in its intrinsic nature (sabhāva), it is twofold by basis of distinction: (1) sa-upādisesa-nibbānadhātu (with residue remaining — extinguishment of defilements while the Arahant's five aggregates remain alive) and (2) anupādisesa-nibbānadhātu (without residue remaining — final cessation of the aggregates at parinibbāna). It has three aspects: void (suññata), signless (animitta), and desireless (appaṇihita).",
                "es": "En el Abhidhamma Theravāda, Nibbāna no es la mera nada, sino una realidad última positiva y supramundana (lokuttara) tomada como objeto directo (ārammaṇa) por las conciencias de camino (maggacitta) y fruto (phalacitta). Aunque único en su naturaleza intrínseca (sabhāva), es doble por distinción de base: sa-upādisesa (con residuo de agregados) y anupādisesa (sin residuo restante), y triple en aspecto: vacío (suññata), sin signo (animitta) y sin deseo (appaṇihita)."
            },
            "bodhiRef": "CMA I, §2 (pp. 28–29); VI, §§30–32 (Guide, pp. 259–262)"
        },
        "seeAlso": ["asaṅkhata", "lokuttara", "magga", "phala", "suññata", "animitta", "appaṇihita"]
    },

    "paññatti": {
        "meaning": {
            "pt": "Conceito; designação convencional; ideia ou nome construído pela mente, em contraste com as quatro realidades últimas (paramattha dhammas). Divide-se em conceito-como-significado (atthapaññatti) e conceito-como-nome (nāmapaññatti).",
            "en": "Concept; conventional designation; mental construct or name, in contrast to the four ultimate realities (paramattha dhammas). Divided into concept-as-meaning (atthapaññatti) and concept-as-name (nāmapaññatti).",
            "es": "Concepto; designación convencional; construcción mental o nombre, en contraste con las cuatro realidades últimas (paramattha dhammas). Se divide en concepto-como-significado (atthapaññatti) y concepto-como-nombre (nāmapaññatti)."
        },
        "grammar": "fem. (pa + √ñā + āpe + ti)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (derivado causativo de pa + √ñā 'fazer conhecer, designar')",
            "en": "Feminine noun (causative derivative from pa + √ñā 'to make known, to designate')",
            "es": "Sustantivo femenino (derivado causativo de pa + √ñā 'hacer conocer, designar')"
        },
        "root": "pa + √ñā (conhecer) + āpe (caus.) + ti",
        "etymology": {
            "pt": "Derivado do verbo causativo paññāpeti ('fazer conhecer, declarar, designar'). No Cap. VIII (§29), o Abhidhammattha Saṅgaha distingue dois polos: paññāpiyatī'ti paññatti ('aquilo que é tornado conhecido', isto é, o conceito-significado, atthapaññatti) e paññāpanato paññatti ('aquilo que torna conhecido', isto é, o conceito-nome, nāmapaññatti).",
            "en": "Derived from the causative verb paññāpeti ('to make known, to declare, to designate'). In Ch. VIII (§29), the Abhidhammattha Saṅgaha distinguishes two poles: paññāpiyatī'ti paññatti ('that which is made known', i.e., concept-as-meaning, atthapaññatti) and paññāpanato paññatti ('that which makes known', i.e., concept-as-name, nāmapaññatti).",
            "es": "Derivado del verbo causativo paññāpeti ('hacer conocer, designar'). En el Cap. VIII (§29), el Abhidhammattha Saṅgaha distingue dos polos: paññāpiyatī'ti paññatti ('lo que es dado a conocer', atthapaññatti) y paññāpanato paññatti ('lo que da a conocer', nāmapaññatti)."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Convencional (Sammuti-sacca / Sabhāva-rahita — Fora dos 4 Paramatthas, mas incluído em Dhammārammaṇa)",
                "en": "Conventional Reality (Sammuti-sacca / Sabhāva-rahita — Outside the 4 Paramatthas, but included in Dhammārammaṇa)",
                "es": "Realidad Convencional (Sammuti-sacca / Sabhāva-rahita — Fuera de los 4 Paramatthas, pero incluido en Dhammārammaṇa)"
            },
            "category": {
                "pt": "2 Classes Principais: Atthapaññatti (Conceito-Significado, 6 tipos) e Nāmapaññatti (Conceito-Nome, 6 tipos)",
                "en": "2 Main Classes: Atthapaññatti (Concept-as-meaning, 6 types) and Nāmapaññatti (Concept-as-name, 6 types)",
                "es": "2 Clases Principales: Atthapaññatti (Concepto-significado, 6 tipos) y Nāmapaññatti (Concepto-nombre, 6 tipos)"
            },
            "philosophy": {
                "pt": "Embora paññatti não possua natureza intrínseca (sabhāva) e seja livre de tempo (kālavimutta — não passa pelas fases de surgimento, presença e dissolução), desempenha papel indispensável no Abhidhamma: é o sexto tipo de objeto mental (dhammārammaṇa) e é o objeto de quase todas as meditações de serenidade (samatha), incluindo os sinais de kasiṇa (uggahanimitta e paṭibhāganimitta) e os seres nas meditações dos incomensuráveis (appamaññā / brahmavihāra). Já a meditação de insight (vipassanā) atravessa o véu de paññatti para contemplar diretamente os paramattha dhammas.",
                "en": "Although paññatti lacks intrinsic nature (sabhāva) and is time-freed (kālavimutta — it does not undergo arising, presence, and dissolution), it plays an indispensable role in the Abhidhamma: it is the sixth kind of mental object (dhammārammaṇa) and serves as the object of most calm (samatha) meditations, including the kasiṇa signs (uggahanimitta and paṭibhāganimitta) and living beings in the illimitables (appamaññā / brahmavihāra). Insight meditation (vipassanā), by contrast, pierces through paññatti to contemplate paramattha dhammas directly.",
                "es": "Aunque paññatti carece de naturaleza intrínseca (sabhāva) y está libre de tiempo (kālavimutta), desempeña un papel indispensable en el Abhidhamma: forma parte de los objetos mentales (dhammārammaṇa) y sirve de objeto a la mayoría de las meditaciones de calma (samatha), incluyendo los signos de kasiṇa y los seres vivos en los inconmensurables (brahmavihāra)."
            },
            "bodhiRef": "CMA I, §2 (pp. 27–28); III, §16 (p. 135); VIII, §§29–32 (Guide, pp. 325–328)"
        },
        "seeAlso": ["paramattha", "sammuti", "atthapaññatti", "nāmapaññatti", "nimitta"]
    },

    # ── PLANOS DE CONSCIÊNCIA (BHŪMI / AVACARA) ───────────────────────────────
    "kāmāvacara": {
        "meaning": {
            "pt": "Pertencente à esfera sensorial; consciência da esfera dos sentidos (54 cittas no total: 12 akusala, 18 ahetuka e 24 kāmāvacara sobhana).",
            "en": "Pertaining to the sense sphere; sense-sphere consciousness (54 cittas in all: 12 akusala, 18 ahetuka, and 24 kāmāvacara sobhana).",
            "es": "Perteneciente a la esfera de los sentidos; conciencia de la esfera sensorial (54 cittas en total: 12 akusala, 18 ahetuka y 24 kāmāvacara sobhana)."
        },
        "grammar": "adj./nt. (kāma + avacara)",
        "grammarLocalized": {
            "pt": "Adjetivo / Substantivo neutro (composto Sattamī-Tappurisa)",
            "en": "Adjective / Neuter noun (Sattamī-Tappurisa compound)",
            "es": "Adjetivo / Sustantivo neutro (compuesto Sattamī-Tappurisa)"
        },
        "root": "kāma (√kam + *a) + ava + √car + a",
        "etymology": {
            "pt": "De kāma (desejo sensorial subjetivo [kilesakāma] ou objetos sensoriais objetivos [vatthukāma], da raiz √kam 'desejar') + avacara ('aquilo que se move, frequenta ou habita em', de ava- + √car 'mover-se, andar').",
            "en": "From kāma (subjective sensual desire [kilesakāma] or objective sense-objects [vatthukāma], from √kam 'to desire') + avacara ('that which moves about in or frequents', from ava- + √car 'to move, roam').",
            "es": "De kāma (deseo sensorial subjetivo [kilesakāma] u objetos sensoriales objetivos [vatthukāma], de √kam 'desear') + avacara ('aquello que se mueve o frecuenta un ámbito', de ava- + √car 'moverse')."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Locativo (Sattamī-Tappurisa)",
                "en": "Locative Determinative Compound (Sattamī-Tappurisa)",
                "es": "Compuesto Determinativo Locativo (Sattamī-Tappurisa)"
            },
            "viggaha": "kāme (kāmabhūmiyaṃ) avacaratī'ti = kāmāvacaraṃ",
            "literal": {
                "pt": "Aquilo que frequenta, circula ou se move com maior frequência no plano do desejo sensorial.",
                "en": "That which moves about in or frequents the sensuous plane of existence.",
                "es": "Aquello que se mueve o frecuenta el plano de la existencia sensorial."
            },
            "parts": [
                {"part": "kāma", "gloss": {"pt": "desejo sensorial / esfera dos sentidos", "en": "sensual desire / sense realm", "es": "deseo sensorial / reino de los sentidos"}},
                {"part": "avacara", "gloss": {"pt": "que frequenta, esfera de atividade", "en": "frequenting, sphere of activity", "es": "que frecuenta, esfera de actividad"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Plano de Consciência (Cittabhūmi — 1º dos 4 planos)",
                "en": "Plane of Consciousness (Cittabhūmi — 1st of 4 planes)",
                "es": "Plano de Conciencia (Cittabhūmi — 1º de 4 planos)"
            },
            "category": {
                "pt": "54 Cittas da Esfera Sensorial (12 Prejudiciais + 18 Sem Raiz + 24 Belos da Esfera Sensorial)",
                "en": "54 Sense-Sphere Cittas (12 Unwholesome + 18 Rootless + 24 Sense-Sphere Beautiful)",
                "es": "54 Cittas de la Esfera Sensorial (12 Perjudiciales + 18 Sin Raíz + 24 Hermosos de la Esfera Sensorial)"
            },
            "philosophy": {
                "pt": "Segundo Bhikkhu Bodhi (CMA I, §3), é fundamental distinguir kāmāvacara (esfera de consciência, uma classificação de tipos de citta) de kāmabhūmi (o plano sensorial de existência, que compreende 11 reinos: 4 estados de privação, o reino humano e os 6 céus sensoriais). Os cittas kāmāvacara são típicos do kāmabhūmi e produzem renascimento nele, mas também podem surgir nos planos rūpabhūmi e arūpabhūmi (por exemplo, quando um Brahmā vê, ouve ou pensa com consciência comum).",
                "en": "According to Bhikkhu Bodhi (CMA I, §3), one must distinguish kāmāvacara (sphere of consciousness, a classification of cittas) from kāmabhūmi (the sensuous plane of existence, comprising 11 realms: 4 woeful states, the human realm, and 6 sensuous heavens). Kāmāvacara cittas are typical of the kāmabhūmi and generate rebirth into it, yet they can also arise in the fine-material and immaterial planes of existence.",
                "es": "Según Bhikkhu Bodhi (CMA I, §3), es fundamental distinguir kāmāvacara (esfera de conciencia) de kāmabhūmi (el plano sensorial de existencia, que comprende 11 reinos: 4 estados de privación, el reino humano y 6 cielos sensoriales). Los cittas kāmāvacara son típicos del kāmabhūmi, pero también pueden surgir en los planos rūpa y arūpa."
            },
            "bodhiRef": "CMA I, §§3–17 (Guide, pp. 31–54)"
        },
        "seeAlso": ["rūpāvacara", "arūpāvacara", "lokuttara", "bhūmi", "kāmabhūmi"]
    },

    "rūpāvacara": {
        "meaning": {
            "pt": "Pertencente à esfera da matéria sutil; consciência da esfera da forma sutil (15 cittas dos rūpajjhānas: 5 salutares, 5 resultantes e 5 funcionais).",
            "en": "Pertaining to the fine-material sphere; fine-material-sphere consciousness (15 cittas of the rūpajjhānas: 5 wholesome, 5 resultant, and 5 functional).",
            "es": "Perteneciente a la esfera de la materia sutil; conciencia de la esfera de la forma sutil (15 cittas de los rūpajjhānas: 5 saludables, 5 resultantes y 5 funcionales)."
        },
        "grammar": "adj./nt. (rūpa + avacara)",
        "grammarLocalized": {
            "pt": "Adjetivo / Substantivo neutro (composto Sattamī-Tappurisa)",
            "en": "Adjective / Neuter noun (Sattamī-Tappurisa compound)",
            "es": "Adjetivo / Sustantivo neutro (compuesto Sattamī-Tappurisa)"
        },
        "root": "rūpa + ava + √car + a",
        "etymology": {
            "pt": "De rūpa (matéria sutil / plano dos Brahmās com forma, ou objeto de meditação baseado na forma como os kasiṇas) + avacara (que frequenta ou se move em).",
            "en": "From rūpa (fine-material realm / Brahmā world with form, or form-based meditation object such as the kasiṇas) + avacara (frequenting, moving about in).",
            "es": "De rūpa (reino de la materia sutil / mundo de Brahmā con forma, u objeto de meditación basado en la forma) + avacara (que frecuenta o se mueve en)."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Locativo (Sattamī-Tappurisa)",
                "en": "Locative Determinative Compound (Sattamī-Tappurisa)",
                "es": "Compuesto Determinativo Locativo (Sattamī-Tappurisa)"
            },
            "viggaha": "rūpe (rūpabhūmiyaṃ) avacaratī'ti = rūpāvacaraṃ",
            "literal": {
                "pt": "Aquilo que frequenta ou é próprio do plano da matéria sutil (rūpabhūmi).",
                "en": "That which moves about in or frequents the fine-material plane (rūpabhūmi).",
                "es": "Aquello que se mueve o frecuenta el plano de la materia sutil (rūpabhūmi)."
            },
            "parts": [
                {"part": "rūpa", "gloss": {"pt": "matéria sutil / forma", "en": "fine-material / form", "es": "materia sutil / forma"}},
                {"part": "avacara", "gloss": {"pt": "esfera que frequenta", "en": "sphere frequented", "es": "esfera que frecuenta"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Plano de Consciência Sublime (Mahaggata Cittabhūmi — 2º dos 4 planos)",
                "en": "Sublime Plane of Consciousness (Mahaggata Cittabhūmi — 2nd of 4 planes)",
                "es": "Plano de Conciencia Sublime (Mahaggata Cittabhūmi — 2º de 4 planos)"
            },
            "category": {
                "pt": "15 Cittas Rūpāvacara: 5 Kusala + 5 Vipāka + 5 Kiriya (distribuídos nos 5 Jhānas)",
                "en": "15 Rūpāvacara Cittas: 5 Kusala + 5 Vipāka + 5 Kiriya (distributed across the 5 Jhānas)",
                "es": "15 Cittas Rūpāvacara: 5 Kusala + 5 Vipāka + 5 Kiriya (distribuidos en los 5 Jhānas)"
            },
            "philosophy": {
                "pt": "Diferentemente do Suttanta (que divide os rūpajjhānas em 4 níveis porque vitakka e vicāra são abandonados juntos na transição do 1º para o 2º jhāna), o método do Abhidhamma divide os cittas rūpāvacara em 5 níveis de jhāna (pañcakanaya): (1) vitakka, vicāra, pīti, sukha, ekaggatā; (2) vicāra, pīti, sukha, ekaggatā; (3) pīti, sukha, ekaggatā; (4) sukha, ekaggatā; (5) upekkhā, ekaggatā. Os 5 kusala são alcançados por puthujjanas e sekkhas em meditação; os 5 vipāka atuam como paṭisandhi, bhavaṅga e cuti nos 15 planos de rūpabhūmi (exceto asaññasatta); os 5 kiriya são exclusivos de Buddhas e Arahants.",
                "en": "Unlike the Suttanta method (which reckons 4 rūpajjhānas by abandoning vitakka and vicāra together after the 1st jhāna), the Abhidhamma method divides rūpāvacara cittas into 5 jhāna stages (pañcakanaya): (1) vitakka, vicāra, pīti, sukha, ekaggatā; (2) vicāra, pīti, sukha, ekaggatā; (3) pīti, sukha, ekaggatā; (4) sukha, ekaggatā; (5) upekkhā, ekaggatā. The 5 kusala are attained by worldlings and trainees; the 5 vipāka serve as rebirth-linking, bhavaṅga, and death consciousness in the fine-material planes; the 5 kiriya are exclusive to Buddhas and Arahants.",
                "es": "A diferencia del método de los Suttas (que enumera 4 rūpajjhānas), el Abhidhamma divide los cittas rūpāvacara en 5 niveles de jhāna (pañcakanaya) mediante la eliminación progresiva de vitakka, vicāra, pīti y sukha, culminando en upekkhā y ekaggatā en el 5º jhāna."
            },
            "bodhiRef": "CMA I, §§18–21 (Guide, pp. 54–62)"
        },
        "seeAlso": ["kāmāvacara", "arūpāvacara", "mahaggata", "jhāna", "rūpabhūmi"]
    },

    "arūpāvacara": {
        "meaning": {
            "pt": "Pertencente à esfera imaterial; consciência das absorções sem forma (12 cittas dos arūpajjhānas: 4 salutares, 4 resultantes e 4 funcionais).",
            "en": "Pertaining to the immaterial sphere; immaterial-sphere consciousness (12 cittas of the arūpajjhānas: 4 wholesome, 4 resultant, and 4 functional).",
            "es": "Perteneciente a la esfera inmaterial; conciencia de las absorciones sin forma (12 cittas de los arūpajjhānas: 4 saludables, 4 resultantes y 4 funcionales)."
        },
        "grammar": "adj./nt. (na > a + rūpa + avacara)",
        "grammarLocalized": {
            "pt": "Adjetivo / Substantivo neutro (composto Sattamī-Tappurisa com prefixo negativo)",
            "en": "Adjective / Neuter noun (Sattamī-Tappurisa compound with negative prefix)",
            "es": "Adjetivo / Sustantivo neutro (compuesto Sattamī-Tappurisa con prefijo negativo)"
        },
        "root": "na > a (sem) + rūpa (matéria) + ava + √car + a",
        "etymology": {
            "pt": "De arūpa (a- privativo + rūpa = imaterial, sem forma material) + avacara (que frequenta ou pertence ao plano imaterial, arūpabhūmi).",
            "en": "From arūpa (privative a- + rūpa = immaterial, formless) + avacara (frequenting or pertaining to the immaterial plane, arūpabhūmi).",
            "es": "De arūpa (a- privativo + rūpa = inmaterial, sin forma) + avacara (que frecuenta o pertenece al plano inmaterial, arūpabhūmi)."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Locativo (Sattamī-Tappurisa)",
                "en": "Locative Determinative Compound (Sattamī-Tappurisa)",
                "es": "Compuesto Determinativo Locativo (Sattamī-Tappurisa)"
            },
            "viggaha": "arūpe (arūpabhūmiyaṃ) avacaratī'ti = arūpāvacaraṃ",
            "literal": {
                "pt": "Aquilo que frequenta ou se move no plano imaterial de existência.",
                "en": "That which moves about in or frequents the immaterial plane of existence.",
                "es": "Aquello que se mueve o frecuenta el plano inmaterial de existencia."
            },
            "parts": [
                {"part": "arūpa", "gloss": {"pt": "imaterial, sem forma (na + rūpa)", "en": "immaterial, formless (na + rūpa)", "es": "inmaterial, sin forma (na + rūpa)"}},
                {"part": "avacara", "gloss": {"pt": "que frequenta, esfera", "en": "frequenting, sphere", "es": "que frecuenta, esfera"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Plano de Consciência Sublime (Mahaggata Cittabhūmi — 3º dos 4 planos)",
                "en": "Sublime Plane of Consciousness (Mahaggata Cittabhūmi — 3rd of 4 planes)",
                "es": "Plano de Conciencia Sublime (Mahaggata Cittabhūmi — 3º de 4 planos)"
            },
            "category": {
                "pt": "12 Cittas Arūpāvacara: 4 Kusala + 4 Vipāka + 4 Kiriya",
                "en": "12 Arūpāvacara Cittas: 4 Kusala + 4 Vipāka + 4 Kiriya",
                "es": "12 Cittas Arūpāvacara: 4 Kusala + 4 Vipāka + 4 Kiriya"
            },
            "philosophy": {
                "pt": "As 12 consciências arūpāvacara diferenciam-se exclusivamente por seus quatro objetos (ālambanabhedena), e não por seus fatores de jhāna: todas as 12 possuem exatamente os mesmos dois fatores do 5º jhāna (upekkhā e ekaggatā). Os 4 estágios são: (1) ākāsānañcāyatana (base do espaço infinito, que toma o espaço deixado pela remoção do kasiṇa); (2) viññāṇañcāyatana (base da consciência infinita, que toma o 1º citta imaterial como objeto); (3) ākiñcaññāyatana (base do nada, que toma o conceito da não-existência do 1º citta imaterial); e (4) nevasaññānāsaññāyatana (base da nem-percepção-nem-não-percepção, que toma o 3º citta imaterial como objeto).",
                "en": "The 12 arūpāvacara cittas are differentiated solely by their four objects (ālambanabhedena), not by their jhāna factors: all 12 possess the exact same two factors of the 5th jhāna (upekkhā and ekaggatā). The 4 bases are: (1) ākāsānañcāyatana (base of infinite space, taking the concept of space left by removing the kasiṇa); (2) viññāṇañcāyatana (base of infinite consciousness, taking the 1st immaterial citta as object); (3) ākiñcaññāyatana (base of nothingness, taking the concept of non-existence of the 1st immaterial citta); and (4) nevasaññānāsaññāyatana (base of neither-perception-nor-non-perception, taking the 3rd immaterial citta as object).",
                "es": "Las 12 conciencias arūpāvacara se diferencian exclusivamente por sus cuatro objetos (ālambanabhedena), no por sus factores de jhāna: las 12 comparten los mismos dos factores del 5º jhāna (upekkhā y ekaggatā): (1) ākāsānañcāyatana, (2) viññāṇañcāyatana, (3) ākiñcaññāyatana y (4) nevasaññānāsaññāyatana."
            },
            "bodhiRef": "CMA I, §§22–25 (Guide, pp. 62–66)"
        },
        "seeAlso": ["rūpāvacara", "mahaggata", "ākāsānañcāyatana", "viññāṇañcāyatana", "ākiñcaññāyatana", "nevasaññānāsaññāyatana"]
    },

    "lokuttara": {
        "meaning": {
            "pt": "Supramundano; transcendental; que transcende o mundo condicionado dos cinco agregados de apego (8 ou 40 cittas supramundanos + Nibbāna + seus cetasikas associados).",
            "en": "Supramundane; transcendental; transcending the conditioned world of the five aggregates of clinging (8 or 40 supramundane cittas + Nibbāna + their associated cetasikas).",
            "es": "Supramundano; trascendental; que trasciende el mundo condicionado de los cinco agregados de apego (8 o 40 cittas supramundanos + Nibbāna + sus cetasikas asociados)."
        },
        "grammar": "adj./nt. (loka + uttara)",
        "grammarLocalized": {
            "pt": "Adjetivo / Substantivo neutro (composto Pañcamī-Tappurisa)",
            "en": "Adjective / Neuter noun (Pañcamī-Tappurisa compound)",
            "es": "Adjetivo / Sustantivo neutro (compuesto Pañcamī-Tappurisa)"
        },
        "root": "loka (√lok + a) + uttara (ud + √tar + a)",
        "etymology": {
            "pt": "De loka (o mundo das formações condicionadas, saṅkhāraloka, de √lok / √luj 'desintegrar-se') + uttara (além de, superior a, que atravessou para o alto, de ud- + √tar 'cruzar, atravessar').",
            "en": "From loka (the world of conditioned formations, saṅkhāraloka, from √lok / √luj 'to crumble/disintegrate') + uttara (beyond, higher, crossed over, from ud- + √tar 'to cross over').",
            "es": "De loka (el mundo de las formaciones condicionadas, saṅkhāraloka) + uttara (más allá de, superior, que ha cruzado hacia arriba, de ud- + √tar 'cruzar')."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Ablativo (Pañcamī-Tappurisa)",
                "en": "Ablative Determinative Compound (Pañcamī-Tappurisa)",
                "es": "Compuesto Determinativo Ablativo (Pañcamī-Tappurisa)"
            },
            "viggaha": "lokā uttaro (lokato uttiṇṇo)'ti = lokuttaro",
            "literal": {
                "pt": "Aquilo que emergiu além do mundo condicionado (loka).",
                "en": "That which has crossed over beyond the conditioned world (loka).",
                "es": "Aquello que ha cruzado más allá del mundo condicionado (loka)."
            },
            "parts": [
                {"part": "loka", "gloss": {"pt": "mundo condicionado (saṅkhāraloka)", "en": "conditioned world (saṅkhāraloka)", "es": "mundo condicionado (saṅkhāraloka)"}},
                {"part": "uttara", "gloss": {"pt": "além de, transcendente, superior", "en": "beyond, transcendent, higher", "es": "más allá de, trascendente, superior"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Plano Supramundano (Lokuttara Bhūmi — 4º plano de consciência + Nibbāna)",
                "en": "Supramundane Plane (Lokuttara Bhūmi — 4th plane of consciousness + Nibbāna)",
                "es": "Plano Supramundano (Lokuttara Bhūmi — 4º plano de conciencia + Nibbāna)"
            },
            "category": {
                "pt": "9 Dhammas Supramundanos (Navavidha Lokuttara Dhamma): 4 Caminhos (Magga), 4 Frutos (Phala) e Nibbāna",
                "en": "9 Supramundane Dhammas (Navavidha Lokuttara Dhamma): 4 Paths (Magga), 4 Fruits (Phala), and Nibbāna",
                "es": "9 Dhammas Supramundanos (Navavidha Lokuttara Dhamma): 4 Caminos (Magga), 4 Frutos (Phala) y Nibbāna"
            },
            "philosophy": {
                "pt": "No Abhidhamma, há 8 cittas lokuttara (ou 40 quando multiplicados pelos 5 níveis de jhāna): os 4 cittas de caminho (sotāpattimagga, sakadāgāmimagga, anāgāmimagga, arahattamagga), que são salutares (kusala) e têm a função de erradicar definitivamente os grilhões (saṃyojana) em um único momento mental; e os 4 cittas de fruto (phala), que são resultantes imediatos (vipāka, por akālikapaccaya) e saboreiam a paz de Nibbāna. Diferentemente dos planos mundanos (lokiya), não existem cittas funcionais (kiriya) supramundanos.",
                "en": "In the Abhidhamma, there are 8 lokuttara cittas (or 40 when multiplied by the 5 jhāna levels): the 4 path cittas (sotāpattimagga, sakadāgāmimagga, anāgāmimagga, arahattamagga), which are wholesome (kusala) and perform the function of permanently eradicating fetters (saṃyojana) in a single mind-moment; and the 4 fruition cittas (phala), which are immediate resultants (vipāka) experiencing the peace of Nibbāna. Unlike the mundane planes (lokiya), there are no supramundane functional (kiriya) cittas.",
                "es": "En el Abhidhamma, hay 8 cittas lokuttara (o 40 al multiplicarse por los 5 niveles de jhāna): los 4 cittas de camino (magga), que son saludables (kusala) y erradican definitivamente las trabas (saṃyojana) en un único momento mental; y los 4 cittas de fruto (phala), que son resultantes inmediatos (vipāka). A diferencia de los planos mundanos (lokiya), no existen cittas funcionales (kiriya) supramundanos."
            },
            "bodhiRef": "CMA I, §§26–31 (Guide, pp. 66–73)"
        },
        "seeAlso": ["lokiya", "magga", "phala", "nibbāna", "sotāpatti", "arahatta"]
    },

    # ── NATUREZAS ÉTICAS E QUALIFICADORES (JĀTI & COMPOSTOS DO CAP. I) ────────
    "kusala": {
        "meaning": {
            "pt": "Salutar; hábil; benéfico; mentalmente saudável, moralmente irrepreensível e produtor de resultados agradáveis (21 ou 37 cittas kusala: 8 kāmāvacara, 5 rūpāvacara, 4 arūpāvacara, 4 ou 20 lokuttara).",
            "en": "Wholesome; skillful; mentally healthy, morally blameless, and productive of pleasant results (21 or 37 kusala cittas: 8 kāmāvacara, 5 rūpāvacara, 4 arūpāvacara, 4 or 20 lokuttara).",
            "es": "Saludable; hábil; benéfico; mentalmente sano, moralmente irreprochable y productor de resultados agradables (21 o 37 cittas kusala: 8 kāmāvacara, 5 rūpāvacara, 4 arūpāvacara, 4 o 20 lokuttara)."
        },
        "grammar": "adj./nt.",
        "grammarLocalized": {
            "pt": "Adjetivo / Substantivo neutro (1ª das 3/4 naturezas éticas, jāti)",
            "en": "Adjective / Neuter noun (1st of the ethical natures, jāti)",
            "es": "Adjetivo / Sustantivo neutro (1ª de las naturalezas éticas, jāti)"
        },
        "root": "ku (mal/corrupção) + √sal (sacudir/mover) ou √kus (cortar) + ala",
        "etymology": {
            "pt": "No Atthasālinī (38–39), kusala é explicado por quatro sentidos exegéticos: (1) ārogya (saúde mental, livre da doença dos kilesas); (2) anavajja (irrepreensibilidade moral); (3) kosallasambhūta (nascido da sabedoria/habilidade); e (4) sukha-vipāka (produtor de resultado feliz). Etimologicamente analisado como aquilo que sacode/remove (salana) o que é vil (kucchita), ou que corta (kusana) as impurezas como a erva kusa.",
            "en": "In the Atthasālinī (38–39), kusala is explained by four exegetical senses: (1) ārogya (mental health, free from the sickness of defilements); (2) anavajja (moral blamelessness); (3) kosallasambhūta (born of wisdom/skill); and (4) sukha-vipāka (productive of happy results). Etymologically analyzed as that which shakes off (salana) what is vile (kucchita), or cuts off (kusana) defilements like kusa grass.",
            "es": "En el Atthasālinī (38–39), kusala se explica por cuatro sentidos exegéticos: (1) ārogya (salud mental), (2) anavajja (irreprochabilidad moral), (3) kosallasambhūta (nacido de la habilidad/sabiduría) y (4) sukha-vipāka (productor de resultado feliz)."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Natureza Ética Kármica (Jāti — Citta & Cetasika)",
                "en": "Kammic Ethical Nature (Jāti — Citta & Cetasika)",
                "es": "Naturaleza Ética Kármica (Jāti — Citta & Cetasika)"
            },
            "category": {
                "pt": "21 (ou 37) Cittas Kusala: 8 Mahākusala + 5 Rūpāvacara + 4 Arūpāvacara + 4 (ou 20) Lokuttara Magga",
                "en": "21 (or 37) Kusala Cittas: 8 Mahākusala + 5 Rūpāvacara + 4 Arūpāvacara + 4 (or 20) Lokuttara Magga",
                "es": "21 (o 37) Cittas Kusala: 8 Mahākusala + 5 Rūpāvacara + 4 Arūpāvacara + 4 (o 20) Lokuttara Magga"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Irrepreensibilidade moral e produzir resultados felizes (anavajja-sukhavipāka-lakkhaṇa).",
                    "en": "Moral blamelessness and producing happy results (anavajja-sukhavipāka-lakkhaṇa).",
                    "es": "Irreprochabilidad moral y producir resultados felices (anavajja-sukhavipāka-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Destruir ou dissipar estados prejudiciais (akusalaviddhaṃsana-rasa).",
                    "en": "Destroying or dispelling unwholesome states (akusalaviddhaṃsana-rasa).",
                    "es": "Destruir o disipar estados perjudiciales (akusalaviddhaṃsana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Pureza mental (vodāna-paccupaṭṭhāna).",
                    "en": "Mental purity or cleansing (vodāna-paccupaṭṭhāna).",
                    "es": "Pureza o limpieza mental (vodāna-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Atenção sábia / criteriosa (yoniso manasikāra-padaṭṭhāna).",
                    "en": "Wise or thorough attention (yoniso manasikāra-padaṭṭhāna).",
                    "es": "Atención sabia o minuciosa (yoniso manasikāra-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Todo citta kusala é necessariamente acompanhado pelas raízes salutares não-cobiça (alobha) e não-ódio (adosa), podendo ser dissociado ou associado à terceira raiz, não-delusão/sabedoria (amoha/paññā). Nos Arahants, os atos salutares mundanos e sublimes deixam de ser kusala (pois não acumulam novo kamma para renascimento futuro) e ocorrem como cittas funcionais (kiriya).",
                "en": "Every kusala citta is necessarily accompanied by the wholesome roots of non-greed (alobha) and non-hatred (adosa), and may be either associated with or dissociated from the third root, non-delusion/wisdom (amoha/paññā). In Arahants, mundane and sublime wholesome acts cease to be kusala (as they no longer generate kamma for future rebirth) and occur instead as functional cittas (kiriya).",
                "es": "Todo citta kusala está necesariamente acompañado por las raíces saludables de no-codicia (alobha) y no-odio (adosa), pudiendo estar asociado o disociado de la sabiduría (amoha/paññā). En los Arahants, los actos mundanos y sublimes ocurren como cittas funcionales (kiriya)."
            },
            "bodhiRef": "CMA I, §3 & §13 (Guide, pp. 33, 47–51)"
        },
        "seeAlso": ["akusala", "vipāka", "kiriya", "abyākata", "sobhana", "alobha", "adosa", "amoha"]
    },

    "akusala": {
        "meaning": {
            "pt": "Prejudicial; inábil; insalubre; estado mental doentio, moralmente repreensível e produtor de resultados dolorosos (12 cittas akusala e 14 cetasikas akusala).",
            "en": "Unwholesome; unskillful; mentally unhealthy, morally blameworthy, and productive of painful results (12 akusala cittas and 14 akusala cetasikas).",
            "es": "Perjudicial; inhábil; insano; estado mental enfermizo, moralmente reprobable y productor de resultados dolorosos (12 cittas akusala y 14 cetasikas akusala)."
        },
        "grammar": "adj./nt. (na > a + kusala)",
        "grammarLocalized": {
            "pt": "Adjetivo / Substantivo neutro (composto negativo Nañ-Tappurisa)",
            "en": "Adjective / Neuter noun (negative compound Nañ-Tappurisa)",
            "es": "Adjetivo / Sustantivo neutro (compuesto negativo Nañ-Tappurisa)"
        },
        "root": "na > a (não) + kusala (hábil/salutar)",
        "etymology": {
            "pt": "Formado pelo prefixo negativo a- (de na) + kusala (salutar, hábil). Significa o oposto direto de kusala: mentalmente enfermo, nascido da ignorância (akosallasambhūta), moralmente censurável (sāvajja) e produtor de fruto doloroso (dukkha-vipāka).",
            "en": "Formed from the negative prefix a- (from na) + kusala (wholesome, skillful). Signifies the direct opposite of kusala: mentally unhealthy, born of unskillfulness (akosallasambhūta), morally blameworthy (sāvajja), and productive of painful results (dukkha-vipāka).",
            "es": "Formado por el prefijo negativo a- (de na) + kusala (saludable, hábil). Significa el opuesto directo de kusala: mentalmente enfermo, moralmente reprobable (sāvajja) y productor de frutos dolorosos (dukkha-vipāka)."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Negativo (Nañ-Tappurisa)",
                "en": "Negative Determinative Compound (Nañ-Tappurisa)",
                "es": "Compuesto Determinativo Negativo (Nañ-Tappurisa)"
            },
            "viggaha": "na kusalaṃ = akusalaṃ",
            "literal": {
                "pt": "Aquilo que não é salutar nem hábil.",
                "en": "That which is not wholesome or skillful.",
                "es": "Aquello que no es saludable ni hábil."
            },
            "parts": [
                {"part": "a (na)", "gloss": {"pt": "não, oposto a", "en": "not, opposed to", "es": "no, opuesto a"}},
                {"part": "kusala", "gloss": {"pt": "salutar, hábil", "en": "wholesome, skillful", "es": "saludable, hábil"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Natureza Ética Kármica Prejudicial (Akusala Jāti)",
                "en": "Unwholesome Kammic Ethical Nature (Akusala Jāti)",
                "es": "Naturaleza Ética Kármica Perjudicial (Akusala Jāti)"
            },
            "category": {
                "pt": "12 Cittas Akusala (8 Lobhamūla + 2 Dosamūla + 2 Mohamūla) e 14 Cetasikas Akusala",
                "en": "12 Akusala Cittas (8 Lobhamūla + 2 Dosamūla + 2 Mohamūla) and 14 Akusala Cetasikas",
                "es": "12 Cittas Akusala (8 Lobhamūla + 2 Dosamūla + 2 Mohamūla) y 14 Cetasikas Akusala"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Repreensibilidade moral e produzir resultados dolorosos (sāvajja-dukkhavipāka-lakkhaṇa).",
                    "en": "Moral blameworthiness and producing painful results (sāvajja-dukkhavipāka-lakkhaṇa).",
                    "es": "Reprobabilidad moral y producir resultados dolorosos (sāvajja-dukkhavipāka-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Causar dano e obstruir os estados salutares (anatthajanana-rasa).",
                    "en": "Causing harm and obstructing wholesome states (anatthajanana-rasa).",
                    "es": "Causar daño y obstruir los estados saludables (anatthajanana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Impureza e aflição mental (saṅkilesa-paccupaṭṭhāna).",
                    "en": "Mental defilement and affliction (saṅkilesa-paccupaṭṭhāna).",
                    "es": "Impureza y aflicción mental (saṅkilesa-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Atenção insensata / não criteriosa (ayoniso manasikāra-padaṭṭhāna).",
                    "en": "Unwise or superficial attention (ayoniso manasikāra-padaṭṭhāna).",
                    "es": "Atención insensata o superficial (ayoniso manasikāra-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Todos os 12 cittas akusala pertencem exclusivamente à esfera sensorial (kāmāvacara) e contêm invariavelmente 4 cetasikas akusala universais (sabbākusalasādhāraṇa): delusão (moha), ausência de vergonha moral (ahirika), ausência de temor moral (anottappa) e inquietação (uddhacca). Classificam-se pela raiz predominante em: 8 enraizados na cobiça (lobhamūla), 2 enraizados no ódio (dosamūla) e 2 enraizados na pura delusão (mohamūla).",
                "en": "All 12 akusala cittas pertain exclusively to the sense sphere (kāmāvacara) and invariably contain the 4 universal unwholesome cetasikas (sabbākusalasādhāraṇa): delusion (moha), shamelessness (ahirika), fearlessness of wrongdoing (anottappa), and restlessness (uddhacca). They are classified by their prominent root into: 8 rooted in greed (lobhamūla), 2 rooted in hatred (dosamūla), and 2 rooted in sheer delusion (mohamūla).",
                "es": "Todos los 12 cittas akusala pertenecen exclusivamente a la esfera sensorial (kāmāvacara) y contienen invariablemente los 4 cetasikas akusala universales (sabbākusalasādhāraṇa): moha, ahirika, anottappa y uddhacca. Se dividen en 8 enraizados en la codicia (lobhamūla), 2 en el odio (dosamūla) y 2 en la pura ilusión (mohamūla)."
            },
            "bodhiRef": "CMA I, §§4–7 (Guide, pp. 34–41); II, §4 (pp. 82–85)"
        },
        "seeAlso": ["kusala", "lobha", "dosa", "moha", "lobhamūlacitta", "dosamūlacitta", "mohamūlacitta"]
    },

    "vipāka": {
        "meaning": {
            "pt": "Resultante; fruto kármico; estado de consciência ou fator mental eticamente indeterminado (abyākata) que surge pela maturação de ações volitivas (kamma) salutares ou prejudiciais passadas (36 ou 52 cittas vipāka).",
            "en": "Resultant; kamma-result; an ethically indeterminate (abyākata) state of consciousness or mental factor arising through the ripening of past wholesome or unwholesome volitional actions (kamma) (36 or 52 vipāka cittas).",
            "es": "Resultante; fruto kármico; estado de conciencia o factor mental éticamente indeterminado (abyākata) que surge por la maduración de acciones volitivas (kamma) saludables o perjudiciales pasadas (36 o 52 cittas vipāka)."
        },
        "grammar": "masc./adj. (vi + √pac + *a)",
        "grammarLocalized": {
            "pt": "Substantivo masculino / Adjetivo (vi [completamente] + √pac [cozinhar, amadurecer] + *a)",
            "en": "Masculine noun / Adjective (vi [thoroughly] + √pac [to cook, ripen, mature] + *a)",
            "es": "Sustantivo masculino / Adjetivo (vi [completamente] + √pac [cocinar, madurar] + *a)"
        },
        "root": "vi (completamente) + √pac (amadurecer / cozinhar) + *a",
        "etymology": {
            "pt": "De vi- (intensivo: completamente, distintamente) + raiz √pac ('cozinhar, amadurecer, maturar'), com fortalecimento vocálico (vuddhi: pac > pāk). Significa literalmente o 'amadurecimento' completo das sementes kármicas plantadas pela volição (cetanā).",
            "en": "From vi- (intensive: thoroughly, distinctly) + root √pac ('to cook, ripen, mature'), with vowel strengthening (vuddhi: pac > pāk). Literally signifies the full 'ripening' or 'maturation' of kammic seeds sown by volition (cetanā).",
            "es": "De vi- (completamente) + raíz √pac ('cocinar, madurar'), con fortalecimiento vocálico (pac > pāk). Significa literalmente la 'maduración' completa de las semillas kármicas sembradas por la volición (cetanā)."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Natureza Indeterminada Resultante (Abyākata Vipāka Jāti — Citta & Cetasika)",
                "en": "Resultant Indeterminate Nature (Abyākata Vipāka Jāti — Citta & Cetasika)",
                "es": "Naturaleza Indeterminada Resultante (Abyākata Vipāka Jāti — Citta & Cetasika)"
            },
            "category": {
                "pt": "36 (ou 52) Cittas Vipāka: 7 Akusalavipāka + 8 Ahetukakusalavipāka + 8 Mahāvipāka + 5 Rūpāvacara + 4 Arūpāvacara + 4 (ou 20) Lokuttara Phala",
                "en": "36 (or 52) Vipāka Cittas: 7 Akusalavipāka + 8 Ahetukakusalavipāka + 8 Mahāvipāka + 5 Rūpāvacara + 4 Arūpāvacara + 4 (or 20) Lokuttara Phala",
                "es": "36 (o 52) Cittas Vipāka: 7 Akusalavipāka + 8 Ahetukakusalavipāka + 8 Mahāvipāka + 5 Rūpāvacara + 4 Arūpāvacara + 4 (o 20) Lokuttara Phala"
            },
            "philosophy": {
                "pt": "No Abhidhamma, tanto o kamma quanto seu vipāka são estritamente mentais (a matéria produzida pelo kamma é chamada kammasamuṭṭhānarūpa, não vipāka). Os cittas vipāka nunca geram novo kamma; são passivos e recepcionam objetos sem esforço ativo, desempenhando funções como consciência de renascimento (paṭisandhi), fluxo vital (bhavaṅga), morte (cuti), as cinco consciências sensoriais (pañcaviññāṇa), recepção (sampaṭicchana), investigação (santīraṇa), retenção (tadārammaṇa) e fruição supramundana (phala).",
                "en": "In the Abhidhamma, both kamma and its vipāka are strictly mental (matter produced by kamma is termed kammasamuṭṭhānarūpa, not vipāka). Vipāka cittas never generate new kamma; they are kammically passive and perform functions such as rebirth-linking (paṭisandhi), life-continuum (bhavaṅga), death (cuti), fivefold sense consciousness (pañcaviññāṇa), receiving (sampaṭicchana), investigating (santīraṇa), registration (tadārammaṇa), and supramundane fruition (phala).",
                "es": "En el Abhidhamma, tanto el kamma como su vipāka son estrictamente mentales. Los cittas vipāka nunca generan nuevo kamma; desempeñan funciones pasivas como reconexión (paṭisandhi), continuo vital (bhavaṅga), muerte (cuti), conciencias sensoriales (pañcaviññāṇa), recepción (sampaṭicchana), investigación (santīraṇa), registro (tadārammaṇa) y fruición (phala)."
            },
            "bodhiRef": "CMA I, §3, §§8–9, §14 (Guide, pp. 33, 41–44, 51–52); V, §§27–33 (pp. 210–219)"
        },
        "seeAlso": ["kamma", "kiriya", "kusala", "akusala", "abyākata", "phala"]
    },

    "kiriya": {
        "meaning": {
            "pt": "Funcional; inoperante karmicamente; consciência ativa que executa uma função cognitiva ou meditativa sem deixar resíduo ou fruto kármico (20 cittas kiriya: 3 ahetuka, 8 mahākiriya, 5 rūpāvacara, 4 arūpāvacara).",
            "en": "Functional; kammically inoperative; active consciousness performing a cognitive or meditative function without generating any kammic result (20 kiriya cittas: 3 ahetuka, 8 mahākiriya, 5 rūpāvacara, 4 arūpāvacara).",
            "es": "Funcional; kármicamente inoperante; conciencia activa que ejecuta una función cognitiva o meditativa sin generar resultado kármico (20 cittas kiriya: 3 ahetuka, 8 mahākiriya, 5 rūpāvacara, 4 arūpāvacara)."
        },
        "grammar": "fem./adj. (de √kar + iya)",
        "grammarLocalized": {
            "pt": "Substantivo feminino / Adjetivo (variante epentética de kriyā, da raiz √kar 'fazer, agir')",
            "en": "Feminine noun / Adjective (epenthetic form of kriyā, from root √kar 'to do, act')",
            "es": "Sustantivo femenino / Adjetivo (variante epentética de kriyā, de la raíz √kar 'hacer, actuar')"
        },
        "root": "√kar (fazer / agir) + iya",
        "etymology": {
            "pt": "De √kar ('fazer, executar') + sufixo -iya (kriyā > kiriya). Significa 'mera ação' (karaṇamatta), isto é, uma atividade que se esgota no próprio ato presente sem projetar semente kármica para o futuro.",
            "en": "From √kar ('to do, perform') + suffix -iya (kriyā > kiriya). Signifies 'mere action' (karaṇamatta), an activity completed in the present act without projecting any kammic seed into the future.",
            "es": "De √kar ('hacer, ejecutar') + sufijo -iya (kriyā > kiriya). Significa 'mera acción' (karaṇamatta), una actividad que se agota en el acto presente sin proyectar semilla kármica hacia el futuro."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Natureza Indeterminada Funcional (Abyākata Kiriya Jāti — Citta & Cetasika)",
                "en": "Functional Indeterminate Nature (Abyākata Kiriya Jāti — Citta & Cetasika)",
                "es": "Naturaleza Indeterminada Funcional (Abyākata Kiriya Jāti — Citta & Cetasika)"
            },
            "category": {
                "pt": "20 Cittas Kiriya: 3 Ahetukakiriya (comuns ou de Arahant) + 17 Sobhanakiriya (exclusivos de Buddhas e Arahants)",
                "en": "20 Kiriya Cittas: 3 Ahetukakiriya + 17 Sobhanakiriya (exclusive to Buddhas and Arahants)",
                "es": "20 Cittas Kiriya: 3 Ahetukakiriya + 17 Sobhanakiriya (exclusivos de Buddhas y Arahants)"
            },
            "philosophy": {
                "pt": "Dos 20 cittas kiriya, dois são comuns a todos os seres: pañcadvārāvajjana (advertência nas cinco portas) e manodvārāvajjana (advertência na porta da mente, que também realiza a função de determinação, voṭṭhabbana). Os outros 18 cittas kiriya são exclusivos de Buddhas e Arahants: a consciência produtora do sorriso (hasituppādacitta), os 8 mahākiriyacittas, os 5 rūpāvacarakiriyacittas e os 4 arūpāvacarakiriyacittas. Como os Arahants erradicaram toda ignorância e anseio, suas ações éticas e absorções meditativas não geram vipāka futuro, sendo puramente funcionais.",
                "en": "Of the 20 kiriya cittas, two are common to all beings: five-sense-door adverting (pañcadvārāvajjana) and mind-door adverting (manodvārāvajjana, which also performs determining, voṭṭhabbana). The remaining 18 kiriya cittas are exclusive to Buddhas and Arahants: smile-producing consciousness (hasituppādacitta), the 8 mahākiriyacittas, the 5 rūpāvacarakiriyacittas, and the 4 arūpāvacarakiriyacittas. Because Arahants have eradicated ignorance and craving, their ethical deeds and meditative absorptions generate no future vipāka and are purely functional.",
                "es": "De los 20 cittas kiriya, dos son comunes a todos los seres (pañcadvārāvajjana y manodvārāvajjana). Los otros 18 (hasituppāda, 8 mahākiriya, 5 rūpāvacarakiriya y 4 arūpāvacarakiriya) son exclusivos de Buddhas y Arahants, cuyas acciones no producen vipāka futuro."
            },
            "bodhiRef": "CMA I, §3, §10, §15 (Guide, pp. 33, 44–46, 52)"
        },
        "seeAlso": ["vipāka", "kusala", "abyākata", "pañcadvārāvajjana", "manodvārāvajjana", "hasituppāda", "mahākiriya"]
    },

    # ── FÓRMULAS COMPOSTAS DO CAPÍTULO I (SAMĀSA PEDAGOGY) ───────────────────
    "somanassasahagata": {
        "meaning": {
            "pt": "Acompanhado de alegria mental; conjugado com sensação mental agradável (qualifica 62 dos 121 cittas).",
            "en": "Accompanied by joy; conjoined with pleasant mental feeling (qualifies 62 of the 121 cittas).",
            "es": "Acompañado de alegría mental; unido a sensación mental agradable (califica 62 de los 121 cittas)."
        },
        "grammar": "adj. composto (somanassa + saha + gata)",
        "grammarLocalized": {
            "pt": "Adjetivo composto (Tatiyā-Tappurisa-gabbha Bahubbīhi)",
            "en": "Compound adjective (Tatiyā-Tappurisa-gabbha Bahubbīhi)",
            "es": "Adjetivo compuesto (Tatiyā-Tappurisa-gabbha Bahubbīhi)"
        },
        "root": "su + √man + as + ya + saha + √gam + ta",
        "etymology": {
            "pt": "Formado por somanassa (de su- [bom, agradável] + manas [mente] + -ya = estado de bom ânimo mental, alegria) + sahagata (saha [junto com] + gata [ido, ocorrido, de √gam + -ta]).",
            "en": "Formed from somanassa (from su- [good, pleasant] + manas [mind] + -ya = pleasant mental state, joy) + sahagata (saha [together with] + gata [gone, proceeded, from √gam + -ta]).",
            "es": "Formado por somanassa (de su- [bueno, agradable] + manas [mente] + -ya = estado mental agradable, alegría) + sahagata (saha [junto con] + gata [ido, ocurrido, de √gam + -ta])."
        },
        "samasa": {
            "type": {
                "pt": "Composto Relativo (Bahubbīhi) contendo relação instrumental (Tatiyā-Tappurisa)",
                "en": "Relative Compound (Bahubbīhi) containing an instrumental relation (Tatiyā-Tappurisa)",
                "es": "Compuesto Relativo (Bahubbīhi) con relación instrumental (Tatiyā-Tappurisa)"
            },
            "viggaha": "somanassena saha gataṃ (ekuppādādibhāvena pavattaṃ)'ti = somanassasahagataṃ (cittaṃ)",
            "literal": {
                "pt": "Aquela consciência que ocorre (gata) juntamente com (saha) a sensação de alegria mental (somanassa).",
                "en": "That consciousness which proceeds (gata) together with (saha) the feeling of mental joy (somanassa).",
                "es": "Aquella conciencia que transcurre (gata) juntamente con (saha) la sensación de alegría mental (somanassa)."
            },
            "parts": [
                {"part": "somanassa", "gloss": {"pt": "alegria mental (su + manas + ya)", "en": "mental joy (su + manas + ya)", "es": "alegría mental (su + manas + ya)"}},
                {"part": "saha", "gloss": {"pt": "junto com, em união", "en": "together with, conjoined", "es": "junto con, en unión"}},
                {"part": "gata", "gloss": {"pt": "ido, ocorrido (√gam + ta)", "en": "gone, occurred (√gam + ta)", "es": "ido, ocurrido (√gam + ta)"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Qualificador Afetivo de Citta (Vedanā-bheda)",
                "en": "Affective Qualifier of Citta (Vedanā-bheda)",
                "es": "Calificador Afectivo de Citta (Vedanā-bheda)"
            },
            "category": {
                "pt": "Presente em 18 Cittas Kāmāvacara (4 Lobha + 2 Ahetuka + 12 Sobhana) e 44 Cittas de 1º a 4º Jhāna (12 Mahaggata + 32 Lokuttara) = 62 Cittas",
                "en": "Present in 18 Kāmāvacara Cittas (4 Lobha + 2 Ahetuka + 12 Sobhana) and 44 Cittas of the 1st–4th Jhāna (12 Mahaggata + 32 Lokuttara) = 62 Cittas",
                "es": "Presente en 18 Cittas Kāmāvacara (4 Lobha + 2 Ahetuka + 12 Sobhana) y 44 Cittas del 1º al 4º Jhāna (12 Mahaggata + 32 Lokuttara) = 62 Cittas"
            },
            "philosophy": {
                "pt": "Conforme explica Bhikkhu Bodhi (CMA I, §4, p. 35), somanassa é a sensação (vedanā) que é mental (cetasika) em vez de corporal, e agradável em vez de dolorosa ou neutra. O termo sahagata ('acompanhada por') indica que a sensação e a consciência estão inseparavelmente mescladas, assim como as águas de dois rios que se encontram e não podem ser separadas.",
                "en": "As Bhikkhu Bodhi explains (CMA I, §4, p. 35), somanassa is feeling (vedanā) that is mental rather than bodily, and pleasant rather than painful or neutral. The term sahagata ('accompanied by') indicates that the feeling and consciousness are inextricably blended together, like the waters of two rivers meeting.",
                "es": "Como explica Bhikkhu Bodhi (CMA I, §4, p. 35), somanassa es la sensación (vedanā) que es mental en lugar de corporal, y agradable en lugar de dolorosa o neutra. El término sahagata indica que la sensación y la conciencia están inextricablemente mezcladas como las aguas de dos ríos."
            },
            "bodhiRef": "CMA I, §4 (Guide, p. 35); III, §§2–4 (pp. 115–118)"
        },
        "seeAlso": ["somanassa", "upekkhāsahagata", "domanassasahagata", "vedanā", "sahagata"]
    },

    "upekkhāsahagata": {
        "meaning": {
            "pt": "Acompanhado de equanimidade; conjugado com sensação mental neutra (adukkhamasukhā vedanā, que qualifica 55 dos 121 cittas).",
            "en": "Accompanied by equanimity; conjoined with neutral mental feeling (adukkhamasukhā vedanā, qualifying 55 of the 121 cittas).",
            "es": "Acompañado de ecuanimidad; unido a sensación mental neutra (adukkhamasukhā vedanā, que califica 55 de los 121 cittas)."
        },
        "grammar": "adj. composto (upekkhā + saha + gata)",
        "grammarLocalized": {
            "pt": "Adjetivo composto (Tatiyā-Tappurisa-gabbha Bahubbīhi)",
            "en": "Compound adjective (Tatiyā-Tappurisa-gabbha Bahubbīhi)",
            "es": "Adjetivo compuesto (Tatiyā-Tappurisa-gabbha Bahubbīhi)"
        },
        "root": "upa + √ikkh + ā + saha + √gam + ta",
        "etymology": {
            "pt": "De upekkhā (upa [de perto / imparcialmente] + √ikkh [olhar, observar] = olhar com imparcialidade, sensação nem dolorosa nem agradável) + sahagata (acompanhado por).",
            "en": "From upekkhā (upa [closely / evenly] + √ikkh [to look, view] = looking on evenly, neither-painful-nor-pleasant feeling) + sahagata (accompanied by).",
            "es": "De upekkhā (upa [imparcialmente] + √ikkh [mirar, observar] = mirar con ecuanimidad, sensación neutra) + sahagata (acompañado por)."
        },
        "samasa": {
            "type": {
                "pt": "Composto Relativo (Bahubbīhi) com relação instrumental (Tatiyā-Tappurisa)",
                "en": "Relative Compound (Bahubbīhi) with instrumental relation (Tatiyā-Tappurisa)",
                "es": "Compuesto Relativo (Bahubbīhi) con relación instrumental (Tatiyā-Tappurisa)"
            },
            "viggaha": "upekkhāya saha gataṃ = upekkhāsahagataṃ (cittaṃ)",
            "literal": {
                "pt": "Aquela consciência que ocorre juntamente com a sensação neutra de equanimidade.",
                "en": "That consciousness which proceeds together with the neutral feeling of equanimity.",
                "es": "Aquella conciencia que transcurre juntamente con la sensación neutra de ecuanimidad."
            },
            "parts": [
                {"part": "upekkhā", "gloss": {"pt": "equanimidade / sensação neutra (upa + √ikkh)", "en": "equanimity / neutral feeling (upa + √ikkh)", "es": "ecuanimidad / sensación neutra (upa + √ikkh)"}},
                {"part": "saha", "gloss": {"pt": "junto com", "en": "together with", "es": "junto con"}},
                {"part": "gata", "gloss": {"pt": "ido, ocorrido", "en": "gone, proceeded", "es": "ido, ocurrido"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Qualificador Afetivo de Citta (Vedanā-bheda)",
                "en": "Affective Qualifier of Citta (Vedanā-bheda)",
                "es": "Calificador Afectivo de Citta (Vedanā-bheda)"
            },
            "category": {
                "pt": "Presente em 55 Cittas (32 Kāmāvacara + 3 de 5º Rūpajjhāna + 12 Arūpāvacara + 8 Lokuttara de 5º Jhāna)",
                "en": "Present in 55 Cittas (32 Kāmāvacara + 3 of 5th Rūpajjhāna + 12 Arūpāvacara + 8 Lokuttara of 5th Jhāna)",
                "es": "Presente en 55 Cittas (32 Kāmāvacara + 3 de 5º Rūpajjhāna + 12 Arūpāvacara + 8 Lokuttara de 5º Jhāna)"
            },
            "philosophy": {
                "pt": "Atenção à distinção crucial apontada por Bhikkhu Bodhi (CMA I, §4, p. 35; II, §5, p. 86): a palavra upekkhā designa dois cetasikas completamente diferentes no Abhidhamma: (1) upekkhā-vedanā (sensação neutra, nem dolorosa nem agradável, adukkhamasukhā vedanā), que é o que significa na fórmula 'upekkhāsahagata'; e (2) tatramajjhattatā (neutralidade mental ou equilíbrio sublime imparcial), que é um cetasika belo universal. Nos cittas akusala (como os 4 lobhamūla e os 2 mohamūla), 'upekkhāsahagata' refere-se exclusivamente à sensação afetiva neutra (vedanā), nunca à virtude espiritual do equilíbrio mental.",
                "en": "Note the crucial distinction highlighted by Bhikkhu Bodhi (CMA I, §4, p. 35; II, §5, p. 86): the word upekkhā denotes two completely different cetasikas in the Abhidhamma: (1) upekkhā-vedanā (neutral feeling, neither-painful-nor-pleasant feeling, adukkhamasukhā vedanā), which is its meaning in the formula 'upekkhāsahagata'; and (2) tatramajjhattatā (neutrality of mind or sublime impartiality), a universal beautiful cetasika. In akusala cittas (4 lobhamūla and 2 mohamūla), 'upekkhāsahagata' signifies solely neutral feeling (vedanā), never the spiritual virtue of mental balance.",
                "es": "Atención a la distinción crucial señalada por Bhikkhu Bodhi (CMA I, §4, p. 35; II, §5, p. 86): la palabra upekkhā designa dos cetasikas completamente distintos: (1) upekkhā-vedanā (sensación neutra, adukkhamasukhā vedanā), que es lo que significa en 'upekkhāsahagata'; y (2) tatramajjhattatā (neutralidad mental o equilibrio imparcial), un cetasika hermoso universal."
            },
            "bodhiRef": "CMA I, §4 & §6 (Guide, pp. 35, 39); III, §§2–4 (pp. 115–118)"
        },
        "seeAlso": ["upekkhā", "tatramajjhattatā", "somanassasahagata", "domanassasahagata", "vedanā"]
    },

    "domanassasahagata": {
        "meaning": {
            "pt": "Acompanhado de desprazer mental; conjugado com sensação mental dolorosa ou tristeza/desgosto (exclusivo dos 2 cittas enraizados no ódio, dosamūlacittāni).",
            "en": "Accompanied by displeasure; conjoined with painful mental feeling or grief (exclusive to the 2 hatred-rooted cittas, dosamūlacittāni).",
            "es": "Acompañado de desagrado mental; unido a sensación mental dolorosa o aflicción (exclusivo de los 2 cittas enraizados en el odio, dosamūlacittāni)."
        },
        "grammar": "adj. composto (domanassa + saha + gata)",
        "grammarLocalized": {
            "pt": "Adjetivo composto (Tatiyā-Tappurisa-gabbha Bahubbīhi)",
            "en": "Compound adjective (Tatiyā-Tappurisa-gabbha Bahubbīhi)",
            "es": "Adjetivo compuesto (Tatiyā-Tappurisa-gabbha Bahubbīhi)"
        },
        "root": "du + √man + as + ya + saha + √gam + ta",
        "etymology": {
            "pt": "De domanassa (du- [mau, penoso, aflitivo] + manas [mente] + -ya = estado mental aflitivo, desprazer mental) + sahagata (acompanhado por).",
            "en": "From domanassa (du- [bad, painful, afflicted] + manas [mind] + -ya = unpleasant mental state, mental displeasure) + sahagata (accompanied by).",
            "es": "De domanassa (du- [malo, penoso] + manas [mente] + -ya = estado mental desagradable, aflicción) + sahagata (acompañado por)."
        },
        "samasa": {
            "type": {
                "pt": "Composto Relativo (Bahubbīhi) com relação instrumental (Tatiyā-Tappurisa)",
                "en": "Relative Compound (Bahubbīhi) with instrumental relation (Tatiyā-Tappurisa)",
                "es": "Compuesto Relativo (Bahubbīhi) con relación instrumental (Tatiyā-Tappurisa)"
            },
            "viggaha": "domanassena saha gataṃ = domanassasahagataṃ (cittaṃ)",
            "literal": {
                "pt": "Aquela consciência que ocorre juntamente com a sensação de desprazer mental.",
                "en": "That consciousness which proceeds together with the feeling of mental displeasure.",
                "es": "Aquella conciencia que transcurre juntamente con la sensación de desagrado mental."
            },
            "parts": [
                {"part": "domanassa", "gloss": {"pt": "desprazer mental (du + manas + ya)", "en": "mental displeasure (du + manas + ya)", "es": "desagrado mental (du + manas + ya)"}},
                {"part": "saha", "gloss": {"pt": "junto com", "en": "together with", "es": "junto con"}},
                {"part": "gata", "gloss": {"pt": "ido, ocorrido", "en": "gone, proceeded", "es": "ido, ocurrido"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Qualificador Afetivo Exclusivo dos Dosamūlacittāni",
                "en": "Exclusive Affective Qualifier of the Dosamūlacittāni",
                "es": "Calificador Afectivo Exclusivo de los Dosamūlacittāni"
            },
            "category": {
                "pt": "Presente exclusivamente nos 2 Cittas Enraizados no Ódio (Dosamūla 1 e 2)",
                "en": "Present exclusively in the 2 Hatred-Rooted Cittas (Dosamūla 1 and 2)",
                "es": "Presente exclusivamente en los 2 Cittas Enraizados en el Odio (Dosamūla 1 y 2)"
            },
            "philosophy": {
                "pt": "Segundo Bhikkhu Bodhi (CMA I, §5, p. 38), domanassa acompanha apenas as consciências enraizadas no ódio (dosa), e tais consciências são necessariamente acompanhadas por essa sensação. Portanto, domanassa é sempre prejudicial (akusala), diferindo da dor corporal (dukkha-vedanā, que é karmicamente indeterminada, vipāka) e de somanassa e upekkhā (que podem ser salutares, prejudiciais ou indeterminadas). Embora domanassa e paṭigha (aversão) surjam sempre juntos, domanassa pertence ao agregado da sensação (vedanākkhandha), enquanto paṭigha pertence ao agregado das formações mentais (saṅkhārakkhandha).",
                "en": "According to Bhikkhu Bodhi (CMA I, §5, p. 38), domanassa accompanies only consciousness rooted in hatred (dosa), and such consciousness is necessarily accompanied by this feeling. Thus domanassa is always unwholesome (akusala), differing from bodily pain (dukkha-vedanā, which is kammically indeterminate, vipāka) and from somanassa and upekkhā. Though domanassa and paṭigha (aversion) always arise together, domanassa belongs to the feeling aggregate (vedanākkhandha), whereas paṭigha belongs to the formations aggregate (saṅkhārakkhandha).",
                "es": "Según Bhikkhu Bodhi (CMA I, §5, p. 38), domanassa acompaña únicamente a las conciencias enraizadas en el odio (dosa), por lo que domanassa es siempre perjudicial (akusala), a diferencia del dolor corporal (dukkha-vedanā, que es vipāka)."
            },
            "bodhiRef": "CMA I, §5 (Guide, pp. 37–38); III, §§2–4 (pp. 115–118)"
        },
        "seeAlso": ["domanassa", "paṭighasampayutta", "dosa", "dosamūlacitta", "vedanā"]
    },

    "diṭṭhigatasampayutta": {
        "meaning": {
            "pt": "Associado a visão errônea; conjugado com o fator mental de entendimento incorreto (diṭṭhi), qualificando 4 dos 8 cittas enraizados na cobiça (lobhamūlacitta 1, 2, 5 e 6).",
            "en": "Associated with wrong view; conjoined with the mental factor of wrong view (diṭṭhi), qualifying 4 of the 8 greed-rooted cittas (lobhamūlacitta 1, 2, 5, and 6).",
            "es": "Asociado con visión errónea; unido al factor mental de entendimiento incorrecto (diṭṭhi), calificando 4 de los 8 cittas enraizados en la codicia (lobhamūlacitta 1, 2, 5 y 6)."
        },
        "grammar": "adj. composto (diṭṭhi + gata + sampayutta)",
        "grammarLocalized": {
            "pt": "Adjetivo composto (Tatiyā-Tappurisa)",
            "en": "Compound adjective (Tatiyā-Tappurisa)",
            "es": "Adjetivo compuesto (Tatiyā-Tappurisa)"
        },
        "root": "√dis + ti + √gam + ta + saṃ + pa + √yuj + ta",
        "etymology": {
            "pt": "De diṭṭhigata (diṭṭhi [visão errônea, de √dis 'ver'] + gata [aqui usado pleonasticamente, sakatthe, sem alterar o sentido de diṭṭhi, segundo a Vibhāvinī-Ṭīkā]) + sampayutta (saṃ [junto] + pa + √yuj [unir, atrelar] + -ta = intimamente associado pelas 4 marcas de ekuppāda, etc.).",
            "en": "From diṭṭhigata (diṭṭhi [wrong view, from √dis 'to see'] + gata [here used pleonastically, sakatthe, with no added meaning beyond diṭṭhi itself, according to the Vibhāvinī-Ṭīkā]) + sampayutta (saṃ [together] + pa + √yuj [to yoke, join] + -ta = intimately associated).",
            "es": "De diṭṭhigata (diṭṭhi [visión errónea, de √dis 'ver'] + gata [sufijo pleonástico según la Vibhāvinī-Ṭīkā]) + sampayutta (saṃ + pa + √yuj + -ta = íntimamente asociado)."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Instrumental (Tatiyā-Tappurisa)",
                "en": "Instrumental Determinative Compound (Tatiyā-Tappurisa)",
                "es": "Compuesto Determinativo Instrumental (Tatiyā-Tappurisa)"
            },
            "viggaha": "diṭṭhova diṭṭhigataṃ; diṭṭhigatena sampayuttaṃ = diṭṭhigatasampayuttaṃ",
            "literal": {
                "pt": "Associado (sampayutta) com a condição de visão errônea (diṭṭhigata).",
                "en": "Associated (sampayutta) with wrong view (diṭṭhigata).",
                "es": "Asociado (sampayutta) con la visión errónea (diṭṭhigata)."
            },
            "parts": [
                {"part": "diṭṭhi", "gloss": {"pt": "visão errônea (micchādiṭṭhi)", "en": "wrong view (micchādiṭṭhi)", "es": "visión errónea (micchādiṭṭhi)"}},
                {"part": "gata", "gloss": {"pt": "estado / sufixo enfático (sakatthe)", "en": "state / pleonastic suffix (sakatthe)", "es": "estado / sufijo enfático (sakatthe)"}},
                {"part": "sampayutta", "gloss": {"pt": "associado com (saṃ + pa + √yuj)", "en": "associated with (saṃ + pa + √yuj)", "es": "asociado con (saṃ + pa + √yuj)"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Qualificador de Associação Mental (Sampayoga-bheda)",
                "en": "Qualifier of Mental Association (Sampayoga-bheda)",
                "es": "Calificador de Asociación Mental (Sampayoga-bheda)"
            },
            "category": {
                "pt": "Presente nos Cittas Lobhamūla 1, 2 (com alegria) e 5, 6 (com equanimidade) — 4 Cittas",
                "en": "Present in Lobhamūla Cittas 1, 2 (with joy) and 5, 6 (with equanimity) — 4 Cittas",
                "es": "Presente en los Cittas Lobhamūla 1, 2 (con alegría) y 5, 6 (con ecuanimidad) — 4 Cittas"
            },
            "philosophy": {
                "pt": "Segundo Bhikkhu Bodhi (CMA I, §4, p. 36), a visão errônea (diṭṭhi) acompanha a consciência enraizada na cobiça como uma convicção dogmática, crença, opinião ou racionalização (por exemplo, negar a lei do kamma ou sustentar a existência de um eu permanente), ou a própria visão especulativa pode ser o objeto direto de apego. Esses 4 cittas são totalmente erradicados no primeiro estágio do despertar (sotāpatti-magga). Nas consciências diṭṭhigatasampayutta, a presunção (māna) nunca pode surgir simultaneamente.",
                "en": "According to Bhikkhu Bodhi (CMA I, §4, p. 36), wrong view (diṭṭhi) accompanies greed-rooted consciousness as a dogmatic conviction, belief, opinion, or rationalization (e.g., denying kamma or affirming a permanent self), or the speculative view itself may be the object of attachment. All 4 diṭṭhigatasampayutta cittas are permanently eradicated by the path of stream-entry (sotāpatti-magga). Conceit (māna) can never arise in diṭṭhigatasampayutta cittas.",
                "es": "Según Bhikkhu Bodhi (CMA I, §4, p. 36), la visión errónea (diṭṭhi) acompaña a la conciencia enraizada en la codicia como una convicción dogmática, creencia o racionalización. Estos 4 cittas son erradicados definitivamente por el camino de entrada en la corriente (sotāpatti-magga)."
            },
            "bodhiRef": "CMA I, §4 (Guide, pp. 35–36); II, §13 (p. 97)"
        },
        "seeAlso": ["diṭṭhigatavippayutta", "diṭṭhi", "māna", "sampayutta", "lobhamūlacitta"]
    },

    "diṭṭhigatavippayutta": {
        "meaning": {
            "pt": "Dissociado de visão errônea; estado de consciência enraizado na cobiça em que o desejo opera sem qualquer justificação doutrinária ou visão incorreta associada (lobhamūlacitta 3, 4, 7 e 8).",
            "en": "Dissociated from wrong view; a greed-rooted consciousness in which desire operates without any accompanying doctrinal justification or wrong view (lobhamūlacitta 3, 4, 7, and 8).",
            "es": "Disociado de visión errónea; conciencia enraizada en la codicia en la que el deseo opera sin justificación doctrinal o visión errónea asociada (lobhamūlacitta 3, 4, 7 y 8)."
        },
        "grammar": "adj. composto (diṭṭhi + gata + vippayutta)",
        "grammarLocalized": {
            "pt": "Adjetivo composto (Tatiyā-Tappurisa)",
            "en": "Compound adjective (Tatiyā-Tappurisa)",
            "es": "Adjetivo compuesto (Tatiyā-Tappurisa)"
        },
        "root": "√dis + ti + √gam + ta + vi + pa + √yuj + ta",
        "etymology": {
            "pt": "De diṭṭhigata (visão errônea) + vippayutta (vi [separação, ausência] + pa + √yuj + -ta = dissociado de, desvinculado de).",
            "en": "From diṭṭhigata (wrong view) + vippayutta (vi [separation, absence] + pa + √yuj + -ta = dissociated from, unyoked from).",
            "es": "De diṭṭhigata (visión errónea) + vippayutta (vi [separación] + pa + √yuj + -ta = disociado de, desvinculado de)."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Instrumental (Tatiyā-Tappurisa)",
                "en": "Instrumental Determinative Compound (Tatiyā-Tappurisa)",
                "es": "Compuesto Determinativo Instrumental (Tatiyā-Tappurisa)"
            },
            "viggaha": "diṭṭhigatena vippayuttaṃ = diṭṭhigatavippayuttaṃ",
            "literal": {
                "pt": "Desvinculado ou dissociado (vippayutta) da visão errônea (diṭṭhigata).",
                "en": "Unyoked or dissociated (vippayutta) from wrong view (diṭṭhigata).",
                "es": "Desvinculado o disociado (vippayutta) de la visión errónea (diṭṭhigata)."
            },
            "parts": [
                {"part": "diṭṭhi", "gloss": {"pt": "visão errônea", "en": "wrong view", "es": "visión errónea"}},
                {"part": "gata", "gloss": {"pt": "sufixo enfático", "en": "pleonastic suffix", "es": "sufijo enfático"}},
                {"part": "vippayutta", "gloss": {"pt": "dissociado de (vi + pa + √yuj)", "en": "dissociated from (vi + pa + √yuj)", "es": "disociado de (vi + pa + √yuj)"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Qualificador de Dissociação Mental (Vippayoga-bheda)",
                "en": "Qualifier of Mental Dissociation (Vippayoga-bheda)",
                "es": "Calificador de Disociación Mental (Vippayoga-bheda)"
            },
            "category": {
                "pt": "Presente nos Cittas Lobhamūla 3, 4 (com alegria) e 7, 8 (com equanimidade) — 4 Cittas",
                "en": "Present in Lobhamūla Cittas 3, 4 (with joy) and 7, 8 (with equanimity) — 4 Cittas",
                "es": "Presente en los Cittas Lobhamūla 3, 4 (con alegría) y 7, 8 (con ecuanimidad) — 4 Cittas"
            },
            "philosophy": {
                "pt": "Nestes 4 cittas, o desejo ou apego surge sem visão errônea concomitante (e.g., desejar prazeres sensoriais sabendo perfeitamente que o apego é inábil, ou sentir afeição comum). É exclusivamente nestes 4 cittas diṭṭhigatavippayutta que o fator mental da presunção/orgulho (māna) pode surgir (como adjuncto não-fixo, aniyatayogī). Diferentemente dos 4 diṭṭhigatasampayutta (erradicados pelo sotāpanna), os 4 diṭṭhigatavippayutta continuam a surgir em sotāpannas e sakadāgāmīs, e só são totalmente erradicados pelo caminho do Arahant.",
                "en": "In these 4 cittas, greed or attachment operates without any accompanying wrong view. It is exclusively in these 4 diṭṭhigatavippayutta cittas that the mental factor of conceit (māna) can arise (as an unfixed adjunct, aniyatayogī). Unlike the 4 diṭṭhigatasampayutta cittas (eradicated at stream-entry), the 4 diṭṭhigatavippayutta cittas continue to arise in stream-enterers and once-returners, and are completely eradicated only by the path of Arahantship.",
                "es": "En estos 4 cittas, la codicia opera sin visión errónea concomitante. Es exclusivamente en estos 4 cittas diṭṭhigatavippayutta donde puede surgir el factor mental de la presunción/orgullo (māna)."
            },
            "bodhiRef": "CMA I, §4 (Guide, p. 36); II, §13 & §17 (pp. 97, 100)"
        },
        "seeAlso": ["diṭṭhigatasampayutta", "māna", "vippayutta", "lobhamūlacitta"]
    },

    "asaṅkhārika": {
        "meaning": {
            "pt": "Não induzido; espontâneo; consciência que surge naturalmente, com prontidão e acuidade, sem necessidade de instigação externa ou esforço deliberado interno.",
            "en": "Unprompted; spontaneous; consciousness arising naturally and keenly, without external instigation or deliberate internal inducement.",
            "es": "No instigado; espontáneo; conciencia que surge naturalmente y con agudeza, sin instigación externa ni inducción deliberada interna."
        },
        "grammar": "adj. (na > a + saṅkhāra + ika)",
        "grammarLocalized": {
            "pt": "Adjetivo derivado (Nañ-Tappurisa + sufixo -ika)",
            "en": "Derived adjective (Nañ-Tappurisa + suffix -ika)",
            "es": "Adjetivo derivado (Nañ-Tappurisa + sufijo -ika)"
        },
        "root": "na > a (sem) + saṃ + √kar (fazer/preparar) + ika",
        "etymology": {
            "pt": "Formado por a- (sem) + saṅkhāra (aqui usado no sentido técnico específico do Abhidhamma de 'indução, instigação, preparação ou aplicação de um expediente', payoga / upāya) + sufixo adjetival -ika.",
            "en": "Formed from a- (without) + saṅkhāra (used here in the specific Abhidhamma technical sense of 'prompting, instigation, inducement, or application of an expedient', payoga / upāya) + adjectival suffix -ika.",
            "es": "Formado por a- (sin) + saṅkhāra (usado aquí en el sentido técnico específico del Abhidhamma de 'instigación, inducción o aplicación de un medio', payoga / upāya) + sufijo -ika."
        },
        "samasa": {
            "type": {
                "pt": "Composto Negativo Derivado (Nañ-Tappurisa / Bahubbīhi)",
                "en": "Negative Derivative Compound (Nañ-Tappurisa / Bahubbīhi)",
                "es": "Compuesto Negativo Derivado (Nañ-Tappurisa / Bahubbīhi)"
            },
            "viggaha": "n'atthi saṅkhāro payogo etassā'ti = asaṅkhārikaṃ",
            "literal": {
                "pt": "Aquela consciência que ocorre sem instigação prévia ou esforço preparatório.",
                "en": "That consciousness which occurs without prior prompting or preparatory inducement.",
                "es": "Aquella conciencia que ocurre sin instigación previa ni esfuerzo preparatorio."
            },
            "parts": [
                {"part": "a (na)", "gloss": {"pt": "sem, não", "en": "without, un-", "es": "sin, no"}},
                {"part": "saṅkhāra", "gloss": {"pt": "indução, instigação (payoga/upāya)", "en": "prompting, inducement (payoga/upāya)", "es": "instigación, inducción (payoga/upāya)"}},
                {"part": "-ika", "gloss": {"pt": "dotado de / relativo a", "en": "pertaining to", "es": "relativo a"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Qualificador de Modo de Surgimento (Saṅkhāra-bheda)",
                "en": "Qualifier of Mode of Arising (Saṅkhāra-bheda)",
                "es": "Calificador de Modo de Surgimiento (Saṅkhāra-bheda)"
            },
            "category": {
                "pt": "Diferencia os pares ímpares nos 8 Lobhamūla, 2 Dosamūla e 24 Kāmāvacara Sobhana",
                "en": "Differentiates the odd-numbered cittas in the 8 Lobhamūla, 2 Dosamūla, and 24 Kāmāvacara Sobhana",
                "es": "Diferencia los cittas impares en los 8 Lobhamūla, 2 Dosamūla y 24 Kāmāvacara Sobhana"
            },
            "philosophy": {
                "pt": "Segundo Bhikkhu Bodhi (CMA I, §4, pp. 36–37), um citta asaṅkhārika surge espontaneamente, com vigor natural, sem precisar vencer resistência interna nem ser instigado por outros. Nos cittas akusala, somente nos cittas sasaṅkhārika (induzidos) podem surgir os fatores mentais de torpor e languidez (thīna-middha); um citta asaṅkhārika nunca contém thīna-middha (CMA II, §13 & §17).",
                "en": "According to Bhikkhu Bodhi (CMA I, §4, pp. 36–37), an asaṅkhārika citta arises spontaneously with natural keenness, without needing to overcome inner resistance or be prompted by others. Among akusala cittas, sloth and torpor (thīna-middha) can arise only in sasaṅkhārika (prompted) cittas; an asaṅkhārika citta never contains thīna-middha (CMA II, §13 & §17).",
                "es": "Según Bhikkhu Bodhi (CMA I, §4, pp. 36–37), un citta asaṅkhārika surge espontáneamente con agudeza natural, sin necesidad de superar resistencia interna ni ser instigado por otros. Nunca contiene pereza y torpor (thīna-middha)."
            },
            "bodhiRef": "CMA I, §4 & §6 (Guide, pp. 36–37, 39–40); II, §13 (p. 97)"
        },
        "seeAlso": ["sasaṅkhārika", "saṅkhāra", "thīna", "middha"]
    },

    "sasaṅkhārika": {
        "meaning": {
            "pt": "Induzido; instigado; consciência que surge mediante esforço deliberado para vencer hesitação ou resistência interna, ou por persuasão/comando de outrem.",
            "en": "Prompted; induced; consciousness arising through deliberate effort to overcome inner resistance or hesitation, or through persuasion/command by another.",
            "es": "Instigado; inducido; conciencia que surge mediante esfuerzo deliberado para vencer la resistencia interna, o por persuasión/orden de otro."
        },
        "grammar": "adj. (sa + saṅkhāra + ika)",
        "grammarLocalized": {
            "pt": "Adjetivo composto (Saha-pubbapada Bahubbīhi + sufixo -ika)",
            "en": "Compound adjective (Saha-pubbapada Bahubbīhi + suffix -ika)",
            "es": "Adjetivo compuesto (Saha-pubbapada Bahubbīhi + sufijo -ika)"
        },
        "root": "sa (com) + saṃ + √kar (preparar/induzir) + ika",
        "etymology": {
            "pt": "De sa- (com, acompanhado de) + saṅkhāra (indução, instigação, aplicação de um meio corporal, verbal ou mental) + -ika.",
            "en": "From sa- (with) + saṅkhāra (prompting, instigation, application of a bodily, verbal, or mental expedient) + -ika.",
            "es": "De sa- (con) + saṅkhāra (instigación, inducción por medio corporal, verbal o mental) + -ika."
        },
        "samasa": {
            "type": {
                "pt": "Composto Relativo (Saha-pubbapada Bahubbīhi)",
                "en": "Relative Compound (Saha-pubbapada Bahubbīhi)",
                "es": "Compuesto Relativo (Saha-pubbapada Bahubbīhi)"
            },
            "viggaha": "saṅkhārena (payogena) saha pavattatī'ti = sasaṅkhārikaṃ",
            "literal": {
                "pt": "Aquela consciência que procede acompanhada de instigação ou indução prévia.",
                "en": "That consciousness which proceeds accompanied by prior prompting or inducement.",
                "es": "Aquella conciencia que procede acompañada de instigación o inducción previa."
            },
            "parts": [
                {"part": "sa", "gloss": {"pt": "com, dotado de", "en": "with, accompanied by", "es": "con, dotado de"}},
                {"part": "saṅkhāra", "gloss": {"pt": "instigação, indução (payoga)", "en": "prompting, inducement (payoga)", "es": "instigación, inducción (payoga)"}},
                {"part": "-ika", "gloss": {"pt": "sufixo adjetival", "en": "adjectival suffix", "es": "sufijo adjetival"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Qualificador de Modo de Surgimento (Saṅkhāra-bheda)",
                "en": "Qualifier of Mode of Arising (Saṅkhāra-bheda)",
                "es": "Calificador de Modo de Surgimiento (Saṅkhāra-bheda)"
            },
            "category": {
                "pt": "Diferencia os pares nos 8 Lobhamūla (2, 4, 6, 8), 2 Dosamūla (10) e 24 Kāmāvacara Sobhana",
                "en": "Differentiates the even-numbered cittas in the 8 Lobhamūla (2, 4, 6, 8), 2 Dosamūla (10), and 24 Kāmāvacara Sobhana",
                "es": "Diferencia los cittas pares en los 8 Lobhamūla (2, 4, 6, 8), 2 Dosamūla (10) y 24 Kāmāvacara Sobhana"
            },
            "philosophy": {
                "pt": "A indução (saṅkhāra) pode vir de outra pessoa (por meio corporal ou verbal) ou de dentro de si mesmo (por reflexão mental deliberada contra a própria relutância). Nos 5 cittas akusala sasaṅkhārika (4 lobhamūla + 1 dosamūla), o par de fatores mentais thīna-middha (torpor e languidez) pode surgir como adjuncto ocasional (aniyatayogī). Na discussão do Cap. V (§30), Ācariya Mahā Dhammarakkhita sustenta que um kamma salutar sasaṅkhārika produz renascimento sasaṅkhārika, enquanto Ācariya Cūḷanāga (aceito pela Vibhāvinī-Ṭīkā) sustenta que tanto kusala asaṅkhārika quanto sasaṅkhārika podem produzir vipāka de ambos os modos.",
                "en": "The prompting (saṅkhāra) may be imposed by others (bodily or verbally) or originate within oneself (by deliberate mental reflection overcoming inner resistance). In the 5 akusala sasaṅkhārika cittas (4 lobhamūla + 1 dosamūla), the pair sloth and torpor (thīna-middha) may arise as unfixed adjuncts (aniyatayogī). In Ch. V (§30), the commentators discuss how asaṅkhārika and sasaṅkhārika wholesome kamma relate to their resultant rebirth consciousnesses.",
                "es": "La instigación (saṅkhāra) puede provenir de otra persona o de uno mismo al vencer la reticencia interna. En los 5 cittas akusala sasaṅkhārika, el par pereza y torpor (thīna-middha) puede surgir como adjunto ocasional (aniyatayogī)."
            },
            "bodhiRef": "CMA I, §4 (Guide, pp. 36–37); II, §13 & §26 (pp. 97, 108); V, §30 (p. 214)"
        },
        "seeAlso": ["asaṅkhārika", "thīna", "middha", "saṅkhāra"]
    },

    "paṭighasampayutta": {
        "meaning": {
            "pt": "Associado à aversão; conjugado com o fator mental do ódio/repulsa (dosa), qualificando os 2 cittas enraizados no ódio (dosamūlacittāni).",
            "en": "Associated with aversion; conjoined with the mental factor of hatred/repulsion (dosa), qualifying the 2 hatred-rooted cittas (dosamūlacittāni).",
            "es": "Asociado con aversión; unido al factor mental del odio/repulsión (dosa), calificando los 2 cittas enraizados en el odio (dosamūlacittāni)."
        },
        "grammar": "adj. composto (paṭigha + sampayutta)",
        "grammarLocalized": {
            "pt": "Adjetivo composto (Tatiyā-Tappurisa)",
            "en": "Compound adjective (Tatiyā-Tappurisa)",
            "es": "Adjetivo compuesto (Tatiyā-Tappurisa)"
        },
        "root": "paṭi (contra) + √ghan / √han (golpear) + a + saṃ + pa + √yuj + ta",
        "etymology": {
            "pt": "De paṭigha (paṭi- [contra] + √han / √ghan [bater, chocar-se, golpear] = 'choque contra', resistência hostil, aversão, sinônimo de dosa) + sampayutta (associado a).",
            "en": "From paṭigha (paṭi- [against] + √han / √ghan [to strike, hit] = 'striking against', hostile resistance, aversion, synonymous with dosa) + sampayutta (associated with).",
            "es": "De paṭigha (paṭi- [contra] + √han / √ghan [golpear, chocar] = 'chocar contra', resistencia hostil, aversión, sinónimo de dosa) + sampayutta (asociado con)."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Instrumental (Tatiyā-Tappurisa)",
                "en": "Instrumental Determinative Compound (Tatiyā-Tappurisa)",
                "es": "Compuesto Determinativo Instrumental (Tatiyā-Tappurisa)"
            },
            "viggaha": "paṭighena sampayuttaṃ = paṭighasampayuttaṃ",
            "literal": {
                "pt": "Associado (sampayutta) com o choque hostil da aversão (paṭigha).",
                "en": "Associated (sampayutta) with the hostile striking of aversion (paṭigha).",
                "es": "Asociado (sampayutta) con el choque hostil de la aversión (paṭigha)."
            },
            "parts": [
                {"part": "paṭigha", "gloss": {"pt": "aversão, repulsa (paṭi + √han)", "en": "aversion, striking against (paṭi + √han)", "es": "aversión, choque contra (paṭi + √han)"}},
                {"part": "sampayutta", "gloss": {"pt": "associado com", "en": "associated with", "es": "asociado con"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Qualificador dos 2 Cittas Enraizados no Ódio (Dosamūlacittāni)",
                "en": "Qualifier of the 2 Hatred-Rooted Cittas (Dosamūlacittāni)",
                "es": "Calificador de los 2 Cittas Enraizados en el Odio (Dosamūlacittāni)"
            },
            "category": {
                "pt": "Presente nos Cittas Akusala 9 (asaṅkhārika) e 10 (sasaṅkhārika)",
                "en": "Present in Akusala Cittas 9 (asaṅkhārika) and 10 (sasaṅkhārika)",
                "es": "Presente en los Cittas Akusala 9 (asaṅkhārika) y 10 (sasaṅkhārika)"
            },
            "philosophy": {
                "pt": "No Abhidhamma, paṭigha (aversão) é estritamente o cetasika dosa (ódio), abrangendo desde a fúria violenta até a mais sutil irritação, medo ou impaciência. Enquanto domanassa é o aspecto afetivo (a dor mental sentida, pertencente a vedanākkhandha), paṭigha é a atitude conativa de rejeição ou hostilidade contra o objeto (pertencente a saṅkhārakkhandha). Ambos são erradicados definitivamente pelo terceiro caminho supramundano (anāgāmimagga).",
                "en": "In the Abhidhamma, paṭigha (aversion) is strictly the cetasika dosa (hatred), ranging from violent rage to subtle irritation, fear, or impatience. While domanassa is the affective aspect (the unpleasant mental feeling, belonging to vedanākkhandha), paṭigha is the conative attitude of resistance or ill will towards the object (belonging to saṅkhārakkhandha). Both are permanently eradicated by the path of non-returning (anāgāmimagga).",
                "es": "En el Abhidhamma, paṭigha (aversión) es estrictamente el cetasika dosa (odio), abarcando desde la ira violenta hasta la irritación sutil o el miedo. Mientras que domanassa pertenece al agregado de la sensación (vedanākkhandha), paṭigha pertenece al agregado de las formaciones (saṅkhārakkhandha)."
            },
            "bodhiRef": "CMA I, §5 (Guide, pp. 37–38); II, §13 (p. 97)"
        },
        "seeAlso": ["domanassasahagata", "dosa", "issā", "macchariya", "kukkucca"]
    },

    "ñāṇasampayutta": {
        "meaning": {
            "pt": "Associado ao conhecimento; consciência bela (sobhana) que surge acompanhada pela faculdade da sabedoria (paññindriya / amoha), tornando-se triplamente enraizada (tihetuka).",
            "en": "Associated with knowledge; beautiful (sobhana) consciousness arising accompanied by the wisdom faculty (paññindriya / amoha), thereby becoming triple-rooted (tihetuka).",
            "es": "Asociado con conocimiento; conciencia hermosa (sobhana) que surge acompañada por la facultad de la sabiduría (paññindriya / amoha), volviéndose triplemente enraizada (tihetuka)."
        },
        "grammar": "adj. composto (ñāṇa + sampayutta)",
        "grammarLocalized": {
            "pt": "Adjetivo composto (Tatiyā-Tappurisa)",
            "en": "Compound adjective (Tatiyā-Tappurisa)",
            "es": "Adjetivo compuesto (Tatiyā-Tappurisa)"
        },
        "root": "√ñā (conhecer) + aṇa + saṃ + pa + √yuj + ta",
        "etymology": {
            "pt": "De ñāṇa (conhecimento, sabedoria, sinônimo de paññā e amoha, da raiz √ñā 'conhecer') + sampayutta (associado a).",
            "en": "From ñāṇa (knowledge, wisdom, synonymous with paññā and amoha, from root √ñā 'to know') + sampayutta (associated with).",
            "es": "De ñāṇa (conocimiento, sabiduría, sinónimo de paññā y amoha, de la raíz √ñā 'conocer') + sampayutta (asociado con)."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Instrumental (Tatiyā-Tappurisa)",
                "en": "Instrumental Determinative Compound (Tatiyā-Tappurisa)",
                "es": "Compuesto Determinativo Instrumental (Tatiyā-Tappurisa)"
            },
            "viggaha": "ñāṇena sampayuttaṃ = ñāṇasampayuttaṃ",
            "literal": {
                "pt": "Associado (sampayutta) ao conhecimento ou sabedoria (ñāṇa).",
                "en": "Associated (sampayutta) with knowledge or wisdom (ñāṇa).",
                "es": "Asociado (sampayutta) con el conocimiento o sabiduría (ñāṇa)."
            },
            "parts": [
                {"part": "ñāṇa", "gloss": {"pt": "conhecimento, sabedoria (√ñā + aṇa)", "en": "knowledge, wisdom (√ñā + aṇa)", "es": "conocimiento, sabiduría (√ñā + aṇa)"}},
                {"part": "sampayutta", "gloss": {"pt": "associado com", "en": "associated with", "es": "asociado con"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Qualificador de Presença de Sabedoria (Ñāṇa-bheda / Tihetuka)",
                "en": "Qualifier of Presence of Wisdom (Ñāṇa-bheda / Tihetuka)",
                "es": "Calificador de Presencia de Sabiduría (Ñāṇa-bheda / Tihetuka)"
            },
            "category": {
                "pt": "Qualifica 12 dos 24 Cittas Kāmāvacara Sobhana (4 Mahākusala, 4 Mahāvipāka, 4 Mahākiriya); todos os 27 Mahaggata e 8/40 Lokuttara são invariavelmente ñāṇasampayutta",
                "en": "Qualifies 12 of the 24 Kāmāvacara Sobhana Cittas (4 Mahākusala, 4 Mahāvipāka, 4 Mahākiriya); all 27 Mahaggata and 8/40 Lokuttara are invariably ñāṇasampayutta",
                "es": "Califica 12 de los 24 Cittas Kāmāvacara Sobhana (4 Mahākusala, 4 Mahāvipāka, 4 Mahākiriya); todos los 27 Mahaggata y 8/40 Lokuttara son invariablemente ñāṇasampayutta"
            },
            "philosophy": {
                "pt": "Como explica Bhikkhu Bodhi (CMA I, §§13–17, pp. 47–54), nos 24 cittas belos da esfera sensorial (kāmāvacarasobhana), 12 são ñāṇasampayutta (possuem as 3 raízes belas: alobha, adosa e amoha/paññā, sendo portanto tihetuka) e 12 são ñāṇavippayutta (possuem apenas alobha e adosa, sendo dvihetuka). Somente uma pessoa cujo renascimento ocorreu por um mahāvipākacitta ñāṇasampayutta (tihetuka-puggala) pode alcançar os jhānas ou os caminhos e frutos supramundanos naquela existência (CMA IV, §24).",
                "en": "As Bhikkhu Bodhi explains (CMA I, §§13–17, pp. 47–54), among the 24 sense-sphere beautiful cittas (kāmāvacarasobhana), 12 are ñāṇasampayutta (possessing all 3 beautiful roots: alobha, adosa, and amoha/paññā, hence triple-rooted, tihetuka) and 12 are ñāṇavippayutta (possessing only alobha and adosa, hence double-rooted, dvihetuka). Only a person whose rebirth-linking occurred via a ñāṇasampayutta mahāvipākacitta (a tihetuka individual) can attain jhānas or supramundane paths and fruits in that life (CMA IV, §24).",
                "es": "Como explica Bhikkhu Bodhi (CMA I, §§13–17, pp. 47–54), de los 24 cittas hermosos de la esfera sensorial, 12 son ñāṇasampayutta (poseen las 3 raíces hermosas: alobha, adosa y amoha/paññā, siendo tihetuka) y 12 son ñāṇavippayutta (dvihetuka). Solo quien renace con un citta tihetuka puede alcanzar jhānas o caminos supramundanos en esa vida."
            },
            "bodhiRef": "CMA I, §§13–17 (Guide, pp. 47–54); IV, §24 (p. 176)"
        },
        "seeAlso": ["ñāṇavippayutta", "paññā", "amoha", "tihetuka", "mahākusala"]
    },

    "ñāṇavippayutta": {
        "meaning": {
            "pt": "Dissociado do conhecimento; consciência bela (sobhana) da esfera sensorial que surge sem a faculdade da sabedoria (paññā), possuindo apenas duas raízes salutares (alobha e adosa — dvihetuka).",
            "en": "Dissociated from knowledge; sense-sphere beautiful (sobhana) consciousness arising without the wisdom faculty (paññā), possessing only two beautiful roots (alobha and adosa — dvihetuka).",
            "es": "Disociado de conocimiento; conciencia hermosa (sobhana) de la esfera sensorial que surge sin la facultad de la sabiduría (paññā), poseyendo solo dos raíces hermosas (alobha y adosa — dvihetuka)."
        },
        "grammar": "adj. composto (ñāṇa + vippayutta)",
        "grammarLocalized": {
            "pt": "Adjetivo composto (Tatiyā-Tappurisa)",
            "en": "Compound adjective (Tatiyā-Tappurisa)",
            "es": "Adjetivo compuesto (Tatiyā-Tappurisa)"
        },
        "root": "√ñā + aṇa + vi + pa + √yuj + ta",
        "etymology": {
            "pt": "De ñāṇa (conhecimento, sabedoria) + vippayutta (dissociado de). Nota importante: 'dissociado do conhecimento' NÃO significa associado à delusão (moha), pois moha jamais surge em cittas belos; significa apenas ausência da compreensão penetrante de paññā naquele ato salutar.",
            "en": "From ñāṇa (knowledge, wisdom) + vippayutta (dissociated from). Important note: 'dissociated from knowledge' does NOT mean associated with delusion (moha), as moha never arises in beautiful cittas; it simply means the absence of penetrating wisdom (paññā) in that wholesome act.",
            "es": "De ñāṇa (conocimiento) + vippayutta (disociado de). Nota importante: 'disociado del conocimiento' NO significa asociado con la ilusión (moha), pues moha jamás surge en cittas hermosos; significa simplemente la ausencia de sabiduría penetrante (paññā) en ese acto."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Instrumental (Tatiyā-Tappurisa)",
                "en": "Instrumental Determinative Compound (Tatiyā-Tappurisa)",
                "es": "Compuesto Determinativo Instrumental (Tatiyā-Tappurisa)"
            },
            "viggaha": "ñāṇena vippayuttaṃ = ñāṇavippayuttaṃ",
            "literal": {
                "pt": "Desvinculado ou dissociado (vippayutta) do conhecimento (ñāṇa).",
                "en": "Unyoked or dissociated (vippayutta) from knowledge (ñāṇa).",
                "es": "Desvinculado o disociado (vippayutta) del conocimiento (ñāṇa)."
            },
            "parts": [
                {"part": "ñāṇa", "gloss": {"pt": "conhecimento, sabedoria", "en": "knowledge, wisdom", "es": "conocimiento, sabiduría"}},
                {"part": "vippayutta", "gloss": {"pt": "dissociado de", "en": "dissociated from", "es": "disociado de"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Qualificador de Ausência de Sabedoria em Citta Sobhana (Dvihetuka)",
                "en": "Qualifier of Absence of Wisdom in Sobhana Citta (Dvihetuka)",
                "es": "Calificador de Ausencia de Sabiduría en Citta Sobhana (Dvihetuka)"
            },
            "category": {
                "pt": "Qualifica 12 dos 24 Cittas Kāmāvacara Sobhana (4 Mahākusala, 4 Mahāvipāka, 4 Mahākiriya)",
                "en": "Qualifies 12 of the 24 Kāmāvacara Sobhana Cittas (4 Mahākusala, 4 Mahāvipāka, 4 Mahākiriya)",
                "es": "Califica 12 de los 24 Cittas Kāmāvacara Sobhana (4 Mahākusala, 4 Mahāvipāka, 4 Mahākiriya)"
            },
            "philosophy": {
                "pt": "Ilustrado por Bhikkhu Bodhi (CMA I, §17, p. 53) como uma boa ação feita sem compreensão da lei de kamma e fruto (ex.: uma criança que reverencia o Buddha imitando os pais, ou alguém que faz generosidade por hábito bondoso sem reflexão sapiencial). Por ter alobha e adosa, é salutar e isento de moha, mas carece da terceira raiz (amoha/paññā).",
                "en": "Illustrated by Bhikkhu Bodhi (CMA I, §17, p. 53) by a good deed performed without understanding the law of kamma and its fruit (e.g., a child bowing to the Buddha out of imitation, or an act of generosity done out of kindly habit without wisdom). Having alobha and adosa, it is wholesome and free of moha, yet lacks the third root (amoha/paññā).",
                "es": "Ilustrado por Bhikkhu Bodhi (CMA I, §17, p. 53) como una buena acción realizada sin comprensión de la ley del kamma y su fruto. Al poseer alobha y adosa, es saludable y libre de moha, pero carece de la tercera raíz (amoha/paññā)."
            },
            "bodhiRef": "CMA I, §§13–17 (Guide, pp. 47–54)"
        },
        "seeAlso": ["ñāṇasampayutta", "dvihetuka", "alobha", "adosa"]
    },

    "ahetuka": {
        "meaning": {
            "pt": "Sem raiz; consciência ou fenômeno desprovido de todas as seis raízes éticas (lobha, dosa, moha, alobha, adosa, amoha). Compreende os 18 cittas ahetuka e toda a matéria (rūpa).",
            "en": "Rootless; consciousness or phenomenon devoid of all six ethical roots (lobha, dosa, moha, alobha, adosa, amoha). Comprises the 18 ahetuka cittas and all matter (rūpa).",
            "es": "Sin raíz; conciencia o fenómeno desprovisto de las seis raíces éticas (lobha, dosa, moha, alobha, adosa, amoha). Comprende los 18 cittas ahetuka y toda la materia (rūpa)."
        },
        "grammar": "adj. (na > a + hetu + ka)",
        "grammarLocalized": {
            "pt": "Adjetivo composto (Nañ-pubbapada Bahubbīhi + sufixo -ka)",
            "en": "Compound adjective (Nañ-pubbapada Bahubbīhi + suffix -ka)",
            "es": "Adjetivo compuesto (Nañ-pubbapada Bahubbīhi + sufijo -ka)"
        },
        "root": "na > a (sem) + hetu (raiz) + ka",
        "etymology": {
            "pt": "De a- (sem) + hetu (raiz ética, mūla; atenção: no Suttanta hetu significa causa em geral, mas no Abhidhamma técnico hetu significa exclusivamente as 6 raízes éticas) + sufixo -ka.",
            "en": "From a- (without) + hetu (ethical root, mūla; note: in the Suttas hetu means cause in general, but in technical Abhidhamma hetu signifies exclusively the 6 ethical roots) + suffix -ka.",
            "es": "De a- (sin) + hetu (raíz ética, mūla; en el Abhidhamma técnico hetu significa exclusivamente las 6 raíces éticas) + sufijo -ka."
        },
        "samasa": {
            "type": {
                "pt": "Composto Relativo Negativo (Nañ-Bahubbīhi)",
                "en": "Negative Relative Compound (Nañ-Bahubbīhi)",
                "es": "Compuesto Relativo Negativo (Nañ-Bahubbīhi)"
            },
            "viggaha": "n'atthi hetū etesanti = ahetukāni (cittāni)",
            "literal": {
                "pt": "Aquelas consciências nas quais não há nenhuma das seis raízes (hetu).",
                "en": "Those consciousnesses in which none of the six roots (hetu) are present.",
                "es": "Aquellas conciencias en las que no hay ninguna de las seis raíces (hetu)."
            },
            "parts": [
                {"part": "a (na)", "gloss": {"pt": "sem, desprovido de", "en": "without, devoid of", "es": "sin, desprovisto de"}},
                {"part": "hetu", "gloss": {"pt": "raiz ética (uma das 6)", "en": "ethical root (one of the 6)", "es": "raíz ética (una de las 6)"}},
                {"part": "-ka", "gloss": {"pt": "sufixo de bahubbīhi", "en": "bahubbīhi suffix", "es": "sufijo de bahubbīhi"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Classe de Consciência Sem Raiz (Ahetukacittāni — 18 tipos)",
                "en": "Class of Rootless Consciousness (Ahetukacittāni — 18 types)",
                "es": "Clase de Conciencia Sin Raíz (Ahetukacittāni — 18 tipos)"
            },
            "category": {
                "pt": "18 Cittas Ahetuka: 7 Akusalavipāka + 8 Kusalavipāka Ahetuka + 3 Ahetukakiriya",
                "en": "18 Ahetuka Cittas: 7 Akusalavipāka + 8 Kusalavipāka Ahetuka + 3 Ahetukakiriya",
                "es": "18 Cittas Ahetuka: 7 Akusalavipāka + 8 Kusalavipāka Ahetuka + 3 Ahetukakiriya"
            },
            "philosophy": {
                "pt": "Todos os 18 cittas ahetuka são eticamente indeterminados (abyākata), pois são ou resultantes (15 vipāka) ou funcionais (3 kiriya); jamais existem cittas ahetuka salutares (kusala) ou prejudiciais (akusala). Eles executam funções cognitivas elementares no processo mental (cittavīthi): advertir (āvajjana), ver/ouvir/cheirar/saborear/tocar (dvipañcaviññāṇa), receber (sampaṭicchana), investigar (santīraṇa), determinar (voṭṭhabbana), reter (tadārammaṇa) e produzir o sorriso sutil dos Arahants (hasituppāda).",
                "en": "All 18 ahetuka cittas are ethically indeterminate (abyākata), being either resultants (15 vipāka) or functionals (3 kiriya); there are never any wholesome (kusala) or unwholesome (akusala) rootless cittas. They perform elementary cognitive functions in the cognitive process (cittavīthi): adverting (āvajjana), bare sense-cognition (dvipañcaviññāṇa), receiving (sampaṭicchana), investigating (santīraṇa), determining (voṭṭhabbana), registration (tadārammaṇa), and producing the gentle smile of Arahants (hasituppāda).",
                "es": "Todos los 18 cittas ahetuka son éticamente indeterminados (abyākata): 15 resultantes (vipāka) y 3 funcionales (kiriya). Ejecutan funciones cognitivas elementales en el proceso mental (cittavīthi) como advertencia, percepción sensorial desnuda, recepción, investigación, determinación, registro y la sonrisa del Arahant (hasituppāda)."
            },
            "bodhiRef": "CMA I, §§8–11 (Guide, pp. 41–47); III, §§5–7 (pp. 118–120)"
        },
        "seeAlso": ["hetu", "sahetuka", "dvipañcaviññāṇa", "sampaṭicchana", "santīraṇa", "hasituppāda"]
    },

    "hasituppāda": {
        "meaning": {
            "pt": "Consciência produtora do sorriso; o 18º citta sem raiz (ahetuka-kiriya, acompanhado de alegria), exclusivo de Buddhas e Arahants quando sorriem diante de um objeto da esfera sensorial.",
            "en": "Smile-producing consciousness; the 18th rootless citta (ahetuka-kiriya, accompanied by joy), exclusive to Buddhas and Arahants when smiling at a sense-sphere object.",
            "es": "Conciencia productora de la sonrisa; el 18º citta sin raíz (ahetuka-kiriya, acompañado de alegría), exclusivo de Buddhas y Arahants al sonreír ante un objeto de la esfera sensorial."
        },
        "grammar": "masc. (hasita + uppāda)",
        "grammarLocalized": {
            "pt": "Substantivo masculino composto (Chaṭṭhī-Tappurisa)",
            "en": "Compound masculine noun (Chaṭṭhī-Tappurisa)",
            "es": "Sustantivo masculino compuesto (Chaṭṭhī-Tappurisa)"
        },
        "root": "√has (sorrir) + ita + ud + √pad (surgir) + *a",
        "etymology": {
            "pt": "De hasita (sorriso sutil dos Nobres, de √has 'rir, sorrir') + uppāda (surgimento, produção, de ud + √pad).",
            "en": "From hasita (gentle smile of the Noble Ones, from √has 'to smile, laugh') + uppāda (arising, production, from ud + √pad).",
            "es": "De hasita (sonrisa sutil de los Nobles, de √has 'sonreír') + uppāda (surgimiento, producción, de ud + √pad)."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Genitivo (Chaṭṭhī-Tappurisa)",
                "en": "Genitive Determinative Compound (Chaṭṭhī-Tappurisa)",
                "es": "Compuesto Determinativo Genitivo (Chaṭṭhī-Tappurisa)"
            },
            "viggaha": "hasitassa uppādo = hasituppādo (tathābhūtaṃ cittaṃ = hasituppādacittaṃ)",
            "literal": {
                "pt": "A consciência que produz o surgimento (uppāda) do sorriso sutil (hasita).",
                "en": "The consciousness that brings about the arising (uppāda) of a gentle smile (hasita).",
                "es": "La conciencia que produce el surgimiento (uppāda) de la sonrisa sutil (hasita)."
            },
            "parts": [
                {"part": "hasita", "gloss": {"pt": "sorriso sutil (√has + ita)", "en": "gentle smile (√has + ita)", "es": "sonrisa sutil (√has + ita)"}},
                {"part": "uppāda", "gloss": {"pt": "surgimento, produção (ud + √pad)", "en": "arising, production (ud + √pad)", "es": "surgimiento, producción (ud + √pad)"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Citta Funcional Sem Raiz Exclusivo de Arahants (Ahetuka Kiriyacitta #30)",
                "en": "Rootless Functional Citta Exclusive to Arahants (Ahetuka Kiriyacitta #30)",
                "es": "Citta Funcional Sin Raíz Exclusivo de Arahants (Ahetuka Kiriyacitta #30)"
            },
            "category": {
                "pt": "1 dos 3 Cittas Ahetukakiriya; único citta ahetuka que desempenha a função de Javana (Impulsão)",
                "en": "1 of the 3 Ahetukakiriya Cittas; the sole ahetuka citta performing the function of Javana",
                "es": "1 de los 3 Cittas Ahetukakiriya; el único citta ahetuka que desempeña la función de Javana"
            },
            "philosophy": {
                "pt": "Segundo Bhikkhu Bodhi (CMA I, §10, pp. 45–46), os Comentários distinguem seis tipos de riso: (1) sita (sorriso quase imperceptível no rosto e olhos, próprio dos Buddhas); (2) hasita (sorriso que mostra levemente as pontas dos dentes, próprio dos Arahants); (3) vihasita (riso com som suave); (4) upahasita (riso que sacode a cabeça e os ombros); (5) apahasita (gargalhada até lacrimejar); e (6) atihasita (gargalhada descontrolada que sacode todo o corpo). Os Buddhas e Arahants sorriem apenas com sita e hasita. Hasituppādacitta contém 12 cetasikas (7 universais + 5 ocasionais, excluindo chanda) e é o único citta sem raiz (ahetuka) que atua como javana.",
                "en": "According to Bhikkhu Bodhi (CMA I, §10, pp. 45–46), the Commentaries distinguish six kinds of laughter: (1) sita (faint smile on the countenance, of Buddhas); (2) hasita (smile slightly revealing the tips of the teeth, of Arahants); (3) vihasita (gentle audible laughter); (4) upahasita (laughter shaking head and shoulders); (5) apahasita (laughing until tears flow); and (6) atihasita (uncontrolled roaring laughter). Buddhas and Arahants smile only with sita and hasita. Hasituppādacitta contains 12 cetasikas (7 universals + 5 occasionals, excluding chanda) and is the only rootless (ahetuka) citta that performs the function of javana.",
                "es": "Según Bhikkhu Bodhi (CMA I, §10, pp. 45–46), los Comentarios distinguen seis tipos de risa (sita, hasita, vihasita, upahasita, apahasita y atihasita). Los Buddhas y Arahants sonríen solo con sita y hasita. Hasituppādacitta contiene 12 cetasikas y es el único citta sin raíz (ahetuka) que ejerce la función de javana."
            },
            "bodhiRef": "CMA I, §10 (Guide, pp. 45–46); II, §28 (p. 109)"
        },
        "seeAlso": ["ahetuka", "kiriya", "javana", "arahant"]
    }
}

PART1_ENTRIES.update({
    "vicikicchāsampayutta": {
        "meaning": {
            "pt": "Associado à dúvida; conjugado com o fator mental da perplexidade cética (vicikicchā), qualificando o 1º citta enraizado na pura delusão (mohamūlacitta 1).",
            "en": "Associated with doubt; conjoined with the mental factor of skeptical perplexity (vicikicchā), qualifying the 1st citta rooted in sheer delusion (mohamūlacitta 1).",
            "es": "Asociado con la duda; unido al factor mental de la perplejidad escéptica (vicikicchā), calificando el 1º citta enraizado en la pura ilusión (mohamūlacitta 1)."
        },
        "grammar": "adj. composto (vicikicchā + sampayutta)",
        "grammarLocalized": {
            "pt": "Adjetivo composto (Tatiyā-Tappurisa)",
            "en": "Compound adjective (Tatiyā-Tappurisa)",
            "es": "Adjetivo compuesto (Tatiyā-Tappurisa)"
        },
        "root": "vi + √cit / √kicch + ā + saṃ + pa + √yuj + ta",
        "etymology": {
            "pt": "De vicikicchā (duas etimologias comentariais em CMA I, nota 3: [i] vici [investigando/pensando] + √kicch [ser atormentado/vexado] = tormento pela perplexidade do pensamento; [ii] vi [desprovido de] + cikicchā [remédio do conhecimento]) + sampayutta (associado a).",
            "en": "From vicikicchā (two commentarial etymologies in CMA I, n. 3: [i] vici [inquiring] + √kicch [to be vexed] = vexation due to perplexed thinking; [ii] vi [devoid of] + cikicchā [the remedy of knowledge]) + sampayutta (associated with).",
            "es": "De vicikicchā (dos etimologías comentariales en CMA I, n. 3: [i] vici [indagando] + √kicch [atormentarse] = aflicción por pensamiento perplejo; [ii] vi [desprovisto de] + cikicchā [el remedio del conocimiento]) + sampayutta (asociado con)."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Instrumental (Tatiyā-Tappurisa)",
                "en": "Instrumental Determinative Compound (Tatiyā-Tappurisa)",
                "es": "Compuesto Determinativo Instrumental (Tatiyā-Tappurisa)"
            },
            "viggaha": "vicikicchāya sampayuttaṃ = vicikicchāsampayuttaṃ",
            "literal": {
                "pt": "Associado (sampayutta) com a dúvida espiritual (vicikicchā).",
                "en": "Associated (sampayutta) with spiritual doubt (vicikicchā).",
                "es": "Asociado (sampayutta) con la duda espiritual (vicikicchā)."
            },
            "parts": [
                {"part": "vicikicchā", "gloss": {"pt": "dúvida, perplexidade cética", "en": "doubt, skeptical perplexity", "es": "duda, perplejidad escéptica"}},
                {"part": "sampayutta", "gloss": {"pt": "associado com", "en": "associated with", "es": "asociado con"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "1º Citta Enraizado na Delusão (Mohamūlacitta #11)",
                "en": "1st Delusion-Rooted Citta (Mohamūlacitta #11)",
                "es": "1º Citta Enraizado en la Ilusión (Mohamūlacitta #11)"
            },
            "category": {
                "pt": "Contém 15 Cetasikas (7 Universais + 3 Ocasionais [vitakka, vicāra, viriya] + 4 Akusala Universais + Vicikicchā — sem adhimokkha!)",
                "en": "Contains 15 Cetasikas (7 Universals + 3 Occasionals [vitakka, vicāra, viriya] + 4 Akusala Universals + Vicikicchā — without adhimokkha!)",
                "es": "Contiene 15 Cetasikas (7 Universales + 3 Ocasionales [vitakka, vicāra, viriya] + 4 Akusala Universales + Vicikicchā — ¡sin adhimokkha!)"
            },
            "philosophy": {
                "pt": "Segundo Bhikkhu Bodhi (CMA I, §6; II, §26), neste citta a indecisão de vicikicchā é tão dominante que exclui o fator mental ocasional da decisão (adhimokkha). Además, a unidirecionalidade (ekaggatā) presente nele é extremamente fraca, servindo apenas para manter a estase momentânea da mente, sem nunca alcançar a força de fator de caminho ou faculdade. É erradicado definitivamente pelo caminho de entrada na correnteza (sotāpattimagga).",
                "en": "According to Bhikkhu Bodhi (CMA I, §6; II, §26), in this citta the indecisiveness of vicikicchā is so dominant that it excludes the occasional mental factor of decision (adhimokkha). Moreover, one-pointedness (ekaggatā) here is extremely weak, merely maintaining momentary mental stasis. It is permanently eradicated by the path of stream-entry (sotāpattimagga).",
                "es": "Según Bhikkhu Bodhi (CMA I, §6; II, §26), en este citta la indecisión de vicikicchā excluye el factor mental de la decisión (adhimokkha). Es erradicado definitivamente por el camino de entrada en la corriente (sotāpattimagga)."
            },
            "bodhiRef": "CMA I, §6 (Guide, pp. 38–40); II, §13 & §26 (pp. 98, 108)"
        },
        "seeAlso": ["vicikicchā", "uddhaccasampayutta", "moha", "adhimokkha", "momūha"]
    },

    "uddhaccasampayutta": {
        "meaning": {
            "pt": "Associado à inquietação; conjugado de modo predominante com a agitação mental (uddhacca), qualificando o 2º citta enraizado na pura delusão (mohamūlacitta 2).",
            "en": "Associated with restlessness; predominantly conjoined with mental agitation (uddhacca), qualifying the 2nd citta rooted in sheer delusion (mohamūlacitta 2).",
            "es": "Asociado con la inquietud; unido de modo predominante a la agitación mental (uddhacca), calificando el 2º citta enraizado en la pura ilusión (mohamūlacitta 2)."
        },
        "grammar": "adj. composto (uddhacca + sampayutta)",
        "grammarLocalized": {
            "pt": "Adjetivo composto (Tatiyā-Tappurisa)",
            "en": "Compound adjective (Tatiyā-Tappurisa)",
            "es": "Adjetivo compuesto (Tatiyā-Tappurisa)"
        },
        "root": "ud + √dhu + ta + ya + saṃ + pa + √yuj + ta",
        "etymology": {
            "pt": "De uddhacca (ud [para cima] + √dhu [sacudir, agitar] = estado de ser sacudido para cima, agitação, distração) + sampayutta (associado a).",
            "en": "From uddhacca (ud [up] + √dhu [to shake, agitate] = state of being shaken up, agitation, distraction) + sampayutta (associated with).",
            "es": "De uddhacca (ud [hacia arriba] + √dhu [sacudir, agitar] = agitación, distracción) + sampayutta (asociado con)."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Instrumental (Tatiyā-Tappurisa)",
                "en": "Instrumental Determinative Compound (Tatiyā-Tappurisa)",
                "es": "Compuesto Determinativo Instrumental (Tatiyā-Tappurisa)"
            },
            "viggaha": "uddhaccena sampayuttaṃ = uddhaccasampayuttaṃ",
            "literal": {
                "pt": "Associado (sampayutta) de modo proeminente à inquietação mental (uddhacca).",
                "en": "Predominantly associated (sampayutta) with mental restlessness (uddhacca).",
                "es": "Asociado (sampayutta) de modo prominente con la inquietud mental (uddhacca)."
            },
            "parts": [
                {"part": "uddhacca", "gloss": {"pt": "inquietação, agitação (ud + √dhu)", "en": "restlessness, agitation (ud + √dhu)", "es": "inquietud, agitación (ud + √dhu)"}},
                {"part": "sampayutta", "gloss": {"pt": "associado com", "en": "associated with", "es": "asociado con"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "2º Citta Enraizado na Delusão (Mohamūlacitta #12)",
                "en": "2nd Delusion-Rooted Citta (Mohamūlacitta #12)",
                "es": "2º Citta Enraizado en la Ilusión (Mohamūlacitta #12)"
            },
            "category": {
                "pt": "Contém 15 Cetasikas (7 Universais + 4 Ocasionais [vitakka, vicāra, adhimokkha, viriya] + 4 Akusala Universais [moha, ahirika, anottappa, uddhacca])",
                "en": "Contains 15 Cetasikas (7 Universals + 4 Occasionals [vitakka, vicāra, adhimokkha, viriya] + 4 Akusala Universals [moha, ahirika, anottappa, uddhacca])",
                "es": "Contiene 15 Cetasikas (7 Universales + 4 Ocasionales [vitakka, vicāra, adhimokkha, viriya] + 4 Akusala Universales [moha, ahirika, anottappa, uddhacca])"
            },
            "philosophy": {
                "pt": "Embora uddhacca seja um dos 4 cetasikas prejudiciais universais (presente em todos os 12 cittas akusala), nos outros 11 cittas sua força é secundária; neste 12º citta, porém, sem lobha, dosa ou vicikicchā, a inquietação torna-se o fator principal. Por ser o mais fraco de todos os 12 cittas akusala, é o único citta prejudicial incapaz de produzir renascimento nos planos inferiores (apāyabhūmi), embora possa gerar resultados kármicos secundários durante o curso da existência (pavatti). Só é erradicado pelo caminho do Arahant.",
                "en": "Although uddhacca is one of the 4 universal unwholesome cetasikas (present in all 12 akusala cittas), in the other 11 cittas its force is secondary; in this 12th citta, however, without lobha, dosa, or vicikicchā, restlessness is the chief factor. Being the weakest of the 12 akusala cittas, it is the only unwholesome citta incapable of generating rebirth-linking (paṭisandhi) in the woeful planes (apāyabhūmi), though it can produce results during the course of existence (pavatti). It is eradicated only by the path of Arahantship.",
                "es": "Aunque uddhacca está presente en los 12 cittas akusala, en este 12º citta es el factor principal. Por ser el más débil de los 12 cittas akusala, es el único incapaz de producir reconexión (paṭisandhi) en los planos inferiores (apāyabhūmi), aunque produce resultados durante el curso de la existencia (pavatti)."
            },
            "bodhiRef": "CMA I, §6 (Guide, pp. 39–40); II, §26 (p. 108); V, §27 (p. 210)"
        },
        "seeAlso": ["uddhacca", "vicikicchāsampayutta", "moha", "momūha"]
    },

    "sobhana": {
        "meaning": {
            "pt": "Belo; resplandecente; purificado; designação coletiva dos 59 (ou 91) cittas e 25 cetasikas que são acompanhados pelas raízes belas (alobha, adosa e, opcionalmente ou necessariamente, amoha).",
            "en": "Beautiful; resplendent; purified; collective designation for the 59 (or 91) cittas and 25 cetasikas accompanied by the beautiful roots (alobha, adosa, and optionally or necessarily amoha).",
            "es": "Hermoso; resplandeciente; purificado; designación colectiva de los 59 (o 91) cittas y 25 cetasikas acompañados por las raíces hermosas (alobha, adosa y amoha)."
        },
        "grammar": "adj./nt. (de √subh + ana)",
        "grammarLocalized": {
            "pt": "Adjetivo / Substantivo neutro (derivado da raiz √subh 'brilhar, embelezar')",
            "en": "Adjective / Neuter noun (derived from root √subh 'to shine, beautify')",
            "es": "Adjetivo / Sustantivo neutro (derivado de la raíz √subh 'brillar, embellecer')"
        },
        "root": "√subh (brilhar / resplandecer) + ana",
        "etymology": {
            "pt": "Da raiz √subh ('brilhar, ser belo, resplandecer') + sufixo -ana. São chamados 'belos' porque embelezam o fluxo mental e são livres da feiura das impurezas (kilesa).",
            "en": "From the root √subh ('to shine, be splendid, beautify') + suffix -ana. Called 'beautiful' because they adorn the mental continuum and are free from the ugliness of defilements (kilesa).",
            "es": "De la raíz √subh ('brillar, ser hermoso') + sufijo -ana. Se llaman 'hermosos' porque embellecen el continuo mental y están libres de las impurezas."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Grande Divisão de Cittas (59/91) e Cetasikas (25)",
                "en": "Major Division of Cittas (59/91) and Cetasikas (25)",
                "es": "Gran División de Cittas (59/91) y Cetasikas (25)"
            },
            "category": {
                "pt": "Abrange 3 Jātis: Kusala (21/37), Vipāka com raiz (21/37) e Kiriya com raiz (17)",
                "en": "Encompasses 3 Jātis: Kusala (21/37), Rooted Vipāka (21/37), and Rooted Kiriya (17)",
                "es": "Abarca 3 Jātis: Kusala (21/37), Vipāka con raíz (21/37) y Kiriya con raíz (17)"
            },
            "philosophy": {
                "pt": "Segundo Bhikkhu Bodhi (CMA I, §12, pp. 46–47), sobhana é mais amplo que kusala: inclui não apenas todas as consciências salutares (kusala), mas também todas as consciências resultantes (vipāka) e funcionais (kiriya) que possuem raízes belas (sahetuka), ou seja, os 24 kāmāvacarasobhana, os 15 rūpāvacara, os 12 arūpāvacara e os 8 (ou 40) lokuttara. Os 30 cittas restantes (12 akusala + 18 ahetuka) são chamados asobhana (não-belos).",
                "en": "According to Bhikkhu Bodhi (CMA I, §12, pp. 46–47), sobhana is broader than kusala: it includes not only all wholesome (kusala) cittas, but also all resultant (vipāka) and functional (kiriya) cittas possessing beautiful roots (sahetuka) — namely, the 24 kāmāvacarasobhana, 15 rūpāvacara, 12 arūpāvacara, and 8 (or 40) lokuttara cittas. The remaining 30 cittas (12 akusala + 18 ahetuka) are termed asobhana (non-beautiful).",
                "es": "Según Bhikkhu Bodhi (CMA I, §12, pp. 46–47), sobhana es más amplio que kusala: incluye no solo todas las conciencias saludables (kusala), sino también todas las conciencias resultantes (vipāka) y funcionales (kiriya) dotadas de raíces hermosas. Los 30 cittas restantes (12 akusala + 18 ahetuka) se denominan asobhana (no hermosos)."
            },
            "bodhiRef": "CMA I, §12 (Guide, pp. 46–47); II, §§5–8 (pp. 85–90)"
        },
        "seeAlso": ["kusala", "sobhanasādhāraṇa", "alobha", "adosa", "amoha", "mahākusala"]
    },

    "mahaggata": {
        "meaning": {
            "pt": "Sublime; exaltado; que alcançou a grandeza; designação conjunta das 27 consciências de jhāna pertencentes à esfera da matéria sutil (15 rūpāvacara) e à esfera imaterial (12 arūpāvacara).",
            "en": "Sublime; exalted; having reached greatness; collective designation for the 27 jhāna consciousnesses pertaining to the fine-material sphere (15 rūpāvacara) and immaterial sphere (12 arūpāvacara).",
            "es": "Sublime; exaltado; que ha alcanzado la grandeza; designación conjunta de las 27 conciencias de jhāna pertenecientes a la esfera de la materia sutil (15 rūpāvacara) y a la esfera inmaterial (12 arūpāvacara)."
        },
        "grammar": "adj. composto (mahanta > mahā + gata)",
        "grammarLocalized": {
            "pt": "Adjetivo composto (Dutiyā-Tappurisa: mahā + gata)",
            "en": "Compound adjective (Dutiyā-Tappurisa: mahā + gata)",
            "es": "Adjetivo compuesto (Dutiyā-Tappurisa: mahā + gata)"
        },
        "root": "mahā (grande) + √gam (ir / alcançar) + ta",
        "etymology": {
            "pt": "De mahā (mahant = grande, vasto, elevado) + gata (ido a, chegado a, de √gam + -ta). Explicado nos Comentários como estados que 'chegaram à grandeza' (mahantabhāvaṃ gata) por terem superado os obstáculos (nīvaraṇa), por sua vasta extensão meditativa e por serem cultivados com grande aspiração (chanda), energia (viriya), mente (citta) e investigação (vīmaṃsā).",
            "en": "From mahā (mahant = great, vast, lofty) + gata (gone to, reached, from √gam + -ta). Explained in the Commentaries as states that have 'reached greatness' (mahantabhāvaṃ gata) by overcoming the hindrances (nīvaraṇa), by their vast meditative scope, and by being developed with great aspiration (chanda), energy (viriya), mind (citta), and investigation (vīmaṃsā).",
            "es": "De mahā (grande, vasto) + gata (llegado a, de √gam + -ta). Explicado en los Comentarios como estados que han 'alcanzado la grandeza' (mahantabhāvaṃ gata) al superar los obstáculos (nīvaraṇa)."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Acusativo (Dutiyā-Tappurisa)",
                "en": "Accusative Determinative Compound (Dutiyā-Tappurisa)",
                "es": "Compuesto Determinativo Acusativo (Dutiyā-Tappurisa)"
            },
            "viggaha": "mahantabhāvaṃ gatā'ti = mahaggatā",
            "literal": {
                "pt": "Aquilo que chegou ao estado de grandeza ou sublimidade.",
                "en": "That which has arrived at the state of greatness or sublimity.",
                "es": "Aquello que ha llegado al estado de grandeza o sublimidad."
            },
            "parts": [
                {"part": "mahā", "gloss": {"pt": "grandeza, vastidão", "en": "greatness, vastness", "es": "grandeza, vastedad"}},
                {"part": "gata", "gloss": {"pt": "chegado a, alcançado", "en": "gone to, reached", "es": "llegado a, alcanzado"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Agrupamento dos Cittas de Absorção Mundana (27 Cittas)",
                "en": "Grouping of Mundane Absorption Cittas (27 Cittas)",
                "es": "Agrupación de los Cittas de Absorción Mundana (27 Cittas)"
            },
            "category": {
                "pt": "15 Rūpāvacara Cittas + 12 Arūpāvacara Cittas = 27 Mahaggata Cittas (9 Kusala + 9 Vipāka + 9 Kiriya)",
                "en": "15 Rūpāvacara Cittas + 12 Arūpāvacara Cittas = 27 Mahaggata Cittas (9 Kusala + 9 Vipāka + 9 Kiriya)",
                "es": "15 Rūpāvacara Cittas + 12 Arūpāvacara Cittas = 27 Mahaggata Cittas (9 Kusala + 9 Vipāka + 9 Kiriya)"
            },
            "philosophy": {
                "pt": "Na tríade de extensão (paritta / mahaggata / appamāṇa), os fenômenos da esfera sensorial (54 cittas + 28 rūpas) são chamados paritta ('limitados' ou 'pequenos'); os 27 cittas de rūpāvacara e arūpāvacara são chamados mahaggata ('sublimes' ou 'exaltados'); e os 8/40 cittas lokuttara mais Nibbāna são chamados appamāṇa ('imensuráveis'). Todos os 27 cittas mahaggata são invariavelmente triplamente enraizados (tihetuka, acompanhados por alobha, adosa e amoha) e excluem as três abstinências (virati).",
                "en": "In the triad of scope (paritta / mahaggata / appamāṇa), sense-sphere phenomena (54 cittas + 28 rūpas) are termed paritta ('limited'); the 27 rūpāvacara and arūpāvacara cittas are termed mahaggata ('sublime' or 'exalted'); and the 8/40 lokuttara cittas plus Nibbāna are termed appamāṇa ('immeasurable'). All 27 mahaggata cittas are invariably triple-rooted (tihetuka) and exclude the three abstinences (virati).",
                "es": "En la tríada de alcance (paritta / mahaggata / appamāṇa), los fenómenos de la esfera sensorial se llaman paritta ('limitados'), los 27 cittas de rūpāvacara y arūpāvacara se llaman mahaggata ('sublimes') y los lokuttara más Nibbāna se llaman appamāṇa ('inconmensurables')."
            },
            "bodhiRef": "CMA I, §25 (Guide, pp. 65–66); II, §§21–22 (pp. 103–104); III, §18 (p. 139)"
        },
        "seeAlso": ["rūpāvacara", "arūpāvacara", "jhāna", "appanā", "paritta"]
    },

    "jhāna": {
        "meaning": {
            "pt": "Absorção meditativa; contemplação estreita de um objeto e queima dos fatores opositores (5 fatores de jhāna: vitakka, vicāra, pīti, sukha e ekaggatā).",
            "en": "Meditative absorption; closely contemplating an object and burning up opposing states (5 jhāna factors: vitakka, vicāra, pīti, sukha, and ekaggatā).",
            "es": "Absorción meditativa; contemplación estrecha de un objeto y quema de los estados opositores (5 factores de jhāna: vitakka, vicāra, pīti, sukha y ekaggatā)."
        },
        "grammar": "nt. (de √jhe + ana)",
        "grammarLocalized": {
            "pt": "Substantivo neutro (derivado de √jhe [meditar/contemplar] e √jhā [queimar])",
            "en": "Neuter noun (derived from √jhe [to meditate/think closely] and √jhā [to burn up])",
            "es": "Sustantivo neutro (derivado de √jhe [meditar/contemplar] y √jhā [quemar])"
        },
        "root": "√jhe (contemplar) / √jhā (queimar) + ana",
        "etymology": {
            "pt": "Como cita Bhikkhu Bodhi (CMA I, §§18–20, p. 55 & nota 5, citando Vism. IV, 119), os Comentários dão dupla derivação para jhāna: 'ārammaṇ'upanijjhānato paccanīkajjhāpanato jhānaṃ' — é chamado jhāna (1) porque contempla estreitamente o objeto (ārammaṇa-upanijjhāna, de √jhe) e (2) porque queima ou incinera os estados adversos (paccanīka-jhāpana, de √jhā), isto é, os cinco obstáculos mentais (pañca nīvaraṇāni).",
            "en": "As Bhikkhu Bodhi explains (CMA I, §§18–20, p. 55 & n. 5, citing Vism. IV, 119), the Commentaries give a twofold derivation for jhāna: 'ārammaṇ'upanijjhānato paccanīkajjhāpanato jhānaṃ' — it is called jhāna (1) because it closely contemplates the object (ārammaṇa-upanijjhāna, from √jhe) and (2) because it burns up opposing states (paccanīka-jhāpana, from √jhā), namely the five mental hindrances (pañca nīvaraṇāni).",
            "es": "Como explica Bhikkhu Bodhi (CMA I, §§18–20, p. 55 y n. 5, citando Vism. IV, 119), los Comentarios dan una doble derivación para jhāna: 'ārammaṇ'upanijjhānato paccanīkajjhāpanato jhānaṃ' — (1) porque contempla estrechamente el objeto (upanijjhāna, de √jhe) y (2) porque quema los estados adversos (paccanīka-jhāpana, de √jhā), es decir, los cinco obstáculos (nīvaraṇa)."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Fatores Constituintes de Absorção (Jhānaṅgāni — Cetasikas) e Cittas de Absorção",
                "en": "Constituent Factors of Absorption (Jhānaṅgāni — Cetasikas) and Absorption Cittas",
                "es": "Factores Constitutivos de Absorción (Jhānaṅgāni — Cetasikas) y Cittas de Absorción"
            },
            "category": {
                "pt": "5 Jhānas Rūpāvacara, 4 Jhānas Arūpāvacara e 5 Níveis de Jhāna Lokuttara; 5 Fatores de Jhāna: Vitakka, Vicāra, Pīti, Sukha/Upekkhā, Ekaggatā",
                "en": "5 Rūpāvacara Jhānas, 4 Arūpāvacara Jhānas, and 5 Levels of Lokuttara Jhāna; 5 Jhāna Factors: Vitakka, Vicāra, Pīti, Sukha/Upekkhā, Ekaggatā",
                "es": "5 Rūpāvacara Jhānas, 4 Arūpāvacara Jhānas y 5 Niveles de Jhāna Lokuttara; 5 Factores de Jhāna: Vitakka, Vicāra, Pīti, Sukha/Upekkhā, Ekaggatā"
            },
            "philosophy": {
                "pt": "Os cinco fatores de jhāna (jhānaṅga) combatem diretamente os cinco obstáculos (nīvaraṇa): (1) vitakka (aplicação inicial) contrapõe-se ao torpor e languidez (thīna-middha); (2) vicāra (aplicação sustentada) contrapõe-se à dúvida (vicikicchā); (3) pīti (êxtase/entusiasmo) contrapõe-se à má vontade (vyāpāda); (4) sukha (felicidade) contrapõe-se à inquietação e remorso (uddhacca-kukkucca); e (5) ekaggatā (unidirecionalidade) contrapõe-se ao desejo sensorial (kāmacchanda). No método quíntuplo do Abhidhamma (pañcakanaya), os fatores são abandonados um a um do 1º ao 5º jhāna.",
                "en": "The five jhāna factors (jhānaṅga) directly counter the five hindrances (nīvaraṇa): (1) vitakka (initial application) counters sloth and torpor (thīna-middha); (2) vicāra (sustained application) counters doubt (vicikicchā); (3) pīti (zest) counters ill will (vyāpāda); (4) sukha (happiness) counters restlessness and worry (uddhacca-kukkucca); and (5) ekaggatā (one-pointedness) counters sensual desire (kāmacchanda). In the fivefold Abhidhamma method (pañcakanaya), the factors are abandoned one by one from the 1st to the 5th jhāna.",
                "es": "Los cinco factores de jhāna (jhānaṅga) contrarrestan directamente los cinco obstáculos (nīvaraṇa): (1) vitakka contrarresta thīna-middha; (2) vicāra contrarresta vicikicchā; (3) pīti contrarresta vyāpāda; (4) sukha contrarresta uddhacca-kukkucca; y (5) ekaggatā contrarresta kāmacchanda."
            },
            "bodhiRef": "CMA I, §§18–21, §§30–31 (Guide, pp. 54–62, 70–73); VII, §16 (p. 274); IX, §§14–20 (pp. 339–343)"
        },
        "seeAlso": ["vitakka", "vicāra", "pīti", "sukha", "ekaggatā", "rūpāvacara", "nīvaraṇa"]
    }
})

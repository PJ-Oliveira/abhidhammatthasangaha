# -*- coding: utf-8 -*-
"""
Parte 2 do Léxico Filosófico do Abhidhammattha Saṅgaha (Baseado em Bhikkhu Bodhi, CMA Cap. II):
- Todos os 52 Fatores Mentais (Cetasikas) com o método clássico completo das 4 definições (Lakkhaṇādi-catukka):
  1. Característica (Lakkhaṇa)
  2. Função (Rasa)
  3. Manifestação (Paccupaṭṭhāna)
  4. Causa Próxima (Padaṭṭhāna)
- Mais os grupos de cetasikas (aññasamāna, sabbacittasādhāraṇa, pakiṇṇaka, sobhanasādhāraṇa, virati, appamaññā).
"""

PART2_ENTRIES = {
    "aññasamāna": {
        "meaning": {
            "pt": "Eticamente variável; literalmente 'comum ao outro'; designação dos 13 fatores mentais (7 universais + 6 ocasionais) que são comuns tanto às consciências belas (sobhana) quanto às não-belas (asobhana), assumindo a qualidade ética dos demais concomitantes.",
            "en": "Ethically variable; literally 'common to the other'; designation for the 13 mental factors (7 universals + 6 occasionals) common to both beautiful (sobhana) and non-beautiful (asobhana) cittas, assuming the ethical quality imparted by their concomitants.",
            "es": "Éticamente variable; literalmente 'común al otro'; designación de los 13 factores mentales (7 universales + 6 ocasionales) comunes tanto a las conciencias hermosas (sobhana) como a las no hermosas (asobhana), asumiendo la cualidad ética de sus concomitantes."
        },
        "grammar": "adj. composto (añña + samāna)",
        "grammarLocalized": {
            "pt": "Adjetivo composto (Tatiyā / Chaṭṭhī-Tappurisa)",
            "en": "Compound adjective (Tatiyā / Chaṭṭhī-Tappurisa)",
            "es": "Adjetivo compuesto (Tatiyā / Chaṭṭhī-Tappurisa)"
        },
        "root": "añña (outro) + samāna (comum / igual)",
        "etymology": {
            "pt": "De añña ('o outro' — para os cittas belos, os não-belos são 'o outro', e vice-versa) + samāna ('comum, igual, semelhante').",
            "en": "From añña ('the other' — non-beautiful cittas are 'other' in relation to beautiful cittas, and vice versa) + samāna ('common, shared, alike').",
            "es": "De añña ('el otro' — los cittas no hermosos son 'el otro' respecto a los hermosos, y viceversa) + samāna ('común, igual')."
        },
        "samasa": {
            "type": {
                "pt": "Composto Determinativo (Tappurisa)",
                "en": "Determinative Compound (Tappurisa)",
                "es": "Compuesto Determinativo (Tappurisa)"
            },
            "viggaha": "aññesaṃ (aññehi vā) samānā'ti = aññasamānā",
            "literal": {
                "pt": "Aqueles fatores que são comuns ou semelhantes à classe oposta ('à outra').",
                "en": "Those factors that are common or shared with the opposite ('the other') class.",
                "es": "Aquellos factores que son comunes o compartidos con la clase opuesta ('la otra')."
            },
            "parts": [
                {"part": "añña", "gloss": {"pt": "outro, classe oposta", "en": "other, opposite class", "es": "otro, clase opuesta"}},
                {"part": "samāna", "gloss": {"pt": "comum, compartilhado", "en": "common, shared", "es": "común, compartido"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "1ª Grande Divisão dos Fatores Mentais (Cetasika — 13 de 52)",
                "en": "1st Major Division of Mental Factors (Cetasika — 13 of 52)",
                "es": "1ª Gran División de los Factores Mentales (Cetasika — 13 de 52)"
            },
            "category": {
                "pt": "13 Aññasamāna = 7 Universais (Sabbacittasādhāraṇa) + 6 Ocasionais (Pakiṇṇaka)",
                "en": "13 Aññasamāna = 7 Universals (Sabbacittasādhāraṇa) + 6 Occasionals (Pakiṇṇaka)",
                "es": "13 Aññasamāna = 7 Universales (Sabbacittasādhāraṇa) + 6 Ocasionales (Pakiṇṇaka)"
            },
            "philosophy": {
                "pt": "Como explica Bhikkhu Bodhi (CMA II, §2, p. 78), os 13 fatores aññasamāna são camaleônicos quanto ao valor moral: em cittas salutares (kusala) tornam-se salutares; em cittas prejudiciais (akusala) tornam-se prejudiciais; e em cittas indeterminados (abyākata: vipāka e kiriya) tornam-se indeterminados, conforme as raízes (hetu) e fatores com que se associam.",
                "en": "As Bhikkhu Bodhi explains (CMA II, §2, p. 78), the 13 aññasamāna factors assume the ethical quality imparted to the citta by the other cetasikas, particularly the associated roots (hetu): in wholesome cittas they become wholesome, in unwholesome cittas they become unwholesome, and in indeterminate cittas they become kammically indeterminate.",
                "es": "Como explica Bhikkhu Bodhi (CMA II, §2, p. 78), los 13 factores aññasamāna asumen la cualidad ética impartida al citta por los demás cetasikas, en particular las raíces asociadas (hetu)."
            },
            "bodhiRef": "CMA II, §§2–3 (Guide, pp. 78–82)"
        },
        "seeAlso": ["sabbacittasādhāraṇa", "pakiṇṇaka", "cetasika"]
    },

    "sabbacittasādhāraṇa": {
        "meaning": {
            "pt": "Universal; comum a toda consciência; os 7 fatores mentais presentes invariavelmente em todas as 89 (ou 121) consciências: contato (phassa), sensação (vedanā), percepção (saññā), volição (cetanā), unidirecionalidade (ekaggatā), faculdade vital mental (jīvitindriya) e atenção (manasikāra).",
            "en": "Universal; common to every consciousness; the 7 mental factors invariably present in all 89 (or 121) cittas: contact (phassa), feeling (vedanā), perception (saññā), volition (cetanā), one-pointedness (ekaggatā), mental life faculty (jīvitindriya), and attention (manasikāra).",
            "es": "Universal; común a toda conciencia; los 7 factores mentales invariablemente presentes en las 89 (o 121) conciencias: contacto (phassa), sensación (vedanā), percepción (saññā), volición (cetanā), unidireccionalidad (ekaggatā), facultad vital mental (jīvitindriya) y atención (manasikāra)."
        },
        "grammar": "adj. composto (sabba + citta + sādhāraṇa)",
        "grammarLocalized": {
            "pt": "Adjetivo composto (Chaṭṭhī-Tappurisa)",
            "en": "Compound adjective (Chaṭṭhī-Tappurisa)",
            "es": "Adjetivo compuesto (Chaṭṭhī-Tappurisa)"
        },
        "root": "sabba + citta + sa + ā + √dhar + aṇa",
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Genitivo (Chaṭṭhī-Tappurisa)",
                "en": "Genitive Determinative Compound (Chaṭṭhī-Tappurisa)",
                "es": "Compuesto Determinativo Genitivo (Chaṭṭhī-Tappurisa)"
            },
            "viggaha": "sabbesaṃ cittānaṃ sādhāraṇā = sabbacittasādhāraṇā",
            "literal": {
                "pt": "Comuns (sādhāraṇa) a todas (sabba) as consciências (citta).",
                "en": "Common (sādhāraṇa) to all (sabba) consciousnesses (citta).",
                "es": "Comunes (sādhāraṇa) a todas (sabba) las conciencias (citta)."
            },
            "parts": [
                {"part": "sabba", "gloss": {"pt": "toda, cada", "en": "all, every", "es": "toda, cada"}},
                {"part": "citta", "gloss": {"pt": "consciência (89/121)", "en": "consciousness (89/121)", "es": "conciencia (89/121)"}},
                {"part": "sādhāraṇa", "gloss": {"pt": "comum, universal", "en": "common, universal", "es": "común, universal"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Grupo dos 7 Cetasikas Universais (Cetasika #1–#7)",
                "en": "Group of the 7 Universal Cetasikas (Cetasika #1–#7)",
                "es": "Grupo de los 7 Cetasikas Universales (Cetasika #1–#7)"
            },
            "category": {
                "pt": "Presentes em todos os 89 / 121 Cittas sem exceção; constituem a estrutura mínima da cognição",
                "en": "Present in all 89 / 121 Cittas without exception; they constitute the minimal architecture of cognition",
                "es": "Presentes en todos los 89 / 121 Cittas sin excepción; constituyen la estructura mínima de la cognición"
            },
            "philosophy": {
                "pt": "Estes sete fatores desempenham as funções cognitivas mais rudimentares e indispensáveis, sem as quais o conhecimento de qualquer objeto seria impossível. Nas dez consciências sensoriais puras (dvipañcaviññāṇa — ver, ouvir, cheirar, saborear, tocar), apenas estes sete fatores universais acompanham a consciência.",
                "en": "These seven factors perform the most rudimentary and essential cognitive functions, without which consciousness of an object would be utterly impossible. In the ten bare sense-consciousnesses (dvipañcaviññāṇa — seeing, hearing, smelling, tasting, touching), these seven universals alone accompany consciousness.",
                "es": "Estos siete factores desempeñan las funciones cognitivas más rudimentarias e indispensables, sin las cuales la conciencia de un objeto sería imposible. En las diez conciencias sensoriales desnudas (dvipañcaviññāṇa), solo estos siete universales acompañan a la conciencia."
            },
            "bodhiRef": "CMA II, §2 & §11 (Guide, pp. 78–80, 95)"
        },
        "seeAlso": ["phassa", "vedanā", "saññā", "cetanā", "ekaggatā", "jīvitindriya", "manasikāra"]
    },

    # ── 7 UNIVERSAIS (SABBACCITTASĀDHĀRAṆA) ──────────────────────────────────
    "phassa": {
        "meaning": {
            "pt": "Contato; toque mental; o fator mental universal pelo qual a consciência 'toca' mentalmente o objeto que entrou no campo de foco, iniciando todo o evento cognitivo.",
            "en": "Contact; mental touch; the universal mental factor by which consciousness mentally 'touches' the object that has appeared in focus, thereby initiating the entire cognitive event.",
            "es": "Contacto; toque mental; el factor mental universal por el cual la conciencia 'toca' mentalmente el objeto que ha aparecido en foco, iniciando todo el evento cognitivo."
        },
        "grammar": "masc. (de √phus + a)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (derivado da raiz √phus 'tocar')",
            "en": "Masculine noun (derived from root √phus 'to touch')",
            "es": "Sustantivo masculino (derivado de la raíz √phus 'tocar')"
        },
        "root": "√phus (tocar / atingir) + a",
        "etymology": {
            "pt": "Derivado do verbo phusati ('tocar'). Não deve ser confundido com o mero impacto físico do objeto no órgão sensorial: é um fator estritamente mental (arūpadhamma) que faz a mente tocar o objeto.",
            "en": "Derived from the verb phusati ('to touch'). It must not be confused with the mere physical impact of an object on a bodily sense organ: it is a strictly mental factor (arūpadhamma) whereby the mind touches the object.",
            "es": "Derivado del verbo phusati ('tocar'). No debe confundirse con el mero impacto físico en el órgano sensorial: es un factor estrictamente mental (arūpadhamma)."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal (Cetasika #1 de 52)",
                "en": "Ultimate Reality — Universal Mental Factor (Cetasika #1 of 52)",
                "es": "Realidad Última — Factor Mental Universal (Cetasika #1 de 52)"
            },
            "category": {
                "pt": "Universal (Sabbacittasādhāraṇa — presente em todos os 89/121 cittas); pertencente a Saṅkhārakkhandha",
                "en": "Universal (Sabbacittasādhāraṇa — present in all 89/121 cittas); belonging to Saṅkhārakkhandha",
                "es": "Universal (Sabbacittasādhāraṇa — presente en los 89/121 cittas); perteneciente a Saṅkhārakkhandha"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Tocar o objeto (phusana-lakkhaṇa).",
                    "en": "Touching the object (phusana-lakkhaṇa).",
                    "es": "Tocar el objeto (phusana-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "O impacto ou choque cognitivo (saṅghaṭṭana-rasa), pois faz a consciência e o objeto colidirem cognitivamente.",
                    "en": "Impingement (saṅghaṭṭana-rasa), as it causes consciousness and the object to impinge.",
                    "es": "El impacto o choque cognitivo (saṅghaṭṭana-rasa), pues hace que la conciencia y el objeto incidan mutuamente."
                },
                "paccupatthana": {
                    "pt": "A concorrência ou encontro tríplice (saṅgati-paccupaṭṭhāna) entre consciência, faculdade sensorial e objeto.",
                    "en": "The concurrence or coming together (saṅgati-paccupaṭṭhāna) of consciousness, sense faculty, and object.",
                    "es": "La concurrencia o encuentro triple (saṅgati-paccupaṭṭhāna) de conciencia, facultad sensorial y objeto."
                },
                "padatthana": {
                    "pt": "Um campo objetivo que entrou em foco de atenção (āhatavisaya-padaṭṭhāna).",
                    "en": "An objective field that has come into focus (āhatavisaya-padaṭṭhāna).",
                    "es": "Un campo objetivo que ha entrado en foco (āhatavisaya-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Na Originação Dependente (paṭiccasamuppāda, Cap. VIII), phassa é o elo condicionante imediato da sensação ('phassapaccayā vedanā') e é também um dos quatro nutrimentos (phassāhāra, Cap. VII, §21), pois nutre a experiência afetiva.",
                "en": "In Dependent Arising (paṭiccasamuppāda, Ch. VIII), phassa is the immediate condition for feeling ('phassapaccayā vedanā') and is also one of the four nutriments (phassāhāra, Ch. VII, §21), sustaining affective experience.",
                "es": "En el Surgimiento Dependiente (paṭiccasamuppāda, Cap. VIII), phassa es la condición inmediata para la sensación ('phassapaccayā vedanā') y es uno de los cuatro alimentos (phassāhāra, Cap. VII, §21)."
            },
            "bodhiRef": "CMA II, §2 (Guide, p. 78); VIII, §3 (p. 297)"
        },
        "seeAlso": ["vedanā", "sabbacittasādhāraṇa", "saḷāyatana", "āhāra"]
    },

    "vedanā": {
        "meaning": {
            "pt": "Sensação; tom afetivo da experiência; o fator mental universal que sente o objeto como agradável, doloroso ou neutro (classificado em 3 tipos por qualidade ou 5 tipos por faculdade).",
            "en": "Feeling; affective tone of experience; the universal mental factor that feels the object as pleasant, painful, or neutral (classified into 3 types by quality or 5 types by faculty).",
            "es": "Sensación; tono afectivo de la experiencia; el factor mental universal que siente el objeto como agradable, doloroso o neutro (clasificado en 3 tipos por cualidad o 5 tipos por facultad)."
        },
        "grammar": "fem. (de √vid + anā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (derivado da raiz √vid 'sentir, experienciar')",
            "en": "Feminine noun (derived from root √vid 'to feel, experience')",
            "es": "Sustantivo femenino (derivado de la raíz √vid 'sentir, experimentar')"
        },
        "root": "√vid (sentir / experienciar) + anā",
        "etymology": {
            "pt": "Derivado da raiz √vid no sentido de 'sentir, provar o sabor de um objeto' (vedayati). Como sublinha Bhikkhu Bodhi, vedanā não significa 'emoção' (que é um complexo de vários fatores no saṅkhārakkhandha), mas a qualidade afetiva nua da experiência.",
            "en": "Derived from the root √vid in the sense of 'to feel, experience the taste of an object' (vedayati). As Bhikkhu Bodhi emphasizes, vedanā does not signify complex 'emotion' (which involves various factors in saṅkhārakkhandha), but the bare affective quality of an experience.",
            "es": "Derivado de la raíz √vid en el sentido de 'sentir, experimentar el sabor de un objeto'. Como subraya Bhikkhu Bodhi, vedanā no significa 'emoción' compleja, sino la cualidad afectiva desnuda de la experiencia."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal (Cetasika #2 de 52) & 2º Agregado (Vedanākkhandha)",
                "en": "Ultimate Reality — Universal Mental Factor (Cetasika #2 of 52) & 2nd Aggregate (Vedanākkhandha)",
                "es": "Realidad Última — Factor Mental Universal (Cetasika #2 de 52) y 2º Agregado (Vedanākkhandha)"
            },
            "category": {
                "pt": "Universal (Sabbacittasādhāraṇa); 5 faculdades afetivas: Sukha, Dukkha, Somanassa, Domanassa, Upekkhā",
                "en": "Universal (Sabbacittasādhāraṇa); 5 affective faculties: Sukha, Dukkha, Somanassa, Domanassa, Upekkhā",
                "es": "Universal (Sabbacittasādhāraṇa); 5 facultades afectivas: Sukha, Dukkha, Somanassa, Domanassa, Upekkhā"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "O que é sentido / experimentado afetivamente (vedayita-lakkhaṇa).",
                    "en": "Being felt / affectively experienced (vedayita-lakkhaṇa).",
                    "es": "Lo que es sentido / experimentado afectivamente (vedayita-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Experimentar o sabor do objeto (anubhavana-rasa) ou desfrutar de seu aspecto desejável.",
                    "en": "Experiencing the taste of the object (anubhavana-rasa), or enjoying its desirable aspect.",
                    "es": "Experimentar el sabor del objeto (anubhavana-rasa), o disfrutar de su aspecto deseable."
                },
                "paccupatthana": {
                    "pt": "O saborear dos fatores mentais associados (cetasikassāda-paccupaṭṭhāna).",
                    "en": "The relishing of the associated mental factors (cetasikassāda-paccupaṭṭhāna).",
                    "es": "El saborear de los factores mentales asociados (cetasikassāda-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O contato (phassa-padaṭṭhāna, em sentido geral: 'phassapaccayā vedanā') ou a tranquilidade (passaddhi, no caso da sensação agradável meditativa).",
                    "en": "Contact (phassa-padaṭṭhāna, in general: 'phassapaccayā vedanā') or tranquillity (passaddhi, for meditative pleasant feeling).",
                    "es": "El contacto (phassa-padaṭṭhāna, en general: 'phassapaccayā vedanā') o la tranquilidad (passaddhi, en la sensación agradable meditativa)."
                }
            },
            "philosophy": {
                "pt": "Enquanto os demais fatores mentais experimentam o objeto apenas parcialmente (como o cozinheiro que prepara um prato para o rei e apenas prova um pouco), vedanā experimenta o sabor do objeto de modo soberano e pleno (como o rei que saboreia o banquete). No Cap. III (§§2–4), analisa-se em 3 tipos por natureza (sukha, dukkha, adukkhamasukha) e em 5 tipos por faculdade (indriyabhedena): sukha (prazer corporal, em 1 citta), dukkha (dor corporal, em 1 citta), somanassa (alegria mental, em 62 cittas), domanassa (desprazer mental, em 2 cittas) e upekkhā (equanimidade/neutralidade afetiva, em 55 cittas).",
                "en": "Whereas the other mental factors experience the object only derivatively (like a cook who prepares a dish for a king and merely samples it), vedanā experiences the object directly and fully (like the king who enjoys the meal). In Ch. III (§§2–4), feeling is analyzed as threefold by nature (sukha, dukkha, adukkhamasukha) and fivefold by faculty (indriyabhedena): sukha (bodily pleasure, 1 citta), dukkha (bodily pain, 1 citta), somanassa (mental joy, 62 cittas), domanassa (mental displeasure, 2 cittas), and upekkhā (neutral feeling, 55 cittas).",
                "es": "Mientras los demás factores mentales experimentan el objeto derivadamente (como el cocinero que prueba el plato), vedanā lo saborea plenamente (como el rey que disfruta del banquete). En el Cap. III (§§2–4) se analiza en 5 tipos por facultad: sukha (1 citta), dukkha (1 citta), somanassa (62 cittas), domanassa (2 cittas) y upekkhā (55 cittas)."
            },
            "bodhiRef": "CMA II, §2 (Guide, p. 79); III, §§2–4 (Guide, pp. 115–118)"
        },
        "seeAlso": ["phassa", "sukha", "dukkha", "somanassa", "domanassa", "upekkhā", "taṇhā"]
    },

    "saññā": {
        "meaning": {
            "pt": "Percepção; reconhecimento; o fator mental universal que apreende as marcas ou sinais distintivos de um objeto, permitindo reconhecê-lo novamente ('isto é o mesmo').",
            "en": "Perception; recognition; the universal mental factor that apprehends the distinctive marks or signs of an object, enabling one to recognize it again ('this is the same').",
            "es": "Percepción; reconocimiento; el factor mental universal que aprehende las marcas o signos distintivos de un objeto, permitiendo reconocerlo nuevamente ('esto es lo mismo')."
        },
        "grammar": "fem. (saṃ + √ñā + ā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (saṃ [junto/por sinais] + √ñā [conhecer])",
            "en": "Feminine noun (saṃ [together/by marks] + √ñā [to know])",
            "es": "Sustantivo femenino (saṃ [junto/por marcas] + √ñā [conocer])"
        },
        "root": "saṃ (junto / por marcas) + √ñā (conhecer) + ā",
        "etymology": {
            "pt": "De saṃ- (reunindo marcas) + √ñā ('conhecer, notar'): sañjānātī'ti saññā — conhece ao tomar nota das marcas distintivas (azul, amarelo, longo, curto, etc.).",
            "en": "From saṃ- (putting marks together) + √ñā ('to know, note'): sañjānātī'ti saññā — it perceives by noting distinctive marks (blue, yellow, etc.).",
            "es": "De saṃ- (reuniendo marcas) + √ñā ('conocer, notar'): sañjānātī'ti saññā — percibe tomando nota de las marcas distintivas."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal (Cetasika #3 de 52) & 3º Agregado (Saññākkhandha)",
                "en": "Ultimate Reality — Universal Mental Factor (Cetasika #3 of 52) & 3rd Aggregate (Saññākkhandha)",
                "es": "Realidad Última — Factor Mental Universal (Cetasika #3 de 52) y 3º Agregado (Saññākkhandha)"
            },
            "category": {
                "pt": "Universal (Sabbacittasādhāraṇa — presente em todos os 89/121 cittas)",
                "en": "Universal (Sabbacittasādhāraṇa — present in all 89/121 cittas)",
                "es": "Universal (Sabbacittasādhāraṇa — presente en todos los 89/121 cittas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Perceber as qualidades ou marcas distintivas do objeto (sañjānana-lakkhaṇa).",
                    "en": "Perceiving the qualities or distinctive marks of the object (sañjānana-lakkhaṇa).",
                    "es": "Percibir las cualidades o marcas distintivas del objeto (sañjānana-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Fazer um sinal ou marca como condição para perceber novamente que 'isto é o mesmo' (paccabhiññāṇa-nimittakaraṇa-rasa), ou reconhecer o que foi percebido antes.",
                    "en": "Making a sign as a condition for perceiving again that 'this is the same' (paccabhiññāṇa-nimittakaraṇa-rasa), or recognizing what has been previously perceived.",
                    "es": "Hacer una señal como condición para percibir nuevamente que 'esto es lo mismo' (paccabhiññāṇa-nimittakaraṇa-rasa), o reconocer lo percibido anteriormente."
                },
                "paccupatthana": {
                    "pt": "Interpretar ou apreender o objeto (abhinivesa-paccupaṭṭhāna) por meio das características ou sinais que foram captados.",
                    "en": "Interpreting the object (abhinivesa-paccupaṭṭhāna) by way of the features that had been apprehended.",
                    "es": "Interpretar el objeto (abhinivesa-paccupaṭṭhāna) por medio de los rasgos aprehendidos."
                },
                "padatthana": {
                    "pt": "O objeto tal como aparece no momento (yathāupaṭṭhitavisaya-padaṭṭhāna).",
                    "en": "The object as it appears at the moment (yathāupaṭṭhitavisaya-padaṭṭhāna).",
                    "es": "El objeto tal como aparece en el momento (yathāupaṭṭhitavisaya-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Os Comentários comparam saññā ao reconhecimento que um carpinteiro faz de diferentes peças de madeira pelas marcas que ele próprio gravou em cada uma. Na famosa símile das três pessoas diante de moedas (Vism. XIV, 130): saññā é como uma criança que vê apenas a cor e o formato vistoso da moeda (sem saber seu valor nem se é verdadeira ou falsa); citta (viññāṇa) é como um aldeão que sabe que a moeda compra coisas, mas não distingue a falsa da verdadeira; e paññā (sabedoria) é como o cambista perito que examina a moeda na palma da mão e conhece sua natureza intrínseca real.",
                "en": "The Commentaries compare saññā to a carpenter's recognition of kinds of wood by the mark he has made on each. In the classic Visuddhimagga simile of the coins (Vism. XIV, 130): saññā is like a child who merely notes the coin's color and shape; viññāṇa (citta) is like a villager who knows it serves as currency; and paññā (wisdom) is like a money-changer who knows its exact composition and intrinsic nature.",
                "es": "Los Comentarios comparan saññā al reconocimiento que hace un carpintero de distintas maderas por la marca que grabó en cada una. Es la base de la memoria y del reconocimiento conceptual."
            },
            "bodhiRef": "CMA II, §2 (Guide, p. 79)"
        },
        "seeAlso": ["citta", "paññā", "sati", "khandha"]
    },

    "cetanā": {
        "meaning": {
            "pt": "Volição; intenção; o fator mental universal responsável pela atualização de um objetivo, organizando e coordenando todos os fatores mentais associados em sua atuação sobre o objeto; é o fator determinante do kamma.",
            "en": "Volition; intention; the universal mental factor concerned with the actualization of a goal, organizing and coordinating its associated mental factors in acting upon the object; the principal factor in generating kamma.",
            "es": "Volición; intención; el factor mental universal encargado de la actualización de un fin, organizando y coordinando los factores mentales asociados al actuar sobre el objeto; el factor principal del kamma."
        },
        "grammar": "fem. (de √cit + anā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (derivado da raiz √cit 'intencionar, coordenar')",
            "en": "Feminine noun (derived from root √cit 'to intend, coordinate')",
            "es": "Sustantivo femenino (derivado de la raíz √cit 'intencionar, coordinar')"
        },
        "root": "√cit (pensar / intencionar / coordenar) + anā",
        "etymology": {
            "pt": "Derivado da mesma raiz verbal que citta (√cit), porém no sentido conativo de coordenar, dirigir e reunir (cetayati / abhisaṅkharoti) os estados associados para realizar uma tarefa.",
            "en": "Derived from the same root as citta (√cit), here in the conative sense of coordinating, marshalling, and directing (cetayati / abhisaṅkharoti) the associated states towards a goal.",
            "es": "Derivado de la misma raíz que citta (√cit), aquí en el sentido conativo de coordinar y dirigir (cetayati) los estados asociados hacia una meta."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal (Cetasika #4 de 52) & Chefe de Saṅkhārakkhandha",
                "en": "Ultimate Reality — Universal Mental Factor (Cetasika #4 of 52) & Chief of Saṅkhārakkhandha",
                "es": "Realidad Última — Factor Mental Universal (Cetasika #4 de 52) y Jefe de Saṅkhārakkhandha"
            },
            "category": {
                "pt": "Universal (Sabbacittasādhāraṇa); constitui a Condição de Kamma Síncrona e Assíncrona (Sahajāta & Nānakkhaṇika Kammapaccaya)",
                "en": "Universal (Sabbacittasādhāraṇa); constitutes Conascent and Asynchronous Kamma Condition (Sahajāta & Nānakkhaṇika Kammapaccaya)",
                "es": "Universal (Sabbacittasādhāraṇa); constituye la Condición de Kamma Conascente y Asincrónica (Kammapaccaya)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "O estado de querer / intencionar ou coordenar (cetayita-lakkhaṇa).",
                    "en": "The state of willing or coordinating (cetayita-lakkhaṇa).",
                    "es": "El estado de querer, intencionar o coordinar (cetayita-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Acumular ou esforçar-se (āyūhana-rasa — especialmente acumular kamma nos cittas kusala e akusala).",
                    "en": "To accumulate or strive (āyūhana-rasa — especially accumulating kamma in wholesome and unwholesome cittas).",
                    "es": "Acumular o esforzarse (āyūhana-rasa — especialmente acumular kamma en los cittas kusala y akusala)."
                },
                "paccupatthana": {
                    "pt": "Coordenação e direção (saṃvidahana-paccupaṭṭhāna) dos estados associados.",
                    "en": "Coordination and directing (saṃvidahana-paccupaṭṭhāna) of the associated states.",
                    "es": "Coordinación y dirección (saṃvidahana-paccupaṭṭhāna) de los estados asociados."
                },
                "padatthana": {
                    "pt": "Os estados mentais associados (sampayuttadhamma-padaṭṭhāna).",
                    "en": "The associated mental states (sampayuttadhamma-padaṭṭhāna).",
                    "es": "Los estados mentales asociados (sampayuttadhamma-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Comparado por Bhikkhu Bodhi (CMA II, §2, p. 79) ao aluno-chefe ou capataz que recita sua própria lição e simultaneamente faz todos os outros alunos recitarem as suas. O Buddha declarou: 'Cetanāhaṃ, bhikkhave, kammaṃ vadāmi' ('É a volição, monges, que eu chamo de kamma' — AN 6.63). Enquanto nos cittas vipāka e kiriya a cetanā apenas coordena os fatores co-surgentes (sahajāta-kammapaccaya), nos 21/37 cittas kusala e 12 akusala ela também deposita a força latente que produzirá vipāka no futuro (nānakkhaṇika-kammapaccaya, Cap. VIII, §14).",
                "en": "Compared by Bhikkhu Bodhi (CMA II, §2, p. 79) to a chief pupil who recites his own lesson and also makes the other pupils recite theirs. The Buddha declared: 'Cetanāhaṃ, bhikkhave, kammaṃ vadāmi' ('It is volition, monks, that I call kamma' — AN 6.63). While in vipāka and kiriya cittas cetanā merely coordinates co-arisen states (sahajāta-kammapaccaya), in wholesome and unwholesome cittas it also deposits the kammic potency that produces future vipāka (nānakkhaṇika-kammapaccaya, Ch. VIII, §14).",
                "es": "Comparado por Bhikkhu Bodhi (CMA II, §2, p. 79) al alumno principal que recita su propia lección y hace que los demás reciten las suyas. Es el factor definitorio del kamma ('Cetanāhaṃ, bhikkhave, kammaṃ vadāmi')."
            },
            "bodhiRef": "CMA II, §2 (Guide, p. 79); V, §18 (p. 200); VIII, §14 (p. 308)"
        },
        "seeAlso": ["kamma", "saṅkhāra", "citta", "kammapaccaya"]
    },

    "ekaggatā": {
        "meaning": {
            "pt": "Unidirecionalidade da mente; concentração (samādhi); o fator mental universal que unifica e fixa a consciência e seus concomitantes em um único objeto.",
            "en": "One-pointedness of mind; concentration (samādhi); the universal mental factor that unifies and fixes consciousness and its concomitants on a single object.",
            "es": "Unidireccionalidad de la mente; concentración (samādhi); el factor mental universal que unifica y fija la conciencia y sus concomitantes en un único objeto."
        },
        "grammar": "fem. (eka + agga + tā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino abstrato (composto Bahubbīhi + sufixo abstrato -tā)",
            "en": "Abstract feminine noun (Bahubbīhi compound + abstract suffix -tā)",
            "es": "Sustantivo femenino abstracto (compuesto Bahubbīhi + sufijo abstracto -tā)"
        },
        "root": "eka (um) + agga (ponto / ápice) + tā (estado de)",
        "samasa": {
            "type": {
                "pt": "Composto Relativo Abstrato (Bahubbīhi + Taddhita -tā)",
                "en": "Abstract Relative Compound (Bahubbīhi + Taddhita -tā)",
                "es": "Compuesto Relativo Abstracto (Bahubbīhi + Taddhita -tā)"
            },
            "viggaha": "eko aggo (ārammaṇaṃ) assā'ti ekaggaṃ; ekaggassa bhāvo = ekaggatā",
            "literal": {
                "pt": "O estado (-tā) de possuir um único (eka) ponto focal ou objeto (agga).",
                "en": "The state (-tā) of having a single (eka) focal point or object (agga).",
                "es": "El estado (-tā) de poseer un único (eka) punto focal u objeto (agga)."
            },
            "parts": [
                {"part": "eka", "gloss": {"pt": "um, único", "en": "one, single", "es": "uno, único"}},
                {"part": "agga", "gloss": {"pt": "ponto, ápice, objeto focal", "en": "point, peak, focal object", "es": "punto, ápice, objeto focal"}},
                {"part": "-tā", "gloss": {"pt": "estado de, qualidade (-dade)", "en": "state of (-ness)", "es": "estado de (-dad)"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal (Cetasika #5 de 52)",
                "en": "Ultimate Reality — Universal Mental Factor (Cetasika #5 of 52)",
                "es": "Realidad Última — Factor Mental Universal (Cetasika #5 de 52)"
            },
            "category": {
                "pt": "Universal (Sabbacittasādhāraṇa); 5º Fator de Jhāna; Faculdade e Poder da Concentração (Samādhindriya / Samādhibala); Sammāsamādhi",
                "en": "Universal (Sabbacittasādhāraṇa); 5th Jhāna Factor; Faculty and Power of Concentration (Samādhindriya / Samādhibala); Sammāsamādhi",
                "es": "Universal (Sabbacittasādhāraṇa); 5º Factor de Jhāna; Facultad y Poder de la Concentración (Samādhindriya); Sammāsamādhi"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Não-dispersão ou não-distração (avikkhepa-lakkhaṇa).",
                    "en": "Non-wandering or non-distraction (avikkhepa-lakkhaṇa).",
                    "es": "No dispersión o no distracción (avikkhepa-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Conglomerar ou unificar os estados mentais associados (sahajātānaṃ sampiṇḍana-rasa), como a água que une o pó de banho numa pasta coesa.",
                    "en": "To conglomerate or unite the associated states (sahajātānaṃ sampiṇḍana-rasa), as water binds bath-powder into a cohesive paste.",
                    "es": "Conglomerar o unificar los estados asociados (sahajātānaṃ sampiṇḍana-rasa), como el agua que une el polvo en una pasta cohesiva."
                },
                "paccupatthana": {
                    "pt": "Paz ou serenidade mental (upasama-paccupaṭṭhāna).",
                    "en": "Peace or mental stillness (upasama-paccupaṭṭhāna).",
                    "es": "Paz o quietud mental (upasama-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "A felicidade, especialmente na concentração profunda (sukha-padaṭṭhāna: 'sukhino cittaṃ samādhiyati').",
                    "en": "Happiness, especially in deep concentration (sukha-padaṭṭhāna: 'the mind of one who is happy becomes concentrated').",
                    "es": "La felicidad, especialmente en la concentración profunda (sukha-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Embora ekaggatā alcance proeminência nos jhānas (onde é o único fator de jhāna presente desde o 1º jhāna até a 4ª absorção imaterial), o Abhidhamma ensina que o germe dessa capacidade de fixar a mente em um objeto por vez está presente em todos os 89 cittas, até mesmo no citta associado à dúvida (onde é meramente a estabilidade estática momentânea, ṭhitimatta).",
                "en": "Although ekaggatā comes to prominence in the jhānas (where it is the only jhāna factor remaining from the 1st jhāna all the way through the 4th immaterial attainment), the Abhidhamma teaches that the germ of this capacity to fix the mind on one object at a time is present in all 89 cittas, even in doubt-accompanied citta (where it is mere momentary stasis, ṭhitimatta).",
                "es": "Aunque ekaggatā alcanza prominencia en los jhānas (donde permanece desde el 1º jhāna hasta el 4º logro inmaterial), el Abhidhamma enseña que el germen de esta fijación mental está presente en todos los 89 cittas."
            },
            "bodhiRef": "CMA I, §§18–20 (p. 57); II, §2 (Guide, pp. 79–80)"
        },
        "seeAlso": ["samādhi", "jhāna", "vitakka", "vicāra", "pīti", "sukha"]
    },

    "jīvitindriya": {
        "meaning": {
            "pt": "Faculdade vital; vitalidade. Existem duas faculdades vitais: (1) a faculdade vital mental (nāma-jīvitindriya, um dos 7 cetasikas universais) e (2) a faculdade vital física (rūpa-jīvitindriya, um dos 28 fenômenos materiais, que mantém a matéria nascida do kamma).",
            "en": "Life faculty; vitality. There are two kinds of life faculty: (1) mental life faculty (nāma-jīvitindriya, one of the 7 universal cetasikas) and (2) physical life faculty (rūpa-jīvitindriya, one of the 28 material phenomena, maintaining kamma-born matter).",
            "es": "Facultad vital; vitalidad. Existen dos facultades vitales: (1) la facultad vital mental (nāma-jīvitindriya, uno de los 7 cetasikas universales) y (2) la facultad vital física (rūpa-jīvitindriya, uno de los 28 fenómenos materiales)."
        },
        "grammar": "nt. (jīvita + indriya)",
        "grammarLocalized": {
            "pt": "Substantivo neutro composto (Kammadhāraya: jīvita + indriya)",
            "en": "Compound neuter noun (Kammadhāraya: jīvita + indriya)",
            "es": "Sustantivo neutro compuesto (Kammadhāraya: jīvita + indriya)"
        },
        "root": "√jīv (viver) + ita + indriya (faculdade governante)",
        "samasa": {
            "type": {
                "pt": "Composto Determinativo Descritivo (Kammadhāraya)",
                "en": "Descriptive Determinative Compound (Kammadhāraya)",
                "es": "Compuesto Determinativo Descriptivo (Kammadhāraya)"
            },
            "viggaha": "jīvitam eva indriyaṃ = jīvitindriyaṃ",
            "literal": {
                "pt": "A vitalidade (jīvita) que exerce domínio soberano como faculdade (indriya).",
                "en": "Vitality (jīvita) which exercises governing predominance as a faculty (indriya).",
                "es": "La vitalidad (jīvita) que ejerce dominio gobernante como facultad (indriya)."
            },
            "parts": [
                {"part": "jīvita", "gloss": {"pt": "vida, vitalidade (√jīv + ita)", "en": "life, vitality (√jīv + ita)", "es": "vida, vitalidad (√jīv + ita)"}},
                {"part": "indriya", "gloss": {"pt": "faculdade governante", "en": "governing faculty", "es": "facultad gobernante"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Dupla Realidade Última: Cetasika Universal (#6 de 52) e Rūpa Concreta (#17 de 28)",
                "en": "Dual Ultimate Reality: Universal Cetasika (#6 of 52) and Concrete Rūpa (#17 of 28)",
                "es": "Doble Realidad Última: Cetasika Universal (#6 de 52) y Rūpa Concreta (#17 de 28)"
            },
            "category": {
                "pt": "Nāma-jīvitindriya (vitaliza citta e cetasikas em todos os 89 cittas) & Rūpa-jīvitindriya (vitaliza os grupos materiais nascidos do kamma)",
                "en": "Nāma-jīvitindriya (vitalizes citta and cetasikas in all 89 cittas) & Rūpa-jīvitindriya (vitalizes kamma-born material groups)",
                "es": "Nāma-jīvitindriya (vitaliza citta y cetasikas en los 89 cittas) y Rūpa-jīvitindriya (vitaliza los grupos materiales nacidos del kamma)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Manter ou proteger os estados co-surgentes (sahajāta-dhamma-anupālana-lakkhaṇa).",
                    "en": "Maintaining or guarding the coexistent states (sahajāta-dhamma-anupālana-lakkhaṇa).",
                    "es": "Mantener o proteger los estados coexistentes (sahajāta-dhamma-anupālana-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Fazer com que os estados co-surgentes ocorram e prossigam até sua cessação (pavattana-rasa).",
                    "en": "Making the coexistent states occur and proceed (pavattana-rasa).",
                    "es": "Hacer que los estados coexistentes ocurran y prosigan (pavattana-rasa)."
                },
                "paccupatthana": {
                    "pt": "O estabelecimento da presença desses estados (ṭhapanā-paccupaṭṭhāna).",
                    "en": "The establishing of the presence of those states (ṭhapanā-paccupaṭṭhāna).",
                    "es": "El establecimiento de la presencia de dichos estados (ṭhapanā-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Os estados mentais (ou os 4 grandes elementos materiais) que devem ser mantidos (yāpayitabbadhamma-padaṭṭhāna).",
                    "en": "The mental states (or the 4 great essentials, for physical life faculty) to be maintained (yāpayitabbadhamma-padaṭṭhāna).",
                    "es": "Los estados mentales (o los 4 grandes elementos) que han de ser mantenidos (yāpayitabbadhamma-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Assim como a água mantém vivas as flores de lótus, a faculdade vital mantém vivos os estados co-surgentes durante seu momento de existência, embora não possa prolongá-los além do submomento da dissolução (bhaṅga).",
                "en": "Just as water sustains lotus flowers, the life faculty maintains its coexistent states during their moment of presence, though it cannot prolong them past the sub-moment of dissolution (bhaṅga).",
                "es": "Así como el agua mantiene vivas las flores de loto, la facultad vital mantiene sus estados coexistentes durante el momento de su presencia."
            },
            "bodhiRef": "CMA II, §2 (Guide, p. 80); VI, §3 (p. 238); VII, §18 (p. 275)"
        },
        "seeAlso": ["indriya", "sabbacittasādhāraṇa", "rūpa"]
    },

    "manasikāra": {
        "meaning": {
            "pt": "Atenção; orientação mental; o fator mental universal que conduz e atrela a consciência e os demais fatores mentais ao objeto, tornando-o presente à mente.",
            "en": "Attention; mental advertence; the universal mental factor that conducts and yokes consciousness and its associated factors to the object, making it present to consciousness.",
            "es": "Atención; advertencia mental; el factor mental universal que conduce y une la conciencia y sus factores asociados hacia el objeto, haciéndolo presente a la mente."
        },
        "grammar": "masc. (manasi + kāra)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (composto Alutta Sattamī-Tappurisa: manasi [loc.] + kāra)",
            "en": "Masculine noun (Alutta Sattamī-Tappurisa compound: manasi [loc.] + kāra)",
            "es": "Sustantivo masculino (compuesto Alutta Sattamī-Tappurisa: manasi [loc.] + kāra)"
        },
        "root": "manasi (na mente, loc. de manas) + √kar (fazer) + *a",
        "etymology": {
            "pt": "Composto locativo sem elisão da desinência (alutta-samāsa): manasi (locativo singular de manas = 'na mente') + kāra ('fazer, pôr', de √kar). Literalmente 'fazer presente na mente'.",
            "en": "Unelided locative compound (alutta-samāsa): manasi (locative singular of manas = 'in the mind') + kāra ('making, placing', from √kar). Literally 'making in the mind'.",
            "es": "Compuesto locativo sin elisión (alutta-samāsa): manasi (locativo singular de manas = 'en la mente') + kāra ('hacer, poner', de √kar). Literalmente 'hacer en la mente'."
        },
        "samasa": {
            "type": {
                "pt": "Composto Locativo com Caso Preservado (Alutta Sattamī-Tappurisa)",
                "en": "Locative Compound with Preserved Case Ending (Alutta Sattamī-Tappurisa)",
                "es": "Compuesto Locativo con Desinencia Conservada (Alutta Sattamī-Tappurisa)"
            },
            "viggaha": "manasi (citte) ārammaṇassa kāro = manasikāro",
            "literal": {
                "pt": "O ato de colocar ou fazer (kāra) o objeto presente na mente (manasi).",
                "en": "The act of making or placing (kāra) the object in the mind (manasi).",
                "es": "El acto de hacer o colocar (kāra) el objeto en la mente (manasi)."
            },
            "parts": [
                {"part": "manasi", "gloss": {"pt": "na mente (locativo de manas)", "en": "in the mind (locative of manas)", "es": "en la mente (locativo de manas)"}},
                {"part": "kāra", "gloss": {"pt": "ato de fazer / pôr (√kar + *a)", "en": "act of making / placing (√kar + *a)", "es": "acto de hacer / poner (√kar + *a)"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal (Cetasika #7 de 52)",
                "en": "Ultimate Reality — Universal Mental Factor (Cetasika #7 of 52)",
                "es": "Realidad Última — Factor Mental Universal (Cetasika #7 de 52)"
            },
            "category": {
                "pt": "Universal (Sabbacittasādhāraṇa — presente em todos os 89/121 cittas)",
                "en": "Universal (Sabbacittasādhāraṇa — present in all 89/121 cittas)",
                "es": "Universal (Sabbacittasādhāraṇa — presente en todos los 89/121 cittas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Conduzir ou guiar (sāraṇa-lakkhaṇa) os estados mentais associados em direção ao objeto.",
                    "en": "Conducting or driving (sāraṇa-lakkhaṇa) the associated mental states towards the object.",
                    "es": "Conducir o dirigir (sāraṇa-lakkhaṇa) los estados mentales asociados hacia el objeto."
                },
                "rasa": {
                    "pt": "Atrelar ou jungir (sampayuttānaṃ ārammaṇe yojana-rasa) os estados associados ao objeto.",
                    "en": "To yoke or join (sampayuttānaṃ ārammaṇe yojana-rasa) the associated states to the object.",
                    "es": "Uncir o unir (sampayuttānaṃ ārammaṇe yojana-rasa) los estados asociados al objeto."
                },
                "paccupatthana": {
                    "pt": "O estar face a face ou confrontado com o objeto (ārammaṇābhimukhabhāva-paccupaṭṭhāna).",
                    "en": "Confrontation with an object (ārammaṇābhimukhabhāva-paccupaṭṭhāna).",
                    "es": "La confrontación cara a cara con el objeto (ārammaṇābhimukhabhāva-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O próprio objeto (ārammaṇa-padaṭṭhāna).",
                    "en": "The object itself (ārammaṇa-padaṭṭhāna).",
                    "es": "El propio objeto (ārammaṇa-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Como explica Bhikkhu Bodhi (CMA II, §2, p. 80), manasikāra é como o leme de um navio que o direciona ao destino, ou como o cocheiro que conduz os cavalos bem treinados (os fatores mentais) até o objeto. Deve ser cuidadosamente distinguido de vitakka: enquanto manasikāra (presente em todos os 89 cittas) volta os concomitantes para o objeto, vitakka (presente apenas em 55 cittas) lança-os e aplica-os sobre o objeto. A distinção ética entre yoniso manasikāra (atenção sábia, que vê a impermanência, dukkha e anattā) e ayoniso manasikāra (atenção insensata) é a causa próxima que decide o surgimento de estados kusala ou akusala.",
                "en": "As Bhikkhu Bodhi explains (CMA II, §2, p. 80), manasikāra is like the rudder of a ship directing it to its destination, or a charioteer sending well-trained horses towards the object. It must be distinguished from vitakka: while manasikāra (present in all 89 cittas) turns its concomitants towards the object, vitakka (present in 55 cittas) applies them onto the object. The contrast between yoniso manasikāra (wise attention) and ayoniso manasikāra (unwise attention) is the proximate cause deciding whether kusala or akusala arises.",
                "es": "Como explica Bhikkhu Bodhi (CMA II, §2, p. 80), manasikāra es como el timón de un barco o un auriga que dirige los caballos hacia el objeto. Mientras manasikāra (en los 89 cittas) vuelve la mente hacia el objeto, vitakka (en 55 cittas) la deposita sobre él."
            },
            "bodhiRef": "CMA II, §2 (Guide, p. 80)"
        },
        "seeAlso": ["vitakka", "āvajjana", "sabbacittasādhāraṇa", "paññā", "moha"]
    },

    # ── 6 OCASIONAIS (PAKIṆṆAKA) ──────────────────────────────────────────────
    "pakiṇṇaka": {
        "meaning": {
            "pt": "Ocasional; particular; miscelâneo; os 6 fatores mentais eticamente variáveis (vitakka, vicāra, adhimokkha, viriya, pīti, chanda) que não estão presentes em todas as consciências, mas apenas em tipos específicos. No Cap. III, significa também 'categorias diversas/miscelâneas'.",
            "en": "Occasional; particular; miscellaneous; the 6 ethically variable mental factors (vitakka, vicāra, adhimokkha, viriya, pīti, chanda) found only in particular types of consciousness, not in all. In Ch. III, it also means 'miscellaneous categories'.",
            "es": "Ocasional; particular; misceláneo; los 6 factores mentales éticamente variables (vitakka, vicāra, adhimokkha, viriya, pīti, chanda) que se encuentran solo en tipos particulares de conciencia, no en todas."
        },
        "grammar": "adj./masc. (pa + √kir + na + ka)",
        "grammarLocalized": {
            "pt": "Adjetivo / Substantivo masculino (particípio passado de pakirati 'espalhar, distribuir' + -ka)",
            "en": "Adjective / Masculine noun (past participle of pakirati 'to scatter, distribute' + -ka)",
            "es": "Adjetivo / Sustantivo masculino (participio pasado de pakirati 'esparcir, distribuir' + -ka)"
        },
        "root": "pa + √kir (espalhar / distribuir) + na + ka",
        "abhidhamma": {
            "ontology": {
                "pt": "Subgrupo dos 6 Cetasikas Ocasionais (Cetasika #8–#13 de 52)",
                "en": "Subgroup of the 6 Occasional Cetasikas (Cetasika #8–#13 of 52)",
                "es": "Subgrupo de los 6 Cetasikas Ocasionales (Cetasika #8–#13 de 52)"
            },
            "category": {
                "pt": "6 Pakiṇṇaka: Vitakka (55 cittas), Vicāra (66 cittas), Adhimokkha (78 cittas), Viriya (73 cittas), Pīti (51 cittas), Chanda (69 cittas)",
                "en": "6 Pakiṇṇaka: Vitakka (55 cittas), Vicāra (66 cittas), Adhimokkha (78 cittas), Viriya (73 cittas), Pīti (51 cittas), Chanda (69 cittas)",
                "es": "6 Pakiṇṇaka: Vitakka (55 cittas), Vicāra (66 cittas), Adhimokkha (78 cittas), Viriya (73 cittas), Pīti (51 cittas), Chanda (69 cittas)"
            },
            "philosophy": {
                "pt": "Como os 7 universais, os 6 pakiṇṇaka são eticamente variáveis (aññasamāna), porém aparecem de modo 'espalhado' ou seletivo conforme a complexidade do ato mental. Nenhum deles surge nas 10 consciências sensoriais puras (dvipañcaviññāṇa).",
                "en": "Like the 7 universals, the 6 pakiṇṇaka are ethically variable (aññasamāna), but they are 'scattered' selectively across cittas depending on cognitive complexity. None of them arise in the 10 bare sense-consciousnesses (dvipañcaviññāṇa).",
                "es": "Al igual que los 7 universales, los 6 pakiṇṇaka son éticamente variables (aññasamāna), pero se distribuyen selectivamente según la complejidad del acto cognitivo. Ninguno surge en los 10 dvipañcaviññāṇa."
            },
            "bodhiRef": "CMA II, §3 & §§11–12 (Guide, pp. 80–82, 95–96)"
        },
        "seeAlso": ["aññasamāna", "vitakka", "vicāra", "adhimokkha", "viriya", "pīti", "chanda"]
    },

    "vitakka": {
        "meaning": {
            "pt": "Aplicação inicial; pensamento aplicado; o fator mental ocasional que eleva e pousa a mente sobre o objeto; 1º fator de jhāna e, quando supramundano ou salutar, intenção correta (sammāsaṅkappa).",
            "en": "Initial application; applied thought; the occasional mental factor that lifts and mounts the mind onto the object; 1st jhāna factor and, when wholesome/supramundane, right intention (sammāsaṅkappa).",
            "es": "Aplicación inicial; pensamiento aplicado; el factor mental ocasional que eleva y deposita la mente sobre el objeto; 1º factor de jhāna y, cuando es saludable/supramundano, intención correcta (sammāsaṅkappa)."
        },
        "grammar": "masc. (vi + √takk + a)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (vi + √takk 'pensar, direcionar')",
            "en": "Masculine noun (vi + √takk 'to think, direct onto')",
            "es": "Sustantivo masculino (vi + √takk 'pensar, dirigir hacia')"
        },
        "root": "vi + √takk (direcionar o pensamento) + a",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Ocasional (Cetasika #8 de 52)",
                "en": "Ultimate Reality — Occasional Mental Factor (Cetasika #8 of 52)",
                "es": "Realidad Última — Factor Mental Ocasional (Cetasika #8 de 52)"
            },
            "category": {
                "pt": "Ocasional (Pakiṇṇaka — presente em 55 de 89 cittas); 1º Fator de Jhāna; Fator de Caminho (Sammāsaṅkappa / Micchāsaṅkappa)",
                "en": "Occasional (Pakiṇṇaka — present in 55 of 89 cittas); 1st Jhāna Factor; Path Factor (Sammāsaṅkappa / Micchāsaṅkappa)",
                "es": "Ocasional (Pakiṇṇaka — presente en 55 de 89 cittas); 1º Factor de Jhāna; Factor de Camino (Sammāsaṅkappa / Micchāsaṅkappa)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Direcionar ou assentar a mente sobre o objeto (ārammaṇe cittassa abhiniropana-lakkhaṇa), como um favorito do rei que conduz um aldeão à presença real.",
                    "en": "Directing or mounting the mind onto the object (ārammaṇe cittassa abhiniropana-lakkhaṇa), like a king's favorite conducting a villager into the palace.",
                    "es": "Dirigir o asentar la mente sobre el objeto (ārammaṇe cittassa abhiniropana-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Tocar e bater repetidamente no objeto (āhanana-pariyāhanana-rasa).",
                    "en": "To strike at and thresh the object all around (āhanana-pariyāhanana-rasa).",
                    "es": "Golpear e incidir sobre el objeto (āhanana-pariyāhanana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Conduzir a mente até o objeto (ānayana-paccupaṭṭhāna).",
                    "en": "The leading of the mind onto an object (ānayana-paccupaṭṭhāna).",
                    "es": "La conducción de la mente hacia el objeto (ānayana-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O objeto (ārammaṇa-padaṭṭhāna).",
                    "en": "The object (ārammaṇa-padaṭṭhāna).",
                    "es": "El objeto (ārammaṇa-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Nas símiles clássicas citadas por Bhikkhu Bodhi (CMA I, §§18–20, p. 56): vitakka é como o primeiro golpe de um badalo contra um sino, enquanto vicāra é o ressoar contínuo do sino; vitakka é como uma ave que bate as asas para alçar voo, enquanto vicāra é a ave planando com as asas estendidas; vitakka é como uma abelha que mergulha em direção ao lótus, enquanto vicāra é a abelha zumbindo sobre a flor. Vitakka está ausente nas 10 consciências sensoriais (dvipañcaviññāṇa, por serem rudimentares demais) e a partir do 2º jhāna (por já ter cumprido sua função de levar a mente à absorção). Combate diretamente o obstáculo do torpor e languidez (thīna-middha).",
                "en": "In the classic similes cited by Bhikkhu Bodhi (CMA I, §§18–20, p. 56): vitakka is like the striking of a bell, while vicāra is its ringing; vitakka is like a bird spreading its wings to take flight, while vicāra is the bird gliding with outstretched wings; vitakka is like a bee diving towards a lotus, while vicāra is the bee hovering over it. Vitakka is absent from the 10 sense-consciousnesses (dvipañcaviññāṇa) and from the 2nd jhāna upwards. It directly counters sloth and torpor (thīna-middha).",
                "es": "En los símiles clásicos citados por Bhikkhu Bodhi (CMA I, §§18–20, p. 56): vitakka es como el golpe inicial de una campana y vicāra como su resonancia; vitakka es como el batir de alas al despegar y vicāra como el planear. Está ausente en los 10 dvipañcaviññāṇa y a partir del 2º jhāna."
            },
            "bodhiRef": "CMA I, §§18–20 (Guide, pp. 56–57); II, §3 & §11 (pp. 80–81, 95)"
        },
        "seeAlso": ["vicāra", "manasikāra", "jhāna", "sammāsaṅkappa", "thīna"]
    },

    "vicāra": {
        "meaning": {
            "pt": "Aplicação sustentada; pensamento sustentado; exame contínuo; o fator mental ocasional que mantém a mente ancorada sobre o objeto, examinando-o continuamente; 2º fator de jhāna.",
            "en": "Sustained application; sustained thought; continued examination; the occasional mental factor that keeps the mind anchored on the object, examining it continuously; 2nd jhāna factor.",
            "es": "Aplicación sostenida; pensamiento sostenido; examen continuo; el factor mental ocasional que mantiene la mente anclada en el objeto, examinándolo continuamente; 2º factor de jhāna."
        },
        "grammar": "masc. (vi + √car + *a)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (vi [ao redor] + √car [mover-se, percorrer] + *a)",
            "en": "Masculine noun (vi [around/about] + √car [to move, roam] + *a)",
            "es": "Sustantivo masculino (vi [alrededor] + √car [moverse, recorrer] + *a)"
        },
        "root": "vi (ao redor) + √car (mover-se / percorrer) + *a",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Ocasional (Cetasika #9 de 52)",
                "en": "Ultimate Reality — Occasional Mental Factor (Cetasika #9 of 52)",
                "es": "Realidad Última — Factor Mental Ocasional (Cetasika #9 de 52)"
            },
            "category": {
                "pt": "Ocasional (Pakiṇṇaka — presente em 66 de 89 cittas, ou 98 de 121); 2º Fator de Jhāna",
                "en": "Occasional (Pakiṇṇaka — present in 66 of 89 cittas, or 98 of 121); 2nd Jhāna Factor",
                "es": "Ocasional (Pakiṇṇaka — presente en 66 de 89 cittas, o 98 de 121); 2º Factor de Jhāna"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Acariciar ou exercer pressão contínua sobre o objeto (ārammaṇ'ānumajjana-lakkhaṇa), no sentido de examiná-lo repetidamente.",
                    "en": "Continued stroking or pressure on the object (ārammaṇ'ānumajjana-lakkhaṇa), in the sense of examining it.",
                    "es": "Acariciar o ejercer presión continua sobre el objeto (ārammaṇ'ānumajjana-lakkhaṇa), examinándolo."
                },
                "rasa": {
                    "pt": "Manter os fenômenos mentais associados continuamente engajados no objeto (tattha sahajātānaṃ anuppabandhana-rasa).",
                    "en": "Sustained application or keeping the associated mental phenomena engaged on the object (tattha sahajātānaṃ anuppabandhana-rasa).",
                    "es": "Mantener los fenómenos mentales asociados continuamente vinculados al objeto (anuppabandhana-rasa)."
                },
                "paccupatthana": {
                    "pt": "O ancoramento da mente no objeto (cittassa anuppabandhatā-paccupaṭṭhāna).",
                    "en": "The anchoring of consciousness and its concomitants on the object (cittassa anuppabandhatā-paccupaṭṭhāna).",
                    "es": "El anclaje de la conciencia en el objeto (cittassa anuppabandhatā-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O objeto (ārammaṇa-padaṭṭhāna).",
                    "en": "The object (ārammaṇa-padaṭṭhāna).",
                    "es": "El objeto (ārammaṇa-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Enquanto vitakka é como a mão que segura firmemente um prato de metal manchado, vicāra é como a outra mão que o esfrega continuamente com um pano para limpá-lo (CMA I, p. 56). No método quíntuplo do Abhidhamma, vicāra permanece presente no 2º jhāna (após o abandono de vitakka) e é superado no 3º jhāna. Combate diretamente o obstáculo da dúvida (vicikicchā).",
                "en": "While vitakka is like the hand gripping a tarnished metal dish, vicāra is like the other hand wiping it back and forth to polish it (CMA I, p. 56). In the fivefold Abhidhamma jhāna scheme, vicāra remains present in the 2nd jhāna (after vitakka is abandoned) and is transcended in the 3rd jhāna. It directly counters the hindrance of doubt (vicikicchā).",
                "es": "Mientras vitakka es como la mano que sujeta firmemente un plato de metal, vicāra es como la otra mano que lo frota continuamente para pulirlo (CMA I, p. 56). Permanece en el 2º jhāna y contrarresta directamente la duda (vicikicchā)."
            },
            "bodhiRef": "CMA I, §§18–20 (Guide, pp. 56–57); II, §3 & §11 (pp. 81, 95)"
        },
        "seeAlso": ["vitakka", "jhāna", "vicikicchā", "pakiṇṇaka"]
    },

    "adhimokkha": {
        "meaning": {
            "pt": "Decisão; resolução; convicção; o fator mental ocasional que liberta a mente da hesitação sobre o objeto, decidindo com firmeza ('isto é justamente assim').",
            "en": "Decision; resolution; conviction; the occasional mental factor that releases the mind onto the object without wavering, deciding firmly ('this is just so').",
            "es": "Decisión; resolución; convicción; el factor mental ocasional que libera la mente hacia el objeto sin vacilación, decidiendo con firmeza."
        },
        "grammar": "masc. (adhi + √muc + a)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (adhi [sobre] + √muc [soltar, lançar] + a)",
            "en": "Masculine noun (adhi [onto] + √muc [to release] + a)",
            "es": "Sustantivo masculino (adhi [sobre] + √muc [soltar, liberar] + a)"
        },
        "root": "adhi (sobre) + √muc (soltar / liberar) + a",
        "etymology": {
            "pt": "De adhi- (sobre, em direção a) + √muc ('soltar, liberar'): significa literalmente 'soltar a mente sobre o objeto' sem vacilar.",
            "en": "From adhi- (onto) + √muc ('to release, free'): literally 'the releasing of the mind onto the object' without hesitation.",
            "es": "De adhi- (sobre) + √muc ('soltar, liberar'): literalmente 'liberar la mente sobre el objeto' sin vacilación."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Ocasional (Cetasika #10 de 52)",
                "en": "Ultimate Reality — Occasional Mental Factor (Cetasika #10 of 52)",
                "es": "Realidad Última — Factor Mental Ocasional (Cetasika #10 de 52)"
            },
            "category": {
                "pt": "Ocasional (Pakiṇṇaka — presente em 78 de 89 cittas; ausente nos 10 dvipañcaviññāṇa e no citta de dúvida, vicikicchāsampayutta)",
                "en": "Occasional (Pakiṇṇaka — present in 78 of 89 cittas; absent in the 10 dvipañcaviññāṇa and the doubt-accompanied citta, vicikicchāsampayutta)",
                "es": "Ocasional (Pakiṇṇaka — presente en 78 de 89 cittas; ausente en los 10 dvipañcaviññāṇa y en el citta de duda, vicikicchāsampayutta)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Convicção ou decisão firme quanto ao objeto (sanniṭṭhāna-lakkhaṇa).",
                    "en": "Conviction or firm resolve regarding the object (sanniṭṭhāna-lakkhaṇa).",
                    "es": "Convicción o resolución firme respecto al objeto (sanniṭṭhāna-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Não tatear nem vacilar (asaṃsappana-rasa).",
                    "en": "Not groping or wavering (asaṃsappana-rasa).",
                    "es": "No tantear ni vacilar (asaṃsappana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Decisividade (nicchaya-paccupaṭṭhāna).",
                    "en": "Decisiveness (nicchaya-paccupaṭṭhāna).",
                    "es": "Decisividad (nicchaya-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Aquilo sobre o qual se deve decidir (sanniṭṭhātabbadhamma-padaṭṭhāna).",
                    "en": "A thing to be convinced or decided about (sanniṭṭhātabbadhamma-padaṭṭhāna).",
                    "es": "Aquello sobre lo cual se ha de decidir (sanniṭṭhātabbadhamma-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Comparado nos Comentários a um pilar de pedra (indakhīla) devido à sua firmeza inabalável perante o objeto, ou a um juiz que pronuncia um veredicto decisivo. É diametralmente incompatível com a dúvida (vicikicchā), razão pela qual está ausente no vicikicchāsampayuttacitta.",
                "en": "Compared in the Commentaries to a stone pillar (indakhīla) owing to its unshakable resolve regarding the object, or a judge pronouncing a decisive verdict. It is directly incompatible with doubt (vicikicchā), and hence is excluded from the vicikicchāsampayuttacitta.",
                "es": "Comparado en los Comentarios a un pilar de piedra (indakhīla) por su firmeza inquebrantable ante el objeto. Es incompatible con la duda (vicikicchā), por lo que está ausente en el vicikicchāsampayuttacitta."
            },
            "bodhiRef": "CMA II, §3 & §11 (Guide, pp. 81, 95)"
        },
        "seeAlso": ["vicikicchā", "vicikicchāsampayutta", "pakiṇṇaka"]
    },

    "viriya": {
        "meaning": {
            "pt": "Energia; esforço; vigor; coragem heroica; o fator mental ocasional que sustenta, revigora e impede o colapso dos estados mentais associados.",
            "en": "Energy; effort; vigor; heroic exertion; the occasional mental factor that upholds, supports, and prevents the collapse of its associated mental states.",
            "es": "Energía; esfuerzo; vigor; el factor mental ocasional que sostiene, apuntala e impide el colapso de sus estados mentales asociados."
        },
        "grammar": "nt. (de vīra + iya)",
        "grammarLocalized": {
            "pt": "Substantivo neutro (derivado abstrato de vīra 'herói, valente' + -iya)",
            "en": "Neuter noun (abstract derivative from vīra 'hero, vigorous one' + -iya)",
            "es": "Sustantivo neutro (derivado abstracto de vīra 'héroe, vigoroso' + -iya)"
        },
        "root": "vīra (valente / vigoroso) + iya",
        "etymology": {
            "pt": "De vīra ('herói, pessoa corajosa e vigorosa') + sufixo abstrato -iya: vīrānaṃ bhāvo kammaṃ vā viriyaṃ — o estado ou ação de quem é destemido e vigoroso.",
            "en": "From vīra ('hero, vigorous person') + abstract suffix -iya: vīrānaṃ bhāvo kammaṃ vā viriyaṃ — the state or action of one who is vigorous and heroic.",
            "es": "De vīra ('héroe, persona vigorosa') + sufijo abstracto -iya: el estado o acción de quien es vigoroso y valiente."
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Ocasional (Cetasika #11 de 52)",
                "en": "Ultimate Reality — Occasional Mental Factor (Cetasika #11 of 52)",
                "es": "Realidad Última — Factor Mental Ocasional (Cetasika #11 de 52)"
            },
            "category": {
                "pt": "Ocasional (Pakiṇṇaka — presente em 73 de 89 cittas); aparece em 9 das 37 Bodhipakkhiyā Dhammā (4 Sammappadhāna, Viriyiddhipāda, Viriyindriya, Viriyabala, Viriyasambojjhaṅga, Sammāvāyāma)",
                "en": "Occasional (Pakiṇṇaka — present in 73 of 89 cittas); appears in 9 of the 37 Requisites of Enlightenment (4 Sammappadhāna, Viriyiddhipāda, Viriyindriya, Viriyabala, Viriyasambojjhaṅga, Sammāvāyāma)",
                "es": "Ocasional (Pakiṇṇaka — presente en 73 de 89 cittas); aparece en 9 de los 37 Requisitos de la Iluminación (4 Sammappadhāna, Viriyiddhipāda, Viriyindriya, Viriyabala, Viriyasambojjhaṅga, Sammāvāyāma)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Esforçar-se, sustentar e mobilizar (ussāha-lakkhaṇa).",
                    "en": "Supporting, exertion, and marshalling (ussāha-lakkhaṇa).",
                    "es": "Esforzarse, sostener y movilizar (ussāha-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Apontar e sustentar os estados associados (sahajātānaṃ upatthambhana-rasa), impedindo que recuem.",
                    "en": "To support and uphold its associated states (sahajātānaṃ upatthambhana-rasa), preventing them from receding.",
                    "es": "Apuntalar y sostener los estados asociados (sahajātānaṃ upatthambhana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Não-colapso ou firmeza (asaṃsīdana-paccupaṭṭhāna).",
                    "en": "Non-collapse or undauntedness (asaṃsīdana-paccupaṭṭhāna).",
                    "es": "No colapso o firmeza (asaṃsīdana-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Senso de urgência espiritual (saṃvega-padaṭṭhāna) ou qualquer base para despertar energia (viriyārambhavatthu).",
                    "en": "A sense of spiritual urgency (saṃvega-padaṭṭhāna) or a ground for arousing energy (viriyārambhavatthu).",
                    "es": "Un sentido de urgencia espiritual (saṃvega-padaṭṭhāna) o una base para despertar la energía (viriyārambhavatthu)."
                }
            },
            "philosophy": {
                "pt": "Comparado por Bhikkhu Bodhi (CMA II, §3, p. 81) a pilares novos adicionados a uma casa antiga para impedi-la de desabar, ou a um forte reforço militar que permite ao exército do rei derrotar o inimigo. Está ausente em 16 cittas sem raiz (10 dvipañcaviññāṇa, 2 sampaṭicchana, 3 santīraṇa e pañcadvārāvajjana). É o único fator mental que aparece 9 vezes nos 37 Requisitos da Iluminação (Cap. VII, §32).",
                "en": "Compared by Bhikkhu Bodhi (CMA II, §3, p. 81) to new timbers added to an old house to prevent it from collapsing, or strong reinforcements enabling the king's army to defeat the enemy. It is absent in 16 rootless cittas (10 dvipañcaviññāṇa, 2 sampaṭicchana, 3 santīraṇa, and pañcadvārāvajjana). Along with paññā, it is the most prominent factor in the 37 Requisites of Enlightenment, appearing 9 times (Ch. VII, §32).",
                "es": "Comparado por Bhikkhu Bodhi (CMA II, §3, p. 81) a vigas nuevas añadidas a una casa antigua para evitar su derrumbe. Está ausente en 16 cittas sin raíz y aparece 9 veces en los 37 Requisitos de la Iluminación (Cap. VII, §32)."
            },
            "bodhiRef": "CMA II, §3 & §11 (Guide, pp. 81, 95); VII, §32 (p. 283)"
        },
        "seeAlso": ["thīna", "middha", "sammappadhāna", "sammāvāyāma", "bodhipakkhiyadhamma"]
    },

    "pīti": {
        "meaning": {
            "pt": "Êxtase; entusiasmo; júbilo; interesse jubiloso no objeto; 3º fator de jhāna e fator de iluminação (pītisambojjhaṅga). Pertence ao agregado das formações mentais (saṅkhārakkhandha), distinguindo-se da sensação de felicidade (sukha/somanassa).",
            "en": "Zest; rapture; enthusiastic interest in the object; 3rd jhāna factor and enlightenment factor (pītisambojjhaṅga). Belongs to the aggregate of mental formations (saṅkhārakkhandha), distinct from pleasant feeling (sukha/somanassa).",
            "es": "Entusiasmo; éxtasis; júbilo; interés entusiasta en el objeto; 3º factor de jhāna y factor de iluminación (pītisambojjhaṅga). Pertenece al agregado de las formaciones mentales (saṅkhārakkhandha), distinto de la sensación agradable (sukha/somanassa)."
        },
        "grammar": "fem. (de √pī + ti)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (derivado da raiz √pī 'alegrar, satisfazer, refrescar')",
            "en": "Feminine noun (derived from root √pī 'to gladden, satisfy, refresh')",
            "es": "Sustantivo femenino (derivado de la raíz √pī 'alegrar, satisfacer, refrescar')"
        },
        "root": "√pī (alegrar / refrescar) + ti",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Ocasional (Cetasika #12 de 52)",
                "en": "Ultimate Reality — Occasional Mental Factor (Cetasika #12 of 52)",
                "es": "Realidad Última — Factor Mental Ocasional (Cetasika #12 de 52)"
            },
            "category": {
                "pt": "Ocasional (Pakiṇṇaka — presente em 51 de 121 cittas: os 18 kāmāvacara com somanassa e os 33 de 1º, 2º e 3º jhāna); 3º Fator de Jhāna; Bojjhaṅga",
                "en": "Occasional (Pakiṇṇaka — present in 51 of 121 cittas: the 18 somanassa-accompanied kāmāvacara cittas and 33 cittas of the 1st, 2nd, and 3rd jhāna); 3rd Jhāna Factor; Bojjhaṅga",
                "es": "Ocasional (Pakiṇṇaka — presente en 51 de 121 cittas: los 18 kāmāvacara con somanassa y los 33 de 1º, 2º y 3º jhāna); 3º Factor de Jhāna; Bojjhaṅga"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Afeição jubilosamente interessada pelo objeto (sampiyāyana-lakkhaṇa).",
                    "en": "Endearing or taking joyful interest in the object (sampiyāyana-lakkhaṇa).",
                    "es": "Aprecio jubiloso o interés entusiasta por el objeto (sampiyāyana-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Refrescar a mente e o corpo (kāyacittapīṇana-rasa) ou permear o organismo com arrebatamento (pharaṇa-rasa).",
                    "en": "To refresh mind and body (kāyacittapīṇana-rasa), or to pervade with rapture (pharaṇa-rasa).",
                    "es": "Refrescar la mente y el cuerpo (kāyacittapīṇana-rasa) o permear con éxtasis (pharaṇa-rasa)."
                },
                "paccupatthana": {
                    "pt": "Exaltação ou elação (odaggya-paccupaṭṭhāna).",
                    "en": "Elation or transport of mind (odaggya-paccupaṭṭhāna).",
                    "es": "Exaltación o elación mental (odaggya-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Mente-e-corpo (nāmarūpa-padaṭṭhāna).",
                    "en": "Mind-and-body (nāmarūpa-padaṭṭhāna).",
                    "es": "Mente-y-cuerpo (nāmarūpa-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Distinção clássica fundamental explicada por Bhikkhu Bodhi (CMA I, §§18–20, pp. 56–57): pīti pertence a saṅkhārakkhandha (formações conativas), enquanto sukha (somanassa) pertence a vedanākkhandha (sensação). Na símile do viajante exausto no deserto: pīti é a empolgação jubilosa ao avistar ou ouvir falar de um oásis com água fresca e bosque sombreado; sukha é o prazer sereno de efetivamente beber a água, banhar-se e descansar à sombra. Os Comentários enumeram 5 graus de pīti: khuddikā (menor, que arrepia os pelos), khaṇikā (momentâneo, como relâmpagos), okkantikā (inundante, como ondas na praia), ubbegā (elevador, capaz de fazer o corpo levitar) e pharaṇā (permeante, que preenche todo o corpo e amadurece em jhāna). No 4º jhāna, pīti é abandonado mas sukha permanece.",
                "en": "Fundamental classical distinction explained by Bhikkhu Bodhi (CMA I, §§18–20, pp. 56–57): pīti belongs to saṅkhārakkhandha (mental formations), whereas sukha (somanassa) belongs to vedanākkhandha (feeling). In the desert traveler simile: pīti is the elation upon seeing or hearing of an oasis; sukha is the actual bliss of drinking the water and resting in the shade. The Commentaries list 5 grades of pīti: minor (khuddikā), momentary (khaṇikā), showering (okkantikā), uplifting (ubbegā), and pervading (pharaṇā, which matures into jhāna). In the 4th jhāna, pīti is abandoned while sukha remains.",
                "es": "Distinción clásica explicada por Bhikkhu Bodhi (CMA I, §§18–20, pp. 56–57): pīti pertenece a saṅkhārakkhandha, mientras que sukha pertenece a vedanākkhandha. En el símil del viajero en el desierto: pīti es el júbilo al divisar un oasis; sukha es el placer de beber el agua y descansar a la sombra. En el 4º jhāna, pīti se abandona pero sukha permanece."
            },
            "bodhiRef": "CMA I, §§18–20 (Guide, pp. 56–57); II, §3 & §11 (pp. 81, 95)"
        },
        "seeAlso": ["sukha", "somanassa", "jhāna", "bojjhaṅga", "vedanā"]
    },

    "chanda": {
        "meaning": {
            "pt": "Desejo de agir (kattukamyatā); aspiração; zelo; o fator mental ocasional e eticamente variável que busca um objeto e estende 'a mão da mente' para realizar uma ação (distinto de lobha/taṇhā, que é sempre prejudicial).",
            "en": "Desire to act (kattukamyatā); aspiration; zeal; the ethically variable occasional mental factor that searches for an object and stretches forth 'the mind's hand' to achieve a goal (distinct from lobha/taṇhā, which is always unwholesome).",
            "es": "Deseo de actuar (kattukamyatā); aspiración; celo; el factor mental ocasional y éticamente variable que busca un objeto y extiende 'la mano de la mente' para lograr un fin (distinto de lobha/taṇhā, siempre perjudicial)."
        },
        "grammar": "masc. (de √chand + a)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (derivado da raiz √chand 'desejar, aspirar')",
            "en": "Masculine noun (derived from root √chand 'to wish, aspire')",
            "es": "Sustantivo masculino (derivado de la raíz √chand 'desear, aspirar')"
        },
        "root": "√chand (desejar / querer fazer) + a",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Ocasional (Cetasika #13 de 52)",
                "en": "Ultimate Reality — Occasional Mental Factor (Cetasika #13 of 52)",
                "es": "Realidad Última — Factor Mental Ocasional (Cetasika #13 de 52)"
            },
            "category": {
                "pt": "Ocasional (Pakiṇṇaka — presente em 69 de 89 cittas; ausente nos 18 ahetuka e nos 2 mohamūla); 1ª Base do Sucesso (Chandiddhipāda) e Predominância (Chandādhipati)",
                "en": "Occasional (Pakiṇṇaka — present in 69 of 89 cittas; absent in the 18 ahetuka and 2 mohamūla); 1st Means to Accomplishment (Chandiddhipāda) and Predominance (Chandādhipati)",
                "es": "Ocasional (Pakiṇṇaka — presente en 69 de 89 cittas; ausente en los 18 ahetuka y 2 mohamūla); 1ª Base del Éxito (Chandiddhipāda) y Predominancia (Chandādhipati)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "O desejo de agir ou realizar algo (kattukāmatā-lakkhaṇa).",
                    "en": "Desire to act or achieve something (kattukāmatā-lakkhaṇa).",
                    "es": "El deseo de actuar o realizar algo (kattukāmatā-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Buscar ou procurar um objeto (ārammaṇapariyesana-rasa).",
                    "en": "Searching for an object (ārammaṇapariyesana-rasa).",
                    "es": "Buscar o procurar un objeto (ārammaṇapariyesana-rasa)."
                },
                "paccupatthana": {
                    "pt": "A necessidade de um objeto (ārammaṇena atthikatā-paccupaṭṭhāna).",
                    "en": "Need for an object (ārammaṇena atthikatā-paccupaṭṭhāna).",
                    "es": "Necesidad de un objeto (ārammaṇena atthikatā-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Esse mesmo objeto tomado como meta (tasseva ārammaṇassa padaṭṭhāna). Deve ser visto como o estender da mão da mente em direção ao objeto.",
                    "en": "That very same object (tasseva ārammaṇassa padaṭṭhāna). It should be regarded as the stretching forth of the mind's hand towards the object.",
                    "es": "Ese mismo objeto (tasseva ārammaṇassa padaṭṭhāna). Debe verse como el extender la mano de la mente hacia el objeto."
                }
            },
            "philosophy": {
                "pt": "Como esclarece Bhikkhu Bodhi (CMA II, §3, pp. 81–82), chanda (desejo de agir, kattukāmatā) deve ser rigorosamente diferenciado de lobha/taṇhā (cobiça/anseio egoísta): enquanto lobha é invariavelmente akusala e gruda no objeto, chanda é um fator eticamente variável (aññasamāna). Quando associado a concomitantes salutares, funciona como dhammacchanda — a nobre aspiração de abandonar estados prejudiciais, cultivar estados salutares e realizar Nibbāna, constituindo a primeira das quatro bases para o sucesso espiritual (iddhipāda) e um dos quatro fatores de predominância (adhipati).",
                "en": "As Bhikkhu Bodhi clarifies (CMA II, §3, pp. 81–82), chanda (desire to act, kattukāmatā) must be strictly distinguished from lobha/taṇhā (selfish greed/craving): whereas lobha is invariably akusala and clings to the object, chanda is an ethically variable factor (aññasamāna). When conjoined with wholesome concomitants, it functions as dhammacchanda — the virtuous aspiration to abandon unwholesome states, cultivate wholesome states, and realize Nibbāna, serving as the first of the four means to accomplishment (iddhipāda) and one of the four predominance factors (adhipati).",
                "es": "Como aclara Bhikkhu Bodhi (CMA II, §3, pp. 81–82), chanda (deseo de actuar, kattukāmatā) debe distinguirse rigurosamente de lobha/taṇhā (codicia/anhelo egoísta): mientras lobha es invariablemente akusala, chanda es éticamente variable (aññasamāna). En cittas saludables actúa como dhammacchanda — la noble aspiración espiritual (iddhipāda y adhipati)."
            },
            "bodhiRef": "CMA II, §3 & §11 (Guide, pp. 81–82, 95); VII, §20 & §26 (pp. 276, 279)"
        },
        "seeAlso": ["lobha", "taṇhā", "iddhipāda", "adhipati", "pakiṇṇaka"]
    },

    # ── 14 FATORES PREJUDICIAIS (AKUSALACETASIKA) ────────────────────────────
    "moha": {
        "meaning": {
            "pt": "Delusão; cegueira mental; ignorância (avijjā); o 1º dos 4 fatores prejudiciais universais (presente em todos os 12 cittas akusala) e a raiz fundamental de todo o mal, que encobre a natureza intrínseca real dos fenômenos.",
            "en": "Delusion; mental blindness; ignorance (avijjā); the 1st of the 4 universal unwholesome factors (present in all 12 akusala cittas) and the fundamental root of all unwholesomeness, concealing the real intrinsic nature of phenomena.",
            "es": "Ilusión; ceguera mental; ignorancia (avijjā); el 1º de los 4 factores perjudiciales universales (presente en los 12 cittas akusala) y la raíz fundamental de todo lo perjudicial, que oculta la naturaleza real de los fenómenos."
        },
        "grammar": "masc. (de √muh + *a)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (derivado da raiz √muh 'estar confuso, iludido, estupefato')",
            "en": "Masculine noun (derived from root √muh 'to be stupefied, deluded, bewildered')",
            "es": "Sustantivo masculino (derivado de la raíz √muh 'estar confundido, iludido')"
        },
        "root": "√muh (estar confuso / iludido) + *a",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Prejudicial Universal (Cetasika #14 de 52)",
                "en": "Ultimate Reality — Universal Unwholesome Mental Factor (Cetasika #14 of 52)",
                "es": "Realidad Última — Factor Mental Perjudicial Universal (Cetasika #14 de 52)"
            },
            "category": {
                "pt": "Akusala Universal (Sabbākusalasādhāraṇa — presente nos 12 cittas akusala); Raiz Prejudicial (Akusalahetu); idêntico a Avijjā",
                "en": "Unwholesome Universal (Sabbākusalasādhāraṇa — present in all 12 akusala cittas); Unwholesome Root (Akusalahetu); identical with Avijjā",
                "es": "Universal Perjudicial (Sabbākusalasādhāraṇa — presente en los 12 cittas akusala); Raíz Perjudicial (Akusalahetu); idéntico a Avijjā"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Cegueira mental (cittassa andhabhāva-lakkhaṇa) ou desconhecimento (aññāṇa-lakkhaṇa).",
                    "en": "Mental blindness (cittassa andhabhāva-lakkhaṇa) or unknowing (aññāṇa-lakkhaṇa).",
                    "es": "Ceguera mental (cittassa andhabhāva-lakkhaṇa) o desconocimiento (aññāṇa-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Não-penetração (asampaṭivedha-rasa) ou encobrimento da verdadeira natureza intrínseca do objeto (ārammaṇasabhāvachādana-rasa).",
                    "en": "Non-penetration (asampaṭivedha-rasa), or concealment of the real nature of the object (ārammaṇasabhāvachādana-rasa).",
                    "es": "No penetración (asampaṭivedha-rasa) u ocultamiento de la naturaleza real del objeto (ārammaṇasabhāvachādana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Ausência de entendimento correto (asammāpaṭipatti-paccupaṭṭhāna) ou escuridão mental (andhakāra-paccupaṭṭhāna).",
                    "en": "Absence of right understanding (asammāpaṭipatti-paccupaṭṭhāna) or mental darkness (andhakāra-paccupaṭṭhāna).",
                    "es": "Ausencia de recto entendimiento (asammāpaṭipatti-paccupaṭṭhāna) u oscuridad mental (andhakāra-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Atenção insensata / não criteriosa (ayoniso manasikāra-padaṭṭhāna). Deve ser visto como a raiz de todo o mal (sabbākusalānaṃ mūla).",
                    "en": "Unwise attention (ayoniso manasikāra-padaṭṭhāna). It should be seen as the root of all that is unwholesome (sabbākusalānaṃ mūla).",
                    "es": "Atención insensata (ayoniso manasikāra-padaṭṭhāna). Debe verse como la raíz de todo lo perjudicial (sabbākusalānaṃ mūla)."
                }
            },
            "philosophy": {
                "pt": "Como explica Bhikkhu Bodhi (CMA I, §6 & II, §4), enquanto a cobiça (lobha) e o ódio (dosa) são mutuamente exclusivos, a delusão (moha) está presente em todos os 12 cittas akusala como alicerce subjacente (nos 8 lobhamūla, nos 2 dosamūla e, como única raiz, nos 2 mohamūla). Ontologicamente, o cetasika moha é idêntico à ignorância (avijjā), o 1º elo do paṭiccasamuppāda, e à impureza da ignorância (avijjāsava).",
                "en": "As Bhikkhu Bodhi explains (CMA I, §6 & II, §4), whereas greed (lobha) and hatred (dosa) are mutually exclusive, delusion (moha) is present in all 12 akusala cittas as their underlying root (in the 8 lobhamūla, 2 dosamūla, and as the sole root in the 2 mohamūla). Ontologically, the cetasika moha is identical with ignorance (avijjā), the 1st link of Dependent Arising, and the taint of ignorance (avijjāsava).",
                "es": "Como explica Bhikkhu Bodhi (CMA I, §6 y II, §4), mientras la codicia (lobha) y el odio (dosa) son mutuamente excluyentes, la ilusión (moha) está presente en todos los 12 cittas akusala. Ontológicamente, moha es idéntico a la ignorancia (avijjā)."
            },
            "bodhiRef": "CMA I, §6 (Guide, pp. 38–40); II, §4 & §13 (pp. 82–83, 96)"
        },
        "seeAlso": ["avijjā", "amoha", "paññā", "lobha", "dosa", "ahirika", "anottappa", "uddhacca"]
    },

    "ahirika": {
        "meaning": {
            "pt": "Ausência de vergonha moral; desfaçatez; impudência; o 2º dos 4 fatores prejudiciais universais (presente em todos os 12 cittas akusala), caracterizado pela falta de repugnância interna perante a má conduta.",
            "en": "Shamelessness; moral impudence; the 2nd of the 4 universal unwholesome factors (present in all 12 akusala cittas), characterized by the absence of internal disgust at bodily and verbal misconduct.",
            "es": "Falta de vergüenza moral; desvergüenza; impudicia; el 2º de los 4 factores perjudiciales universales (presente en los 12 cittas akusala), caracterizado por la ausencia de repugnancia ante la mala conducta."
        },
        "grammar": "nt. (na > a + hirī + ka)",
        "grammarLocalized": {
            "pt": "Substantivo neutro (Nañ-Tappurisa: a + hirī + -ka)",
            "en": "Neuter noun (Nañ-Tappurisa: a + hirī + -ka)",
            "es": "Sustantivo neutro (Nañ-Tappurisa: a + hirī + -ka)"
        },
        "root": "na > a (não) + √hir (envergonhar-se) + ī + ka",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Prejudicial Universal (Cetasika #15 de 52)",
                "en": "Ultimate Reality — Universal Unwholesome Mental Factor (Cetasika #15 of 52)",
                "es": "Realidad Última — Factor Mental Perjudicial Universal (Cetasika #15 de 52)"
            },
            "category": {
                "pt": "Akusala Universal (Sabbākusalasādhāraṇa — presente nos 12 cittas akusala); Poder Prejudicial (Ahirikabala); oposto de Hiri",
                "en": "Unwholesome Universal (Sabbākusalasādhāraṇa — present in all 12 akusala cittas); Unwholesome Power (Ahirikabala); opposite of Hiri",
                "es": "Universal Perjudicial (Sabbākusalasādhāraṇa — presente en los 12 cittas akusala); Poder Perjudicial (Ahirikabala); opuesto de Hiri"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Ausência de repugnância ou aversão pela má conduta corporal e verbal (kāyaduccaritādīhi ajegucchana-lakkhaṇa), ou ausência de vergonha (alajjā-lakkhaṇa).",
                    "en": "Absence of disgust at bodily and verbal misconduct (kāyaduccaritādīhi ajegucchana-lakkhaṇa), or immodesty (alajjā-lakkhaṇa).",
                    "es": "Ausencia de repugnancia ante la mala conducta corporal y verbal (ajegucchana-lakkhaṇa), o falta de pudor (alajjā-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Cometer ações más sem pudor (pāpānaṃ karaṇa-rasa).",
                    "en": "Doing evil things without modesty (pāpānaṃ karaṇa-rasa).",
                    "es": "Cometer malas acciones sin pudor (pāpānaṃ karaṇa-rasa)."
                },
                "paccupatthana": {
                    "pt": "Não recuar perante o mal (asaṅkoca-paccupaṭṭhāna).",
                    "en": "Not shrinking away from evil (asaṅkoca-paccupaṭṭhāna).",
                    "es": "No retroceder ante el mal (asaṅkoca-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Falta de respeito por si mesmo (attani agārava-padaṭṭhāna).",
                    "en": "Lack of respect for oneself (attani agārava-padaṭṭhāna).",
                    "es": "Falta de respeto por uno mismo (attani agārava-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Nos Comentários (Atthasālinī 248), ahirika é comparado a um porco doméstico que não sente qualquer repulsa pela imundície, enquanto seu oposto belo, hiri (pudor moral), é comparado a um cisne real que jamais pousa na sujeira. Sua causa próxima é a falta de autorrespeito (attāgārava).",
                "en": "In the Commentaries (Atthasālinī 248), ahirika is compared to a village pig that feels no disgust towards filth, whereas its beautiful opposite, hiri (moral shame), is compared to a royal swan that refuses to alight on filth. Its proximate cause is lack of self-respect (attāgārava).",
                "es": "En los Comentarios (Atthasālinī 248), ahirika se compara con un cerdo de aldea que no siente repugnancia por la inmundicia, mientras que su opuesto hermoso, hiri (pudor moral), nace del respeto por uno mismo."
            },
            "bodhiRef": "CMA II, §4 & §5 (Guide, pp. 83, 86)"
        },
        "seeAlso": ["anottappa", "hiri", "ottappa", "moha", "uddhacca"]
    },

    "anottappa": {
        "meaning": {
            "pt": "Ausência de temor moral; imprudência moral; destemor perante o mal; o 3º dos 4 fatores prejudiciais universais (presente em todos os 12 cittas akusala), caracterizado pela falta de receio das consequências kármicas e sociais da má conduta.",
            "en": "Fearlessness of wrongdoing; moral recklessness; the 3rd of the 4 universal unwholesome factors (present in all 12 akusala cittas), characterized by the absence of dread regarding the consequences of misconduct.",
            "es": "Ausencia de temor moral; temeridad moral; el 3º de los 4 factores perjudiciales universales (presente en los 12 cittas akusala), caracterizado por la ausencia de temor ante las consecuencias de obrar mal."
        },
        "grammar": "nt. (na > an + ottappa)",
        "grammarLocalized": {
            "pt": "Substantivo neutro (Nañ-Tappurisa: an + ottappa)",
            "en": "Neuter noun (Nañ-Tappurisa: an + ottappa)",
            "es": "Sustantivo neutro (Nañ-Tappurisa: an + ottappa)"
        },
        "root": "na > an (não) + ud + √tap (queimar / atormentar) + ya",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Prejudicial Universal (Cetasika #16 de 52)",
                "en": "Ultimate Reality — Universal Unwholesome Mental Factor (Cetasika #16 of 52)",
                "es": "Realidad Última — Factor Mental Perjudicial Universal (Cetasika #16 de 52)"
            },
            "category": {
                "pt": "Akusala Universal (Sabbākusalasādhāraṇa — presente nos 12 cittas akusala); Poder Prejudicial (Anottappabala); oposto de Ottappa",
                "en": "Unwholesome Universal (Sabbākusalasādhāraṇa — present in all 12 akusala cittas); Unwholesome Power (Anottappabala); opposite of Ottappa",
                "es": "Universal Perjudicial (Sabbākusalasādhāraṇa — presente en los 12 cittas akusala); Poder Perjudicial (Anottappabala); opuesto de Ottappa"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Ausência de pavor ou receio perante a má conduta (duccaritādīhi anuttāsana-lakkhaṇa).",
                    "en": "Absence of dread on account of misconduct (duccaritādīhi anuttāsana-lakkhaṇa).",
                    "es": "Ausencia de temor o recelo ante la mala conducta (anuttāsana-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Praticar ações prejudiciais sem temer suas consequências (pāpānaṃ karaṇa-rasa).",
                    "en": "Doing evil things reckless of consequences (pāpānaṃ karaṇa-rasa).",
                    "es": "Hacer cosas malas sin temer sus consecuencias (pāpānaṃ karaṇa-rasa)."
                },
                "paccupatthana": {
                    "pt": "Não recuar diante do mal (asaṅkoca-paccupaṭṭhāna).",
                    "en": "Not shrinking away from evil (asaṅkoca-paccupaṭṭhāna).",
                    "es": "No retroceder ante el mal (asaṅkoca-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Falta de respeito pelos outros e pelas consequências kármicas (paresu agārava-padaṭṭhāna).",
                    "en": "Lack of respect for others and kammic consequences (paresu agārava-padaṭṭhāna).",
                    "es": "Falta de respeto por los demás y por las consecuencias kármicas (paresu agārava-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Enquanto ahirika tem origem interna (falta de respeito por si mesmo, como o porco que se lança na lama), anottappa tem referência externa (falta de respeito pelos outros e pelas consequências dolorosas, como uma mariposa que se lança cegamente na chama de uma lâmpada sem perceber que vai se queimar — Atthasālinī 249).",
                "en": "Whereas ahirika has an internal reference (lack of respect for oneself, like a pig wallowing in mire), anottappa has an external reference (lack of respect for others and for kammic consequences, like a moth blindly hurling itself into a flame without realizing it will be burned — Atthasālinī 249).",
                "es": "Mientras ahirika tiene referencia interna (falta de respeto por uno mismo), anottappa tiene referencia externa (falta de respeto por los demás y por el fruto kármico, como una polilla que se lanza ciegamente al fuego)."
            },
            "bodhiRef": "CMA II, §4 & §5 (Guide, pp. 83, 86)"
        },
        "seeAlso": ["ahirika", "ottappa", "hiri", "moha", "uddhacca"]
    },

    "uddhacca": {
        "meaning": {
            "pt": "Inquietação; agitação mental; distração; o 4º dos 4 fatores prejudiciais universais (presente em todos os 12 cittas akusala), oposto à tranquilidade e à concentração.",
            "en": "Restlessness; mental agitation; distraction; the 4th of the 4 universal unwholesome factors (present in all 12 akusala cittas), opposed to tranquillity and concentration.",
            "es": "Inquietud; agitación mental; distracción; el 4º de los 4 factores perjudiciales universales (presente en los 12 cittas akusala), opuesto a la tranquilidad y la concentración."
        },
        "grammar": "nt. (ud + √dhu + ta + ya)",
        "grammarLocalized": {
            "pt": "Substantivo neutro abstrato (ud + √dhu 'sacudir, agitar' + -ya)",
            "en": "Abstract neuter noun (ud + √dhu 'to shake, agitate' + -ya)",
            "es": "Sustantivo neutro abstracto (ud + √dhu 'sacudir, agitar' + -ya)"
        },
        "root": "ud (para cima) + √dhu (sacudir / agitar) + ta + ya",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Prejudicial Universal (Cetasika #17 de 52)",
                "en": "Ultimate Reality — Universal Unwholesome Mental Factor (Cetasika #17 of 52)",
                "es": "Realidad Última — Factor Mental Perjudicial Universal (Cetasika #17 de 52)"
            },
            "category": {
                "pt": "Akusala Universal (Sabbākusalasādhāraṇa — presente nos 12 cittas akusala); Obstáculo (Nīvaraṇa); Grilhão Superior (Uddhambhāgiya-saṃyojana)",
                "en": "Unwholesome Universal (Sabbākusalasādhāraṇa — present in all 12 akusala cittas); Hindrance (Nīvaraṇa); Higher Fetter (Uddhambhāgiya-saṃyojana)",
                "es": "Universal Perjudicial (Sabbākusalasādhāraṇa — presente en los 12 cittas akusala); Obstáculo (Nīvaraṇa); Traba Superior (Uddhambhāgiya-saṃyojana)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Desassossego ou intranquilidade da mente (avyūpasama-lakkhaṇa), como a água agitada pelo vento ou cinzas atingidas por uma pedra.",
                    "en": "Disquietude or unsettledness of mind (avyūpasama-lakkhaṇa), like water whipped up by the wind or ashes struck by a stone.",
                    "es": "Desasosiego o intranquilidad de la mente (avyūpasama-lakkhaṇa), como el agua agitada por el viento."
                },
                "rasa": {
                    "pt": "Tornar a mente instável e vacilante (anavaṭṭhāna-rasa), como o vento que faz tremular uma bandeira.",
                    "en": "To make the mind unsteady (anavaṭṭhāna-rasa), as wind makes a banner ripple.",
                    "es": "Hacer que la mente sea inestable (anavaṭṭhāna-rasa), como el viento que hace ondear una bandera."
                },
                "paccupatthana": {
                    "pt": "Turbulência, dispersão ou vagueio mental (bhantatta-paccupaṭṭhāna).",
                    "en": "Turmoil or mental wandering (bhantatta-paccupaṭṭhāna).",
                    "es": "Turbulencia o divagación mental (bhantatta-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Atenção insensata à inquietação mental (cetaso avyūpasame ayonisomanasikāra-padaṭṭhāna).",
                    "en": "Unwise attention to mental disquiet (cetaso avyūpasame ayonisomanasikāra-padaṭṭhāna).",
                    "es": "Atención insensata al desasosiego mental (cetaso avyūpasame ayonisomanasikāra-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Uddhacca está presente em todos os 12 cittas prejudiciais, sendo o fator dominante no 12º citta (uddhaccasampayutta). É um dos cinco obstáculos (junto com kukkucca) e um dos cinco grilhões superiores (uddhambhāgiya-saṃyojana), só sendo erradicado definitivamente pelo quarto caminho supramundano (arahattamagga).",
                "en": "Uddhacca is present in all 12 unwholesome cittas and is the chief factor in the 12th citta (uddhaccasampayutta). It is one of the five hindrances (paired with kukkucca) and one of the five higher fetters (uddhambhāgiya-saṃyojana), eradicated only by the fourth supramundane path (arahattamagga).",
                "es": "Uddhacca está presente en todos los 12 cittas akusala y es uno de los cinco obstáculos y una de las cinco trabas superiores (uddhambhāgiya-saṃyojana), erradicada solo por el camino del Arahant."
            },
            "bodhiRef": "CMA I, §6 (p. 39); II, §4 & §13 (Guide, pp. 83, 96); IX, §41 (p. 363)"
        },
        "seeAlso": ["uddhaccasampayutta", "moha", "ahirika", "anottappa", "passaddhi", "ekaggatā"]
    },

    "lobha": {
        "meaning": {
            "pt": "Cobiça; apego; desejo egoísta (taṇhā / rāga); a primeira raiz prejudicial (akusalahetu), presente em todos os 8 cittas enraizados na cobiça (lobhamūlacittāni).",
            "en": "Greed; attachment; selfish desire (taṇhā / rāga); the first unwholesome root (akusalahetu), present in all 8 greed-rooted cittas (lobhamūlacittāni).",
            "es": "Codicia; apego; deseo egoísta (taṇhā / rāga); la primera raíz perjudicial (akusalahetu), presente en todos los 8 cittas enraizados en la codicia (lobhamūlacittāni)."
        },
        "grammar": "masc. (de √lubh + *a)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (derivado da raiz √lubh 'cobiçar, desejar ardentemente')",
            "en": "Masculine noun (derived from root √lubh 'to covet, long for')",
            "es": "Sustantivo masculino (derivado de la raíz √lubh 'codiciar, anhelar')"
        },
        "root": "√lubh (cobiçar / desejar) + *a",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Prejudicial (Cetasika #18 de 52) & 1ª Raiz Prejudicial",
                "en": "Ultimate Reality — Unwholesome Mental Factor (Cetasika #18 of 52) & 1st Unwholesome Root",
                "es": "Realidad Última — Factor Mental Perjudicial (Cetasika #18 de 52) y 1ª Raíz Perjudicial"
            },
            "category": {
                "pt": "Tríade da Cobiça (Lobhatika — presente nos 8 Lobhamūlacittāni); idêntico a Taṇhā (2ª Nobre Verdade), Kāmāsava, Bhavāsava, Rāga, Abhijjhā",
                "en": "Greed Triad (Lobhatika — present in the 8 Lobhamūlacittāni); identical with Taṇhā (2nd Noble Truth), Kāmāsava, Bhavāsava, Rāga, Abhijjhā",
                "es": "Tríada de la Codicia (Lobhatika — presente en los 8 Lobhamūlacittāni); idéntico a Taṇhā (2ª Noble Verdad), Kāmāsava, Bhavāsava, Rāga, Abhijjhā"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Agarrar ou prender-se a um objeto (ārammaṇaggahaṇa-lakkhaṇa), como a visco de caçar macacos (makkaṭalekhā).",
                    "en": "Grasping an object (ārammaṇaggahaṇa-lakkhaṇa), like monkey-lime.",
                    "es": "Agarrar o aferrarse a un objeto (ārammaṇaggahaṇa-lakkhaṇa), como la liga para cazar monos."
                },
                "rasa": {
                    "pt": "Aderir ou grudar (abhiṣaṅga-rasa), assim como um pedaço de carne crua gruda numa panela quente.",
                    "en": "Sticking or adhering (abhisaṅga-rasa), as a piece of raw meat sticks to a hot pan.",
                    "es": "Adherirse o pegarse (abhisaṅga-rasa), como la carne cruda se pega a una sartén caliente."
                },
                "paccupatthana": {
                    "pt": "Não largar ou não renunciar (apariccāga-paccupaṭṭhāna), como a tinta de óleo que mancha um tecido.",
                    "en": "Not giving up or not relinquishing (apariccāga-paccupaṭṭhāna), like a dye of lampblack.",
                    "es": "No soltar o no renunciar (apariccāga-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Ver deleite e gratificação nas coisas que levam ao cativeiro (saṃyojaniyesu dhammesu assādadassana-padaṭṭhāna).",
                    "en": "Seeing enjoyment in things that lead to bondage (saṃyojaniyesu dhammesu assādadassana-padaṭṭhāna).",
                    "es": "Ver disfrute y gratificación en las cosas que conducen a la esclavitud (saṃyojaniyesu dhammesu assādadassana-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "No Abhidhamma, o cetasika lobha abrange todos os graus de apego — desde a paixão sensual voraz até o mais sutil apego à existência nos reinos de jhāna (rūparāga e arūparāga). No Cap. VII (§14), o mesmo cetasika lobha aparece sob diferentes nomes funcionais: kāmāsava e bhavāsava (entre os āsavas), abhijjhā kāyagantha (entre os nós), kāmupādāna (entre os apegos), kāmacchanda (entre os obstáculos) e kāmarāga/bhavarāga (entre as tendências latentes e grilhões).",
                "en": "In the Abhidhamma, the single cetasika lobha covers all degrees of attachment — from intense sensual passion to the subtlest attachment to jhānic existence (rūparāga and arūparāga). In Ch. VII (§14), this single cetasika lobha is shown to underlie numerous categories under different functional names: kāmāsava and bhavāsava, abhijjhā-kāyagantha, kāmupādāna, kāmacchanda-nīvaraṇa, and kāmarāga/bhavarāga.",
                "es": "En el Abhidhamma, el único cetasika lobha abarca todos los grados de apego, desde la pasión sensual intensa hasta el apego sutil a los reinos de jhāna (rūparāga y arūparāga). En el Cap. VII (§14), subyace a taṇhā, kāmāsava, bhavāsava, kāmupādāna y kāmacchanda."
            },
            "bodhiRef": "CMA I, §4 (Guide, pp. 34–37); II, §4 & §13 (pp. 83, 97); VII, §14 (p. 272)"
        },
        "seeAlso": ["alobha", "taṇhā", "diṭṭhi", "māna", "chanda", "dosa", "moha"]
    },

    "diṭṭhi": {
        "meaning": {
            "pt": "Visão errônea (micchādiṭṭhi); entendimento distorcido; crença especulativa ou dogmática que interpreta equivocadamente a natureza da realidade (presente em 4 dos 8 cittas enraizados na cobiça).",
            "en": "Wrong view (micchādiṭṭhi); distorted belief; dogmatic or speculative misapprehension of the nature of actuality (present in 4 of the 8 greed-rooted cittas).",
            "es": "Visión errónea (micchādiṭṭhi); creencia distorsionada; interpretación dogmática o especulativa equivocada de la realidad (presente en 4 de los 8 cittas enraizados en la codicia)."
        },
        "grammar": "fem. (de √dis + ti)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (derivado da raiz √dis 'ver, interpretar')",
            "en": "Feminine noun (derived from root √dis 'to see, view')",
            "es": "Sustantivo femenino (derivado de la raíz √dis 'ver, interpretar')"
        },
        "root": "√dis (ver) + ti (> ṭṭhi)",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Prejudicial Ocasional (Cetasika #19 de 52)",
                "en": "Ultimate Reality — Occasional Unwholesome Mental Factor (Cetasika #19 of 52)",
                "es": "Realidad Última — Factor Mental Perjudicial Ocasional (Cetasika #19 de 52)"
            },
            "category": {
                "pt": "Tríade da Cobiça (Lobhatika — presente nos 4 Lobhamūlacittas diṭṭhigatasampayutta: #1, #2, #5, #6); Erradicado no Sotāpatti-magga",
                "en": "Greed Triad (Lobhatika — present in the 4 diṭṭhigatasampayutta Lobhamūlacittas: #1, #2, #5, #6); Eradicated at Sotāpatti-magga",
                "es": "Tríada de la Codicia (Lobhatika — presente en los 4 Lobhamūlacittas diṭṭhigatasampayutta: #1, #2, #5, #6); Erradicado en Sotāpatti-magga"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Interpretação ou aderência insensata e injustificada às coisas (ayoniso abhinivesa-lakkhaṇa).",
                    "en": "Unwise (unjustified) interpretation of things (ayoniso abhinivesa-lakkhaṇa).",
                    "es": "Interpretación insensata e injustificada de las cosas (ayoniso abhinivesa-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Pressupor ou agarrar-se erroneamente com base em aparências superficiais (parāmāsa-rasa).",
                    "en": "To preassume or misapprehend (parāmāsa-rasa).",
                    "es": "Presuponer o aferrarse erróneamente (parāmāsa-rasa)."
                },
                "paccupatthana": {
                    "pt": "Crença ou interpretação distorcida (micchābhinivesa-paccupaṭṭhāna).",
                    "en": "Wrong interpretation or belief (micchābhinivesa-paccupaṭṭhāna).",
                    "es": "Creencia o interpretación distorsionada (micchābhinivesa-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Falta de disposição para ver os Nobres (ariyānaṃ adassanakāmatādi-padaṭṭhāna) e não desejar ouvir o verdadeiro Dhamma.",
                    "en": "Unwillingness to see the Noble Ones (ariyānaṃ adassanakāmatādi-padaṭṭhāna) and lack of desire to hear the true Dhamma.",
                    "es": "Falta de disposición para ver a los Nobles (ariyānaṃ adassanakāmatādi-padaṭṭhāna) y no desear escuchar el verdadero Dhamma."
                }
            },
            "philosophy": {
                "pt": "Salvo quando qualificado pelo prefixo sammā- (em sammādiṭṭhi, que é o cetasika paññā), a palavra diṭṭhi isolada no Abhidhamma denota sempre micchādiṭṭhi (visão errônea). Compreende a visão de identidade pessoal (sakkāyadiṭṭhi), o apego a ritos e cerimônias como suficientes para a libertação (sīlabbataparāmāsa), o eternalismo (sassatadiṭṭhi), o niilismo (ucchedadiṭṭhi) e as visões que negam a eficácia moral do kamma (natthikadiṭṭhi, ahetukadiṭṭhi, akiriyadiṭṭhi). Diṭṭhi e māna (presunção) são como dois leões que não podem habitar na mesma caverna: jamais surgem no mesmo citta.",
                "en": "Unless qualified by the prefix sammā- (in sammādiṭṭhi, which is the cetasika paññā), the bare word diṭṭhi in the Abhidhamma always denotes wrong view (micchādiṭṭhi). It encompasses personality view (sakkāyadiṭṭhi), adherence to rites and ceremonies (sīlabbataparāmāsa), eternalism (sassatadiṭṭhi), annihilationism (ucchedadiṭṭhi), and views denying kammic efficacy (natthikadiṭṭhi, ahetukadiṭṭhi, akiriyadiṭṭhi). Diṭṭhi and māna (conceit) are compared to two lions that cannot share the same cave: they never arise in the same citta.",
                "es": "Salvo cuando va precedido por sammā- (en sammādiṭṭhi = paññā), la palabra diṭṭhi en el Abhidhamma denota siempre visión errónea (micchādiṭṭhi). Diṭṭhi y māna (presunción) jamás surgen en el mismo citta."
            },
            "bodhiRef": "CMA I, §4 (Guide, pp. 35–36); II, §4 & §13 (pp. 83, 97); V, §22 (p. 206); VII, §7 (p. 269)"
        },
        "seeAlso": ["diṭṭhigatasampayutta", "diṭṭhigatavippayutta", "māna", "sammādiṭṭhi", "paññā"]
    },

    "māna": {
        "meaning": {
            "pt": "Presunção; orgulho; arrogância; autoexaltação comparativa ('sou superior', 'sou igual' ou 'sou inferior'); fator mental prejudicial ocasional que surge apenas nos 4 cittas enraizados na cobiça e dissociados de visão errônea (diṭṭhigatavippayutta).",
            "en": "Conceit; pride; haughtiness; comparative self-measurement ('I am superior', 'I am equal', or 'I am inferior'); an occasional unwholesome mental factor arising only in the 4 greed-rooted cittas dissociated from wrong view (diṭṭhigatavippayutta).",
            "es": "Presunción; orgullo; altivez; autoevaluación comparativa ('soy superior', 'soy igual' o 'soy inferior'); factor mental perjudicial ocasional que surge solo en los 4 cittas enraizados en la codicia disociados de visión errónea."
        },
        "grammar": "masc. (de √man + *a)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (derivado da raiz √man 'pensar de si, medir-se')",
            "en": "Masculine noun (derived from root √man 'to think of oneself, measure')",
            "es": "Sustantivo masculino (derivado de la raíz √man 'pensar de sí, medirse')"
        },
        "root": "√man (pensar / medir-se) + *a",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Prejudicial Ocasional (Cetasika #20 de 52)",
                "en": "Ultimate Reality — Occasional Unwholesome Mental Factor (Cetasika #20 of 52)",
                "es": "Realidad Última — Factor Mental Perjudicial Ocasional (Cetasika #20 de 52)"
            },
            "category": {
                "pt": "Tríade da Cobiça (Lobhatika — adjuncto não-fixo [aniyatayogī] nos 4 Lobhamūlacittas diṭṭhigatavippayutta: #3, #4, #7, #8); Grilhão Superior erradicado no Arahattamagga",
                "en": "Greed Triad (Lobhatika — unfixed adjunct [aniyatayogī] in the 4 diṭṭhigatavippayutta Lobhamūlacittas: #3, #4, #7, #8); Higher Fetter eradicated at Arahattamagga",
                "es": "Tríada de la Codicia (Lobhatika — adjunto no fijo [aniyatayogī] en los 4 Lobhamūlacittas diṭṭhigatavippayutta: #3, #4, #7, #8); Traba Superior erradicada en Arahattamagga"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Altivez ou soberba (unnati-lakkhaṇa).",
                    "en": "Haughtiness or loftiness (unnati-lakkhaṇa).",
                    "es": "Altivez o soberbia (unnati-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Autoexaltação (sampaggaha-rasa).",
                    "en": "Self-exaltation (sampaggaha-rasa).",
                    "es": "Autoexaltación (sampaggaha-rasa)."
                },
                "paccupatthana": {
                    "pt": "Vanglória ou desejo de erguer um estandarte para exibir-se (ketukamyatā-paccupaṭṭhāna).",
                    "en": "Vainglory, lit. desire to fly a banner to advertise oneself (ketukamyatā-paccupaṭṭhāna).",
                    "es": "Vanagloria, deseo de alzar un estandarte para exhibirse (ketukamyatā-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "A cobiça dissociada de visões errôneas (diṭṭhivippayuttalobha-padaṭṭhāna). Deve ser visto como uma forma de loucura (ummāda).",
                    "en": "Greed dissociated from views (diṭṭhivippayuttalobha-padaṭṭhāna). It should be regarded as madness (ummāda).",
                    "es": "La codicia disociada de visiones erróneas (diṭṭhivippayuttalobha-padaṭṭhāna). Debe verse como locura (ummāda)."
                }
            },
            "philosophy": {
                "pt": "Diferentemente de sakkāyadiṭṭhi (a visão dogmática de um 'eu' substancial, erradicada pelo sotāpanna), māna é o hábito afetivo-comparativo de medir os cinco agregados em relação aos outros ('sou melhor', 'sou igual', 'sou pior' — as 9 formas de māna). Por surgir apenas nos cittas diṭṭhigatavippayutta, māna ainda persiste sutilmente (como asmimāna, o senso residual de 'eu sou') nos sotāpannas, sakadāgāmīs e anāgāmīs, sendo totalmente erradicado apenas pelo caminho do Arahant.",
                "en": "Unlike sakkāyadiṭṭhi (the dogmatic view of a substantial 'self', eradicated at stream-entry), māna is the comparative habit of measuring the five aggregates against others ('I am better', 'I am equal', 'I am worse'). Because it arises only in diṭṭhigatavippayutta cittas, subtle conceit (asmimāna, the residual sense 'I am') persists in stream-enterers, once-returners, and non-returners, being completely eradicated only by the path of Arahantship.",
                "es": "A diferencia de sakkāyadiṭṭhi (erradicada al entrar en la corriente), māna es el hábito comparativo de medirse frente a otros ('soy superior', 'soy igual', 'soy inferior'). Persiste sutilmente como asmimāna hasta ser erradicado por el camino del Arahant."
            },
            "bodhiRef": "CMA II, §4, §13 & §17 (Guide, pp. 83–84, 97, 100); IX, §41 (p. 363)"
        },
        "seeAlso": ["diṭṭhigatavippayutta", "diṭṭhi", "lobha", "aniyatayogī"]
    },

    "dosa": {
        "meaning": {
            "pt": "Ódio; aversão (paṭigha); má vontade (vyāpāda); raiva; a segunda raiz prejudicial (akusalahetu), presente exclusivamente nos 2 cittas enraizados no ódio (dosamūlacittāni).",
            "en": "Hatred; aversion (paṭigha); ill will (vyāpāda); anger; the second unwholesome root (akusalahetu), present exclusively in the 2 hatred-rooted cittas (dosamūlacittāni).",
            "es": "Odio; aversión (paṭigha); mala voluntad (vyāpāda); ira; la segunda raíz perjudicial (akusalahetu), presente exclusivamente en los 2 cittas enraizados en el odio (dosamūlacittāni)."
        },
        "grammar": "masc. (de √dus + *a)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (derivado da raiz √dus 'corromper-se, irar-se, odiar')",
            "en": "Masculine noun (derived from root √dus 'to be corrupted, angered, hate')",
            "es": "Sustantivo masculino (derivado de la raíz √dus 'corromperse, airarse, odiar')"
        },
        "root": "√dus (odiar / irritar-se) + *a",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Prejudicial (Cetasika #21 de 52) & 2ª Raiz Prejudicial",
                "en": "Ultimate Reality — Unwholesome Mental Factor (Cetasika #21 of 52) & 2nd Unwholesome Root",
                "es": "Realidad Última — Factor Mental Perjudicial (Cetasika #21 de 52) y 2ª Raíz Perjudicial"
            },
            "category": {
                "pt": "Quarteto do Ódio (Dosacatukka — presente nos 2 Dosamūlacittāni: #9 e #10); idêntico a Paṭigha e Vyāpāda; erradicado no Anāgāmimagga",
                "en": "Hatred Quartet (Dosacatukka — present in the 2 Dosamūlacittāni: #9 and #10); identical with Paṭigha and Vyāpāda; eradicated at Anāgāmimagga",
                "es": "Cuarteto del Odio (Dosacatukka — presente en los 2 Dosamūlacittāni: #9 y #10); idéntico a Paṭigha y Vyāpāda; erradicado en Anāgāmimagga"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Ferocidade ou aspereza agressiva (caṇḍikka-lakkhaṇa), como uma cobra venenosa golpeada com um bastão.",
                    "en": "Ferocity or savageness (caṇḍikka-lakkhaṇa), like a provoked venomous snake.",
                    "es": "Ferocidad o aspereza agresiva (caṇḍikka-lakkhaṇa), como una serpiente venenosa provocada."
                },
                "rasa": {
                    "pt": "Espalhar-se (visappana-rasa, como veneno no corpo) ou queimar e consumir seu próprio suporte psicofísico (attano nissayadahana-rasa), como um incêndio florestal.",
                    "en": "To spread (visappana-rasa, like poison) or to burn up its own mind-and-body support (attano nissayadahana-rasa), like a forest fire.",
                    "es": "Esparcirse (visappana-rasa, como veneno) o quemar su propio soporte psicofísico (attano nissayadahana-rasa), como un incendio forestal."
                },
                "paccupatthana": {
                    "pt": "Perseguir, ofender ou destruir (dūsana-paccupaṭṭhāna), como um inimigo que encontra oportunidade.",
                    "en": "Persecuting or offending (dūsana-paccupaṭṭhāna), like an enemy who has found an opportunity.",
                    "es": "Perseguir, ofender o destruir (dūsana-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Uma das nove bases para irritação ou ressentimento (āghātavatthu-padaṭṭhāna).",
                    "en": "One of the nine grounds for annoyance or malice (āghātavatthu-padaṭṭhāna).",
                    "es": "Una de las nueve bases de irritación o malicia (āghātavatthu-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Como explica Bhikkhu Bodhi (CMA I, §5 & II, §4, p. 84), dosa abrange todas as gradações de aversão: fúria, rancor, hostilidade, irritação, tristeza, medo e tédio aversivo. Surge sempre acompanhado pela sensação de desprazer mental (domanassa). No quarteto do ódio (dosa, issā, macchariya, kukkucca), dosa é fixo nos 2 dosamūlacittas, enquanto inveja (issā), avareza (macchariya) e remorso (kukkucca) são adjunctos ocasionais que nunca surgem juntos no mesmo momento mental.",
                "en": "As Bhikkhu Bodhi explains (CMA I, §5 & II, §4, p. 84), dosa comprises all degrees of aversion: rage, ill will, anger, irritation, grief, fear, and aversive boredom. It always arises accompanied by unpleasant mental feeling (domanassa). In the hatred quartet (dosa, issā, macchariya, kukkucca), dosa is fixed in both dosamūlacittas, while envy (issā), avarice (macchariya), and worry (kukkucca) are unfixed adjuncts that can never arise simultaneously.",
                "es": "Como explica Bhikkhu Bodhi (CMA I, §5 y II, §4, p. 84), dosa abarca todos los grados de aversión y surge siempre con sensación mental desagradable (domanassa). En el cuarteto del odio (dosa, issā, macchariya, kukkucca), dosa es fijo mientras los otros tres surgen por separado."
            },
            "bodhiRef": "CMA I, §5 (Guide, pp. 37–38); II, §4, §13 & §17 (pp. 84, 97, 100)"
        },
        "seeAlso": ["adosa", "mettā", "paṭighasampayutta", "domanassa", "issā", "macchariya", "kukkucca"]
    },

    "issā": {
        "meaning": {
            "pt": "Inveja; ciúme; fator mental prejudicial ocasional caracterizado pelo descontentamento e ressentimento perante o sucesso, honra ou prosperidade alheia (surge apenas nos 2 dosamūlacittas).",
            "en": "Envy; jealousy; an occasional unwholesome mental factor characterized by dissatisfaction and resentment at others' success, honor, or prosperity (arising only in the 2 dosamūlacittas).",
            "es": "Envidia; celos; factor mental perjudicial ocasional caracterizado por el descontento y resentimiento ante el éxito o prosperidad ajena (surge solo en los 2 dosamūlacittas)."
        },
        "grammar": "fem. (de √iss + ā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (derivado da raiz √iss 'invejar')",
            "en": "Feminine noun (derived from root √iss 'to envy')",
            "es": "Sustantivo femenino (derivado de la raíz √iss 'envidiar')"
        },
        "root": "√iss (invejar / ressentir-se) + ā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Prejudicial Ocasional (Cetasika #22 de 52)",
                "en": "Ultimate Reality — Occasional Unwholesome Mental Factor (Cetasika #22 of 52)",
                "es": "Realidad Última — Factor Mental Perjudicial Ocasional (Cetasika #22 de 52)"
            },
            "category": {
                "pt": "Quarteto do Ódio (Dosacatukka — aniyatayogī nos 2 Dosamūlacittāni); Erradicado no Sotāpatti-magga; oposto de Muditā",
                "en": "Hatred Quartet (Dosacatukka — unfixed adjunct in the 2 Dosamūlacittāni); Eradicated at Sotāpatti-magga; opposite of Muditā",
                "es": "Cuarteto del Odio (Dosacatukka — adjunto no fijo en los 2 Dosamūlacittāni); Erradicado en Sotāpatti-magga; opuesto de Muditā"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Ter ciúme ou inveja do sucesso e das conquistas dos outros (parasampattīsu usūyana-lakkhaṇa).",
                    "en": "Being jealous of others' success and prosperity (parasampattīsu usūyana-lakkhaṇa).",
                    "es": "Sentir celos o envidia del éxito y prosperidad de los demás (parasampattīsu usūyana-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Estar insatisfeito ou descontente com o sucesso alheio (tattheva anabhirati-rasa).",
                    "en": "To be dissatisfied with others' success (tattheva anabhirati-rasa).",
                    "es": "Estar insatisfecho con el éxito ajeno (tattheva anabhirati-rasa)."
                },
                "paccupatthana": {
                    "pt": "Virar as costas ou ter aversão a esse sucesso alheio (tato vimukhabhāva-paccupaṭṭhāna).",
                    "en": "Turning one's face away from or aversion towards others' success (tato vimukhabhāva-paccupaṭṭhāna).",
                    "es": "Dar la espalda o sentir aversión hacia el éxito ajeno (tato vimukhabhāva-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O sucesso ou prosperidade dos outros (parasampatti-padaṭṭhāna).",
                    "en": "Others' success or prosperity (parasampatti-padaṭṭhāna).",
                    "es": "El éxito o prosperidad de los demás (parasampatti-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Embora tanto issā quanto macchariya surjam nos 2 dosamūlacittas, nunca surgem no mesmo momento mental porque seus objetos são opostos: issā toma como objeto a prosperidade dos outros (parasampatti), enquanto macchariya toma como objeto a própria prosperidade (attasampatti). Seu antídoto direto é a alegria altruísta (muditā). Tanto issā quanto macchariya são erradicados já no primeiro caminho supramundano (sotāpattimagga — CMA IX, §38).",
                "en": "Although both issā and macchariya arise in the 2 dosamūlacittas, they never arise simultaneously because their objects are opposite: issā takes others' success (parasampatti) as object, whereas macchariya takes one's own success (attasampatti) as object. Its direct antidote is appreciative joy (muditā). Both issā and macchariya are eradicated at the very first supramundane path (sotāpattimagga — CMA IX, §38).",
                "es": "Aunque issā y macchariya surgen en los 2 dosamūlacittas, nunca coexisten en el mismo momento mental: issā toma como objeto el éxito ajeno (parasampatti) y macchariya el éxito propio (attasampatti). Su antídoto directo es muditā."
            },
            "bodhiRef": "CMA II, §4, §13 & §17 (Guide, pp. 84, 97, 100); IX, §38 (p. 361)"
        },
        "seeAlso": ["macchariya", "kukkucca", "dosa", "muditā"]
    },

    "macchariya": {
        "meaning": {
            "pt": "Avareza; mesquinhez; egoísmo possessivo; fator mental prejudicial ocasional caracterizado por ocultar o próprio sucesso ou posses e não suportar compartilhá-los com outros (surge apenas nos 2 dosamūlacittas).",
            "en": "Avarice; stinginess; meanness; an occasional unwholesome mental factor characterized by concealing one's own success or possessions and not bearing to share them with others (arising only in the 2 dosamūlacittas).",
            "es": "Avaricia; mezquindad; tacañería; factor mental perjudicial ocasional caracterizado por ocultar el propio éxito o posesiones y no soportar compartirlos con otros (surge solo en los 2 dosamūlacittas)."
        },
        "grammar": "nt. (de macchara + ya)",
        "grammarLocalized": {
            "pt": "Substantivo neutro abstrato (macchara 'avarento' + -ya)",
            "en": "Abstract neuter noun (macchara 'stingy' + -ya)",
            "es": "Sustantivo neutro abstracto (macchara 'avaro' + -ya)"
        },
        "root": "macchara (avarento) + ya",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Prejudicial Ocasional (Cetasika #23 de 52)",
                "en": "Ultimate Reality — Occasional Unwholesome Mental Factor (Cetasika #23 of 52)",
                "es": "Realidad Última — Factor Mental Perjudicial Ocasional (Cetasika #23 de 52)"
            },
            "category": {
                "pt": "Quarteto do Ódio (Dosacatukka — aniyatayogī nos 2 Dosamūlacittāni); Erradicado no Sotāpatti-magga; oposto de Dāna / Alobha",
                "en": "Hatred Quartet (Dosacatukka — unfixed adjunct in the 2 Dosamūlacittāni); Eradicated at Sotāpatti-magga; opposite of Dāna / Alobha",
                "es": "Cuarteto del Odio (Dosacatukka — adjunto no fijo en los 2 Dosamūlacittāni); Erradicado en Sotāpatti-magga; opuesto de Dāna / Alobha"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Ocultar o próprio sucesso ou bens já obtidos ou prestes a serem obtidos (laddhānaṃ vā labhitabbānaṃ vā attano sampattīnaṃ nigūhana-lakkhaṇa).",
                    "en": "Concealing one's own success or possessions when obtained or about to be obtained (attano sampattīnaṃ nigūhana-lakkhaṇa).",
                    "es": "Ocultar el propio éxito o posesiones obtenidas o por obtener (attano sampattīnaṃ nigūhana-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Não suportar compartilhá-los com os outros ('que isto pertença só a mim e a mais ninguém' — parehi sādhāraṇabhāva-akkhamaṇa-rasa).",
                    "en": "Not bearing to share them with others ('may this belong to me alone and not to others' — parehi sādhāraṇabhāva-akkhamaṇa-rasa).",
                    "es": "No soportar compartirlos con otros (parehi sādhāraṇabhāva-akkhamaṇa-rasa)."
                },
                "paccupatthana": {
                    "pt": "Encolher-se perante o ato de compartilhar (saṅkocanabhāva-paccupaṭṭhāna) ou amargura mesquinha (kaṭukañcukatā).",
                    "en": "Shrinking away from sharing (saṅkocanabhāva-paccupaṭṭhāna) and meanness or sour feeling (kaṭukañcukatā).",
                    "es": "Encogerse ante el compartir (saṅkocanabhāva-paccupaṭṭhāna) y amargura mezquina (kaṭukañcukatā)."
                },
                "padatthana": {
                    "pt": "O próprio sucesso ou bens (attasampatti-padaṭṭhāna).",
                    "en": "One's own success or possessions (attasampatti-padaṭṭhāna).",
                    "es": "El propio éxito o posesiones (attasampatti-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Ponto técnico sutil do Abhidhamma: embora no senso comum a avareza pareça cobiça, no Abhidhamma macchariya NÃO pertence aos cittas de cobiça (lobhamūla), mas sim aos 2 cittas de ódio/aversão (dosamūla)! Enquanto o apego às próprias posses é lobha, a repulsa hostil à ideia de que outra pessoa usufrua delas ('que ninguém toque no que é meu!') é macchariya, acompanhada de domanassa e dosa. Os Comentários enumeram 5 tipos de macchariya: quanto à moradia (āvāsa), famílias de apoiadores (kula), ganhos materiais (lābha), beleza/elogio (vaṇṇa) e conhecimento do Dhamma (dhamma).",
                "en": "Subtle technical point of the Abhidhamma: although in ordinary usage stinginess seems like greed, in the Abhidhamma macchariya does NOT belong to greed-rooted cittas (lobhamūla), but to the 2 hatred-rooted cittas (dosamūla)! While attachment to one's possessions is lobha, the hostile shrinking away from letting others share in them ('may no one else have what is mine!') is macchariya, accompanied by domanassa and dosa. The Commentaries list 5 kinds of macchariya: regarding dwellings (āvāsa), families (kula), gains (lābha), praise/beauty (vaṇṇa), and Dhamma knowledge (dhamma).",
                "es": "Punto técnico sutil del Abhidhamma: aunque la avaricia parezca codicia, en el Abhidhamma macchariya NO pertenece a los cittas de codicia (lobhamūla), sino a los 2 cittas de odio (dosamūla): mientras el apego a lo propio es lobha, el rechazo hostil a compartirlo con otros es macchariya."
            },
            "bodhiRef": "CMA II, §4, §13 & §17 (Guide, pp. 84, 97, 100); IX, §38 (p. 361)"
        },
        "seeAlso": ["issā", "kukkucca", "dosa", "alobha", "dāna"]
    },

    "kukkucca": {
        "meaning": {
            "pt": "Remorso; preocupação aflitiva; inquietação da consciência; fator mental prejudicial ocasional que se angustia sobre o mal que foi feito e o bem que deixou de ser feito (surge apenas nos 2 dosamūlacittas).",
            "en": "Worry; remorse; scruples; an occasional unwholesome mental factor that sorrows over evil done and good left undone (arising only in the 2 dosamūlacittas).",
            "es": "Remordimiento; preocupación aflictiva; factor mental perjudicial ocasional que se aflige por el mal hecho y el bien no hecho (surge solo en los 2 dosamūlacittas)."
        },
        "grammar": "nt. (de kukata + ya)",
        "grammarLocalized": {
            "pt": "Substantivo neutro abstrato (kukata 'malfeito' + -ya > kukkucca)",
            "en": "Abstract neuter noun (kukata 'wrongly done' + -ya > kukkucca)",
            "es": "Sustantivo neutro abstracto (kukata 'mal hecho' + -ya > kukkucca)"
        },
        "root": "ku (mal) + √kar (fazer) + ta + ya",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Prejudicial Ocasional (Cetasika #24 de 52)",
                "en": "Ultimate Reality — Occasional Unwholesome Mental Factor (Cetasika #24 of 52)",
                "es": "Realidad Última — Factor Mental Perjudicial Ocasional (Cetasika #24 de 52)"
            },
            "category": {
                "pt": "Quarteto do Ódio (Dosacatukka — aniyatayogī nos 2 Dosamūlacittāni); Obstáculo (Uddhacca-kukkucca Nīvaraṇa); Erradicado no Anāgāmimagga",
                "en": "Hatred Quartet (Dosacatukka — unfixed adjunct in the 2 Dosamūlacittāni); Hindrance (Uddhacca-kukkucca Nīvaraṇa); Eradicated at Anāgāmimagga",
                "es": "Cuarteto del Odio (Dosacatukka — adjunto no fijo en los 2 Dosamūlacittāni); Obstáculo (Uddhacca-kukkucca Nīvaraṇa); Erradicado en Anāgāmimagga"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Arrependimento ou pesar subsequente (pacchānutāpa-lakkhaṇa).",
                    "en": "Subsequent regret (pacchānutāpa-lakkhaṇa).",
                    "es": "Arrepentimiento o pesar subsiguiente (pacchānutāpa-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Afligir-se pelo que foi feito de errado e pelo que deixou de ser feito de bom (katākatānusocana-rasa).",
                    "en": "To sorrow over what has and what has not been done (katākatānusocana-rasa).",
                    "es": "Afligirse por lo que se ha hecho y lo que se ha dejado de hacer (katākatānusocana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Remorso na mente (vippaṭisāra-paccupaṭṭhāna).",
                    "en": "Remorse (vippaṭisāra-paccupaṭṭhāna).",
                    "es": "Remordimiento (vippaṭisāra-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Faltas de comissão e omissão (katākata-padaṭṭhāna — o mal cometido e o bem omitido).",
                    "en": "Wrongs of commission and omission (katākata-padaṭṭhāna — what has and has not been done).",
                    "es": "Faltas de comisión y omisión (katākata-padaṭṭhāna — lo hecho y lo no hecho)."
                }
            },
            "philosophy": {
                "pt": "No Abhidhamma, o remorso (kukkucca) nunca é considerado uma virtude salutar, pois é sempre acompanhado de desprazer mental (domanassa) e aversão (dosa), perturbando a paz da mente e constituindo, junto com uddhacca, o quarto obstáculo à meditação (uddhacca-kukkucca-nīvaraṇa). A resolução sábia de corrigir uma falha futura não é kukkucca, mas hiri-ottappa e paññā em um citta kusala. Kukkucca é erradicado junto com dosa pelo caminho do não-retorno (anāgāmimagga).",
                "en": "In the Abhidhamma, remorse (kukkucca) is never regarded as a wholesome virtue, because it is always accompanied by mental displeasure (domanassa) and aversion (dosa), agitating the mind and forming, with uddhacca, the fourth hindrance to meditation (uddhacca-kukkucca-nīvaraṇa). The wise resolve to refrain from future faults is not kukkucca, but hiri-ottappa and paññā in a kusala citta. Kukkucca is eradicated together with dosa by the path of non-returning (anāgāmimagga).",
                "es": "En el Abhidhamma, el remordimiento (kukkucca) nunca se considera un estado saludable, pues siempre surge con desagrado mental (domanassa) y aversión (dosa), formando junto con uddhacca el cuarto obstáculo meditativo. Es erradicado por el camino del no-retorno (anāgāmimagga)."
            },
            "bodhiRef": "CMA II, §4, §13 & §17 (Guide, pp. 84, 97, 100); IX, §40 (p. 362)"
        },
        "seeAlso": ["dosa", "issā", "macchariya", "uddhacca", "nīvaraṇa"]
    },

    "thīna": {
        "meaning": {
            "pt": "Torpor; indolência da consciência (cittagelañña); fator mental prejudicial ocasional que embota a consciência e dissipa a energia (surge sempre em par com middha apenas nos 5 cittas akusala induzidos, sasaṅkhārika).",
            "en": "Sloth; sluggishness or dullness of consciousness (cittagelañña); an occasional unwholesome mental factor that dulls citta and dispels energy (always arising paired with middha solely in the 5 prompted akusala cittas, sasaṅkhārika).",
            "es": "Pereza; embotamiento de la conciencia (cittagelañña); factor mental perjudicial ocasional que embota el citta y disipa la energía (surge siempre en par con middha únicamente en los 5 cittas akusala instigados, sasaṅkhārika)."
        },
        "grammar": "nt.",
        "grammarLocalized": {
            "pt": "Substantivo neutro (derivado de √thī 'contrair, coagular, endurecer')",
            "en": "Neuter noun (derived from √thī 'to congeal, stiffen, contract')",
            "es": "Sustantivo neutro (derivado de √thī 'contraerse, entumecerse')"
        },
        "root": "√thī (contrair / estagnar) + na",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Prejudicial Ocasional (Cetasika #25 de 52)",
                "en": "Ultimate Reality — Occasional Unwholesome Mental Factor (Cetasika #25 of 52)",
                "es": "Realidad Última — Factor Mental Perjudicial Ocasional (Cetasika #25 de 52)"
            },
            "category": {
                "pt": "Díade de Torpor e Languidez (Thīnaduka — aniyatayogī nos 5 Cittas Akusala Sasaṅkhārika: #2, #4, #6, #8, #10); 3º Obstáculo (Thīnamiddha Nīvaraṇa)",
                "en": "Sloth-and-Torpor Dyad (Thīnaduka — unfixed adjunct in the 5 Sasaṅkhārika Akusala Cittas: #2, #4, #6, #8, #10); 3rd Hindrance (Thīnamiddha Nīvaraṇa)",
                "es": "Díada de Pereza y Torpor (Thīnaduka — adjunto no fijo en los 5 Cittas Akusala Sasaṅkhārika: #2, #4, #6, #8, #10); 3º Obstáculo (Thīnamiddha Nīvaraṇa)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Falta de impulso ou força motriz (anussāhana-lakkhaṇa).",
                    "en": "Lack of driving power (anussāhana-lakkhaṇa).",
                    "es": "Falta de impulso o fuerza motriz (anussāhana-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Dissipar ou remover a energia (viriyavinodana-rasa).",
                    "en": "To dispel or remove energy (viriyavinodana-rasa).",
                    "es": "Disipar o eliminar la energía (viriyavinodana-rasa)."
                },
                "paccupatthana": {
                    "pt": "O afundamento ou abatimento da mente (saṃsīdana-paccupaṭṭhāna).",
                    "en": "The sinking of the mind (saṃsīdana-paccupaṭṭhāna).",
                    "es": "El hundimiento o abatimiento de la mente (saṃsīdana-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Atenção insensata ao tédio, preguiça, sonolência, etc. (arati-tandī-vijambhikādīsu ayonisomanasikāra-padaṭṭhāna).",
                    "en": "Unwise attention to boredom, drowsiness, stretching, etc. (arati-tandī-vijambhikādīsu ayonisomanasikāra-padaṭṭhāna).",
                    "es": "Atención insensata al tedio, somnolencia, pereza, etc. (arati-tandī-vijambhikādīsu ayonisomanasikāra-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Como explica Bhikkhu Bodhi (CMA II, §4, p. 84), thīna e middha ocorrem sempre juntos (sahajāta) nos 5 cittas akusala induzidos (sasaṅkhārika) e opõem-se diretamente à energia (viriya). Thīna é identificado como a enfermidade da consciência (cittagelañña), enquanto middha é a enfermidade do corpo mental dos fatores mentais (kāyagelañña). Como par, constituem um dos cinco obstáculos (thīnamiddha-nīvaraṇa), superado em jhāna pela aplicação inicial (vitakka) e erradicado definitivamente pelo caminho do Arahant.",
                "en": "As Bhikkhu Bodhi explains (CMA II, §4, p. 84), thīna and middha always occur in conjunction in the 5 prompted (sasaṅkhārika) akusala cittas and are directly opposed to energy (viriya). Thīna is identified as sickness of consciousness (cittagelañña), while middha is sickness of the mental factors (kāyagelañña). Together they form one of the five hindrances, countered in jhāna by initial application (vitakka) and eradicated by the path of Arahantship.",
                "es": "Como explica Bhikkhu Bodhi (CMA II, §4, p. 84), thīna y middha siempre ocurren juntos en los 5 cittas akusala instigados (sasaṅkhārika) y se oponen directamente a la energía (viriya). Thīna es la enfermedad de la conciencia (cittagelañña) y middha la enfermedad de los factores mentales (kāyagelañña)."
            },
            "bodhiRef": "CMA II, §4, §13 & §17 (Guide, pp. 84–85, 97, 100); IX, §41 (p. 363)"
        },
        "seeAlso": ["middha", "sasaṅkhārika", "viriya", "vitakka", "lahutā", "nīvaraṇa"]
    },

    "middha": {
        "meaning": {
            "pt": "Languidez; torpor dos fatores mentais (kāyagelañña); morbidez e inaptidão do corpo mental que sufoca os concomitantes (surge sempre em par com thīna apenas nos 5 cittas akusala induzidos, sasaṅkhārika).",
            "en": "Torpor; morbid unwieldiness of the mental factors (kāyagelañña); mental sluggishness that smothers its concomitants (always arising paired with thīna solely in the 5 prompted akusala cittas, sasaṅkhārika).",
            "es": "Torpor; languidez de los factores mentales (kāyagelañña); estado mórbido que sofoca los concomitantes (surge siempre en par con thīna únicamente en los 5 cittas akusala instigados, sasaṅkhārika)."
        },
        "grammar": "nt.",
        "grammarLocalized": {
            "pt": "Substantivo neutro (sempre associado a thīna na díade thīnamiddha)",
            "en": "Neuter noun (always paired with thīna in the dyad thīnamiddha)",
            "es": "Sustantivo neutro (siempre emparejado con thīna en la díada thīnamiddha)"
        },
        "root": "√midh (ser inapto / entorpecer) + a",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Prejudicial Ocasional (Cetasika #26 de 52)",
                "en": "Ultimate Reality — Occasional Unwholesome Mental Factor (Cetasika #26 of 52)",
                "es": "Realidad Última — Factor Mental Perjudicial Ocasional (Cetasika #26 de 52)"
            },
            "category": {
                "pt": "Díade de Torpor e Languidez (Thīnaduka — aniyatayogī nos 5 Cittas Akusala Sasaṅkhārika); 3º Obstáculo (Thīnamiddha Nīvaraṇa)",
                "en": "Sloth-and-Torpor Dyad (Thīnaduka — unfixed adjunct in the 5 Sasaṅkhārika Akusala Cittas); 3rd Hindrance (Thīnamiddha Nīvaraṇa)",
                "es": "Díada de Pereza y Torpor (Thīnaduka — adjunto no fijo en los 5 Cittas Akusala Sasaṅkhārika); 3º Obstáculo (Thīnamiddha Nīvaraṇa)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Inaptidão ou falta de maleabilidade funcional do corpo mental (akammaññatā-lakkhaṇa).",
                    "en": "Unwieldiness of the mental body (akammaññatā-lakkhaṇa).",
                    "es": "Falta de manejabilidad del cuerpo mental (akammaññatā-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Sufocar, obstruir ou encerrar os fatores mentais associados (onāhana-rasa).",
                    "en": "To smother or enclose the associated mental factors (onāhana-rasa).",
                    "es": "Sofocar o encerrar los factores mentales asociados (onāhana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Pender, cabecear e sonolência (līnatta-paccupaṭṭhāna / pacalāyikāmiddha-paccupaṭṭhāna).",
                    "en": "Drooping, or nodding and sleepiness (līnatta-paccupaṭṭhāna / pacalāyikāmiddha-paccupaṭṭhāna).",
                    "es": "Decaimiento, cabeceo y somnolencia (līnatta-paccupaṭṭhāna / pacalāyikāmiddha-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "A mesma causa próxima de thīna: atenção insensata ao tédio, preguiça e sonolência.",
                    "en": "The same proximate cause as sloth: unwise attention to boredom, drowsiness, etc.",
                    "es": "La misma causa próxima que thīna: atención insensata al tedio y la somnolencia."
                }
            },
            "philosophy": {
                "pt": "Nota importante da tradição Theravāda: embora middha se manifeste como cabecear e sonolência, o cansaço meramente fisiológico do corpo físico (que ocorre inclusive em Buddhas e Arahants após longas caminhadas ou jejuns) não é o cetasika akusala middha, mas apenas enfraquecimento dos grupos materiais (rūpakalāpa). O cetasika middha é estritamente uma morbidez mental prejudicial (kāyagelañña) que só ocorre em cittas akusala sasaṅkhārika e é erradicado no Arahattamagga.",
                "en": "Important note in the Theravāda tradition: although middha manifests as nodding and sleepiness, purely physiological fatigue of the physical body (which occurs even in Buddhas and Arahants) is not the unwholesome cetasika middha, but a weakening of material groups (rūpakalāpa). The cetasika middha is strictly a morbid state of the mental factors (kāyagelañña) occurring only in sasaṅkhārika akusala cittas and eradicated at Arahattamagga.",
                "es": "Nota importante de la tradición Theravāda: el cansancio puramente fisiológico del cuerpo físico (que ocurre incluso en Buddhas y Arahants) no es el cetasika akusala middha, sino debilitamiento de los grupos materiales. El cetasika middha es estrictamente una morbidez de los factores mentales (kāyagelañña) en los cittas akusala sasaṅkhārika."
            },
            "bodhiRef": "CMA II, §4, §13 & §17 (Guide, pp. 84–85, 97, 100)"
        },
        "seeAlso": ["thīna", "sasaṅkhārika", "kammaññatā", "lahutā", "viriya"]
    },

    "vicikicchā": {
        "meaning": {
            "pt": "Dúvida espiritual; perplexidade cética; indecisão; o 14º fator mental prejudicial, caracterizado pela incapacidade de depositar confiança no Buddha, no Dhamma, na Saṅgha e na condicionalidade (surge apenas no 1º mohamūlacitta).",
            "en": "Spiritual doubt; skeptical perplexity; indecisiveness; the 14th unwholesome mental factor, characterized by the inability to place confidence in the Buddha, Dhamma, Saṅgha, and conditionality (arising solely in the 1st mohamūlacitta).",
            "es": "Duda espiritual; perplejidad escéptica; indecisión; el 14º factor mental perjudicial, caracterizado por la incapacidad de depositar confianza en el Buddha, el Dhamma, la Saṅgha y la condicionalidad (surge solo en el 1º mohamūlacitta)."
        },
        "grammar": "fem.",
        "grammarLocalized": {
            "pt": "Substantivo feminino (desiderativo de √cit / √kicch 'estar perplexo ao investigar' ou vi + cikicchā)",
            "en": "Feminine noun (desiderative of √cit / √kicch 'to be vexed in inquiring' or vi + cikicchā)",
            "es": "Sustantivo femenino (desiderativo de √cit / √kicch 'atormentarse al indagar' o vi + cikicchā)"
        },
        "root": "vi + √cit / √kicch + ā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Prejudicial Ocasional (Cetasika #27 de 52)",
                "en": "Ultimate Reality — Occasional Unwholesome Mental Factor (Cetasika #27 of 52)",
                "es": "Realidad Última — Factor Mental Perjudicial Ocasional (Cetasika #27 de 52)"
            },
            "category": {
                "pt": "Exclusivo do 1º Mohamūlacitta (Vicikicchāsampayutta — Citta #11); 5º Obstáculo (Nīvaraṇa); 2º Grilhão (Saṃyojana); Erradicado no Sotāpatti-magga",
                "en": "Exclusive to the 1st Mohamūlacitta (Vicikicchāsampayutta — Citta #11); 5th Hindrance (Nīvaraṇa); 2nd Fetter (Saṃyojana); Eradicated at Sotāpatti-magga",
                "es": "Exclusivo del 1º Mohamūlacitta (Vicikicchāsampayutta — Citta #11); 5º Obstáculo (Nīvaraṇa); 2ª Traba (Saṃyojana); Erradicado en Sotāpatti-magga"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Duvidar ou estar perplexo (saṃsayana-lakkhaṇa).",
                    "en": "Doubting or perplexity (saṃsayana-lakkhaṇa).",
                    "es": "Dudar o estar perplejo (saṃsayana-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Vacilar ou oscilar mentalmente (kampana-rasa).",
                    "en": "To waver or vacillate (kampana-rasa).",
                    "es": "Vacilar u oscilar mentalmente (kampana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Indecisão (aniścaya-paccupaṭṭhāna) e tomar vários lados sem se fixar em nenhum (anekamsaggāha-paccupaṭṭhāna).",
                    "en": "Indecisiveness (anicchaya-paccupaṭṭhāna) and taking various sides without settling (anekamsaggāha-paccupaṭṭhāna).",
                    "es": "Indecisión (anicchaya-paccupaṭṭhāna) y tomar varios lados sin decidirse (anekamsaggāha-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Atenção insensata às coisas que dão margem à dúvida (vicikicchāṭṭhāniyesu dhammesu ayonisomanasikāra-padaṭṭhāna).",
                    "en": "Unwise attention to matters that offer ground for doubt (ayonisomanasikāra-padaṭṭhāna).",
                    "es": "Atención insensata a los asuntos que dan pie a la duda (ayonisomanasikāra-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Comparado nos Comentários a um viajante perdido numa encruzilhada no deserto que hesita sem saber qual caminho seguir. Não é a dúvida investigativa saudável ou curiosidade intelectual, mas a paralisia cética perante as 8 bases (Buddha, Dhamma, Saṅgha, o treinamento, o passado, o futuro, ambos, e o paṭiccasamuppāda). É superada temporariamente pela 4ª purificação de insight (kaṅkhāvitaraṇavisuddhi, o conhecimento que discerne as condições de nāmarūpa, Cap. IX, §31) e erradicada definitivamente pelo caminho de entrada na correnteza (sotāpattimagga).",
                "en": "Compared in the Commentaries to a traveler at a crossroads in a desert who hesitates, unable to decide which path to take. It is not healthy investigative inquiry, but skeptical paralysis regarding the 8 grounds (Buddha, Dhamma, Saṅgha, the training, the past, the future, both, and Dependent Arising). It is temporarily overcome by the 4th purification (kaṅkhāvitaraṇavisuddhi, discerning the conditions of nāmarūpa, Ch. IX, §31) and permanently eradicated at stream-entry (sotāpattimagga).",
                "es": "Comparado en los Comentarios a un viajero perdido en una encrucijada en el desierto que vacila sin saber qué camino tomar. Se supera temporalmente en la 4ª purificación (kaṅkhāvitaraṇavisuddhi) y se erradica definitivamente en sotāpattimagga."
            },
            "bodhiRef": "CMA I, §6 (Guide, pp. 38–39); II, §4 & §13 (pp. 85, 98); IX, §31 & §38 (pp. 350, 361)"
        },
        "seeAlso": ["vicikicchāsampayutta", "adhimokkha", "saddhā", "paññā", "vicāra"]
    },

    # ── 25 FATORES BELOS (SOBHANACETASIKA) ───────────────────────────────────
    "sobhanasādhāraṇa": {
        "meaning": {
            "pt": "Universais belos; os 19 fatores mentais belos que estão invariavelmente presentes em todos os 59 ou 91 tipos de consciência bela (sobhanacittāni).",
            "en": "Universal beautiful factors; the 19 beautiful mental factors that are invariably present in all 59 or 91 types of beautiful consciousness (sobhanacittāni).",
            "es": "Factores hermosos universales; los 19 factores mentales hermosos que están invariablemente presentes en todos los 59 o 91 tipos de conciencia hermosa (sobhanacittāni)."
        },
        "grammar": "masc. pl. / adj. (Tappurisa / Kammadhāraya)",
        "grammarLocalized": {
            "pt": "Adjetivo / Substantivo masculino plural (sobhana + sādhāraṇa)",
            "en": "Adjective / Masculine plural noun (sobhana + sādhāraṇa)",
            "es": "Adjetivo / Sustantivo masculino plural (sobhana + sādhāraṇa)"
        },
        "root": "√subh (brilhar) + ana + sa + ā + √dhar + aṇa",
        "samasa": {
            "breakdown": "sobhana + sādhāraṇa",
            "type": {
                "pt": "Chaṭṭhī-Tappurisa Samāsa (Composto Determinativo Genitivo)",
                "en": "Chaṭṭhī-Tappurisa Samāsa (Genitive Determinative Compound)",
                "es": "Chaṭṭhī-Tappurisa Samāsa (Compuesto Determinativo Genitivo)"
            },
            "viggaha": "sobhanānaṃ cittānaṃ sādhāraṇā ti sobhanasādhāraṇā",
            "literal": {
                "pt": "Comuns a todas as consciências belas",
                "en": "Common to all beautiful consciousnesses",
                "es": "Comunes a todas las conciencias hermosas"
            },
            "parts": [
                {"pali": "sobhana", "gloss": {"pt": "belo / radiante", "en": "beautiful", "es": "hermoso"}},
                {"pali": "sādhāraṇa", "gloss": {"pt": "comum / universal", "en": "common / universal", "es": "común / universal"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Classificação de Realidade Última (19 Cetasikas Universais Belos)",
                "en": "Classification of Ultimate Reality (19 Universal Beautiful Cetasikas)",
                "es": "Clasificación de Realidad Última (19 Cetasikas Hermosos Universales)"
            },
            "category": {
                "pt": "19 Sobhanasādhāraṇa: saddhā, sati, hiri, ottappa, alobha, adosa, tatramajjhattatā + os 6 pares de kāya/citta (passaddhi, lahutā, mudutā, kammaññatā, pāguññatā, ujjukatā)",
                "en": "19 Sobhanasādhāraṇa: saddhā, sati, hiri, ottappa, alobha, adosa, tatramajjhattatā + the 6 pairs of kāya/citta (passaddhi, lahutā, mudutā, kammaññatā, pāguññatā, ujjukatā)",
                "es": "19 Sobhanasādhāraṇa: saddhā, sati, hiri, ottappa, alobha, adosa, tatramajjhattatā + los 6 pares de kāya/citta (passaddhi, lahutā, mudutā, kammaññatā, pāguññatā, ujjukatā)"
            },
            "philosophy": {
                "pt": "Sempre que surge qualquer consciência bela — seja um simples ato de generosidade mundana, uma absorção meditativa (jhāna) ou a iluminação supramundana — estes 19 fatores mentais surgem simultaneamente como sua base luminosa mínima (junto com os 7 universais, totalizando no mínimo 26 cetasikas em qualquer citta belo).",
                "en": "Whenever any beautiful consciousness arises — whether a simple act of mundane generosity, a jhāna absorption, or supramundane enlightenment — these 19 mental factors arise simultaneously as its minimal luminous core (together with the 7 universals, making at least 26 cetasikas in every beautiful citta).",
                "es": "Siempre que surge cualquier conciencia hermosa, estos 19 factores mentales surgen simultáneamente como su núcleo luminoso mínimo."
            },
            "bodhiRef": "CMA II, §5 & §14 (Guide, pp. 85–88, 98–99)"
        },
        "seeAlso": ["sobhana", "saddhā", "sati", "hiri", "ottappa", "alobha", "adosa", "tatramajjhattatā"]
    },

    "saddhā": {
        "meaning": {
            "pt": "Fé; confiança serena e lúcida; convicção fundamentada no Buddha, no Dhamma, na Saṅgha e na lei de kamma; o 1º dos 19 fatores universais belos, que clarifica a mente como uma joia purificadora da água.",
            "en": "Faith; serene confidence; lucid trust placed in the Buddha, the Dhamma, the Saṅgha, and the law of kamma; the 1st of the 19 universal beautiful factors, which clarifies the mind like a water-clearing gem.",
            "es": "Fe; confianza serena y lúcida depositada en el Buddha, el Dhamma, la Saṅgha y la ley del kamma; el 1º de los 19 factores hermosos universales, que clarifica la mente como una gema purificadora del agua."
        },
        "grammar": "fem. (saddahati > saddhā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (prefixo sad/saddha 'coração/confiança' + raiz √dhā 'colocar, depositar')",
            "en": "Feminine noun (prefix sad/saddha 'heart/trust' + root √dhā 'to place, set')",
            "es": "Sustantivo femenino (prefijo sad/saddha 'corazón/confianza' + raíz √dhā 'colocar, depositar')"
        },
        "root": "sad + √dhā (depositar confiança) + a + ā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #28 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #28 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #28 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa — presente nos 59/91 sobhanacittas); Faculdade (Saddhindriya) e Poder (Saddhābala)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa — present in all 59/91 sobhanacittas); Faculty (Saddhindriya) and Power (Saddhābala)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa — presente en los 59/91 sobhanacittas); Facultad (Saddhindriya) y Poder (Saddhābala)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Depositar fé ou confiar (saddahana-lakkhaṇa / okappana-lakkhaṇa).",
                    "en": "Placing faith or trusting (saddahana-lakkhaṇa / okappana-lakkhaṇa).",
                    "es": "Depositar fe o confiar (saddahana-lakkhaṇa / okappana-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Clarificar os estados mentais associados (pasādana-rasa), como a gema purificadora do monarca universal faz decantar o lodo e torna a água límpida; ou lançar-se adiante (pakkhandana-rasa), como quem atravessa uma torrente.",
                    "en": "To clarify the associated states (pasādana-rasa), as a water-clearing gem causes muddy water to become clear; or to set forth (pakkhandana-rasa), as one sets forth to cross a flood.",
                    "es": "Clarificar los estados asociados (pasādana-rasa), como una gema purificadora aclara el agua turbia; o lanzarse adelante (pakkhandana-rasa), como quien cruza un torrente."
                },
                "paccupatthana": {
                    "pt": "Ausência de turvação ou nebulosidade mental (akālussiya-paccupaṭṭhāna) ou decisão resoluta (adhimutti-paccupaṭṭhāna).",
                    "en": "Non-fogginess (akālussiya-paccupaṭṭhāna), i.e., removal of mental impurities, or resolution (adhimutti-paccupaṭṭhāna).",
                    "es": "Ausencia de turbidez mental (akālussiya-paccupaṭṭhāna) o resolución (adhimutti-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Um objeto digno de confiança (saddheyya-vatthu-padaṭṭhāna, a Joia Tríplice) ou ouvir o Bom Dhamma (saddhammassavana) e os demais fatores de entrada na correnteza.",
                    "en": "An object worthy of faith (saddheyya-vatthu-padaṭṭhāna, the Triple Gem) or hearing the Good Dhamma (saddhammassavana), etc., constituting the factors of stream-entry.",
                    "es": "Un objeto digno de fe (saddheyya-vatthu-padaṭṭhāna, la Triple Joya) o escuchar el Buen Dhamma (saddhammassavana)."
                }
            },
            "philosophy": {
                "pt": "Na psicologia budista clássica (CMA II, §5, p. 86), saddhā não é crença cega dogmática, mas a clareza confiante (pasāda) que dissolve o lodo dos obstáculos mentais e inspira a ação corajosa rumo à libertação. Deve ser equilibrada com a sabedoria (paññā) nas cinco faculdades espirituais (indriyasamatta) para que a confiança não degenere em credulidade.",
                "en": "In classical Buddhist psychology (CMA II, §5, p. 86), saddhā is not blind dogmatic belief, but lucid confidence (pasāda) that settles the sediment of the hindrances and inspires courageous action toward liberation. It must be balanced with wisdom (paññā) among the five spiritual faculties (indriyasamatta).",
                "es": "En la psicología budista clásica (CMA II, §5, p. 86), saddhā no es creencia ciega, sino confianza lúcida (pasāda) que asienta el lodo de los obstáculos y debe equilibrarse con la sabiduría (paññā)."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 86); VII, §18 & §27–28 (pp. 275, 280)"
        },
        "seeAlso": ["paññā", "vicikicchā", "adhimokkha", "sati", "pāguññatā"]
    },

    "sati": {
        "meaning": {
            "pt": "Atenção plena; presença de espírito; vigilância lúcida; não-esquecimento (asammussanā) do objeto no momento presente; o 2º dos 19 fatores universais belos, 1º fator de iluminação e 7º fator do Nobre Caminho Óctuplo.",
            "en": "Mindfulness; presence of mind; lucid attentiveness to the present; non-forgetfulness (asammussanā) of the object; the 2nd of the 19 universal beautiful factors, 1st enlightenment factor, and 7th factor of the Noble Eightfold Path.",
            "es": "Atención plena; presencia de ánimo; vigilancia lúcida del presente; no olvido (asammussanā) del objeto; el 2º de los 19 factores hermosos universales, 1º factor de iluminación y 7º factor del Noble Camino Óctuple."
        },
        "grammar": "fem. (de √sar + ti)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (derivado da raiz √sar 'lembrar, manter presente na mente')",
            "en": "Feminine noun (derived from root √sar 'to remember, bear in mind')",
            "es": "Sustantivo femenino (derivado de la raíz √sar 'recordar, tener presente')"
        },
        "root": "√sar (lembrar / manter presente) + ti",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #29 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #29 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #29 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa — presente nos 59/91 sobhanacittas); aparece 8 vezes nas 37 Bodhipakkhiyā Dhammā (4 Satipaṭṭhāna, Satindriya, Satibala, Satisambojjhaṅga, Sammāsati)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa — present in all 59/91 sobhanacittas); appears 8 times in the 37 Requisites of Enlightenment (4 Satipaṭṭhāna, Satindriya, Satibala, Satisambojjhaṅga, Sammāsati)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa — presente en los 59/91 sobhanacittas); aparece 8 veces en los 37 Requisitos de la Iluminación (4 Satipaṭṭhāna, Satindriya, Satibala, Satisambojjhaṅga, Sammāsati)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Não flutuar ou não oscilar na superfície (apilāpana-lakkhaṇa) — mergulhar profundamente no objeto em vez de boiar como uma cabaça oca na água — e fazer o objeto presente.",
                    "en": "Not wobbling or not floating away from the object (apilāpana-lakkhaṇa) — plunging deeply into the object rather than bobbing on the surface like a hollow gourd — and keeping the object present.",
                    "es": "No flotar ni oscilar lejos del objeto (apilāpana-lakkhaṇa) — sumergirse profundamente en el objeto en vez de flotar como una calabaza hueca."
                },
                "rasa": {
                    "pt": "Ausência de confusão ou não-esquecimento (asammosa-rasa).",
                    "en": "Absence of confusion or non-forgetfulness (asammosa-rasa).",
                    "es": "Ausencia de confusión o no olvido (asammosa-rasa)."
                },
                "paccupatthana": {
                    "pt": "Guardião vigilante da porta dos sentidos (ārakkha-paccupaṭṭhāna) ou o estado de confrontar diretamente o campo objetivo face a face (visayābhimukhabhāva-paccupaṭṭhāna).",
                    "en": "Guardianship (ārakkha-paccupaṭṭhāna), or the state of confronting an objective field face-to-face (visayābhimukhabhāva-paccupaṭṭhāna).",
                    "es": "Custodia vigilante (ārakkha-paccupaṭṭhāna) o el estado de confrontar directamente el campo objetivo cara a cara (visayābhimukhabhāva-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Percepção firme (thirasaññā-padaṭṭhāna) ou os quatro fundamentos da atenção plena (kāyādisatipaṭṭhāna-padaṭṭhāna).",
                    "en": "Strong perception (thirasaññā-padaṭṭhāna) or the four foundations of mindfulness (kāyādisatipaṭṭhāna-padaṭṭhāna).",
                    "es": "Percepción firme (thirasaññā-padaṭṭhāna) o los cuatro fundamentos de la atención plena (kāyādisatipaṭṭhāna-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Como explica Bhikkhu Bodhi (CMA II, §5, p. 86 & nota 18), embora sati derive da raiz √sar ('lembrar'), como cetasika técnico no Abhidhamma significa presença de espírito e atenção vigilante ao momento presente. Na exegese clássica, apilāpana significa 'não flutuar' como uma cabaça na água (entrando profundamente no objeto), bem como 'lembrar/apresentar' (apilapati) os dhammas salutares à mente. Sati nunca surge em consciências prejudiciais (akusala) nem em consciências sem raiz (ahetuka): toda atenção plena genuína é eticamente bela (sobhana).",
                "en": "As Bhikkhu Bodhi explains (CMA II, §5, p. 86 & n. 18), although sati derives from √sar ('to remember'), as a technical cetasika in the Abhidhamma it signifies presence of mind and attentiveness to the present. Apilāpana means 'not wobbling/floating' like a gourd on water (plunging into the object). Sati never arises in unwholesome (akusala) or rootless (ahetuka) consciousness: all genuine sati is ethically beautiful (sobhana).",
                "es": "Como explica Bhikkhu Bodhi (CMA II, §5, p. 86 y n. 18), aunque sati deriva de √sar ('recordar'), como cetasika técnico significa presencia de ánimo en el presente y 'no flotar' (apilāpana) en la superficie del objeto. Sati nunca surge en conciencias akusala ni ahetuka."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 86); VII, §24 & §32 (pp. 279, 283)"
        },
        "seeAlso": ["satipaṭṭhāna", "saññā", "manasikāra", "paññā", "ekaggatā", "bodhipakkhiyadhamma"]
    },

    "hiri": {
        "meaning": {
            "pt": "Pudor moral; vergonha ética; autorrespeito; aversão interna à má conduta corporal, verbal e mental; o 3º dos 19 fatores universais belos e um dos dois 'guardiões do mundo' (lokapālā dhammā).",
            "en": "Moral shame; conscience; self-respect; internal disgust at bodily, verbal, and mental misconduct; the 3rd of the 19 universal beautiful factors and one of the two 'guardians of the world' (lokapālā dhammā).",
            "es": "Pudor moral; vergüenza ética; respeto por uno mismo; repugnancia interna ante la mala conducta; el 3º de los 19 factores hermosos universales y uno de los dos 'guardianes del mundo' (lokapālā dhammā)."
        },
        "grammar": "fem. (de √hir + i)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (também grafado hirī; da raiz √hir 'envergonhar-se, ter pudor')",
            "en": "Feminine noun (also spelled hirī; from root √hir 'to be ashamed, modest')",
            "es": "Sustantivo femenino (también escrito hirī; de la raíz √hir 'avergonzarse, tener pudor')"
        },
        "root": "√hir (ter pudor / envergonhar-se) + i",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #30 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #30 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #30 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa); Guardião do Mundo (Lokapāla); Poder (Hiribala); oposto de Ahirika",
                "en": "Universal Beautiful (Sobhanasādhāraṇa); Guardian of the World (Lokapāla); Power (Hiribala); opposite of Ahirika",
                "es": "Universal Hermoso (Sobhanasādhāraṇa); Guardián del Mundo (Lokapāla); Poder (Hiribala); opuesto de Ahirika"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Repugnância ou aversão ética pela má conduta corporal e verbal (kāyaduccaritādīhi jegucchana-lakkhaṇa).",
                    "en": "Disgust at bodily and verbal misconduct (kāyaduccaritādīhi jegucchana-lakkhaṇa).",
                    "es": "Repugnancia ética ante la mala conducta corporal y verbal (kāyaduccaritādīhi jegucchana-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Não praticar ações más (pāpānaṃ akaraṇa-rasa).",
                    "en": "Not doing evil things (pāpānaṃ akaraṇa-rasa).",
                    "es": "No cometer malas acciones (pāpānaṃ akaraṇa-rasa)."
                },
                "paccupatthana": {
                    "pt": "Recuar diante do mal (saṅkoca-paccupaṭṭhāna).",
                    "en": "Shrinking away from evil (saṅkoca-paccupaṭṭhāna).",
                    "es": "Retroceder ante el mal (saṅkoca-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Respeito por si mesmo e pela própria dignidade espiritual (attani gārava-padaṭṭhāna).",
                    "en": "Respect for oneself and one's own spiritual dignity (attani gārava-padaṭṭhāna).",
                    "es": "Respeto por uno mismo y por la propia dignidad espiritual (attani gārava-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "O Buddha denomina hiri e ottappa os 'dois estados luminosos que protegem o mundo' (sukkadhammā lokapālā, AN 2.9). Como explica Bhikkhu Bodhi (CMA II, §5, p. 86), hiri possui causa interna (attādhipateyya): o senso de honra e respeito por si mesmo que faz o praticante considerar o mal indigno de si, como uma bola de ferro coberta de excremento que não se deseja tocar por nojo.",
                "en": "The Buddha calls hiri and ottappa the 'two bright states that guard the world' (sukkadhammā lokapālā, AN 2.9). As Bhikkhu Bodhi explains (CMA II, §5, p. 86), hiri has an internal reference (attādhipateyya): self-respect and personal honor that makes one view evil as beneath one's dignity, like an iron ball smeared with excrement that one refuses to touch out of disgust.",
                "es": "El Buddha llama a hiri y ottappa los 'dos estados luminosos que protegen al mundo' (lokapālā). Hiri tiene origen interno: el respeto por uno mismo que ve el mal como algo indigno."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 86)"
        },
        "seeAlso": ["ottappa", "ahirika", "anottappa", "virati", "sīla"]
    },

    "ottappa": {
        "meaning": {
            "pt": "Temor moral; escrúpulo ético; receio sensato das consequências dolorosas da má conduta; o 4º dos 19 fatores universais belos e segundo 'guardião do mundo' (lokapāla).",
            "en": "Fear of wrongdoing; moral dread; wise scrupulousness regarding the painful consequences of evil deeds; the 4th of the 19 universal beautiful factors and second 'guardian of the world' (lokapāla).",
            "es": "Temor moral; escrúpulo ético; recelo sabio ante las consecuencias dolorosas de obrar mal; el 4º de los 19 factores hermosos universales y segundo 'guardián del mundo' (lokapāla)."
        },
        "grammar": "nt. (ud + √tap + ya)",
        "grammarLocalized": {
            "pt": "Substantivo neutro (derivado de ud + √tap 'queimar, atormentar a consciência')",
            "en": "Neuter noun (derived from ud + √tap 'to burn, torment')",
            "es": "Sustantivo neutro (derivado de ud + √tap 'quemar, atormentar')"
        },
        "root": "ud + √tap (queimar / recear) + ya",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #31 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #31 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #31 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa); Guardião do Mundo (Lokapāla); Poder (Ottappabala); oposto de Anottappa",
                "en": "Universal Beautiful (Sobhanasādhāraṇa); Guardian of the World (Lokapāla); Power (Ottappabala); opposite of Anottappa",
                "es": "Universal Hermoso (Sobhanasādhāraṇa); Guardián del Mundo (Lokapāla); Poder (Ottappabala); opuesto de Anottappa"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Receio ou temor ético perante a má conduta (duccaritādīhi uttāsana-lakkhaṇa).",
                    "en": "Dread in regard to bodily and verbal misconduct (duccaritādīhi uttāsana-lakkhaṇa).",
                    "es": "Temor ético respecto a la mala conducta (duccaritādīhi uttāsana-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Não praticar ações más (pāpānaṃ akaraṇa-rasa).",
                    "en": "Not doing evil things (pāpānaṃ akaraṇa-rasa).",
                    "es": "No cometer malas acciones (pāpānaṃ akaraṇa-rasa)."
                },
                "paccupatthana": {
                    "pt": "Recuar diante do mal (saṅkoca-paccupaṭṭhāna).",
                    "en": "Shrinking away from evil (saṅkoca-paccupaṭṭhāna).",
                    "es": "Retroceder ante el mal (saṅkoca-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Respeito pelos outros e pela opinião dos sábios no mundo (paresu gārava-padaṭṭhāna).",
                    "en": "Respect for others and the wise in the world (paresu gārava-padaṭṭhāna).",
                    "es": "Respeto por los demás y por los sabios en el mundo (paresu gārava-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Enquanto hiri recua diante do mal por nojo moral interno (como diante de uma bola de ferro suja de excremento), ottappa recua diante do mal por temer suas consequências kármicas e sociais (como diante de uma bola de ferro em brasa que queimará quem a segurar — Atthasālinī 125–126).",
                "en": "Whereas hiri shrinks from evil out of internal moral disgust (as from an iron ball smeared with excrement), ottappa shrinks from evil out of dread of its kammic and social consequences (as from a red-hot iron ball that will burn whoever grasps it — Atthasālinī 125–126).",
                "es": "Mientras hiri retrocede ante el mal por repugnancia moral interna, ottappa retrocede por temor a sus consecuencias kármicas (como ante una bola de hierro al rojo vivo que quemará a quien la toque)."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 86)"
        },
        "seeAlso": ["hiri", "anottappa", "ahirika", "virati", "kamma"]
    },

    "alobha": {
        "meaning": {
            "pt": "Não-cobiça; desapego; generosidade; renúncia; a 1ª das três raízes belas (sobhanahetu) e o 5º dos 19 fatores universais belos, presente em todos os 59/91 cittas belos.",
            "en": "Non-greed; detachment; generosity; renunciation; the 1st of the three beautiful roots (sobhanahetu) and the 5th of the 19 universal beautiful factors, present in all 59/91 beautiful cittas.",
            "es": "No-codicia; desapego; generosidad; renuncia; la 1ª de las tres raíces hermosas (sobhanahetu) y el 5º de los 19 factores hermosos universales, presente en todos los 59/91 cittas hermosos."
        },
        "grammar": "masc. (na > a + lobha)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (Nañ-Tappurisa: a + lobha)",
            "en": "Masculine noun (Nañ-Tappurisa: a + lobha)",
            "es": "Sustantivo masculino (Nañ-Tappurisa: a + lobha)"
        },
        "root": "na > a (não) + √lubh (cobiçar) + *a",
        "samasa": {
            "breakdown": "a (na) + lobha",
            "type": {
                "pt": "Nañ-Tappurisa Samāsa (Composto Determinativo de Oposição Positiva)",
                "en": "Nañ-Tappurisa Samāsa (Negative Determinative Compound of Positive Opposition)",
                "es": "Nañ-Tappurisa Samāsa (Compuesto Determinativo de Oposición Positiva)"
            },
            "viggaha": "lobhassa paṭipakkho ti alobho",
            "literal": {
                "pt": "O oposto positivo da cobiça (desapego / generosidade)",
                "en": "The positive opposite of greed (detachment / generosity)",
                "es": "El opuesto positivo de la codicia (desapego / generosidad)"
            },
            "parts": [
                {"pali": "a-", "gloss": {"pt": "oposto de", "en": "opposite of", "es": "opuesto de"}},
                {"pali": "lobha", "gloss": {"pt": "cobiça / apego", "en": "greed / attachment", "es": "codicia / apego"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #32 de 52) & 1ª Raiz Bela",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #32 of 52) & 1st Beautiful Root",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #32 de 52) y 1ª Raíz Hermosa"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa); Raiz Salutar/Indeterminada (Kusala/Abyākata Hetu, Cap. III, §5)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa); Wholesome/Indeterminate Root (Kusala/Abyākata Hetu, Ch. III, §5)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa); Raíz Saludable/Indeterminada (Kusala/Abyākata Hetu, Cap. III, §5)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "A ausência de desejo egoísta da mente pelo objeto (ārammaṇe cittassa agiddhitā-lakkhaṇa) ou não-aderência (alagga-bhāva), como uma gota de água sobre uma folha de lótus.",
                    "en": "The mind's lack of desire for its object (ārammaṇe cittassa agiddhitā-lakkhaṇa), or non-adherence (alagga-bhāva) like a drop of water on a lotus leaf.",
                    "es": "La falta de deseo egoísta de la mente por su objeto (agiddhitā-lakkhaṇa) o no adherencia (alagga-bhāva), como una gota de agua sobre una hoja de loto."
                },
                "rasa": {
                    "pt": "Não se apossar nem agarrar (apariggaha-rasa), como um bhikkhu libertado.",
                    "en": "Not to lay hold or not to grasp (apariggaha-rasa), like a liberated bhikkhu.",
                    "es": "No apoderarse ni aferrarse (apariggaha-rasa), como un bhikkhu liberado."
                },
                "paccupatthana": {
                    "pt": "Desapego ou estado de não estar preso (anallīnabhāva-paccupaṭṭhāna).",
                    "en": "Detachment or the state of not treating as a shelter (anallīnabhāva-paccupaṭṭhāna).",
                    "es": "Desapego o el estado de no quedar adherido (anallīnabhāva-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Atenção sábia / criteriosa (yoniso manasikāra-padaṭṭhāna).",
                    "en": "Wise attention (yoniso manasikāra-padaṭṭhāna).",
                    "es": "Atención sabia (yoniso manasikāra-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Como enfatiza Bhikkhu Bodhi (CMA II, §5, p. 86), alobha não é a mera ausência passiva de cobiça (que também existe em cittas ahetuka ou dosamūla), mas uma virtude positiva ativa (sabhāvadhamma) que se manifesta como generosidade (dāna), caridade (cāga) e renúncia (nekkhamma).",
                "en": "As Bhikkhu Bodhi emphasizes (CMA II, §5, p. 86), alobha is not the mere passive absence of greed, but a positive reality (sabhāvadhamma) comprising active virtues such as generosity (dāna), charity (cāga), and renunciation (nekkhamma).",
                "es": "Como enfatiza Bhikkhu Bodhi (CMA II, §5, p. 86), alobha no es la mera ausencia pasiva de codicia, sino una virtud positiva activa que comprende la generosidad (dāna) y la renuncia (nekkhamma)."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 86); III, §§5–7 (pp. 117–119)"
        },
        "seeAlso": ["lobha", "adosa", "amoha", "hetu", "macchariya"]
    },

    "adosa": {
        "meaning": {
            "pt": "Não-ódio; não-aversão; benevolência; amabilidade; amor-bondade (mettā); a 2ª das três raízes belas (sobhanahetu) e o 6º dos 19 fatores universais belos, presente em todos os 59/91 cittas belos.",
            "en": "Non-hatred; non-aversion; amity; gentleness; loving-kindness (mettā); the 2nd of the three beautiful roots (sobhanahetu) and the 6th of the 19 universal beautiful factors, present in all 59/91 beautiful cittas.",
            "es": "No-odio; no-aversión; benevolencia; amabilidad; amor benevolente (mettā); la 2ª de las tres raíces hermosas (sobhanahetu) y el 6º de los 19 factores hermosos universales, presente en todos los 59/91 cittas hermosos."
        },
        "grammar": "masc. (na > a + dosa)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (Nañ-Tappurisa: a + dosa)",
            "en": "Masculine noun (Nañ-Tappurisa: a + dosa)",
            "es": "Sustantivo masculino (Nañ-Tappurisa: a + dosa)"
        },
        "root": "na > a (não) + √dus (odiar) + *a",
        "samasa": {
            "breakdown": "a (na) + dosa",
            "type": {
                "pt": "Nañ-Tappurisa Samāsa (Composto Determinativo de Oposição Positiva)",
                "en": "Nañ-Tappurisa Samāsa (Negative Determinative Compound of Positive Opposition)",
                "es": "Nañ-Tappurisa Samāsa (Compuesto Determinativo de Oposición Positiva)"
            },
            "viggaha": "dosassa paṭipakkho ti adoso",
            "literal": {
                "pt": "O oposto positivo do ódio (benevolência / mettā)",
                "en": "The positive opposite of hatred (amity / mettā)",
                "es": "El opuesto positivo del odio (benevolencia / mettā)"
            },
            "parts": [
                {"pali": "a-", "gloss": {"pt": "oposto de", "en": "opposite of", "es": "opuesto de"}},
                {"pali": "dosa", "gloss": {"pt": "ódio / aversão", "en": "hatred / aversion", "es": "odio / aversión"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #33 de 52, base ontológica de Mettā)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #33 of 52, ontological basis of Mettā)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #33 de 52, base ontológica de Mettā)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa); Raiz Bela (Sobhanahetu); quando dirigido aos seres vivos, constitui o 1º Brahmavihāra (Mettā)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa); Beautiful Root (Sobhanahetu); when directed toward living beings, constitutes the 1st Brahmavihāra (Mettā)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa); Raíz Hermosa (Sobhanahetu); cuando se dirige a los seres vivos, constituye el 1º Brahmavihāra (Mettā)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Ausência de ferocidade (acaṇḍikka-lakkhaṇa) ou não-oposição (avirodha-lakkhaṇa), como um amigo gentil e prestativo.",
                    "en": "Lack of ferocity (acaṇḍikka-lakkhaṇa) or non-opposing (avirodha-lakkhaṇa), like a gentle friend.",
                    "es": "Falta de ferocidad (acaṇḍikka-lakkhaṇa) o no oposición (avirodha-lakkhaṇa), como un amigo gentil."
                },
                "rasa": {
                    "pt": "Remover a irritação (āghātavinaya-rasa) ou dissipar a febre mental (parilāhavinaya-rasa), como pasta de sândalo refrescante.",
                    "en": "To remove annoyance (āghātavinaya-rasa) or remove fever (parilāhavinaya-rasa), like sandalwood paste.",
                    "es": "Eliminar la irritación (āghātavinaya-rasa) o disipar la fiebre mental (parilāhavinaya-rasa), como pasta de sándalo."
                },
                "paccupatthana": {
                    "pt": "Agradabilidade e doçura serena (sommabhāva-paccupaṭṭhāna), como a lua cheia.",
                    "en": "Agreeableness (sommabhāva-paccupaṭṭhāna), like the full moon.",
                    "es": "Agradabilidad y dulzura serena (sommabhāva-paccupaṭṭhāna), como la luna llena."
                },
                "padatthana": {
                    "pt": "Atenção sábia (yoniso manasikāra-padaṭṭhāna).",
                    "en": "Wise attention (yoniso manasikāra-padaṭṭhāna).",
                    "es": "Atención sabia (yoniso manasikāra-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Por que o Abhidhammattha Saṅgaha lista apenas dois incomensuráveis (karuṇā e muditā) na seção §7 em vez de quatro? Como explica Bhikkhu Bodhi (CMA II, §5 & §7, pp. 86, 89–90), mettā (amor-bondade) não é um cetasika separado, mas um modo específico do cetasika universal belo adosa (não-ódio) quando dirigido ao bem-estar dos seres vivos! Do mesmo modo, upekkhā como incomensurável é um modo do cetasika tatramajjhattatā.",
                "en": "Why does the Abhidhammattha Saṅgaha list only two illimitables (karuṇā and muditā) in §7 rather than four? As Bhikkhu Bodhi explains (CMA II, §5 & §7, pp. 86, 89–90), loving-kindness (mettā) is not a separate cetasika, but a sublime mode of the universal beautiful cetasika adosa (non-hatred) when directed toward the welfare of living beings! Similarly, equanimity as an illimitable is a mode of the cetasika tatramajjhattatā.",
                "es": "Como explica Bhikkhu Bodhi (CMA II, §5 y §7, pp. 86, 89–90), el amor benevolente (mettā) no es un cetasika separado, sino un modo sublime del cetasika universal hermoso adosa (no-odio) dirigido al bienestar de los seres vivos."
            },
            "bodhiRef": "CMA II, §5 & §7 (Guide, pp. 86, 89–90); IX, §9 (p. 335)"
        },
        "seeAlso": ["mettā", "dosa", "alobha", "amoha", "karuṇā", "muditā", "tatramajjhattatā"]
    },

    "mettā": {
        "meaning": {
            "pt": "Amor-bondade; benevolência universal; amizade incondicional que deseja o bem-estar e a felicidade de todos os seres; o 1º dos 4 estados sublimes (brahmavihāra / appamaññā). Ontologicamente, é uma manifestação do cetasika adosa.",
            "en": "Loving-kindness; universal benevolence; unconditional friendliness wishing for the welfare and happiness of all beings; the 1st of the 4 sublime states (brahmavihāra / appamaññā). Ontologically, it is a mode of the cetasika adosa.",
            "es": "Amor benevolente; benevolencia universal; amistad incondicional que desea el bienestar y la felicidad de todos los seres; el 1º de los 4 estados sublimes (brahmavihāra / appamaññā). Ontológicamente, es un modo del cetasika adosa."
        },
        "grammar": "fem. (de mitta + ya)",
        "grammarLocalized": {
            "pt": "Substantivo feminino abstrato (derivado de mitta 'amigo': mittassa bhāvo mettā)",
            "en": "Abstract feminine noun (derived from mitta 'friend': mittassa bhāvo mettā)",
            "es": "Sustantivo femenino abstracto (derivado de mitta 'amigo': mittassa bhāvo mettā)"
        },
        "root": "√mid (amar / ser afetuoso) > mitta + ya",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Modo Sublime do Cetasika Adosa (#33 de 52)",
                "en": "Ultimate Reality — Sublime Mode of the Cetasika Adosa (#33 of 52)",
                "es": "Realidad Última — Modo Sublime del Cetasika Adosa (#33 de 52)"
            },
            "category": {
                "pt": "1º Incomensurável / Morada Divina (Appamaññā / Brahmavihāra); conduz até o 3º (ou 4º) Jhāna",
                "en": "1st Illimitable / Divine Abode (Appamaññā / Brahmavihāra); leads up to the 3rd (or 4th) Jhāna",
                "es": "1º Inconmensurable / Morada Divina (Appamaññā / Brahmavihāra); conduce hasta el 3º (o 4º) Jhāna"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Promover o bem-estar e a felicidade dos seres vivos (hitākārappavatti-lakkhaṇa).",
                    "en": "Promoting the welfare of living beings (hitākārappavatti-lakkhaṇa).",
                    "es": "Promover el bienestar de los seres vivos (hitākārappavatti-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Preferir e aportar o bem-estar deles (hitūpasaṃhāra-rasa).",
                    "en": "To prefer or bring about their welfare (hitūpasaṃhāra-rasa).",
                    "es": "Preferir y aportar su bienestar (hitūpasaṃhāra-rasa)."
                },
                "paccupatthana": {
                    "pt": "A remoção da má vontade e aversão (āghātavinaya-paccupaṭṭhāna).",
                    "en": "The removal of ill will (āghātavinaya-paccupaṭṭhāna).",
                    "es": "La eliminación de la mala voluntad (āghātavinaya-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Ver os seres como amáveis e dignos de apreço (sattānaṃ manāpapassanā-padaṭṭhāna). Seu 'inimigo próximo' é a afeição egoísta (gehasita-pema) e seu 'inimigo distante' é a má vontade (vyāpāda).",
                    "en": "Seeing beings as lovable (sattānaṃ manāpapassanā-padaṭṭhāna). Its 'near enemy' is selfish affection (gehasita-pema) and its 'far enemy' is ill will (vyāpāda).",
                    "es": "Ver a los seres como amables (sattānaṃ manāpapassanā-padaṭṭhāna). Su 'enemigo cercano' es el afecto egoísta y su 'enemigo lejano' la mala voluntad."
                }
            },
            "philosophy": {
                "pt": "Como objeto de meditação (kammaṭṭhāna, Cap. IX, §§9, 19–20), mettā toma o conceito de seres vivos (satta-paññatti) como objeto e alcança os três primeiros jhānas na contagem quádrupla (ou quatro na quíntupla), pois está sempre associado à sensação mental alegre (somanassa).",
                "en": "As a meditation subject (kammaṭṭhāna, Ch. IX, §§9, 19–20), mettā takes the concept of living beings (satta-paññatti) as object and reaches the first three jhānas in the fourfold reckoning (four in the fivefold), since it is always accompanied by joyful feeling (somanassa).",
                "es": "Como objeto de meditación (kammaṭṭhāna, Cap. IX, §§9, 19–20), mettā toma el concepto de seres vivos (satta-paññatti) y alcanza los primeros tres jhānas (cuatro en el sistema quíntuple)."
            },
            "bodhiRef": "CMA II, §5 & §7 (Guide, pp. 86, 89–90); IX, §9 & §19 (pp. 335, 341)"
        },
        "seeAlso": ["adosa", "karuṇā", "muditā", "tatramajjhattatā", "appamaññā"]
    },

    "tatramajjhattatā": {
        "meaning": {
            "pt": "Neutralidade mental; equilíbrio da mente; imparcialidade; equanimidade conativa (saṅkhārupekkhā, distinta da sensação neutra vedanā-upekkhā); o 7º dos 19 fatores universais belos.",
            "en": "Neutrality of mind; mental balance; impartiality; conative equanimity (saṅkhārupekkhā, distinct from neutral feeling vedanā-upekkhā); the 7th of the 19 universal beautiful factors.",
            "es": "Neutralidad de la mente; equilibrio mental; imparcialidad; ecuanimidad conativa (saṅkhārupekkhā, distinta de la sensación neutra vedanā-upekkhā); el 7º de los 19 factores hermosos universales."
        },
        "grammar": "fem. (tatra + majjhatta + tā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino abstrato (tatra 'ali, nesses estados' + majjha 'meio' + tta + tā)",
            "en": "Abstract feminine noun (tatra 'there, among those states' + majjha 'middle' + tta + tā)",
            "es": "Sustantivo femenino abstracto (tatra 'allí, en esos estados' + majjha 'medio' + tta + tā)"
        },
        "root": "tatra (ali) + majjha (meio) + tta + tā",
        "samasa": {
            "breakdown": "tatra + majjhatta + tā",
            "type": {
                "pt": "Sattamī-Tappurisa Samāsa + Taddhita (-tā)",
                "en": "Sattamī-Tappurisa Samāsa + Abstract Suffix (-tā)",
                "es": "Sattamī-Tappurisa Samāsa + Sufijo Abstracto (-tā)"
            },
            "viggaha": "tattha dhammesu majjhattabhāvo ti tatramajjhattatā",
            "literal": {
                "pt": "O estar exatamente no meio ali (entre os dhammas conascidos)",
                "en": "There-in-the-middleness (among the conascent states)",
                "es": "El estar en el medio allí (entre los estados co-nacidos)"
            },
            "parts": [
                {"pali": "tatra", "gloss": {"pt": "ali (nesses dhammas)", "en": "there (in those states)", "es": "allí (en esos estados)"}},
                {"pali": "majjhatta", "gloss": {"pt": "centralidade / imparcialidade", "en": "middleness / neutrality", "es": "centralidad / imparcialidad"}},
                {"pali": "-tā", "gloss": {"pt": "estado abstrato de", "en": "abstract state of", "es": "estado abstracto de"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #34 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #34 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #34 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa — presente nos 59/91 sobhanacittas); Fator de Iluminação (Upekkhāsambojjhaṅga); 4º Brahmavihāra (Upekkhā)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa — present in all 59/91 sobhanacittas); Enlightenment Factor (Upekkhāsambojjhaṅga); 4th Brahmavihāra (Upekkhā)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa — presente en los 59/91 sobhanacittas); Factor de Iluminación (Upekkhāsambojjhaṅga); 4º Brahmavihāra (Upekkhā)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Conduzir a consciência e os fatores mentais de modo uniforme e equilibrado (cittacetasikānaṃ samavāhita-lakkhaṇa).",
                    "en": "Conveying consciousness and the mental factors evenly (cittacetasikānaṃ samavāhita-lakkhaṇa).",
                    "es": "Conducir la conciencia y los factores mentales de manera uniforme y equilibrada (cittacetasikānaṃ samavāhita-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Impedir a deficiência e o excesso (ūṇādhikatā-nivāraṇa-rasa) ou eliminar a parcialidade (pakkhapātupaccheda-rasa).",
                    "en": "To prevent deficiency and excess (ūnādhikatā-nivāraṇa-rasa), or to prevent partiality (pakkhapātupaccheda-rasa).",
                    "es": "Impedir la deficiencia y el exceso (ūnādhikatā-nivāraṇa-rasa) o eliminar la parcialidad (pakkhapātupaccheda-rasa)."
                },
                "paccupatthana": {
                    "pt": "Neutralidade e equilíbrio (majjhattabhāva-paccupaṭṭhāna).",
                    "en": "Neutrality and balance (majjhattabhāva-paccupaṭṭhāna).",
                    "es": "Neutralidad y equilibrio (majjhattabhāva-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Os estados mentais conascidos. Deve ser visto como um cocheiro que observa com equanimidade os cavalos puro-sangue avançando em ritmo uniforme pela estrada.",
                    "en": "The conascent mental states. It should be seen as a charioteer who looks on with equanimity at the thoroughbreds progressing evenly along the roadway.",
                    "es": "Los estados mentales co-nacidos. Debe verse como un auriga que contempla con ecuanimidad a los corceles avanzando uniformemente."
                }
            },
            "philosophy": {
                "pt": "Distinção crucial do Abhidhamma (CMA I, §10, p. 44; II, §5, pp. 86–87): a palavra upekkhā é usada na literatura em Pāli para dois cetasikas totalmente diferentes: (1) upekkhā-vedanā (sensação neutra, pertencente a vedanākkhandha) e (2) tatramajjhattatā (equilíbrio/imparcialidade sublime da mente, pertencente a saṅkhārakkhandha). Como tatramajjhattatā é um universal belo, ele está presente inclusive nos cittas belos acompanhados por somanassa (alegria)! É este cetasika tatramajjhattatā que constitui o 4º brahmavihāra (upekkhā-appamaññā), o 7º fator de iluminação (upekkhāsambojjhaṅga) e a equanimidade das formações no insight (saṅkhārupekkhāñāṇa).",
                "en": "Crucial Abhidhamma distinction (CMA I, §10, p. 44; II, §5, pp. 86–87): the word upekkhā is used in Pāli for two completely different cetasikas: (1) upekkhā-vedanā (neutral feeling, belonging to vedanākkhandha) and (2) tatramajjhattatā (sublime mental balance and impartiality, belonging to saṅkhārakkhandha). Because tatramajjhattatā is a universal beautiful factor, it is present even in beautiful cittas accompanied by joyful feeling (somanassa)! It is tatramajjhattatā that constitutes the 4th brahmavihāra (upekkhā), the 7th enlightenment factor (upekkhāsambojjhaṅga), and equanimity toward formations in insight (saṅkhārupekkhāñāṇa).",
                "es": "Distinción crucial del Abhidhamma (CMA I, §10, p. 44; II, §5, pp. 86–87): upekkhā designa dos cetasikas distintos: (1) upekkhā-vedanā (sensación neutra) y (2) tatramajjhattatā (equilibrio mental sublime, perteneciente a saṅkhārakkhandha). Incluso los cittas hermosos con somanassa poseen tatramajjhattatā."
            },
            "bodhiRef": "CMA I, §10 (p. 44); II, §5 & §7 (Guide, pp. 86–87, 89–90)"
        },
        "seeAlso": ["upekkhāsahagata", "vedanā", "mettā", "karuṇā", "muditā", "appamaññā"]
    },

    "passaddhi": {
        "meaning": {
            "pt": "Tranquilidade; serenidade; acalmamento dos distúrbios mentais (daratha); abrange o par universal belo kāyapassaddhi (tranquilidade do corpo mental dos cetasikas, #35) e cittapassaddhi (tranquilidade da consciência, #36), e constitui o 5º fator de iluminação (passaddhisambojjhaṅga).",
            "en": "Tranquillity; serenity; the quieting down of mental disturbances (daratha); comprises the universal beautiful pair kāyapassaddhi (tranquillity of the mental body of cetasikas, #35) and cittapassaddhi (tranquillity of consciousness, #36), and forms the 5th enlightenment factor (passaddhisambojjhaṅga).",
            "es": "Tranquilidad; serenidad; apaciguamiento de las perturbaciones mentales (daratha); comprende el par universal hermoso kāyapassaddhi (#35) y cittapassaddhi (#36), y constituye el 5º factor de iluminación (passaddhisambojjhaṅga)."
        },
        "grammar": "fem. (pa + √sambh + ti)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (pa + √sambh 'acalmar, aquietar' + ti)",
            "en": "Feminine noun (pa + √sambh 'to calm down, quiet' + ti)",
            "es": "Sustantivo femenino (pa + √sambh 'calmar, aquietar' + ti)"
        },
        "root": "pa + √sambh (acalmar / serenar) + ti",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Par de Fatores Mentais Universais Belos (Cetasikas #35 e #36 de 52)",
                "en": "Ultimate Reality — Pair of Universal Beautiful Mental Factors (Cetasikas #35 and #36 of 52)",
                "es": "Realidad Última — Par de Factores Mentales Hermosos Universales (Cetasikas #35 y #36 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa: Kāyapassaddhi + Cittapassaddhi); 5º Bojjhaṅga; oposto direto de Uddhacca e Kukkucca",
                "en": "Universal Beautiful (Sobhanasādhāraṇa: Kāyapassaddhi + Cittapassaddhi); 5th Bojjhaṅga; direct opposite of Uddhacca and Kukkucca",
                "es": "Universal Hermoso (Sobhanasādhāraṇa: Kāyapassaddhi + Cittapassaddhi); 5º Bojjhaṅga; opuesto directo de Uddhacca y Kukkucca"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Aquietamento das perturbações e febres (darathavūpasama-lakkhaṇa) no corpo mental (kāya = cetasikas) e na consciência (citta).",
                    "en": "Quieting down of disturbances (darathavūpasama-lakkhaṇa) in the mental body (kāya = cetasikas) and consciousness (citta).",
                    "es": "Apaciguamiento de las perturbaciones (darathavūpasama-lakkhaṇa) en el cuerpo mental y la conciencia."
                },
                "rasa": {
                    "pt": "Esmagar e dissipar tais perturbações (darathanimmaddana-rasa).",
                    "en": "To crush such disturbances (darathanimmaddana-rasa).",
                    "es": "Aplastar tales perturbaciones (darathanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Ausência de agitação / paz e frescor sereno (aparipphandatā-sītibhāva-paccupaṭṭhāna).",
                    "en": "Peacefulness and coolness, absence of trembling (aparipphandatā-sītibhāva-paccupaṭṭhāna).",
                    "es": "Paz y frescura serena, ausencia de agitación (aparipphandatā-sītibhāva-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O corpo mental (cetasikas) e a consciência (kāyacitta-padaṭṭhāna).",
                    "en": "The mental body and consciousness (kāyacitta-padaṭṭhāna).",
                    "es": "El cuerpo mental y la conciencia (kāyacitta-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Como explica Bhikkhu Bodhi (CMA II, §5, p. 87), nos 6 pares de cetasikas universais belos (#35 a #46), 'kāya' não significa o corpo físico material, mas o 'corpo mental' (nāmakāya) — isto é, a coleção dos três agregados de cetasikas (vedanā, saññā e saṅkhāra), enquanto 'citta' designa a própria consciência (viññāṇakkhandha). Passaddhi opõe-se diretamente às impurezas que criam aflição, como a inquietação (uddhacca) e o remorso (kukkucca).",
                "en": "As Bhikkhu Bodhi explains (CMA II, §5, p. 87), in the 6 pairs of universal beautiful cetasikas (#35 to #46), 'kāya' does not mean the physical body, but the 'mental body' (nāmakāya) — the aggregation of associated cetasikas (vedanā, saññā, saṅkhāra), while 'citta' denotes consciousness itself. Passaddhi is directly opposed to restlessness (uddhacca) and worry (kukkucca).",
                "es": "Como explica Bhikkhu Bodhi (CMA II, §5, p. 87), en los 6 pares de cetasikas hermosos (#35 a #46), 'kāya' significa el 'cuerpo mental' (nāmakāya, la colección de cetasikas asociados), y 'citta' la conciencia. Passaddhi se opone directamente a uddhacca y kukkucca."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 87)"
        },
        "seeAlso": ["kāyapassaddhi", "cittapassaddhi", "uddhacca", "kukkucca", "lahutā", "mudutā"]
    },

    "kāyapassaddhi": {
        "meaning": {
            "pt": "Tranquilidade do corpo mental (dos cetasikas associados); o 8º dos 19 fatores universais belos (Cetasika #35 de 52), oposto a uddhacca e kukkucca.",
            "en": "Tranquillity of the mental body (of associated cetasikas); the 8th of the 19 universal beautiful factors (Cetasika #35 of 52), opposed to uddhacca and kukkucca.",
            "es": "Tranquilidad del cuerpo mental (de los cetasikas asociados); el 8º de los 19 factores hermosos universales (Cetasika #35 de 52), opuesto a uddhacca y kukkucca."
        },
        "grammar": "fem. (Chaṭṭhī-Tappurisa: kāya + passaddhi)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (Chaṭṭhī-Tappurisa: kāyassa passaddhi)",
            "en": "Feminine noun (Chaṭṭhī-Tappurisa: kāyassa passaddhi)",
            "es": "Sustantivo femenino (Chaṭṭhī-Tappurisa: kāyassa passaddhi)"
        },
        "root": "kāya (corpo mental de cetasikas) + pa + √sambh + ti",
        "samasa": {
            "breakdown": "kāya + passaddhi",
            "type": {
                "pt": "Chaṭṭhī-Tappurisa Samāsa (Composto Determinativo Genitivo)",
                "en": "Chaṭṭhī-Tappurisa Samāsa (Genitive Determinative Compound)",
                "es": "Chaṭṭhī-Tappurisa Samāsa (Compuesto Determinativo Genitivo)"
            },
            "viggaha": "kāyassa (nāmakāyassa) passaddhi ti kāyapassaddhi",
            "literal": {
                "pt": "Tranquilidade do corpo (mental dos cetasikas)",
                "en": "Tranquillity of the (mental) body (of cetasikas)",
                "es": "Tranquilidad del cuerpo (mental de cetasikas)"
            },
            "parts": [
                {"pali": "kāya", "gloss": {"pt": "corpo mental (cetasikas)", "en": "mental body (cetasikas)", "es": "cuerpo mental (cetasikas)"}},
                {"pali": "passaddhi", "gloss": {"pt": "tranquilidade / serenidade", "en": "tranquillity / serenity", "es": "tranquilidad / serenidad"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #35 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #35 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #35 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa — presente nos 59/91 sobhanacittas)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa — present in all 59/91 sobhanacittas)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa — presente en los 59/91 sobhanacittas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Aquietamento das perturbações no corpo mental dos fatores mentais (kāyadarathavūpasama-lakkhaṇa).",
                    "en": "Quieting down of disturbances in the mental body (kāyadarathavūpasama-lakkhaṇa).",
                    "es": "Apaciguamiento de las perturbaciones en el cuerpo mental (kāyadarathavūpasama-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Esmagar as perturbações do corpo mental (kāyadarathanimmaddana-rasa).",
                    "en": "To crush disturbances of the mental body (kāyadarathanimmaddana-rasa).",
                    "es": "Aplastar las perturbaciones del cuerpo mental (kāyadarathanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Paz, estabilidade e frescor do corpo mental (kāyassa aparipphandatā-sītibhāva-paccupaṭṭhāna).",
                    "en": "Peacefulness and coolness of the mental body (kāyassa aparipphandatā-sītibhāva-paccupaṭṭhāna).",
                    "es": "Paz y frescura del cuerpo mental (kāyassa aparipphandatā-sītibhāva-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O corpo mental (kāya-padaṭṭhāna).",
                    "en": "The mental body (kāya-padaṭṭhāna).",
                    "es": "El cuerpo mental (kāya-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Aqui 'kāya' designa nāmakāya (o conjunto dos cetasikas vedanā, saññā e saṅkhāra). Quando os cetasikas e a consciência se tranquilizam por kāyapassaddhi e cittapassaddhi, o próprio corpo físico material também experimenta alívio e bem-estar através da matéria originada pela mente (cittajarūpa).",
                "en": "Here 'kāya' denotes nāmakāya (the collection of cetasikas). When the mental body and consciousness are tranquillized by kāyapassaddhi and cittapassaddhi, the physical body also experiences calm through mind-born matter (cittajarūpa).",
                "es": "Aquí 'kāya' designa nāmakāya (la colección de cetasikas asociados). Surge siempre en par con cittapassaddhi."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 87)"
        },
        "seeAlso": ["cittapassaddhi", "passaddhi", "uddhacca", "kukkucca"]
    },

    "cittapassaddhi": {
        "meaning": {
            "pt": "Tranquilidade da consciência; o 9º dos 19 fatores universais belos (Cetasika #36 de 52), que aquieta a agitação da própria consciência (citta).",
            "en": "Tranquillity of consciousness; the 9th of the 19 universal beautiful factors (Cetasika #36 of 52), which quiets down disturbances in consciousness (citta) itself.",
            "es": "Tranquilidad de la conciencia; el 9º de los 19 factores hermosos universales (Cetasika #36 de 52), que apacigua las perturbaciones en la conciencia (citta)."
        },
        "grammar": "fem. (Chaṭṭhī-Tappurisa: citta + passaddhi)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (Chaṭṭhī-Tappurisa: cittassa passaddhi)",
            "en": "Feminine noun (Chaṭṭhī-Tappurisa: cittassa passaddhi)",
            "es": "Sustantivo femenino (Chaṭṭhī-Tappurisa: cittassa passaddhi)"
        },
        "root": "citta + pa + √sambh + ti",
        "samasa": {
            "breakdown": "citta + passaddhi",
            "type": {
                "pt": "Chaṭṭhī-Tappurisa Samāsa (Composto Determinativo Genitivo)",
                "en": "Chaṭṭhī-Tappurisa Samāsa (Genitive Determinative Compound)",
                "es": "Chaṭṭhī-Tappurisa Samāsa (Compuesto Determinativo Genitivo)"
            },
            "viggaha": "cittassa passaddhi ti cittapassaddhi",
            "literal": {
                "pt": "Tranquilidade da consciência",
                "en": "Tranquillity of consciousness",
                "es": "Tranquilidad de la conciencia"
            },
            "parts": [
                {"pali": "citta", "gloss": {"pt": "consciência", "en": "consciousness", "es": "conciencia"}},
                {"pali": "passaddhi", "gloss": {"pt": "tranquilidade", "en": "tranquillity", "es": "tranquilidad"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #36 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #36 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #36 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa — presente nos 59/91 sobhanacittas)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa — present in all 59/91 sobhanacittas)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa — presente en los 59/91 sobhanacittas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Aquietamento das perturbações na consciência (cittadarathavūpasama-lakkhaṇa).",
                    "en": "Quieting down of disturbances in consciousness (cittadarathavūpasama-lakkhaṇa).",
                    "es": "Apaciguamiento de las perturbaciones en la conciencia (cittadarathavūpasama-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Esmagar as perturbações da consciência (cittadarathanimmaddana-rasa).",
                    "en": "To crush disturbances of consciousness (cittadarathanimmaddana-rasa).",
                    "es": "Aplastar las perturbaciones de la conciencia (cittadarathanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Paz e frescor sereno da consciência (cittassa aparipphandatā-sītibhāva-paccupaṭṭhāna).",
                    "en": "Peacefulness and coolness of consciousness (cittassa aparipphandatā-sītibhāva-paccupaṭṭhāna).",
                    "es": "Paz y frescura serena de la conciencia (cittassa aparipphandatā-sītibhāva-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "A consciência (citta-padaṭṭhāna).",
                    "en": "Consciousness (citta-padaṭṭhāna).",
                    "es": "La conciencia (citta-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Atua sempre em par com kāyapassaddhi em todas as consciências belas, opondo-se diretamente à inquietação (uddhacca).",
                "en": "Always operates in tandem with kāyapassaddhi in all beautiful cittas, directly countering restlessness (uddhacca).",
                "es": "Opera siempre en par con kāyapassaddhi en todas las conciencias hermosas, oponiéndose a uddhacca."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 87)"
        },
        "seeAlso": ["kāyapassaddhi", "passaddhi", "uddhacca"]
    },

    "lahutā": {
        "meaning": {
            "pt": "Leveza; agilidade; ausência de peso e lentidão; designa tanto o par de fatores mentais universais belos kāyalahutā (#37) e cittalahutā (#38), que se opõem ao torpor e languidez (thīna-middha), quanto a propriedade material mutável rūpassa lahutā (Cap. VI, §4).",
            "en": "Lightness; agility; absence of sluggishness; denotes both the pair of universal beautiful mental factors kāyalahutā (#37) and cittalahutā (#38), opposed to sloth and torpor (thīna-middha), and the mutable material phenomenon rūpassa lahutā (Ch. VI, §4).",
            "es": "Ligereza; agilidad; ausencia de pesadez; designa tanto el par de factores mentales hermosos universales kāyalahutā (#37) y cittalahutā (#38), opuestos a thīna-middha, como la propiedad material mutable rūpassa lahutā (Cap. VI, §4)."
        },
        "grammar": "fem. (lahu + tā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino abstrato (lahu 'leve, ágil' + sufixo abstrato -tā)",
            "en": "Abstract feminine noun (lahu 'light, agile' + abstract suffix -tā)",
            "es": "Sustantivo femenino abstracto (lahu 'ligero, ágil' + sufijo abstracto -tā)"
        },
        "root": "√lagh (ser leve / rápido) > lahu + tā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última Mental (Cetasikas #37 e #38 de 52) & Matéria Mutável (Vikārarūpa #22 de 28)",
                "en": "Mental Ultimate Reality (Cetasikas #37 and #38 of 52) & Mutable Matter (Vikārarūpa #22 of 28)",
                "es": "Realidad Última Mental (Cetasikas #37 y #38 de 52) y Materia Mutable (Vikārarūpa #22 de 28)"
            },
            "category": {
                "pt": "Universal Belo (Kāyalahutā + Cittalahutā — opostos a Thīna e Middha); também Vikārarūpa (Rūpassa Lahutā)",
                "en": "Universal Beautiful (Kāyalahutā + Cittalahutā — opposed to Thīna and Middha); also Vikārarūpa (Rūpassa Lahutā)",
                "es": "Universal Hermoso (Kāyalahutā + Cittalahutā — opuestos a Thīna y Middha); también Vikārarūpa (Rūpassa Lahutā)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Abrandamento do peso ou lentidão (garubhāvavūpasama-lakkhaṇa) no corpo mental e na consciência.",
                    "en": "The subsiding of heaviness (garubhāvavūpasama-lakkhaṇa) in the mental body and consciousness.",
                    "es": "El apaciguamiento de la pesadez (garubhāvavūpasama-lakkhaṇa) en el cuerpo mental y la conciencia."
                },
                "rasa": {
                    "pt": "Esmagar o peso mental (garubhāvanimmaddana-rasa).",
                    "en": "To crush heaviness (garubhāvanimmaddana-rasa).",
                    "es": "Aplastar la pesadez (garubhāvanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Ausência de lentidão ou agilidade mental (adandhatā-paccupaṭṭhāna).",
                    "en": "Non-sluggishness (adandhatā-paccupaṭṭhāna).",
                    "es": "Ausencia de lentitud o pesadez (adandhatā-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O corpo mental e a consciência (kāyacitta-padaṭṭhāna).",
                    "en": "The mental body and consciousness (kāyacitta-padaṭṭhāna).",
                    "es": "El cuerpo mental y la conciencia (kāyacitta-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "No plano mental (CMA II, §5, p. 87), kāyalahutā e cittalahutā opõem-se diretamente a thīna e middha (torpor e languidez), que tornam a mente pesada como uma pedra. No plano material (CMA VI, §4, p. 240), rūpassa lahutā é a agilidade física produzida por mente serena, temperatura favorável ou alimento nutritivo.",
                "en": "On the mental plane (CMA II, §5, p. 87), kāyalahutā and cittalahutā are directly opposed to sloth and torpor (thīna-middha), which make the mind heavy. On the material plane (CMA VI, §4, p. 240), rūpassa lahutā is physical agility produced by consciousness, temperature, or nutriment.",
                "es": "En el plano mental (CMA II, §5, p. 87), kāyalahutā y cittalahutā se oponen directamente a thīna y middha. En el plano material (CMA VI, §4, p. 240), rūpassa lahutā es la ligereza de la materia."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 87); VI, §4 (p. 240)"
        },
        "seeAlso": ["kāyalahutā", "cittalahutā", "thīna", "middha", "mudutā", "kammaññatā"]
    },

    "kāyalahutā": {
        "meaning": {
            "pt": "Leveza do corpo mental (dos cetasikas); o 10º dos 19 fatores universais belos (Cetasika #37 de 52), oposto a thīna e middha.",
            "en": "Lightness of the mental body (of cetasikas); the 10th of the 19 universal beautiful factors (Cetasika #37 of 52), opposed to thīna and middha.",
            "es": "Ligereza del cuerpo mental (de los cetasikas); el 10º de los 19 factores hermosos universales (Cetasika #37 de 52), opuesto a thīna y middha."
        },
        "grammar": "fem. (Chaṭṭhī-Tappurisa: kāya + lahutā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (Chaṭṭhī-Tappurisa: kāyassa lahutā)",
            "en": "Feminine noun (Chaṭṭhī-Tappurisa: kāyassa lahutā)",
            "es": "Sustantivo femenino (Chaṭṭhī-Tappurisa: kāyassa lahutā)"
        },
        "root": "kāya + lahu + tā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #37 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #37 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #37 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa — presente nos 59/91 sobhanacittas)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa — present in all 59/91 sobhanacittas)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa — presente en los 59/91 sobhanacittas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Abrandamento do peso no corpo mental (kāyagarubhāvavūpasama-lakkhaṇa).",
                    "en": "Subsiding of heaviness in the mental body (kāyagarubhāvavūpasama-lakkhaṇa).",
                    "es": "Apaciguamiento de la pesadez en el cuerpo mental (kāyagarubhāvavūpasama-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Esmagar o peso do corpo mental (kāyagarubhāvanimmaddana-rasa).",
                    "en": "To crush heaviness of the mental body (kāyagarubhāvanimmaddana-rasa).",
                    "es": "Aplastar la pesadez del cuerpo mental (kāyagarubhāvanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Não-lentidão dos fatores mentais (kāyassa adandhatā-paccupaṭṭhāna).",
                    "en": "Non-sluggishness of the mental body (kāyassa adandhatā-paccupaṭṭhāna).",
                    "es": "No lentitud del cuerpo mental (kāyassa adandhatā-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O corpo mental (kāya-padaṭṭhāna).",
                    "en": "The mental body (kāya-padaṭṭhāna).",
                    "es": "El cuerpo mental (kāya-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Impede a languidez mórbida dos fatores mentais (middha), conferindo prontidão ágil às operações benéficas.",
                "en": "Counteracts morbid torpor of the mental factors (middha), imparting agile readiness to wholesome operations.",
                "es": "Contrarresta el torpor mórbido de los factores mentales (middha)."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 87)"
        },
        "seeAlso": ["cittalahutā", "lahutā", "middha", "thīna"]
    },

    "cittalahutā": {
        "meaning": {
            "pt": "Leveza da consciência; o 11º dos 19 fatores universais belos (Cetasika #38 de 52), oposto a thīna e middha.",
            "en": "Lightness of consciousness; the 11th of the 19 universal beautiful factors (Cetasika #38 of 52), opposed to thīna and middha.",
            "es": "Ligereza de la conciencia; el 11º de los 19 factores hermosos universales (Cetasika #38 de 52), opuesto a thīna y middha."
        },
        "grammar": "fem. (Chaṭṭhī-Tappurisa: citta + lahutā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (Chaṭṭhī-Tappurisa: cittassa lahutā)",
            "en": "Feminine noun (Chaṭṭhī-Tappurisa: cittassa lahutā)",
            "es": "Sustantivo femenino (Chaṭṭhī-Tappurisa: cittassa lahutā)"
        },
        "root": "citta + lahu + tā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #38 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #38 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #38 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa — presente nos 59/91 sobhanacittas)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa — present in all 59/91 sobhanacittas)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa — presente en los 59/91 sobhanacittas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Abrandamento do peso na consciência (cittagarubhāvavūpasama-lakkhaṇa).",
                    "en": "Subsiding of heaviness in consciousness (cittagarubhāvavūpasama-lakkhaṇa).",
                    "es": "Apaciguamiento de la pesadez en la conciencia (cittagarubhāvavūpasama-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Esmagar o peso da consciência (cittagarubhāvanimmaddana-rasa).",
                    "en": "To crush heaviness of consciousness (cittagarubhāvanimmaddana-rasa).",
                    "es": "Aplastar la pesadez de la conciencia (cittagarubhāvanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Não-lentidão da consciência (cittassa adandhatā-paccupaṭṭhāna).",
                    "en": "Non-sluggishness of consciousness (cittassa adandhatā-paccupaṭṭhāna).",
                    "es": "No lentitud de la conciencia (cittassa adandhatā-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "A consciência (citta-padaṭṭhāna).",
                    "en": "Consciousness (citta-padaṭṭhāna).",
                    "es": "La conciencia (citta-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Impede a estagnação mórbida da consciência (thīna), atuando sempre em par com kāyalahutā.",
                "en": "Counteracts morbid sluggishness of consciousness (thīna), always operating paired with kāyalahutā.",
                "es": "Contrarresta el embotamiento de la conciencia (thīna), operando siempre con kāyalahutā."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 87)"
        },
        "seeAlso": ["kāyalahutā", "lahutā", "thīna", "middha"]
    },

    "mudutā": {
        "meaning": {
            "pt": "Maleabilidade; suavidade; flexibilidade; ausência de rigidez; designa tanto o par de fatores mentais universais belos kāyamudutā (#39) e cittamudutā (#40), que se opõem à rigidez de visões errôneas (diṭṭhi) e presunção (māna), quanto a propriedade material mutável rūpassa mudutā (Cap. VI, §4).",
            "en": "Malleability; softness; pliability; absence of rigidity; denotes both the pair of universal beautiful mental factors kāyamudutā (#39) and cittamudutā (#40), opposed to the rigidity of wrong views (diṭṭhi) and conceit (māna), and the mutable material phenomenon rūpassa mudutā (Ch. VI, §4).",
            "es": "Maleabilidad; suavidad; flexibilidad; ausencia de rigidez; designa tanto el par de factores mentales hermosos universales kāyamudutā (#39) y cittamudutā (#40), opuestos a diṭṭhi y māna, como la propiedad material mutable rūpassa mudutā (Cap. VI, §4)."
        },
        "grammar": "fem. (mudu + tā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino abstrato (mudu 'macio, flexível, dócil' + sufixo abstrato -tā)",
            "en": "Abstract feminine noun (mudu 'soft, pliable' + abstract suffix -tā)",
            "es": "Sustantivo femenino abstracto (mudu 'suave, flexible' + sufijo abstracto -tā)"
        },
        "root": "√mud / mudu (macio / flexível) + tā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última Mental (Cetasikas #39 e #40 de 52) & Matéria Mutável (Vikārarūpa #23 de 28)",
                "en": "Mental Ultimate Reality (Cetasikas #39 and #40 of 52) & Mutable Matter (Vikārarūpa #23 of 28)",
                "es": "Realidad Última Mental (Cetasikas #39 y #40 de 52) y Materia Mutable (Vikārarūpa #23 de 28)"
            },
            "category": {
                "pt": "Universal Belo (Kāyamudutā + Cittamudutā — opostos a Diṭṭhi e Māna); também Vikārarūpa (Rūpassa Mudutā)",
                "en": "Universal Beautiful (Kāyamudutā + Cittamudutā — opposed to Diṭṭhi and Māna); also Vikārarūpa (Rūpassa Mudutā)",
                "es": "Universal Hermoso (Kāyamudutā + Cittamudutā — opuestos a Diṭṭhi y Māna); también Vikārarūpa (Rūpassa Mudutā)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Abrandamento da rigidez (thambhavūpasama-lakkhaṇa) no corpo mental e na consciência.",
                    "en": "Subsiding of rigidity (thambhavūpasama-lakkhaṇa) in the mental body and consciousness.",
                    "es": "Apaciguamiento de la rigidez (thambhavūpasama-lakkhaṇa) en el cuerpo mental y la conciencia."
                },
                "rasa": {
                    "pt": "Esmagar a rigidez e inflexibilidade (thambhanimmaddana-rasa).",
                    "en": "To crush stiffness and rigidity (thambhanimmaddana-rasa).",
                    "es": "Aplastar la rigidez e inflexibilidad (thambhanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Não-resistência ou receptividade dócil (appaṭighāta-paccupaṭṭhāna).",
                    "en": "Non-resistance (appaṭighāta-paccupaṭṭhāna).",
                    "es": "No resistencia o receptividad dócil (appaṭighāta-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O corpo mental e a consciência (kāyacitta-padaṭṭhāna).",
                    "en": "The mental body and consciousness (kāyacitta-padaṭṭhāna).",
                    "es": "El cuerpo mental y la conciencia (kāyacitta-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Como explica Bhikkhu Bodhi (CMA II, §5, p. 87), as visões errôneas dogmáticas (diṭṭhi) e a presunção arrogante (māna) criam endurecimento e rigidez mental (thambha). Mudutā dissolve essa dureza, tornando os fatores mentais e a consciência macios e receptivos como couro bem curtido.",
                "en": "As Bhikkhu Bodhi explains (CMA II, §5, p. 87), dogmatic wrong views (diṭṭhi) and arrogant conceit (māna) create mental rigidity and stiffness (thambha). Mudutā crushes this stiffness, making the mental factors and consciousness pliable like well-tanned leather.",
                "es": "Como explica Bhikkhu Bodhi (CMA II, §5, p. 87), las visiones erróneas (diṭṭhi) y la presunción (māna) crean rigidez mental (thambha). Mudutā aplasta esa rigidez, haciendo dóciles a los cetasikas y la conciencia."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 87); VI, §4 (p. 240)"
        },
        "seeAlso": ["kāyamudutā", "cittamudutā", "diṭṭhi", "māna", "lahutā", "kammaññatā"]
    },

    "kāyamudutā": {
        "meaning": {
            "pt": "Maleabilidade do corpo mental (dos cetasikas); o 12º dos 19 fatores universais belos (Cetasika #39 de 52), oposto a diṭṭhi e māna.",
            "en": "Malleability of the mental body (of cetasikas); the 12th of the 19 universal beautiful factors (Cetasika #39 of 52), opposed to diṭṭhi and māna.",
            "es": "Maleabilidad del cuerpo mental (de los cetasikas); el 12º de los 19 factores hermosos universales (Cetasika #39 de 52), opuesto a diṭṭhi y māna."
        },
        "grammar": "fem. (Chaṭṭhī-Tappurisa: kāya + mudutā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (Chaṭṭhī-Tappurisa: kāyassa mudutā)",
            "en": "Feminine noun (Chaṭṭhī-Tappurisa: kāyassa mudutā)",
            "es": "Sustantivo femenino (Chaṭṭhī-Tappurisa: kāyassa mudutā)"
        },
        "root": "kāya + mudu + tā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #39 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #39 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #39 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa — presente nos 59/91 sobhanacittas)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa — present in all 59/91 sobhanacittas)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa — presente en los 59/91 sobhanacittas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Abrandamento da rigidez no corpo mental (kāyathambhavūpasama-lakkhaṇa).",
                    "en": "Subsiding of rigidity in the mental body (kāyathambhavūpasama-lakkhaṇa).",
                    "es": "Apaciguamiento de la rigidez en el cuerpo mental (kāyathambhavūpasama-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Esmagar a rigidez do corpo mental (kāyathambhanimmaddana-rasa).",
                    "en": "To crush rigidity of the mental body (kāyathambhanimmaddana-rasa).",
                    "es": "Aplastar la rigidez del cuerpo mental (kāyathambhanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Não-resistência do corpo mental (kāyassa appaṭighāta-paccupaṭṭhāna).",
                    "en": "Non-resistance of the mental body (kāyassa appaṭighāta-paccupaṭṭhāna).",
                    "es": "No resistencia del cuerpo mental (kāyassa appaṭighāta-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O corpo mental (kāya-padaṭṭhāna).",
                    "en": "The mental body (kāya-padaṭṭhāna).",
                    "es": "El cuerpo mental (kāya-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Atua sempre em par com cittamudutā, eliminando o enrijecimento dogmático ou orgulhoso dos fatores mentais.",
                "en": "Always operates paired with cittamudutā, eliminating dogmatic or conceited stiffness in the mental factors.",
                "es": "Opera siempre en par con cittamudutā, eliminando la rigidez de los factores mentales."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 87)"
        },
        "seeAlso": ["cittamudutā", "mudutā", "diṭṭhi", "māna"]
    },

    "cittamudutā": {
        "meaning": {
            "pt": "Maleabilidade da consciência; o 13º dos 19 fatores universais belos (Cetasika #40 de 52), oposto a diṭṭhi e māna.",
            "en": "Malleability of consciousness; the 13th of the 19 universal beautiful factors (Cetasika #40 of 52), opposed to diṭṭhi and māna.",
            "es": "Maleabilidad de la conciencia; el 13º de los 19 factores hermosos universales (Cetasika #40 de 52), opuesto a diṭṭhi y māna."
        },
        "grammar": "fem. (Chaṭṭhī-Tappurisa: citta + mudutā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (Chaṭṭhī-Tappurisa: cittassa mudutā)",
            "en": "Feminine noun (Chaṭṭhī-Tappurisa: cittassa mudutā)",
            "es": "Sustantivo femenino (Chaṭṭhī-Tappurisa: cittassa mudutā)"
        },
        "root": "citta + mudu + tā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #40 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #40 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #40 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa — presente nos 59/91 sobhanacittas)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa — present in all 59/91 sobhanacittas)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa — presente en los 59/91 sobhanacittas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Abrandamento da rigidez na consciência (cittathambhavūpasama-lakkhaṇa).",
                    "en": "Subsiding of rigidity in consciousness (cittathambhavūpasama-lakkhaṇa).",
                    "es": "Apaciguamiento de la rigidez en la conciencia (cittathambhavūpasama-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Esmagar a rigidez da consciência (cittathambhanimmaddana-rasa).",
                    "en": "To crush rigidity of consciousness (cittathambhanimmaddana-rasa).",
                    "es": "Aplastar la rigidez de la conciencia (cittathambhanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Não-resistência da consciência (cittassa appaṭighāta-paccupaṭṭhāna).",
                    "en": "Non-resistance of consciousness (cittassa appaṭighāta-paccupaṭṭhāna).",
                    "es": "No resistencia de la conciencia (cittassa appaṭighāta-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "A consciência (citta-padaṭṭhāna).",
                    "en": "Consciousness (citta-padaṭṭhāna).",
                    "es": "La conciencia (citta-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Atua sempre em par com kāyamudutā em todas as consciências belas, tornando a consciência receptiva e livre de obstinação.",
                "en": "Always operates paired with kāyamudutā in all beautiful cittas, making consciousness receptive and free of obstinacy.",
                "es": "Opera siempre en par con kāyamudutā en todas las conciencias hermosas."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 87)"
        },
        "seeAlso": ["kāyamudutā", "mudutā", "diṭṭhi", "māna"]
    },

    "kammaññatā": {
        "meaning": {
            "pt": "Aptidão funcional; manejabilidade; prontidão para o trabalho espiritual; designa tanto o par de fatores mentais universais belos kāyakammaññatā (#41) e cittakammaññatā (#42), que se opõem aos demais obstáculos (kāmacchanda, vyāpāda, vicikicchā), quanto a propriedade material mutável rūpassa kammaññatā (Cap. VI, §4).",
            "en": "Wieldiness; workability; functional readiness for spiritual work; denotes both the pair of universal beautiful mental factors kāyakammaññatā (#41) and cittakammaññatā (#42), opposed to the remaining hindrances, and the mutable material phenomenon rūpassa kammaññatā (Ch. VI, §4).",
            "es": "Manejabilidad; aptitud funcional; disposición para el trabajo espiritual; designa tanto el par de factores mentales hermosos universales kāyakammaññatā (#41) y cittakammaññatā (#42) como la propiedad material mutable rūpassa kammaññatā (Cap. VI, §4)."
        },
        "grammar": "fem. (kammañña + tā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino abstrato (kammañña 'apto ao trabalho, manejável' + -tā)",
            "en": "Abstract feminine noun (kammañña 'fit for work, wieldy' + -tā)",
            "es": "Sustantivo femenino abstracto (kammañña 'apto para el trabajo, manejable' + -tā)"
        },
        "root": "√kar (fazer) > kamma + nya (> ñña) + tā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última Mental (Cetasikas #41 e #42 de 52) & Matéria Mutável (Vikārarūpa #24 de 28)",
                "en": "Mental Ultimate Reality (Cetasikas #41 and #42 of 52) & Mutable Matter (Vikārarūpa #24 of 28)",
                "es": "Realidad Última Mental (Cetasikas #41 y #42 de 52) y Materia Mutable (Vikārarūpa #24 de 28)"
            },
            "category": {
                "pt": "Universal Belo (Kāyakammaññatā + Cittakammaññatā); também Vikārarūpa (Rūpassa Kammaññatā)",
                "en": "Universal Beautiful (Kāyakammaññatā + Cittakammaññatā); also Vikārarūpa (Rūpassa Kammaññatā)",
                "es": "Universal Hermoso (Kāyakammaññatā + Cittakammaññatā); también Vikārarūpa (Rūpassa Kammaññatā)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Abrandamento da inaptidão funcional (akammaññabhāvavūpasama-lakkhaṇa) no corpo mental e na consciência.",
                    "en": "Subsiding of unwieldiness (akammaññabhāvavūpasama-lakkhaṇa) in the mental body and consciousness.",
                    "es": "Apaciguamiento de la falta de manejabilidad (akammaññabhāvavūpasama-lakkhaṇa) en el cuerpo mental y la conciencia."
                },
                "rasa": {
                    "pt": "Esmagar a inaptidão funcional (akammaññabhāvanimmaddana-rasa).",
                    "en": "To crush unwieldiness (akammaññabhāvanimmaddana-rasa).",
                    "es": "Aplastar la falta de manejabilidad (akammaññabhāvanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Êxito do corpo mental e da consciência em tomar algo como objeto e operar sobre ele (ārammaṇakaraṇasampatti-paccupaṭṭhāna).",
                    "en": "Success of the mental body and consciousness in making something an object (ārammaṇakaraṇasampatti-paccupaṭṭhāna).",
                    "es": "Éxito del cuerpo mental y la conciencia al hacer de algo un objeto (ārammaṇakaraṇasampatti-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O corpo mental e a consciência (kāyacitta-padaṭṭhāna).",
                    "en": "The mental body and consciousness (kāyacitta-padaṭṭhāna).",
                    "es": "El cuerpo mental y la conciencia (kāyacitta-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Comparada nos Comentários ao ouro puro refinado no fogo, que se torna totalmente manejável (kammañña) nas mãos do ourives para ser moldado em qualquer ornamento desejado (CMA II, §5, p. 87).",
                "en": "Compared in the Commentaries to pure gold refined in fire, which becomes completely wieldy and workable (kammañña) in the goldsmith's hands to be fashioned into any ornament (CMA II, §5, p. 87).",
                "es": "Comparada en los Comentarios al oro puro refinado en el fuego, que se vuelve totalmente manejable (kammañña) en manos del orfebre (CMA II, §5, p. 87)."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 87); VI, §4 (p. 240)"
        },
        "seeAlso": ["kāyakammaññatā", "cittakammaññatā", "lahutā", "mudutā", "pāguññatā"]
    },

    "kāyakammaññatā": {
        "meaning": {
            "pt": "Aptidão funcional (manejabilidade) do corpo mental (dos cetasikas); o 14º dos 19 fatores universais belos (Cetasika #41 de 52).",
            "en": "Wieldiness of the mental body (of cetasikas); the 14th of the 19 universal beautiful factors (Cetasika #41 of 52).",
            "es": "Manejabilidad del cuerpo mental (de los cetasikas); el 14º de los 19 factores hermosos universales (Cetasika #41 de 52)."
        },
        "grammar": "fem. (Chaṭṭhī-Tappurisa: kāya + kammaññatā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (Chaṭṭhī-Tappurisa: kāyassa kammaññatā)",
            "en": "Feminine noun (Chaṭṭhī-Tappurisa: kāyassa kammaññatā)",
            "es": "Sustantivo femenino (Chaṭṭhī-Tappurisa: kāyassa kammaññatā)"
        },
        "root": "kāya + kammañña + tā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #41 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #41 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #41 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa — presente nos 59/91 sobhanacittas)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa — present in all 59/91 sobhanacittas)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa — presente en los 59/91 sobhanacittas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Abrandamento da inaptidão funcional no corpo mental (kāyākammaññabhāvavūpasama-lakkhaṇa).",
                    "en": "Subsiding of unwieldiness in the mental body (kāyākammaññabhāvavūpasama-lakkhaṇa).",
                    "es": "Apaciguamiento de la falta de manejabilidad en el cuerpo mental (kāyākammaññabhāvavūpasama-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Esmagar a inaptidão funcional do corpo mental (kāyākammaññabhāvanimmaddana-rasa).",
                    "en": "To crush unwieldiness of the mental body (kāyākammaññabhāvanimmaddana-rasa).",
                    "es": "Aplastar la falta de manejabilidad del cuerpo mental (kāyākammaññabhāvanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Êxito do corpo mental em tomar um objeto (kāyassa ārammaṇakaraṇasampatti-paccupaṭṭhāna).",
                    "en": "Success of the mental body in making something an object (kāyassa ārammaṇakaraṇasampatti-paccupaṭṭhāna).",
                    "es": "Éxito del cuerpo mental al hacer de algo un objeto (kāyassa ārammaṇakaraṇasampatti-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O corpo mental (kāya-padaṭṭhāna).",
                    "en": "The mental body (kāya-padaṭṭhāna).",
                    "es": "El cuerpo mental (kāya-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Atua sempre em par com cittakammaññatā, opondo-se aos obstáculos que tornam os fatores mentais refratários às ações salutares.",
                "en": "Always operates paired with cittakammaññatā, opposing the hindrances that make mental factors refractory to wholesome action.",
                "es": "Opera siempre en par con cittakammaññatā, oponiéndose a los obstáculos restantes."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 87)"
        },
        "seeAlso": ["cittakammaññatā", "kammaññatā"]
    },

    "cittakammaññatā": {
        "meaning": {
            "pt": "Aptidão funcional (manejabilidade) da consciência; o 15º dos 19 fatores universais belos (Cetasika #42 de 52).",
            "en": "Wieldiness of consciousness; the 15th of the 19 universal beautiful factors (Cetasika #42 of 52).",
            "es": "Manejabilidad de la conciencia; el 15º de los 19 factores hermosos universales (Cetasika #42 de 52)."
        },
        "grammar": "fem. (Chaṭṭhī-Tappurisa: citta + kammaññatā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (Chaṭṭhī-Tappurisa: cittassa kammaññatā)",
            "en": "Feminine noun (Chaṭṭhī-Tappurisa: cittassa kammaññatā)",
            "es": "Sustantivo femenino (Chaṭṭhī-Tappurisa: cittassa kammaññatā)"
        },
        "root": "citta + kammañña + tā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #42 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #42 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #42 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa — presente nos 59/91 sobhanacittas)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa — present in all 59/91 sobhanacittas)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa — presente en los 59/91 sobhanacittas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Abrandamento da inaptidão funcional na consciência (cittākammaññabhāvavūpasama-lakkhaṇa).",
                    "en": "Subsiding of unwieldiness in consciousness (cittākammaññabhāvavūpasama-lakkhaṇa).",
                    "es": "Apaciguamiento de la falta de manejabilidad en la conciencia (cittākammaññabhāvavūpasama-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Esmagar a inaptidão funcional da consciência (cittākammaññabhāvanimmaddana-rasa).",
                    "en": "To crush unwieldiness of consciousness (cittākammaññabhāvanimmaddana-rasa).",
                    "es": "Aplastar la falta de manejabilidad de la conciencia (cittākammaññabhāvanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Êxito da consciência em tomar um objeto (cittassa ārammaṇakaraṇasampatti-paccupaṭṭhāna).",
                    "en": "Success of consciousness in making something an object (cittassa ārammaṇakaraṇasampatti-paccupaṭṭhāna).",
                    "es": "Éxito de la conciencia al hacer de algo un objeto (cittassa ārammaṇakaraṇasampatti-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "A consciência (citta-padaṭṭhāna).",
                    "en": "Consciousness (citta-padaṭṭhāna).",
                    "es": "La conciencia (citta-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Torna a consciência apta e dócil (kammaniya) para as mais elevadas realizações meditativas e cognitivas.",
                "en": "Makes consciousness fit and workable (kammaniya) for the highest meditative and cognitive realizations.",
                "es": "Hace que la conciencia sea apta y manejable para las realizaciones meditativas y cognitivas."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 87)"
        },
        "seeAlso": ["kāyakammaññatā", "kammaññatā"]
    },

    "pāguññatā": {
        "meaning": {
            "pt": "Proficiência; competência; saúde espiritual (ārogya) do corpo mental e da consciência; abrange o par de fatores universais belos kāyapāguññatā (#43) e cittapāguññatā (#44), opostos à falta de fé e demais enfermidades espirituais.",
            "en": "Proficiency; competence; spiritual healthiness (ārogya) of the mental body and consciousness; comprises the universal beautiful pair kāyapāguññatā (#43) and cittapāguññatā (#44), opposed to lack of faith and mental sickness.",
            "es": "Competencia; pericia; salud espiritual (ārogya) del cuerpo mental y la conciencia; comprende el par universal hermoso kāyapāguññatā (#43) y cittapāguññatā (#44), opuestos a la falta de fe y enfermedad mental."
        },
        "grammar": "fem. (paguṇa + ya + tā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino abstrato (de paguṇa 'proficiente, familiarizado, saudável' + -ya + -tā)",
            "en": "Abstract feminine noun (from paguṇa 'proficient, well-versed, healthy' + -ya + -tā)",
            "es": "Sustantivo femenino abstracto (de paguṇa 'competente, saludable' + -ya + -tā)"
        },
        "root": "pa + guṇa (qualidade / perícia) + ya + tā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Par de Fatores Mentais Universais Belos (Cetasikas #43 e #44 de 52)",
                "en": "Ultimate Reality — Pair of Universal Beautiful Mental Factors (Cetasikas #43 and #44 of 52)",
                "es": "Realidad Última — Par de Factores Mentales Hermosos Universales (Cetasikas #43 y #44 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa: Kāyapāguññatā + Cittapāguññatā)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa: Kāyapāguññatā + Cittapāguññatā)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa: Kāyapāguññatā + Cittapāguññatā)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Saúde ou robustez funcional do corpo mental e da consciência (kāyacittānaṃ ārogya-lakkhaṇa).",
                    "en": "Healthiness of the mental body and consciousness (kāyacittānaṃ ārogya-lakkhaṇa).",
                    "es": "Salud o robustez del cuerpo mental y la conciencia (kāyacittānaṃ ārogya-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Esmagar a enfermidade espiritual do corpo mental e da consciência (kāyacittagelaññanimmaddana-rasa).",
                    "en": "To crush unhealthiness of the mental body and consciousness (kāyacittagelaññanimmaddana-rasa).",
                    "es": "Aplastar la enfermedad del cuerpo mental y la conciencia (kāyacittagelaññanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Ausência de deficiência ou incapacidade (anādīnava-paccupaṭṭhāna).",
                    "en": "Absence of disability or defect (anādīnava-paccupaṭṭhāna).",
                    "es": "Ausencia de discapacidad o defecto (anādīnava-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O corpo mental e a consciência (kāyacitta-padaṭṭhāna).",
                    "en": "The mental body and consciousness (kāyacitta-padaṭṭhāna).",
                    "es": "El cuerpo mental y la conciencia (kāyacitta-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Enquanto lahutā, mudutā e kammaññatā têm contrapartes materiais (vikārarūpa), pāguññatā (proficiência/saúde) e ujjukatā (retidão) são qualidades exclusivamente mentais (cetasikas), pois a matéria inanimada não possui competência cognitiva nem integridade ética.",
                "en": "Whereas lahutā, mudutā, and kammaññatā have material counterparts (vikārarūpa), pāguññatā (proficiency) and ujjukatā (rectitude) are exclusively mental factors (cetasikas).",
                "es": "Mientras lahutā, mudutā y kammaññatā tienen contrapartes materiales (vikārarūpa), pāguññatā y ujjukatā son exclusivamente factores mentales."
            },
            "bodhiRef": "CMA II, §5 (Guide, pp. 87–88)"
        },
        "seeAlso": ["kāyapāguññatā", "cittapāguññatā", "saddhā", "ujjukatā"]
    },

    "kāyapāguññatā": {
        "meaning": {
            "pt": "Proficiência (saúde funcional) do corpo mental (dos cetasikas); o 16º dos 19 fatores universais belos (Cetasika #43 de 52).",
            "en": "Proficiency (healthiness) of the mental body (of cetasikas); the 16th of the 19 universal beautiful factors (Cetasika #43 of 52).",
            "es": "Competencia (salud funcional) del cuerpo mental (de los cetasikas); el 16º de los 19 factores hermosos universales (Cetasika #43 de 52)."
        },
        "grammar": "fem. (Chaṭṭhī-Tappurisa: kāya + pāguññatā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (Chaṭṭhī-Tappurisa: kāyassa pāguññatā)",
            "en": "Feminine noun (Chaṭṭhī-Tappurisa: kāyassa pāguññatā)",
            "es": "Sustantivo femenino (Chaṭṭhī-Tappurisa: kāyassa pāguññatā)"
        },
        "root": "kāya + paguṇa + ya + tā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #43 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #43 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #43 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa — presente nos 59/91 sobhanacittas)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa — present in all 59/91 sobhanacittas)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa — presente en los 59/91 sobhanacittas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Saúde funcional do corpo mental (kāyārogya-lakkhaṇa).",
                    "en": "Healthiness of the mental body (kāyārogya-lakkhaṇa).",
                    "es": "Salud funcional del cuerpo mental (kāyārogya-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Esmagar a enfermidade do corpo mental (kāyagelaññanimmaddana-rasa).",
                    "en": "To crush unhealthiness of the mental body (kāyagelaññanimmaddana-rasa).",
                    "es": "Aplastar la enfermedad del cuerpo mental (kāyagelaññanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Ausência de incapacidade no corpo mental (kāyassa anādīnava-paccupaṭṭhāna).",
                    "en": "Absence of disability in the mental body (kāyassa anādīnava-paccupaṭṭhāna).",
                    "es": "Ausencia de discapacidad en el cuerpo mental (kāyassa anādīnava-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O corpo mental (kāya-padaṭṭhāna).",
                    "en": "The mental body (kāya-padaṭṭhāna).",
                    "es": "El cuerpo mental (kāya-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Opõe-se à falta de fé (assaddhiya) e demais fraquezas que adoecem os fatores mentais.",
                "en": "Opposed to lack of faith (assaddhiya), etc., which cause unhealthiness of the mental body.",
                "es": "Se opone a la falta de fe (assaddhiya) que enferma el cuerpo mental."
            },
            "bodhiRef": "CMA II, §5 (Guide, pp. 87–88)"
        },
        "seeAlso": ["cittapāguññatā", "pāguññatā"]
    },

    "cittapāguññatā": {
        "meaning": {
            "pt": "Proficiência (saúde funcional) da consciência; o 17º dos 19 fatores universais belos (Cetasika #44 de 52).",
            "en": "Proficiency (healthiness) of consciousness; the 17th of the 19 universal beautiful factors (Cetasika #44 of 52).",
            "es": "Competencia (salud funcional) de la conciencia; el 17º de los 19 factores hermosos universales (Cetasika #44 de 52)."
        },
        "grammar": "fem. (Chaṭṭhī-Tappurisa: citta + pāguññatā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (Chaṭṭhī-Tappurisa: cittassa pāguññatā)",
            "en": "Feminine noun (Chaṭṭhī-Tappurisa: cittassa pāguññatā)",
            "es": "Sustantivo femenino (Chaṭṭhī-Tappurisa: cittassa pāguññatā)"
        },
        "root": "citta + paguṇa + ya + tā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #44 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #44 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #44 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa — presente nos 59/91 sobhanacittas)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa — present in all 59/91 sobhanacittas)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa — presente en los 59/91 sobhanacittas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Saúde funcional da consciência (cittārogya-lakkhaṇa).",
                    "en": "Healthiness of consciousness (cittārogya-lakkhaṇa).",
                    "es": "Salud funcional de la conciencia (cittārogya-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Esmagar a enfermidade da consciência (cittagelaññanimmaddana-rasa).",
                    "en": "To crush unhealthiness of consciousness (cittagelaññanimmaddana-rasa).",
                    "es": "Aplastar la enfermedad de la conciencia (cittagelaññanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Ausência de incapacidade na consciência (cittassa anādīnava-paccupaṭṭhāna).",
                    "en": "Absence of disability in consciousness (cittassa anādīnava-paccupaṭṭhāna).",
                    "es": "Ausencia de discapacidad en la conciencia (cittassa anādīnava-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "A consciência (citta-padaṭṭhāna).",
                    "en": "Consciousness (citta-padaṭṭhāna).",
                    "es": "La conciencia (citta-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Atua sempre em par com kāyapāguññatā em todos os cittas belos.",
                "en": "Always operates paired with kāyapāguññatā in all beautiful cittas.",
                "es": "Opera siempre en par con kāyapāguññatā en todos los cittas hermosos."
            },
            "bodhiRef": "CMA II, §5 (Guide, pp. 87–88)"
        },
        "seeAlso": ["kāyapāguññatā", "pāguññatā"]
    },

    "ujjukatā": {
        "meaning": {
            "pt": "Retidão; sinceridade; integridade; ausência de tortuosidade (ajimhatā); abrange o par de fatores mentais universais belos kāyujjukatā (#45) e cittujjukatā (#46), opostos à fraude (māyā) e à hipocrisia (sāṭheyya).",
            "en": "Rectitude; straightness; uprightness; absence of crookedness (ajimhatā); comprises the universal beautiful pair kāyujjukatā (#45) and cittujjukatā (#46), opposed to fraudulence (māyā) and hypocrisy (sāṭheyya).",
            "es": "Rectitud; sinceridad; integridad; ausencia de tortuosidad (ajimhatā); comprende el par universal hermoso kāyujjukatā (#45) y cittujjukatā (#46), opuestos al fraude (māyā) y la hipocresía (sāṭheyya)."
        },
        "grammar": "fem. (ujjuka + tā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino abstrato (de uju / ujjuka 'reto, direto, honesto' + -tā)",
            "en": "Abstract feminine noun (from uju / ujjuka 'straight, upright, honest' + -tā)",
            "es": "Sustantivo femenino abstracto (de uju / ujjuka 'recto, directo, honesto' + -tā)"
        },
        "root": "√uj (ser reto / direto) > ujjuka + tā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Par de Fatores Mentais Universais Belos (Cetasikas #45 e #46 de 52)",
                "en": "Ultimate Reality — Pair of Universal Beautiful Mental Factors (Cetasikas #45 and #46 of 52)",
                "es": "Realidad Última — Par de Factores Mentales Hermosos Universales (Cetasikas #45 y #46 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa: Kāyujjukatā + Cittujjukatā)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa: Kāyujjukatā + Cittujjukatā)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa: Kāyujjukatā + Cittujjukatā)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Retidão ou honestidade do corpo mental e da consciência (kāyacittānaṃ ajjava-lakkhaṇa).",
                    "en": "Uprightness of the mental body and consciousness (kāyacittānaṃ ajjava-lakkhaṇa).",
                    "es": "Rectitud u honestidad del cuerpo mental y la conciencia (kāyacittānaṃ ajjava-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Esmagar a tortuosidade e dissimulação do corpo mental e da consciência (kāyacittakuṭilabhāvanimmaddana-rasa).",
                    "en": "To crush tortuousness of the mental body and consciousness (kāyacittakuṭilabhāvanimmaddana-rasa).",
                    "es": "Aplastar la tortuosidad del cuerpo mental y la conciencia (kāyacittakuṭilabhāvanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Ausência de obliquidade ou não-tortuosidade (ajimhatā-paccupaṭṭhāna).",
                    "en": "Non-crookedness (ajimhatā-paccupaṭṭhāna).",
                    "es": "Ausencia de doblez o no tortuosidad (ajimhatā-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O corpo mental e a consciência (kāyacitta-padaṭṭhāna).",
                    "en": "The mental body and consciousness (kāyacitta-padaṭṭhāna).",
                    "es": "El cuerpo mental y la conciencia (kāyacitta-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Como explica Bhikkhu Bodhi (CMA II, §5, p. 88), ujjukatā opõe-se diretamente à dissimulação/fraude (māyā, que oculta os próprios defeitos) e à hipocrisia/pretensão (sāṭheyya, que finge possuir virtudes inexistentes), estados derivados da cobiça (lobha) e da visão errônea (diṭṭhi) que entortam a mente.",
                "en": "As Bhikkhu Bodhi explains (CMA II, §5, p. 88), ujjukatā is directly opposed to deceit/fraudulence (māyā, concealing one's faults) and hypocrisy (sāṭheyya, pretending to possess virtues one lacks), states derived from greed and wrong view that make the mind crooked.",
                "es": "Como explica Bhikkhu Bodhi (CMA II, §5, p. 88), ujjukatā se opone directamente al engaño (māyā) y la hipocresía (sāṭheyya), que tuercen el cuerpo mental y la conciencia."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 88)"
        },
        "seeAlso": ["kāyujjukatā", "cittujjukatā", "pāguññatā", "hiri", "ottappa"]
    },

    "kāyujjukatā": {
        "meaning": {
            "pt": "Retidão do corpo mental (dos cetasikas); o 18º dos 19 fatores universais belos (Cetasika #45 de 52).",
            "en": "Rectitude of the mental body (of cetasikas); the 18th of the 19 universal beautiful factors (Cetasika #45 of 52).",
            "es": "Rectitud del cuerpo mental (de los cetasikas); el 18º de los 19 factores hermosos universales (Cetasika #45 de 52)."
        },
        "grammar": "fem. (Chaṭṭhī-Tappurisa: kāya + ujjukatā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (Chaṭṭhī-Tappurisa com sandhi: kāya + ujjukatā)",
            "en": "Feminine noun (Chaṭṭhī-Tappurisa with sandhi: kāya + ujjukatā)",
            "es": "Sustantivo femenino (Chaṭṭhī-Tappurisa con sandhi: kāya + ujjukatā)"
        },
        "root": "kāya + ujjuka + tā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #45 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #45 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #45 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa — presente nos 59/91 sobhanacittas)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa — present in all 59/91 sobhanacittas)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa — presente en los 59/91 sobhanacittas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Retidão do corpo mental (kāyajjava-lakkhaṇa).",
                    "en": "Uprightness of the mental body (kāyajjava-lakkhaṇa).",
                    "es": "Rectitud del cuerpo mental (kāyajjava-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Esmagar a tortuosidade do corpo mental (kāyakuṭilabhāvanimmaddana-rasa).",
                    "en": "To crush tortuousness of the mental body (kāyakuṭilabhāvanimmaddana-rasa).",
                    "es": "Aplastar la tortuosidad del cuerpo mental (kāyakuṭilabhāvanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Não-tortuosidade do corpo mental (kāyassa ajimhatā-paccupaṭṭhāna).",
                    "en": "Non-crookedness of the mental body (kāyassa ajimhatā-paccupaṭṭhāna).",
                    "es": "No tortuosidad del cuerpo mental (kāyassa ajimhatā-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "O corpo mental (kāya-padaṭṭhāna).",
                    "en": "The mental body (kāya-padaṭṭhāna).",
                    "es": "El cuerpo mental (kāya-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Atua sempre em par com cittujjukatā em todos os cittas belos, eliminando a hipocrisia e a fraude dos cetasikas.",
                "en": "Always operates paired with cittujjukatā in all beautiful cittas, eliminating hypocrisy and fraudulence from the cetasikas.",
                "es": "Opera siempre en par con cittujjukatā en todos los cittas hermosos."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 88)"
        },
        "seeAlso": ["cittujjukatā", "ujjukatā"]
    },

    "cittujjukatā": {
        "meaning": {
            "pt": "Retidão da consciência; o 19º dos 19 fatores universais belos (Cetasika #46 de 52).",
            "en": "Rectitude of consciousness; the 19th of the 19 universal beautiful factors (Cetasika #46 of 52).",
            "es": "Rectitud de la conciencia; el 19º de los 19 factores hermosos universales (Cetasika #46 de 52)."
        },
        "grammar": "fem. (Chaṭṭhī-Tappurisa: citta + ujjukatā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (Chaṭṭhī-Tappurisa com sandhi: citta + ujjukatā)",
            "en": "Feminine noun (Chaṭṭhī-Tappurisa with sandhi: citta + ujjukatā)",
            "es": "Sustantivo femenino (Chaṭṭhī-Tappurisa con sandhi: citta + ujjukatā)"
        },
        "root": "citta + ujjuka + tā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Universal Belo (Cetasika #46 de 52)",
                "en": "Ultimate Reality — Universal Beautiful Mental Factor (Cetasika #46 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Universal (Cetasika #46 de 52)"
            },
            "category": {
                "pt": "Universal Belo (Sobhanasādhāraṇa — presente nos 59/91 sobhanacittas)",
                "en": "Universal Beautiful (Sobhanasādhāraṇa — present in all 59/91 sobhanacittas)",
                "es": "Universal Hermoso (Sobhanasādhāraṇa — presente en los 59/91 sobhanacittas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Retidão da consciência (cittajjava-lakkhaṇa).",
                    "en": "Uprightness of consciousness (cittajjava-lakkhaṇa).",
                    "es": "Rectitud de la conciencia (cittajjava-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Esmagar a tortuosidade da consciência (cittakuṭilabhāvanimmaddana-rasa).",
                    "en": "To crush tortuousness of consciousness (cittakuṭilabhāvanimmaddana-rasa).",
                    "es": "Aplastar la tortuosidad de la conciencia (cittakuṭilabhāvanimmaddana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Não-tortuosidade da consciência (cittassa ajimhatā-paccupaṭṭhāna).",
                    "en": "Non-crookedness of consciousness (cittassa ajimhatā-paccupaṭṭhāna).",
                    "es": "No tortuosidad de la conciencia (cittassa ajimhatā-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "A consciência (citta-padaṭṭhāna).",
                    "en": "Consciousness (citta-padaṭṭhāna).",
                    "es": "La conciencia (citta-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Encerra a lista dos 19 fatores universais belos (sobhanasādhāraṇa) que acompanham invariavelmente toda consciência bela.",
                "en": "Concludes the list of the 19 universal beautiful factors (sobhanasādhāraṇa) that invariably accompany every beautiful consciousness.",
                "es": "Cierra la lista de los 19 factores hermosos universales (sobhanasādhāraṇa)."
            },
            "bodhiRef": "CMA II, §5 (Guide, p. 88)"
        },
        "seeAlso": ["kāyujjukatā", "ujjukatā", "sobhanasādhāraṇa"]
    },

    "virati": {
        "meaning": {
            "pt": "Abstinência; refreamento ético deliberado; o grupo de 3 fatores mentais belos variáveis (sammāvācā, sammākammanta, sammā-ājīva) que constituem o grupo da virtude (sīlakkhandha) do Nobre Caminho Óctuplo.",
            "en": "Abstinence; deliberate ethical restraint; the group of 3 variable beautiful mental factors (sammāvācā, sammākammanta, sammā-ājīva) that constitute the morality group (sīlakkhandha) of the Noble Eightfold Path.",
            "es": "Abstinencia; refrenamiento ético deliberado; el grupo de 3 factores mentales hermosos variables (sammāvācā, sammākammanta, sammā-ājīva) que constituyen el grupo de la virtud (sīlakkhandha) del Noble Camino Óctuple."
        },
        "grammar": "fem. (vi + √ram + ti)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (vi 'afastar-se de' + √ram 'deleitar-se' + ti: cessar de deleitar-se no mal, abster-se)",
            "en": "Feminine noun (vi 'away from' + √ram 'to delight' + ti: to desist, abstain)",
            "es": "Sustantivo femenino (vi 'apartarse de' + √ram 'deleitarse' + ti: desistir, abstenerse)"
        },
        "root": "vi + √ram (abster-se / desistir) + ti",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Grupo de 3 Fatores Mentais Belos Variáveis (Cetasikas #47–#49 de 52)",
                "en": "Ultimate Reality — Group of 3 Variable Beautiful Mental Factors (Cetasikas #47–#49 of 52)",
                "es": "Realidad Última — Grupo de 3 Factores Mentales Hermosos Variables (Cetasikas #47–#49 de 52)"
            },
            "category": {
                "pt": "3 Viratiyo: Sammāvācā (#47), Sammākammanta (#48), Sammā-ājīva (#49). Variáveis (aniyatayogī, separadas) nos 8 mahākusalacittas; fixas e simultâneas (niyata-ekato) nos 8/40 lokuttaracittas",
                "en": "3 Viratiyo: Sammāvācā (#47), Sammākammanta (#48), Sammā-ājīva (#49). Variable and separate in the 8 mahākusalacittas; fixed and simultaneous in the 8/40 lokuttaracittas",
                "es": "3 Viratiyo: Sammāvācā (#47), Sammākammanta (#48), Sammā-ājīva (#49). Variables y separadas en los 8 mahākusalacittas; fijas y simultáneas en los 8/40 lokuttaracittas"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Não-transgressão (avītikkama-lakkhaṇa) ou não pisar sobre o campo da má conduta verbal, corporal e de meio de vida.",
                    "en": "Non-transgression (avītikkama-lakkhaṇa) in the fields of wrong speech, wrong bodily action, and wrong livelihood.",
                    "es": "No transgresión (avītikkama-lakkhaṇa) en los campos del habla incorrecta, la acción corporal incorrecta y el medio de vida incorrecto."
                },
                "rasa": {
                    "pt": "Recuar diante das ocasiões de má conduta (duccaritato saṅkocana-rasa).",
                    "en": "To shrink back from evil deeds (duccaritato saṅkocana-rasa).",
                    "es": "Retroceder ante las malas acciones (duccaritato saṅkocana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Abster-se de tais ações prejudiciais (akiriyā-paccupaṭṭhāna / viramana-paccupaṭṭhāna).",
                    "en": "Abstinence from such evil deeds (akiriyā-paccupaṭṭhāna / viramana-paccupaṭṭhāna).",
                    "es": "Abstinencia de tales malas acciones (akiriyā-paccupaṭṭhāna / viramana-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "As qualidades especiais de fé (saddhā), pudor moral (hiri), temor moral (ottappa) e modéstia de desejos (appicchatā).",
                    "en": "The special qualities of faith (saddhā), shame (hiri), fear of wrongdoing (ottappa), fewness of wishes (appicchatā), etc.",
                    "es": "Las cualidades especiales de fe (saddhā), pudor moral (hiri), temor moral (ottappa) y pocos deseos (appicchatā)."
                }
            },
            "philosophy": {
                "pt": "Exegese fundamental de Bhikkhu Bodhi (CMA II, §6 & §15, pp. 88–89, 99): existem 3 modos de virati: (1) sampattavirati (abstinência natural ao deparar-se com uma oportunidade de transgressão, por respeito à própria dignidade); (2) samādānavirati (abstinência por ter assumido preceitos, ex: Pañcasīla); e (3) samucchedavirati (abstinência por erradicação, supramundana). Nas consciências mundanas (apenas nos 8 mahākusalacittas), as três viratis surgem apenas uma de cada vez (paccekam) e somente quando surge oportunidade real de transgressão da qual a pessoa deliberadamente se abstém. Já nos 8/40 cittas supramundanos (lokuttara), todas as três viratis surgem juntas (ekato) e invariavelmente (niyatā) num único instante de consciência — mesmo tendo Nibbāna como objeto — porque o caminho supramundano corta simultaneamente a raiz da tríplice transgressão!",
                "en": "Fundamental exegesis by Bhikkhu Bodhi (CMA II, §6 & §15, pp. 88–89, 99): there are 3 types of virati: (1) sampattavirati (natural abstinence when an opportunity for transgression arises); (2) samādānavirati (abstinence by undertaking precepts); and (3) samucchedavirati (abstinence by eradication, supramundane). In mundane consciousness (only the 8 mahākusalacittas), the three viratis arise only one at a time (paccekam) and only when one intentionally refrains from an actual opportunity for wrongdoing. In the 8/40 supramundane (lokuttara) cittas, however, all three viratis are invariably present together (niyatā ekato) in a single moment, cutting off the tendencies toward the threefold misconduct simultaneously!",
                "es": "Exégesis fundamental de Bhikkhu Bodhi (CMA II, §6 y §15, pp. 88–89, 99): existen 3 tipos de virati: sampattavirati (natural), samādānavirati (por preceptos) y samucchedavirati (por erradicación, supramundana). En los 8 mahākusalacittas surgen separadamente solo ante una oportunidad de transgresión; en los 8/40 lokuttaracittas surgen las tres juntas e invariablemente."
            },
            "bodhiRef": "CMA II, §6 & §15 (Guide, pp. 88–89, 99)"
        },
        "seeAlso": ["sammāvācā", "sammākammanta", "sammā-ājīva", "sīla", "lokuttara", "magga"]
    },

    "sammāvācā": {
        "meaning": {
            "pt": "Linguagem correta; fala reta; a 1ª das 3 abstinências (virati, Cetasika #47 de 52) e 3º fator do Nobre Caminho Óctuplo: a abstinência deliberada das quatro formas de linguagem prejudicial (mentira, calúnia/intriga, fala grosseira e conversa frívola).",
            "en": "Right speech; the 1st of the 3 abstinences (virati, Cetasika #47 of 52) and 3rd factor of the Noble Eightfold Path: deliberate abstinence from the four forms of wrong speech (false speech, slander, harsh speech, and frivolous talk).",
            "es": "Habla correcta; lenguaje recto; la 1ª de las 3 abstinencias (virati, Cetasika #47 de 52) y 3º factor del Noble Camino Óctuple: abstinencia deliberada de las cuatro formas de habla incorrecta (mentira, calumnia, habla áspera y charla frívola)."
        },
        "grammar": "fem. (Kammadhāraya: sammā + vācā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (Kammadhāraya: sammā 'correta, elogiável' + vācā 'fala, linguagem')",
            "en": "Feminine noun (Kammadhāraya: sammā 'right, praiseworthy' + vācā 'speech')",
            "es": "Sustantivo femenino (Kammadhāraya: sammā 'correcta, loable' + vācā 'habla')"
        },
        "root": "sammā (corretamente) + √vac (falar) + ā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Belo Variável / Abstinência (Cetasika #47 de 52)",
                "en": "Ultimate Reality — Variable Beautiful Mental Factor / Abstinence (Cetasika #47 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Variable / Abstinencia (Cetasika #47 de 52)"
            },
            "category": {
                "pt": "Abstinência (Virati — presente ocasionalmente nos 8 mahākusalacittas e invariavelmente nos 8/40 lokuttaracittas); 3º Fator do Nobre Caminho Óctuplo (Maggaṅga)",
                "en": "Abstinence (Virati — occasionally present in the 8 mahākusalacittas and invariably in the 8/40 lokuttaracittas); 3rd Factor of the Noble Eightfold Path (Maggaṅga)",
                "es": "Abstinencia (Virati — ocasionalmente en los 8 mahākusalacittas e invariablemente en los 8/40 lokuttaracittas); 3º Factor del Noble Camino Óctuple (Maggaṅga)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Não-transgressão na esfera da má conduta verbal (vacīduccaritāvītikkama-lakkhaṇa).",
                    "en": "Non-transgression by way of wrong speech (vacīduccaritāvītikkama-lakkhaṇa).",
                    "es": "No transgresión por medio del habla incorrecta (vacīduccaritāvītikkama-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Recuar diante da fala prejudicial (vacīduccaritato saṅkocana-rasa).",
                    "en": "To shrink back from wrong speech (vacīduccaritato saṅkocana-rasa).",
                    "es": "Retroceder ante el habla incorrecta (vacīduccaritato saṅkocana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Abstenção das quatro formas de má conduta verbal (musāvādādīhi viramana-paccupaṭṭhāna).",
                    "en": "Abstinence from the four kinds of wrong speech (musāvādādīhi viramana-paccupaṭṭhāna).",
                    "es": "Abstinencia de las cuatro formas de habla incorrecta (musāvādādīhi viramana-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Fé (saddhā), pudor moral (hiri), temor moral (ottappa), etc.",
                    "en": "Faith (saddhā), shame (hiri), fear of wrongdoing (ottappa), etc.",
                    "es": "Fe (saddhā), pudor moral (hiri), temor moral (ottappa), etc."
                }
            },
            "philosophy": {
                "pt": "Abstém-se de musāvāda (mentira), pisuṇāvācā (fala divisiva/caluniosa), pharusāvācā (fala áspera/ofensiva) e samphappalāpa (conversa vã/frívola), desde que essa transgressão não pertença ao meio de vida da pessoa (caso em que a abstinência é exercida por sammā-ājīva).",
                "en": "Refrains from false speech (musāvāda), slanderous speech (pisuṇāvācā), harsh speech (pharusāvācā), and frivolous talk (samphappalāpa), provided such speech does not pertain to one's livelihood (in which case the restraint is exercised by sammā-ājīva).",
                "es": "Se abstiene de la mentira (musāvāda), la calumnia (pisuṇāvācā), el habla áspera (pharusāvācā) y la charla frívola (samphappalāpa)."
            },
            "bodhiRef": "CMA II, §6 & §15 (Guide, pp. 88–89, 99); VII, §29 (p. 280)"
        },
        "seeAlso": ["virati", "sammākammanta", "sammā-ājīva", "vacīviññatti", "magga"]
    },

    "sammākammanta": {
        "meaning": {
            "pt": "Ação correta; conduta corporal reta; a 2ª das 3 abstinências (virati, Cetasika #48 de 52) e 4º fator do Nobre Caminho Óctuplo: a abstinência deliberada das três formas de má conduta corporal (matar seres vivos, tomar o que não foi dado e conduta sexual imprópria).",
            "en": "Right action; right bodily conduct; the 2nd of the 3 abstinences (virati, Cetasika #48 of 52) and 4th factor of the Noble Eightfold Path: deliberate abstinence from the three forms of wrong bodily action (killing, stealing, and sexual misconduct).",
            "es": "Acción correcta; conducta corporal recta; la 2ª de las 3 abstinencias (virati, Cetasika #48 de 52) y 4º factor del Noble Camino Óctuple: abstinencia deliberada de las tres formas de mala conducta corporal (matar, robar y conducta sexual inapropiada)."
        },
        "grammar": "masc. (Kammadhāraya: sammā + kammanta)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (Kammadhāraya: sammā 'correta' + kammanta 'ação, atividade')",
            "en": "Masculine noun (Kammadhāraya: sammā 'right' + kammanta 'action, work')",
            "es": "Sustantivo masculino (Kammadhāraya: sammā 'correcta' + kammanta 'acción, actividad')"
        },
        "root": "sammā (corretamente) + √kar (fazer) > kammanta",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Belo Variável / Abstinência (Cetasika #48 de 52)",
                "en": "Ultimate Reality — Variable Beautiful Mental Factor / Abstinence (Cetasika #48 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Variable / Abstinencia (Cetasika #48 de 52)"
            },
            "category": {
                "pt": "Abstinência (Virati — presente ocasionalmente nos 8 mahākusalacittas e invariavelmente nos 8/40 lokuttaracittas); 4º Fator do Nobre Caminho Óctuplo (Maggaṅga)",
                "en": "Abstinence (Virati — occasionally present in the 8 mahākusalacittas and invariably in the 8/40 lokuttaracittas); 4th Factor of the Noble Eightfold Path (Maggaṅga)",
                "es": "Abstinencia (Virati — ocasionalmente en los 8 mahākusalacittas e invariablemente en los 8/40 lokuttaracittas); 4º Factor del Noble Camino Óctuple (Maggaṅga)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Não-transgressão na esfera da má conduta corporal (kāyaduccaritāvītikkama-lakkhaṇa).",
                    "en": "Non-transgression by way of wrong bodily action (kāyaduccaritāvītikkama-lakkhaṇa).",
                    "es": "No transgresión por medio de la mala conducta corporal (kāyaduccaritāvītikkama-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Recuar diante da má conduta corporal (kāyaduccaritato saṅkocana-rasa).",
                    "en": "To shrink back from wrong bodily action (kāyaduccaritato saṅkocana-rasa).",
                    "es": "Retroceder ante la mala conducta corporal (kāyaduccaritato saṅkocana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Abstenção de matar (pāṇātipāta), furtar (adinnādāna) e conduta sexual imprópria (kāmesumicchācāra).",
                    "en": "Abstinence from killing (pāṇātipāta), stealing (adinnādāna), and sexual misconduct (kāmesumicchācāra).",
                    "es": "Abstinencia de matar (pāṇātipāta), robar (adinnādāna) y conducta sexual incorrecta (kāmesumicchācāra)."
                },
                "padatthana": {
                    "pt": "Fé (saddhā), pudor moral (hiri), temor moral (ottappa), etc.",
                    "en": "Faith (saddhā), shame (hiri), fear of wrongdoing (ottappa), etc.",
                    "es": "Fe (saddhā), pudor moral (hiri), temor moral (ottappa), etc."
                }
            },
            "philosophy": {
                "pt": "No Abhidhamma, sammākammanta como cetasika específico refere-se à abstinência das três transgressões corporais (pāṇātipāta, adinnādāna, kāmesumicchācāra) quando não vinculadas ao sustento econômico. Nos cittas supramundanos, erradica definitivamente a propensão a essas transgressões.",
                "en": "In the Abhidhamma, sammākammanta as a distinct cetasika refers to abstinence from the three bodily transgressions (killing, stealing, sexual misconduct) when not bound up with one's livelihood. In supramundane cittas, it permanently eradicates the disposition toward such deeds.",
                "es": "En el Abhidhamma, sammākammanta se refiere a la abstinencia de las tres transgresiones corporales cuando no están ligadas al medio de vida."
            },
            "bodhiRef": "CMA II, §6 & §15 (Guide, pp. 88–89, 99); VII, §29 (p. 280)"
        },
        "seeAlso": ["virati", "sammāvācā", "sammā-ājīva", "kāyaviññatti", "magga"]
    },

    "sammā-ājīva": {
        "meaning": {
            "pt": "Meio de vida correto; sustento reto; a 3ª das 3 abstinências (virati, Cetasika #49 de 52) e 5º fator do Nobre Caminho Óctuplo: a abstinência deliberada de ganhar a vida por meio de conduta verbal ou corporal prejudicial (como comércio de armas, seres vivos, carne para abate, intoxicantes ou venenos).",
            "en": "Right livelihood; the 3rd of the 3 abstinences (virati, Cetasika #49 of 52) and 5th factor of the Noble Eightfold Path: deliberate abstinence from wrong livelihood involving unwholesome speech or bodily action (such as dealing in weapons, slaves, animals for slaughter, intoxicants, or poisons).",
            "es": "Medio de vida correcto; sustento recto; la 3ª de las 3 abstinencias (virati, Cetasika #49 de 52) y 5º factor del Noble Camino Óctuple: abstinencia deliberada de medios de vida perjudiciales (comercio de armas, seres vivos, animales para matanza, intoxicantes o venenos)."
        },
        "grammar": "masc. (Kammadhāraya: sammā + ājīva)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (Kammadhāraya: sammā 'correto' + ājīva 'modo de vida, sustento')",
            "en": "Masculine noun (Kammadhāraya: sammā 'right' + ājīva 'livelihood')",
            "es": "Sustantivo masculino (Kammadhāraya: sammā 'correcto' + ājīva 'medio de vida')"
        },
        "root": "sammā + ā + √jīv (viver / sustentar-se) + a",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Belo Variável / Abstinência (Cetasika #49 de 52)",
                "en": "Ultimate Reality — Variable Beautiful Mental Factor / Abstinence (Cetasika #49 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Variable / Abstinencia (Cetasika #49 de 52)"
            },
            "category": {
                "pt": "Abstinência (Virati — presente ocasionalmente nos 8 mahākusalacittas e invariavelmente nos 8/40 lokuttaracittas); 5º Fator do Nobre Caminho Óctuplo (Maggaṅga)",
                "en": "Abstinence (Virati — occasionally present in the 8 mahākusalacittas and invariably in the 8/40 lokuttaracittas); 5th Factor of the Noble Eightfold Path (Maggaṅga)",
                "es": "Abstinencia (Virati — ocasionalmente en los 8 mahākusalacittas e invariablemente en los 8/40 lokuttaracittas); 5º Factor del Noble Camino Óctuple (Maggaṅga)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Não-transgressão na esfera do meio de vida incorreto (micchājīvāvītikkama-lakkhaṇa).",
                    "en": "Non-transgression by way of wrong livelihood (micchājīvāvītikkama-lakkhaṇa).",
                    "es": "No transgresión en el ámbito del medio de vida incorrecto (micchājīvāvītikkama-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Recuar diante do sustento ilícito ou prejudicial (micchājīvato saṅkocana-rasa).",
                    "en": "To shrink back from wrong livelihood (micchājīvato saṅkocana-rasa).",
                    "es": "Retroceder ante el medio de vida incorrecto (micchājīvato saṅkocana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Abstenção de ganhar a vida mediante as sete formas de transgressão corporal e verbal.",
                    "en": "Abstinence from earning one's living through the seven kinds of bodily and verbal transgression.",
                    "es": "Abstinencia de ganarse la vida mediante las siete formas de transgresión corporal y verbal."
                },
                "padatthana": {
                    "pt": "Fé (saddhā), pudor moral (hiri), temor moral (ottappa), contentamento e modéstia de desejos (appicchatā).",
                    "en": "Faith (saddhā), shame (hiri), fear of wrongdoing (ottappa), contentment, and fewness of wishes (appicchatā).",
                    "es": "Fe (saddhā), pudor moral (hiri), temor moral (ottappa) y pocos deseos (appicchatā)."
                }
            },
            "philosophy": {
                "pt": "Embora toda má conduta no sustento ocorra através da porta do corpo ou da fala, o Abhidhamma distingue sammā-ājīva como um cetasika próprio porque sua esfera causal é especificamente a purificação do meio de subsistência (ājīvapārisuddhi).",
                "en": "Although wrong livelihood always occurs through the bodily or vocal door, the Abhidhamma distinguishes sammā-ājīva as a separate cetasika because its specific domain is the purification of one's means of subsistence (ājīvapārisuddhi).",
                "es": "Aunque el medio de vida incorrecto ocurre por vía corporal o verbal, el Abhidhamma distingue sammā-ājīva como un cetasika propio encargado de purificar el sustento."
            },
            "bodhiRef": "CMA II, §6 & §15 (Guide, pp. 88–89, 99); VII, §29 (p. 280)"
        },
        "seeAlso": ["virati", "sammāvācā", "sammākammanta", "magga"]
    },

    "appamaññā": {
        "meaning": {
            "pt": "Os Incomensuráveis (ou Ilimitados); as quatro atitudes sublimes (brahmavihāra: mettā, karuṇā, muditā, upekkhā) irradiadas sem fronteiras para todos os seres sencientes. Como cetasikas distintos no Cap. II (§7), designam especificamente karuṇā (#50) e muditā (#51).",
            "en": "The Illimitables (or Immeasurables); the four sublime attitudes (brahmavihāra: mettā, karuṇā, muditā, upekkhā) radiated boundlessly toward all living beings. As distinct cetasikas in Ch. II (§7), the term specifically denotes karuṇā (#50) and muditā (#51).",
            "es": "Los Inconmensurables (o Ilimitados); las cuatro actitudes sublimes (brahmavihāra: mettā, karuṇā, muditā, upekkhā) irradiadas sin límites hacia todos los seres vivos. Como cetasikas propios en el Cap. II (§7), designan específicamente karuṇā (#50) y muditā (#51)."
        },
        "grammar": "fem. pl. (na > a + pamāṇa + ya + ā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (na > a 'sem' + pamāṇa 'medida, limite' + -ya: aquilo que tem alcance ilimitado)",
            "en": "Feminine noun (na > a 'without' + pamāṇa 'measure, limit' + -ya: that which has a limitless range)",
            "es": "Sustantivo femenino (na > a 'sin' + pamāṇa 'medida, límite' + -ya: lo que tiene alcance ilimitado)"
        },
        "root": "na > a + pa + √mā (medir) + aṇa + ya",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — 2 Cetasikas Próprios (Karuṇā #50, Muditā #51) + 2 Modos de Universais Belos (Adosa = Mettā, Tatramajjhattatā = Upekkhā)",
                "en": "Ultimate Reality — 2 Distinct Cetasikas (Karuṇā #50, Muditā #51) + 2 Modes of Universal Beautiful Factors (Adosa = Mettā, Tatramajjhattatā = Upekkhā)",
                "es": "Realidad Última — 2 Cetasikas Propios (Karuṇā #50, Muditā #51) + 2 Modos de Hermosos Universales (Adosa = Mettā, Tatramajjhattatā = Upekkhā)"
            },
            "category": {
                "pt": "Presentes (separadamente, kadāci) em 28 cittas: 8 mahākusala, 8 mahākiriya e os 12 cittas dos 4 primeiros jhānas rūpāvacara (ausentes no 5º jhāna, que tem upekkhā, e nos cittas lokuttara, cujo objeto é Nibbāna e não seres conceitos)",
                "en": "Present (separately, kadāci) in 28 cittas: 8 mahākusala, 8 mahākiriya, and the 12 cittas of the first 4 rūpāvacara jhānas (absent in the 5th jhāna, which has upekkhā, and in lokuttara cittas, whose object is Nibbāna rather than conceptual beings)",
                "es": "Presentes (separadamente, kadāci) en 28 cittas: 8 mahākusala, 8 mahākiriya y los 12 cittas de los primeros 4 jhānas rūpāvacara (ausentes en el 5º jhāna y en los cittas lokuttara)"
            },
            "philosophy": {
                "pt": "Explicação magistral de Bhikkhu Bodhi (CMA II, §7 & §15, pp. 89–90, 99): por que karuṇā e muditā estão presentes em 28 cittas (8 mahākusala, 8 mahākiriya e 12 rūpāvacara dos 4 primeiros jhānas), mas ausentes nos 15 mahāvipāka, no 5º jhāna e nos 8/40 lokuttara? (1) Nos mahāvipāka da esfera sensual, a consciência toma apenas objetos dhammas últimos (paramattha), ao passo que os appamaññās tomam o conceito de seres sencientes (satta-paññatti). (2) No 5º jhāna rūpāvacara, o incomensurável desenvolvido é upekkhā (que é o cetasika tatramajjhattatā). (3) Nos cittas lokuttara, o objeto é exclusivamente Nibbāna (paramattha incondicionado).",
                "en": "Masterful explanation by Bhikkhu Bodhi (CMA II, §7 & §15, pp. 89–90, 99): why do karuṇā and muditā occur in 28 cittas (8 mahākusala, 8 mahākiriya, and 12 rūpāvacara of the first 4 jhānas), but never in the 15 mahāvipāka, the 5th jhāna, or the 8/40 lokuttara cittas? (1) Sense-sphere mahāvipāka cittas take only ultimate realities (paramattha) as objects, whereas the appamaññās take the concept of living beings (satta-paññatti). (2) In the 5th rūpāvacara jhāna, the illimitable developed is equanimity (tatramajjhattatā). (3) Supramundane cittas take Nibbāna as their sole object.",
                "es": "Explicación magistral de Bhikkhu Bodhi (CMA II, §7 y §15, pp. 89–90, 99): karuṇā y muditā surgen en 28 cittas (8 mahākusala, 8 mahākiriya y 12 rūpāvacara de los primeros 4 jhānas), pero nunca en mahāvipāka ni en lokuttara porque su objeto es el concepto de seres vivos (satta-paññatti)."
            },
            "bodhiRef": "CMA II, §7 & §15 (Guide, pp. 89–90, 99); IX, §9 & §19 (pp. 335, 341)"
        },
        "seeAlso": ["karuṇā", "muditā", "mettā", "adosa", "tatramajjhattatā"]
    },

    "karuṇā": {
        "meaning": {
            "pt": "Compaixão; o 1º dos 2 incomensuráveis listados como cetasikas distintos (Cetasika #50 de 52) e 2º brahmavihāra: a nobre qualidade que estremece diante do sofrimento alheio e aspira removê-lo (distinta da tristeza, domanassa, que é seu 'inimigo próximo').",
            "en": "Compassion; the 1st of the 2 illimitables listed as distinct cetasikas (Cetasika #50 of 52) and 2nd brahmavihāra: the noble quality that trembles at the suffering of others and seeks to remove it (distinct from sorrow/grief, domanassa, its 'near enemy').",
            "es": "Compasión; el 1º de los 2 inconmensurables listados como cetasikas distintos (Cetasika #50 de 52) y 2º brahmavihāra: la noble cualidad que se conmueve ante el sufrimiento ajeno y busca aliviarlo (distinta de la tristeza, domanassa, su 'enemigo cercano')."
        },
        "grammar": "fem. (de √kar + uṇā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (da raiz √kar 'fazer estremecer o coração dos bons diante da dor alheia' ou √kir 'dissipar o sofrimento')",
            "en": "Feminine noun (from root √kar 'making the hearts of the good quiver at others' pain' or √kir 'scattering others' suffering')",
            "es": "Sustantivo femenino (de la raíz √kar 'hacer estremecer el corazón de los buenos ante el dolor ajeno' o √kir 'disipar el sufrimiento')"
        },
        "root": "√kar / √kir + uṇā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Belo Variável / Incomensurável (Cetasika #50 de 52)",
                "en": "Ultimate Reality — Variable Beautiful Mental Factor / Illimitable (Cetasika #50 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Variable / Inconmensurable (Cetasika #50 de 52)"
            },
            "category": {
                "pt": "Incomensurável (Appamaññā — surge ocasionalmente, kadāci, e separadamente de muditā em 28 cittas: 8 mahākusala, 8 mahākiriya e 12 rūpāvacara dos 4 primeiros jhānas)",
                "en": "Illimitable (Appamaññā — arises occasionally, kadāci, and separately from muditā in 28 cittas: 8 mahākusala, 8 mahākiriya, and 12 rūpāvacara of the first 4 jhānas)",
                "es": "Inconmensurable (Appamaññā — surge ocasionalmente, kadāci, y separadamente de muditā en 28 cittas: 8 mahākusala, 8 mahākiriya y 12 rūpāvacara de los primeros 4 jhānas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Promover a remoção do sofrimento nos outros (paradukkhāpanayanākārappavatti-lakkhaṇa).",
                    "en": "Promoting the removal of suffering in others (paradukkhāpanayanākārappavatti-lakkhaṇa).",
                    "es": "Promover la eliminación del sufrimiento en los demás (paradukkhāpanayanākārappavatti-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Não suportar ver o sofrimento alheio (paradukkhāsahana-rasa).",
                    "en": "Not being able to bear others' suffering (paradukkhāsahana-rasa).",
                    "es": "No poder soportar el sufrimiento de los demás (paradukkhāsahana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Não-crueldade (avihiṃsā-paccupaṭṭhāna).",
                    "en": "Non-cruelty (avihiṃsā-paccupaṭṭhāna).",
                    "es": "No crueldad (avihiṃsā-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Ver o desamparo daqueles que estão oprimidos pelo sofrimento (dukkhābhibhūtānaṃ anāthabhāvadassana-padaṭṭhāna). Triunfa quando faz cessar a crueldade (vihiṃsā) e fracassa quando produz tristeza (domanassa).",
                    "en": "Seeing helplessness in those overwhelmed by suffering (dukkhābhibhūtānaṃ anāthabhāvadassana-padaṭṭhāna). It succeeds when it causes cruelty to subside, and fails when it produces sorrow (domanassa).",
                    "es": "Ver el desamparo de los abrumados por el sufrimiento (dukkhābhibhūtānaṃ anāthabhāvadassana-padaṭṭhāna). Triunfa cuando apacigua la crueldad y fracasa cuando produce tristeza (domanassa)."
                }
            },
            "philosophy": {
                "pt": "Ponto psicológico sutil do Abhidhamma (CMA II, §7, p. 90): embora karuṇā tome como objeto seres em sofrimento (dukkhita-satta), o próprio estado mental de compaixão nunca é acompanhado por sensação dolorosa (domanassa, que é exclusiva dos 2 cittas enraizados no ódio!). Ao contrário, karuṇā surge em cittas belos acompanhados por sensação neutra (upekkhā) ou, quando desenvolvido em jhāna (1º ao 3º jhāna), acompanhado por alegria espiritual serena (somanassa)! A tristeza depressiva (gehasita-domanassa) é o 'inimigo próximo' da compaixão, não a compaixão genuína.",
                "en": "Subtle psychological point of the Abhidhamma (CMA II, §7, p. 90): although karuṇā takes suffering beings (dukkhita-satta) as its object, the mental state of compassion itself is never accompanied by painful mental feeling (domanassa, which occurs exclusively in the 2 hate-rooted cittas!). Rather, karuṇā arises in beautiful cittas accompanied either by neutral feeling (upekkhā) or, when developed in the first three jhānas, by serene spiritual joy (somanassa)! Worldly grief (domanassa) is compassion's 'near enemy,' not genuine karuṇā.",
                "es": "Punto psicológico sutil del Abhidhamma (CMA II, §7, p. 90): aunque karuṇā toma como objeto a seres que sufren, nunca va acompañada de sensación mental dolorosa (domanassa, exclusiva de los 2 cittas con odio), sino de upekkhā o somanassa en cittas hermosos."
            },
            "bodhiRef": "CMA II, §7 & §15 (Guide, pp. 89–90, 99); IX, §9 & §19 (pp. 335, 341)"
        },
        "seeAlso": ["muditā", "mettā", "appamaññā", "domanassasahagata", "adosa"]
    },

    "muditā": {
        "meaning": {
            "pt": "Alegria apreciativa (ou altruísta); regozijo empático; o 2º dos 2 incomensuráveis listados como cetasikas distintos (Cetasika #51 de 52) e 3º brahmavihāra: a qualidade bela que se alegra genuinamente com o sucesso, a felicidade e as virtudes dos outros, opondo-se diretamente à inveja (issā) e ao descontentamento (arati).",
            "en": "Appreciative joy; sympathetic gladness; the 2nd of the 2 illimitables listed as distinct cetasikas (Cetasika #51 of 52) and 3rd brahmavihāra: the beautiful quality that rejoices in the success and happiness of others, directly opposed to envy (issā) and discontent (arati).",
            "es": "Alegría apreciativa (o altruista); regocijo empático; el 2º de los 2 inconmensurables listados como cetasikas distintos (Cetasika #51 de 52) y 3º brahmavihāra: la cualidad hermosa que se regocija en el éxito y felicidad ajenos, oponiéndose a la envidia (issā) y al descontento (arati)."
        },
        "grammar": "fem. (de √mud + ita + ā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (derivado da raiz √mud 'alegrar-se, regozijar-se')",
            "en": "Feminine noun (derived from root √mud 'to be glad, rejoice')",
            "es": "Sustantivo femenino (derivado de la raíz √mud 'alegrarse, regocijarse')"
        },
        "root": "√mud (regozijar-se / alegrar-se) + ita + ā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Belo Variável / Incomensurável (Cetasika #51 de 52)",
                "en": "Ultimate Reality — Variable Beautiful Mental Factor / Illimitable (Cetasika #51 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso Variable / Inconmensurable (Cetasika #51 de 52)"
            },
            "category": {
                "pt": "Incomensurável (Appamaññā — surge ocasionalmente, kadāci, e separadamente de karuṇā em 28 cittas: 8 mahākusala, 8 mahākiriya e 12 rūpāvacara dos 4 primeiros jhānas)",
                "en": "Illimitable (Appamaññā — arises occasionally, kadāci, and separately from karuṇā in 28 cittas: 8 mahākusala, 8 mahākiriya, and 12 rūpāvacara of the first 4 jhānas)",
                "es": "Inconmensurable (Appamaññā — surge ocasionalmente, kadāci, y separadamente de karuṇā en 28 cittas: 8 mahākusala, 8 mahākiriya y 12 rūpāvacara de los primeros 4 jhānas)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Alegria jubilosa perante o êxito e a felicidade alheia (pamodana-lakkhaṇa).",
                    "en": "Gladness at the success and happiness of others (pamodana-lakkhaṇa).",
                    "es": "Alegría ante el éxito y la felicidad de los demás (pamodana-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Ausência de inveja pelo sucesso dos outros (anissāyana-rasa).",
                    "en": "Being unenvious at others' success (anissāyana-rasa).",
                    "es": "No tener envidia ante el éxito ajeno (anissāyana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Eliminação do tédio, aversão ou descontentamento (arativighāta-paccupaṭṭhāna).",
                    "en": "The elimination of aversion or discontent (arativighāta-paccupaṭṭhāna).",
                    "es": "La eliminación de la aversión o el descontento (arativighāta-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Ver o sucesso e a prosperidade dos seres (sattānaṃ sampattidassana-padaṭṭhāna). Triunfa quando faz cessar o descontentamento (arati) e fracassa quando produz euforia mundana frívola (pahāsa).",
                    "en": "Seeing the success of beings (sattānaṃ sampattidassana-padaṭṭhāna). It succeeds when it causes aversion/discontent (arati) to subside, and fails when it produces frivolous merriment (pahāsa).",
                    "es": "Ver el éxito de los seres (sattānaṃ sampattidassana-padaṭṭhāna). Triunfa cuando disipa el descontento (arati) y fracasa cuando produce euforia mundana frívola (pahāsa)."
                }
            },
            "philosophy": {
                "pt": "Karuṇā e muditā nunca podem surgir juntos no mesmo momento de consciência (paccekam eva), pois tomam objetos opostos: karuṇā dirige-se aos seres aflitos pelo sofrimento (dukkhita-satta), enquanto muditā dirige-se aos seres prósperos e felizes (sukhita-satta).",
                "en": "Karuṇā and muditā can never arise together in the same moment of consciousness (paccekam eva), since they take opposite objects: karuṇā is directed toward suffering beings (dukkhita-satta), whereas muditā is directed toward prosperous, happy beings (sukhita-satta).",
                "es": "Karuṇā y muditā nunca pueden surgir juntas en el mismo momento de conciencia (paccekam eva), pues toman objetos opuestos: karuṇā se dirige a los seres que sufren y muditā a los seres felices y prósperos."
            },
            "bodhiRef": "CMA II, §7 & §15 (Guide, pp. 89–90, 99); IX, §9 & §19 (pp. 335, 341)"
        },
        "seeAlso": ["karuṇā", "mettā", "appamaññā", "issā", "pīti"]
    },

    "paññā": {
        "meaning": {
            "pt": "Sabedoria; discernimento; conhecimento penetrante (ñāṇa); não-delusão (amoha); a faculdade da sabedoria (paññindriya, 52º e último cetasika) e a 3ª raiz bela (sobhanahetu), que compreende os fenômenos exatamente de acordo com sua natureza intrínseca real (yathāsabhāva).",
            "en": "Wisdom; discernment; penetrative knowledge (ñāṇa); non-delusion (amoha); the faculty of wisdom (paññindriya, 52nd and final cetasika) and the 3rd beautiful root (sobhanahetu), which comprehends phenomena according to their real intrinsic nature (yathāsabhāva).",
            "es": "Sabiduría; discernimiento; conocimiento penetrante (ñāṇa); no-ilusión (amoha); la facultad de la sabiduría (paññindriya, 52º y último cetasika) y la 3ª raíz hermosa (sobhanahetu), que comprende los fenómenos según su naturaleza intrínseca real (yathāsabhāva)."
        },
        "grammar": "fem. (pa + √ñā + ā)",
        "grammarLocalized": {
            "pt": "Substantivo feminino (pa 'completamente, distintamente' + raiz √ñā 'conhecer, discernir' + -ā)",
            "en": "Feminine noun (pa 'thoroughly, distinctly' + root √ñā 'to know, discern' + -ā)",
            "es": "Sustantivo femenino (pa 'completamente, distintamente' + raíz √ñā 'conocer, discernir' + -ā)"
        },
        "root": "pa + √ñā (conhecer / discernir profundamente) + ā",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Belo / Faculdade da Sabedoria (Cetasika #52 de 52)",
                "en": "Ultimate Reality — Beautiful Mental Factor / Faculty of Wisdom (Cetasika #52 of 52)",
                "es": "Realidad Última — Factor Mental Hermoso / Facultad de la Sabiduría (Cetasika #52 de 52)"
            },
            "category": {
                "pt": "Faculdade da Sabedoria (Paññindriya / Amoha / Ñāṇa — presente em 47 de 89 cittas ou 79 de 121 cittas: 12 kāmāvacara ñāṇasampayutta, 27 mahaggata e 8/40 lokuttara); aparece 5 vezes nas 37 Bodhipakkhiyā Dhammā (Vīmaṃsiddhipāda, Paññindriya, Paññābala, Dhammavicayasambojjhaṅga, Sammādiṭṭhi)",
                "en": "Wisdom Faculty (Paññindriya / Amoha / Ñāṇa — present in 47 of 89 cittas or 79 of 121 cittas: 12 ñāṇasampayutta kāmāvacara, 27 mahaggata, and 8/40 lokuttara); appears 5 times in the 37 Requisites of Enlightenment (Vīmaṃsiddhipāda, Paññindriya, Paññābala, Dhammavicayasambojjhaṅga, Sammādiṭṭhi)",
                "es": "Facultad de la Sabiduría (Paññindriya / Amoha / Ñāṇa — presente en 47 de 89 cittas o 79 de 121 cittas: 12 kāmāvacara ñāṇasampayutta, 27 mahaggata y 8/40 lokuttara); aparece 5 veces en los 37 Requisitos de la Iluminación"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Penetrar as coisas de acordo com sua verdadeira natureza intrínseca (yathāsabhāvapaṭivedha-lakkhaṇa), ou penetração infalível como a flecha disparada por um arqueiro habilidoso (akkhalitappaṭivedha-lakkhaṇa).",
                    "en": "Penetrating things according to their intrinsic nature (yathāsabhāvapaṭivedha-lakkhaṇa), or unerring penetration like the penetration of an arrow shot by a skilled archer (akkhalitappaṭivedha-lakkhaṇa).",
                    "es": "Penetrar las cosas según su verdadera naturaleza intrínseca (yathāsabhāvapaṭivedha-lakkhaṇa), como la flecha disparada por un arquero hábil."
                },
                "rasa": {
                    "pt": "Iluminar o campo objetivo como uma lâmpada que dissipa a escuridão (visayobhāsana-rasa).",
                    "en": "To illuminate the objective field like a lamp that dispels darkness (visayobhāsana-rasa).",
                    "es": "Iluminar el campo objetivo como una lámpara que disipa la oscuridad (visayobhāsana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Ausência de confusão ou não-perplexidade (asammoha-paccupaṭṭhāna), como um guia experiente numa floresta.",
                    "en": "Non-bewilderment (asammoha-paccupaṭṭhāna), like a skilled guide in a forest.",
                    "es": "Ausencia de confusión o no perplejidad (asammoha-paccupaṭṭhāna), como un guía experto en un bosque."
                },
                "padatthana": {
                    "pt": "Atenção sábia / criteriosa (yoniso manasikāra-padaṭṭhāna) ou concentração (samādhi-padaṭṭhāna, conforme a máxima canônica: 'quem está concentrado compreende as coisas como realmente são', samāhito yathābhūtaṃ pajānāti).",
                    "en": "Wise attention (yoniso manasikāra-padaṭṭhāna) or concentration (samādhi-padaṭṭhāna, per the canonical dictum: 'one who is concentrated knows and sees things as they really are,' samāhito yathābhūtaṃ pajānāti).",
                    "es": "Atención sabia (yoniso manasikāra-padaṭṭhāna) o concentración (samādhi-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "No Abhidhamma (CMA II, §8, p. 90; I, §18, pp. 55–56), paññā, ñāṇa e amoha são estritamente sinônimos e designam o 52º cetasika (paññindriya). Na famosa símile de Ācariya Buddhaghosa (Visuddhimagga XIV, 7) sobre os três modos de conhecer uma moeda: saññā (percepção) é como uma criança pequena que vê apenas a cor e o formato da moeda; viññāṇa (consciência, citta) é como um aldeão adulto que sabe que a moeda serve como meio de troca; paññā (sabedoria) é como um mestre ourives que examina a moeda e sabe exatamente sua composição metálica, se é verdadeira ou falsa, e onde e por quem foi cunhada.",
                "en": "In the Abhidhamma (CMA II, §8, p. 90; I, §18, pp. 55–56), paññā, ñāṇa, and amoha are strictly synonymous, denoting the 52nd cetasika (paññindriya). In Ācariya Buddhaghosa's famous simile (Visuddhimagga XIV, 7) of knowing a coin: saññā (perception) is like a young child who sees only the coin's color and shape; viññāṇa (consciousness, citta) is like an adult villager who knows its value as currency; paññā (wisdom) is like a master money-changer who examines the coin and knows its exact metallic composition, whether it is genuine or counterfeit, and where and by whom it was minted.",
                "es": "En el Abhidhamma (CMA II, §8, p. 90; I, §18, pp. 55–56), paññā, ñāṇa y amoha son estrictamente sinónimos y designan el 52º cetasika (paññindriya). En el célebre símil de la moneda (Visuddhimagga XIV, 7), saññā es como un niño que solo ve el color y la forma; viññāṇa es como un aldeano que conoce su valor comercial; paññā es como un maestro orfebre que discierne su composición exacta, autenticidad y origen."
            },
            "bodhiRef": "CMA I, §18 (p. 55); II, §8 & §16 (Guide, pp. 90, 99); VII, §32 (p. 283)"
        },
        "seeAlso": ["paññindriya", "amoha", "ñāṇa", "ñāṇasampayutta", "moha", "diṭṭhi", "saññā", "citta"]
    },

    "paññindriya": {
        "meaning": {
            "pt": "A faculdade da sabedoria; o nome técnico pelo qual o 52º cetasika (paññā / amoha / ñāṇa) é enumerado no Abhidhammattha Saṅgaha (Cap. II, §8), por exercer soberania e predominância (indriyasaṅkhāta) em compreender as coisas como elas realmente são.",
            "en": "The faculty of wisdom; the technical name under which the 52nd cetasika (paññā / amoha / ñāṇa) is enumerated in the Abhidhammattha Saṅgaha (Ch. II, §8), because it exercises predominance (indriyasaṅkhāta) in comprehending things as they really are.",
            "es": "La facultad de la sabiduría; el nombre técnico bajo el cual se enumera el 52º cetasika (paññā / amoha / ñāṇa) en el Abhidhammattha Saṅgaha (Cap. II, §8), por ejercer predominio en comprender las cosas como realmente son."
        },
        "grammar": "nt. (Kammadhāraya: paññā + indriya)",
        "grammarLocalized": {
            "pt": "Substantivo neutro (Kammadhāraya com sandhi: paññā + indriya)",
            "en": "Neuter noun (Kammadhāraya with sandhi: paññā + indriya)",
            "es": "Sustantivo neutro (Kammadhāraya con sandhi: paññā + indriya)"
        },
        "root": "pa + √ñā + ā + √ind + riya",
        "samasa": {
            "breakdown": "paññā + indriya",
            "type": {
                "pt": "Avadhāraṇa-Kammadhāraya Samāsa (Composto Descritivo de Identificação)",
                "en": "Avadhāraṇa-Kammadhāraya Samāsa (Descriptive Compound of Identification)",
                "es": "Avadhāraṇa-Kammadhāraya Samāsa (Compuesto Descriptivo de Identificación)"
            },
            "viggaha": "paññā eva indriyaṃ paññindriyaṃ",
            "literal": {
                "pt": "A faculdade soberana que consiste na sabedoria",
                "en": "The governing faculty that is wisdom",
                "es": "La facultad soberana que es la sabiduría"
            },
            "parts": [
                {"pali": "paññā", "gloss": {"pt": "sabedoria", "en": "wisdom", "es": "sabiduría"}},
                {"pali": "indriya", "gloss": {"pt": "faculdade soberana", "en": "governing faculty", "es": "facultad soberana"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Belo (Cetasika #52 de 52, idêntico a Paññā / Amoha / Ñāṇa)",
                "en": "Ultimate Reality — Beautiful Mental Factor (Cetasika #52 of 52, identical with Paññā / Amoha / Ñāṇa)",
                "es": "Realidad Última — Factor Mental Hermoso (Cetasika #52 de 52, idéntico a Paññā / Amoha / Ñāṇa)"
            },
            "category": {
                "pt": "Presente em 47 de 89 cittas (ou 79 de 121 cittas); 16ª das 22 Faculdades (Indriya, Cap. VII, §18)",
                "en": "Present in 47 of 89 cittas (or 79 of 121 cittas); 16th of the 22 Faculties (Indriya, Ch. VII, §18)",
                "es": "Presente en 47 de 89 cittas (o 79 de 121 cittas); 16ª de las 22 Facultades (Indriya, Cap. VII, §18)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Penetrar as coisas segundo sua natureza intrínseca (yathāsabhāvapaṭivedha-lakkhaṇa).",
                    "en": "Penetrating things according to their intrinsic nature (yathāsabhāvapaṭivedha-lakkhaṇa).",
                    "es": "Penetrar las cosas según su naturaleza intrínseca (yathāsabhāvapaṭivedha-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Iluminar o campo objetivo como uma lâmpada (visayobhāsana-rasa).",
                    "en": "To illuminate the objective field like a lamp (visayobhāsana-rasa).",
                    "es": "Iluminar el campo objetivo como una lámpara (visayobhāsana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Não-confusão ou lucidez (asammoha-paccupaṭṭhāna).",
                    "en": "Non-bewilderment (asammoha-paccupaṭṭhāna).",
                    "es": "Ausencia de confusión (asammoha-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Atenção sábia (yoniso manasikāra-padaṭṭhāna).",
                    "en": "Wise attention (yoniso manasikāra-padaṭṭhāna).",
                    "es": "Atención sabia (yoniso manasikāra-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "No Cap. VII (§18), das 22 faculdades (indriya), três são faculdades supramundanas de sabedoria (aññātaññassāmītindriya no Sotāpatti-magga, aññindriya dos 6 estágios intermediários e aññātāvindriya no Arahattaphala), todas tendo este mesmo cetasika paññindriya como realidade última subjacente.",
                "en": "In Ch. VII (§18), besides the general paññindriya, the three supramundane faculties (aññātaññassāmītindriya at Sotāpatti-magga, aññindriya in the 6 intermediate stages, and aññātāvindriya at Arahattaphala) all have this single cetasika paññā as their underlying ultimate reality.",
                "es": "En el Cap. VII (§18), tanto paññindriya como las tres facultades supramundanas tienen este mismo cetasika paññā como realidad última subyacente."
            },
            "bodhiRef": "CMA II, §8 & §16 (Guide, pp. 90, 99); VII, §18 (p. 275)"
        },
        "seeAlso": ["paññā", "amoha", "ñāṇa", "ñāṇasampayutta"]
    },

    "amoha": {
        "meaning": {
            "pt": "Não-delusão; sabedoria (paññā); conhecimento (ñāṇa); a 3ª das três raízes belas (sobhanahetu, ao lado de alobha e adosa), presente em todos os 47/79 cittas triplamente enraizados (tihetuka).",
            "en": "Non-delusion; wisdom (paññā); knowledge (ñāṇa); the 3rd of the three beautiful roots (sobhanahetu, alongside alobha and adosa), present in all 47/79 triple-rooted (tihetuka) cittas.",
            "es": "No-ilusión; sabiduría (paññā); conocimiento (ñāṇa); la 3ª de las tres raíces hermosas (sobhanahetu, junto a alobha y adosa), presente en todos los 47/79 cittas con tres raíces (tihetuka)."
        },
        "grammar": "masc. (na > a + moha)",
        "grammarLocalized": {
            "pt": "Substantivo masculino (Nañ-Tappurisa: a + moha)",
            "en": "Masculine noun (Nañ-Tappurisa: a + moha)",
            "es": "Sustantivo masculino (Nañ-Tappurisa: a + moha)"
        },
        "root": "na > a (oposto de) + √muh (estar iludido) + *a",
        "samasa": {
            "breakdown": "a (na) + moha",
            "type": {
                "pt": "Nañ-Tappurisa Samāsa (Composto Determinativo de Oposição Positiva)",
                "en": "Nañ-Tappurisa Samāsa (Negative Determinative Compound of Positive Opposition)",
                "es": "Nañ-Tappurisa Samāsa (Compuesto Determinativo de Oposición Positiva)"
            },
            "viggaha": "mohassa paṭipakkho ti amoho",
            "literal": {
                "pt": "O oposto positivo da delusão (sabedoria / paññā)",
                "en": "The positive opposite of delusion (wisdom / paññā)",
                "es": "El opuesto positivo de la ilusión (sabiduría / paññā)"
            },
            "parts": [
                {"pali": "a-", "gloss": {"pt": "oposto de", "en": "opposite of", "es": "opuesto de"}},
                {"pali": "moha", "gloss": {"pt": "delusão / ignorância", "en": "delusion / ignorance", "es": "ilusión / ignorancia"}}
            ]
        },
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — 3ª Raiz Bela (idêntico ao Cetasika #52 Paññindriya)",
                "en": "Ultimate Reality — 3rd Beautiful Root (identical with Cetasika #52 Paññindriya)",
                "es": "Realidad Última — 3ª Raíz Hermosa (idéntico al Cetasika #52 Paññindriya)"
            },
            "category": {
                "pt": "Raiz Salutar e Indeterminada (Kusala/Abyākata Hetu, Cap. III, §5); distingue os cittas tihetuka (3 raízes) dos cittas duhetuka (2 raízes: apenas alobha e adosa)",
                "en": "Wholesome and Indeterminate Root (Kusala/Abyākata Hetu, Ch. III, §5); distinguishes tihetuka (3-rooted) cittas from duhetuka (2-rooted: alobha and adosa only) cittas",
                "es": "Raíz Saludable e Indeterminada (Kusala/Abyākata Hetu, Cap. III, §5); distingue los cittas tihetuka (3 raíces) de los cittas duhetuka (2 raíces)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Penetrar a natureza intrínseca real dos fenômenos (yathāsabhāvapaṭivedha-lakkhaṇa).",
                    "en": "Penetrating the real intrinsic nature of phenomena (yathāsabhāvapaṭivedha-lakkhaṇa).",
                    "es": "Penetrar la naturaleza intrínseca real de los fenómenos (yathāsabhāvapaṭivedha-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Iluminar o campo objetivo como uma lâmpada (visayobhāsana-rasa).",
                    "en": "To illuminate the objective field like a lamp (visayobhāsana-rasa).",
                    "es": "Iluminar el campo objetivo como una lámpara (visayobhāsana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Não-perplexidade (asammoha-paccupaṭṭhāna).",
                    "en": "Non-bewilderment (asammoha-paccupaṭṭhāna).",
                    "es": "No perplejidad (asammoha-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Atenção sábia (yoniso manasikāra-padaṭṭhāna).",
                    "en": "Wise attention (yoniso manasikāra-padaṭṭhāna).",
                    "es": "Atención sabia (yoniso manasikāra-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "Enquanto alobha e adosa estão presentes em todos os 59/91 cittas belos, amoha (paññā) está ausente nos 12 cittas belos dissociados de conhecimento (ñāṇavippayutta) e presente nos 47/79 cittas associados a conhecimento (ñāṇasampayutta / tihetuka). Apenas um renascimento tihetuka (com amoha presente na consciência de reconexão, paṭisandhi) permite alcançar jhāna e os caminhos supramundanos naquela mesma vida (CMA IV, §16, p. 171).",
                "en": "Whereas alobha and adosa are present in all 59/91 beautiful cittas, amoha (paññā) is absent in the 12 beautiful cittas dissociated from knowledge (ñāṇavippayutta) and present in the 47/79 cittas associated with knowledge (ñāṇasampayutta / tihetuka). Only a tihetuka rebirth (with amoha present in the paṭisandhi-citta) enables the attainment of jhāna and the supramundane paths in that very life (CMA IV, §16, p. 171).",
                "es": "Mientras alobha y adosa están presentes en todos los 59/91 cittas hermosos, amoha (paññā) está presente en los 47/79 cittas ñāṇasampayutta (tihetuka). Solo un renacimiento tihetuka permite alcanzar jhāna y los caminos supramundanos en esa misma vida."
            },
            "bodhiRef": "CMA II, §8 (Guide, p. 90); III, §§5–7 (pp. 117–119); IV, §16 (p. 171)"
        },
        "seeAlso": ["paññā", "paññindriya", "ñāṇa", "moha", "alobha", "adosa", "hetu"]
    },

    "ñāṇa": {
        "meaning": {
            "pt": "Conhecimento; compreensão lúcida; sabedoria (sinônimo ontológico de paññā e amoha no Abhidhamma, Cetasika #52 de 52). Especialmente usado para os conhecimentos de insight (vipassanāñāṇa) e dos caminhos supramundanos (maggañāṇa).",
            "en": "Knowledge; lucid comprehension; wisdom (ontological synonym of paññā and amoha in the Abhidhamma, Cetasika #52 of 52). Especially used for the insight knowledges (vipassanāñāṇa) and supramundane path knowledges (maggañāṇa).",
            "es": "Conocimiento; comprensión lúcida; sabiduría (sinónimo ontológico de paññā y amoha en el Abhidhamma, Cetasika #52 de 52). Especialmente usado para los conocimientos de insight (vipassanāñāṇa) y de los caminos supramundanos (maggañāṇa)."
        },
        "grammar": "nt. (de √ñā + yu / ana)",
        "grammarLocalized": {
            "pt": "Substantivo neutro (derivado da raiz √ñā 'conhecer, saber' + -ana)",
            "en": "Neuter noun (derived from root √ñā 'to know' + -ana)",
            "es": "Sustantivo neutro (derivado de la raíz √ñā 'conocer, saber' + -ana)"
        },
        "root": "√ñā (conhecer / compreender) + ana",
        "abhidhamma": {
            "ontology": {
                "pt": "Realidade Última — Fator Mental Belo (Cetasika #52 de 52, idêntico a Paññā / Amoha)",
                "en": "Ultimate Reality — Beautiful Mental Factor (Cetasika #52 of 52, identical with Paññā / Amoha)",
                "es": "Realidad Última — Factor Mental Hermoso (Cetasika #52 de 52, idéntico a Paññā / Amoha)"
            },
            "category": {
                "pt": "Faculdade da Sabedoria (Paññindriya); qualifica os cittas Ñāṇasampayutta (associados a conhecimento)",
                "en": "Wisdom Faculty (Paññindriya); qualifies the Ñāṇasampayutta (knowledge-associated) cittas",
                "es": "Facultad de la Sabiduría (Paññindriya); califica los cittas Ñāṇasampayutta (asociados al conocimiento)"
            },
            "lakkhanaCatukka": {
                "lakkhana": {
                    "pt": "Penetrar a natureza intrínseca real dos fenômenos (yathāsabhāvapaṭivedha-lakkhaṇa).",
                    "en": "Penetrating the real intrinsic nature of phenomena (yathāsabhāvapaṭivedha-lakkhaṇa).",
                    "es": "Penetrar la naturaleza intrínseca real de los fenómenos (yathāsabhāvapaṭivedha-lakkhaṇa)."
                },
                "rasa": {
                    "pt": "Iluminar o objeto (visayobhāsana-rasa).",
                    "en": "To illuminate the object (visayobhāsana-rasa).",
                    "es": "Iluminar el objeto (visayobhāsana-rasa)."
                },
                "paccupatthana": {
                    "pt": "Não-delusão (asammoha-paccupaṭṭhāna).",
                    "en": "Non-bewilderment (asammoha-paccupaṭṭhāna).",
                    "es": "No perplejidad (asammoha-paccupaṭṭhāna)."
                },
                "padatthana": {
                    "pt": "Atenção sábia (yoniso manasikāra-padaṭṭhāna).",
                    "en": "Wise attention (yoniso manasikāra-padaṭṭhāna).",
                    "es": "Atención sabia (yoniso manasikāra-padaṭṭhāna)."
                }
            },
            "philosophy": {
                "pt": "No Cap. IX (§§22–37), o progresso do insight meditativo é estruturado nos dez conhecimentos de insight (dasa vipassanāñāṇāni), todos manifestações progressivamente mais penetrantes deste cetasika ñāṇa contemplando a impermanência (anicca), o sofrimento (dukkha) e o não-eu (anattā) de nāmarūpa.",
                "en": "In Ch. IX (§§22–37), the progress of insight is structured around the ten insight knowledges (dasa vipassanāñāṇāni), all progressively deeper manifestations of this cetasika ñāṇa contemplating the impermanence (anicca), suffering (dukkha), and non-self (anattā) of nāmarūpa.",
                "es": "En el Cap. IX (§§22–37), el progreso del insight se estructura en los diez conocimientos de insight (dasa vipassanāñāṇāni), manifestaciones de este cetasika ñāṇa."
            },
            "bodhiRef": "CMA I, §18 (p. 55); II, §8 (p. 90); IX, §§22–37 (Guide, pp. 344–360)"
        },
        "seeAlso": ["paññā", "amoha", "paññindriya", "ñāṇasampayutta", "ñāṇavippayutta", "vipassanā"]
    }
}


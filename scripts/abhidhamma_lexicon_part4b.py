# -*- coding: utf-8 -*-
"""
Canonical Abhidhamma Lexicon — Part 4B:
Chapters V (Planes/Kamma), VII (Samuccaya), VIII (Paccaya), IX (Kammaṭṭhāna),
and Core Classification Formulas (Vedanā, Saṅkhāra, Sampayoga).
Grounded in Bhikkhu Bodhi's A Comprehensive Manual of Abhidhamma (CMA).
"""

PART4B_ENTRIES = {
    "bhūmi": {
        "meaning": {
            "pt": "Plano de existência; reino cosmológico ou nível de consciência (4 planos: kāmabhūmi, rūpabhūmi, arūpabhūmi e lokuttarabhūmi; 31 reinos de existência)",
            "en": "Plane of existence; cosmological realm or level of consciousness (4 planes: kāmabhūmi, rūpabhūmi, arūpabhūmi, and lokuttarabhūmi; 31 realms of existence)",
            "es": "Plano de existencia; reino cosmológico o nivel de conciencia (4 planos: kāmabhūmi, rūpabhūmi, arūpabhūmi y lokuttarabhūmi; 31 reinos de existencia)"
        },
        "grammar": "Feminino (bhūmi) · derivado de √bhū",
        "grammarLocalized": {
            "pt": "Substantivo Feminino (bhūmi) · derivado de √bhū",
            "en": "Feminine Noun (bhūmi) · derived from √bhū",
            "es": "Sustantivo Femenino (bhūmi) · derivado de √bhū"
        },
        "root": "√bhū (ser, tornar-se, existir) + -mi",
        "abhidhamma": {
            "ontology": {"pt": "Princípio Cosmológico e Psicológico (Catubhūmi)", "en": "Cosmological & Psychological Principle (Catubhūmi)", "es": "Principio Cosmológico y Psicológico (Catubhūmi)"},
            "category": {"pt": "Quatro Planos e Trinta e Um Reinos (Cap. I & Cap. V)", "en": "Four Planes & Thirty-One Realms (Ch. I & Ch. V)", "es": "Cuatro Planos y Treinta y Un Reinos (Cap. I y Cap. V)"},
            "philosophy": {
                "pt": "No Abhidhamma, bhūmi designa tanto os níveis psicológicos de consciência (4 planos de citta) quanto os 31 reinos cosmológicos onde os seres renascem conforme seu kamma: 4 estados de privação (apāyabhūmi), 7 reinos felizes sensuais (kāmasugatibhūmi), 16 reinos de matéria sutil (rūpāvacarabhūmi) e 4 reinos imateriais (arūpāvacarabhūmi).",
                "en": "In Abhidhamma, bhūmi designates both psychological levels of consciousness (4 planes of citta) and the 31 cosmological realms where beings are reborn according to their kamma: 4 woeful states (apāyabhūmi), 7 sensual blissful realms (kāmasugatibhūmi), 16 fine-material realms (rūpāvacarabhūmi), and 4 immaterial realms (arūpāvacarabhūmi).",
                "es": "En el Abhidhamma, bhūmi designa tanto los niveles psicológicos de conciencia (4 planos de citta) como los 31 reinos cosmológicos donde los seres renacen según su kamma: 4 estados de privación (apāyabhūmi), 7 reinos felices sensuales (kāmasugatibhūmi), 16 reinos de materia sutil (rūpāvacarabhūmi) y 4 reinos inmateriales (arūpāvacarabhūmi)."
            },
            "bodhiRef": "CMA I §3 (p. 28); V §§2–8 (pp. 187–196)"
        },
        "seeAlso": ["kāmāvacara", "rūpāvacara", "arūpāvacara", "lokuttara", "apāya"]
    },
    "apāya": {
        "meaning": {
            "pt": "Estado de privação, plano de miséria ou mundo inferior; os 4 reinos infelizes (inferno/niraya, reino animal/tiracchāna, espíritos famintos/peta e titãs/asura)",
            "en": "State of deprivation, plane of misery, or woeful realm; the 4 unhappy realms (hell/niraya, animal realm/tiracchāna, ghosts/peta, and titans/asura)",
            "es": "Estado de privación, plano de miseria o mundo inferior; los 4 reinos infelices (infierno/niraya, reino animal/tiracchāna, espíritus hambrientos/peta y titanes/asura)"
        },
        "grammar": "Masculino (apāya) · apa + √i + -a",
        "grammarLocalized": {
            "pt": "Substantivo Masculino (apāya) · apa + √i + -a",
            "en": "Masculine Noun (apāya) · apa + √i + -a",
            "es": "Sustantivo Masculino (apāya) · apa + √i + -a"
        },
        "root": "apa (afastamento, perda) + √i (ir) + -a",
        "abhidhamma": {
            "ontology": {"pt": "Cosmologia Kármica (Apāyabhūmi)", "en": "Kammic Cosmology (Apāyabhūmi)", "es": "Cosmología Kármica (Apāyabhūmi)"},
            "category": {"pt": "Quatro Planos de Privação (Cap. V, §4)", "en": "Four Woeful Planes (Ch. V, §4)", "es": "Cuatro Planos de Privación (Cap. V, §4)"},
            "philosophy": {
                "pt": "Etimologicamente, apāya significa 'afastamento (apa) da felicidade e do mérito (aya)'. O renascimento nos quatro apāyas ocorre exclusivamente por meio da consciência de investigação resultante imoral acompanhada de equanimidade (upekkhāsahagataṃ akusalavipākaṃ santīraṇacittaṃ).",
                "en": "Etymologically, apāya means 'departure (apa) from happiness and merit (aya)'. Rebirth in the four apāyas occurs exclusively through the unwholesome-resultant investigating consciousness accompanied by equanimity (upekkhāsahagataṃ akusalavipākaṃ santīraṇacittaṃ).",
                "es": "Etimológicamente, apāya significa 'alejamiento (apa) de la felicidad y del mérito (aya)'. El renacimiento en los cuatro apāyas ocurre exclusivamente mediante la conciencia de investigación resultante inmoral acompañada de ecuanimidad (upekkhāsahagataṃ akusalavipākaṃ santīraṇacittaṃ)."
            },
            "bodhiRef": "CMA V §4 (pp. 188–189); V §9 (p. 197)"
        },
        "seeAlso": ["bhūmi", "santīraṇa", "paṭisandhi", "kamma"]
    },
    "kamma": {
        "meaning": {
            "pt": "Ação volitiva; volição (cetanā) saudável ou prejudicial que produz resultados (vipāka) e molda o fluxo de existência",
            "en": "Volitional action; wholesome or unwholesome volition (cetanā) that produces results (vipāka) and shapes the continuum of existence",
            "es": "Acción volitiva; volición (cetanā) saludable o perjudicial que produce resultados (vipāka) y moldea el continuo de la existencia"
        },
        "grammar": "Neutro (kamma, tema em -an: kamman) · √kar + -man",
        "grammarLocalized": {
            "pt": "Substantivo Neutro (kamma, tema kamman) · √kar + -man",
            "en": "Neuter Noun (kamma, stem kamman) · √kar + -man",
            "es": "Sustantivo Neutro (kamma, tema kamman) · √kar + -man"
        },
        "root": "√kar (fazer, agir) + -man",
        "abhidhamma": {
            "ontology": {"pt": "Realidade Última (Cetasika: Cetanā) & Lei Causal", "en": "Ultimate Reality (Cetasika: Cetanā) & Causal Law", "es": "Realidad Última (Cetasika: Cetanā) y Ley Causal"},
            "category": {"pt": "Quádruplo de Kamma (Kamacatukka — Cap. V, §§18–33)", "en": "Fourfold Kamma Classification (Kammacatukka — Ch. V, §§18–33)", "es": "Cuádruple Clasificación del Kamma (Kammacatukka — Cap. V, §§18–33)"},
            "philosophy": {
                "pt": "Ultimamente, kamma é a volição (cetanā) nos 12 akusala cittas e 17 lokiya kusala cittas. O Cap. V classifica o kamma em 16 tipos (quatro tétrades): (1) por função (janaka/produtor, upatthambhaka/sustentador, upapīḷaka/obstrutivo, upaghātaka/destrutivo); (2) por ordem de maturação (garuka/pesado, āsanna/próximo à morte, āciṇṇa/habitual, kaṭattā/reserva); (3) por tempo de fruto (diṭṭhadhammavedanīya, upapajjavedanīya, aparāpariyavedanīya, ahosi); e (4) por local de maturação.",
                "en": "Ultimately, kamma is volition (cetanā) in the 12 akusala cittas and 17 lokiya kusala cittas. Ch. V classifies kamma into 16 types (four tetrads): (1) by function (janaka/productive, upatthambhaka/supportive, upapīḷaka/obstructive, upaghātaka/destructive); (2) by order of ripening (garuka/weighty, āsanna/death-proximate, āciṇṇa/habitual, kaṭattā/reserve); (3) by time of ripening (diṭṭhadhammavedanīya, upapajjavedanīya, aparāpariyavedanīya, ahosi); and (4) by place of ripening.",
                "es": "Últimamente, kamma es la volición (cetanā) en las 12 akusala cittas y 17 lokiya kusala cittas. El Cap. V clasifica el kamma en 16 tipos (cuatro tétradas): (1) por función (janaka/productivo, upatthambhaka/sustentador, upapīḷaka/obstructivo, upaghātaka/destructivo); (2) por orden de maduración (garuka/pesado, āsanna/próximo a la muerte, āciṇṇa/habitual, kaṭattā/reserva); (3) por tiempo de maduración (diṭṭhadhammavedanīya, upapajjavedanīya, aparāpariyavedanīya, ahosi); y (4) por lugar de maduración."
            },
            "bodhiRef": "CMA V §§18–33 (pp. 200–213)"
        },
        "seeAlso": ["cetanā", "vipāka", "kusala", "akusala", "paṭisandhi"]
    },
    "somanassa": {
        "meaning": {
            "pt": "Alegria mental, prazer mental ou bem-estar psíquico; uma das cinco modalidades de sensação (vedanā), presente em 62 cittas",
            "en": "Mental joy, gladness, or pleasant mental feeling; one of the five modes of feeling (vedanā), present in 62 cittas",
            "es": "Alegría mental, gozo o sensación mental placentera; una de las cinco modalidades de sensación (vedanā), presente en 62 cittas"
        },
        "grammar": "Neutro (somanassa) · Taddhita abstrato de sumanas (su + manas + -ya)",
        "grammarLocalized": {
            "pt": "Substantivo Neutro (somanassa) · Derivado secundário (Taddhita) de su-manas",
            "en": "Neuter Noun (somanassa) · Secondary derivative (Taddhita) from su-manas",
            "es": "Sustantivo Neutro (somanassa) · Derivado secundario (Taddhita) de su-manas"
        },
        "root": "su (bom, bem) + √man (pensar, mente) + -ya",
        "samasa": {
            "breakdown": "su + manas + -ya (somanassa)",
            "type": {"pt": "Taddhita (Derivado Abstrato de Composto)", "en": "Taddhita (Abstract Derivative of Compound)", "es": "Taddhita (Derivado Abstracto de Compuesto)"},
            "viggaha": "sumanaso bhāvo = somanassaṃ",
            "literal": {"pt": "estado de ter uma mente feliz / bem-disposta", "en": "state of having a happy / well-disposed mind", "es": "estado de tener una mente feliz / bien dispuesta"},
            "parts": [{"pali": "su", "meaning": {"pt": "bom/feliz", "en": "good/happy", "es": "bueno/feliz"}}, {"pali": "manas", "meaning": {"pt": "mente", "en": "mind", "es": "mente"}}]
        },
        "abhidhamma": {
            "ontology": {"pt": "Realidade Última (Paramattha Dhamma — Cetasika: Vedanā)", "en": "Ultimate Reality (Paramattha Dhamma — Cetasika: Vedanā)", "es": "Realidad Última (Paramattha Dhamma — Cetasika: Vedanā)"},
            "category": {"pt": "Análise Quíntupla da Sensação (Pañcavidhavedanā — Cap. III, §§2–4)", "en": "Fivefold Analysis of Feeling (Pañcavidhavedanā — Ch. III, §§2–4)", "es": "Análisis Quíntuple de la Sensación (Pañcavidhavedanā — Cap. III, §§2–4)"},
            "lakkhanaCatukka": {
                "lakkhana": {"pt": "Experienciar um objeto mental agradável (iṭṭhārammaṇānubhavana-lakkhaṇa)", "en": "Experiencing an agreeable mental object (iṭṭhārammaṇānubhavana-lakkhaṇa)", "es": "Experimentar un objeto mental agradable (iṭṭhārammaṇānubhavana-lakkhaṇa)"},
                "rasa": {"pt": "Desfrutar o aspecto desejável do objeto mentalmente (sambhoga-rasa)", "en": "Enjoying the desirable aspect of the object mentally (sambhoga-rasa)", "es": "Disfrutar mentalmente el aspecto deseable del objeto (sambhoga-rasa)"},
                "paccupatthana": {"pt": "Satisfação psíquica ou estado alegre da mente (cetasika-assāda-paccupaṭṭhāna)", "en": "Mental gratification or joyful state of mind (cetasika-assāda-paccupaṭṭhāna)", "es": "Gratificación psíquica o estado alegre de la mente (cetasika-assāda-paccupaṭṭhāna)"},
                "padatthana": {"pt": "Tranquilidade (passaddhi) ou objeto aprazível", "en": "Tranquillity (passaddhi) or agreeable object", "es": "Tranquilidad (passaddhi) u objeto agradable"}
            },
            "philosophy": {
                "pt": "Distinto de pīti (entusiasmo/interesse que pertence a saṅkhārakkhandha), somanassa é a sensação prazerosa propriamente dita (vedanākkhandha) experimentada pela mente. Acompanha 18 cittas sem causa/da esfera sensual e 44 cittas de jhāna (1º ao 4º jhāna).",
                "en": "Distinct from pīti (zest/interest belonging to saṅkhārakkhandha), somanassa is pleasant mental feeling proper (vedanākkhandha). It accompanies 18 sense-sphere cittas and 44 jhāna cittas (1st to 4th jhāna).",
                "es": "Distinto de pīti (entusiasmo/interés que pertenece a saṅkhārakkhandha), somanassa es la sensación placentera mental propiamente dicha (vedanākkhandha). Acompaña a 18 cittas de la esfera sensual y 44 cittas de jhāna (1º al 4º jhāna)."
            },
            "bodhiRef": "CMA I §5 (p. 34); III §§2–4 (pp. 116–118)"
        },
        "seeAlso": ["vedanā", "pīti", "domanassa", "upekkhā", "sukha"]
    },
    "domanassa": {
        "meaning": {
            "pt": "Desprazer mental, tristeza, angústia ou dor psíquica; modalidade de sensação (vedanā) presente exclusivamente nas 2 cittas enraizadas em aversão (dosamūla)",
            "en": "Mental displeasure, grief, distress, or painful mental feeling; mode of feeling (vedanā) present exclusively in the 2 aversion-rooted cittas (dosamūla)",
            "es": "Displacer mental, tristeza, angustia o dolor psíquico; modalidad de sensación (vedanā) presente exclusivamente en las 2 cittas enraizadas en aversión (dosamūla)"
        },
        "grammar": "Neutro (domanassa) · Taddhita abstrato de dummanas (du + manas + -ya)",
        "grammarLocalized": {
            "pt": "Substantivo Neutro (domanassa) · Derivado secundário (Taddhita) de du-manas",
            "en": "Neuter Noun (domanassa) · Secondary derivative (Taddhita) from du-manas",
            "es": "Sustantivo Neutro (domanassa) · Derivado secundario (Taddhita) de du-manas"
        },
        "root": "du (mau, difícil, penoso) + √man (pensar, mente) + -ya",
        "abhidhamma": {
            "ontology": {"pt": "Realidade Última (Paramattha Dhamma — Cetasika: Vedanā)", "en": "Ultimate Reality (Paramattha Dhamma — Cetasika: Vedanā)", "es": "Realidad Última (Paramattha Dhamma — Cetasika: Vedanā)"},
            "category": {"pt": "Análise Quíntupla da Sensação (Pañcavidhavedanā — Cap. III, §§2–4)", "en": "Fivefold Analysis of Feeling (Pañcavidhavedanā — Ch. III, §§2–4)", "es": "Análisis Quíntuple de la Sensación (Pañcavidhavedanā — Cap. III, §§2–4)"},
            "lakkhanaCatukka": {
                "lakkhana": {"pt": "Experienciar um objeto mental desagradável (aniṭṭhārammaṇānubhavana-lakkhaṇa)", "en": "Experiencing an disagreeable mental object (aniṭṭhārammaṇānubhavana-lakkhaṇa)", "es": "Experimentar un objeto mental desagradable (aniṭṭhārammaṇānubhavana-lakkhaṇa)"},
                "rasa": {"pt": "Afligir a mente de modo aversivo (cetasika-vighāta-rasa)", "en": "Afflicting the mind aversively (cetasika-vighāta-rasa)", "es": "Afligir la mente de modo aversivo (cetasika-vighāta-rasa)"},
                "paccupatthana": {"pt": "Aflição ou dor mental (cetasika-ābādha-paccupaṭṭhāna)", "en": "Mental affliction or distress (cetasika-ābādha-paccupaṭṭhāna)", "es": "Aflicción o dolor mental (cetasika-ābādha-paccupaṭṭhāna)"},
                "padatthana": {"pt": "Base cardíaca (hadayavatthu) invariavelmente", "en": "Heart-base (hadayavatthu) invariably", "es": "Base cardíaca (hadayavatthu) invariablemente"}
            },
            "philosophy": {
                "pt": "Diferente da dor corporal (kāyika dukkha, que é resultado kármico neutro), domanassa é estritamente mental e sempre prejudicial (akusala), pois só surge invariavelmente associada à aversão (paṭigha/dosa). É abandonada definitivamente pelo Não-Retornante (Anāgāmī).",
                "en": "Unlike bodily pain (kāyika dukkha, which is kammically neutral resultant), domanassa is strictly mental and always unwholesome (akusala), as it arises invariably associated with aversion (paṭigha/dosa). It is definitively abandoned by the Non-Returner (Anāgāmī).",
                "es": "A diferencia del dolor corporal (kāyika dukkha, que es resultante kármicamente neutro), domanassa es estrictamente mental y siempre perjudicial (akusala), pues surge invariablemente asociada con la aversión (paṭigha/dosa). Es abandonada definitivamente por el No-Retornante (Anāgāmī)."
            },
            "bodhiRef": "CMA I §9 (p. 39); III §§2–4 (pp. 116–118)"
        },
        "seeAlso": ["vedanā", "dosa", "paṭigha", "somanassa", "upekkhā"]
    },
    "upekkhā": {
        "meaning": {
            "pt": "Equanimidade ou sensação neutra; (1) como sensação neutra (adukkhamasukhā vedanā) em 55 cittas, ou (2) como equilíbrio mental sublime (tatramajjhattatā, saṅkhārupekkhā, brahmavihārupekkhā)",
            "en": "Equanimity or neutral feeling; (1) as neutral feeling (adukkhamasukhā vedanā) in 55 cittas, or (2) as sublime mental balance (tatramajjhattatā, saṅkhārupekkhā, brahmavihārupekkhā)",
            "es": "Ecuanimidad o sensación neutra; (1) como sensación neutra (adukkhamasukhā vedanā) en 55 cittas, o (2) como equilibrio mental sublime (tatramajjhattatā, saṅkhārupekkhā, brahmavihārupekkhā)"
        },
        "grammar": "Feminino (upekkhā) · upa + √ikkh + -ā",
        "grammarLocalized": {
            "pt": "Substantivo Feminino (upekkhā) · upa + √ikkh + -ā",
            "en": "Feminine Noun (upekkhā) · upa + √ikkh + -ā",
            "es": "Sustantivo Femenino (upekkhā) · upa + √ikkh + -ā"
        },
        "root": "upa (sobre, imparcialmente) + √ikkh (olhar, observar) + -ā",
        "abhidhamma": {
            "ontology": {"pt": "Realidade Última (Cetasika: Vedanā ou Tatramajjhattatā)", "en": "Ultimate Reality (Cetasika: Vedanā or Tatramajjhattatā)", "es": "Realidad Última (Cetasika: Vedanā o Tatramajjhattatā)"},
            "category": {"pt": "Sensação Neutra (Vedanāpekkhā) & Equilíbrio Mental (Tatramajjhattatā)", "en": "Neutral Feeling (Vedanāpekkhā) & Mental Balance (Tatramajjhattatā)", "es": "Sensación Neutra (Vedanāpekkhā) y Equilibrio Mental (Tatramajjhattatā)"},
            "lakkhanaCatukka": {
                "lakkhana": {"pt": "Experienciar um objeto neutro/intermediário (majjhattārammaṇānubhavana-lakkhaṇa)", "en": "Experiencing a neutral/intermediate object (majjhattārammaṇānubhavana-lakkhaṇa)", "es": "Experimentar un objeto neutro/intermedio (majjhattārammaṇānubhavana-lakkhaṇa)"},
                "rasa": {"pt": "Não afligir nem entusiasmar excessivamente a mente (upamajjhatta-rasa)", "en": "Neither afflicting nor overly exciting the mind (upamajjhatta-rasa)", "es": "No afligir ni excitar excesivamente la mente (upamajjhatta-rasa)"},
                "paccupatthana": {"pt": "Estado silencioso ou pacificado da sensação (avyāpāra-bhāva-paccupaṭṭhāna)", "en": "Quiet or stilled state of feeling (avyāpāra-bhāva-paccupaṭṭhāna)", "es": "Estado silencioso o aquietado de la sensación (avyāpāra-bhāva-paccupaṭṭhāna)"},
                "padatthana": {"pt": "Ausência de entusiasmo (nippītika-cetovimutti) ou objeto neutro", "en": "Absence of zest (nippītika-cetovimutti) or neutral object", "es": "Ausencia de entusiasmo (nippītika-cetovimutti) u objeto neutro"}
            },
            "philosophy": {
                "pt": "O Abhidhamma faz uma distinção crucial: nas fórmulas de citta ('upekkhāsahagataṃ'), upekkhā refere-se ao cetasika vedanā (sensação neutra, nem dolorosa nem prazerosa). Já como virtude meditativa (4ª brahmavihāra ou 7º fator de iluminação), upekkhā refere-se ao cetasika tatramajjhattatā (neutralidade imparcial).",
                "en": "Abhidhamma makes a crucial distinction: in citta formulas ('upekkhāsahagataṃ'), upekkhā refers to the cetasika vedanā (neutral feeling, neither painful nor pleasant). As a meditative virtue (4th brahmavihāra or 7th enlightenment factor), upekkhā refers to the cetasika tatramajjhattatā (impartial neutrality).",
                "es": "El Abhidhamma hace una distinción crucial: en las fórmulas de citta ('upekkhāsahagataṃ'), upekkhā se refiere al cetasika vedanā (sensación neutra, ni dolorosa ni placentera). Como virtud meditativa (4ª brahmavihāra o 7º factor de iluminación), upekkhā se refiere al cetasika tatramajjhattatā (neutralidad imparcial)."
            },
            "bodhiRef": "CMA I §5 (p. 35); II §8 (p. 86); III §§2–4 (pp. 116–118)"
        },
        "seeAlso": ["vedanā", "tatramajjhattatā", "somanassa", "domanassa"]
    },
    "āsava": {
        "meaning": {
            "pt": "Impureza, efluente ou intoxicação mental profunda; as 4 correntes tóxicas que mantêm os seres no saṃsāra (kāmāsava, bhavāsava, diṭṭhāsava e avijjāsava)",
            "en": "Taint, canker, effluent, or deep mental intoxicant; the 4 toxic currents keeping beings in saṃsāra (kāmāsava, bhavāsava, diṭṭhāsava, and avijjāsava)",
            "es": "Impureza, efluente o intoxicación mental profunda; las 4 corrientes tóxicas que mantienen a los seres en el saṃsāra (kāmāsava, bhavāsava, diṭṭhāsava y avijjāsava)"
        },
        "grammar": "Masculino (āsava) · ā + √su + -a",
        "grammarLocalized": {
            "pt": "Substantivo Masculino (āsava) · ā + √su + -a",
            "en": "Masculine Noun (āsava) · ā + √su + -a",
            "es": "Sustantivo Masculino (āsava) · ā + √su + -a"
        },
        "root": "ā (até, desde) + √su (fluir, destilar) + -a",
        "abhidhamma": {
            "ontology": {"pt": "Realidade Última (3 Cetasikas: Lobha, Diṭṭhi, Moha)", "en": "Ultimate Reality (3 Cetasikas: Lobha, Diṭṭhi, Moha)", "es": "Realidad Última (3 Cetasikas: Lobha, Diṭṭhi, Moha)"},
            "category": {"pt": "Compêndio do Mal (Akusalasaṅgaha — Cap. VII, §3)", "en": "Compendium of the Unwholesome (Akusalasaṅgaha — Ch. VII, §3)", "es": "Compendio de lo Inmoral (Akusalasaṅgaha — Cap. VII, §3)"},
            "philosophy": {
                "pt": "Chamados de āsavas porque fluem até o topo da existência (bhavagga) no espaço e até a mudança-de-linhagem (gotrabhū) no tempo, ou porque são como licores fermentados por longo tempo. Embora sejam 4 em nome, correspondem a 3 cetasikas últimos: kāmāsava e bhavāsava são lobha; diṭṭhāsava é diṭṭhi; avijjāsava é moha.",
                "en": "Called āsavas because they flow up to the topmost plane of existence (bhavagga) in space and up to change-of-lineage (gotrabhū) in time, or because they are like long-fermented liquor. Though 4 in name, they reduce to 3 ultimate cetasikas: kāmāsava and bhavāsava are lobha; diṭṭhāsava is diṭṭhi; avijjāsava is moha.",
                "es": "Llamados āsavas porque fluyen hasta la cima de la existencia (bhavagga) en el espacio y hasta el cambio de linaje (gotrabhū) en el tiempo, o porque son como licores largamente fermentados. Aunque son 4 en nombre, se reducen a 3 cetasikas últimos: kāmāsava y bhavāsava son lobha; diṭṭhāsava es diṭṭhi; avijjāsava es moha."
            },
            "bodhiRef": "CMA VII §3 (pp. 266–267)"
        },
        "seeAlso": ["lobha", "diṭṭhi", "moha", "kilesa", "upādāna"]
    },
    "nīvaraṇa": {
        "meaning": {
            "pt": "Obstáculo ou impedimento mental; os 5 obstáculos (kāmacchanda, vyāpāda, thīnamiddha, uddhaccakukkucca, vicikicchā — mais avijjā no Abhidhamma, totalizando 6)",
            "en": "Hindrance or mental obstacle; the 5 hindrances (kāmacchanda, vyāpāda, thīnamiddha, uddhaccakukkucca, vicikicchā — plus avijjā in Abhidhamma, totaling 6)",
            "es": "Obstáculo o impedimento mental; los 5 obstáculos (kāmacchanda, vyāpāda, thīnamiddha, uddhaccakukkucca, vicikicchā — más avijjā en el Abhidhamma, totalizando 6)"
        },
        "grammar": "Neutro (nīvaraṇa) · ni + √var + -ana",
        "grammarLocalized": {
            "pt": "Substantivo Neutro (nīvaraṇa) · ni + √var + -ana",
            "en": "Neuter Noun (nīvaraṇa) · ni + √var + -ana",
            "es": "Sustantivo Neutro (nīvaraṇa) · ni + √var + -ana"
        },
        "root": "ni (para baixo, completamente) + √var (obstruir, cobrir) + -ana",
        "abhidhamma": {
            "ontology": {"pt": "Realidade Última (8 Cetasikas Akusala)", "en": "Ultimate Reality (8 Akusala Cetasikas)", "es": "Realidad Última (8 Cetasikas Akusala)"},
            "category": {"pt": "Compêndio do Mal (Akusalasaṅgaha — Cap. VII, §7)", "en": "Compendium of the Unwholesome (Akusalasaṅgaha — Ch. VII, §7)", "es": "Compendio de lo Inmoral (Akusalasaṅgaha — Cap. VII, §7)"},
            "philosophy": {
                "pt": "Chamados de nīvaraṇas porque obstruem a saída do saṃsāra, impedem o surgimento dos jhānas e cegam o olho da sabedoria. No Cap. VII §7 do Sangaha, são listados 6 obstáculos (adicionando avijjā aos 5 clássicos dos Suttas), que se reduzem a 8 cetasikas últimos: lobha, dosa, thīna, middha, uddhacca, kukkucca, vicikicchā e moha.",
                "en": "Called nīvaraṇas because they obstruct the outlet from saṃsāra, prevent the arising of jhānas, and blind the eye of wisdom. In Ch. VII §7 of the Sangaha, 6 hindrances are listed (adding avijjā to the 5 classical Sutta hindrances), which reduce to 8 ultimate cetasikas: lobha, dosa, thīna, middha, uddhacca, kukkucca, vicikicchā, and moha.",
                "es": "Llamados nīvaraṇas porque obstruyen la salida del saṃsāra, impiden el surgimiento de los jhānas y ciegan el ojo de la sabiduría. En el Cap. VII §7 del Sangaha, se enumeran 6 obstáculos (añadiendo avijjā a los 5 obstáculos clásicos de los Suttas), que se reducen a 8 cetasikas últimos: lobha, dosa, thīna, middha, uddhacca, kukkucca, vicikicchā y moha."
            },
            "bodhiRef": "CMA VII §7 (p. 269); IX §17 (p. 341)"
        },
        "seeAlso": ["jhāna", "kilesa", "thīna", "middha", "vicikicchā"]
    },
    "kilesa": {
        "meaning": {
            "pt": "Contaminação, impureza ou aflição mental; as 10 contaminações (lobha, dosa, moha, māna, diṭṭhi, vicikicchā, thīna, uddhacca, ahirika, anottappa)",
            "en": "Defilement, impurity, or mental affliction; the 10 defilements (lobha, dosa, moha, māna, diṭṭhi, vicikicchā, thīna, uddhacca, ahirika, anottappa)",
            "es": "Contaminación, impureza o aflicción mental; las 10 contaminaciones (lobha, dosa, moha, māna, diṭṭhi, vicikicchā, thīna, uddhacca, ahirika, anottappa)"
        },
        "grammar": "Masculino (kilesa) · √kilis + -a",
        "grammarLocalized": {
            "pt": "Substantivo Masculino (kilesa) · √kilis + -a",
            "en": "Masculine Noun (kilesa) · √kilis + -a",
            "es": "Sustantivo Masculino (kilesa) · √kilis + -a"
        },
        "root": "√kilis (atormentar, manchar, afligir) + -a",
        "abhidhamma": {
            "ontology": {"pt": "Realidade Última (10 Cetasikas Akusala)", "en": "Ultimate Reality (10 Akusala Cetasikas)", "es": "Realidad Última (10 Cetasikas Akusala)"},
            "category": {"pt": "Compêndio do Mal (Akusalasaṅgaha — Cap. VII, §12)", "en": "Compendium of the Unwholesome (Akusalasaṅgaha — Ch. VII, §12)", "es": "Compendio de lo Inmoral (Akusalasaṅgaha — Cap. VII, §12)"},
            "philosophy": {
                "pt": "São chamados de kilesas porque são eles mesmos afligidos/impuros e porque atormentam e mancham a corrente mental. Diferentemente das outras categorias do Cap. VII (onde múltiplos nomes apontam para 2 ou 3 cetasikas), os 10 kilesas têm correspondência 1-para-1 exata com 10 cetasikas akusala distintos.",
                "en": "Called kilesas because they are themselves afflicted/impure and because they torment and stain the mental stream. Unlike other categories in Ch. VII (where multiple names point to 2 or 3 cetasikas), the 10 kilesas have an exact 1-to-1 correspondence with 10 distinct akusala cetasikas.",
                "es": "Llamados kilesas porque ellos mismos están afligidos/impuros y porque atormentan y manchan la corriente mental. A diferencia de otras categorías del Cap. VII (donde múltiples nombres apuntan a 2 o 3 cetasikas), los 10 kilesas tienen una correspondencia exacta 1 a 1 con 10 cetasikas akusala distintos."
            },
            "bodhiRef": "CMA VII §12 (p. 272); VII §13 (p. 273)"
        },
        "seeAlso": ["akusala", "āsava", "nīvaraṇa", "anusaya", "saṃyojana"]
    },
    "paccaya": {
        "meaning": {
            "pt": "Condição, suporte causal ou força condicionante; aquilo de que um fenômeno depende para surgir ou persistir (as 24 condições do Paṭṭhāna)",
            "en": "Condition, causal support, or conditioning force; that upon which a phenomenon depends for its arising or persistence (the 24 conditions of the Paṭṭhāna)",
            "es": "Condición, soporte causal o fuerza condicionante; aquello de lo que depende un fenómeno para surgir o persistir (las 24 condiciones del Paṭṭhāna)"
        },
        "grammar": "Masculino (paccaya) · paṭi + √i + -a",
        "grammarLocalized": {
            "pt": "Substantivo Masculino (paccaya) · paṭi + √i + -a",
            "en": "Masculine Noun (paccaya) · paṭi + √i + -a",
            "es": "Sustantivo Masculino (paccaya) · paṭi + √i + -a"
        },
        "root": "paṭi (em direção a, dependendo de) + √i (ir) + -a",
        "abhidhamma": {
            "ontology": {"pt": "Princípio Relacional e Causal (Paccayasaṅgaha)", "en": "Relational & Causal Principle (Paccayasaṅgaha)", "es": "Principio Relacional y Causal (Paccayasaṅgaha)"},
            "category": {"pt": "Compêndio das Condições (Paccayasaṅgahavibhāga — Cap. VIII)", "en": "Compendium of Conditions (Paccayasaṅgahavibhāga — Ch. VIII)", "es": "Compendio de las Condiciones (Paccayasaṅgahavibhāga — Cap. VIII)"},
            "lakkhanaCatukka": {
                "lakkhana": {"pt": "Ter a característica de prestar assistência ou ser um suporte eficaz (upakāraka-lakkhaṇa)", "en": "Having the characteristic of rendering assistance or being an efficacious support (upakāraka-lakkhaṇa)", "es": "Tener la característica de prestar asistencia o ser un soporte eficaz (upakāraka-lakkhaṇa)"},
                "rasa": {"pt": "Fazer surgir ou sustentar os estados condicionados (paccayuppanna-dhamma)", "en": "Causing conditioned states (paccayuppanna-dhamma) to arise or persist", "es": "Hacer surgir o sostener los estados condicionados (paccayuppanna-dhamma)"},
                "paccupatthana": {"pt": "Não-independência dos fenômenos; interdependência causal", "en": "Non-independence of phenomena; causal interdependence", "es": "No-independencia de los fenómenos; interdependencia causal"},
                "padatthana": {"pt": "A própria natureza específica (sabhāva) do estado condicionante", "en": "The specific intrinsic nature (sabhāva) of the conditioning state", "es": "La naturaleza intrínseca específica (sabhāva) del estado condicionante"}
            },
            "philosophy": {
                "pt": "A definição clássica nos Comentários é 'upakārako dhammo paccayo' ('uma condição é um dhamma que presta assistência'). O Cap. VIII expõe os dois métodos de condicionalidade: (1) Paṭiccasamuppāda (que analisa que estados condicionam quais outros) e (2) Paṭṭhāna (que analisa pelas 24 forças condicionantes — paccayasatti — o modo como um estado assiste outro).",
                "en": "The classical commentarial definition is 'upakārako dhammo paccayo' ('a condition is a dhamma that renders assistance'). Ch. VIII expounds the two methods of conditionality: (1) Paṭiccasamuppāda (analyzing which states condition which) and (2) Paṭṭhāna (analyzing via 24 conditioning forces — paccayasatti — how one state assists another).",
                "es": "La definición clásica en los Comentarios es 'upakārako dhammo paccayo' ('una condición es un dhamma que presta asistencia'). El Cap. VIII expone los dos métodos de condicionalidad: (1) Paṭiccasamuppāda (que analiza qué estados condicionan a cuáles) y (2) Paṭṭhāna (que analiza mediante las 24 fuerzas condicionantes — paccayasatti — cómo un estado asiste a otro)."
            },
            "bodhiRef": "CMA VIII §§1–29 (pp. 291–326)"
        },
        "seeAlso": ["paṭṭhāna", "paṭiccasamuppāda", "hetu", "ārammaṇa"]
    },
    "paṭṭhāna": {
        "meaning": {
            "pt": "Relações Condicionais; o 7º e culminante livro do Abhidhamma Piṭaka, que analisa a matriz de 24 condições (paccaya) entre todas as realidades últimas",
            "en": "Conditional Relations; the 7th and culminating book of the Abhidhamma Piṭaka, analyzing the matrix of 24 conditions (paccaya) among all ultimate realities",
            "es": "Relaciones Condicionales; el 7º y culminante libro del Abhidhamma Piṭaka, que analiza la matriz de 24 condiciones (paccaya) entre todas las realidades últimas"
        },
        "grammar": "Neutro (paṭṭhāna) · pa + √ṭhā + -ana",
        "grammarLocalized": {
            "pt": "Substantivo Neutro (paṭṭhāna) · pa + √ṭhā + -ana",
            "en": "Neuter Noun (paṭṭhāna) · pa + √ṭhā + -ana",
            "es": "Sustantivo Neutro (paṭṭhāna) · pa + √ṭhā + -ana"
        },
        "root": "pa (vários, principais) + √ṭhā (estar de pé, estabelecer, causa) + -ana",
        "abhidhamma": {
            "ontology": {"pt": "Método de Condicionalidade (Paṭṭhānanaya)", "en": "Method of Conditionality (Paṭṭhānanaya)", "es": "Método de Condicionalidad (Paṭṭhānanaya)"},
            "category": {"pt": "Compêndio das Condições (Cap. VIII, §§11–28)", "en": "Compendium of Conditions (Ch. VIII, §§11–28)", "es": "Compendio de las Condiciones (Cap. VIII, §§11–28)"},
            "philosophy": {
                "pt": "Enquanto o método do Paṭiccasamuppāda mostra a sequência vertical dos elos que geram o saṃsāra, o método do Paṭṭhāna examina a rede multidimensional de 24 modos de condicionalidade (hetu, ārammaṇa, adhipati, anantara, samanantara, sahajāta, aññamañña, nissaya, upanissaya, etc.), sintetizados no Sangaha em 6 pares relacionais entre nāma, rūpa e paññatti.",
                "en": "While the Paṭiccasamuppāda method shows the vertical sequence of links generating saṃsāra, the Paṭṭhāna method examines the multidimensional web of 24 modes of conditionality (hetu, ārammaṇa, adhipati, anantara, samanantara, sahajāta, aññamañña, nissaya, upanissaya, etc.), synthesized in the Sangaha into 6 relational pairs among nāma, rūpa, and paññatti.",
                "es": "Mientras el método del Paṭiccasamuppāda muestra la secuencia vertical de eslabones que generan el saṃsāra, el método del Paṭṭhāna examina la red multidimensional de 24 modos de condicionalidad (hetu, ārammaṇa, adhipati, anantara, samanantara, sahajāta, aññamañña, nissaya, upanissaya, etc.), sintetizados en el Sangaha en 6 pares relacionales entre nāma, rūpa y paññatti."
            },
            "bodhiRef": "CMA VIII §§11–28 (pp. 303–324)"
        },
        "seeAlso": ["paccaya", "paṭiccasamuppāda", "abhidhamma", "hetu"]
    },
    "paṭiccasamuppāda": {
        "meaning": {
            "pt": "Origem Dependente ou Co-originação Condicionada; a cadeia de 12 elos (nidānas) que explica o surgimento condicionado do sofrimento sem um eu criador",
            "en": "Dependent Origination or Conditioned Co-arising; the 12-link chain (nidānas) explaining the conditioned arising of suffering without a creator self",
            "es": "Originación Dependiente o Co-surgimiento Condicionado; la cadena de 12 eslabones (nidānas) que explica el surgimiento condicionado del sufrimiento sin un yo creador"
        },
        "grammar": "Masculino (paṭiccasamuppāda) · paṭicca + saṃ + ud + √pad + -a",
        "grammarLocalized": {
            "pt": "Substantivo Masculino Composto · paṭicca (gerúndio) + samuppāda",
            "en": "Masculine Compound Noun · paṭicca (gerund) + samuppāda",
            "es": "Sustantivo Masculino Compuesto · paṭicca (gerundio) + samuppāda"
        },
        "root": "paṭi + √i + -tvā (paṭicca) + saṃ + ud + √pad (surgir juntamente)",
        "samasa": {
            "breakdown": "paṭicca + samuppāda",
            "type": {"pt": "Kammadhāraya / Tatpurisa Verbal", "en": "Kammadhāraya / Verbal Tatpurisa", "es": "Kammadhāraya / Tatpurisa Verbal"},
            "viggaha": "paṭiccahetuṃ paṭicca samuppajjatī ti paṭiccasamuppādo",
            "literal": {"pt": "surgimento conjunto na dependência de (condições)", "en": "arising together in dependence upon (conditions)", "es": "surgimiento conjunto en dependencia de (condiciones)"},
            "parts": [{"pali": "paṭicca", "meaning": {"pt": "dependendo de", "en": "depending on", "es": "dependiendo de"}}, {"pali": "samuppāda", "meaning": {"pt": "surgimento conjunto", "en": "co-arising", "es": "co-surgimiento"}}]
        },
        "abhidhamma": {
            "ontology": {"pt": "Lei Causal das Realidades Condicionadas (Cap. VIII, §§3–10)", "en": "Causal Law of Conditioned Realities (Ch. VIII, §§3–10)", "es": "Ley Causal de las Realidades Condicionadas (Cap. VIII, §§3–10)"},
            "category": {"pt": "Método da Origem Dependente (Paṭiccasamuppādanaya — Cap. VIII)", "en": "Method of Dependent Origination (Paṭiccasamuppādanaya — Ch. VIII)", "es": "Método de la Originación Dependiente (Paṭiccasamuppādanaya — Cap. VIII)"},
            "philosophy": {
                "pt": "No Cap. VIII §§3–10, os 12 elos (avijjā, saṅkhārā, viññāṇa, nāmarūpa, saḷāyatana, phassa, vedanā, taṇhā, upādāna, bhava, jāti, jarāmaraṇa) são analisados através de 3 tempos (passado, presente, futuro), 4 grupos de resumo, 20 modos (ākāras), 3 conexões (sandhi) e 3 voltas (vaṭṭa: kilesavaṭṭa, kammavaṭṭa, vipākavaṭṭa).",
                "en": "In Ch. VIII §§3–10, the 12 links (avijjā, saṅkhārā, viññāṇa, nāmarūpa, saḷāyatana, phassa, vedanā, taṇhā, upādāna, bhava, jāti, jarāmaraṇa) are analyzed across 3 periods (past, present, future), 4 summary sections, 20 modes (ākāras), 3 connections (sandhi), and 3 rounds (vaṭṭa: kilesavaṭṭa, kammavaṭṭa, vipākavaṭṭa).",
                "es": "En el Cap. VIII §§3–10, los 12 eslabones (avijjā, saṅkhārā, viññāṇa, nāmarūpa, saḷāyatana, phassa, vedanā, taṇhā, upādāna, bhava, jāti, jarāmaraṇa) se analizan a través de 3 tiempos (pasado, presente, futuro), 4 secciones de resumen, 20 modos (ākāras), 3 conexiones (sandhi) y 3 rondas (vaṭṭa: kilesavaṭṭa, kammavaṭṭa, vipākavaṭṭa)."
            },
            "bodhiRef": "CMA VIII §§3–10 (pp. 293–303)"
        },
        "seeAlso": ["paccaya", "paṭṭhāna", "avijjā", "kamma", "vipāka"]
    },
    "samatha": {
        "meaning": {
            "pt": "Serenidade, calma meditativa ou tranquilidade mental; o desenvolvimento da concentração (samādhi-bhāvanā) através dos 40 objetos de meditação (kammaṭṭhāna)",
            "en": "Serenity, meditative calm, or mental tranquillity; the development of concentration (samādhi-bhāvanā) through the 40 meditation subjects (kammaṭṭhāna)",
            "es": "Serenidad, calma meditativa o tranquilidad mental; el desarrollo de la concentración (samādhi-bhāvanā) a través de los 40 sujetos de meditación (kammaṭṭhāna)"
        },
        "grammar": "Masculino (samatha) · √sam + -atha",
        "grammarLocalized": {
            "pt": "Substantivo Masculino (samatha) · √sam + -atha",
            "en": "Masculine Noun (samatha) · √sam + -atha",
            "es": "Sustantivo Masculino (samatha) · √sam + -atha"
        },
        "root": "√sam (acalmar, pacificar, aquietar) + -atha",
        "abhidhamma": {
            "ontology": {"pt": "Realidade Última (Cetasika: Ekaggatā em Cittas Saudáveis)", "en": "Ultimate Reality (Cetasika: Ekaggatā in Wholesome Cittas)", "es": "Realidad Última (Cetasika: Ekaggatā en Cittas Saludables)"},
            "category": {"pt": "Compêndio de Objetos de Meditação (Cap. IX, §§2–21)", "en": "Compendium of Meditation Subjects (Ch. IX, §§2–21)", "es": "Compendio de Sujetos de Meditación (Cap. IX, §§2–21)"},
            "philosophy": {
                "pt": "Chamado de samatha porque pacifica (sameti) os 5 obstáculos (nīvaraṇas). Ultimamente, corresponde à unidirecionalidade (ekaggatā) nos cittas de concentração de acesso (upacārasamādhi) e absorção (appanāsamādhi), desenvolvida por meio dos 40 kammaṭṭhānas (10 kasiṇas, 10 asubhas, 10 anussatis, 4 brahmavihāras, 4 āruppas, 1 saññā, 1 vavatthāna).",
                "en": "Called samatha because it pacifies (sameti) the 5 hindrances (nīvaraṇas). Ultimately, it corresponds to one-pointedness (ekaggatā) in cittas of access concentration (upacārasamādhi) and absorption (appanāsamādhi), developed through the 40 kammaṭṭhānas (10 kasiṇas, 10 asubhas, 10 anussatis, 4 brahmavihāras, 4 āruppas, 1 saññā, 1 vavatthāna).",
                "es": "Llamado samatha porque pacifica (sameti) los 5 obstáculos (nīvaraṇas). Últimamente, corresponde a la unidireccionalidad (ekaggatā) en las cittas de concentración de acceso (upacārasamādhi) y absorción (appanāsamādhi), desarrollada mediante los 40 kammaṭṭhānas (10 kasiṇas, 10 asubhas, 10 anussatis, 4 brahmavihāras, 4 āruppas, 1 saññā, 1 vavatthāna)."
            },
            "bodhiRef": "CMA IX §§2–21 (pp. 329–344)"
        },
        "seeAlso": ["vipassanā", "kammaṭṭhāna", "ekaggatā", "jhāna", "nimitta"]
    },
    "vipassanā": {
        "meaning": {
            "pt": "Insight, visão cabal ou discernimento meditativo direto; a sabedoria (paññā) que contempla nāma e rūpa sob a luz das três marcas (anicca, dukkha, anattā)",
            "en": "Insight or direct meditative discernment; wisdom (paññā) contemplating nāma and rūpa in the light of the three characteristics (anicca, dukkha, anattā)",
            "es": "Insight, visión penetrante o discernimiento meditativo directo; la sabiduría (paññā) que contempla nāma y rūpa a la luz de las tres características (anicca, dukkha, anattā)"
        },
        "grammar": "Feminino (vipassanā) · vi + √dis/pass + -anā",
        "grammarLocalized": {
            "pt": "Substantivo Feminino (vipassanā) · vi + √dis/pass + -anā",
            "en": "Feminine Noun (vipassanā) · vi + √dis/pass + -anā",
            "es": "Sustantivo Femenino (vipassanā) · vi + √dis/pass + -anā"
        },
        "root": "vi (de modos distintos, penetrantemente) + √dis / pass (ver) + -anā",
        "abhidhamma": {
            "ontology": {"pt": "Realidade Última (Paramattha Dhamma — Cetasika: Paññindriya)", "en": "Ultimate Reality (Paramattha Dhamma — Cetasika: Paññindriya)", "es": "Realidad Última (Paramattha Dhamma — Cetasika: Paññindriya)"},
            "category": {"pt": "Compêndio de Insight (Vipassanākammaṭṭhāna — Cap. IX, §§22–44)", "en": "Compendium of Insight (Vipassanākammaṭṭhāna — Ch. IX, §§22–44)", "es": "Compendio de Insight (Vipassanākammaṭṭhāna — Cap. IX, §§22–44)"},
            "lakkhanaCatukka": {
                "lakkhana": {"pt": "Penetrar as características universais (impermanência, sofrimento, não-eu) das formações (aniccādi-lakkhaṇa-paṭivedha)", "en": "Penetrating the universal characteristics (impermanence, suffering, non-self) of formations (aniccādi-lakkhaṇa-paṭivedha)", "es": "Penetrar las características universales (impermanencia, sufrimiento, no-yo) de las formaciones (aniccādi-lakkhaṇa-paṭivedha)"},
                "rasa": {"pt": "Destruir a escuridão da delusão que oculta a natureza real dos dhammas", "en": "Destroying the darkness of delusion that conceals the real nature of dhammas", "es": "Destruir la oscuridad de la ilusión que oculta la naturaleza real de los dhammas"},
                "paccupatthana": {"pt": "Desapego e visão clara das formações condicionais (asaṃmoha-paccupaṭṭhāna)", "en": "Disenchantment and clear vision of conditioned formations (asaṃmoha-paccupaṭṭhāna)", "es": "Desencanto y visión clara de las formaciones condicionadas (asaṃmoha-paccupaṭṭhāna)"},
                "padatthana": {"pt": "As 7 purificações (visuddhi) e a atenção com sabedoria (yoniso manasikāra)", "en": "The 7 purifications (visuddhi) and wise attention (yoniso manasikāra)", "es": "Las 7 purificaciones (visuddhi) y la atención sabia (yoniso manasikāra)"}
            },
            "philosophy": {
                "pt": "Enquanto samatha toma conceitos (paññatti) ou realidades para aquietar a mente e suprimir os obstáculos temporariamente (vikkhambhanappahāna), vipassanā toma exclusivamente realidades últimas condicionadas (nāma-rūpa / saṅkhāra-dhamma) como objeto, progredindo pelas 7 purificações (satta visuddhi) e 10 conhecimentos de insight (vipassanā-ñāṇa) até emergir no Caminho Supramundano (lokuttara magga).",
                "en": "While samatha takes concepts (paññatti) or realities to calm the mind and temporarily suppress hindrances (vikkhambhanappahāna), vipassanā takes exclusively conditioned ultimate realities (nāma-rūpa / saṅkhāra-dhamma) as its object, progressing through the 7 purifications (satta visuddhi) and 10 insight knowledges (vipassanā-ñāṇa) until emerging in the Supramundane Path (lokuttara magga).",
                "es": "Mientras samatha toma conceptos (paññatti) o realidades para calmar la mente y suprimir temporalmente los obstáculos (vikkhambhanappahāna), vipassanā toma exclusivamente realidades últimas condicionadas (nāma-rūpa / saṅkhāra-dhamma) como objeto, progresando por las 7 purificaciones (satta visuddhi) y los 10 conocimientos de insight (vipassanā-ñāṇa) hasta emerger en el Sendero Supramundano (lokuttara magga)."
            },
            "bodhiRef": "CMA IX §§22–44 (pp. 344–369)"
        },
        "seeAlso": ["samatha", "paññā", "visuddhi", "tilakkhaṇa", "magga"]
    },
    "kammaṭṭhāna": {
        "meaning": {
            "pt": "Objeto de meditação ou 'lugar de trabalho' meditativo; os 40 temas de Samatha e os temas de Vipassanā expostos no Cap. IX",
            "en": "Meditation subject or meditative 'workplace'; the 40 subjects of Samatha and the subjects of Vipassanā expounded in Ch. IX",
            "es": "Sujeto de meditación o 'lugar de trabajo' meditativo; los 40 temas de Samatha y los temas de Vipassanā expuestos en el Cap. IX"
        },
        "grammar": "Neutro (kammaṭṭhāna) · kamma + ṭhāna",
        "grammarLocalized": {
            "pt": "Substantivo Neutro Composto (Chattī Tatpurisa) · kamma + ṭhāna",
            "en": "Neuter Compound Noun (Genitive Tatpurisa) · kamma + ṭhāna",
            "es": "Sustantivo Neutro Compuesto (Tatpurisa Genitivo) · kamma + ṭhāna"
        },
        "root": "√kar (fazer) + √ṭhā (permanecer, lugar)",
        "samasa": {
            "breakdown": "kamma + ṭhāna",
            "type": {"pt": "Chattī Tatpurisa (Determinativo Genitivo)", "en": "Genitive Tatpurisa (Determinative)", "es": "Tatpurisa Genitivo (Determinativo)"},
            "viggaha": "bhāvanā-kammassa ṭhānaṃ = kammaṭṭhānaṃ",
            "literal": {"pt": "lugar de trabalho (da meditação) / base da ação", "en": "workplace (of meditation) / basis of work", "es": "lugar de trabajo (de la meditación) / base del trabajo"},
            "parts": [{"pali": "kamma", "meaning": {"pt": "trabalho/prática", "en": "work/practice", "es": "trabajo/práctica"}}, {"pali": "ṭhāna", "meaning": {"pt": "lugar/base", "en": "place/ground", "es": "lugar/base"}}]
        },
        "abhidhamma": {
            "ontology": {"pt": "Metodologia Meditativa (Bhāvanā)", "en": "Meditative Methodology (Bhāvanā)", "es": "Metodología Meditativa (Bhāvanā)"},
            "category": {"pt": "Compêndio dos Objetos de Meditação (Kammaṭṭhānasaṅgahavibhāga — Cap. IX)", "en": "Compendium of Meditation Subjects (Kammaṭṭhānasaṅgahavibhāga — Ch. IX)", "es": "Compendio de los Sujetos de Meditación (Kammaṭṭhānasaṅgahavibhāga — Cap. IX)"},
            "philosophy": {
                "pt": "O Cap. IX encerra o Abhidhammattha Saṅgaha aplicando toda a ontologia teórica dos capítulos I–VIII à prática meditativa (bhāvanā), dividida em Samatha-kammaṭṭhāna (tranquilidade) e Vipassanā-kammaṭṭhāna (insight).",
                "en": "Ch. IX concludes the Abhidhammattha Saṅgaha by applying the entire theoretical ontology of Chapters I–VIII to meditative practice (bhāvanā), divided into Samatha-kammaṭṭhāna (tranquillity) and Vipassanā-kammaṭṭhāna (insight).",
                "es": "El Cap. IX concluye el Abhidhammattha Saṅgaha aplicando toda la ontología teórica de los capítulos I–VIII a la práctica meditativa (bhāvanā), dividida en Samatha-kammaṭṭhāna (tranquilidad) y Vipassanā-kammaṭṭhāna (insight)."
            },
            "bodhiRef": "CMA IX §§1–2 (pp. 328–331)"
        },
        "seeAlso": ["samatha", "vipassanā", "nimitta", "visuddhi"]
    },
    "visuddhi": {
        "meaning": {
            "pt": "Purificação; as 7 etapas progressivas de purificação (satta visuddhi) que estruturam o caminho de Vipassanā e o Visuddhimagga",
            "en": "Purification; the 7 progressive stages of purification (satta visuddhi) structuring the path of Vipassanā and the Visuddhimagga",
            "es": "Purificación; las 7 etapas progresivas de purificación (satta visuddhi) que estructuran el sendero de Vipassanā y el Visuddhimagga"
        },
        "grammar": "Feminino (visuddhi) · vi + √sudh + -ti",
        "grammarLocalized": {
            "pt": "Substantivo Feminino (visuddhi) · vi + √sudh + -ti",
            "en": "Feminine Noun (visuddhi) · vi + √sudh + -ti",
            "es": "Sustantivo Femenino (visuddhi) · vi + √sudh + -ti"
        },
        "root": "vi (completamente) + √sudh (purificar) + -ti",
        "abhidhamma": {
            "ontology": {"pt": "Estrutura Soteriológica (Satta Visuddhi)", "en": "Soteriological Framework (Satta Visuddhi)", "es": "Estructura Soteriológica (Satta Visuddhi)"},
            "category": {"pt": "Compêndio de Insight (Cap. IX, §22 & §§28–37)", "en": "Compendium of Insight (Ch. IX, §22 & §§28–37)", "es": "Compendio de Insight (Cap. IX, §22 y §§28–37)"},
            "philosophy": {
                "pt": "As 7 purificações são: (1) Sīlavisuddhi (virtude), (2) Cittavisuddhi (mente/concentração), (3) Diṭṭhivisuddhi (visão: discernimento de nāma-rūpa), (4) Kaṅkhāvitaraṇavisuddhi (superação da dúvida: discernimento das condições), (5) Maggāmaggañāṇadassanavisuddhi (distinção entre caminho e não-caminho), (6) Paṭipadāñāṇadassanavisuddhi (conhecimento do progresso pelas 9 ñāṇas de insight) e (7) Ñāṇadassanavisuddhi (os 4 Caminhos Supramundanos).",
                "en": "The 7 purifications are: (1) Sīlavisuddhi (virtue), (2) Cittavisuddhi (mind/concentration), (3) Diṭṭhivisuddhi (view: discerning nāma-rūpa), (4) Kaṅkhāvitaraṇavisuddhi (overcoming doubt: discerning conditions), (5) Maggāmaggañāṇadassanavisuddhi (distinguishing path and non-path), (6) Paṭipadāñāṇadassanavisuddhi (knowledge of progress through the 9 insight ñāṇas), and (7) Ñāṇadassanavisuddhi (the 4 Supramundane Paths).",
                "es": "Las 7 purificaciones son: (1) Sīlavisuddhi (virtud), (2) Cittavisuddhi (mente/concentración), (3) Diṭṭhivisuddhi (visión: discernimiento de nāma-rūpa), (4) Kaṅkhāvitaraṇavisuddhi (superación de la duda: discernimiento de las condiciones), (5) Maggāmaggañāṇadassanavisuddhi (distinción entre sendero y no-sendero), (6) Paṭipadāñāṇadassanavisuddhi (conocimiento del progreso por los 9 ñāṇas de insight) y (7) Ñāṇadassanavisuddhi (los 4 Senderos Supramundanos)."
            },
            "bodhiRef": "CMA IX §22 (p. 345); IX §§28–37 (pp. 348–359)"
        },
        "seeAlso": ["vipassanā", "paññā", "magga", "nibbāna"]
    }
}

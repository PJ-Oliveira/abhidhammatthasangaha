// src/data/ankiCards.ts
export type Language = 'en' | 'pt' | 'es';

export interface CardContent {
  question: string;
  answer: string;
  breakdown: string[];
  explanation: string;
  mnemonicOrExamTip: string;
  examQuestionType: string;
}

export interface AnkiCard {
  id: string;
  chapter: number;
  chapterName: {
    en: string;
    pt: string;
    es: string;
    pali: string;
  };
  section: string;
  category: 'quantities' | 'structures' | 'relations' | 'philosophy' | 'exam_traps';
  paliTerm: string;
  en: CardContent;
  pt: CardContent;
  es: CardContent;
  tags: string[];
}

export const ANKI_CARDS: AnkiCard[] = [
  {
    "id": "ch1-01",
    "chapter": 1,
    "chapterName": {
      "pali": "Cittaparicchedo",
      "en": "Chapter 1: Consciousness",
      "pt": "Capítulo 1: Consciência",
      "es": "Capítulo 1: Conciencia"
    },
    "section": "Paramattha Dhammas",
    "category": "philosophy",
    "paliTerm": "Catudhā Paramatthato",
    "tags": [
      "paramattha",
      "citta",
      "cetasika",
      "rupa",
      "nibbana"
    ],
    "en": {
      "question": "What are the Four Ultimate Realities (Paramattha Dhammas) in the Abhidhamma?",
      "answer": "1. Citta (Consciousness - 89 or 121)\n2. Cetasika (Mental Factors - 52)\n3. Rūpa (Matter - 28)\n4. Nibbāna (The Unconditioned - 1)",
      "breakdown": [
        "Citta: Knowing the object (vijānana).",
        "Cetasika: Concomitants qualifying awareness.",
        "Rūpa: Material phenomena subject to physical disruption (ruppana).",
        "Nibbāna: Unconditioned peace (asaṅkhata-dhātu)."
      ],
      "explanation": "Citta, cetasika, and rūpa are conditioned (saṅkhata). Nibbāna alone is unconditioned (asaṅkhata).",
      "mnemonicOrExamTip": "Mnemonic: C-C-R-N. Never confuse conventional concept (paññatti) with Paramattha.",
      "examQuestionType": "Fundamental Ontology"
    },
    "pt": {
      "question": "Quais são as Quatro Realidades Últimas (Paramattha Dhammas) no Abhidhamma?",
      "answer": "1. Citta (Consciência - 89 ou 121)\n2. Cetasika (Fatores Mentais - 52)\n3. Rūpa (Matéria - 28)\n4. Nibbāna (O Incondicionado - 1)",
      "breakdown": [
        "Citta: Apreensão do objeto.",
        "Cetasika: Concomitantes mentais que qualificam o citta.",
        "Rūpa: Matéria sujeita a alteração física.",
        "Nibbāna: Elemento incondicionado e cessação do sofrimento."
      ],
      "explanation": "As três primeiras são realidades condicionadas (saṅkhata); Nibbāna é incondicionado (asaṅkhata).",
      "mnemonicOrExamTip": "Dica de Prova: Paññatti (conceito) não é Paramattha Dhamma.",
      "examQuestionType": "Ontologia Fundamental"
    },
    "es": {
      "question": "¿Cuáles son las Cuatro Realidades Últimas (Paramattha Dhammas)?",
      "answer": "1. Citta (Conciencia - 89 o 121)\n2. Cetasika (Factores Mentales - 52)\n3. Rūpa (Materia - 28)\n4. Nibbāna (Lo Incondicionado - 1)",
      "breakdown": [
        "Citta: Aprehensión del objeto.",
        "Cetasika: Factores que acompañan.",
        "Rūpa: Materia física.",
        "Nibbāna: Cesación incondicionada."
      ],
      "explanation": "Citta, cetasika y rūpa son condicionados; Nibbāna es incondicionado.",
      "mnemonicOrExamTip": "Consejo: Paññatti no es una realidad última.",
      "examQuestionType": "Ontología Fundamental"
    }
  },
  {
    "id": "ch1-02",
    "chapter": 1,
    "chapterName": {
      "pali": "Cittaparicchedo",
      "en": "Chapter 1: Consciousness",
      "pt": "Capítulo 1: Consciência",
      "es": "Capítulo 1: Conciencia"
    },
    "section": "Citta Totals & Planes",
    "category": "quantities",
    "paliTerm": "Cittabheda 89 / 121",
    "tags": [
      "totals",
      "planes",
      "kamavacara",
      "rupavacara",
      "arupavacara",
      "lokuttara"
    ],
    "en": {
      "question": "How are the 89 and 121 Cittas classified across the 4 Planes (Bhūmi)?",
      "answer": "Brief: 89 | Detailed: 121\n• Kāmāvacara (Sensuous): 54\n• Rūpāvacara (Fine-Material): 15\n• Arūpāvacara (Immaterial): 12\n• Lokuttara (Supramundane): 8 (brief) or 40 (detailed)",
      "breakdown": [
        "Kāma: 12 Akusala + 18 Ahetuka + 24 Sobhana = 54.",
        "Rūpa: 5 Kusala + 5 Vipāka + 5 Kiriya = 15.",
        "Arūpa: 4 Kusala + 4 Vipāka + 4 Kiriya = 12.",
        "Lokuttara: 4 Magga + 4 Phala = 8 (× 5 Jhānas = 40).",
        "Totals: 54 + 15 + 12 + 8 = 89; 54 + 15 + 12 + 40 = 121."
      ],
      "explanation": "The 81 mundane cittas remain fixed; only the 8 supramundane cittas multiply by 5 jhānas.",
      "mnemonicOrExamTip": "Formula: 89 - 8 + 40 = 121.",
      "examQuestionType": "Quantitative Taxonomy"
    },
    "pt": {
      "question": "Como se distribuem os 89 e 121 Cittas nos 4 Planos (Bhūmi)?",
      "answer": "Breve: 89 | Detalhado: 121\n• Kāmāvacara (Sensorial): 54\n• Rūpāvacara (Forma Sutil): 15\n• Arūpāvacara (Imaterial): 12\n• Lokuttara (Supramundano): 8 (breve) ou 40 (detalhado)",
      "breakdown": [
        "Sensorial: 12 Akusala + 18 Ahetuka + 24 Sobhana = 54.",
        "Forma Sutil: 5 Kusala + 5 Vipāka + 5 Kiriya = 15.",
        "Imaterial: 4 Kusala + 4 Vipāka + 4 Kiriya = 12.",
        "Supramundano: 4 Magga + 4 Phala = 8 (× 5 Jhānas = 40).",
        "Totais: 54 + 15 + 12 + 8 = 89; 54 + 15 + 12 + 40 = 121."
      ],
      "explanation": "Os 81 mundanos são fixos; apenas os 8 supramundanos quintuplicam pelos 5 jhānas.",
      "mnemonicOrExamTip": "Fórmula de Prova: 89 - 8 + 40 = 121.",
      "examQuestionType": "Taxonomia Quantitativa"
    },
    "es": {
      "question": "¿Cómo se distribuyen los 89 y 121 Cittas en los 4 Planos?",
      "answer": "Breve: 89 | Detallado: 121\n• Sensorial: 54\n• Forma Sutil: 15\n• Inmaterial: 12\n• Supramundano: 8 o 40",
      "breakdown": [
        "Sensorial (54) = 12 akusala + 18 ahetuka + 24 sobhana.",
        "Forma Sutil (15) = 5 kusala + 5 vipāka + 5 kiriya.",
        "Inmaterial (12) = 4 kusala + 4 vipāka + 4 kiriya.",
        "Supramundano (8/40) = 4 magga + 4 phala (× 5 jhānas).",
        "Totales: 54 + 15 + 12 + 8 = 89; 54 + 15 + 12 + 40 = 121."
      ],
      "explanation": "81 mundanos fijos; 8 supramundanos se expanden a 40.",
      "mnemonicOrExamTip": "Fórmula: 81 + 40 = 121.",
      "examQuestionType": "Taxonomía Cuantitativa"
    }
  },
  {
    "id": "ch1-03",
    "chapter": 1,
    "chapterName": {
      "pali": "Cittaparicchedo",
      "en": "Chapter 1: Consciousness",
      "pt": "Capítulo 1: Consciência",
      "es": "Capítulo 1: Conciencia"
    },
    "section": "Akusalacitta 12",
    "category": "structures",
    "paliTerm": "Akusalacitta 12",
    "tags": [
      "akusala",
      "lobha",
      "dosa",
      "moha",
      "12"
    ],
    "en": {
      "question": "What are the 12 Akusala Cittas and their roots?",
      "answer": "12 Unwholesome Consciousnesses:\n• 8 Lobhamūla (Rooted in Greed)\n• 2 Dosamūla (Rooted in Hatred/Aversion)\n• 2 Mohamūla (Rooted in Delusion alone)",
      "breakdown": [
        "8 Lobha: 4 joyful (somanassa) + 4 equanimous (upekkhā); half wrong view, half without; half unprompted, half prompted.",
        "2 Dosa: Both displeasure (domanassa) + aversion (paṭigha); 1 unprompted, 1 prompted.",
        "2 Moha: Both equanimous (upekkhā); 1 doubt (vicikicchā), 1 restlessness (uddhacca)."
      ],
      "explanation": "All 12 contain delusion; in the 2 Moha cittas, delusion acts as the solitary root.",
      "mnemonicOrExamTip": "Why no prompted Mohamūla? Delusion is too inert and hesitant to be coaxed.",
      "examQuestionType": "Structural Classification"
    },
    "pt": {
      "question": "Quais são os 12 Akusala Cittas e suas raízes?",
      "answer": "12 Consciências Inábeis:\n• 8 Lobhamūla (Enraizadas no Apego)\n• 2 Dosamūla (Enraizadas na Aversão)\n• 2 Mohamūla (Enraizadas unicamente na Ilusão)",
      "breakdown": [
        "8 Lobha: 4 alegres + 4 neutros; 4 com visão errônea + 4 sem; 4 espontâneos + 4 instigados.",
        "2 Dosa: Ambos com desprazer e aversão; 1 espontâneo, 1 instigado.",
        "2 Moha: Ambos neutros; 1 com dúvida, 1 com inquietação."
      ],
      "explanation": "Todos contêm ilusão (moha); nos 2 últimos, ela opera sem cobiça nem aversão.",
      "mnemonicOrExamTip": "Pegadinha: Não há Mohamūla induzido (sasaṅkhārika) porque a ilusão cega não é influenciável por instigação motora.",
      "examQuestionType": "Classificação Estrutural"
    },
    "es": {
      "question": "¿Cuáles son los 12 Akusala Cittas y sus raíces?",
      "answer": "12 Conciencias Perjudiciales:\n• 8 Lobhamūla (Apego)\n• 2 Dosamūla (Aversión)\n• 2 Mohamūla (Ilusión pura)",
      "breakdown": [
        "8 Lobha: 4 somanassa + 4 upekkhā; 4 con diṭṭhi + 4 sin; 4 asaṅkhārika + 4 sasaṅkhārika.",
        "2 Dosa: Ambos domanassa y paṭigha.",
        "2 Moha: Ambos upekkhā (vicikicchā y uddhacca)."
      ],
      "explanation": "Todos tienen moha; en los 2 últimos es la raíz solitaria.",
      "mnemonicOrExamTip": "Moha carece de variantes sasaṅkhārika por su inercia.",
      "examQuestionType": "Clasificación Estructural"
    }
  },
  {
    "id": "ch1-04",
    "chapter": 1,
    "chapterName": {
      "pali": "Cittaparicchedo",
      "en": "Chapter 1: Consciousness",
      "pt": "Capítulo 1: Consciência",
      "es": "Capítulo 1: Conciencia"
    },
    "section": "Ahetukacitta 18",
    "category": "structures",
    "paliTerm": "Ahetukacittāni 18",
    "tags": [
      "ahetuka",
      "rootless",
      "vipaka",
      "kiriya",
      "18"
    ],
    "en": {
      "question": "Enumerate the 18 Ahetuka Cittas into their 3 groups.",
      "answer": "18 Rootless Consciousnesses:\n1. 7 Akusalavipāka (Unwholesome Resultants)\n2. 8 Kusalavipāka-ahetuka (Wholesome Resultants Rootless)\n3. 3 Ahetuka-kiriya (Rootless Functionals)",
      "breakdown": [
        "7 Akusalavipāka: Eye, ear, nose, tongue (upekkhā), body (DUKKHA), receiving (upekkhā), investigating (upekkhā).",
        "8 Kusalavipāka: Eye, ear, nose, tongue (upekkhā), body (SUKHA), receiving (upekkhā), investigating with joy (somanassa), investigating with upekkhā.",
        "3 Kiriya: Five-door adverting, mind-door adverting, smile of Arahants (hasituppāda)."
      ],
      "explanation": "They lack the 6 ethical roots. Wholesome resultants have 8 cittas because investigating splits into joy (for exceedingly good objects) and neutral.",
      "mnemonicOrExamTip": "Exam Trap: Kāyaviññāṇa is the ONLY sense with bodily pleasure (sukha) or pain (dukkha).",
      "examQuestionType": "Taxonomy & Exceptions"
    },
    "pt": {
      "question": "Enumere os 18 Ahetuka Cittas em seus 3 grupos.",
      "answer": "18 Consciências Sem Raízes:\n1. 7 Akusalavipāka (Resultantes Inábeis)\n2. 8 Kusalavipāka Ahetuka (Resultantes Hábeis)\n3. 3 Ahetuka Kiriya (Funcionais Sem Raiz)",
      "breakdown": [
        "7 Akusalavipāka: Olho, ouvido, nariz, língua (upekkhā), corpo (DUKKHA), recepção (upekkhā), investigação (upekkhā).",
        "8 Kusalavipāka: Olho, ouvido, nariz, língua (upekkhā), corpo (SUKHA), recepção (upekkhā), investigação com alegria (somanassa), investigação neutra (upekkhā).",
        "3 Kiriya: Advertência nas 5 portas, advertência na mente, riso dos Arahants (hasituppāda)."
      ],
      "explanation": "Não possuem nenhuma das 6 raízes. O resultado hábil tem 8 porque a investigação se bifurca em alegre e neutra.",
      "mnemonicOrExamTip": "Pegadinha: Kāyaviññāṇa é o ÚNICO sentido com dor ou prazer físico real.",
      "examQuestionType": "Taxonomia e Exceções"
    },
    "es": {
      "question": "¿Cuáles son los 18 Ahetuka Cittas en sus 3 grupos?",
      "answer": "18 Conciencias sin raíz:\n1. 7 Akusalavipāka (Resultante perjudicial)\n2. 8 Kusalavipāka (Resultante beneficioso)\n3. 3 Ahetuka Kiriya (Funcionales sin raíz)",
      "breakdown": [
        "7 Akusalavipāka: 5 sentidos (cuerpo con DUKKHA), recepción, investigación.",
        "8 Kusalavipāka: 5 sentidos (cuerpo con SUKHA), recepción, 2 investigaciones.",
        "3 Kiriya: Advertencia sentidos, advertencia mente, risa de Arahant."
      ],
      "explanation": "Carecen de raíces hetu. Kusalavipāka tiene 8 por la doble investigación.",
      "mnemonicOrExamTip": "Kāyaviññāṇa es el único con sensación física directa.",
      "examQuestionType": "Taxonomía de Ahetuka"
    }
  },
  {
    "id": "ch1-05",
    "chapter": 1,
    "chapterName": {
      "pali": "Cittaparicchedo",
      "en": "Chapter 1: Consciousness",
      "pt": "Capítulo 1: Consciência",
      "es": "Capítulo 1: Conciencia"
    },
    "section": "Kāmāvacara Sobhana 24",
    "category": "structures",
    "paliTerm": "Kāmāvacara Sobhana 24",
    "tags": [
      "sobhana",
      "mahakusala",
      "mahavipaka",
      "mahakiriya",
      "24"
    ],
    "en": {
      "question": "What are the 24 Sense-Sphere Beautiful Cittas?",
      "answer": "3 identical octets:\n• 8 Mahākusala (Great Wholesome)\n• 8 Mahāvipāka (Great Resultants)\n• 8 Mahākiriya (Great Functionals of Arahants)\nTotal: 24 Cittas.",
      "breakdown": [
        "Each octet has 3 pairs:",
        "1. Feeling: Joy (somanassa - 4) vs Equanimity (upekkhā - 4).",
        "2. Wisdom: Associated with knowledge (ñāṇasampayutta - 4) vs Dissociated (ñāṇavippayutta - 4).",
        "3. Prompt: Unprompted (asaṅkhārika - 4) vs Prompted (sasaṅkhārika - 4)."
      ],
      "explanation": "Mahākusala creates merit; Mahāvipāka functions in rebirth-linking, life-continuum, retention; Mahākiriya is action of Arahants.",
      "mnemonicOrExamTip": "All 3 octets share identical names and factor matrices.",
      "examQuestionType": "Symmetric Taxonomy"
    },
    "pt": {
      "question": "Quais são os 24 Cittas Belos do Plano Sensorial?",
      "answer": "3 octetos idênticos:\n• 8 Mahākusala (Grandes Hábiles)\n• 8 Mahāvipāka (Grandes Resultantes)\n• 8 Mahākiriya (Grandes Funcionais dos Arahants)\nTotal: 24 Cittas.",
      "breakdown": [
        "Cada octeto é formado por 3 pares:",
        "1. Sensação: Somanassa (4) vs Upekkhā (4).",
        "2. Sabedoria: Com sabedoria (ñāṇasampayutta - 4) vs Sem sabedoria (ñāṇavippayutta - 4).",
        "3. Instigação: Espontâneo (asaṅkhārika - 4) vs Induzido (sasaṅkhārika - 4)."
      ],
      "explanation": "Mahākusala gera mérito; Mahāvipāka opera no renascimento e retenção; Mahākiriya é a ação dos Arahants.",
      "mnemonicOrExamTip": "Os 3 octetos são perfeitamente simétricos em seus termos.",
      "examQuestionType": "Taxonomia Simétrica"
    },
    "es": {
      "question": "¿Cuáles son los 24 Cittas Bellos de la Esfera Sensorial?",
      "answer": "3 octetos simétricos:\n• 8 Mahākusala (Beneficiosos)\n• 8 Mahāvipāka (Resultantes)\n• 8 Mahākiriya (Funcionales de Arahants)\nTotal: 24.",
      "breakdown": [
        "Cada octeto está formado por 3 pares:",
        "1. Sensación: Alegría (somanassa - 4) vs Ecuanimidad (upekkhā - 4).",
        "2. Sabiduría: Asociado con conocimiento (ñāṇasampayutta - 4) vs Disociado (ñāṇavippayutta - 4).",
        "3. Instigación: Espontáneo (asaṅkhārika - 4) vs Inducido (sasaṅkhārika - 4)."
      ],
      "explanation": "Estructura idéntica en los 3 grupos.",
      "mnemonicOrExamTip": "Simetría perfecta de 8 × 3.",
      "examQuestionType": "Taxonomía de Sobhana"
    }
  },
  {
    "id": "ch1-06",
    "chapter": 1,
    "chapterName": {
      "pali": "Cittaparicchedo",
      "en": "Chapter 1: Consciousness",
      "pt": "Capítulo 1: Consciência",
      "es": "Capítulo 1: Conciencia"
    },
    "section": "Rūpāvacara 15 & Factors",
    "category": "structures",
    "paliTerm": "Rūpāvacaracitta 15",
    "tags": [
      "rupavacara",
      "jhana",
      "factors",
      "vitakka",
      "vicara",
      "15"
    ],
    "en": {
      "question": "What are the 15 Rūpāvacara Cittas and the factors of the 5 Jhānas?",
      "answer": "15 Cittas = 5 Kusala + 5 Vipāka + 5 Kiriya corresponding to the 5 Jhānas.\nFactors:\n• 1st: Vitakka, Vicāra, Pīti, Sukha, Ekaggatā (5 factors)\n• 2nd: Vicāra, Pīti, Sukha, Ekaggatā (4 factors - vitakka dropped)\n• 3rd: Pīti, Sukha, Ekaggatā (3 factors - vicāra dropped)\n• 4th: Sukha, Ekaggatā (2 factors - pīti dropped)\n• 5th: Upekkhā, Ekaggatā (2 factors - sukha replaced by upekkhā)",
      "breakdown": [
        "Abhidhamma uses the 5-fold Jhāna system (pañcakanaya).",
        "Suttas use a 4-fold system where vitakka and vicāra drop together."
      ],
      "explanation": "Progressive abandonment of coarser factors leaves concentration deeply tranquil.",
      "mnemonicOrExamTip": "Exam Trap: In Abhidhamma, always calculate 5 Jhānas, not 4.",
      "examQuestionType": "Jhāna Factors & Taxonomy"
    },
    "pt": {
      "question": "Quais são os 15 Rūpāvacara Cittas e os fatores dos 5 Jhānas?",
      "answer": "15 Cittas = 5 Kusala + 5 Vipāka + 5 Kiriya correspondentes aos 5 Jhānas.\nFatores:\n• 1º: Vitakka, Vicāra, Pīti, Sukha, Ekaggatā (5 fatores)\n• 2º: Vicāra, Pīti, Sukha, Ekaggatā (4 fatores - vitakka descartado)\n• 3º: Pīti, Sukha, Ekaggatā (3 fatores - vicāra descartado)\n• 4º: Sukha, Ekaggatā (2 fatores - pīti descartada)\n• 5º: Upekkhā, Ekaggatā (2 fatores - sukha substituído por upekkhā)",
      "breakdown": [
        "Abhidhamma adota o esquema quíntuplo de Jhānas (pañcakanaya).",
        "Os Suttas adotam o esquema quádruplo."
      ],
      "explanation": "Abandono progressivo dos fatores mais agitados em prol da paz concentrada.",
      "mnemonicOrExamTip": "Dica: O Abhidhamma utiliza 5 Jhānas (5 × 3 = 15).",
      "examQuestionType": "Fatores de Absorção"
    },
    "es": {
      "question": "¿Cuáles son los 15 Rūpāvacara Cittas y los factores de los 5 Jhānas?",
      "answer": "15 = 5 Kusala + 5 Vipāka + 5 Kiriya.\nFactores: 1º (5), 2º (4), 3º (3), 4º (2 con sukha), 5º (2 con upekkhā).",
      "breakdown": [
        "Abhidhamma usa 5 niveles de Jhāna.",
        "Abandono progresivo de factores."
      ],
      "explanation": "Base de concentración de la forma sutil.",
      "mnemonicOrExamTip": "Siempre usar el esquema de 5 Jhānas.",
      "examQuestionType": "Factores de Jhāna"
    }
  },
  {
    "id": "ch1-07",
    "chapter": 1,
    "chapterName": {
      "pali": "Cittaparicchedo",
      "en": "Chapter 1: Consciousness",
      "pt": "Capítulo 1: Consciência",
      "es": "Capítulo 1: Conciencia"
    },
    "section": "Arūpāvacara 12",
    "category": "structures",
    "paliTerm": "Arūpāvacaracitta 12",
    "tags": [
      "arupavacara",
      "immaterial",
      "infinite space",
      "nothingness",
      "12"
    ],
    "en": {
      "question": "What are the 12 Arūpāvacara Cittas and their factors?",
      "answer": "12 Cittas = 4 Realms × 3 Modes (Kusala, Vipāka, Kiriya).\nRealms:\n1. Ākāsānañcāyatana (Infinite Space)\n2. Viññāṇañcāyatana (Infinite Consciousness)\n3. Ākiñcaññāyatana (Nothingness)\n4. Nevasaññānāsaññāyatana (Neither-Perception-Nor-Non-Perception)\nAll 12 have 5th Jhāna factors: Upekkhā + Ekaggatā.",
      "breakdown": [
        "They do not discard factors; their progression is purely in the subtlety of their meditation objects.",
        "Objects alternate: Concept -> Citta -> Concept -> Citta."
      ],
      "explanation": "Immaterial states transcend all fine-material imagery.",
      "mnemonicOrExamTip": "All 12 Arūpa cittas belong to the 5th Jhāna category.",
      "examQuestionType": "Immaterial Realms"
    },
    "pt": {
      "question": "Quais são os 12 Arūpāvacara Cittas e seus fatores?",
      "answer": "12 Cittas = 4 Esferas × 3 Modos (Kusala, Vipāka, Kiriya).\nEsferas:\n1. Ākāsānañcāyatana (Espaço Infinito)\n2. Viññāṇañcāyatana (Consciência Infinita)\n3. Ākiñcaññāyatana (Nada / Não-existência)\n4. Nevasaññānāsaññāyatana (Nem-Percepção-Nem-Não-Percepção)\nTodos possuem fatores de 5º Jhāna: Upekkhā + Ekaggatā.",
      "breakdown": [
        "Não descartam fatores; a progressão dá-se pela sutileza do objeto.",
        "Objetos alternam: Conceito -> Citta -> Conceito -> Citta."
      ],
      "explanation": "Superação total de imagens materiais.",
      "mnemonicOrExamTip": "Pergunta de Prova: Todos pertencem ao nível do 5º Jhāna.",
      "examQuestionType": "Esferas Imateriais"
    },
    "es": {
      "question": "¿Cuáles son los 12 Arūpāvacara Cittas y sus factores?",
      "answer": "12 Cittas = 4 Esferas × 3 Modos.\n1. Espacio, 2. Conciencia, 3. Nada, 4. Ni-percepción.\nTodos tienen factores de 5º Jhāna: Upekkhā + Ekaggatā.",
      "breakdown": [
        "Difieren por el objeto, no por factores.",
        "Pertenecen al 5º Jhāna."
      ],
      "explanation": "Trascendencia de la materia.",
      "mnemonicOrExamTip": "Todos corresponden al 5º Jhāna.",
      "examQuestionType": "Cittas Inmateriales"
    }
  },
  {
    "id": "ch1-08",
    "chapter": 1,
    "chapterName": {
      "pali": "Cittaparicchedo",
      "en": "Chapter 1: Consciousness",
      "pt": "Capítulo 1: Consciência",
      "es": "Capítulo 1: Conciencia"
    },
    "section": "Lokuttara 8 to 40",
    "category": "quantities",
    "paliTerm": "Lokuttara 8 / 40",
    "tags": [
      "lokuttara",
      "magga",
      "phala",
      "8",
      "40"
    ],
    "en": {
      "question": "How do the 8 Supramundane Cittas expand to 40?",
      "answer": "Brief: 8 (4 Magga + 4 Phala)\nDetailed: 40 (8 × 5 Jhānas)\n• 20 Maggacittas (4 Paths × 5 Jhānas)\n• 20 Phalacittas (4 Fruits × 5 Jhānas)",
      "breakdown": [
        "Sotāpatti, Sakadāgāmī, Anāgāmī, Arahatta each multiply by 5 jhāna factor levels.",
        "Total cittas: 81 mundane + 40 supramundane = 121."
      ],
      "explanation": "The path consciousness adopts the factors of the jhāna used as foundation for insight.",
      "mnemonicOrExamTip": "Kusala total: 21 or 37. Vipāka total: 36 or 52.",
      "examQuestionType": "Mathematical Expansion"
    },
    "pt": {
      "question": "Como os 8 Cittas Supramundanos se expandem para 40?",
      "answer": "Breve: 8 (4 Magga + 4 Phala)\nDetalhado: 40 (8 × 5 Jhānas)\n• 20 Maggacittas (4 Caminhos × 5 Jhānas)\n• 20 Phalacittas (4 Frutos × 5 Jhānas)",
      "breakdown": [
        "Sotāpatti, Sakadāgāmī, Anāgāmī, Arahatta multiplicam-se pelos 5 jhānas.",
        "Total: 81 mundanos + 40 supramundanos = 121."
      ],
      "explanation": "O caminho manifesta os fatores do jhāna utilizado como base meditativa.",
      "mnemonicOrExamTip": "Total Kusala: 21 ou 37. Total Vipāka: 36 ou 52.",
      "examQuestionType": "Expansão Matemática"
    },
    "es": {
      "question": "¿Cómo se expanden los 8 Lokuttara a 40?",
      "answer": "Breve: 8 | Detallado: 40 (8 × 5 Jhānas = 40).\n20 Maggas + 20 Phalas.",
      "breakdown": [
        "Sotāpatti, Sakadāgāmī, Anāgāmī y Arahatta se multiplican por los 5 niveles de jhāna.",
        "Total de cittas: 81 mundanos + 40 supramundanos = 121."
      ],
      "explanation": "Adoptan los factores del jhāna base de discernimiento.",
      "mnemonicOrExamTip": "Total Kusala: 21/37; Vipāka: 36/52.",
      "examQuestionType": "Expansión Supramundana"
    }
  },
  {
    "id": "ch1-09",
    "chapter": 1,
    "chapterName": {
      "pali": "Cittaparicchedo",
      "en": "Chapter 1: Consciousness",
      "pt": "Capítulo 1: Consciência",
      "es": "Capítulo 1: Conciencia"
    },
    "section": "Feeling Classification",
    "category": "quantities",
    "paliTerm": "Vedanābheda 121",
    "tags": [
      "vedana",
      "feelings",
      "somanassa",
      "upekkhā",
      "domanassa"
    ],
    "en": {
      "question": "How are the 121 Cittas classified according to Feeling (Vedanā)?",
      "answer": "5 Feelings in 121 Cittas:\n• Somanassa (Mental Joy): 62\n• Domanassa (Mental Displeasure): 2 (the 2 dosamūlacittas)\n• Sukha (Bodily Pleasure): 1 (kusalavipāka kāyaviññāṇa)\n• Dukkha (Bodily Pain): 1 (akusalavipāka kāyaviññāṇa)\n• Upekkhā (Equanimity / Neutral): 55\nTotal: 62 + 2 + 1 + 1 + 55 = 121.",
      "breakdown": [
        "Somanassa (62): 4 lobha + 1 santīraṇa + 1 hasituppāda + 12 kāma-sobhana + 12 rūpāvacara (1st–4th jhānas × 3 classes: kusala, vipāka, kiriya) + 32 lokuttara (1st–4th jhānas × 8).",
        "Domanassa (2): ONLY the 2 dosamūlacittas.",
        "Sukha (1) and Dukkha (1): ONLY in the 2 bodily consciousnesses (kāyaviññāṇa)."
      ],
      "explanation": "Notice the predominance of equanimity (55) and joy (62) in the mind's landscape.",
      "mnemonicOrExamTip": "Exam Question: Which cittas have domanassa? EXACTLY 2 (dosamūlacittas).",
      "examQuestionType": "Feeling Matrix"
    },
    "pt": {
      "question": "Como se distribuem os 121 Cittas segundo a Sensação (Vedanā)?",
      "answer": "5 Sensações nos 121 Cittas:\n• Somanassa (Alegria mental): 62\n• Domanassa (Desprazer mental): 2 (os 2 dosamūlacittas)\n• Sukha (Prazer corporal): 1 (kusalavipāka kāyaviññāṇa)\n• Dukkha (Dor corporal): 1 (akusalavipāka kāyaviññāṇa)\n• Upekkhā (Equanimidade/Neutra): 55\nTotal: 62 + 2 + 1 + 1 + 55 = 121.",
      "breakdown": [
        "Somanassa (62): 4 lobha + 1 santīraṇa + 1 hasituppāda + 12 kāma-sobhana + 12 rūpāvacara (1º ao 4º jhānas × 3 classes: kusala, vipāka, kiriya) + 32 lokuttara (1º ao 4º jhānas × 8).",
        "Domanassa (2): APENAS nos 2 dosamūlacittas.",
        "Sukha (1) e Dukkha (1) corporais: APENAS nas 2 consciências do tato (kāyaviññāṇa)."
      ],
      "explanation": "Destaque para a predominância de upekkhā (55) e somanassa (62).",
      "mnemonicOrExamTip": "Dica: Domanassa existe em apenas 2 cittas.",
      "examQuestionType": "Distribuição das Sensações"
    },
    "es": {
      "question": "¿Cómo se clasifican los 121 Cittas por Sensación (Vedanā)?",
      "answer": "5 Sensaciones en los 121 Cittas:\n• Somanassa (Alegría mental): 62\n• Domanassa (Displacer mental): 2 (los 2 dosamūlacittas)\n• Sukha (Placer corporal): 1 (kusalavipāka kāyaviññāṇa)\n• Dukkha (Dolor corporal): 1 (akusalavipāka kāyaviññāṇa)\n• Upekkhā (Ecuanimidad/Neutra): 55\nTotal: 62 + 2 + 1 + 1 + 55 = 121.",
      "breakdown": [
        "Somanassa (62): 4 lobha + 1 santīraṇa + 1 hasituppāda + 12 kāma-sobhana + 12 rūpāvacara (1º al 4º jhānas × 3 clases) + 32 lokuttara (1º al 4º jhānas × 8).",
        "Domanassa exclusiva de los 2 dosamūlacittas.",
        "Sukha y Dukkha exclusivos de las 2 conciencias táctiles."
      ],
      "explanation": "Predominio de alegría (62) y ecuanimidad (55).",
      "mnemonicOrExamTip": "Domanassa solo en 2 cittas.",
      "examQuestionType": "Distribución de Vedanā"
    }
  },
  {
    "id": "ch1-10",
    "chapter": 1,
    "chapterName": {
      "pali": "Cittaparicchedo",
      "en": "Chapter 1: Consciousness",
      "pt": "Capítulo 1: Consciência",
      "es": "Capítulo 1: Conciencia"
    },
    "section": "Root Classification",
    "category": "quantities",
    "paliTerm": "Hetubheda 121",
    "tags": [
      "hetu",
      "roots",
      "ahetuka",
      "dvihetuka",
      "tihetuka"
    ],
    "en": {
      "question": "How are Cittas classified by Root (Hetubheda)?",
      "answer": "• Ahetuka (Rootless): 18\n• Ekahetuka (1 Root): 2 (the 2 mohamūlacittas - moha alone)\n• Dvihetuka (2 Roots): 22 (8 lobha, 2 dosa, 12 ñāṇavippayutta sobhana)\n• Tihetuka (3 Roots): 47 (brief) or 79 (detailed) (12 ñāṇasampayutta sobhana + 15 rūpa + 12 arūpa + 8/40 lokuttara)",
      "breakdown": [
        "Calculation: 18 + 2 + 22 + 47 = 89; or 18 + 2 + 22 + 79 = 121.",
        "Tihetuka cittas possess non-greed, non-hatred, and wisdom (alobha, adosa, amoha)."
      ],
      "explanation": "Only tihetuka rebirth can achieve Jhāna or Enlightenment in that life.",
      "mnemonicOrExamTip": "Formula: 18 + 2 + 22 + 47/79 = 89/121.",
      "examQuestionType": "Root Distribution"
    },
    "pt": {
      "question": "Como se classificam os Cittas quanto às Raízes (Hetubheda)?",
      "answer": "• Ahetuka (Sem raízes): 18\n• Ekahetuka (1 raiz): 2 (os 2 mohamūlacittas - apenas moha)\n• Dvihetuka (2 raízes): 22 (8 lobha, 2 dosa, 12 sobhanas sem sabedoria)\n• Tihetuka (3 raízes): 47 (breve) ou 79 (detalhado) (12 sobhanas com sabedoria + 15 rūpa + 12 arūpa + 8/40 lokuttara)",
      "breakdown": [
        "Cálculo: 18 + 2 + 22 + 47 = 89; ou 18 + 2 + 22 + 79 = 121.",
        "Cittas tihetuka possuem alobha, adosa e amoha."
      ],
      "explanation": "Apenas o renascimento tihetuka pode alcançar Jhāna ou Despertar naquela vida.",
      "mnemonicOrExamTip": "Fórmula de Prova: 18 + 2 + 22 + 47/79.",
      "examQuestionType": "Classificação por Raízes"
    },
    "es": {
      "question": "¿Cómo se clasifican los Cittas por Raíz (Hetubheda)?",
      "answer": "• Ahetuka (0 raíces): 18\n• Ekahetuka (1 raíz): 2 (los 2 momūhacittas solo tienen moha)\n• Dvihetuka (2 raíces): 22 (8 lobha + 2 dosa + 12 kāma-sobhana sin conocimiento)\n• Tihetuka (3 raíces): 47 (breve) o 79 (detallado) (12 kāma-sobhana con conocimiento + 15 rūpa + 12 arūpa + 8 o 40 lokuttara)",
      "breakdown": [
        "Cálculo: 18 + 2 + 22 + 47 = 89; o 18 + 2 + 22 + 79 = 121.",
        "Los cittas tihetuka poseen no-codicia, no-aversión y sabiduría (alobha, adosa, amoha)."
      ],
      "explanation": "Distribución de alobha, adosa, amoha.",
      "mnemonicOrExamTip": "Ahetuka (18), Eka (2), Dvi (22), Ti (47/79).",
      "examQuestionType": "Clasificación por Hetu"
    }
  },
  {
    "id": "ch2-01",
    "chapter": 2,
    "chapterName": {
      "pali": "Cetasikaparicchedo",
      "en": "Chapter 2: Mental Factors",
      "pt": "Capítulo 2: Fatores Mentais",
      "es": "Capítulo 2: Factores Mentales"
    },
    "section": "Cetasika Definition",
    "category": "philosophy",
    "paliTerm": "Cetasika Lakkhaṇacatukka",
    "tags": [
      "cetasika",
      "characteristics",
      "ekuppada",
      "association"
    ],
    "en": {
      "question": "What are the 4 characteristics of association of Cetasikas?",
      "answer": "1. Ekuppāda (Arise together with citta)\n2. Ekanirodha (Cease together with citta)\n3. Ekālambaṇa (Share the exact same object)\n4. Ekavatthuka (Share the exact same physical base)",
      "breakdown": [
        "Simultaneous in arising and dissolution.",
        "Identity of cognitive object and physical support."
      ],
      "explanation": "Citta and cetasikas are functionally inseparable in cognition.",
      "mnemonicOrExamTip": "Memorize the 4 'Eka' prefixes.",
      "examQuestionType": "Essential Marks of Association"
    },
    "pt": {
      "question": "Quais são as 4 características de associação dos Cetasikas?",
      "answer": "1. Ekuppāda (Surgir junto com o citta)\n2. Ekanirodha (Cessar junto com o citta)\n3. Ekālambaṇa (Ter o mesmo objeto)\n4. Ekavatthuka (Compartilhar a mesma base física)",
      "breakdown": [
        "Simultaneidade em nascimento e dissolução.",
        "Identidade de objeto e suporte físico."
      ],
      "explanation": "A mente e os fatores mentais formam uma unidade funcional indissolúvel.",
      "mnemonicOrExamTip": "Decore os 4 prefixos 'Eka-'.",
      "examQuestionType": "Marcas Essenciais de Associação"
    },
    "es": {
      "question": "¿Cuáles son las 4 características de asociación de los Cetasikas?",
      "answer": "1. Ekuppāda (Surgen juntos)\n2. Ekanirodha (Cesan juntos)\n3. Ekālambaṇa (Mismo objeto)\n4. Ekavatthuka (Misma base física)",
      "breakdown": [
        "Simultaneidad en surgimiento y disolución.",
        "Identidad de objeto cognitivo y soporte físico."
      ],
      "explanation": "Inseparables en la cognición.",
      "mnemonicOrExamTip": "Los 4 términos 'Eka-'.",
      "examQuestionType": "Asociación de Cetasikas"
    }
  },
  {
    "id": "ch2-02",
    "chapter": 2,
    "chapterName": {
      "pali": "Cetasikaparicchedo",
      "en": "Chapter 2: Mental Factors",
      "pt": "Capítulo 2: Fatores Mentais",
      "es": "Capítulo 2: Factores Mentales"
    },
    "section": "52 Cetasikas Total",
    "category": "quantities",
    "paliTerm": "Cetasikāni 52",
    "tags": [
      "cetasika",
      "52",
      "annasamana",
      "akusala",
      "sobhana"
    ],
    "en": {
      "question": "What is the total count of 52 Cetasikas by group?",
      "answer": "• Aññasamāna (Ethically Variable): 13 (7 Universals + 6 Occasionals)\n• Akusalacetasika (Unwholesome): 14\n• Sobhanacetasika (Beautiful): 25\nTotal: 13 + 14 + 25 = 52.",
      "breakdown": [
        "Aññasamāna take on the ethical tone of the host citta.",
        "Akusala arise only in unwholesome states.",
        "Sobhana arise only in beautiful states."
      ],
      "explanation": "Subdivisions: (7+6) + (4+3+4+2+1) + (19+3+2+1) = 52.",
      "mnemonicOrExamTip": "Formula: 13 + 14 + 25 = 52.",
      "examQuestionType": "Quantitative Taxonomy"
    },
    "pt": {
      "question": "Qual a divisão geral dos 52 Cetasikas?",
      "answer": "• Aññasamāna (Eticamente Variáveis): 13 (7 Universais + 6 Ocasionais)\n• Akusalacetasika (Inábeis): 14\n• Sobhanacetasika (Belos): 25\nTotal: 13 + 14 + 25 = 52.",
      "breakdown": [
        "Variáveis adaptam-se à qualidade moral do citta.",
        "Inábeis surgem apenas em estados prejudiciais.",
        "Belos surgem apenas em estados virtuosos."
      ],
      "explanation": "Subdivisão: (7+6) + (4+3+4+2+1) + (19+3+2+1) = 52.",
      "mnemonicOrExamTip": "Fórmula: 13 + 14 + 25 = 52.",
      "examQuestionType": "Taxonomia Quantitativa"
    },
    "es": {
      "question": "¿Cómo se dividen los 52 Cetasikas?",
      "answer": "• Variables éticos: 13 (7 Universales + 6 Ocasionales)\n• Perjudiciales: 14\n• Bellos: 25\nTotal: 52.",
      "breakdown": [
        "Aññasamāna adoptan la cualidad ética del citta anfitrión.",
        "Akusala surgen únicamente en estados perjudiciales.",
        "Sobhana surgen únicamente en estados bellos."
      ],
      "explanation": "Clasificación categórica fija.",
      "mnemonicOrExamTip": "Fórmula: 13 + 14 + 25 = 52.",
      "examQuestionType": "Recuento de Factores"
    }
  },
  {
    "id": "ch2-03",
    "chapter": 2,
    "chapterName": {
      "pali": "Cetasikaparicchedo",
      "en": "Chapter 2: Mental Factors",
      "pt": "Capítulo 2: Fatores Mentais",
      "es": "Capítulo 2: Factores Mentales"
    },
    "section": "7 Sabbacittasādhāraṇa",
    "category": "structures",
    "paliTerm": "Sabbacittasādhāraṇa 7",
    "tags": [
      "sabbacitta",
      "phassa",
      "vedana",
      "sanna",
      "cetana",
      "7"
    ],
    "en": {
      "question": "List the 7 Universal Mental Factors (Sabbacittasādhāraṇa).",
      "answer": "1. Phassa (Contact)\n2. Vedanā (Feeling)\n3. Saññā (Perception)\n4. Cetanā (Volition)\n5. Ekaggatā (One-pointedness)\n6. Jīvitindriya (Psychic Life Faculty)\n7. Manasikāra (Attention)",
      "breakdown": [
        "Present in all 89/121 cittas.",
        "They are the ONLY cetasikas in Dvipañcaviññāṇa (10 senses)."
      ],
      "explanation": "Minimum required cognitive bundle for any consciousness to function.",
      "mnemonicOrExamTip": "Minimum cetasikas in a citta: Exactly 7.",
      "examQuestionType": "Universals Catalog"
    },
    "pt": {
      "question": "Liste os 7 Fatores Mentais Universais (Sabbacittasādhāraṇa).",
      "answer": "1. Phassa (Contato)\n2. Vedanā (Sensação)\n3. Saññā (Percepção)\n4. Cetanā (Volicão)\n5. Ekaggatā (Concentração/Unificação)\n6. Jīvitindriya (Vida psíquica)\n7. Manasikāra (Atenção)",
      "breakdown": [
        "Presentes em todos os 89/121 cittas.",
        "São os ÚNICOS presentes nos 10 sentidos básicos."
      ],
      "explanation": "Estrutura mínima indispensável para o ato de conhecer.",
      "mnemonicOrExamTip": "Mínimo de fatores num citta: Exatamente 7.",
      "examQuestionType": "Catálogo dos Universais"
    },
    "es": {
      "question": "¿Cuáles son los 7 Factores Universales (Sabbacittasādhāraṇa)?",
      "answer": "1. Phassa, 2. Vedanā, 3. Saññā, 4. Cetanā, 5. Ekaggatā, 6. Jīvitindriya, 7. Manasikāra.",
      "breakdown": [
        "En todos los 89/121 cittas.",
        "Únicos en las 10 conciencias sensoriales."
      ],
      "explanation": "Requisitos indispensables del conocimiento.",
      "mnemonicOrExamTip": "Mínimo de cetasikas: 7.",
      "examQuestionType": "Universales Mentales"
    }
  },
  {
    "id": "ch2-04",
    "chapter": 2,
    "chapterName": {
      "pali": "Cetasikaparicchedo",
      "en": "Chapter 2: Mental Factors",
      "pt": "Capítulo 2: Fatores Mentais",
      "es": "Capítulo 2: Factores Mentales"
    },
    "section": "6 Pakiṇṇaka Factors",
    "category": "structures",
    "paliTerm": "Pakiṇṇaka 6",
    "tags": [
      "pakinnaka",
      "vitakka",
      "vicara",
      "viriya",
      "piti",
      "chanda"
    ],
    "en": {
      "question": "What are the 6 Occasionals and their key restrictions?",
      "answer": "1. Vitakka (Applied thought - absent in senses & 2nd-5th jhānas)\n2. Vicāra (Sustained thought - absent in senses & 3rd-5th jhānas)\n3. Adhimokkha (Decision - absent in senses & doubt)\n4. Vīriya (Energy - absent in senses & 5 passive ahetukas)\n5. Pīti (Rapture - only in joy/somanassa)\n6. Chanda (Zeal/Desire-to-act - absent in ahetuka & moha)",
      "breakdown": [
        "Unlike universals, they arise selectively.",
        "Ethically variable."
      ],
      "explanation": "Do not confuse Chanda (ethical zeal) with Lobha (unwholesome greed).",
      "mnemonicOrExamTip": "Chanda is neutral; Lobha is always unwholesome.",
      "examQuestionType": "Occasionals & Restrictions"
    },
    "pt": {
      "question": "Quais são os 6 Ocasionais e suas principais restrições?",
      "answer": "1. Vitakka (Pensamento aplicado - ausente nos sentidos e 2º-5º jhānas)\n2. Vicāra (Pensamento sustentado - ausente nos sentidos e 3º-5º jhānas)\n3. Adhimokkha (Decisão - ausente nos sentidos e na dúvida)\n4. Vīriya (Energia - ausente nos sentidos e 5 ahetukas passivos)\n5. Pīti (Êxtase - apenas com alegria/somanassa)\n6. Chanda (Zelo/Vontade - ausente em ahetuka e moha)",
      "breakdown": [
        "Surgem seletivamente.",
        "Eticamente variáveis."
      ],
      "explanation": "Nunca confunda Chanda (vontade neutra) com Lobha (cobiça inábil).",
      "mnemonicOrExamTip": "Chanda pode ser virtuoso; Lobha é sempre inábil.",
      "examQuestionType": "Ocasionais e Restrições"
    },
    "es": {
      "question": "¿Cuáles son los 6 Ocasionales y sus restricciones?",
      "answer": "1. Vitakka, 2. Vicāra, 3. Adhimokkha, 4. Vīriya, 5. Pīti, 6. Chanda.",
      "breakdown": [
        "Pīti solo con alegría.",
        "Adhimokkha ausente en la duda."
      ],
      "explanation": "Chanda es neutro; Lobha es perjudicial.",
      "mnemonicOrExamTip": "Chanda ≠ Lobha.",
      "examQuestionType": "Factores Ocasionales"
    }
  },
  {
    "id": "ch2-05",
    "chapter": 2,
    "chapterName": {
      "pali": "Cetasikaparicchedo",
      "en": "Chapter 2: Mental Factors",
      "pt": "Capítulo 2: Fatores Mentais",
      "es": "Capítulo 2: Factores Mentales"
    },
    "section": "14 Akusala Cetasikas",
    "category": "structures",
    "paliTerm": "Akusala 14",
    "tags": [
      "akusala",
      "ditthi",
      "mana",
      "dosa",
      "thina",
      "middha"
    ],
    "en": {
      "question": "List the 14 Akusala Cetasikas and their exclusivity rules.",
      "answer": "• 4 Moha: Moha, Ahirika, Anottappa, Uddhacca\n• 3 Lobha: Lobha, Diṭṭhi, Māna\n• 4 Dosa: Dosa, Issā, Macchariya, Kukkucca\n• 2 Torpor: Thīna, Middha\n• 1 Doubt: Vicikicchā\nRules:\n1. Diṭṭhi & Māna NEVER arise together.\n2. Issā, Macchariya, Kukkucca arise only in Dosa cittas, individually.\n3. Thīna-Middha arise only in 5 prompted (sasaṅkhārika) cittas.",
      "breakdown": [
        "4 Moha factors accompany all 12 akusala cittas.",
        "Vicikicchā in only 1 citta."
      ],
      "explanation": "Diṭṭhi (dogma) and Māna (conceit) represent opposing ego orientations.",
      "mnemonicOrExamTip": "Diṭṭhi and Māna are strictly mutually exclusive.",
      "examQuestionType": "Exclusivity Rules"
    },
    "pt": {
      "question": "Liste os 14 Akusala Cetasikas e suas regras de exclusão.",
      "answer": "• 4 Moha: Moha, Ahirika, Anottappa, Uddhacca\n• 3 Lobha: Lobha, Diṭṭhi, Māna\n• 4 Dosa: Dosa, Issā, Macchariya, Kukkucca\n• 2 Torpor: Thīna, Middha\n• 1 Dúvida: Vicikicchā\nRegras:\n1. Diṭṭhi e Māna NUNCA surgem juntos.\n2. Inveja, avareza e remorso surgem apenas nos 2 Dosa cittas, separadamente.\n3. Thīna-Middha surgem apenas nos 5 cittas induzidos (sasaṅkhārika).",
      "breakdown": [
        "4 fatores de Moha estão em todos os 12 inábeis.",
        "Vicikicchā em apenas 1 citta."
      ],
      "explanation": "Diṭṭhi e Māna são incompatíveis no mesmo instante.",
      "mnemonicOrExamTip": "Diṭṭhi e Māna são mutuamente exclusivos.",
      "examQuestionType": "Regras de Exclusão Mútua"
    },
    "es": {
      "question": "¿Cuáles son los 14 Akusala Cetasikas y sus incompatibilidades?",
      "answer": "4 Moha + 3 Lobha (lobha, diṭṭhi, māna) + 4 Dosa + 2 Torpor + 1 Vicikicchā.\n• Diṭṭhi y Māna nunca coexisten.\n• Issā, macchariya y kukkucca solo en Dosa.\n• Thīna-middha solo en 5 inducidos.",
      "breakdown": [
        "Los 4 factores de Moha acompañan a todos los 12 akusala cittas.",
        "Vicikicchā surge únicamente en 1 citta."
      ],
      "explanation": "Incompatibilidad de diṭṭhi y māna.",
      "mnemonicOrExamTip": "Diṭṭhi y Māna son mutuamente excluyentes.",
      "examQuestionType": "Incompatibilidades de Akusala"
    }
  },
  {
    "id": "ch2-06",
    "chapter": 2,
    "chapterName": {
      "pali": "Cetasikaparicchedo",
      "en": "Chapter 2: Mental Factors",
      "pt": "Capítulo 2: Fatores Mentais",
      "es": "Capítulo 2: Factores Mentales"
    },
    "section": "25 Sobhana & Virati",
    "category": "structures",
    "paliTerm": "Sobhana 25 & Virati",
    "tags": [
      "sobhana",
      "virati",
      "appamanna",
      "panna",
      "25"
    ],
    "en": {
      "question": "What are the 25 Sobhana Cetasikas and how do Viratis behave?",
      "answer": "• 19 Sobhana-sādhāraṇa (Beautiful Universals)\n• 3 Virati (Abstinences: Right Speech, Action, Livelihood)\n• 2 Appamaññā (Compassion, Sympathetic Joy)\n• 1 Paññindriya (Wisdom)\nVirati Rule: In mundane kusala, they arise separately and conditionally; in Lokuttara, they arise SIMULTANEOUSLY and INVARIABLY.",
      "breakdown": [
        "Appamaññā take living beings as object; cannot arise in Lokuttara (object is Nibbāna).",
        "Paññā arises in 47 or 79 tihetuka cittas."
      ],
      "explanation": "Supramundane path cuts all bodily/verbal misconduct simultaneously.",
      "mnemonicOrExamTip": "Appamaññā cannot enter Lokuttara due to object incompatibility.",
      "examQuestionType": "Beautiful Factor Dynamics"
    },
    "pt": {
      "question": "Quais são os 25 Sobhana Cetasikas e como as Viratis operam?",
      "answer": "• 19 Universais Belos\n• 3 Virati (Palavra, Ação e Modo de Vida Corretos)\n• 2 Appamaññā (Compaixão e Alegria Altruísta)\n• 1 Paññindriya (Sabedoria)\nRegra das Viratis: No mundo sensorial surgem separadas e condicionais; no Lokuttara surgem SIMULTÂNEAS e INFALÍVEIS.",
      "breakdown": [
        "Appamaññā têm seres como objeto; não entram no Lokuttara (objeto é Nibbāna).",
        "Paññā surge nos 47/79 cittas tihetuka."
      ],
      "explanation": "No caminho nobre a abstenção é una e integral.",
      "mnemonicOrExamTip": "Karuṇā e Muditā nunca entram no Lokuttara.",
      "examQuestionType": "Dinâmica dos Fatores Belos"
    },
    "es": {
      "question": "¿Cuáles son los 25 Sobhana Cetasikas y la regla de las Virati?",
      "answer": "19 Universales bellos + 3 Virati + 2 Appamaññā + 1 Paññindriya.\nVirati: En lo mundano surgen por separado; en Lokuttara surgen SIMULTÁNEAMENTE.",
      "breakdown": [
        "Appamaññā toman a los seres vivos como objeto; no entran en Lokuttara (cuyo objeto es Nibbāna).",
        "Paññā surge en los 47 o 79 cittas tihetuka."
      ],
      "explanation": "Purificación simultánea en el despertar.",
      "mnemonicOrExamTip": "Virati simultáneas en Lokuttara.",
      "examQuestionType": "Dinámica de Sobhana"
    }
  },
  {
    "id": "ch2-07",
    "chapter": 2,
    "chapterName": {
      "pali": "Cetasikaparicchedo",
      "en": "Chapter 2: Mental Factors",
      "pt": "Capítulo 2: Fatores Mentais",
      "es": "Capítulo 2: Factores Mentales"
    },
    "section": "Saṅgahanaya Math",
    "category": "structures",
    "paliTerm": "Saṅgahanaya Counts",
    "tags": [
      "sanganahaya",
      "19",
      "15",
      "36",
      "combinations"
    ],
    "en": {
      "question": "Calculate Cetasikas in: (1) 1st Lobha, (2) Vicikicchā, (3) Lokuttara 1st Jhāna.",
      "answer": "(1) 1st Lobha: 19 (13 aññasamāna + 4 moha + lobha + diṭṭhi)\n(2) Vicikicchā: 15 (7 universals + 3 occasionals [vitakka, vicāra, vīriya] + 4 moha + vicikicchā)\n(3) Lokuttara 1st Jhāna: 36 (13 aññasamāna + 19 sobhana universals + 3 virati + paññā)",
      "breakdown": [
        "Vicikicchā has no adhimokkha (decision), pīti, or chanda.",
        "Lokuttara 1st Jhāna has no Appamaññā."
      ],
      "explanation": "Saṅgahanaya is the combination calculus of Buddhist psychology.",
      "mnemonicOrExamTip": "Why no adhimokkha in vicikicchā? Decision is the opposite of doubt.",
      "examQuestionType": "Combination Calculus"
    },
    "pt": {
      "question": "Calcule os Cetasikas em: (1) 1º Lobha, (2) Vicikicchā, (3) Lokuttara 1º Jhāna.",
      "answer": "(1) 1º Lobha: 19 (13 variáveis + 4 moha + lobha + diṭṭhi)\n(2) Vicikicchā: 15 (7 universais + vitakka, vicāra, vīriya + 4 moha + vicikicchā)\n(3) Lokuttara 1º Jhāna: 36 (13 variáveis + 19 belos universais + 3 virati + paññā)",
      "breakdown": [
        "Vicikicchā não tem adhimokkha (decisão), pīti nem chanda.",
        "Lokuttara não tem Appamaññā."
      ],
      "explanation": "Cálculo combinatório rigoroso do Abhidhamma.",
      "mnemonicOrExamTip": "Por que sem adhimokkha na dúvida? Decisão e dúvida são opostos.",
      "examQuestionType": "Cálculo Combinatório"
    },
    "es": {
      "question": "¿Cuántos Cetasikas hay en: (1) 1º Lobha, (2) Vicikicchā, (3) Lokuttara 1º Jhāna?",
      "answer": "(1) 1º Lobha: 19 cetasikas (13 aññasamāna + 4 moha + 2 lobha/diṭṭhi)\n(2) Vicikicchā: 15 cetasikas (7 universales + 3 ocasionales + 4 moha + 1 vicikicchā)\n(3) Lokuttara 1º Jhāna: 36 cetasikas (13 aññasamāna + 19 bellos + 3 virati + 1 paññā)",
      "breakdown": [
        "Vicikicchā excluye adhimokkha.",
        "Lokuttara excluye Appamaññā."
      ],
      "explanation": "Cálculo de combinaciones.",
      "mnemonicOrExamTip": "Adhimokkha incompatible con duda.",
      "examQuestionType": "Cálculo de Saṅgahanaya"
    }
  },
  {
    "id": "ch3-01",
    "chapter": 3,
    "chapterName": {
      "pali": "Pakiṇṇakaparicchedo",
      "en": "Chapter 3: Miscellaneous",
      "pt": "Capítulo 3: Categorias Diversas",
      "es": "Capítulo 3: Misceláneas"
    },
    "section": "14 Kiccas of Consciousness",
    "category": "structures",
    "paliTerm": "Kiccasaṅgaho 14",
    "tags": [
      "kicca",
      "functions",
      "patisandhi",
      "bhavanga",
      "cuti",
      "javana"
    ],
    "en": {
      "question": "List the 14 Functions of Consciousness and the citta with the most functions.",
      "answer": "14 Functions:\n1. Paṭisandhi (Rebirth), 2. Bhavaṅga (Life-continuum), 3. Āvajjana (Adverting), 4-8. 5 Senses (seeing, hearing, smelling, tasting, touching), 9. Sampaṭicchana (Receiving), 10. Santīraṇa (Investigating), 11. Voṭṭhabbana (Determining), 12. Javana (Impulsion), 13. Tadārammaṇa (Registration), 14. Cuti (Death).\nMost functions: Santīraṇa-upekkhā performs 5 functions.",
      "breakdown": [
        "19 Cittas perform Paṭisandhi, Bhavaṅga, Cuti.",
        "55 Cittas perform Javana.",
        "11 Cittas perform Tadārammaṇa."
      ],
      "explanation": "Consciousness is an event series, not a permanent soul.",
      "mnemonicOrExamTip": "19 cittas perform the rebirth-life-death cycle.",
      "examQuestionType": "14 Functions Sequence"
    },
    "pt": {
      "question": "Liste as 14 Funções da Consciência e o citta com mais funções.",
      "answer": "14 Funções:\n1. Paṭisandhi (Renascimento), 2. Bhavaṅga (Fluxo vital), 3. Āvajjana (Advertência), 4-8. 5 Sentidos (ver, ouvir, cheirar, saborear, tocar), 9. Sampaṭicchana (Recepção), 10. Santīraṇa (Investigação), 11. Voṭṭhabbana (Determinação), 12. Javana (Impulsão cármica), 13. Tadārammaṇa (Registro), 14. Cuti (Morte).\nMais funções: Santīraṇa com upekkhā executa 5 funções.",
      "breakdown": [
        "19 Cittas realizam Paṭisandhi, Bhavaṅga, Cuti.",
        "55 realizam Javana.",
        "11 realizam Tadārammaṇa."
      ],
      "explanation": "A mente é um fluxo dinâmico funcional.",
      "mnemonicOrExamTip": "19 cittas operam o renascimento, vida e morte.",
      "examQuestionType": "Sequência das 14 Funções"
    },
    "es": {
      "question": "¿Cuáles son las 14 Funciones y qué citta cumple más funciones?",
      "answer": "1. Paṭisandhi, 2. Bhavaṅga, 3. Āvajjana, 4-8. 5 sentidos, 9. Sampaṭicchana, 10. Santīraṇa, 11. Voṭṭhabbana, 12. Javana, 13. Tadārammaṇa, 14. Cuti.\nCitta con más funciones: Santīraṇa upekkhā (5).",
      "breakdown": [
        "19 Cittas realizan Paṭisandhi, Bhavaṅga y Cuti.",
        "55 Cittas realizan Javana.",
        "11 Cittas realizan Tadārammaṇa."
      ],
      "explanation": "Proceso sin alma fija.",
      "mnemonicOrExamTip": "19 cittas del ciclo vital.",
      "examQuestionType": "14 Funciones de Citta"
    }
  },
  {
    "id": "ch3-02",
    "chapter": 3,
    "chapterName": {
      "pali": "Pakiṇṇakaparicchedo",
      "en": "Chapter 3: Miscellaneous",
      "pt": "Capítulo 3: Categorias Diversas",
      "es": "Capítulo 3: Misceláneas"
    },
    "section": "6 Physical Bases & Heart-Base",
    "category": "structures",
    "paliTerm": "Vatthusaṅgaho 6",
    "tags": [
      "vatthu",
      "hadayavatthu",
      "bases",
      "arupabhumi"
    ],
    "en": {
      "question": "What are the 6 Physical Bases (Vatthu) and how are the 89 Cittas distributed among them?",
      "answer": "6 Bases: Eye, ear, nose, tongue, body (5 sense bases), and Heart-base (hadayavatthu).\nCanonical Distribution (10 + 33 + 42 + 4 = 89):\n• 10 Sense-consciousnesses: Invariably depend on the 5 physical sense bases.\n• 33 Cittas: Invariably depend on the Heart-base (2 dosa + 3 manodhātu + 3 santīraṇa + 1 hasituppāda + 8 mahāvipāka + 15 rūpāvacara + 1 sotāpattimagga).\n• 42 Cittas: Depend on the Heart-base in Kāma/Rūpa realms, or arise BASELESS in the Arūpa realm (10 akusala [lobha/moha] + 1 manodvārāvajjana + 16 mahākusala/kiriya + 8 arūpa kusala/kiriya + 7 higher lokuttara).\n• 4 Cittas: ALWAYS Baseless (the 4 Arūpāvacara Vipāka cittas).",
      "breakdown": [
        "85 cittas (10 + 33 + 42) can depend on a physical base; 4 cittas (Arūpa vipākas) never have a base.",
        "Why does Sotāpattimagga invariably require the Heart-base? Because Stream-Entry cannot be attained in Arūpabhūmi (no ear-base to hear the Dhamma!)."
      ],
      "explanation": "Abhidhamma maps mind-matter interdependence down to the exact realm and path level.",
      "mnemonicOrExamTip": "Exam Formula: 10 (5 bases) + 33 (always heart-base, incl. Sotāpattimagga!) + 42 (optional heart-base) + 4 (never a base) = 89 Cittas.",
      "examQuestionType": "Bases & Realms"
    },
    "pt": {
      "question": "Quais são as 6 Bases Físicas (Vatthu) e como os 89 Cittas se distribuem nelas?",
      "answer": "6 Bases: Olho, ouvido, nariz, língua, corpo (5 bases sensoriais) e Base do coração (hadayavatthu).\nDistribuição Canônica (10 + 33 + 42 + 4 = 89):\n• 10 Consciências sensoriais: Dependem invariavelmente dos 5 órgãos físicos.\n• 33 Cittas: Dependem invariavelmente da Base do Coração (2 dosa + 3 manodhātu + 3 santīraṇa + 1 hasituppāda + 8 mahāvipāka + 15 rūpāvacara + 1 sotāpattimagga).\n• 42 Cittas: Dependem do coração nos planos Kāma/Rūpa, e surgem SEM BASE no Reino Imaterial (10 akusala [lobha/moha] + 1 manodvārāvajjana + 16 mahākusala/kiriya + 8 arūpa kusala/kiriya + 7 lokuttara superiores).\n• 4 Cittas: SEMPRE sem base física (os 4 Arūpāvacara Vipāka).",
      "breakdown": [
        "85 cittas (10 + 33 + 42) podem ter base física; 4 cittas (Arūpa vipākas) nunca têm base.",
        "Por que o Sotāpattimagga exige invariavelmente a base do coração? Porque não se pode atingir o Entrar-na-Correnteza em Arūpabhūmi (sem ouvido físico para ouvir o Dhamma!)."
      ],
      "explanation": "Demonstração rigorosa da interdependência mente-matéria e da autonomia mental nos reinos imateriais.",
      "mnemonicOrExamTip": "Fórmula de Prova: 10 (5 sentidos) + 33 (sempre coração, incl. Sotāpattimagga!) + 42 (com ou sem base) + 4 (sempre sem base) = 89 Cittas.",
      "examQuestionType": "Bases Físicas e Planos"
    },
    "es": {
      "question": "¿Cuáles son las 6 Bases Físicas (Vatthu) y cómo se distribuyen los 89 Cittas?",
      "answer": "6 Bases: 5 órganos sensoriales + Base del corazón (hadayavatthu).\nDistribución Canónica (10 + 33 + 42 + 4 = 89):\n• 10 Sentidos: En las 5 bases físicas.\n• 33 Cittas: Siempre en la base del corazón (incluye 2 dosa, 15 rūpa y 1 sotāpattimagga).\n• 42 Cittas: Con base en Kāma/Rūpa, y SIN base en Arūpa.\n• 4 Cittas: SIEMPRE sin base (los 4 Arūpāvacara Vipāka).",
      "breakdown": [
        "85 cittas pueden tener base física; 4 nunca tienen base.",
        "Sotāpattimagga exige siempre base física porque no puede surgir en Arūpabhūmi."
      ],
      "explanation": "Autonomía mental en lo inmaterial e interdependencia en planos materiales.",
      "mnemonicOrExamTip": "Fórmula: 10 + 33 + 42 + 4 = 89 Cittas.",
      "examQuestionType": "Bases Físicas"
    }
  },
  {
    "id": "ch4-01",
    "chapter": 4,
    "chapterName": {
      "pali": "Vīthiparicchedo",
      "en": "Chapter 4: Cognitive Process",
      "pt": "Capítulo 4: Processo Cognitivo",
      "es": "Capítulo 4: Proceso Cognitivo"
    },
    "section": "17 Thought-Moments Sequence",
    "category": "structures",
    "paliTerm": "Pañcadvāravīthi 17",
    "tags": [
      "vithi",
      "17 moments",
      "javana",
      "cittakkhana"
    ],
    "en": {
      "question": "Enumerate the 17 moments of the Five-Door Cognitive Process and where kamma is made.",
      "answer": "1. Atīta-bhavaṅga, 2. Bhavaṅga-calana, 3. Bhavaṅgupaccheda, 4. Pañcadvārāvajjana, 5. Sense consciousness (seeing, etc.), 6. Sampaṭicchana, 7. Santīraṇa, 8. Voṭṭhabbana, 9-15. Javana (7 moments), 16-17. Tadārammaṇa (2 moments).\nKamma Generation: ONLY in the 7 Javana moments (9 to 15)!",
      "breakdown": [
        "1 material unit (rūpa) lasts exactly 17 thought-moments.",
        "Moments 1-8 are passive/receptive; 9-15 are active kamma."
      ],
      "explanation": "Cognitive process lifespan matches physical lifespan of perceived matter.",
      "mnemonicOrExamTip": "Kamma is created ONLY during Javana (moments 9-15).",
      "examQuestionType": "Cognitive Process Sequence"
    },
    "pt": {
      "question": "Enumere os 17 momentos do processo dos sentidos e onde o karma é gerado.",
      "answer": "1. Atīta-bhavaṅga, 2. Bhavaṅga-calana, 3. Bhavaṅgupaccheda, 4. Pañcadvārāvajjana, 5. Consciência sensorial (ver, etc.), 6. Sampaṭicchana, 7. Santīraṇa, 8. Voṭṭhabbana, 9-15. Javana (7 momentos), 16-17. Tadārammaṇa (2 momentos).\nGeração Cármica: EXCLUSIVAMENTE nos 7 momentos de Javana (9 a 15)!",
      "breakdown": [
        "A vida da matéria dura 17 momentos mentais.",
        "Momentos 1 a 8 são passivos; 9 a 15 geram karma."
      ],
      "explanation": "Sincronia entre física da matéria e psicologia mental.",
      "mnemonicOrExamTip": "O karma só é gerado nos momentos 9 a 15 (Javana).",
      "examQuestionType": "Sequência dos 17 Momentos"
    },
    "es": {
      "question": "¿Cuáles son los 17 momentos del proceso sensorial y dónde se crea el kamma?",
      "answer": "1-3. Bhavaṅga, 4. Advertencia, 5. Sentido, 6. Recepción, 7. Investigación, 8. Determinación, 9-15. Javana (7 momentos), 16-17. Registro (2).\nEl kamma se crea ÚNICAMENTE en Javana (9-15).",
      "breakdown": [
        "Materia dura 17 momentos de pensamiento.",
        "Javana es la fase activa."
      ],
      "explanation": "Sincronía psico-física.",
      "mnemonicOrExamTip": "Kamma solo en Javana.",
      "examQuestionType": "Proceso de 17 Momentos"
    }
  },
  {
    "id": "ch4-02",
    "chapter": 4,
    "chapterName": {
      "pali": "Vīthiparicchedo",
      "en": "Chapter 4: Cognitive Process",
      "pt": "Capítulo 4: Processo Cognitivo",
      "es": "Capítulo 4: Proceso Cognitivo"
    },
    "section": "Appanāvīthi Stages",
    "category": "structures",
    "paliTerm": "Appanāvīthi 5 Stages",
    "tags": [
      "appanavithi",
      "jhana",
      "magga",
      "gotrabhu"
    ],
    "en": {
      "question": "What are the stages of the Absorption Cognitive Process (Appanāvīthi)?",
      "answer": "1. Parikamma (Preparation)\n2. Upacāra (Access)\n3. Anuloma (Adaptation)\n4. Gotrabhū (Change-of-lineage) [Vodāna in higher paths]\n5. Appanā (Absorption: Jhāna or Magga)\nNote: Sharp intellect (tikkhapuggala) omits Parikamma.",
      "breakdown": [
        "First attainment of Jhāna or Path lasts exactly 1 thought-moment.",
        "Gotrabhū transcends the worldling lineage."
      ],
      "explanation": "Prepares the mind to break into fine-material or supramundane frequency.",
      "mnemonicOrExamTip": "First attainment of Jhāna or Magga lasts only ONE single thought-moment.",
      "examQuestionType": "Absorption Stages"
    },
    "pt": {
      "question": "Quais são as etapas do Processo de Absorção (Appanāvīthi)?",
      "answer": "1. Parikamma (Preparação)\n2. Upacāra (Acesso)\n3. Anuloma (Adaptação)\n4. Gotrabhū (Mudança de linhagem) [Vodāna nos caminhos superiores]\n5. Appanā (Absorção: Jhāna ou Magga)\nNota: Praticante perspicaz omite o Parikamma.",
      "breakdown": [
        "A primeira realização dura exatamente 1 momento mental.",
        "Gotrabhū rompe a linhagem mundana."
      ],
      "explanation": "Transição acelerada para o plano sublime ou supramundano.",
      "mnemonicOrExamTip": "A primeira absorção dura apenas UM momento de pensamento.",
      "examQuestionType": "Etapas de Absorção"
    },
    "es": {
      "question": "¿Cuáles son las etapas de Appanāvīthi?",
      "answer": "1. Parikamma, 2. Upacāra, 3. Anuloma, 4. Gotrabhū, 5. Appanā.\nEl practicante agudo omite Parikamma.",
      "breakdown": [
        "Primer logro dura 1 solo momento.",
        "Gotrabhū corta el linaje mundano."
      ],
      "explanation": "Aceleración hacia la absorción.",
      "mnemonicOrExamTip": "Primera absorción = 1 momento.",
      "examQuestionType": "Etapas de Appanāvīthi"
    }
  },
  {
    "id": "ch5-01",
    "chapter": 5,
    "chapterName": {
      "pali": "Vīthimuttaparicchedo",
      "en": "Chapter 5: Process-Freed",
      "pt": "Capítulo 5: Consciência Fora do Processo",
      "es": "Capítulo 5: Fuera del Proceso"
    },
    "section": "4 Kinds of Kamma by Function",
    "category": "structures",
    "paliTerm": "Kammacatukka Function",
    "tags": [
      "kamma",
      "janaka",
      "upatthambhaka",
      "upapilaka",
      "upaghataka"
    ],
    "en": {
      "question": "What are the 4 Kinds of Kamma classified by Function?",
      "answer": "1. Janaka (Productive - produces rebirth and aggregates)\n2. Upatthambhaka (Supportive - sustains existing results)\n3. Upapīḷaka (Obstructive - weakens other kamma)\n4. Upaghātaka (Destructive - completely cuts off and supplants other kamma)",
      "breakdown": [
        "Analogy: Janaka is the seed; Upatthambhaka is water/fertilizer; Upapīḷaka is pests/drought; Upaghātaka is lightning striking the tree."
      ],
      "explanation": "Dynamics of karmic interaction across lifetimes.",
      "mnemonicOrExamTip": "Seed, Fertilizer, Pest, Lightning.",
      "examQuestionType": "Functional Kamma"
    },
    "pt": {
      "question": "Quais são os 4 Tipos de Karma por Função?",
      "answer": "1. Janaka (Produtor - gera renascimento e agregados)\n2. Upatthambhaka (Sustentador - apoia resultados em curso)\n3. Upapīḷaka (Obstrutor - enfraquece outro karma)\n4. Upaghātaka (Destrutivo - corta e substitui abruptamente outro karma)",
      "breakdown": [
        "Analogia: Janaka é a semente; Upatthambhaka é água/adubo; Upapīḷaka é praga; Upaghātaka é o raio que queima a árvore."
      ],
      "explanation": "Dinâmica de retribuição cármica entre vidas.",
      "mnemonicOrExamTip": "Semente, Adubo, Praga, Raio.",
      "examQuestionType": "Karma por Função"
    },
    "es": {
      "question": "¿Cuáles son los 4 Tipos de Kamma por Función?",
      "answer": "1. Janaka (Productor), 2. Upatthambhaka (Sostenedor), 3. Upapīḷaka (Obstructor), 4. Upaghātaka (Destructivo).",
      "breakdown": [
        "Semilla, Abono, Plaga, Rayo."
      ],
      "explanation": "Interacción de fuerzas cármicas.",
      "mnemonicOrExamTip": "Semilla, Abono, Plaga, Rayo.",
      "examQuestionType": "Tipos de Kamma"
    }
  },
  {
    "id": "ch5-02",
    "chapter": 5,
    "chapterName": {
      "pali": "Vīthimuttaparicchedo",
      "en": "Chapter 5: Process-Freed",
      "pt": "Capítulo 5: Consciência Fora do Processo",
      "es": "Capítulo 5: Fuera del Proceso"
    },
    "section": "Death & Rebirth Sequence",
    "category": "structures",
    "paliTerm": "Maraṇāsanna Transition",
    "tags": [
      "death",
      "rebirth",
      "cuti",
      "patisandhi",
      "signs",
      "antarabhava"
    ],
    "en": {
      "question": "Describe the 3 Death Signs and the Cuti-to-Paṭisandhi transition.",
      "answer": "3 Signs:\n1. Kamma (Memory of deed)\n2. Kammanimitta (Sign/tool of deed)\n3. Gatinimitta (Vision of destination)\nTransition: Cuti citta falls away; immediately in the next instant, Paṭisandhi citta arises in the new realm WITHOUT ANY INTERMEDIATE STATE (antarābhava).",
      "breakdown": [
        "Theravāda rejects intermediate bardo states.",
        "Immediate continuity of causal conditioning."
      ],
      "explanation": "Rebirth is like a seal pressed into wax or an echo in a cavern.",
      "mnemonicOrExamTip": "No intermediate state between death and rebirth in Theravāda.",
      "examQuestionType": "Death & Rebirth"
    },
    "pt": {
      "question": "Descreva os 3 Sinais da Morte e a transição Cuti-Paṭisandhi.",
      "answer": "3 Sinais:\n1. Kamma (Lembrança da ação)\n2. Kammanimitta (Símbolo/objeto da ação)\n3. Gatinimitta (Visão do destino futuro)\nTransição: O Cuti citta cessa; imediatamente no próximo instante surge o Paṭisandhi citta no novo reino SEM NENHUM ESTADO INTERMEDIÁRIO (antarābhava).",
      "breakdown": [
        "O Theravāda rejeita qualquer bardo ou estado intermediário.",
        "Continuidade causal imediata."
      ],
      "explanation": "O renascimento é instantâneo como um sinete na cera.",
      "mnemonicOrExamTip": "Não há bardo intermediário no Theravāda.",
      "examQuestionType": "Morte e Renascimento"
    },
    "es": {
      "question": "¿Cuáles son los 3 signos de muerte y cómo es la transición?",
      "answer": "3 Signos: Kamma, Kammanimitta, Gatinimitta.\nTransición: Cuti cesa y surge Paṭisandhi de inmediato sin estado intermedio.",
      "breakdown": [
        "Rechazo de bardo en Theravāda.",
        "Causalidad instantánea."
      ],
      "explanation": "Continuidad sin alma fija.",
      "mnemonicOrExamTip": "Sin estado intermedio.",
      "examQuestionType": "Transición de Vida"
    }
  },
  {
    "id": "ch6-01",
    "chapter": 6,
    "chapterName": {
      "pali": "Rūpaparicchedo",
      "en": "Chapter 6: Matter & Nibbāna",
      "pt": "Capítulo 6: Matéria e Nibbāna",
      "es": "Capítulo 6: Materia y Nibbāna"
    },
    "section": "28 Rūpas Breakdown",
    "category": "structures",
    "paliTerm": "Rūpa 28",
    "tags": [
      "rupa",
      "28",
      "mahabhuta",
      "upadarupa",
      "nipphanna"
    ],
    "en": {
      "question": "What are the 28 Rūpas and their division into Nipphanna and Anipphanna?",
      "answer": "28 Rūpas = 4 Mahābhūtas (Earth, Water, Fire, Air) + 24 Upādārūpas.\nDivided into:\n• 18 Nipphanna (Concretely produced - real physical substances)\n• 10 Anipphanna (Non-concretely produced - abstract modes, limits, traits)",
      "breakdown": [
        "18 Nipphanna: 4 elements, 5 sensitivities, 4 sense objects, 2 sexes, heart-base, life faculty, nutriment.",
        "10 Anipphanna: space, 2 intimations, 3 mutabilities, 4 characteristics."
      ],
      "explanation": "Only the 18 Nipphannas have intrinsic material reality (sabhāva).",
      "mnemonicOrExamTip": "Formula: 18 Real + 10 Abstract = 28 Rūpas.",
      "examQuestionType": "Matter Taxonomy"
    },
    "pt": {
      "question": "Quais são os 28 Rūpas e sua divisão em Nipphanna e Anipphanna?",
      "answer": "28 Rūpas = 4 Mahābhūtas (Terra, Água, Fogo, Ar) + 24 Upādārūpas.\nDivididos em:\n• 18 Nipphanna (Concretamente produzidos - matéria real sabhāva)\n• 10 Anipphanna (Não-concretos - modos, limites e características)",
      "breakdown": [
        "18 Nipphanna: 4 elementos, 5 sentidos, 4 objetos, 2 sexos, coração, vida física, nutriente.",
        "10 Anipphanna: espaço, 2 comunicações, 3 mutabilidades, 4 características de mudança."
      ],
      "explanation": "Apenas os 18 Nipphanna possuem substância ontológica concreta.",
      "mnemonicOrExamTip": "Fórmula: 18 Concretos + 10 Modais = 28 Rūpas.",
      "examQuestionType": "Taxonomia da Matéria"
    },
    "es": {
      "question": "¿Cuáles son los 28 Rūpas y su división?",
      "answer": "28 Rūpas = 4 Elementos + 24 Materias Derivadas.\n• 18 Nipphanna (Concretos)\n• 10 Anipphanna (Abstractos/Modales)",
      "breakdown": [
        "18 concretos tienen sabhāva real.",
        "10 abstractos describen límites y cambios."
      ],
      "explanation": "Base física analítica.",
      "mnemonicOrExamTip": "18 reales + 10 abstractos = 28.",
      "examQuestionType": "Taxonomía de Rūpa"
    }
  },
  {
    "id": "ch6-02",
    "chapter": 6,
    "chapterName": {
      "pali": "Rūpaparicchedo",
      "en": "Chapter 6: Matter & Nibbāna",
      "pt": "Capítulo 6: Matéria e Nibbāna",
      "es": "Capítulo 6: Materia y Nibbāna"
    },
    "section": "Touch Physics Exception",
    "category": "exam_traps",
    "paliTerm": "Phoṭṭhabba Physics",
    "tags": [
      "touch",
      "water",
      "earth",
      "fire",
      "air",
      "photthabba"
    ],
    "en": {
      "question": "Why can Water (āpodhātu) NEVER be physically touched according to Abhidhamma?",
      "answer": "Tangible object (Phoṭṭhabbārammaṇa) consists of only 3 Great Essentials: Earth (solidity/hardness), Fire (temperature/hot-cold), and Air (motion/pressure).\nWater (āpodhātu) has the characteristic of cohesion/flowing, which cannot be sensed by the physical body sense; 'wetness' is mentally inferred through temperature and fluidity.",
      "breakdown": [
        "You feel temperature (tejo), pressure (vāyo), and softness/hardness (pathavī).",
        "Cohesion (āpo) binds matter together invisibly."
      ],
      "explanation": "Water is perceived mentally as a concept, never directly touched as a tangible.",
      "mnemonicOrExamTip": "Water is NOT a tangible object in Abhidhamma physics.",
      "examQuestionType": "Sensory Physics (Exam Trap)"
    },
    "pt": {
      "question": "Por que a Água (āpodhātu) NUNCA pode ser tocada fisicamente segundo o Abhidhamma?",
      "answer": "O objeto tátil (Phoṭṭhabba) consiste em apenas 3 Grandes Elementos: Terra (dureza/maciez), Fogo (temperatura quente/frio) e Ar (pressão/movimento).\nA Água (āpodhātu) tem a característica de coesão e fluidez, que não pode ser sentida pela sensibilidade do corpo; a 'umidade' é inferida mentalmente através da temperatura e da resistência.",
      "breakdown": [
        "Sentimos temperatura (tejo), pressão (vāyo) e maciez (pathavī).",
        "A coesão da água apenas une os outros elementos."
      ],
      "explanation": "A água é apreendida como conceito mental, nunca como estímulo tátil primário.",
      "mnemonicOrExamTip": "A água NÃO é um objeto tátil na física do Abhidhamma.",
      "examQuestionType": "Física Sensorial (Pegadinha)"
    },
    "es": {
      "question": "¿Por qué el Agua (āpodhātu) NO es tangible?",
      "answer": "El tacto solo percibe 3 elementos: Tierra (solidez), Fuego (temperatura) y Aire (presión).\nEl Agua es cohesión/fluidez que no choca con el cuerpo; 'humedad' es inferencia mental.",
      "breakdown": [
        "Se siente calor/frío y presión.",
        "La cohesión une la materia."
      ],
      "explanation": "El agua no es tangible primario.",
      "mnemonicOrExamTip": "El agua no es objeto táctil.",
      "examQuestionType": "Física del Tacto"
    }
  },
  {
    "id": "ch6-03",
    "chapter": 6,
    "chapterName": {
      "pali": "Rūpaparicchedo",
      "en": "Chapter 6: Matter & Nibbāna",
      "pt": "Capítulo 6: Matéria e Nibbāna",
      "es": "Capítulo 6: Materia y Nibbāna"
    },
    "section": "Kalāpas & Conception",
    "category": "structures",
    "paliTerm": "Kalāpas & Conception",
    "tags": [
      "kalapa",
      "suddhatthaka",
      "conception",
      "30 rupas"
    ],
    "en": {
      "question": "What is the Pure Octad (Suddhaṭṭhaka) and what arises at human conception?",
      "answer": "Pure Octad (8): Earth, Water, Fire, Air, Color, Smell, Taste, Nutriment (ojā).\nAt Human Conception in the Womb:\nExactly 3 Kamma-born Decads arise simultaneously:\n1. Kāya-dasaka (Body-decad: 8 + life + body-sensitivity)\n2. Bhāva-dasaka (Sex-decad: 8 + life + sex-matter)\n3. Hadaya-dasaka (Heart-decad: 8 + life + heart-base)\nTotal: Exactly 30 physical elements arise at the moment of paṭisandhi.",
      "breakdown": [
        "Matter always exists in inseparable clusters (kalāpas); at conception, 3 decads = 30 kamma-produced material qualities.",
        "Total canonical Rūpakalāpas = 21 (9 kammaja + 6 cittaja + 4 utuja + 2 āhāraja = 21)."
      ],
      "explanation": "Embryological genesis begins with body, sex, and heart.",
      "mnemonicOrExamTip": "Conception: 3 decads = 30 physical units. Total Kalāpas: 9 + 6 + 4 + 2 = 21.",
      "examQuestionType": "Atomic Clusters & Embryology"
    },
    "pt": {
      "question": "O que é o Octeto Puro (Suddhaṭṭhaka) e o que surge na concepção humana?",
      "answer": "Octeto Puro (8): Terra, Água, Fogo, Ar, Cor, Cheiro, Sabor e Nutriente (ojā).\nNa Concepção Humana no Útero:\nSurgem exatamente 3 Décadas geradas pelo Karma:\n1. Kāya-dasaka (Década do corpo: 8 + vida + sensibilidade corporal)\n2. Bhāva-dasaka (Década do sexo: 8 + vida + matéria sexual)\n3. Hadaya-dasaka (Década do coração: 8 + vida + base do coração)\nTotal: Exatamente 30 elementos físicos no instante do paṭisandhi.",
      "breakdown": [
        "A matéria existe em conglomerados atômicos (kalāpas); na concepção, 3 décadas = 30 elementos materiais.",
        "Total canônico de Rūpakalāpas = 21 (9 kammaja + 6 cittaja + 4 utuja + 2 āhāraja = 21)."
      ],
      "explanation": "O embrião começa com corpo, sexo e suporte cardíaco.",
      "mnemonicOrExamTip": "Concepção: 3 décadas = 30 elementos materiais. Total de Kalāpas: 9 + 6 + 4 + 2 = 21.",
      "examQuestionType": "Clusters Atômicos e Embriologia"
    },
    "es": {
      "question": "¿Qué es el Octeto Puro y qué surge en la concepción humana?",
      "answer": "Octeto Puro: 4 elementos + Color, Olor, Sabor, Nutrición (8).\nEn la concepción: 3 Décadas generadas por kamma (Cuerpo, Sexo, Corazón) = 30 elementos materiales.",
      "breakdown": [
        "Materia en racimos (kalāpas); en la concepción, 3 décadas = 30 elementos.",
        "Total canónico de Rūpakalāpas = 21 (9 kammaja + 6 cittaja + 4 utuja + 2 āhāraja = 21)."
      ],
      "explanation": "Base embrionaria.",
      "mnemonicOrExamTip": "30 elementos en la concepción.",
      "examQuestionType": "Kalāpas y Concepción"
    }
  },
  {
    "id": "ch6-04",
    "chapter": 6,
    "chapterName": {
      "pali": "Rūpaparicchedo",
      "en": "Chapter 6: Matter & Nibbāna",
      "pt": "Capítulo 6: Matéria e Nibbāna",
      "es": "Capítulo 6: Materia y Nibbāna"
    },
    "section": "Nibbāna Definition & Aspects",
    "category": "philosophy",
    "paliTerm": "Nibbāna",
    "tags": [
      "nibbana",
      "asankhata",
      "saupadisesa",
      "anupadisesa"
    ],
    "en": {
      "question": "Define Nibbāna and explain its two aspects.",
      "answer": "Nibbāna: The 4th Ultimate Reality, unconditioned (asaṅkhata-dhātu), cessation of craving and suffering.\nTwo Aspects:\n1. Sa-upādisesa-nibbāna: With aggregates remaining (attained at enlightenment while living).\n2. Anupādisesa-nibbāna: Without aggregates remaining (at Parinibbāna/death of an Arahant).",
      "breakdown": [
        "Nibbāna is ONE in its intrinsic nature (sabhāva).",
        "Difference refers purely to presence or absence of the physical body."
      ],
      "explanation": "Object of all supramundane path and fruition consciousnesses.",
      "mnemonicOrExamTip": "Nibbāna is ontologically ONE; the two aspects refer only to the physical body.",
      "examQuestionType": "Ultimate Reality of Nibbāna"
    },
    "pt": {
      "question": "Defina Nibbāna e explique seus dois aspectos.",
      "answer": "Nibbāna: A 4ª Realidade Última, incondicionado (asaṅkhata), cessação da sede e do sofrimento.\nDois Aspectos:\n1. Sa-upādisesa-nibbāna: Com resíduo dos agregados (iluminação em vida).\n2. Anupādisesa-nibbāna: Sem resíduo dos agregados (no Parinibbāna/morte do Arahant).",
      "breakdown": [
        "Nibbāna é estritamente UM em sua essência (sabhāva).",
        "A divisão refere-se apenas à presença ou extinção do corpo físico."
      ],
      "explanation": "Objeto exclusivo dos estados supramundanos.",
      "mnemonicOrExamTip": "Nibbāna é ontologicamente UM; os dois aspectos referem-se ao corpo.",
      "examQuestionType": "Realidade de Nibbāna"
    },
    "es": {
      "question": "¿Qué es Nibbāna y cuáles son sus dos aspectos?",
      "answer": "Nibbāna: Lo incondicionado, cese del sufrimiento.\n• Sa-upādisesa: Con remanente (en vida).\n• Anupādisesa: Sin remanente (Parinibbāna).",
      "breakdown": [
        "Ontológicamente es UNO solo.",
        "La distinción es por la presencia física del cuerpo."
      ],
      "explanation": "Objeto exclusivo de Lokuttara.",
      "mnemonicOrExamTip": "Nibbāna es uno en esencia.",
      "examQuestionType": "Nibbāna"
    }
  },
  {
    "id": "ch7-01",
    "chapter": 7,
    "chapterName": {
      "pali": "Samuccayaparicchedo",
      "en": "Chapter 7: Categories",
      "pt": "Capítulo 7: Categorias Gerais",
      "es": "Capítulo 7: Categorías Generales"
    },
    "section": "37 Bodhipakkhiyadhamma",
    "category": "structures",
    "paliTerm": "Bodhipakkhiya 37",
    "tags": [
      "bodhipakkhiya",
      "37",
      "viriya",
      "satipatthana",
      "bojjhanga"
    ],
    "en": {
      "question": "What are the 37 Bodhipakkhiya Dhammas and their reduction to 14 factors?",
      "answer": "37 Factors: 4 Satipaṭṭhāna + 4 Sammappadhāna + 4 Iddhipāda + 5 Indriya + 5 Bala + 7 Bojjhaṅga + 8 Maggaṅga = 37.\nReduction: They reduce to only 14 distinct Cetasikas!\nVīriya (Energy) appears 9 times across the 37 factors.",
      "breakdown": [
        "Vīriya is the supreme factor of effort in awakening.",
        "Mindfulness (Sati) appears 8 times; Wisdom (Paññā) 5 times."
      ],
      "explanation": "Synthesizes thousands of Sutta discourses into 14 psychological factors.",
      "mnemonicOrExamTip": "Most frequent factor: Vīriya (repeated 9 times).",
      "examQuestionType": "Enlightenment Synthesis"
    },
    "pt": {
      "question": "Quais são os 37 Bodhipakkhiya Dhammas e sua redução a 14 fatores?",
      "answer": "37 Fatores: 4 Satipaṭṭhāna + 4 Sammappadhāna + 4 Iddhipāda + 5 Indriya + 5 Bala + 7 Bojjhaṅga + 8 Maggaṅga = 37.\nRedução: Reduzem-se a apenas 14 Cetasikas distintos!\nVīriya (Energia) surge 9 vezes ao longo dos 37 fatores.",
      "breakdown": [
        "Vīriya é o fator supremo de esforço na iluminação.",
        "Sati aparece 8 vezes; Paññā aparece 5 vezes."
      ],
      "explanation": "Síntese magistral de toda a prática budista em 14 fatores mentais.",
      "mnemonicOrExamTip": "Fator mais frequente: Vīriya (repetido 9 vezes).",
      "examQuestionType": "Síntese da Iluminação"
    },
    "es": {
      "question": "¿Cuáles son los 37 Bodhipakkhiya Dhammas y su reducción a 14 factores?",
      "answer": "37 Factores (Satipaṭṭhāna, Sammappadhāna, Iddhipāda, Indriya, Bala, Bojjhaṅga, Maggaṅga).\nSe reducen a 14 Cetasikas. Vīriya se repite 9 veces.",
      "breakdown": [
        "Vīriya es el factor supremo de esfuerzo que aparece 9 veces en los 37 factores.",
        "Sati aparece 8 veces; Paññā aparece 5 veces."
      ],
      "explanation": "Gran síntesis del camino budista.",
      "mnemonicOrExamTip": "Factor más repetido: Vīriya (9 veces).",
      "examQuestionType": "37 Factores del Despertar"
    }
  },
  {
    "id": "ch7-02",
    "chapter": 7,
    "chapterName": {
      "pali": "Samuccayaparicchedo",
      "en": "Chapter 7: Categories",
      "pt": "Capítulo 7: Categorias Gerais",
      "es": "Capítulo 7: Categorías Generales"
    },
    "section": "Nīvaraṇas Count in Abhidhamma",
    "category": "exam_traps",
    "paliTerm": "Nīvaraṇa 6",
    "tags": [
      "nivarana",
      "hindrances",
      "avijja",
      "6 nivaranas"
    ],
    "en": {
      "question": "How many Hindrances (Nīvaraṇas) are in Abhidhamma and why?",
      "answer": "In Abhidhammatthasaṅgaha: Exactly 6 Nīvaraṇas!\n1. Kāmacchanda (Sensual lust - lobha)\n2. Byāpāda (Ill-will - dosa)\n3. Thīna-Middha (Sloth-torpor - 2 cetasikas)\n4. Uddhacca-Kukkucca (Restlessness-remorse - 2 cetasikas)\n5. Vicikicchā (Doubt)\n6. Avijjā (Ignorance - moha)",
      "breakdown": [
        "Suttas list 5 hindrances.",
        "Abhidhamma adds Avijjā as the 6th hindrance."
      ],
      "explanation": "Covers 8 actual unwholesome cetasikas.",
      "mnemonicOrExamTip": "Exam Trap: In Abhidhamma there are 6 Nīvaraṇas (adds Avijjā).",
      "examQuestionType": "Hindrances Count"
    },
    "pt": {
      "question": "Quantos Obstáculos (Nīvaraṇas) há no Abhidhamma e por quê?",
      "answer": "No Abhidhammatthasaṅgaha: Exatamente 6 Nīvaraṇas!\n1. Kāmacchanda (Desejo sensorial)\n2. Byāpāda (Má vontade/aversão)\n3. Thīna-Middha (Preguiça e torpor)\n4. Uddhacca-Kukkucca (Inquietação e remorso)\n5. Vicikicchā (Dúvida)\n6. Avijjā (Ignorância - moha)",
      "breakdown": [
        "Os Suttas contam 5 obstáculos.",
        "O Abhidhamma acrescenta Avijjā como o 6º."
      ],
      "explanation": "Engloba 8 cetasikas inábeis reais.",
      "mnemonicOrExamTip": "Pegadinha de Prova: No Abhidhamma há 6 Nīvaraṇas (inclui Avijjā).",
      "examQuestionType": "Contagem dos Obstáculos"
    },
    "es": {
      "question": "¿Cuántos Obstáculos (Nīvaraṇas) enumera el Abhidhamma?",
      "answer": "Exactamente 6 Nīvaraṇas (añade Avijjā/Ignorancia como 6º obstáculo).",
      "breakdown": [
        "Suttas = 5; Abhidhamma = 6.",
        "Cubren 8 cetasikas perjudiciales."
      ],
      "explanation": "Clasificación técnica precisa.",
      "mnemonicOrExamTip": "Abhidhamma = 6 Nīvaraṇas.",
      "examQuestionType": "Obstáculos en Abhidhamma"
    }
  },
  {
    "id": "ch8-01",
    "chapter": 8,
    "chapterName": {
      "pali": "Paccayaparicchedo",
      "en": "Chapter 8: Conditionality",
      "pt": "Capítulo 8: Condicionalidade",
      "es": "Capítulo 8: Condicionalidad"
    },
    "section": "24 Paccayas of Paṭṭhāna",
    "category": "structures",
    "paliTerm": "Paṭṭhāna 24",
    "tags": [
      "patthana",
      "24 conditions",
      "hetu",
      "sahajata",
      "paccaya"
    ],
    "en": {
      "question": "What are the 24 Conditions of Paṭṭhāna and what is Hetupaccaya?",
      "answer": "24 Conditions: 1. Hetu, 2. Ārammaṇa, 3. Adhipati, 4. Anantara, 5. Samanantara, 6. Sahajāta, 7. Aññamañña, 8. Nissaya, 9. Upanissaya, 10. Purejāta, 11. Pacchājāta, 12. Āsevana, 13. Kamma, 14. Vipāka, 15. Āhāra, 16. Indriya, 17. Jhāna, 18. Magga, 19. Sampayutta, 20. Vippayutta, 21. Atthi, 22. Natthi, 23. Vigata, 24. Avigata.\nHetupaccaya: Condition of root (the 6 roots anchoring mind like a tree).",
      "breakdown": [
        "Paṭṭhāna analyzes multidimensional relations.",
        "Sahajāta = co-nascence; Aññamañña = mutuality."
      ],
      "explanation": "Interconnected matrix of conditional causation.",
      "mnemonicOrExamTip": "Sahajāta = together; Aññamañña = mutual support like tripods.",
      "examQuestionType": "24 Conditions Catalog"
    },
    "pt": {
      "question": "Quais são os 24 Paccayas do Paṭṭhāna e o que é Hetupaccaya?",
      "answer": "24 Condições: 1. Hetu, 2. Ārammaṇa, 3. Adhipati, 4. Anantara, 5. Samanantara, 6. Sahajāta, 7. Aññamañña, 8. Nissaya, 9. Upanissaya, 10. Purejāta, 11. Pacchājāta, 12. Āsevana, 13. Kamma, 14. Vipāka, 15. Āhāra, 16. Indriya, 17. Jhāna, 18. Magga, 19. Sampayutta, 20. Vippayutta, 21. Atthi, 22. Natthi, 23. Vigata, 24. Avigata.\nHetupaccaya: As 6 raízes ancorando a mente como raízes de uma árvore.",
      "breakdown": [
        "O Paṭṭhāna analisa relações multidimensionais.",
        "Sahajāta = co-nascimento; Aññamañña = mutualidade."
      ],
      "explanation": "Teia viva de condicionalidade.",
      "mnemonicOrExamTip": "Sahajāta = nascer junto; Aññamañña = suporte mútuo recíproco.",
      "examQuestionType": "Catálogo dos 24 Paccayas"
    },
    "es": {
      "question": "¿Cuáles son las 24 Condiciones del Paṭṭhāna?",
      "answer": "24 Condiciones (Paccayas): 1. Hetu, 2. Ārammaṇa, 3. Adhipati, 4. Anantara, 5. Samanantara, 6. Sahajāta, 7. Aññamañña, 8. Nissaya, 9. Upanissaya, 10. Purejāta, 11. Pacchājāta, 12. Āsevana, 13. Kamma, 14. Vipāka, 15. Āhāra, 16. Indriya, 17. Jhāna, 18. Magga, 19. Sampayutta, 20. Vippayutta, 21. Atthi, 22. Natthi, 23. Vigata, 24. Avigata.\nHetupaccaya: Las 6 raíces que dan firmeza a la mente como las raíces de un árbol.",
      "breakdown": [
        "Relaciones causales simultáneas.",
        "Sahajāta (co-nacimiento) vs Aññamañña (mutuo)."
      ],
      "explanation": "Matriz suprema de condicionalidad.",
      "mnemonicOrExamTip": "Sahajāta = coexistencia; Aññamañña = interdependencia.",
      "examQuestionType": "24 Paccayas"
    }
  },
  {
    "id": "ch8-02",
    "chapter": 8,
    "chapterName": {
      "pali": "Paccayaparicchedo",
      "en": "Chapter 8: Conditionality",
      "pt": "Capítulo 8: Condicionalidade",
      "es": "Capítulo 8: Condicionalidad"
    },
    "section": "Paññatti Concepts",
    "category": "philosophy",
    "paliTerm": "Paññattibheda",
    "tags": [
      "pannatti",
      "atthapannatti",
      "namapannatti",
      "concepts",
      "kasina"
    ],
    "en": {
      "question": "What is the difference between Atthapaññatti and Nāmapaññatti?",
      "answer": "• Atthapaññatti: Concept as Meaning / What is signified (the idea or image in the mind, e.g. 'table', 'person', or the 'kasiṇa sign').\n• Nāmapaññatti: Concept as Name / Word (the verbal sound, sign, or label used to communicate).",
      "breakdown": [
        "6 combinations of designations.",
        "Kasiṇa sign is an Atthapaññatti (not a Paramattha)."
      ],
      "explanation": "Distinguishes between signified mental concept and signifier verbal label.",
      "mnemonicOrExamTip": "The Kasiṇa sign is Atthapaññatti.",
      "examQuestionType": "Concept Epistemology"
    },
    "pt": {
      "question": "Qual a diferença entre Atthapaññatti e Nāmapaññatti?",
      "answer": "• Atthapaññatti: Conceito como Significado (a ideia, imagem mental, ex.: 'carro', 'pessoa' ou o 'sinal do kasiṇa').\n• Nāmapaññatti: Conceito como Nome (o som verbal, palavra ou rótulo comunicativo).",
      "breakdown": [
        "6 combinações de nomes.",
        "O sinal do Kasiṇa é Atthapaññatti (não é Paramattha)."
      ],
      "explanation": "Diferença entre o conceito significado e o significante linguístico.",
      "mnemonicOrExamTip": "O sinal do Kasiṇa é Atthapaññatti.",
      "examQuestionType": "Epistemologia dos Conceitos"
    },
    "es": {
      "question": "¿Cuál es la diferencia entre Atthapaññatti y Nāmapaññatti?",
      "answer": "• Atthapaññatti: Concepto como significado / imagen mental.\n• Nāmapaññatti: Concepto como nombre / palabra designadora.",
      "breakdown": [
        "Significado vs Significante.",
        "El nimitta de meditación es Atthapaññatti."
      ],
      "explanation": "Teoría semiótica budista.",
      "mnemonicOrExamTip": "El nimitta es Atthapaññatti.",
      "examQuestionType": "Teoría de Paññatti"
    }
  },
  {
    "id": "ch9-01",
    "chapter": 9,
    "chapterName": {
      "pali": "Kammaṭṭhānaparicchedo",
      "en": "Chapter 9: Meditation",
      "pt": "Capítulo 9: Meditação e Libertação",
      "es": "Capítulo 9: Meditación y Liberación"
    },
    "section": "40 Samatha Kammaṭṭhāna",
    "category": "structures",
    "paliTerm": "Samatha 40",
    "tags": [
      "samatha",
      "40",
      "kasina",
      "anussati",
      "asubha"
    ],
    "en": {
      "question": "List the 40 Samatha Meditation Subjects and which can reach Jhāna.",
      "answer": "40 Subjects: 10 Kasiṇas + 10 Asubhas (corpses) + 10 Anussatis + 4 Brahmavihāras + 1 Food Loathsomeness + 1 Four Elements + 4 Arūpas = 40.\nJhāna Reach: Kasiṇas and Ānāpānasati (breathing) reach all 5 Jhānas. Asubhas and body mindfulness reach 1st Jhāna only. Most recollections reach only access concentration (upacārasamādhi).",
      "breakdown": [
        "Samatha pacifies the mind on a conceptual nimitta."
      ],
      "explanation": "Breathing and kasiṇas are the versatile highways to 5th Jhāna.",
      "mnemonicOrExamTip": "Only Ānāpānasati and Kasiṇas reach all 5 jhānas.",
      "examQuestionType": "Samatha Catalog"
    },
    "pt": {
      "question": "Liste os 40 Temas de Samatha e quais alcançam Jhāna.",
      "answer": "40 Temas: 10 Kasiṇas + 10 Asubhas (cadáveres) + 10 Anussatis + 4 Brahmavihāras + 1 Alimento + 1 Quatro Elementos + 4 Arūpas = 40.\nAlcance de Jhāna: Kasiṇas e Ānāpānasati alcançam os 5 Jhānas. Asubhas alcançam apenas o 1º Jhāna. A maioria das recordações atinge apenas concentração de acesso (upacāra).",
      "breakdown": [
        "Samatha pacifica a mente num nimitta."
      ],
      "explanation": "Respiração e Kasiṇas são os veículos mais completos.",
      "mnemonicOrExamTip": "Apenas Ānāpāna e Kasiṇas atingem os 5 jhānas.",
      "examQuestionType": "Catálogo de Samatha"
    },
    "es": {
      "question": "¿Cuáles son los 40 Temas de Samatha y su alcance?",
      "answer": "10 Kasiṇas + 10 Asubhas + 10 Anussatis + 4 Brahmavihāras + 1 Comida + 1 Elementos + 4 Arūpas = 40.\nKasiṇas y respiración alcanzan los 5 Jhānas.",
      "breakdown": [
        "Samatha pacifica la mente fijándola en un nimitta conceptual (Asubhas alcanzan el 1º Jhāna; recordaciones alcanzan upacāra)."
      ],
      "explanation": "Pacificación mental.",
      "mnemonicOrExamTip": "Solo Kasiṇas y Ānāpāna alcanzan 5º Jhāna.",
      "examQuestionType": "Temas de Samatha"
    }
  },
  {
    "id": "ch9-02",
    "chapter": 9,
    "chapterName": {
      "pali": "Kammaṭṭhānaparicchedo",
      "en": "Chapter 9: Meditation",
      "pt": "Capítulo 9: Meditação e Libertação",
      "es": "Capítulo 9: Meditación y Liberación"
    },
    "section": "7 Visuddhi & 10 Ñāṇa",
    "category": "structures",
    "paliTerm": "7 Visuddhi & 10 Ñāṇa",
    "tags": [
      "visuddhi",
      "nana",
      "insight",
      "sankharupekkha"
    ],
    "en": {
      "question": "What are the 7 Purifications and the peak Insight Knowledge?",
      "answer": "7 Purifications: 1. Sīla (Virtue), 2. Citta (Mind/calm), 3. Diṭṭhi (View: mind & matter), 4. Kaṅkhāvitaraṇa (Doubt: causes), 5. Maggāmagga (Path & non-path), 6. Paṭipadā (The Way - 10 Vipassanā-ñāṇas), 7. Ñāṇadassana (Knowledge & Vision - 4 Noble Paths).\nPeak Insight: Saṅkhārupekkhā-ñāṇa (Equanimity toward formations) immediately precedes the breakthrough.",
      "breakdown": [
        "1-2 are foundation; 3-6 are Vipassanā; 7 is Supramundane awakening."
      ],
      "explanation": "The staircase of spiritual development.",
      "mnemonicOrExamTip": "Saṅkhārupekkhā-ñāṇa is the immediate springboard into Stream-Entry.",
      "examQuestionType": "7 Purifications & Insight"
    },
    "pt": {
      "question": "Quais são as 7 Purificações e o ápice dos Conhecimentos de Insight?",
      "answer": "7 Purificações: 1. Sīla (Conduta), 2. Citta (Mente/calma), 3. Diṭṭhi (Visão mente-matéria), 4. Kaṅkhāvitaraṇa (Superação da dúvida/causas), 5. Maggāmagga (Caminho e não-caminho), 6. Paṭipadā (Prática - 10 Vipassanā-ñāṇas), 7. Ñāṇadassana (Visão e Conhecimento - 4 Nobres Caminhos).\nÁpice do Insight: Saṅkhārupekkhā-ñāṇa (Equanimidade com as formações).",
      "breakdown": [
        "1-2 base; 3-6 Vipassanā; 7 Despertar supramundano."
      ],
      "explanation": "Escadaria clássica da libertação.",
      "mnemonicOrExamTip": "Saṅkhārupekkhā-ñāṇa é o trampolim imediato para o Despertar.",
      "examQuestionType": "7 Purificações e Insight"
    },
    "es": {
      "question": "¿Cuáles son las 7 Purificaciones y el clímax de insight?",
      "answer": "7 Purificaciones (Sīla a Ñāṇadassana).\nClímax: Saṅkhārupekkhā-ñāṇa (Ecuanimidad ante las formaciones).",
      "breakdown": [
        "Camino clásico del Visuddhimagga."
      ],
      "explanation": "Trampolín hacia Nibbāna.",
      "mnemonicOrExamTip": "Saṅkhārupekkhā es el umbral de iluminación.",
      "examQuestionType": "7 Purificaciones"
    }
  },
  {
    "id": "ch9-03",
    "chapter": 9,
    "chapterName": {
      "pali": "Kammaṭṭhānaparicchedo",
      "en": "Chapter 9: Meditation",
      "pt": "Capítulo 9: Meditação e Libertação",
      "es": "Capítulo 9: Meditación y Liberación"
    },
    "section": "4 Noble Persons & Fetters",
    "category": "philosophy",
    "paliTerm": "Ariyapuggala & Fetters",
    "tags": [
      "ariyapuggala",
      "sotapanna",
      "sakadagami",
      "anagami",
      "arahant",
      "fetters"
    ],
    "en": {
      "question": "Identify the 4 Noble Persons, their destroyed fetters, and rebirth limits.",
      "answer": "1. Sotāpanna: Eradicates 3 fetters (personality view, doubt, rites); max 7 rebirths, never in lower realms.\n2. Sakadāgāmī: Weakens sensual lust and ill-will; max 1 sensuous rebirth.\n3. Anāgāmī: Completely eradicates sensual lust and ill-will; reborn only in Suddhāvāsa.\n4. Arahant: Eradicates remaining 5 fetters (attachment to fine-material/immaterial, conceit, restlessness, ignorance); zero rebirths.",
      "breakdown": [
        "10 Fetters total.",
        "Ill-will is destroyed at Anāgāmī; conceit and ignorance at Arahant."
      ],
      "explanation": "Irreversible structural eradication of defilements.",
      "mnemonicOrExamTip": "Ill-will is eradicated at ANĀGĀMĪ; Conceit is eradicated at ARAHANT.",
      "examQuestionType": "Noble Persons & Fetters"
    },
    "pt": {
      "question": "Identifique os 4 Nobres Indivíduos, grilhões destruídos e renascimentos.",
      "answer": "1. Sotāpanna: Destrói 3 grilhões (visão de eu, dúvida, ritos); máximo 7 vidas, nunca nos reinos inferiores.\n2. Sakadāgāmī: Enfraquece desejo sensual e aversão; máximo 1 vida sensorial.\n3. Anāgāmī: Erradica TOTALMENTE desejo sensual e aversão; renasce nas Moradas Puras.\n4. Arahant: Erradica os 5 grilhões superiores (apego à forma, ao imaterial, presunção, inquietação, ignorância); zero renascimentos.",
      "breakdown": [
        "10 grilhões no total.",
        "A aversão cessa no Anāgāmī; a presunção e ignorância no Arahant."
      ],
      "explanation": "Erradicação cirúrgica irreversível.",
      "mnemonicOrExamTip": "Aversão é extirpada em ANĀGĀMĪ; Orgulho (māna) em ARAHANT.",
      "examQuestionType": "Nobres e Grilhões"
    },
    "es": {
      "question": "¿Cuáles son las 4 Personas Nobles y sus grillos erradicados?",
      "answer": "1. Sotāpanna (3 grillos, max 7 vidas).\n2. Sakadāgāmī (debilita apego y aversión, 1 vida).\n3. Anāgāmī (destruye apego sensual y aversión, solo Suddhāvāsa).\n4. Arahant (destruye los 5 superiores, fin del renacimiento).",
      "breakdown": [
        "10 Grillos (saṃyojana) en total.",
        "La aversión se erradica en el Anāgāmī; el orgullo y la ignorancia en el Arahant."
      ],
      "explanation": "Fin definitivo de Saṃsāra.",
      "mnemonicOrExamTip": "Aversión en Anāgāmī; orgullo en Arahant.",
      "examQuestionType": "Nobles y Grillos"
    }
  },
  {
    "id": "ch9-04",
    "chapter": 9,
    "chapterName": {
      "pali": "Kammaṭṭhānaparicchedo",
      "en": "Chapter 9: Meditation",
      "pt": "Capítulo 9: Meditação e Libertação",
      "es": "Capítulo 9: Meditación y Liberación"
    },
    "section": "Nirodhasamāpatti Rules",
    "category": "exam_traps",
    "paliTerm": "Nirodhasamāpatti",
    "tags": [
      "nirodhasamapatti",
      "cessation",
      "anagami",
      "arahant",
      "7 days"
    ],
    "en": {
      "question": "Who can enter Nirodhasamāpatti and why is the maximum duration 7 days?",
      "answer": "Qualifications: Can be attained ONLY by Anāgāmīs and Arahants who master all 8 Jhānas.\nDuration Limit: Maximum 7 days, because bodily nutriment (āhāra) previously consumed sustains physical life for at most 7 days without replenishment.\nDifference from Death: Bodily heat and physical life faculty persist intact.",
      "breakdown": [
        "Worldlings and Sotāpannas/Sakadāgāmīs cannot enter.",
        "Upon emerging, fruition consciousness arises."
      ],
      "explanation": "Supreme peace of temporary experiential cessation.",
      "mnemonicOrExamTip": "Maximum duration is exactly 7 days due to nutritional limit.",
      "examQuestionType": "Cessation Attainment Rules"
    },
    "pt": {
      "question": "Quem pode entrar em Nirodhasamāpatti e por que a duração máxima é 7 dias?",
      "answer": "Qualificação: Apenas Anāgāmīs e Arahants que dominem todos os 8 Jhānas.\nLimite de Duração: Máximo de 7 dias, porque a nutrição física (āhāra) previamente ingerida sustenta o corpo por no máximo 7 dias sem reposição alimentar.\nDiferença da Morte: Calor corporal e faculdade da vida física permanecem intactos.",
      "breakdown": [
        "Pessoas comuns e praticantes dos 2 primeiros níveis não entram.",
        "Ao sair, surge o Fruto correspondente."
      ],
      "explanation": "Paz suprema de cessação em vida.",
      "mnemonicOrExamTip": "Duração máxima de 7 dias devido ao limite biológico de nutrição.",
      "examQuestionType": "Regras de Nirodhasamāpatti"
    },
    "es": {
      "question": "¿Quién puede entrar en Nirodhasamāpatti y por qué dura máximo 7 días?",
      "answer": "Solo Anāgāmīs y Arahants con los 8 Jhānas.\nDura máximo 7 días por el límite biológico de nutrición física acumulada.",
      "breakdown": [
        "El calor y la vida física persisten.",
        "Al emerger surge el fruto noble."
      ],
      "explanation": "Cese supremo en vida.",
      "mnemonicOrExamTip": "Máximo 7 días por nutrición.",
      "examQuestionType": "Reglas de Cesación"
    }
  },
  {
    "id": "ch1-11",
    "chapter": 1,
    "chapterName": {
      "pali": "Cittaparicchedo",
      "en": "Chapter 1: Consciousness",
      "pt": "Capítulo 1: Consciência",
      "es": "Capítulo 1: Conciencia"
    },
    "section": "3 Ahetuka Kiriya Cittas",
    "category": "structures",
    "paliTerm": "Ahetuka Kiriya 3",
    "tags": [
      "ahetuka",
      "kiriya",
      "hasituppada",
      "avajjana"
    ],
    "en": {
      "question": "What are the 3 Rootless Functional Consciousnesses (Ahetuka Kiriya Cittas) and their functions?",
      "answer": "1. Pañcadvārāvajjana (Five-door adverting - upekkhā)\n2. Manodvārāvajjana (Mind-door adverting - upekkhā)\n3. Hasituppāda (Smile-producing consciousness of Arahants - somanassa)",
      "breakdown": [
        "Pañcadvārāvajjana: Turns the stream of consciousness from bhavaṅga outward toward the 5 physical sense objects.",
        "Manodvārāvajjana: Adverts to mental objects in the mind door, AND functions as the determining (voṭṭhabbana) consciousness in the 5 sense doors!",
        "Hasituppāda: Arises solely in Buddhas, Paccekabuddhas, and Arahants, causing them to smile at sensuous worldly sights."
      ],
      "explanation": "These cittas are functional (kiriya): they perform cognitive tasks without bearing karmic fruit.",
      "mnemonicOrExamTip": "Exam High-Yield: Hasituppāda belongs EXCLUSIVELY to Arahants and Buddhas; ordinary beings never experience it.",
      "examQuestionType": "Functional Consciousness"
    },
    "pt": {
      "question": "Quais são os 3 Cittas Funcionais Sem Raiz (Ahetuka Kiriya) e quais suas funções?",
      "answer": "1. Pañcadvārāvajjana (Advertência nas 5 portas - upekkhā)\n2. Manodvārāvajjana (Advertência na porta da mente - upekkhā)\n3. Hasituppāda (Consciência do riso dos Arahants - somanassa)",
      "breakdown": [
        "Pañcadvārāvajjana: Vira a atenção do fluxo passivo para o estímulo exterior nos 5 sentidos.",
        "Manodvārāvajjana: Direciona a mente para pensamentos na porta mental E atua como determinante (voṭṭhabbana) nas 5 portas sensoriais!",
        "Hasituppāda: Surge exclusivamente em Budas e Arahants, produzindo um leve sorriso diante de fenômenos mundanos."
      ],
      "explanation": "São funcionais (kiriya): desempenham tarefas cognitivas sem acumular karma.",
      "mnemonicOrExamTip": "Pegadinha de Prova: O Hasituppāda é exclusivo de Arahants e Budas; pessoas comuns jamais o vivenciam.",
      "examQuestionType": "Consciências Funcionais"
    },
    "es": {
      "question": "¿Cuáles son los 3 Ahetuka Kiriya Cittas y sus funciones?",
      "answer": "1. Pañcadvārāvajjana (Advertencia 5 sentidos)\n2. Manodvārāvajjana (Advertencia mente y determinación sensorial)\n3. Hasituppāda (Risa de Arahants con alegría)",
      "breakdown": [
        "Pañcadvārāvajjana: Dirige el flujo de la conciencia desde el bhavaṅga hacia los objetos de los 5 sentidos físicos.",
        "Manodvārāvajjana: Advierte objetos mentales en la puerta de la mente Y actúa como determinador (voṭṭhabbana) en las 5 puertas sensoriales.",
        "Hasituppāda: Surge exclusivamente en Budas y Arahants al sonreír ante fenómenos mundanos."
      ],
      "explanation": "Actividad funcional pura sin residuo cármico.",
      "mnemonicOrExamTip": "Hasituppāda es exclusivo de Arahants.",
      "examQuestionType": "Kiriya Cittas"
    }
  },
  {
    "id": "ch1-12",
    "chapter": 1,
    "chapterName": {
      "pali": "Cittaparicchedo",
      "en": "Chapter 1: Consciousness",
      "pt": "Capítulo 1: Consciência",
      "es": "Capítulo 1: Conciencia"
    },
    "section": "3 Santīraṇa Cittas",
    "category": "structures",
    "paliTerm": "Santīraṇa 3",
    "tags": [
      "santirana",
      "investigating",
      "ati-ittha",
      "itthamajjhatta"
    ],
    "en": {
      "question": "What are the 3 Investigating Consciousnesses (Santīraṇa Cittas) and when does Somanassa Santīraṇa arise?",
      "answer": "1. Akusalavipāka Santīraṇa (Unwholesome resultant - with upekkhā)\n2. Kusalavipāka Santīraṇa with Upekkhā (Wholesome resultant - with upekkhā)\n3. Kusalavipāka Santīraṇa with Somanassa (Wholesome resultant - with joy)\n\nSomanassa Santīraṇa arises ONLY when the perceived object is exceedingly pleasant and desirable (atiiṭṭha-ārammaṇa).",
      "breakdown": [
        "When object is undesirable (aniṭṭha) -> Akusalavipāka santīraṇa (upekkhā).",
        "When object is moderately desirable (iṭṭhamajjhatta) -> Kusalavipāka santīraṇa with upekkhā.",
        "When object is exceptionally desirable (atiiṭṭha) -> Kusalavipāka santīraṇa with somanassa."
      ],
      "explanation": "The feeling accompanying investigation reflects the intrinsic karmic quality and desirability of the object experienced.",
      "mnemonicOrExamTip": "Exam Favorite: Why are there 3 Santīraṇas instead of 2? Because wholesome karma can yield either neutral or joyful investigation depending on the excellence of the object.",
      "examQuestionType": "Investigating Consciousness Criteria"
    },
    "pt": {
      "question": "Quais são os 3 Cittas de Investigação (Santīraṇa) e quando surge o Somanassa Santīraṇa?",
      "answer": "1. Akusalavipāka Santīraṇa (Resultante inábil - com upekkhā)\n2. Kusalavipāka Santīraṇa com Upekkhā (Resultante hábil neutro)\n3. Kusalavipāka Santīraṇa com Somanassa (Resultante hábil com alegria)\n\nO Somanassa Santīraṇa surge EXCLUSIVAMENTE quando o objeto percebido é extraordinariamente desejável e belo (atiiṭṭha-ārammaṇa).",
      "breakdown": [
        "Objeto indesejável (aniṭṭha) -> Santīraṇa inábil (upekkhā).",
        "Objeto moderadamente desejável (iṭṭhamajjhatta) -> Santīraṇa hábil com upekkhā.",
        "Objeto supremamente agradável (atiiṭṭha) -> Santīraṇa hábil com somanassa."
      ],
      "explanation": "A sensação da investigação espelha o grau de excelência objetiva do estímulo sensorial colhido pelo karma.",
      "mnemonicOrExamTip": "Pergunta de Exame: Por que há 3 Santīraṇas e não 2? Porque o resultado hábil se subdivide segundo a intensidade do objeto (moderado vs extraordinário).",
      "examQuestionType": "Critérios de Investigação Sensorial"
    },
    "es": {
      "question": "¿Cuáles son los 3 Santīraṇa Cittas y cuándo surge con alegría?",
      "answer": "1. Akusalavipāka (upekkhā)\n2. Kusalavipāka (upekkhā)\n3. Kusalavipāka (somanassa)\nSurge con alegría ÚNICAMENTE ante objetos extraordinariamente deseables (atiiṭṭha).",
      "breakdown": [
        "Objeto no deseable -> Akusalavipāka upekkhā.",
        "Objeto moderado -> Kusalavipāka upekkhā.",
        "Objeto supremo -> Kusalavipāka somanassa."
      ],
      "explanation": "La sensación refleja la calidad del objeto percibido.",
      "mnemonicOrExamTip": "Atiiṭṭha = Somanassa Santīraṇa.",
      "examQuestionType": "Investigación Sensorial"
    }
  },
  {
    "id": "ch2-08",
    "chapter": 2,
    "chapterName": {
      "pali": "Cetasikaparicchedo",
      "en": "Chapter 2: Mental Factors",
      "pt": "Capítulo 2: Fatores Mentais",
      "es": "Capítulo 2: Factores Mentales"
    },
    "section": "11 Aniyata Cetasikas",
    "category": "structures",
    "paliTerm": "Aniyata Cetasikāni 11",
    "tags": [
      "aniyata",
      "inconstant",
      "occasional",
      "mana",
      "issa",
      "macchariya",
      "virati"
    ],
    "en": {
      "question": "What are the 11 Inconstant Mental Factors (Aniyata Cetasikas), and why are they called 'inconstant'?",
      "answer": "They are called 'aniyata' (inconstant/variable) because they do not arise unfailingly in their respective cittas, but only conditionally and intermittently.\nThe 11 Aniyata Factors:\n1. Māna (Conceit)\n2. Issā (Envy)\n3. Macchariya (Stinginess)\n4. Kukkucca (Remorse)\n5. Thīna (Sloth)\n6. Middha (Torpor)\n7. Sammāvācā (Right Speech)\n8. Sammākammanta (Right Action)\n9. Sammā-ājīva (Right Livelihood)\n10. Karuṇā (Compassion)\n11. Muditā (Sympathetic Joy)",
      "breakdown": [
        "All other 41 cetasikas are Niyata (constant): whenever their host citta arises, they unfailingly arise with it.",
        "The 11 Aniyata factors arise only when their specific psychological trigger is present (e.g., conceit arises only when one compares oneself with others; envy arises only when seeing another's prosperity).",
        "In Lokuttara cittas, the 3 Virati factors transform from Aniyata into NIYATA (they arise unfailingly and simultaneously)."
      ],
      "explanation": "This distinction is essential for calculating the exact combinations (saṅgahanaya) in momentary cognitive states.",
      "mnemonicOrExamTip": "Exam Rule: 52 Cetasikas = 41 Niyata (Constant) + 11 Aniyata (Inconstant).",
      "examQuestionType": "Constant vs Inconstant Dynamics"
    },
    "pt": {
      "question": "Quais são os 11 Fatores Mentais Inconstantes (Aniyata Cetasikas) e por que recebem essa denominação?",
      "answer": "São chamados 'aniyata' (inconstantes/intermitentes) porque não surgem infalivelmente em seus cittas respectivos, mas apenas de forma condicional e episódica.\nOs 11 Fatores Aniyata:\n1. Māna (Orgulho/Presunção)\n2. Issā (Inveja)\n3. Macchariya (Avareza)\n4. Kukkucca (Remorso)\n5. Thīna (Preguiça mental)\n6. Middha (Torpor)\n7. Sammāvācā (Palavra Correta)\n8. Sammākammanta (Ação Correta)\n9. Sammā-ājīva (Modo de Vida Correto)\n10. Karuṇā (Compaixão)\n11. Muditā (Alegria Altruísta)",
      "breakdown": [
        "Os outros 41 cetasikas são Niyata (constantes): sempre que aquele tipo de citta nasce, eles surgem obrigatoriamente.",
        "Os 11 Aniyata dependem de gatilhos situacionais (ex.: presunção só nasce na comparação de status; inveja só nasce ao ver a fortuna alheia).",
        "No Lokuttara, as 3 Virati deixam de ser Aniyata e tornam-se NIYATA (surgem juntas e infalivelmente)."
      ],
      "explanation": "Fundamental para compreender as variações pontuais na contagem de fatores associados a cada mente.",
      "mnemonicOrExamTip": "Equação de Prova: 52 Cetasikas = 41 Constantes (Niyata) + 11 Inconstantes (Aniyata).",
      "examQuestionType": "Fatores Constantes vs Inconstantes"
    },
    "es": {
      "question": "¿Cuáles son los 11 Cetasikas Inconstantes (Aniyata)?",
      "answer": "Surgen de forma intermitente según circunstancias:\n1. Māna (Orgullo)\n2. Issā (Envidia)\n3. Macchariya (Avaricia)\n4. Kukkucca (Remordimiento)\n5. Thīna (Pereza)\n6. Middha (Letargo)\n7-9. 3 Virati (en lo mundano)\n10-11. 2 Appamaññā (Compasión y Alegría altruista)",
      "breakdown": [
        "Los otros 41 cetasikas son constantes (niyata): surgen infaliblemente con su citta.",
        "Los 11 Aniyata dependen de su estímulo psicológico específico (ej. orgullo al compararse; envidia ante el éxito ajeno).",
        "En Lokuttara, las 3 Virati pasan de Aniyata a NIYATA (surgen juntas e infaliblemente)."
      ],
      "explanation": "No siempre están presentes en sus cittas huéspedes.",
      "mnemonicOrExamTip": "52 = 41 Constantes + 11 Inconstantes.",
      "examQuestionType": "Factores Aniyata"
    }
  },
  {
    "id": "ch3-03",
    "chapter": 3,
    "chapterName": {
      "pali": "Pakiṇṇakaparicchedo",
      "en": "Chapter 3: Miscellaneous",
      "pt": "Capítulo 3: Categorias Diversas",
      "es": "Capítulo 3: Misceláneas"
    },
    "section": "Door-Freed Consciousness",
    "category": "structures",
    "paliTerm": "Dvāravimuttacitta 19",
    "tags": [
      "dvara",
      "dvaravimutta",
      "door-freed",
      "patisandhi",
      "bhavanga",
      "cuti"
    ],
    "en": {
      "question": "What does 'Door-Freed' (Dvāravimutta) mean, and which 19 Cittas can function without a door?",
      "answer": "A 'Door-Freed' consciousness is one that operates without entering or receiving objects through any of the 6 cognitive sense doors (the 5 sense organs or mind door).\n\nThe 19 Dvāravimutta Cittas:\n1. 2 Upekkhā-santīraṇa (1 unwholesome resultant + 1 wholesome rootless resultant)\n2. 8 Mahāvipāka Cittas (Great Resultants of the sensuous sphere)\n3. 5 Rūpāvacara Vipāka Cittas (Fine-material resultants)\n4. 4 Arūpāvacara Vipāka Cittas (Immaterial resultants)\nTotal: Exactly 19 Cittas.",
      "breakdown": [
        "They function as Dvāravimutta ONLY when performing the three tasks of:\n• Paṭisandhi (Rebirth-linking)\n• Bhavaṅga (Life-continuum)\n• Cuti (Death)",
        "During these three moments, the mind does not look outward at present sense stimuli; it solely holds the deathbed object of the previous life!"
      ],
      "explanation": "In deep dreamless sleep or at death, consciousness does not process sights, sounds, or current thoughts; it flows smoothly within the life-continuum door-free.",
      "mnemonicOrExamTip": "Exam High-Yield Rule: The 19 Dvāravimutta cittas are the EXACT SAME 19 cittas that perform Paṭisandhi, Bhavaṅga, and Cuti!",
      "examQuestionType": "Doorless Cognitive Theory"
    },
    "pt": {
      "question": "O que significa 'Livre de Portas' (Dvāravimutta) e quais são os 19 Cittas que operam sem portas sensoriais?",
      "answer": "'Livre de Portas' designa a consciência que opera sem receber estímulos por nenhuma das 6 portas cognitivas (os 5 sentidos físicos ou a porta mental).\n\nOs 19 Dvāravimutta Cittas:\n1. 2 Santīraṇa com upekkhā (1 inábil + 1 hábil ahetuka)\n2. 8 Mahāvipāka Cittas (Grandes Resultantes sensoriais)\n3. 5 Rūpāvacara Vipāka Cittas (Resultantes da forma sutil)\n4. 4 Arūpāvacara Vipāka Cittas (Resultantes imateriais)\nTotal: Exatamente 19 Cittas.",
      "breakdown": [
        "Operam como Dvāravimutta APENAS ao exercer as três funções de:\n• Paṭisandhi (Renascimento)\n• Bhavaṅga (Fluxo vital passivo)\n• Cuti (Morte)",
        "Nesses momentos, a mente não olha para estímulos presentes; apenas mantém o objeto captado no leito de morte da vida anterior!"
      ],
      "explanation": "No sono profundo sem sonhos ou na morte, a mente não apreende o mundo exterior: flui livre de portas.",
      "mnemonicOrExamTip": "Identidade Canônica Essencial: Os 19 cittas livres de portas são EXATAMENTE os mesmos 19 cittas que exercem Paṭisandhi, Bhavaṅga e Cuti!",
      "examQuestionType": "Consciência Fora das Portas"
    },
    "es": {
      "question": "¿Qué significa Dvāravimutta (Libre de Puertas) y cuáles son los 19 cittas?",
      "answer": "Conciencia que no interactúa a través de las 6 puertas sensoriales ni mentales.\nSon exactamente los 19 cittas de Paṭisandhi, Bhavaṅga y Cuti:\n• 2 santīraṇa upekkhā\n• 8 mahāvipāka\n• 5 rūpavipāka\n• 4 arūpavipāka.",
      "breakdown": [
        "Operan sin puerta en el renacimiento, sueño profundo y muerte.",
        "Mantienen el objeto de la vida anterior."
      ],
      "explanation": "Flujo continuo subconsciente.",
      "mnemonicOrExamTip": "Los 19 de Paṭisandhi son los 19 Dvāravimutta.",
      "examQuestionType": "Dvāravimutta"
    }
  },
  {
    "id": "ch3-04",
    "chapter": 3,
    "chapterName": {
      "pali": "Pakiṇṇakaparicchedo",
      "en": "Chapter 3: Miscellaneous",
      "pt": "Capítulo 3: Categorias Diversas",
      "es": "Capítulo 3: Misceláneas"
    },
    "section": "Object Restrictions",
    "category": "exam_traps",
    "paliTerm": "Ālambaṇaniyama Restrictions",
    "tags": [
      "arammana",
      "objects",
      "lokuttara",
      "nibbana",
      "restrictions"
    ],
    "en": {
      "question": "Which Consciousnesses can NEVER take Lokuttara (Nibbāna & Path/Fruit) as an object?",
      "answer": "The following cittas can NEVER take Lokuttara as object:\n• All 12 Akusala Cittas (Unwholesome minds can never grasp Nibbāna)\n• All 18 Ahetuka Cittas (Rootless minds cannot know Nibbāna)\n• 4 Mahāvipāka dissociated from wisdom (ñāṇavippayutta)\n• 4 Mahākiriya dissociated from wisdom (ñāṇavippayutta)\n• All 15 Rūpāvacara Cittas\n• All 12 Arūpāvacara Cittas\nTotal: These mundane consciousnesses are strictly barred from perceiving supramundane reality.",
      "breakdown": [
        "Which mundane cittas CAN take Lokuttara as object? ONLY the 4 Mahākusala ñāṇasampayutta and 4 Mahākiriya ñāṇasampayutta (when Noble Disciples and Arahants review their attainments in paccavekkhaṇa-vīthi)!",
        "Can unwholesome greed, hatred, or delusion take Nibbāna as an object? IMPOSSIBLE. Nibbāna can only be known by mind endowed with non-delusion/wisdom."
      ],
      "explanation": "This rule prevents philosophical confusion: unwholesome craving can crave the concept or idea of liberation, but it can never touch actual unconditioned Nibbāna.",
      "mnemonicOrExamTip": "High-Yield Exam Trap: Can an akusala citta crave Nibbāna? It can crave the CONCEPT (paññatti) of Nibbāna, but it can NEVER take real ultimate Nibbāna as its object!",
      "examQuestionType": "Cognitive Limits & Epistemological Boundaries"
    },
    "pt": {
      "question": "Quais Consciências NUNCA podem tomar o Supramundano (Lokuttara / Nibbāna) como objeto?",
      "answer": "Os seguintes cittas JAMAIS podem tomar Lokuttara como objeto:\n• Todos os 12 Akusala Cittas (Mentes inábeis nunca podem apreender Nibbāna)\n• Todos os 18 Ahetuka Cittas (Mentes sem raízes não conhecem Nibbāna)\n• 4 Mahāvipāka sem sabedoria (ñāṇavippayutta)\n• 4 Mahākiriya sem sabedoria (ñāṇavippayutta)\n• Todos os 15 Rūpāvacara Cittas\n• Todos os 12 Arūpāvacara Cittas\nTotal: Estes cittas mundanos estão totalmente excluídos de apreender Nibbāna.",
      "breakdown": [
        "Quais cittas mundanos PODEM apreender Nibbāna? APENAS os 4 Mahākusala associados à sabedoria e os 4 Mahākiriya com sabedoria (quando Nobres revisitam seus frutos na reflexão retrospectiva / paccavekkhaṇa)!",
        "O apego (lobha) pode ter Nibbāna como objeto? IMPOSSÍVEL. Nibbāna só é tocado por mentes com sabedoria lúcida."
      ],
      "explanation": "Regra epistemológica capital: o desejo pode desejar o 'conceito' de iluminação, mas nunca pode fazer contato com a realidade incondicionada de Nibbāna.",
      "mnemonicOrExamTip": "Pegadinha de Ouro em Exames: Um citta inábil (akusala) pode ter Nibbāna como objeto? Resposta: NÃO. Pode desejar o CONCEITO de Nibbāna, mas nunca a realidade última de Nibbāna!",
      "examQuestionType": "Limites Cognitivos e Epistemologia de Nibbāna"
    },
    "es": {
      "question": "¿Cuáles Cittas NUNCA pueden tomar Lokuttara/Nibbāna como objeto?",
      "answer": "Los 12 Akusala, 18 Ahetuka, 4 Mahāvipāka sin sabiduría, 4 Mahākiriya sin sabiduría, 15 Rūpa y 12 Arūpa.\nNUNCA pueden aprehender Nibbāna.",
      "breakdown": [
        "Solo mentes con sabiduría (ñāṇasampayutta) pueden reflexionar sobre Nibbāna.",
        "El apego jamás toca la realidad incondicionada."
      ],
      "explanation": "El deseo desea el concepto de paz, pero no puede contactar a Nibbāna.",
      "mnemonicOrExamTip": "Akusala jamás tiene a Nibbāna como objeto.",
      "examQuestionType": "Límites Epistemológicos"
    }
  },
  {
    "id": "ch4-03",
    "chapter": 4,
    "chapterName": {
      "pali": "Vīthiparicchedo",
      "en": "Chapter 4: Cognitive Process",
      "pt": "Capítulo 4: Processo Cognitivo",
      "es": "Capítulo 4: Proceso Cognitivo"
    },
    "section": "Tadārammaṇa Rules",
    "category": "exam_traps",
    "paliTerm": "Tadārammaṇaniyama",
    "tags": [
      "tadarammana",
      "registration",
      "rules",
      "kama",
      "conditions"
    ],
    "en": {
      "question": "What are the 3 Strict Conditions required for Registration (Tadārammaṇa) to arise in a cognitive process?",
      "answer": "Tadārammaṇa arises ONLY when all 3 conditions are met simultaneously:\n1. The Being belongs to the Sensuous Plane (Kāmāvacara-satta - humans, devas, woeful beings; never in Brahma realms).\n2. The Javana moments are Sensuous (Kāmāvacara-javana; never after Jhāna or Supramundane javanas).\n3. The Object is a Sensuous Phenomenon of clear prominence (Kāmāvacara-ārammaṇa - Atimahanta in sense doors, Vibhūta in mind door).",
      "breakdown": [
        "If any one of these 3 conditions is missing, Tadārammaṇa CANNOT arise!",
        "Total Cittas performing Tadārammaṇa: Exactly 11 (3 Santīraṇa + 8 Mahāvipāka).",
        "Why doesn't it arise in Brahma realms? Because Brahmas lack the coarse sense-retention mechanism of sensuous beings."
      ],
      "explanation": "Tadārammaṇa acts as an echo or retention of sense data. It occurs only within the sensuous atmosphere.",
      "mnemonicOrExamTip": "Triple-Kāma Rule: Kāma Being + Kāma Javana + Kāma Object = Tadārammaṇa.",
      "examQuestionType": "Strict Cognitive Conditions"
    },
    "pt": {
      "question": "Quais são as 3 Condições Estritas necessárias para que a Retenção (Tadārammaṇa) surja num processo cognitivo?",
      "answer": "O Tadārammaṇa surge APENAS quando as 3 condições coincidem simultaneamente:\n1. O Ser pertence ao Plano Sensorial (Kāmāvacara - humanos, devas, seres inferiores; nunca nos reinos Brahma).\n2. Os Javanas são do Plano Sensorial (Kāmāvacara-javana; nunca após absorções Jhāna ou caminhos nobres).\n3. O Objeto é do Plano Sensorial de grande nitidez (Atimahanta nos sentidos, Vibhūta na mente).",
      "breakdown": [
        "Se qualquer uma das 3 faltar, o Tadārammaṇa NÃO surge!",
        "Total de Cittas que exercem Tadārammaṇa: Exatamente 11 (3 Santīraṇa + 8 Mahāvipāka).",
        "Por que não surge nos reinos de Brahma? Porque os Brahmas não possuem o mecanismo de apego residual aos estímulos sensoriais comuns."
      ],
      "explanation": "Funciona como o eco ou retentiva da experiência sensorial antes do retorno ao bhavaṅga.",
      "mnemonicOrExamTip": "Regra do Triplo-Kāma: Ser de Kāma + Javana de Kāma + Objeto de Kāma = Tadārammaṇa.",
      "examQuestionType": "Condições Estritas de Cognição"
    },
    "es": {
      "question": "¿Cuáles son las 3 condiciones indispensables para que surja Tadārammaṇa?",
      "answer": "1. Ser del plano sensorial (Kāma)\n2. Javanas del plano sensorial\n3. Objeto sensorial claro y nítido",
      "breakdown": [
        "¡Si falta cualquiera de estas 3 condiciones, Tadārammaṇa NO puede surgir!",
        "Total de Cittas que cumplen Tadārammaṇa: Exactamente 11 (3 Santīraṇa + 8 Mahāvipāka).",
        "¿Por qué no surge en los reinos de Brahma? Porque los Brahmas carecen del mecanismo de retención sensorial de los seres del plano sensual."
      ],
      "explanation": "Es el registro o eco del estímulo sensorial.",
      "mnemonicOrExamTip": "Regla del Triple Kāma.",
      "examQuestionType": "Reglas de Tadārammaṇa"
    }
  },
  {
    "id": "ch5-03",
    "chapter": 5,
    "chapterName": {
      "pali": "Vīthimuttaparicchedo",
      "en": "Chapter 5: Process-Freed",
      "pt": "Capítulo 5: Consciência Fora do Processo",
      "es": "Capítulo 5: Fuera del Proceso"
    },
    "section": "5 Anantariya Kammas",
    "category": "philosophy",
    "paliTerm": "Pañca Ānantariya Kammāni",
    "tags": [
      "anantariya",
      "heinous deeds",
      "avici",
      "kamma"
    ],
    "en": {
      "question": "What are the 5 Heinous Crimes with Immediate Retribution (Ānantariya Kamma)?",
      "answer": "The 5 Heinous Deeds:\n1. Mātu-ghāta (Matricide - killing one's mother)\n2. Pitu-ghāta (Patricide - killing one's father)\n3. Arahanta-ghāta (Killing an Arahant)\n4. Lohituppāda (Wounding a Buddha to draw blood)\n5. Saṅgha-bheda (Causing a formal schism in the monastic Saṅgha)",
      "breakdown": [
        "Category: Weightiest evil kamma (Akusala Garuka Kamma).",
        "Consequence: Guarantees rebirth in the lowest hell (Avīci) immediately in the very next life; no good kamma can obstruct it, and one is permanently barred from attaining Jhāna or Path in that life.",
        "Rankings of evil: Saṅgha-bheda is the weightiest of all five."
      ],
      "explanation": "These deeds irreparably rupture the moral fabric of consciousness, creating a gravitational pull that overrides all other karmas at death.",
      "mnemonicOrExamTip": "Exam Essential: Which of the five is the most severe? Saṅgha-bheda (schism in the Order) is the heaviest evil kamma in existence.",
      "examQuestionType": "Heinous Kamma Classification"
    },
    "pt": {
      "question": "Quais são as 5 Ações Hediondas de Retribuição Imediata (Ānantariya Kamma)?",
      "answer": "As 5 Ações Hediondas:\n1. Mātu-ghāta (Matricídio - matar a própria mãe)\n2. Pitu-ghāta (Patricídio - matar o próprio pai)\n3. Arahanta-ghāta (Matar um Arahant plenamente desperto)\n4. Lohituppāda (Ferir intencionalmente um Buda até verter sangue)\n5. Saṅgha-bheda (Causar cisma formal na Ordem Monástica / Saṅgha)",
      "breakdown": [
        "Categoria: Karma Pesado Maléfico (Akusala Garuka Kamma).",
        "Consequência: Garante renascimento inevitável no inferno mais profundo (Avīci) na vida imediatamente seguinte; impede qualquer realização de Jhāna ou Iluminação naquela existência.",
        "Hierarquia de gravidade: O cisma na Saṅgha (Saṅgha-bheda) é o mais pesado de todos os cinco."
      ],
      "explanation": "Esses atos fraturam a estrutura moral da mente de forma tão extrema que sobrepujam qualquer outra ação no momento da morte.",
      "mnemonicOrExamTip": "Pergunta de Exame: Qual das 5 ações é a mais pesada e terrível de todas? Saṅgha-bheda (provocar cisma na Saṅgha).",
      "examQuestionType": "Classificação de Karma Gravíssimo"
    },
    "es": {
      "question": "¿Cuáles son las 5 Acciones con Retribución Inmediata (Ānantariya Kamma)?",
      "answer": "1. Matar a la madre\n2. Matar al padre\n3. Matar a un Arahant\n4. Herir a un Buda\n5. Provocar un cisma en la Saṅgha (la más grave de todas).",
      "breakdown": [
        "Categoría: Kamma Perjudicial de Máximo Peso (Akusala Garuka Kamma).",
        "Consecuencia: Garantiza renacimiento inmediato en el infierno Avīci en la siguiente vida e impide alcanzar Jhāna o Iluminación en esa existencia.",
        "Jerarquía de gravedad: Provocar un cisma en la Saṅgha (Saṅgha-bheda) es el más pesado de los cinco."
      ],
      "explanation": "Los crímenes más graves de la ética budista.",
      "mnemonicOrExamTip": "Saṅgha-bheda es el acto más perjudicial de todos.",
      "examQuestionType": "Kamma Gravísimo"
    }
  },
  {
    "id": "ch7-03",
    "chapter": 7,
    "chapterName": {
      "pali": "Samuccayaparicchedo",
      "en": "Chapter 7: Categories",
      "pt": "Capítulo 7: Categorias Gerais",
      "es": "Capítulo 7: Categorías Generales"
    },
    "section": "Nibbāna in Sabbasaṅgaha",
    "category": "philosophy",
    "paliTerm": "Nibbāna Sabbasaṅgaha Placement",
    "tags": [
      "nibbana",
      "khandha",
      "ayatana",
      "dhatu",
      "sacca"
    ],
    "en": {
      "question": "How is Nibbāna classified across the 4 All-Inclusive Categories of Sabbasaṅgaha (Khandhas, Āyatanas, Dhātus, Saccas)?",
      "answer": "1. In 5 Khandhas (Aggregates): Nibbāna is EXCLUDED (Khandhavimutta - beyond aggregates, because aggregates are conditioned).\n2. In 12 Āyatanas (Bases): Classified under Dhammāyatana (Mental Base).\n3. In 18 Dhātus (Elements): Classified under Dhammadhātu (Mental Element).\n4. In 4 Ariyasaccas (Noble Truths): Classified as Nirodhasacca (The Truth of Cessation).",
      "breakdown": [
        "Why is Nibbāna excluded from Khandhas? The Buddha defined aggregates as phenomena of the past, future, or present, internal or external, gross or subtle—all conditioned marks. Nibbāna is unconditioned.",
        "In Āyatanas and Dhātus, it serves as an object for the mind element.",
        "In Noble Truths, it is the 3rd Truth: Nirodha."
      ],
      "explanation": "Mastering Nibbāna's classification across these four canonical taxonomies is a crowning question in formal Abhidhamma examinations.",
      "mnemonicOrExamTip": "Exam Favorite: Is Nibbāna included in the 5 Khandhas? NO! It is Khandhavimutta (freed from the aggregates).",
      "examQuestionType": "Doctrinal Categorization (Exam Favorite)"
    },
    "pt": {
      "question": "Como Nibbāna é classificado nas 4 Categorias Abrangentes do Sabbasaṅgaha (Khandhas, Āyatanas, Dhātus, Saccas)?",
      "answer": "1. Nos 5 Khandhas (Agregados): Nibbāna é EXCLUÍDO (Khandhavimutta - além dos agregados, pois agregados são condicionados).\n2. Nos 12 Āyatanas (Bases): Classificado em Dhammāyatana (Base dos Objetos Mentais).\n3. Nos 18 Dhātus (Elementos): Classificado em Dhammadhātu (Elemento dos Objetos Mentais).\n4. Nos 4 Ariyasaccas (Nobres Verdades): Classificado como Nirodhasacca (A Verdade da Cessação).",
      "breakdown": [
        "Por que Nibbāna não é um Khandha? O Buda definiu os agregados como tudo o que tem passado, presente, futuro, interior ou exterior—marcas do condicionado. Nibbāna é incondicionado.",
        "Em Āyatanas e Dhātus, figura como o objeto captado pela mente.",
        "Nas 4 Nobres Verdades, é a 3ª Verdade: a Cessação do Sofrimento."
      ],
      "explanation": "Compreender a localização ontológica de Nibbāna nesses 4 esquemas canônicos é prova cabal de domínio do Abhidhamma.",
      "mnemonicOrExamTip": "Pegadinha Suprema de Prova: Nibbāna está contido nos 5 Khandhas? NÃO! Nibbāna é Khandhavimutta (livre dos agregados).",
      "examQuestionType": "Classificação Doutrinária Avançada"
    },
    "es": {
      "question": "¿Cómo se clasifica Nibbāna en Khandhas, Āyatanas, Dhātus y Saccas?",
      "answer": "• 5 Khandhas: EXCLUIDO (Khandhavimutta - los agregados son condicionados; solo los 71 dhammas condicionados entran en los 5 agregados).\n• 12 Āyatanas: Incluido en Dhammāyatana.\n• 18 Dhātus: Incluido en Dhammadhātu.\n• 4 Saccas: Es la 3ª Noble Verdad (Nirodhasacca).",
      "breakdown": [
        "¿Por qué Nibbāna está excluido de los Khandhas? Porque los agregados tienen pasado, presente y futuro (marcas de lo condicionado), mientras que Nibbāna es incondicionado.",
        "En las 12 Āyatanas y los 18 Dhātus, actúa como objeto supremo de la mente.",
        "En las 4 Nobles Verdades, es la 3ª Verdad: Nirodha (Cesación)."
      ],
      "explanation": "Localización ontológica precisa de lo incondicionado.",
      "mnemonicOrExamTip": "Nibbāna es Khandhavimutta (fuera de los agregados).",
      "examQuestionType": "Clasificación de Nibbāna"
    }
  },
  {
    "id": "ch1-13",
    "chapter": 1,
    "chapterName": {
      "pali": "Cittaparicchedo",
      "en": "Chapter 1: Consciousness",
      "pt": "Capítulo 1: Consciência",
      "es": "Capítulo 1: Conciencia"
    },
    "section": "8 Lobhamūla Formulas",
    "category": "structures",
    "paliTerm": "Lobhamūla Canonical Formula",
    "tags": [
      "lobha",
      "8 cittas",
      "ditthi",
      "sankharika"
    ],
    "en": {
      "question": "Enumerate the 8 Lobhamūlacittas in standard Pali terminology.",
      "answer": "1. Somanassa-sahagataṃ diṭṭhigatasampayuttaṃ asaṅkhārikaṃ\n2. Somanassa-sahagataṃ diṭṭhigatasampayuttaṃ sasaṅkhārikaṃ\n3. Somanassa-sahagataṃ diṭṭhigatavippayuttaṃ asaṅkhārikaṃ\n4. Somanassa-sahagataṃ diṭṭhigatavippayuttaṃ sasaṅkhārikaṃ\n5. Upekkhāsahagataṃ diṭṭhigatasampayuttaṃ asaṅkhārikaṃ\n6. Upekkhāsahagataṃ diṭṭhigatasampayuttaṃ sasaṅkhārikaṃ\n7. Upekkhāsahagataṃ diṭṭhigatavippayuttaṃ asaṅkhārikaṃ\n8. Upekkhāsahagataṃ diṭṭhigatavippayuttaṃ sasaṅkhārikaṃ",
      "breakdown": [
        "1-4 are with Joy (Somanassa); 5-8 are with Equanimity (Upekkhā).",
        "1, 2, 5, 6 are Associated with Wrong View (Diṭṭhigata-sampayutta).",
        "3, 4, 7, 8 are Dissociated from Wrong View (Diṭṭhigata-vippayutta).",
        "Odd numbers (1,3,5,7) are Unprompted (Asaṅkhārika); Even numbers (2,4,6,8) are Prompted (Sasaṅkhārika)."
      ],
      "explanation": "This canonical 8-fold formula is the foundational cornerstone of Abhidhamma psychological taxonomy.",
      "mnemonicOrExamTip": "Odd = Asaṅkhārika (spontaneous); Even = Sasaṅkhārika (prompted).",
      "examQuestionType": "Pali Canonical Formulations"
    },
    "pt": {
      "question": "Enumere os 8 Lobhamūlacittas na terminologia canônica em Pāli.",
      "answer": "1. Somanassa-sahagataṃ diṭṭhigatasampayuttaṃ asaṅkhārikaṃ\n2. Somanassa-sahagataṃ diṭṭhigatasampayuttaṃ sasaṅkhārikaṃ\n3. Somanassa-sahagataṃ diṭṭhigatavippayuttaṃ asaṅkhārikaṃ\n4. Somanassa-sahagataṃ diṭṭhigatavippayuttaṃ sasaṅkhārikaṃ\n5. Upekkhāsahagataṃ diṭṭhigatasampayuttaṃ asaṅkhārikaṃ\n6. Upekkhāsahagataṃ diṭṭhigatasampayuttaṃ sasaṅkhārikaṃ\n7. Upekkhāsahagataṃ diṭṭhigatavippayuttaṃ asaṅkhārikaṃ\n8. Upekkhāsahagataṃ diṭṭhigatavippayuttaṃ sasaṅkhārikaṃ",
      "breakdown": [
        "1 a 4 com alegria (somanassa); 5 a 8 neutros (upekkhā).",
        "1, 2, 5 e 6 associados à visão errônea (sampayutta).",
        "3, 4, 7 e 8 dissociados da visão errônea (vippayutta).",
        "Ímpares (1,3,5,7) são espontâneos (asaṅkhārika); Pares (2,4,6,8) são induzidos (sasaṅkhārika)."
      ],
      "explanation": "Matriz clássica indispensável para a identificação instantânea de qualquer estado de apego.",
      "mnemonicOrExamTip": "Regra prática: Ímpares = Asaṅkhārika; Pares = Sasaṅkhārika.",
      "examQuestionType": "Fórmulas Canônicas em Pāli"
    },
    "es": {
      "question": "¿Cuáles son las 8 fórmulas canónicas de Lobhamūlacitta en Pāli?",
      "answer": "1. Somanassa + diṭṭhigatasampayutta + asaṅkhārika\n2. Somanassa + diṭṭhigatasampayutta + sasaṅkhārika\n3. Somanassa + diṭṭhigatavippayutta + asaṅkhārika\n4. Somanassa + diṭṭhigatavippayutta + sasaṅkhārika\n5. Upekkhā + diṭṭhigatasampayutta + asaṅkhārika\n6. Upekkhā + diṭṭhigatasampayutta + sasaṅkhārika\n7. Upekkhā + diṭṭhigatavippayutta + asaṅkhārika\n8. Upekkhā + diṭṭhigatavippayutta + sasaṅkhārika",
      "breakdown": [
        "1 a 4 son con alegría (somanassa); 5 a 8 son con ecuanimidad (upekkhā).",
        "1, 2, 5 y 6 están asociados con visión errónea (diṭṭhigata-sampayutta).",
        "3, 4, 7 y 8 están disociados de visión errónea (diṭṭhigata-vippayutta).",
        "Impares (1,3,5,7) son espontáneos (asaṅkhārika); Pares (2,4,6,8) son inducidos (sasaṅkhārika)."
      ],
      "explanation": "Fórmula canónica esencial del Abhidhamma.",
      "mnemonicOrExamTip": "Impar = espontáneo; Par = inducido.",
      "examQuestionType": "Fórmulas en Pāli"
    }
  },
  {
    "id": "ch2-09",
    "chapter": 2,
    "chapterName": {
      "pali": "Cetasikaparicchedo",
      "en": "Chapter 2: Mental Factors",
      "pt": "Capítulo 2: Fatores Mentais",
      "es": "Capítulo 2: Factores Mentales"
    },
    "section": "The 6 Pairs of Beautiful Universals",
    "category": "structures",
    "paliTerm": "Sobhana Yugala 6",
    "tags": [
      "sobhana",
      "yugala",
      "passaddhi",
      "lahuta",
      "muduta",
      "kammanannata"
    ],
    "en": {
      "question": "What are the 6 Pairs (Yugala) among the 19 Beautiful Universals (Sobhanasādhāraṇa)?",
      "answer": "The 6 Pairs (12 cetasikas in total):\n1. Kāya-passaddhi & Citta-passaddhi (Tranquility of mental factors & consciousness)\n2. Kāya-lahutā & Citta-lahutā (Lightness/buoyancy)\n3. Kāya-mudutā & Citta-mudutā (Malleability/pliancy)\n4. Kāya-kammaññatā & Citta-kammaññatā (Wieldiness/adaptability)\n5. Kāya-pāguññatā & Citta-pāguññatā (Proficiency/competence)\n6. Kāya-ujukatā & Citta-ujukatā (Rectitude/uprightness)",
      "breakdown": [
        "In these pairs, 'Kāya' refers to the cetasika body (nāmakāya), NOT the physical body!",
        "'Citta' refers to consciousness itself.",
        "They counteract restlessness (uddhacca), heaviness (thīna-middha), dogmatic rigidity (diṭṭhi-māna), spiritual clumsiness, and deceit (māyā-sāṭheyya)."
      ],
      "explanation": "Whenever any beautiful state arises, it is accompanied by these 12 factors providing calmness, buoyancy, plasticity, wieldiness, health, and straightforward honesty.",
      "mnemonicOrExamTip": "Exam Trap: What does 'Kāya' mean in Kāya-passaddhi? It means the mental factor aggregate (nāmakāya), NEVER the physical biological body!",
      "examQuestionType": "Analytical Anatomy of Beautiful States"
    },
    "pt": {
      "question": "Quais são os 6 Pares (Yugala) entre os 19 Universais Belos (Sobhanasādhāraṇa)?",
      "answer": "Os 6 Pares (12 cetasikas no total):\n1. Kāya-passaddhi e Citta-passaddhi (Tranquilidade dos fatores e da mente)\n2. Kāya-lahutā e Citta-lahutā (Leveza dos fatores e da mente)\n3. Kāya-mudutā e Citta-mudutā (Maleabilidade dos fatores e da mente)\n4. Kāya-kammaññatā e Citta-kammaññatā (Adequação/agilidade funcional)\n5. Kāya-pāguññatā e Citta-pāguññatā (Proficiência/competência lúcida)\n6. Kāya-ujukatā e Citta-ujukatā (Retidão/integridade dos fatores e da mente)",
      "breakdown": [
        "Nesses pares, 'Kāya' refere-se ao corpo de fatores mentais (nāmakāya), e NÃO ao corpo biológico físico!",
        "'Citta' refere-se à consciência em si.",
        "Combatem a agitação, o torpor, a rigidez dogmática, o desajeito mental e a dissimulação."
      ],
      "explanation": "Qualquer mente bela é naturalmente serena, leve, maleável, pronta para a ação ética, competente e honesta.",
      "mnemonicOrExamTip": "Pegadinha Canônica Suprema: O que significa 'Kāya' em Kāya-passaddhi? Significa o conjunto dos fatores mentais (nāmakāya), JAMAIS a carne física biológica!",
      "examQuestionType": "Anatomia dos Estados Belos"
    },
    "es": {
      "question": "¿Cuáles son los 6 Pares (Yugala) de Sobhana Cetasikas?",
      "answer": "6 Pares (12 cetasikas):\n1. Passaddhi (Tranquilidad)\n2. Lahutā (Ligereza)\n3. Mudutā (Maleabilidad)\n4. Kammaññatā (Adaptabilidad)\n5. Pāguññatā (Competencia)\n6. Ujukatā (Rectitud)\nCada uno aplicado a Kāya (factores) y Citta (conciencia).",
      "breakdown": [
        "En estos pares, 'Kāya' se refiere al cuerpo de factores mentales (nāmakāya), ¡NO al cuerpo físico!",
        "'Citta' se refiere a la conciencia en sí misma.",
        "Contrarrestan la agitación (uddhacca), pesadez (thīna-middha), rigidez (diṭṭhi-māna), torpeza espiritual y engaño."
      ],
      "explanation": "Cualidades de gracia y pureza en la mente sana.",
      "mnemonicOrExamTip": "Kāya = factores mentales, no cuerpo físico.",
      "examQuestionType": "Los 6 Pares Yugala"
    }
  },
  {
    "id": "ch3-05",
    "chapter": 3,
    "chapterName": {
      "pali": "Pakiṇṇakaparicchedo",
      "en": "Chapter 3: Miscellaneous",
      "pt": "Capítulo 3: Categorias Diversas",
      "es": "Capítulo 3: Misceláneas"
    },
    "section": "55 Javana Cittas",
    "category": "quantities",
    "paliTerm": "Javanacitta 55",
    "tags": [
      "javana",
      "55",
      "kamma",
      "merit",
      "demerit"
    ],
    "en": {
      "question": "Which 55 Consciousnesses perform the function of Javana (Impulsion)?",
      "answer": "The 55 Javana Cittas:\n• 12 Akusala Cittas (Unwholesome)\n• 1 Ahetuka Hasituppāda (Arahant's smile)\n• 8 Mahākusala (Sense-sphere wholesome)\n• 8 Mahākiriya (Sense-sphere functional of Arahants)\n• 5 Rūpāvacara Kusala + 5 Rūpāvacara Kiriya = 10\n• 4 Arūpāvacara Kusala + 4 Arūpāvacara Kiriya = 8\n• 8 or 40 Lokuttara Cittas (Supramundane paths & fruits)\nTotal: 12 + 1 + 8 + 8 + 10 + 8 + 8 = 55 (or 87 detailed).",
      "breakdown": [
        "Why are Vipāka cittas NOT javanas? Because resultants are passive fruits; Javana is active experience where kamma is created or noble fruits are savored.",
        "Hasituppāda is the ONLY ahetuka citta that can run as a javana."
      ],
      "explanation": "Javana literally means 'running swiftly'. It is the experiential heart of the cognitive process where intentional moral or immoral action is stamped into the mental continuum.",
      "mnemonicOrExamTip": "Exam Question: Can any rootless (ahetuka) citta perform javana? YES, exactly ONE: Hasituppāda (smile of the Arahant).",
      "examQuestionType": "Javana Census & Exceptions"
    },
    "pt": {
      "question": "Quais são os 55 Cittas que desempenham a função de Javana (Impulsão Cármica)?",
      "answer": "Exatamente 55 Cittas (ou 87 detalhado) operam como Javana:\n• 12 Akusala (todos os 12)\n• 1 Ahetuka Kiriya: APENAS o Hasituppāda (sorriso do Arahant)\n• 8 Mahākusala + 8 Mahākiriya (16 Kāma-sobhana)\n• 5 Rūpa Kusala + 5 Rūpa Kiriya (10 Rūpāvacara)\n• 4 Arūpa Kusala + 4 Arūpa Kiriya (8 Arūpāvacara)\n• 4 Magga + 4 Phala (8 ou 40 Lokuttara)\nTotal: 12 + 1 + 16 + 10 + 8 + 8 = 55 Cittas.",
      "breakdown": [
        "Por que os Vipākas não são javanas? Porque resultantes são frutos passivos; Javana é o momento ativo onde se planta karma novo ou se vivencia o fruto sublime da libertação.",
        "O Hasituppāda é o ÚNICO citta ahetuka que opera como javana."
      ],
      "explanation": "Javana significa 'correr velozmente'. É o ápice da experiência consciente onde a vontade livre opera.",
      "mnemonicOrExamTip": "Pergunta de Prova: Algum citta sem raiz (ahetuka) pode atuar como javana? SIM, exatamente UM: Hasituppāda.",
      "examQuestionType": "Censo dos Javanas e Exceções"
    },
    "es": {
      "question": "¿Cuáles son los 55 Javana Cittas?",
      "answer": "Exactamente 55 Cittas (u 87 detallado) operan como Javana:\n• 12 Akusala + 1 Hasituppāda + 8 Mahākusala + 8 Mahākiriya + 10 Rūpa (kusala/kiriya) + 8 Arūpa (kusala/kiriya) + 8 (o 40) Lokuttara = 55.",
      "breakdown": [
        "Fase activa de generación de kamma.",
        "Hasituppāda es el único ahetuka en javana."
      ],
      "explanation": "Donde se define la cualidad moral del acto.",
      "mnemonicOrExamTip": "Vipāka nunca es javana. Total: 55.",
      "examQuestionType": "Censo de Javana"
    }
  },
  {
    "id": "ch4-04",
    "chapter": 4,
    "chapterName": {
      "pali": "Vīthiparicchedo",
      "en": "Chapter 4: Cognitive Process",
      "pt": "Capítulo 4: Processo Cognitivo",
      "es": "Capítulo 4: Proceso Cognitivo"
    },
    "section": "4 Varieties of Five-Door Process",
    "category": "structures",
    "paliTerm": "Vīthibheda 4",
    "tags": [
      "atimahanta",
      "mahanta",
      "paritta",
      "atiparitta",
      "vithi"
    ],
    "en": {
      "question": "Name and describe the 4 Varieties of the Five-Door Cognitive Process based on object duration.",
      "answer": "The 4 Varieties:\n1. Atimahanta (Very Great Object): Reaches all the way to Tadārammaṇa (17 thought-moments full run).\n2. Mahanta (Great Object): Reaches Javana (runs 7 javanas, but no tadārammaṇa; lapses into bhavaṅga).\n3. Paritta (Slight Object): Reaches Voṭṭhabbana only (determines 2 or 3 times, but cannot trigger javana).\n4. Atiparitta (Very Slight Object): Vibrates bhavaṅga only (calana), no cognitive process arises at all.",
      "breakdown": [
        "Atimahantārammaṇa: Object is powerful and strikes at the 1st moment of bhavaṅga.",
        "Mahantārammaṇa: Object strikes after 2 or 3 moments of past bhavaṅga, leaving no time for registration.",
        "Parittārammaṇa: Weak object; mind determines what it is but fails to respond with emotional/karmic impulsion.",
        "Atiparittārammaṇa: Extremely faint stimulus; fades before the senses can advert to it."
      ],
      "explanation": "Illustrates how the intensity of a stimulus and prior attention dictate whether a sensation triggers full karmic reaction or fades unremarked.",
      "mnemonicOrExamTip": "Vīthi Horizons: Atimahanta -> Tadārammaṇa | Mahanta -> Javana | Paritta -> Voṭṭhabbana | Atiparitta -> Bhavaṅga only.",
      "examQuestionType": "Process Horizons by Intensity"
    },
    "pt": {
      "question": "Nomeie e descreva as 4 Variedades do Processo Cognitivo nas Portas dos Sentidos conforme a intensidade do objeto.",
      "answer": "As 4 Variedades:\n1. Atimahanta (Objeto Muito Grande): Completa os 17 momentos mentais, atingindo o Tadārammaṇa.\n2. Mahanta (Objeto Grande): Atinge o Javana (ocorre resposta cármica, mas sem tadārammaṇa final).\n3. Paritta (Objeto Pequeno): Atinge apenas a Determinação (Voṭṭhabbana), sem força para iniciar o Javana.\n4. Atiparitta (Objeto Muito Pequeno): Apenas oscila o bhavaṅga (calana), dissolvendo-se sem gerar percepção ativa.",
      "breakdown": [
        "Atimahanta: Impacto vigoroso desde o 1º instante do objeto.",
        "Mahanta: Chega com pequeno atraso; faltam momentos para o registro final.",
        "Paritta: A mente reconhece formalmente, mas não reage emocionalmente.",
        "Atiparitta: Estímulo tão fraco que não desperta a atenção consciente."
      ],
      "explanation": "Mostra como a mente humana filtra estímulos: nem todo ruído ou imagem gera reação cármica.",
      "mnemonicOrExamTip": "Fronteiras do Vīthi: Atimahanta -> Tadārammaṇa | Mahanta -> Javana | Paritta -> Voṭṭhabbana | Atiparitta -> Apenas bhavaṅga.",
      "examQuestionType": "Horizontes do Processo Cognitivo"
    },
    "es": {
      "question": "¿Cuáles son las 4 variedades del proceso en los sentidos por intensidad del objeto?",
      "answer": "1. Atimahanta (Muy grande): Llega a Tadārammaṇa (17 momentos).\n2. Mahanta (Grande): Llega a Javana.\n3. Paritta (Pequeño): Llega a Voṭṭhabbana (sin javana).\n4. Atiparitta (Muy pequeño): Solo sacude el bhavaṅga.",
      "breakdown": [
        "Atimahantārammaṇa: Impacto intenso desde el 1º instante de bhavaṅga.",
        "Mahantārammaṇa: Llega tras 2 o 3 momentos de bhavaṅga pasado, sin tiempo para tadārammaṇa.",
        "Parittārammaṇa: Objeto débil; la mente determina pero no genera javana.",
        "Atiparittārammaṇa: Estímulo levísimo; solo vibra el bhavaṅga sin advertencia."
      ],
      "explanation": "Filtrado cognitivo de estímulos en la mente.",
      "mnemonicOrExamTip": "Tadārammaṇa, Javana, Voṭṭhabbana, Bhavaṅga.",
      "examQuestionType": "Variedades de Vīthi"
    }
  },
  {
    "id": "ch5-04",
    "chapter": 5,
    "chapterName": {
      "pali": "Vīthimuttaparicchedo",
      "en": "Chapter 5: Process-Freed",
      "pt": "Capítulo 5: Consciência Fora do Processo",
      "es": "Capítulo 5: Fuera del Proceso"
    },
    "section": "Kamma by Time of Ripening",
    "category": "structures",
    "paliTerm": "Pākakāla Kamma 4",
    "tags": [
      "kamma",
      "ditthadhamma",
      "upapajja",
      "aparapariya",
      "ahosi"
    ],
    "en": {
      "question": "What are the 4 Kinds of Kamma by Time of Ripening (Pākakāla)?",
      "answer": "1. Diṭṭhadhamma-vedanīya (Immediately effective - ripens in this present lifetime; generated by 1st Javana).\n2. Upapajja-vedanīya (Subsequently effective - ripens in the immediately following life; generated by 7th Javana).\n3. Aparāpariya-vedanīya (Indefinitely effective - ripens in any future lifetime until Nibbāna; generated by middle 5 Javanas [2nd to 6th]).\n4. Ahosi Kamma (Defunct / Expired kamma - kamma whose window of opportunity passed without fruition).",
      "breakdown": [
        "1st Javana: Has weakest momentum, can only ripen in the current life; if it fails to ripen, it becomes Ahosi.",
        "7th Javana: Closes the active process, ripens in next life; if conditions fail, it becomes Ahosi.",
        "Middle Javanas (2-6): Carry enormous accumulative force; they NEVER expire as Ahosi until one attains final Parinibbāna!"
      ],
      "explanation": "Shows the extraordinary structural mapping of how mental moments during intention determine the temporal horizons of karmic ripening across saṃsāra.",
      "mnemonicOrExamTip": "Javana Alignment: 1st moment = Present life | 7th moment = Next life | Middle 5 moments = Any future life until Arahantship.",
      "examQuestionType": "Temporal Ripening & Javana Mechanics"
    },
    "pt": {
      "question": "Quais são os 4 Tipos de Karma quanto ao Tempo de Maturação (Pākakāla)?",
      "answer": "1. Diṭṭhadhamma-vedanīya (Maturação nesta vida presente; gerado pelo 1º Javana).\n2. Upapajja-vedanīya (Maturação na vida imediatamente seguinte; gerado pelo 7º Javana).\n3. Aparāpariya-vedanīya (Maturação em qualquer vida futura indefinida até o Nibbāna; gerado pelos 5 Javanas intermediários [2º ao 6º]).\n4. Ahosi Kamma (Karma extinto / nulo - ação cuja janela de oportunidade expirou sem maturar).",
      "breakdown": [
        "1º Javana: Menor ímpeto; só amadurece na vida presente; se não maturar, torna-se Ahosi.",
        "7º Javana: Fecha o ciclo; matura na próxima existência; se não puder, torna-se Ahosi.",
        "Javanas Intermediários (2 a 6): Força cumulativa indestrutível; NUNCA caducam até o Parinibbāna final!"
      ],
      "explanation": "Mapeamento fascinante que liga cada um dos 7 instantes de impulsão mental à amplitude temporal do karma no Saṃsāra.",
      "mnemonicOrExamTip": "Alinhamento dos Javanas: 1º momento = Esta vida | 7º momento = Próxima vida | 5 intermediários = Vidas futuras sem prazo de validade.",
      "examQuestionType": "Tempo de Maturação e Mecânica dos Javanas"
    },
    "es": {
      "question": "¿Cuáles son los 4 Tipos de Kamma por Tiempo de Maduración?",
      "answer": "1. Diṭṭhadhamma (Esta vida - 1º Javana)\n2. Upapajja (Próxima vida - 7º Javana)\n3. Aparāpariya (Vidas futuras indefinidas - Javanas 2 a 6)\n4. Ahosi (Kamma caducado que perdió vigencia)",
      "breakdown": [
        "1º Javana: El más débil; solo madura en la vida presente; si no, caduca como Ahosi.",
        "7º Javana: Cierra el proceso; madura en la próxima vida; si falla, caduca como Ahosi.",
        "Javanas intermedios (2 al 6): Fuerza acumulativa indestructible; ¡NUNCA caducan hasta el Parinibbāna final!"
      ],
      "explanation": "Relación entre micro-momentos mentales y horizontes temporales de renacimiento.",
      "mnemonicOrExamTip": "1º = Presente; 7º = Siguiente vida; 2-6 = Futuro.",
      "examQuestionType": "Maduración Temporal"
    }
  },
  {
    "id": "ch7-04",
    "chapter": 7,
    "chapterName": {
      "pali": "Samuccayaparicchedo",
      "en": "Chapter 7: Categories",
      "pt": "Capítulo 7: Categorias Gerais",
      "es": "Capítulo 7: Categorías Generales"
    },
    "section": "Ariyasacca Abhidhamma Mapping",
    "category": "philosophy",
    "paliTerm": "Cattāri Ariyasaccāni Paramattha",
    "tags": [
      "ariyasacca",
      "dukkha",
      "samudaya",
      "nirodha",
      "magga",
      "paramattha"
    ],
    "en": {
      "question": "What is the exact Ultimate Reality (Paramattha) definition of each of the Four Noble Truths (Ariyasacca)?",
      "answer": "1. Dukkhasacca (The Truth of Suffering):\nAll 81 mundane cittas + 51 cetasikas (excluding lobha/taṇhā) + all 28 rūpas.\n\n2. Samudayasacca (The Truth of the Cause of Suffering):\nTanha alone, which is ontologically LOBHA cetasika (Greed/Craving).\n\n3. Nirodhasacca (The Truth of Cessation):\nNIBBĀNA alone (the unconditioned reality).\n\n4. Maggasacca (The Truth of the Path):\nThe 8 Factors of the Noble Eightfold Path existing within the 4 Supramundane Path Consciousnesses (Maggacittas).",
      "breakdown": [
        "Notice that Lobha is extracted out of the defilements to stand alone as the 2nd Truth (Samudaya).",
        "Notice that the Supramundane Fruition consciousnesses (Phalacittas) are NOT included in the 4 Truths (they are resultant fruits of the path, not suffering, cause, cessation, or path).",
        "Suffering is not just physical pain; it is the entire totality of mundane mind and matter (5 aggregates of clinging)."
      ],
      "explanation": "This is the ultimate philosophical reduction of the Buddha's inaugural sermon at the Deer Park into exact paramattha definitions.",
      "mnemonicOrExamTip": "Exam High-Yield Point: Which cetasika is Samudayasacca? Lobha (Greed). Are Phalacittas in the 4 Truths? NO, they are outside the 4 Truths!",
      "examQuestionType": "Master Ontological Mapping of the 4 Truths"
    },
    "pt": {
      "question": "Qual é a definição exata em Realidades Últimas (Paramattha) de cada uma das Quatro Nobres Verdades (Ariyasacca)?",
      "answer": "1. Dukkhasacca (A Verdade do Sofrimento):\nTodos os 81 cittas mundanos + 51 cetasikas (excluindo lobha/taṇhā) + todos os 28 rūpas.\n\n2. Samudayasacca (A Verdade da Origem do Sofrimento):\nTaṇhā (o desejo/sede), que ontologicamente é o cetasika LOBHA (Apego/Cobiça).\n\n3. Nirodhasacca (A Verdade da Cessação):\nNIBBĀNA unicamente (o elemento incondicionado).\n\n4. Maggasacca (A Verdade do Caminho):\nOs 8 Fatores do Nobre Caminho Óctuplo presentes nos 4 Cittas do Nobre Caminho (Maggacittas).",
      "breakdown": [
        "Lobha é isolado de todos os outros fatores para constituir a 2ª Verdade (Origem).",
        "Os Cittas de Fruto Supramundano (Phalacittas) NÃO pertencem a nenhuma das 4 Nobres Verdades (são a colheita passiva do caminho, não o caminho em si nem sofrimento mundano).",
        "O sofrimento no Abhidhamma é a totalidade de toda mente e matéria mundana."
      ],
      "explanation": "A mais precisa tradução dos ensinamentos fundamentais do Buda para a gramática ontológica estrita do Abhidhamma.",
      "mnemonicOrExamTip": "Pergunta de Doutorado em Abhidhamma: Os Phalacittas fazem parte das 4 Nobres Verdades? Resposta: NÃO, eles são excluídos das 4 Nobres Verdades!",
      "examQuestionType": "Mapeamento Ontológico das 4 Nobres Verdades"
    },
    "es": {
      "question": "¿Cómo se definen las Cuatro Nobles Verdades en términos de Paramattha Dhammas?",
      "answer": "1. Dukkha: 81 cittas mundanos + 51 cetasikas + 28 rūpas.\n2. Samudaya: Cetasika LOBHA (apego/deseo).\n3. Nirodha: NIBBĀNA.\n4. Magga: Los 8 factores del Óctuple Sendero en los 4 Maggacittas.",
      "breakdown": [
        "Lobha se extrae de las impurezas para constituir por sí solo la 2ª Noble Verdad (Samudaya).",
        "Los Cittas de Fruto Supramundano (Phalacittas) NO están incluidos en ninguna de las 4 Nobles Verdades (son frutos resultantes, no sufrimiento ni sendero).",
        "El sufrimiento abarca la totalidad de la mente y materia mundanas (los 5 agregados de apego)."
      ],
      "explanation": "Traducción analítica definitiva del Dharma.",
      "mnemonicOrExamTip": "Phalacitta queda fuera de las 4 Nobles Verdades.",
      "examQuestionType": "Las 4 Nobles Verdades en Paramattha"
    }
  },
  {
    "id": "ch8-03",
    "chapter": 8,
    "chapterName": {
      "pali": "Paccayaparicchedo",
      "en": "Chapter 8: Conditionality",
      "pt": "Capítulo 8: Condicionalidade",
      "es": "Capítulo 8: Condicionalidad"
    },
    "section": "Paṭiccasamuppāda 20 Modes & 3 Sandhi",
    "category": "structures",
    "paliTerm": "Paṭiccasamuppāda 20 Ākārā",
    "tags": [
      "paticcasamuppada",
      "20 akara",
      "sandhi",
      "connections",
      "vatta"
    ],
    "en": {
      "question": "What are the 3 Connections (Sandhi) and 4 Groups (Saṅkhepa) of Dependent Arising?",
      "answer": "The 3 Connections (Sandhi):\n1. Past Cause to Present Result (Between Saṅkhāra and Viññāṇa)\n2. Present Result to Present Cause (Between Vedanā and Taṇhā)\n3. Present Cause to Future Result (Between Bhava and Jāti)\n\nThe 4 Groups (Saṅkhepa):\n1. Past Causes: Avijjā, Saṅkhāra (plus implied Taṇhā, Upādāna, Bhava)\n2. Present Results: Viññāṇa, Nāmarūpa, Saḷāyatana, Phassa, Vedanā\n3. Present Causes: Taṇhā, Upādāna, Bhava (plus implied Avijjā, Saṅkhāra)\n4. Future Results: Jāti, Jarāmaraṇa (representing the 5 fruits)",
      "breakdown": [
        "Each causal group contains 5 factors, creating the 20 Modes (Ākārā):",
        "5 Past Causes + 5 Present Fruits + 5 Present Causes + 5 Future Fruits = 20 Modes.",
        "The 2nd connection (between Vedanā and Taṇhā) is the CRITICAL JUNCTURE where mindfulness can intervene to break the cycle of suffering!"
      ],
      "explanation": "Shows the exact mechanics of how past deeds generate present consciousness, and how present reaction dictates future rebirth.",
      "mnemonicOrExamTip": "Vipassanā Leverage Point: Where can the wheel of Dependent Arising be broken? Exactly at the second Sandhi: between Vedanā (Feeling) and Taṇhā (Craving)!",
      "examQuestionType": "Dependent Origination Structural Topology"
    },
    "pt": {
      "question": "Quais são as 3 Conexões (Sandhi) e os 4 Grupos (Saṅkhepa) da Originação Dependente?",
      "answer": "As 3 Conexões (Sandhi):\n1. Da Causa Passada ao Fruto Presente (Entre Saṅkhāra e Viññāṇa)\n2. Do Fruto Presente à Causa Presente (Entre Vedanā e Taṇhā)\n3. Da Causa Presente ao Fruto Futuro (Entre Bhava e Jāti)\n\nOs 4 Grupos (Saṅkhepa):\n1. Causas Passadas (5 fatores)\n2. Frutos Presentes (5 fatores)\n3. Causas Presentes (5 fatores)\n4. Frutos Futuros (5 fatores)",
      "breakdown": [
        "Cada grupo causal contém 5 fatores, estruturando os 20 Modos (Ākārā):",
        "5 Causas Passadas + 5 Frutos Presentes + 5 Causas Presentes + 5 Frutos Futuros = 20 Modos.",
        "A 2ª conexão (entre Sensação e Desejo) é o PONTO DE RUPTURA onde a atenção plena pode cortar a reação e cessar o renascimento!"
      ],
      "explanation": "A anatomia detalhada do mecanismo que acorrenta a consciência ao ciclo de vidas.",
      "mnemonicOrExamTip": "Ponto de Libertação Prática: Onde a roda do Paṭiccasamuppāda é cortada pelo praticante de meditação? Entre Vedanā (Sensação) e Taṇhā (Desejo)!",
      "examQuestionType": "Topologia Estrutural do Paṭiccasamuppāda"
    },
    "es": {
      "question": "¿Cuáles son las 3 Conexiones (Sandhi) y dónde se corta la rueda del Paṭiccasamuppāda?",
      "answer": "3 Conexiones: 1. Saṅkhāra a Viññāṇa, 2. Vedanā a Taṇhā, 3. Bhava a Jāti.\nSe corta ÚNICAMENTE en la 2ª conexión: entre Vedanā (sensación) y Taṇhā (deseo).",
      "breakdown": [
        "Cada grupo causal contiene 5 factores, formando los 20 Modos (Ākārā):",
        "5 Causas Pasadas + 5 Frutos Presentes + 5 Causas Presentes + 5 Frutos Futuros = 20 Modos.",
        "La 2ª conexión (entre Vedanā y Taṇhā) es el PUNTO CRÍTICO donde la atención plena corta el ciclo del renacimiento."
      ],
      "explanation": "Clave soteriológica del budismo.",
      "mnemonicOrExamTip": "Corte de la rueda: Entre Vedanā y Taṇhā.",
      "examQuestionType": "Conexiones de Paṭiccasamuppāda"
    }
  },
  {
    "id": "ch9-05",
    "chapter": 9,
    "chapterName": {
      "pali": "Kammaṭṭhānaparicchedo",
      "en": "Chapter 9: Meditation",
      "pt": "Capítulo 9: Meditação e Libertação",
      "es": "Capítulo 9: Meditación y Liberación"
    },
    "section": "6 Temperaments & Objects",
    "category": "structures",
    "paliTerm": "Caritabhedo 6",
    "tags": [
      "carita",
      "temperament",
      "personality",
      "samatha",
      "objects"
    ],
    "en": {
      "question": "What are the 6 Temperaments (Carita) and their matching meditation subjects in the Abhidhamma?",
      "answer": "The 6 Temperaments & Suitable Subjects:\n1. Rāga-carita (Lustful / Sensual): 10 Asubhas (foulness of corpses) & Kāyagatāsati (32 parts of the body).\n2. Dosa-carita (Hateful / Aversive): 4 Brahmavihāras (especially Metta) & the 4 Color Kasiṇas (blue, yellow, red, white).\n3. Moha-carita (Deluded / Dull): Ānāpānasati (Mindfulness of Breathing) to anchor wandering awareness.\n4. Saddhā-carita (Devotional / Faithful): The 6 Recollections (Buddha, Dhamma, Saṅgha, Sīla, Cāga, Devas).\n5. Buddhi-carita (Intellectual / Wise): Recollection of Death, Peace of Nibbāna, Loathsomeness of Food, and Analysis of the 4 Elements.\n6. Vitakka-carita (Discursive / Agitated): Ānāpānasati (Breathing) to cut mental proliferation.",
      "breakdown": [
        "Notice that Ānāpānasati is the medicine for BOTH Moha (delusion) and Vitakka (discursive agitation).",
        "Color kasiṇas soothe hatred with their serene, uniform visual beauty."
      ],
      "explanation": "Psychotherapeutic classification matching individual personality traits to specific meditation remedies.",
      "mnemonicOrExamTip": "Exam Match: What is the primary object for a person dominated by Hatred (dosa)? Metta and the 4 Color Kasiṇas!",
      "examQuestionType": "Personality & Meditation Prescription"
    },
    "pt": {
      "question": "Quais são os 6 Tipamentos de Caráter (Carita) e os temas de meditação correspondentes no Abhidhamma?",
      "answer": "Os 6 Tipos de Caráter e seus Objetos Adequados:\n1. Rāga-carita (Apego/Sensual): 10 Asubhas (decomposição cadavérica) e Atenção às 32 partes do corpo.\n2. Dosa-carita (Aversivo/Irado): 4 Brahmavihāras (especialmente Metta) e os 4 Kasiṇas de Cor (azul, amarelo, vermelho e branco).\n3. Moha-carita (Iludido/Confuso): Ānāpānasati (Atenção à Respiração) para ancorar a mente dispersa.\n4. Saddhā-carita (Devocional/Fiel): As 6 Recordações (Buda, Dhamma, Saṅgha, Virtude, Generosidade e Devas).\n5. Buddhi-carita (Intelectual/Analítico): Recordação da Morte, Paz de Nibbāna, Repugnância no Alimento e Análise dos 4 Elementos.\n6. Vitakka-carita (Discursivo/Agitado): Ānāpānasati (Respiração) para silenciar o excesso de pensamentos.",
      "breakdown": [
        "Atenção à respiração cura tanto a confusão (moha) quanto o pensamento incessante (vitakka).",
        "Os Kasiṇas de cores suaves acalmam a irritação da aversão."
      ],
      "explanation": "Prescrição psicológica e terapêutica tradicional do Abhidhamma e Visuddhimagga.",
      "mnemonicOrExamTip": "Questão Clássica: Qual o remédio meditativo para quem tem temperamento de aversão/raiva (dosa)? Metta e Kasiṇas de cor!",
      "examQuestionType": "Temperamentos e Prescrição Meditativa"
    },
    "es": {
      "question": "¿Cuáles son los 6 Temperamentos (Carita) y sus temas de meditación?",
      "answer": "1. Apego (Rāga) -> Asubha y 32 partes del cuerpo.\n2. Aversión (Dosa) -> Metta y 4 Kasiṇas de color.\n3. Confusión (Moha) -> Respiración (Ānāpāna).\n4. Fe (Saddhā) -> 6 Recordaciones.\n5. Sabiduría (Buddhi) -> Muerte, Nibbāna, 4 elementos.\n6. Pensamiento excesivo (Vitakka) -> Respiración (Ānāpāna).",
      "breakdown": [
        "La respiración cura la confusión y la dispersión mental.",
        "Metta cura la aversión."
      ],
      "explanation": "Medicina meditativa personalizada.",
      "mnemonicOrExamTip": "Dosa = Metta y Kasiṇas de color. Moha/Vitakka = Respiración.",
      "examQuestionType": "Temperamentos y Kammaṭṭhāna"
    }
  },
  {
    "id": "ch1-14",
    "chapter": 1,
    "chapterName": {
      "pali": "Cittaparicchedo",
      "en": "Chapter 1: Consciousness",
      "pt": "Capítulo 1: Consciência",
      "es": "Capítulo 1: Conciencia"
    },
    "section": "Dosamūla & Mohamūla Formulas",
    "category": "structures",
    "paliTerm": "Dosa & Moha Formulas",
    "tags": [
      "dosa",
      "moha",
      "patigha",
      "vicikiccha",
      "uddhacca"
    ],
    "en": {
      "question": "What are the exact Pali formulas of the 2 Dosamūlacittas and 2 Mohamūlacittas?",
      "answer": "Dosamūlacittas (2):\n1. Domanassa-sahagataṃ paṭighasampayuttaṃ asaṅkhārikaṃ\n2. Domanassa-sahagataṃ paṭighasampayuttaṃ sasaṅkhārikaṃ\n\nMohamūlacittas (2):\n1. Upekkhā-sahagataṃ vicikicchāsampayuttaṃ\n2. Upekkhā-sahagataṃ uddhaccasampayuttaṃ",
      "breakdown": [
        "Dosamūla feeling is ALWAYS Domanassa (mental displeasure); association is ALWAYS Paṭigha (aversion/ill-will).",
        "Mohamūla feeling is ALWAYS Upekkhā (equanimity/neutrality); neither has prompted/unprompted divisions."
      ],
      "explanation": "Hatred burns with grief and aversion. Pure delusion is blind, numb, and uncertain, lacking the sharp clarity needed for anger or greed.",
      "mnemonicOrExamTip": "Exam Question: Why does mohamūlacitta lack prompted/unprompted variations? Because delusion is inherently dull and hesitating; it cannot be persuaded or prompted.",
      "examQuestionType": "Canonical Formulas & Core Logic"
    },
    "pt": {
      "question": "Quais são as fórmulas canônicas exatas dos 2 Dosamūlacittas e 2 Mohamūlacittas?",
      "answer": "Dosamūlacittas (2):\n1. Domanassa-sahagataṃ paṭighasampayuttaṃ asaṅkhārikaṃ\n2. Domanassa-sahagataṃ paṭighasampayuttaṃ sasaṅkhārikaṃ\n\nMohamūlacittas (2):\n1. Upekkhā-sahagataṃ vicikicchāsampayuttaṃ\n2. Upekkhā-sahagataṃ uddhaccasampayuttaṃ",
      "breakdown": [
        "A sensação de Dosa é SEMPRE Domanassa (desprazer); a associação é SEMPRE Paṭigha (aversão).",
        "A sensação de Moha é SEMPRE Upekkhā (neutra); nenhum possui variantes induzidas."
      ],
      "explanation": "A aversão queima com aflição. A ilusão pura é cega, hesitante e apática, sem o foco necessário para a ira ou o apego.",
      "mnemonicOrExamTip": "Pegadinha de Exame: Por que o mohamūla não se divide em espontâneo e induzido? Porque a cegueira da ignorância é passiva e inerte.",
      "examQuestionType": "Fórmulas Canônicas e Lógica Central"
    },
    "es": {
      "question": "¿Cuáles son las fórmulas canónicas de los 2 Dosamūlacittas y 2 Mohamūlacittas?",
      "answer": "Dosa (2): Domanassa + paṭighasampayutta + asaṅkhārika / sasaṅkhārika.\nMoha (2): Upekkhā + vicikicchā / uddhacca.",
      "breakdown": [
        "Dosa siempre es domanassa y paṭigha.",
        "Moha siempre es upekkhā."
      ],
      "explanation": "Estructuras fijas de aversión e ignorancia.",
      "mnemonicOrExamTip": "Dosa = domanassa; Moha = upekkhā.",
      "examQuestionType": "Fórmulas en Pāli"
    }
  },
  {
    "id": "ch4-05",
    "chapter": 4,
    "chapterName": {
      "pali": "Vīthiparicchedo",
      "en": "Chapter 4: Cognitive Process",
      "pt": "Capítulo 4: Processo Cognitivo",
      "es": "Capítulo 4: Proceso Cognitivo"
    },
    "section": "Deathbed Javana Rule",
    "category": "exam_traps",
    "paliTerm": "Maraṇāsanna Javana 5",
    "tags": [
      "javana",
      "death",
      "maranasanna",
      "5 moments"
    ],
    "en": {
      "question": "How many Javana moments occur in the Near-Death Cognitive Process (Maraṇāsannavīthi) compared to normal cognitive processes?",
      "answer": "Normally: 7 Javana moments.\nAt Death (Maraṇāsanna): ONLY 5 Javana moments!\n(Also in fainting or states of extreme weakness, javanas run only 5 times).",
      "breakdown": [
        "Due to the physical exhaustion of the heart-base (hadayavatthu) and failing life faculty at the end of life, the mind lacks the vitality to sustain the full 7 impulse moments.",
        "The 5th death javana concludes the active karmic phase; immediately thereafter, cuti (death consciousness) arises."
      ],
      "explanation": "This physiological and psychological weakening at the moment of death demonstrates the rigorous realism of Abhidhamma psycho-physics.",
      "mnemonicOrExamTip": "Exam High-Yield Rule: Normal life = 7 Javanas. Deathbed process = 5 Javanas. First Jhāna attainment = 1 Javana.",
      "examQuestionType": "Javana Moment Rules"
    },
    "pt": {
      "question": "Quantos momentos de Javana ocorrem no Processo Cognitivo de Morte (Maraṇāsannavīthi) em comparação com o processo normal?",
      "answer": "No fluxo normal: 7 momentos de Javana.\nNo momento da Morte (Maraṇāsanna): APENAS 5 momentos de Javana!\n(Também em desmaios ou debilidade extrema o javana ocorre apenas 5 vezes).",
      "breakdown": [
        "Devido ao enfraquecimento da base do coração e da faculdade da vida física, a mente não tem energia biológica para sustentar 7 impulsos.",
        "O 5º javana encerra o ciclo de karma ativo daquela vida; logo a seguir surge o cuti (morte)."
      ],
      "explanation": "O realismo do Abhidhamma registra o declínio bio-psíquico na transição da morte.",
      "mnemonicOrExamTip": "Regra Canônica de Javanas: Vida normal = 7 Javanas. Leito de morte = 5 Javanas. Primeira absorção Jhāna = 1 Javana.",
      "examQuestionType": "Regras Temporais de Javana"
    },
    "es": {
      "question": "¿Cuántos momentos de Javana ocurren en el proceso de muerte (Maraṇāsanna)?",
      "answer": "En la muerte ocurren solo 5 momentos de Javana (frente a los 7 normales).",
      "breakdown": [
        "Por debilidad del soporte físico del corazón.",
        "Normal = 7; Muerte = 5; Primer Jhāna = 1."
      ],
      "explanation": "Agotamiento de la energía biológica antes del cese.",
      "mnemonicOrExamTip": "Muerte = 5 Javanas.",
      "examQuestionType": "Javanas en la Muerte"
    }
  },
  {
    "id": "ch5-05",
    "chapter": 5,
    "chapterName": {
      "pali": "Vīthimuttaparicchedo",
      "en": "Chapter 5: Process-Freed",
      "pt": "Capítulo 5: Consciência Fora do Processo",
      "es": "Capítulo 5: Fuera del Proceso"
    },
    "section": "31 Planes of Existence",
    "category": "structures",
    "paliTerm": "Ekatiṃsa Bhūmi 31",
    "tags": [
      "bhumi",
      "31 planes",
      "apaya",
      "kama",
      "rupa",
      "arupa"
    ],
    "en": {
      "question": "Enumerate the 31 Planes of Existence (Ekatiṃsa Bhūmi) in the Buddhist cosmos.",
      "answer": "The 31 Planes:\n1. 4 Apāya (Woeful realms: Hell/Niraya, Animal, Ghost/Peta, Titan/Asura)\n2. 7 Kāmasugati (Sensuous Blissful: Human + 6 Deva realms [Cātumahārājikā, Tāvatiṃsa, Yāmā, Tusita, Nimmānarati, Paranimmitavasavattī])\n[1-11 = 11 Kāmaphūmi]\n3. 16 Rūpabhūmi (Fine-material Brahma realms: 3 1st Jhāna, 3 2nd Jhāna, 3 3rd Jhāna, 7 4th Jhāna including Asaññasatta and 5 Suddhāvāsa Pure Abodes)\n4. 4 Arūpabhūmi (Immaterial realms: Infinite Space, Consciousness, Nothingness, Neither-Perception)\nTotal: 11 + 16 + 4 = 31 Planes.",
      "breakdown": [
        "Asaññasatta: In this realm, Brahmas possess ONLY physical matter and ZERO consciousness for 500 great eons!",
        "Suddhāvāsa (5 Pure Abodes): Rebirth exclusively for Non-Returners (Anāgāmīs) who achieve final Parinibbāna there."
      ],
      "explanation": "The 31 planes correspond directly to psychological states of consciousness (Kāma, Rūpa, Arūpa jhānas). Rebirth in each realm is the exact karmic fruit of mental culture.",
      "mnemonicOrExamTip": "Exam Question: In which plane do beings exist with ONLY matter and NO consciousness? Answer: Asaññasatta (Non-percipient realm).",
      "examQuestionType": "Cosmological Architecture"
    },
    "pt": {
      "question": "Enumere os 31 Planos de Existência (Ekatiṃsa Bhūmi) no cosmos budista.",
      "answer": "Os 31 Planos:\n1. 4 Apāya (Reinos inferiores: Inferno/Niraya, Animais, Fantasmas Famintos/Peta, Asuras)\n2. 7 Kāmasugati (Reinos Felizes Sensoriais: Humano + 6 Devas celestiais)\n[1 a 11 = 11 Planos Sensoriais]\n3. 16 Rūpabhūmi (Reinos Brahma da Forma Sutil: 3 do 1º Jhāna, 3 do 2º, 3 do 3º, 7 do 4º Jhāna incluindo Asaññasatta e as 5 Moradas Puras/Suddhāvāsa)\n4. 4 Arūpabhūmi (Reinos Imateriais: Espaço, Consciência, Nada e Nem-Percepção)\nTotal: 11 + 16 + 4 = 31 Planos.",
      "breakdown": [
        "Asaññasatta: Reino onde os seres têm APENAS corpo material e ZERO mente por 500 grandes eras!",
        "Suddhāvāsa (5 Moradas Puras): Destino exclusivo de Não-Retornantes (Anāgāmīs)."
      ],
      "explanation": "A cosmologia budista reflete diretamente os estados meditativos da mente.",
      "mnemonicOrExamTip": "Pergunta de Prova Clássica: Em qual reino os seres possuem apenas matéria e nenhuma mente? Resposta: Asaññasatta.",
      "examQuestionType": "Arquitetura Cosmológica"
    },
    "es": {
      "question": "¿Cuáles son los 31 Planos de Existencia?",
      "answer": "11 Planos Sensoriales (4 inferiores + 1 humano + 6 devas) + 16 Planos de Forma (Rūpa) + 4 Planos Inmateriales (Arūpa) = 31.",
      "breakdown": [
        "Asaññasatta: Solo materia sin mente.",
        "Suddhāvāsa: 5 Moradas Puras de Anāgāmīs."
      ],
      "explanation": "Cosmología basada en niveles de conciencia.",
      "mnemonicOrExamTip": "Asaññasatta = Solo cuerpo, sin mente.",
      "examQuestionType": "Los 31 Planos"
    }
  },
  {
    "id": "ch6-05",
    "chapter": 6,
    "chapterName": {
      "pali": "Rūpaparicchedo",
      "en": "Chapter 6: Matter & Nibbāna",
      "pt": "Capítulo 6: Matéria e Nibbāna",
      "es": "Capítulo 6: Materia y Nibbāna"
    },
    "section": "4 Origins of Matter Counts",
    "category": "quantities",
    "paliTerm": "Rūpasamuṭṭhāna Counts",
    "tags": [
      "samutthana",
      "kammaja",
      "cittaja",
      "utuja",
      "aharaja",
      "rupa"
    ],
    "en": {
      "question": "How many Rūpas are produced by each of the 4 Origins of Matter (Samuṭṭhāna)?",
      "answer": "• Kamma-born (Kammaja): Produces 18 Rūpas\n• Mind-born (Cittaja): Produces 15 Rūpas\n• Temperature-born (Utuja): Produces 13 Rūpas\n• Nutriment-born (Āhāraja): Produces 12 Rūpas",
      "breakdown": [
        "Kammaja (18): 8 inseparables (suddhaṭṭhaka) + life faculty + 5 sensitive matters (pasāda) + 2 sex matters + heart-base + space.",
        "Cittaja (15): 8 inseparables + space + 2 intimations (body/speech) + 3 mutabilities (lightness, pliancy, wieldiness) + sound (speech).",
        "Utuja (13): 8 inseparables + space + sound (natural sounds) + 3 mutabilities.",
        "Āhāraja (12): 8 inseparables + space + 3 mutabilities."
      ],
      "explanation": "Every physical quality in the organism has a specific generative condition. Some (like eye sensitivity and heart base) can only be generated by past kamma.",
      "mnemonicOrExamTip": "Exam Counts: Kamma 18 | Citta 15 | Utu 13 | Āhāra 12.",
      "examQuestionType": "Material Origins Quantitative Breakdown"
    },
    "pt": {
      "question": "Quantos Rūpas são produzidos por cada uma das 4 Origens da Matéria (Samuṭṭhāna)?",
      "answer": "• Gerados pelo Karma (Kammaja): Produz 18 Rūpas\n• Gerados pela Mente (Cittaja): Produz 15 Rūpas\n• Gerados pela Temperatura (Utuja): Produz 13 Rūpas\n• Gerados pelo Alimento (Āhāraja): Produz 12 Rūpas",
      "breakdown": [
        "Kammaja (18): 8 inseparáveis + vida física + 5 sensibilidades sensoriais + 2 sexos + coração + espaço.",
        "Cittaja (15): 8 inseparáveis + espaço + 2 comunicações (gesto/fala) + 3 mutabilidades + som.",
        "Utuja (13): 8 inseparáveis + espaço + som (sons naturais) + 3 mutabilidades.",
        "Āhāraja (12): 8 inseparáveis + espaço + 3 mutabilidades."
      ],
      "explanation": "A sensibilidade visual e o órgão do coração só podem ser formados pelo karma, enquanto gestos corporais e fala consciente são gerados pela mente presente.",
      "mnemonicOrExamTip": "Fórmula Numérica de Prova: Karma = 18 | Mente = 15 | Temperatura = 13 | Alimento = 12.",
      "examQuestionType": "Contagem das 4 Origens da Matéria"
    },
    "es": {
      "question": "¿Cuántos Rūpas produce cada uno de los 4 Orígenes de la Materia?",
      "answer": "Kamma = 18 | Citta = 15 | Utu = 13 | Āhāra = 12.",
      "breakdown": [
        "Kammaja (18): 8 inseparables (suddhaṭṭhaka) + vida física + 5 sensibilidades + 2 sexos + corazón + espacio.",
        "Cittaja (15): 8 inseparables + espacio + 2 intimaciones (gesto/habla) + 3 mutabilidades + sonido.",
        "Utuja (13): 8 inseparables + espacio + sonido (sonidos naturales) + 3 mutabilidades.",
        "Āhāraja (12): 8 inseparables + espacio + 3 mutabilidades."
      ],
      "explanation": "Causalidad física precisa.",
      "mnemonicOrExamTip": "18, 15, 13, 12.",
      "examQuestionType": "Orígenes de Rūpa"
    }
  },
  {
    "id": "ch9-06",
    "chapter": 9,
    "chapterName": {
      "pali": "Kammaṭṭhānaparicchedo",
      "en": "Chapter 9: Meditation",
      "pt": "Capítulo 9: Meditação e Libertação",
      "es": "Capítulo 9: Meditación y Liberación"
    },
    "section": "3 Nimittas of Meditation",
    "category": "structures",
    "paliTerm": "Nimittabhedo 3",
    "tags": [
      "nimitta",
      "parikamma",
      "uggaha",
      "patibhaga",
      "samatha"
    ],
    "en": {
      "question": "What are the 3 Meditation Signs (Nimitta) in the progression of Samatha meditation?",
      "answer": "The 3 Signs:\n1. Parikamma-nimitta (Preliminary Sign): The physical, raw external object as observed by the open eye (e.g., the physical colored disc of a kasiṇa or the breath at the nostrils).\n2. Uggaha-nimitta (Acquired / Learning Sign): The mental copy or internalized mental image seen with closed eyes; it retains flaws, edges, and textures of the physical object.\n3. Paṭibhāga-nimitta (Counterpart Sign): The radiant, purified mental counterpart; completely devoid of material flaws, shining like a polished mother-of-pearl or clear crystal disc, born of pure concentration.",
      "breakdown": [
        "Parikamma-nimitta -> Preliminary concentration (Parikammabhāvanā).",
        "Uggaha-nimitta -> Access concentration (Upacārabhāvanā).",
        "Paṭibhāga-nimitta -> Fixed absorption (Appanābhāvanā / Jhāna!).",
        "The Paṭibhāganimitta is an Atthapaññatti (a conceptual mental sign)."
      ],
      "explanation": "The transition from physical object to internalized mental image, and from mental image to radiant concept, marks the ascension from sensuous dispersion into absorption.",
      "mnemonicOrExamTip": "Exam Essential: At which sign does Jhāna absorption arise? ONLY at the Paṭibhāga-nimitta (Counterpart sign)!",
      "examQuestionType": "Progressive Meditation Signs"
    },
    "pt": {
      "question": "Quais são os 3 Sinais Meditativos (Nimitta) na progressão de Samatha?",
      "answer": "Os 3 Sinais:\n1. Parikamma-nimitta (Sinal Preliminar): O objeto físico exterior observado pelos olhos abertos (ex.: o disco de terra/cor do kasiṇa ou o toque físico da respiração).\n2. Uggaha-nimitta (Sinal Adquirido / Aprendido): A imagem mental internalizada vista de olhos fechados; retém as imperfeições e textura do objeto físico.\n3. Paṭibhāga-nimitta (Sinal de Contraparte): O sinal mental radiante e purificado; translúcido, brilhante como cristal ou madrepérola, desprovido de qualquer defeito físico, fruto da concentração profunda.",
      "breakdown": [
        "Parikamma-nimitta -> Concentração preliminar.",
        "Uggaha-nimitta -> Concentração de acesso (upacāra).",
        "Paṭibhāga-nimitta -> Absorção plena (Appanā / Jhāna!).",
        "O Paṭibhāganimitta é uma Atthapaññatti (conceito puro da mente)."
      ],
      "explanation": "Descreve a transformação do estímulo físico externo em uma representação mental pura que permite a unificação meditativa.",
      "mnemonicOrExamTip": "Pergunta Decisiva de Prova: Em qual sinal emerge o Jhāna? EXCLUSIVAMENTE sobre o Paṭibhāga-nimitta!",
      "examQuestionType": "Sinais Meditativos Progressivos"
    },
    "es": {
      "question": "¿Cuáles son los 3 Signos (Nimitta) de la Meditación Samatha?",
      "answer": "1. Parikamma-nimitta (Objeto físico externo)\n2. Uggaha-nimitta (Imagen mental interna con imperfecciones)\n3. Paṭibhāga-nimitta (Signo de contraparte radiante y purificado)",
      "breakdown": [
        "Parikamma-nimitta -> Concentración preliminar (Parikammabhāvanā).",
        "Uggaha-nimitta -> Concentración de acceso (Upacārabhāvanā).",
        "Paṭibhāga-nimitta -> Absorción plena (Appanābhāvanā / ¡Jhāna!).",
        "El Paṭibhāganimitta es un concepto mental puro (Atthapaññatti)."
      ],
      "explanation": "Evolución de la concentración hacia la absorción.",
      "mnemonicOrExamTip": "Jhāna surge en Paṭibhāga-nimitta.",
      "examQuestionType": "Nimittas de Meditación"
    }
  },
  {
    "id": "ch1-15",
    "chapter": 1,
    "chapterName": {
      "pali": "Cittaparicchedo",
      "en": "Chapter 1: Consciousness",
      "pt": "Capítulo 1: Consciência",
      "es": "Capítulo 1: Conciencia"
    },
    "section": "Somanassa in 62 Cittas",
    "category": "quantities",
    "paliTerm": "Somanassa 62",
    "tags": [
      "somanassa",
      "feeling",
      "62 cittas",
      "joy"
    ],
    "en": {
      "question": "Which 62 Consciousnesses arise with Joy / Mental Pleasure (Somanassa)?",
      "answer": "In the 121 scheme, exactly 62 Cittas have Somanassa:\n• 4 Lobhamūlacittas (the 4 somanassa greed minds)\n• 1 Kusalavipāka Santīraṇa (investigating with joy)\n• 1 Hasituppāda (Arahant's smile)\n• 4 Mahākusala (wholesome with joy)\n• 4 Mahāvipāka (resultant with joy)\n• 4 Mahākiriya (functional with joy)\n• 12 Rūpāvacara (1st, 2nd, 3rd, 4th Jhānas: 4 jhānas × 3 classes [kusala, vipāka, kiriya] = 12)\n• 32 Lokuttara (1st, 2nd, 3rd, 4th Jhāna paths & fruits: 4 jhānas × 8 = 32)\nTotal: 4 + 1 + 1 + 4 + 4 + 4 + 12 + 32 = 62 Cittas.",
      "breakdown": [
        "In the 5-fold Jhāna system (Pañcakanaya), the 4th Jhāna drops Pīti (rapture) but RETAINS Sukha/Somanassa (pleasant feeling); only in the 5th Jhāna is Somanassa replaced by Upekkhā.",
        "Contrast Somanassa (62 cittas, 1st–4th jhānas) with Sapītika / Pīti (51 cittas: 18 kāma + 9 rūpa [1st–3rd jhānas] + 24 lokuttara [1st–3rd jhānas])."
      ],
      "explanation": "Calculates every joyful state in the entire Theravāda psychological taxonomy and distinguishes feeling (somanassa = 62) from rapture (pīti = 51).",
      "mnemonicOrExamTip": "Calculation: 18 Kāma (4+2+12) + 12 Rūpa (4×3) + 32 Lokuttara (4×8) = 62 Somanassa Cittas (vs. 51 Sapītika Cittas).",
      "examQuestionType": "Feeling Distribution Calculus"
    },
    "pt": {
      "question": "Quais são os 62 Cittas que surgem com Alegria Mental (Somanassa)?",
      "answer": "No esquema de 121 cittas, exatamente 62 possuem Somanassa:\n• 4 Lobhamūlacittas (com alegria)\n• 1 Kusalavipāka Santīraṇa (investigação alegre)\n• 1 Hasituppāda (sorriso do Arahant)\n• 4 Mahākusala (hábeis alegres)\n• 4 Mahāvipāka (resultantes alegres)\n• 4 Mahākiriya (funcionais alegres)\n• 12 Rūpāvacara (1º, 2º, 3º e 4º Jhānas: 4 jhānas × 3 classes [kusala, vipāka, kiriya] = 12)\n• 32 Lokuttara (1º ao 4º Jhāna: 4 jhānas × 8 = 32)\nTotal: 4 + 1 + 1 + 4 + 4 + 4 + 12 + 32 = 62 Cittas.",
      "breakdown": [
        "No sistema quíntuplo (Pañcakanaya), o 4º Jhāna abandona Pīti (êxtase), mas MANTÉM Sukha/Somanassa (felicidade); somente no 5º Jhāna a alegria é substituída por Upekkhā (equanimidade).",
        "Contraste Somanassa (62 cittas, 1º ao 4º jhānas) com Sapītika / Pīti (51 cittas: 18 kāma + 9 rūpa [1º–3º jhānas] + 24 lokuttara [1º–3º jhānas])."
      ],
      "explanation": "Mapeamento rigoroso de todos os estados mentais felizes do Abhidhamma, distinguindo sensação alegre (62) de êxtase/pīti (51).",
      "mnemonicOrExamTip": "Fórmula: 18 Kāma (4+2+12) + 12 Rūpa (4×3) + 32 Lokuttara (4×8) = 62 Cittas Somanassa (vs. 51 Sapītika).",
      "examQuestionType": "Cálculo de Distribuição de Sensações"
    },
    "es": {
      "question": "¿Cuáles son los 62 Cittas que surgen con Alegría (Somanassa)?",
      "answer": "En el esquema de 121 cittas, exactamente 62 tienen Somanassa:\n• 4 Lobhamūlacittas\n• 1 Kusalavipāka Santīraṇa + 1 Hasituppāda (2 Ahetuka)\n• 12 Kāma-sobhana (4 mahākusala + 4 mahāvipāka + 4 mahākiriya)\n• 12 Rūpāvacara (1º al 4º Jhāna: 4 jhānas × 3 clases = 12)\n• 32 Lokuttara (1º al 4º Jhāna: 4 jhānas × 8 = 32)\nTotal: 18 + 12 + 32 = 62 Cittas.",
      "breakdown": [
        "En el sistema quíntuple (Pañcakanaya), el 4º Jhāna abandona Pīti pero conserva Sukha/Somanassa; solo el 5º Jhāna tiene Upekkhā.",
        "Contraste: 62 cittas con Somanassa (1º–4º jhānas) vs. 51 cittas con Pīti / Sapītika (18 kāma + 9 rūpa + 24 lokuttara)."
      ],
      "explanation": "Censo completo de mentes gozosas y distinción entre Somanassa (62) y Pīti (51).",
      "mnemonicOrExamTip": "18 Kāma + 12 Rūpa (4×3) + 32 Lokuttara (4×8) = 62 cittas con Somanassa.",
      "examQuestionType": "Distribución de Somanassa"
    }
  },
  {
    "id": "ch2-10",
    "chapter": 2,
    "chapterName": {
      "pali": "Cetasikaparicchedo",
      "en": "Chapter 2: Mental Factors",
      "pt": "Capítulo 2: Fatores Mentais",
      "es": "Capítulo 2: Factores Mentales"
    },
    "section": "Paññā in 47 or 79 Cittas",
    "category": "quantities",
    "paliTerm": "Paññindriya Distribution",
    "tags": [
      "panna",
      "pannindriya",
      "amoha",
      "wisdom",
      "47",
      "79"
    ],
    "en": {
      "question": "In how many Cittas does the Faculty of Wisdom (Paññindriya / Amoha) arise?",
      "answer": "Paññindriya arises in 47 Cittas (brief) or 79 Cittas (detailed):\n• 12 Kāmāvacara-sobhana (the 4 Mahākusala + 4 Mahāvipāka + 4 Mahākiriya associated with knowledge [ñāṇasampayutta])\n• 15 Rūpāvacara Cittas (all fine-material jhānas require wisdom)\n• 12 Arūpāvacara Cittas (all immaterial jhānas require wisdom)\n• 8 or 40 Lokuttara Cittas (all supramundane paths & fruits require wisdom)\nTotal: 12 + 15 + 12 + 8 = 47 (or 12 + 15 + 12 + 40 = 79).",
      "breakdown": [
        "Never arises in unwholesome states (akusala).",
        "Never arises in rootless states (ahetuka).",
        "Never arises in mundane beautiful states that lack wisdom (ñāṇavippayutta)."
      ],
      "explanation": "These 47 or 79 consciousnesses are known as 'Tihetuka Cittas' (consciousness endowed with 3 wholesome roots: alobha, adosa, amoha).",
      "mnemonicOrExamTip": "Exam Identity: The number of cittas containing Paññā (47/79) is EXACTLY identical to the number of Tihetuka Cittas!",
      "examQuestionType": "Factor Distribution & Root Correlation"
    },
    "pt": {
      "question": "Em quantos Cittas surge a Faculdade da Sabedoria (Paññindriya / Amoha)?",
      "answer": "A sabedoria surge em 47 Cittas (breve) ou 79 Cittas (detalhado):\n• 12 Kāmāvacara-sobhana (4 Mahākusala + 4 Mahāvipāka + 4 Mahākiriya com sabedoria [ñāṇasampayutta])\n• 15 Rūpāvacara (todas as absorções da forma exigem sabedoria)\n• 12 Arūpāvacara (todas as absorções imateriais exigem sabedoria)\n• 8 ou 40 Lokuttara (todos os caminhos e frutos supramundanos exigem sabedoria)\nTotal: 12 + 15 + 12 + 8 = 47 (ou 12 + 15 + 12 + 40 = 79).",
      "breakdown": [
        "Nunca surge nos inábeis (akusala).",
        "Nunca surge nos sem raiz (ahetuka).",
        "Nunca surge nos belos sem conhecimento (ñāṇavippayutta)."
      ],
      "explanation": "Estes 47 ou 79 cittas são precisamente os 'Cittas Tihetuka' (dotados das 3 raízes sublimes: alobha, adosa e amoha).",
      "mnemonicOrExamTip": "Equivalência de Ouro: O número de cittas com sabedoria (47/79) é EXATAMENTE idêntico ao número de cittas Tihetuka!",
      "examQuestionType": "Distribuição de Fatores e Correlação de Raízes"
    },
    "es": {
      "question": "¿En cuántos Cittas surge la Sabiduría (Paññindriya)?",
      "answer": "En 47 (breve) o 79 (detallado) Cittas:\n12 Kāma con conocimiento + 15 Rūpa + 12 Arūpa + 8/40 Lokuttara.\nTotal: 47 o 79.",
      "breakdown": [
        "Nunca surge en estados perjudiciales (akusala).",
        "Nunca surge en estados sin raíz (ahetuka).",
        "Nunca surge en estados bellos mundanos sin conocimiento (ñāṇavippayutta)."
      ],
      "explanation": "Presencia de la luz del discernimiento.",
      "mnemonicOrExamTip": "Cittas con Paññā = Cittas Tihetuka = 47 o 79.",
      "examQuestionType": "Distribución de Sabiduría"
    }
  },
  {
    "id": "ch3-06",
    "chapter": 3,
    "chapterName": {
      "pali": "Pakiṇṇakaparicchedo",
      "en": "Chapter 3: Miscellaneous",
      "pt": "Capítulo 3: Categorias Diversas",
      "es": "Capítulo 3: Misceláneas"
    },
    "section": "Door Distribution of Cittas",
    "category": "structures",
    "paliTerm": "Dvārasaṅgaho Distribution",
    "tags": [
      "dvara",
      "doors",
      "ekadvarika",
      "chaddvarika",
      "dvaravimutta"
    ],
    "en": {
      "question": "How are Cittas classified by the Doors (Dvāra) through which they arise?",
      "answer": "• Single-Door (Ekadvārika): 36 Cittas (10 sense consciousnesses arise in their respective 5 physical doors; 26 sublime & supramundane cittas arise only in the Mind-door).\n• Five-Doors (Pañcadvārika): 3 Cittas (the 3 mind elements: 2 Sampaṭicchana + 1 Pañcadvārāvajjana arise in all 5 physical doors).\n• Six-Doors (Chaddvārika): 31 Cittas (can arise through any of the 6 doors: 1 Voṭṭhabbana + 29 Kāma Javanas + 1 Hasituppāda).\n• Door-Freed (Dvāravimutta): 19 Cittas (at Paṭisandhi, Bhavaṅga, Cuti).",
      "breakdown": [
        "Some cittas are fixed to one door; others can experience objects through multiple doors.",
        "The 19 Dvāravimutta cittas can also function through doors at other times (e.g. Mahāvipāka as Tadārammaṇa in 6 doors)."
      ],
      "explanation": "Illustrates how consciousness interfaces with physical reality and mental reflection.",
      "mnemonicOrExamTip": "Exam Question: Which cittas can arise through all 6 doors? The 31 cittas (Voṭṭhabbana + Kāma Javanas).",
      "examQuestionType": "Door Interfacing Taxonomy"
    },
    "pt": {
      "question": "Como se classificam os Cittas segundo as Portas (Dvāra) por onde surgem?",
      "answer": "• Porta Única (Ekadvārika): 36 Cittas (10 consciências sensoriais nas suas 5 portas físicas; 26 sublimes e supramundanos apenas na Porta Mental).\n• Cinco Portas (Pañcadvārika): 3 Cittas (2 Sampaṭicchanas + 1 Pañcadvārāvajjana surgem nas 5 portas físicas).\n• Seis Portas (Chaddvārika): 31 Cittas (1 Voṭṭhabbana + 29 Javanas de Kāma + 1 Hasituppāda surgem em qualquer das 6 portas).\n• Livres de Portas (Dvāravimutta): 19 Cittas (no renascimento, fluxo vital e morte).",
      "breakdown": [
        "Alguns cittas são fixos em uma porta; outros transitam livremente.",
        "Os 19 Dvāravimutta atuam sem porta nas 3 funções passivas."
      ],
      "explanation": "Mapeia as interfaces pelas quais a mente se conecta ao mundo físico e interior.",
      "mnemonicOrExamTip": "Pergunta de Exame: Quais cittas surgem em todas as 6 portas? Os 31 cittas (Determinação + Javanas de Kāma).",
      "examQuestionType": "Classificação por Portas Sensoriais"
    },
    "es": {
      "question": "¿Cómo se clasifican los Cittas según sus Puertas (Dvāra)?",
      "answer": "• 1 Puerta: 36 (10 sentidos físicos + 26 absorciones/lokuttara en la mente).\n• 5 Puertas: 3 (Pañcadvārāvajjana y 2 sampaṭicchana).\n• 6 Puertas: 31 (Voṭṭhabbana + 29 javanas de Kāma + Hasituppāda).\n• Sin Puerta: 19 (Paṭisandhi, Bhavaṅga, Cuti).",
      "breakdown": [
        "Clasificación según acceso sensorial.",
        "Totaliza los 89 cittas."
      ],
      "explanation": "Interacción con los canales de percepción.",
      "mnemonicOrExamTip": "36 (1 puerta), 3 (5 puertas), 31 (6 puertas), 19 (sin puerta).",
      "examQuestionType": "Puertas Cognitivas"
    }
  },
  {
    "id": "ch5-06",
    "chapter": 5,
    "chapterName": {
      "pali": "Vīthimuttaparicchedo",
      "en": "Chapter 5: Process-Freed",
      "pt": "Capítulo 5: Consciência Fora do Processo",
      "es": "Capítulo 5: Fuera del Proceso"
    },
    "section": "4 Modes of Rebirth-Linking",
    "category": "structures",
    "paliTerm": "Paṭisandhicatukka",
    "tags": [
      "patisandhi",
      "rebirth",
      "apaya",
      "kamasugati",
      "rupa",
      "arupa"
    ],
    "en": {
      "question": "What are the 4 Modes of Rebirth-linking (Paṭisandhicatukka) and which exact citta links each?",
      "answer": "1. Apāyapaṭisandhi (Woeful Rebirth - hell, animal, peta, asura):\nLinked by exactly 1 Citta: Akusalavipāka Upekkhā-santīraṇa.\n\n2. Kāmasugatipaṭisandhi (Sensuous Blissful Rebirth - humans and 6 devas):\nLinked by 9 Cittas:\n• 1 Ahetuka Kusalavipāka Upekkhā-santīraṇa (for congenitally handicapped/blind humans and low earth-devas).\n• 8 Mahāvipāka Cittas (for normal humans and celestial devas).\n\n3. Rūpāvacarapaṭisandhi (Fine-Material Rebirth):\nLinked by 5 Rūpāvacara Vipāka Cittas (matching the 5 Jhānas).\n\n4. Arūpāvacarapaṭisandhi (Immaterial Rebirth):\nLinked by 4 Arūpāvacara Vipāka Cittas (matching the 4 Arūpa states).\nTotal: Exactly 1 + 9 + 5 + 4 = 19 Rebirth-linking Cittas!",
      "breakdown": [
        "A person born congenitally blind or intellectually disabled took rebirth with the rootless wholesome resultant santīraṇa.",
        "Noble disciples and fortunate beings take rebirth with Tihetuka or Dvihetuka Mahāvipāka."
      ],
      "explanation": "Every single being in the cosmos is born into their plane by one of these 19 specific resultant consciousnesses.",
      "mnemonicOrExamTip": "Exam Math: 1 woeful + 9 sensuous blissful + 5 fine-material + 4 immaterial = Exactly 19 Paṭisandhi Cittas.",
      "examQuestionType": "Rebirth-linking Typology"
    },
    "pt": {
      "question": "Quais são os 4 Modos de Renascimento (Paṭisandhicatukka) e qual citta exato opera cada um?",
      "answer": "1. Apāyapaṭisandhi (Renascimento nos reinos de sofrimento - inferno, animais, fantasmas, asuras):\nOperado por 1 único Citta: Akusalavipāka Santīraṇa com upekkhā.\n\n2. Kāmasugatipaṭisandhi (Renascimento humano e celestial):\nOperado por 9 Cittas:\n• 1 Ahetuka Kusalavipāka Santīraṇa com upekkhā (para humanos que nascem com deficiências congênitas graves, cegos de nascença, etc.).\n• 8 Mahāvipāka Cittas (para humanos saudáveis e devas dos 6 céus).\n\n3. Rūpāvacarapaṭisandhi (Renascimento nos reinos da Forma Sutil):\nOperado por 5 Rūpāvacara Vipāka Cittas (conforme o nível de Jhāna).\n\n4. Arūpāvacarapaṭisandhi (Renascimento nos reinos Imateriais):\nOperado por 4 Arūpāvacara Vipāka Cittas.\nTotal: Exatamente 1 + 9 + 5 + 4 = 19 Cittas de Renascimento!",
      "breakdown": [
        "Humanos nascidos cegos ou surdos de nascença renasceram com o santīraṇa sem raiz.",
        "Seres com capacidade de despertar naquela vida renascem com Mahāvipāka dotado de sabedoria (tihetuka)."
      ],
      "explanation": "Mapeamento ontológico exato de como o karma passado determina o ponto de partida de cada vida.",
      "mnemonicOrExamTip": "Fórmula de Prova: 1 inferior + 9 sensoriais + 5 forma + 4 imateriais = 19 Cittas de Paṭisandhi.",
      "examQuestionType": "Tipologia do Renascimento"
    },
    "es": {
      "question": "¿Cuáles son los 4 Modos de Renacimiento (Paṭisandhi) y sus cittas?",
      "answer": "1. Apāya: 1 akusalavipāka santīraṇa.\n2. Kāmasugati: 1 ahetukakusala santīraṇa (humanos con discapacidad congénita) + 8 mahāvipāka (humanos y devas normales) = 9.\n3. Rūpa: 5 rūpavipāka.\n4. Arūpa: 4 arūpavipāka.\nTotal: 19 cittas.",
      "breakdown": [
        "Explica el punto de partida biológico y mental en cada renacimiento.",
        "1 + 9 + 5 + 4 = 19."
      ],
      "explanation": "Determinación del nuevo ser según kamma.",
      "mnemonicOrExamTip": "Total cittas de paṭisandhi = 19.",
      "examQuestionType": "Modos de Paṭisandhi"
    }
  },
  {
    "id": "ch6-06",
    "chapter": 6,
    "chapterName": {
      "pali": "Rūpaparicchedo",
      "en": "Chapter 6: Matter & Nibbāna",
      "pt": "Capítulo 6: Matéria e Nibbāna",
      "es": "Capítulo 6: Materia y Nibbāna"
    },
    "section": "Cessation of Matter at Death",
    "category": "structures",
    "paliTerm": "Kammaja Rūpa Cessation",
    "tags": [
      "death",
      "matter",
      "kammaja",
      "17 moments",
      "cuti"
    ],
    "en": {
      "question": "At what exact point does Kamma-produced matter (Kammaja-rūpa) stop arising before physical death?",
      "answer": "Kamma-produced matter stops arising at the static phase (ṭhitikkhaṇa) of the 17th thought-moment preceding the Death Consciousness (Cuti Citta)!\nAll existing kammaja-rūpa then perishes simultaneously with the dissolution of the Cuti Citta.",
      "breakdown": [
        "Since a material phenomenon endures for 17 thought-moments, the kamma-born matter generated at that 17th preceding moment reaches its natural lifespan and dissolves at the exact instant the cuti citta ceases.",
        "At that point, physical life faculty (jīvitarūpa), eye sensitivity, heart base, and body sensitivity completely cease.",
        "Only temperature-born matter (utuja-rūpa) continues to arise and decay in the lifeless corpse."
      ],
      "explanation": "Demonstrates the astonishing precision of Buddhist medical and physical science: physical biological death is synchronized down to the microsecond with the final cognitive stream.",
      "mnemonicOrExamTip": "Exam High-Yield Statistic: When does kamma-produced matter cease being generated? Exactly 17 thought-moments before cuti citta!",
      "examQuestionType": "Somatic Dissolution Dynamics"
    },
    "pt": {
      "question": "Em que momento exato a matéria gerada pelo Karma (Kammaja-rūpa) para de ser produzida antes da morte física?",
      "answer": "A matéria gerada pelo karma para de surgir no momento estático (ṭhitikkhaṇa) do 17º momento mental ANTERIOR à Consciência de Morte (Cuti Citta)!\nToda a matéria originada pelo karma cessa simultaneamente com a dissolução do Cuti Citta.",
      "breakdown": [
        "Como a matéria dura 17 momentos mentais, a última partícula gerada pelo karma atinge o fim de sua vida útil exatamente quando o cuti se extingue.",
        "Nesse instante cessam a vida física (jīvitarūpa), a sensibilidade dos sentidos e a base do coração.",
        "Apenas a matéria gerada pela temperatura (utuja-rūpa) prossegue existindo no cadáver."
      ],
      "explanation": "Sincronização cronológica assombrosa entre a biologia material e o fluxo da mente no instante da morte.",
      "mnemonicOrExamTip": "Dado de Prova Decisivo: A matéria de karma para de ser gerada exatamente 17 momentos mentais antes do cuti citta!",
      "examQuestionType": "Dinâmica da Dissolução Biológica"
    },
    "es": {
      "question": "¿Cuándo cesa de producirse la materia originada por kamma antes de morir?",
      "answer": "Cesa de surgir exactamente en el 17º momento de pensamiento previo a la muerte (Cuti Citta).\nAl disolverse Cuti, toda la materia de kamma perece a la vez.",
      "breakdown": [
        "Como la materia dura 17 momentos mentales, la materia generada por kamma en ese 17º momento previo se extingue exactamente cuando cesa el cuti citta.",
        "En ese instante cesan la facultad vital física (jīvitarūpa), las 5 sensibilidades y la base del corazón.",
        "En el cadáver solo continúa surgiendo materia generada por la temperatura (utuja-rūpa)."
      ],
      "explanation": "Sincronía bio-psíquica de la muerte.",
      "mnemonicOrExamTip": "17 momentos antes de cuti cesa la producción de kammaja-rūpa.",
      "examQuestionType": "Materia en la Muerte"
    }
  },
  {
    "id": "ch8-04",
    "chapter": 8,
    "chapterName": {
      "pali": "Paccayaparicchedo",
      "en": "Chapter 8: Conditionality",
      "pt": "Capítulo 8: Condicionalidade",
      "es": "Capítulo 8: Condicionalidad"
    },
    "section": "Sahajāta vs Aññamañña vs Nissaya",
    "category": "relations",
    "paliTerm": "Sahajāta vs Aññamañña",
    "tags": [
      "patthana",
      "sahajata",
      "annamanna",
      "nissaya",
      "paccaya"
    ],
    "en": {
      "question": "Distinguish between Sahajāta-paccaya (Co-nascence), Aññamañña-paccaya (Mutuality), and Nissaya-paccaya (Dependence).",
      "answer": "• Sahajāta-paccaya (Co-nascence):\nThe conditioning state assists the conditioned state merely by arising simultaneously with it (e.g., a candle flame and its illumination).\n• Aññamañña-paccaya (Mutuality / Reciprocity):\nThe states not only arise together, but MUTUALLY condition each other reciprocally (e.g., three walking sticks leaning against one another—if one falls, all fall!).\n• Nissaya-paccaya (Dependence):\nThe conditioning state serves as the supporting base or foundation for the conditioned state (e.g., the earth supporting trees, or a canvas supporting a painting).",
      "breakdown": [
        "All Aññamañña relations are Sahajāta, but NOT all Sahajāta relations are Aññamañña!",
        "For example: Mind-produced matter arises simultaneously with citta (Sahajāta), but mind-produced matter DOES NOT support the citta in return (so it is not Aññamañña)."
      ],
      "explanation": "This distinction illustrates the rigorous relational calculus of the Paṭṭhāna, avoiding superficial assumptions about causation.",
      "mnemonicOrExamTip": "Exam Trap: Is mind-produced matter related to citta by Aññamañña? NO! It is Sahajāta, but not Aññamañña (citta creates matter, but that matter does not support citta in return).",
      "examQuestionType": "Conditional Relational Calculus"
    },
    "pt": {
      "question": "Distinga entre Sahajāta-paccaya (Co-nascimento), Aññamañña-paccaya (Mutualidade) e Nissaya-paccaya (Dependência).",
      "answer": "• Sahajāta-paccaya (Co-nascimento):\nA condição auxilia o fenômeno condicionado pelo simples fato de surgirem simultaneamente (ex.: a chama da vela e a sua luz).\n• Aññamañña-paccaya (Mutualidade recíproca):\nOs fenômenos não apenas nascem juntos, mas SUSTENTAM-SE MUTUAMENTE de forma recíproca (ex.: três bastões apoiados um no outro—se tirar um, todos caem!).\n• Nissaya-paccaya (Dependência / Fundação):\nA condição atua como base de suporte estável (ex.: a terra firme sustentando as árvores, ou a tela que apoia a pintura).",
      "breakdown": [
        "Toda relação de Aññamañña é Sahajāta, mas NEM TODA relação de Sahajāta é Aññamañña!",
        "Exemplo: A matéria gerada pela mente nasce junto com o citta (Sahajāta), mas essa matéria NÃO apoia a mente de volta (portanto, NÃO é Aññamañña)."
      ],
      "explanation": "Demonstra o rigor matemático das 24 relações causais do Paṭṭhāna.",
      "mnemonicOrExamTip": "Pegadinha de Prova: A matéria gerada pela mente apoia o citta por Aññamañña? NÃO! É apenas Sahajāta, mas não mútua.",
      "examQuestionType": "Diferenciação Crítica de Paccayas"
    },
    "es": {
      "question": "¿Cuál es la diferencia entre Sahajāta, Aññamañña y Nissaya?",
      "answer": "• Sahajāta: Nacen juntos (llama y luz).\n• Aññamañña: Soporte mutuo recíproco (3 bastones apoyados).\n• Nissaya: Base de apoyo (la tierra para los árboles).",
      "breakdown": [
        "Todo Aññamañña es Sahajāta, pero no al revés.",
        "La materia mental nace con el citta (sahajāta) pero no lo sostiene a él (no es aññamañña)."
      ],
      "explanation": "Precisión relacional del Paṭṭhāna.",
      "mnemonicOrExamTip": "Vela y luz (Sahajāta) vs Trípode (Aññamañña).",
      "examQuestionType": "Distinciones de Paccaya"
    }
  },
  {
    "id": "ch9-07",
    "chapter": 9,
    "chapterName": {
      "pali": "Kammaṭṭhānaparicchedo",
      "en": "Chapter 9: Meditation",
      "pt": "Capítulo 9: Meditação e Libertação",
      "es": "Capítulo 9: Meditación y Liberación"
    },
    "section": "3 Doors to Deliverance",
    "category": "philosophy",
    "paliTerm": "Vimokkhamukha 3",
    "tags": [
      "vimokkha",
      "deliverance",
      "sunnata",
      "animitta",
      "appanihita",
      "tilakkhana"
    ],
    "en": {
      "question": "What are the 3 Doors to Deliverance (Vimokkhamukha) and their corresponding Three Characteristics (Ti-lakkhaṇa)?",
      "answer": "1. Suññata-vimokkha (Void Deliverance):\nEntered through the contemplation of ANATTĀ (Non-Self), seeing all phenomena as void of an abiding self, soul, or controller.\n\n2. Animitta-vimokkha (Signless Deliverance):\nEntered through the contemplation of ANICCA (Impermanence), seeing all formations as transient, unstable, and devoid of permanent signs.\n\n3. Appaṇihita-vimokkha (Desireless Deliverance):\nEntered through the contemplation of DUKKHA (Unsatisfactoriness/Suffering), extinguishing all yearning and feverish desire for conditioned existence.",
      "breakdown": [
        "Contemplation of Anattā -> Suññata (Voidness).",
        "Contemplation of Anicca -> Animitta (Signlessness).",
        "Contemplation of Dukkha -> Appaṇihita (Desirelessness).",
        "Whichever characteristic is prominent at the peak moment of insight (anuloma/gotrabhū) gives its name to the noble deliverance."
      ],
      "explanation": "These three doors show how the contemplation of reality's three universal marks leads straight into the unconditioned peace of Nibbāna.",
      "mnemonicOrExamTip": "Direct Mapping: Anattā = Suññata | Anicca = Animitta | Dukkha = Appaṇihita.",
      "examQuestionType": "Liberation Doors & Three Characteristics"
    },
    "pt": {
      "question": "Quais são as 3 Portas da Libertação (Vimokkhamukha) e suas Três Características (Ti-lakkhaṇa) correspondentes?",
      "answer": "1. Suññata-vimokkha (Libertação do Vazio):\nAtingida pela contemplação de ANATTĀ (Não-Eu), contemplando todos os fenômenos como vazios de um eu substantivo ou controlador.\n\n2. Animitta-vimokkha (Libertação Sem-Sinais):\nAtingida pela contemplação de ANICCA (Impermanência), contemplando todas as formações como transitórias e desprovidas de estabilidade substancial.\n\n3. Appaṇihita-vimokkha (Libertação Sem-Desejos):\nAtingida pela contemplação de DUKKHA (Insatisfatoriedade), extinguindo todo anseio de posse pelo que é condicionado.",
      "breakdown": [
        "Anattā -> Vazio (Suññata).",
        "Anicca -> Sem Sinais (Animitta).",
        "Dukkha -> Sem Desejos (Appaṇihita).",
        "A marca que prevalece no momento culminante do discernimento batiza a porta pela qual o nobre entra em Nibbāna."
      ],
      "explanation": "Conecta as três marcas universais da existência diretamente aos três modos de entrada na iluminação.",
      "mnemonicOrExamTip": "Mapeamento Direto: Anattā = Suññata | Anicca = Animitta | Dukkha = Appaṇihita.",
      "examQuestionType": "Portas da Libertação e Três Características"
    },
    "es": {
      "question": "¿Cuáles son las 3 Puertas de la Liberación (Vimokkhamukha)?",
      "answer": "1. Suññata (Vacío) -> Vía ANATTĀ (No-yo).\n2. Animitta (Sin signo) -> Vía ANICCA (Impermanencia).\n3. Appaṇihita (Sin deseo) -> Vía DUKKHA (Sufrimiento).",
      "breakdown": [
        "Contemplación de Anattā -> Suññata (Vacío).",
        "Contemplación de Anicca -> Animitta (Sin Signo).",
        "Contemplación de Dukkha -> Appaṇihita (Sin Deseo).",
        "La característica que predomina en el instante culminante de introspección da su nombre a la liberación."
      ],
      "explanation": "Los 3 modos de acceso a Nibbāna.",
      "mnemonicOrExamTip": "Anattā = Vacío; Anicca = Sin signo; Dukkha = Sin deseo.",
      "examQuestionType": "Puertas de Liberación"
    }
  }
];

import fs from 'fs';

const dictPath = './src/data/paliDictionary.json';
const dict = JSON.parse(fs.readFileSync(dictPath, 'utf8'));

// Mapa para checagem rápida de verbetes existentes
const existingPali = new Set(dict.map((d) => d.pali.toLowerCase().trim()));

// Dicionário canônico rigoroso dos termos técnicos e compostos do Abhidhammatthasaṅgaha
const abhidhammaAdditions = [
  {
    pali: "tatramajjhattatā",
    meaning: {
      en: "specific neutrality; equanimity regarding mental states; impartial balance of consciousness and concomitants (one of the 19 beautiful universal mental factors, sobhana-sādhāraṇa-cetasika)",
      pt: "equanimidade mental específica; neutralidade e equilíbrio imparcial da consciência e dos fatores mentais concomitantes (um dos 19 fatores mentais belos universais, sobhana-sādhāraṇa-cetasika)",
      es: "ecuanimidad mental específica; neutralidad y equilibrio imparcial de la conciencia y factores mentales (uno de los 19 factores mentales bellos universales, sobhana-sādhāraṇa-cetasika)"
    },
    grammar: "f. (subst.), tatra + majjhatta + tā",
    root: "tatra (ali/naquilo) + majjha (meio) + √ṭhā (permanecer) + sufixo abstrato tā"
  },
  {
    pali: "voṭṭhabbana",
    meaning: {
      en: "determining consciousness; the cognitive act of ascertaining and determining the sensory object in a thought-process (vīthi); performed by manodvārāvajjana at the five sense-doors",
      pt: "consciência determinadora; a função cognitiva de determinar, verificar e fixar o objeto sensorial no processo cognitivo (vīthi); desempenhada por manodvārāvajjana nas cinco portas sensoriais",
      es: "conciencia determinadora; la función cognitiva de determinar y fijar el objeto sensorial en el proceso cognitivo (vīthi)"
    },
    grammar: "nt. (subst.), vi + ava + √ṭhā + ana",
    root: "vi + ava + √ṭhā (estabelecer) + ana"
  },
  {
    pali: "voṭṭhabbanaṃ",
    meaning: {
      en: "determining consciousness (accusative/nominative); the phase of determining the object in the perceptual process",
      pt: "a consciência determinadora (acusativo/nominativo neutro); a etapa de determinação do objeto no processo perceptivo",
      es: "la conciencia determinadora; la etapa de determinación del objeto en el proceso perceptual"
    },
    grammar: "nt. nom./acc. sg. de voṭṭhabbana",
    root: "vi + ava + √ṭhā + ana"
  },
  {
    pali: "voṭṭhabbane",
    meaning: {
      en: "in the determining consciousness; at the stage of determination (locative singular)",
      pt: "na determinação; no momento da consciência determinadora (locativo singular)",
      es: "en la determinación; en el momento de la conciencia determinadora (locativo singular)"
    },
    grammar: "nt. loc. sg. de voṭṭhabbana",
    root: "vi + ava + √ṭhā + ana"
  },
  {
    pali: "voṭṭhabbanameva",
    meaning: {
      en: "only the determining consciousness; precisely the determining stage (voṭṭhabbanaṃ + eva)",
      pt: "apenas a consciência determinadora; precisamente a etapa de determinação (voṭṭhabbanaṃ + eva)",
      es: "precisamente la conciencia determinadora (voṭṭhabbanaṃ + eva)"
    },
    grammar: "composto sandhi, voṭṭhabbanaṃ + eva",
    root: "vi + ava + √ṭhā + ana + eva"
  },
  {
    pali: "voṭṭhabbananti",
    meaning: {
      en: "namely, determining consciousness; quoted as 'voṭṭhabbana' (voṭṭhabbanaṃ + iti)",
      pt: "isto é, a consciência determinadora; chamado de 'voṭṭhabbana' (voṭṭhabbanaṃ + iti)",
      es: "a saber, la conciencia determinadora (voṭṭhabbanaṃ + iti)"
    },
    grammar: "sandhi com citação iti, voṭṭhabbanaṃ + iti",
    root: "vi + ava + √ṭhā + ana + iti"
  },
  {
    pali: "saupādisesanibbānadhātu",
    meaning: {
      en: "the Nibbāna-element with residue of clinging/aggregates remaining; the realization of Nibbāna attained by an Arahant during life while the five aggregates persist",
      pt: "o elemento de Nibbāna com o resíduo dos agregados remanescentes; a realização de Nibbāna alcançada por um Arahant em vida enquanto os cinco agregados corpóreo-mentais ainda subsistem",
      es: "el elemento de Nibbāna con residuo de los agregados restante; la realización de Nibbāna alcanzada en vida por un Arahant"
    },
    grammar: "f., sa + upādi + sesa + nibbāna + dhātu",
    root: "sa (com) + upādi (combustível/apego aos agregados) + sesa (remanescente) + nibbāna + dhātu"
  },
  {
    pali: "anipphannā",
    meaning: {
      en: "non-produced matter (nominative plural feminine); the 10 derivative material phenomena not concretely produced by the four causes (kamma, citta, utu, āhāra)",
      pt: "matéria não produzida concretamente (nominativo feminino plural); os 10 fenômenos materiais derivados não gerados concretamente pelas 4 causas, atuando como características ou modos da matéria",
      es: "materia no producida concretamente (plural); los 10 fenómenos materiales derivados que actúan como modos o delimitaciones de la materia"
    },
    grammar: "adj. f. pl., a + nipphanna",
    root: "a (não) + ni + √pad + na > nipphanna"
  },
  {
    pali: "salakkhaṇā",
    meaning: {
      en: "individual/specific characteristics (plural); the intrinsic, quintessential nature that uniquely defines each ultimate reality (paramattha dhamma)",
      pt: "características individuais / intrínsecas (plural); os traços próprios e essenciais que definem de modo único cada realidade última (paramattha dhamma), em contraste com as características universais",
      es: "características individuales / intrínsecas (plural); los rasgos esenciales que definen exclusivamente cada realidad última (paramattha dhamma)"
    },
    grammar: "f. pl., sa + lakkhaṇa",
    root: "sa (próprio) + √lakkh (marcar/caracterizar) + ana"
  },
  {
    pali: "diṭṭhāsavo",
    meaning: {
      en: "taint of wrong view (nominative singular masculine); the defiling influx (āsava) of speculative and erroneous views",
      pt: "o eflúvio da visão errônea (nominativo singular masculino); a contaminação mental (āsava) consistente na adesão a visões equivocadas e especulativas (diṭṭhi)",
      es: "la fermentación / efluvio de las visiones erróneas (āsava); mácula mental de puntos de vista distorsionados"
    },
    grammar: "m. nom. sg., diṭṭhi + āsava",
    root: "diṭṭhi (visão) + ā + √su (fluir/fermentar) > āsava"
  },
  {
    pali: "kāyānupassanāsatipaṭṭhānaṃ",
    meaning: {
      en: "the foundation of mindfulness in contemplation of the body; the first of the four foundations of mindfulness (satipaṭṭhāna)",
      pt: "o estabelecimento da atenção plena na contemplação do corpo; a primeira das quatro bases da atenção plena (satipaṭṭhāna)",
      es: "el establecimiento de la atención plena en la contemplación del cuerpo; la primera de las cuatro bases de la atención plena"
    },
    grammar: "nt. nom./acc. sg., kāya + anupassanā + satipaṭṭhāna",
    root: "kāya + anu + √pass + anā + sati + pa + √ṭhā + ana"
  },
  {
    pali: "dukkhānupassanā",
    meaning: {
      en: "contemplation of suffering/unsatisfactoriness; one of the three principal contemplations (anupassanā) abandoning the perception of pleasure in conditioned phenomena",
      pt: "contemplação do sofrimento / insatisfatoriedade; uma das três contemplações contemplativas principais que erradica a percepção errônea de prazer nas formações condicionadas",
      es: "contemplación del sufrimiento / insatisfactoriedad; una de las tres contemplaciones principales de la visión penetrante"
    },
    grammar: "f., dukkha + anupassanā",
    root: "dukkha + anu + √pass + anā"
  },
  {
    pali: "purejāta",
    meaning: {
      en: "pre-nascent condition; existing prior to; the conditional relation (purejāta-paccaya) where a cause must precede its effect",
      pt: "condição de pré-existência / pré-nascimento (purejāta-paccaya); relação condicional na qual a causa (como a base física ou o objeto) surge antes do efeito mental que sobre ela se apoia",
      es: "condición de pre-existencia / pre-nacimiento (purejāta-paccaya); relación en la que la condición surge antes de su efecto"
    },
    grammar: "adj. / nt., pure + jāta",
    root: "pure (antes) + √jan > jāta (nascido)"
  },
  {
    pali: "purejātassa",
    meaning: {
      en: "of that which has arisen beforehand; of the pre-nascent condition (genitive/dative singular)",
      pt: "daquilo que surgiu precedentemente; da condição pré-existente (genitivo/dativo singular)",
      es: "de lo que ha surgido con anterioridad; de la condición pre-existente"
    },
    grammar: "gen./dat. sg. de purejāta",
    root: "pure + √jan > jāta + assa"
  },
  {
    pali: "purejātaṃ",
    meaning: {
      en: "pre-nascent condition (nominative/accusative neuter); arisen beforehand",
      pt: "condição de pré-nascimento (nominativo/acusativo neutro); que surgiu previamente",
      es: "condición de pre-nacimiento (nominativo/acusativo); surgido con anterioridad"
    },
    grammar: "nt. nom./acc. sg. de purejāta",
    root: "pure + √jan > jāta + aṃ"
  },
  {
    pali: "pumbhāvadasakaṃ",
    meaning: {
      en: "the decuple of masculinity (pumbhāva-dasaka); material group (kalāpa) of 10 material qualities including the 8 inseparables, life-faculty, and male sex-faculty",
      pt: "o grupo décuplo da masculinidade (pumbhāva-dasaka); kalāpa material constituído pelas 8 matérias inseparáveis, a vitalidade material e a faculdade sexual masculina",
      es: "el grupo décuplo de la masculinidad; kalāpa material formado por las 8 materias inseparables, la vitalidad y la facultad sexual masculina"
    },
    grammar: "nt., pumbhāva + dasaka",
    root: "puṃ (macho) + bhāva (natureza/estado) + dasa + ka"
  },
  {
    pali: "upapīḷakaṃ",
    meaning: {
      en: "debilitating/obstructive kamma (upapīḷaka-kamma); action that suppresses, impedes, or shortens the fruiting of another kamma",
      pt: "kamma debilitador / obstrutor (upapīḷaka-kamma); ação que oprime, enfraquece ou encurta a fruição de outro kamma sem gerar seu próprio renascimento",
      es: "kamma debilitador u obstructivo; acción que sofoca o acorta la maduración de otro kamma"
    },
    grammar: "adj. / nt. nom./acc. sg., upa + √pīḷ + aka",
    root: "upa + √pīḷ (oprimir/atormentar) + aka"
  },
  {
    pali: "paṭibhāganimittaṃ",
    meaning: {
      en: "counterpart sign (paṭibhāga-nimitta); the purified, radiant conceptual mental image arising from samatha meditation that leads directly to meditative absorption (jhāna)",
      pt: "o sinal correspondente / contraparte mental pura (paṭibhāga-nimitta); a representação mental purificada e luminosa que surge na meditação de samatha após o sinal aprendido, conduzindo ao jhāna",
      es: "el signo correspondiente / contraparte pura (paṭibhāga-nimitta); imagen mental refinada que surge en la meditación samatha conducente al jhāna"
    },
    grammar: "nt. nom./acc. sg., paṭibhāga + nimitta",
    root: "paṭi + √bhaj > bhāga + nimitta"
  },
  {
    pali: "santīraṇaṃ",
    meaning: {
      en: "investigating consciousness (santīraṇa-citta); rootless resultant mind that investigates a sense-object prior to the determining stage",
      pt: "consciência investigadora (santīraṇa-citta); consciência resultante sem raiz (ahetuka-vipāka) que examina o objeto sensorial imediatamente antes da etapa de determinação (voṭṭhabbana)",
      es: "conciencia investigadora (santīraṇa-citta); mente resultante sin raíz que examina el objeto antes de la determinación"
    },
    grammar: "nt. nom./acc. sg., sam + √tīr + ana",
    root: "sam + √tīr (examinar/decidir) + ana"
  },
  {
    pali: "hasanampi",
    meaning: {
      en: "even smiling; also the production of mirth (hasana + api)",
      pt: "mesmo o sorriso; também a manifestação de júbilo / riso (hasana + api)",
      es: "incluso el sonreír; también la manifestación de sonrisa (hasana + api)"
    },
    grammar: "sandhi, hasana + api",
    root: "√has (rir/sorrir) + ana + api"
  },
  {
    pali: "hasituppādaṃ",
    meaning: {
      en: "consciousness of the genesis of smile; the rootless functional citta (ahetuka-kiriya) peculiar to Arahants that produces a subtle smile",
      pt: "consciência da produção de sorriso (hasituppāda-citta); a consciência funcional sem raiz peculiar aos Budas e Arahants que engendra um sorriso gracioso",
      es: "conciencia de producción de sonrisa; citta funcional sin raíz peculiar de los Arahants"
    },
    grammar: "nt. nom./acc. sg., hasita + uppāda",
    root: "√has + ita + ud + √pad > uppāda"
  },
  {
    pali: "rūpādipañcārammaṇaṃ",
    meaning: {
      en: "the five sense-objects beginning with visible form (form, sound, smell, taste, touch)",
      pt: "os cinco objetos sensoriais encabeçados pela forma visível (forma visível, som, odor, sabor e tangível)",
      es: "los cinco objetos sensoriales encabezados por la forma visible (forma, sonido, olor, sabor y tangible)"
    },
    grammar: "nt. nom./acc. sg., rūpa + ādi + pañca + ārammaṇa",
    root: "rūpa + ādi + pañca + ā + √ram > ārammaṇa"
  },
  {
    pali: "sampayujjanti",
    meaning: {
      en: "they are associated with; they unite harmoniously (mental factors with consciousness)",
      pt: "associam-se; combinam-se e unem-se harmoniosamente (os fatores mentais com a consciência)",
      es: "se asocian; se combinan armoniosamente (los factores mentales con la conciencia)"
    },
    grammar: "v. 3ª pl. pres. pass., sam + pra + √yuj",
    root: "sam + pa + √yuj (unir/juntar) + ya + nti"
  },
  {
    pali: "sampiṇḍeti",
    meaning: {
      en: "condenses; aggregates; sums up concisely",
      pt: "condensa; resume; agrupa sinteticamente",
      es: "condensa; resume; agrupa sintéticamente"
    },
    grammar: "v. 3ª sg. pres., sam + √piṇḍ",
    root: "sam + √piṇḍ (acumular/resumir) + e + ti"
  },
  {
    pali: "sampiṇḍetvā",
    meaning: {
      en: "having condensed; having grouped together concisely",
      pt: "tendo condensado; tendo agrupado sinteticamente",
      es: "habiendo condensado; habiendo agrupado sintéticamente"
    },
    grammar: "absolutivo, sam + √piṇḍ + tvā",
    root: "sam + √piṇḍ + tvā"
  },
  {
    pali: "vavatthapentaṃ",
    meaning: {
      en: "defining; establishing distinctly; ascertaining parameters (present participle)",
      pt: "definindo; delimitando e estabelecendo distintamente os parâmetros dos dhammas (particípio presente)",
      es: "definiendo; estableciendo distintamente los parámetros de los estados (participio presente)"
    },
    grammar: "part. pres. acc. sg. m./nt., vi + ava + √ṭhā + ape + nta",
    root: "vi + ava + √ṭhā (estabelecer) + ape + nta"
  },
  {
    pali: "vavatthapetīti",
    meaning: {
      en: "defines; establishes distinctly, thus quoted (vavatthapeti + iti)",
      pt: "estabelece distintamente; define com precisão, assim citado (vavatthapeti + iti)",
      es: "establece distintamente; define con precisión (vavatthapeti + iti)"
    },
    grammar: "sandhi com citação iti, vavatthapeti + iti",
    root: "vi + ava + √ṭhā + e + ti + iti"
  },
  {
    pali: "visesetvā",
    meaning: {
      en: "having distinguished; having differentiated specifically",
      pt: "tendo distinguido; tendo especificado com detalhamento analítico",
      es: "habiendo distinguido; habiendo especificado analíticamente"
    },
    grammar: "absolutivo, vi + √sis + e + tvā",
    root: "vi + √sis (diferenciar) + tvā"
  },
  {
    pali: "vocchinditvā",
    meaning: {
      en: "having severed; having interrupted the continuity of a process",
      pt: "tendo interrompido; tendo cortado a continuidade do fluxo (ex.: o bhavaṅga)",
      es: "habiendo interrumpido; habiendo cortado la continuidad del flujo"
    },
    grammar: "absolutivo, vi + ud + √chid + tvā",
    root: "vi + ud + √chid (cortar) + tvā"
  },
  {
    pali: "vomissetvā",
    meaning: {
      en: "having mixed together; having combined different categories",
      pt: "tendo mesclado; tendo combinado diferentes categorias conceituais e reais",
      es: "habiendo mezclado; habiendo combinado diversas categorías"
    },
    grammar: "absolutivo, vi + ava + √mis + e + tvā",
    root: "vi + ava + √mis (misturar) + tvā"
  },
  {
    pali: "alobhādīhi",
    meaning: {
      en: "by means of non-greed and the other beautiful roots (instrumental plural)",
      pt: "por meio do desapego (alobha) e das demais raízes benéficas (instrumental plural)",
      es: "por medio del desapego (alobha) y las demás raíces beneficiosas (instrumental plural)"
    },
    grammar: "adj. instr. pl., a + lobha + ādi + ehi",
    root: "a + √lubh + ādi + ehi"
  },
  {
    pali: "tisattati",
    meaning: {
      en: "seventy-three (73)",
      pt: "setenta e três (73)",
      es: "setenta y tres (73)"
    },
    grammar: "numeral cardinal, ti + sattati",
    root: "ti (3) + sattati (70)"
  },
  {
    pali: "tepaññāsa",
    meaning: {
      en: "fifty-three (53)",
      pt: "cinquenta e três (53)",
      es: "cincuenta y tres (53)"
    },
    grammar: "numeral cardinal, te + paññāsa",
    root: "te (3) + paññāsa (50)"
  },
  {
    pali: "catupaññāsa",
    meaning: {
      en: "fifty-four (54); especially the 54 sense-sphere consciousnesses (kāmāvacara-cittāni)",
      pt: "cinquenta e quatro (54); em especial as 54 consciências da esfera dos sentidos (kāmāvacara-cittāni)",
      es: "cincuenta y cuatro (54); en especial las 54 conciencias de la esfera de los sentidos"
    },
    grammar: "numeral cardinal, catu + paññāsa",
    root: "catu (4) + paññāsa (50)"
  },
  {
    pali: "ekūnasaṭṭhi",
    meaning: {
      en: "fifty-nine (59); especially the 59 beautiful consciousnesses (sobhana-cittāni)",
      pt: "cinquenta e nove (59); em especial as 59 consciências belas (sobhana-cittāni)",
      es: "cincuenta y nueve (59); en especial las 59 conciencias bellas"
    },
    grammar: "numeral cardinal, eka + ūna + saṭṭhi",
    root: "eka (1) + ūna (menos) + saṭṭhi (60)"
  },
  {
    pali: "chasaṭṭhi",
    meaning: {
      en: "sixty-six (66)",
      pt: "sessenta e seis (66)",
      es: "sesenta y seis (66)"
    },
    grammar: "numeral cardinal, cha + saṭṭhi",
    root: "cha (6) + saṭṭhi (60)"
  },
  {
    pali: "upaḍḍhakappo",
    meaning: {
      en: "half an aeon / half a cosmic cycle (kappa)",
      pt: "meio eon; metade de um ciclo cósmico (kappa)",
      es: "medio eón; la mitad de un ciclo cósmico (kappa)"
    },
    grammar: "m. nom. sg., upaḍḍha + kappa",
    root: "upaḍḍha (metade) + kappa (ciclo cósmico/eon)"
  },
  {
    pali: "nopalabbhanti",
    meaning: {
      en: "are not found; do not obtain (na + upalabbhanti)",
      pt: "não são obtidos; não são encontrados na realidade última (na + upalabbhanti)",
      es: "no se encuentran; no son obtenidos (na + upalabbhanti)"
    },
    grammar: "sandhi verbal, na + upalabbhanti",
    root: "na + upa + √labh + ya + nti"
  },
  {
    pali: "tamanantaritvā",
    meaning: {
      en: "immediately following that; contiguous without interruption",
      pt: "imediatamente após aquilo; sucedendo de forma contígua sem intervalo",
      es: "inmediatamente después de aquello; sucediendo sin interrupción"
    },
    grammar: "absolutivo, taṃ + anantara + itvā",
    root: "taṃ + an + antara + itvā"
  },
  {
    pali: "tamevārammaṇamārabbha",
    meaning: {
      en: "taking precisely that same cognitive object as its basis (taṃ + eva + ārammaṇaṃ + ārabbha)",
      pt: "tomando precisamente aquele mesmíssimo objeto cognitivo como base (taṃ + eva + ārammaṇaṃ + ārabbha)",
      es: "tomando precisamente ese mismo objeto cognitivo como base"
    },
    grammar: "composto sandhi frasal, taṃ + eva + ārammaṇaṃ + ārabbha",
    root: "taṃ + eva + ārammaṇa + ā + √rabh + tvā"
  },
  {
    pali: "tammūlakāni",
    meaning: {
      en: "having that as their root; originating from those roots (plural neuter)",
      pt: "tendo aquilo como raiz; originados daquelas mesmas raízes (neutro plural)",
      es: "teniendo aquello como raíz; originados de esas raíces (plural)"
    },
    grammar: "adj. nom./acc. pl. nt., taṃ + mūla + ka",
    root: "taṃ + mūla (raiz) + ka + āni"
  },
  {
    pali: "sopekkhaṃ",
    meaning: {
      en: "accompanied by equanimity (sa + upekkhā)",
      pt: "acompanhado de equanimidade neutra (sa + upekkhā)",
      es: "acompañado de ecuanimidad (sa + upekkhā)"
    },
    grammar: "adj. / nt. acc. sg., sa + upekkhā",
    root: "sa + upa + √ikkha"
  },
  {
    pali: "duvaṅgikaṃ",
    meaning: {
      en: "having two factors; two-factored",
      pt: "tendo dois fatores; composto de dois constituintes",
      es: "que tiene dos factores; compuesto de dos miembros"
    },
    grammar: "adj. / nt., dvi > du + aṅga + ika",
    root: "du (2) + aṅga (fator) + ika"
  },
  {
    pali: "tivaṅgikaṃ",
    meaning: {
      en: "having three factors; three-factored",
      pt: "tendo três fatores; composto de três membros",
      es: "que tiene tres factores; de tres miembros"
    },
    grammar: "adj. / nt., ti + aṅga + ika",
    root: "ti (3) + aṅga (fator) + ika"
  },
  {
    pali: "sikhāppattā",
    meaning: {
      en: "having reached the culmination/zenith; perfected at the peak",
      pt: "tendo alcançado a culminância ou o ápice; aperfeiçoado no zênite meditativo",
      es: "que ha alcanzado la culminación o cenit; perfeccionado en la cúspide"
    },
    grammar: "adj. nom. pl., sikhā + patta",
    root: "sikhā (ápice/crista) + pra + √āp > patta (alcançado)"
  },
  {
    pali: "āvajjeti",
    meaning: {
      en: "adverts to; directs attention toward an object (the mental function of adverting, āvajjana)",
      pt: "adverte para; orienta a atenção da mente em direção a um objeto (a função de āvajjana)",
      es: "advierte hacia; dirige la atención hacia un objeto mental o sensorial"
    },
    grammar: "v. 3ª sg. pres., ā + √vajj",
    root: "ā + √vajj (virar/inclinar) + e + ti"
  },
  {
    pali: "kammānurūpato",
    meaning: {
      en: "according to the nature/quality of one's actions (kamma)",
      pt: "segundo a natureza correspondente das próprias ações (kamma)",
      es: "según la naturaleza y correspondencia de las propias acciones (kamma)"
    },
    grammar: "adv. ablativo, kamma + anurūpa + to",
    root: "kamma + anu + rūpa + to"
  },
  {
    pali: "pannarasīraye",
    meaning: {
      en: "fifteen are declared (pannarasa + īraye)",
      pt: "quinze são declarados / explicados pelos Mestres (pannarasa + īraye)",
      es: "quince son declarados por los maestros (pannarasa + īraye)"
    },
    grammar: "frase métrica, pannarasa + īrayi",
    root: "pañca + dasa + √īr (proferir)"
  },
  {
    pali: "katvekekantu",
    meaning: {
      en: "having taken each one individually (katvā + eka-ekaṃ + tu)",
      pt: "tendo tomado cada um individualmente (katvā + eka-ekaṃ + tu)",
      es: "habiendo tomado cada uno individualmente (katvā + eka-ekaṃ + tu)"
    },
    grammar: "sandhi de verso, katvā + ekekaṃ + tu",
    root: "√kar + tvā + eka + eka + tu"
  },
  {
    pali: "alamatippapañcena",
    meaning: {
      en: "enough with excessive elaboration / proliferation (alaṃ + ati-papañca)",
      pt: "basta de proliferação ou elaboração excessiva (fórmula de concisão canônica dos tratados)",
      es: "basta de proliferación o elaboración excesiva (fórmula de concisión canónica)"
    },
    grammar: "expressão idiomática, alaṃ + ati + papañca + ina",
    root: "alaṃ (basta) + ati + pa + √pañc (proliferar) + ena"
  },
  {
    pali: "alamativisāraṇiyā",
    meaning: {
      en: "enough of excessive diffusion / expansion",
      pt: "basta de expansão e dispersão textual excessiva",
      es: "basta de difusión o expansión excesiva"
    },
    grammar: "expressão instrumental, alaṃ + ati + visāraṇī",
    root: "alaṃ + ati + vi + √sar (estender) + anā + iyā"
  },
  {
    pali: "racayissāmi",
    meaning: {
      en: "I shall compose; I will author (Ācariya Anuruddha's declaration in opening verse)",
      pt: "comporei; hei de redigir (declaração solene do Venerável Ācariya Anuruddha no verso de abertura)",
      es: "compondré; redactaré (declaración solemne del Venerable Anuruddha)"
    },
    grammar: "v. 1ª sg. futuro, √rac + aya + issāmi",
    root: "√rac (compor/ordenar) + issāmi"
  },
  {
    pali: "sasaddhammagaṇuttama",
    meaning: {
      en: "together with the sublime Sangha of the True Dhamma (homage to the Triple Gem)",
      pt: "juntamente com o supremo Nobre Sangha do Verdadeiro Dhamma (verso de veneração à Joia Tríplice)",
      es: "junto con la suprema Sangha del Verdadero Dhamma (homenaje a la Triple Joya)"
    },
    grammar: "composto honorífico acusativo, sa + saddhamma + gaṇa + uttama",
    root: "sa + sat + dhamma + gaṇa + ud + tama"
  },
  {
    pali: "munindena",
    meaning: {
      en: "by the Lord of Sages; by the Buddha (instrumental singular)",
      pt: "pelo Soberano dos Sábios; pelo Nobre Buda (instrumental singular)",
      es: "por el Soberano de los Sabios; por el Buda (instrumental singular)"
    },
    grammar: "m. instr. sg., muni + inda + ina",
    root: "muni (sábio) + inda (senhor) + ina"
  }
];

// Adiciona os novos verbetes
let added = 0;
for (const item of abhidhammaAdditions) {
  const key = item.pali.toLowerCase().trim();
  if (!existingPali.has(key)) {
    dict.push(item);
    existingPali.add(key);
    added++;
  }
}

// Salva de volta
fs.writeFileSync(dictPath, JSON.stringify(dict, null, 2), 'utf8');
console.log(`Adicionados ${added} novos verbetes canônicos eruditos do Abhidhamma. Total no dicionário: ${dict.length}`);

import fs from 'fs';

const dictPath = './src/data/paliDictionary.json';
const dict = JSON.parse(fs.readFileSync(dictPath, 'utf8'));
const existingPali = new Set(dict.map((d) => d.pali.toLowerCase().trim()));

const batch3 = [
  {
    pali: "avacarati",
    meaning: {
      en: "frequents; moves about in; operates within (the sphere of existence, plane or realm)",
      pt: "frequenta; atua em; move-se dentro de (uma esfera de existência ou plano cognitivo, de onde provém kāmāvacara, rūpāvacara, arūpāvacara)",
      es: "frecuenta; opera dentro de; se mueve en una esfera de existencia o plano cognitivo"
    },
    grammar: "v. 3ª sg. pres., ava + √car",
    root: "ava + √car (mover-se/agir) + a + ti"
  },
  {
    pali: "avacaratīti",
    meaning: {
      en: "operates within, thus (avacarati + iti; classical Abhidhamma definition of 'āvacara')",
      pt: "atua dentro de, assim citado (avacarati + iti; definição etimológica clássica de 'āvacara' na Vibhāvinī-ṭīkā)",
      es: "opera dentro de, así citado (definición etimológica de āvacara)"
    },
    grammar: "sandhi com citação iti, avacarati + iti",
    root: "ava + √car + ti + iti"
  },
  {
    pali: "cinoti",
    meaning: {
      en: "accumulates; heaps up; gathers (actions, kamma, or mental formations)",
      pt: "acumula; amontoa; reúne (ações volitivas, kamma e formações mentais que geram renascimento)",
      es: "acumula; amontona; junta (acciones kármicas o formaciones mentales)"
    },
    grammar: "v. 3ª sg. pres., √ci",
    root: "√ci (acumular/juntar) + no + ti"
  },
  {
    pali: "cikicchā",
    meaning: {
      en: "remedy; therapeutics; spiritual curing of mental defilements",
      pt: "remédio; terapêutica medicinal; a cura espiritual e erradicação das contaminações mentais pelo Nobre Dhamma",
      es: "remedio; terapéutica; curación espiritual de las impurezas mentales"
    },
    grammar: "f. (subst. desiderativo), de √kit / √ci",
    root: "√kit (curar) + sa + ā"
  },
  {
    pali: "cikicchituṃ",
    meaning: {
      en: "to heal; to cure; to apply therapeutic remedy to",
      pt: "para curar; para aplicar o remédio espiritual às aflições da mente",
      es: "para curar; para aplicar remedio a las aflicciones"
    },
    grammar: "infinitivo, de √kit",
    root: "√kit + sa + ituṃ"
  },
  {
    pali: "kicchati",
    meaning: {
      en: "is troubled; suffers hardship; struggles with difficulty",
      pt: "passa por tribulações; experimenta dificuldade e aflição",
      es: "padece dificultad; sufre penalidad"
    },
    grammar: "v. 3ª sg. pres., √kiccha",
    root: "√kiccha (esforçar-se/afligir-se) + a + ti"
  },
  {
    pali: "cakkhati",
    meaning: {
      en: "tastes; relishes; perceives flavors (sensory cognition)",
      pt: "degusta; saboreia; percebe o sabor (cognição sensorial gustativa)",
      es: "saborea; degusta; percibe el sabor"
    },
    grammar: "v. 3ª sg. pres., √cakkh",
    root: "√cakkh (saborear) + a + ti"
  },
  {
    pali: "cakkhatī",
    meaning: {
      en: "tastes; savors (metrical variant with long vowel)",
      pt: "degusta; prova (variante métrica com vogal longa)",
      es: "saborea; degusta"
    },
    grammar: "v. 3ª sg. pres.",
    root: "√cakkh + a + tī"
  },
  {
    pali: "cakkhatīti",
    meaning: {
      en: "tastes, thus quoted (cakkhati + iti)",
      pt: "degusta, assim definido (cakkhati + iti)",
      es: "saborea, así definido"
    },
    grammar: "sandhi, cakkhati + iti",
    root: "√cakkh + ti + iti"
  },
  {
    pali: "ikkhati",
    meaning: {
      en: "looks at; beholds; observes with awareness",
      pt: "olha; contempla; observa com atenção visual",
      es: "mira; contempla; observa con atención"
    },
    grammar: "v. 3ª sg. pres., √ikkh",
    root: "√ikkh (olhar/ver) + a + ti"
  },
  {
    pali: "ikkhā",
    meaning: {
      en: "vision; viewing; looking; observing",
      pt: "visão; observação; contemplação direta",
      es: "visión; observación; contemplación"
    },
    grammar: "f., √ikkh + ā",
    root: "√ikkh + ā"
  },
  {
    pali: "phusanaṃ",
    meaning: {
      en: "touching; contacting; the tactile experience and essential function of phassa (contact)",
      pt: "o tocar; o contato; a experiência tátil e a função essencial do fator mental phassa (contato mental)",
      es: "el tocar; el contacto; la función esencial del factor mental phassa"
    },
    grammar: "nt. nom./acc. sg., √phus + ana",
    root: "√phus (tocar/contatar) + ana"
  },
  {
    pali: "anubhavananti",
    meaning: {
      en: "they experience; they undergo; they taste the fruition of kamma",
      pt: "experimentam; vivenciam; sentem o resultado e fruição das ações (kamma-vipāka)",
      es: "experimentan; vivencian; degustan la fruición del kamma"
    },
    grammar: "v. 3ª pl. pres., anu + √bhū",
    root: "anu + √bhū (experimentar) + a + nti"
  },
  {
    pali: "anubhavane",
    meaning: {
      en: "in the experiencing; in the process of tasting the object through feeling (vedanā)",
      pt: "na vivência; na experiência de sentir e desfrutar o objeto através da sensação (vedanā, locativo singular)",
      es: "en el experimentar; en la vivencia de sentir el objeto a través de vedanā"
    },
    grammar: "nt. loc. sg., anu + √bhū + ana + e",
    root: "anu + √bhū + ana + e"
  },
  {
    pali: "pīnanaṃ",
    meaning: {
      en: "refreshing; exhilaration; the characteristic nature of joy/rapture (pīti-cetasika)",
      pt: "o ato de refrescar e revitalizar; a característica intrínseca do enlevo meditativo (pīti-cetasika)",
      es: "el refrescar y revitalizar; la característica intrínseca del gozo meditativo (pīti)"
    },
    grammar: "nt., √pī + ana",
    root: "√pī (refrescar/regozijar) + ana"
  },
  {
    pali: "pinayati",
    meaning: {
      en: "gladdens; delights; invigorates the mind and body",
      pt: "regozija; alegra; infunde ânimo e vigor na mente e no corpo",
      es: "alegra; deleita; infunde vigor en la mente"
    },
    grammar: "v. 3ª sg. pres., √pī",
    root: "√pī + naya + ti"
  },
  {
    pali: "tappeti",
    meaning: {
      en: "satiates; satisfies; brings contentment to the mind",
      pt: "sacia; gratifica plenamente; produz contentamento contemplativo",
      es: "sacia; satisface; brinda contentamiento a la mente"
    },
    grammar: "v. 3ª sg. pres. caus., √tapp",
    root: "√tapp (satisfazer) + e + ti"
  },
  {
    pali: "upabrūhanaṃ",
    meaning: {
      en: "augmenting; strengthening; fostering wholesome mental states",
      pt: "o ato de nutrir, robustecer e fortalecer os estados mentais benéficos (kusala dhammas)",
      es: "el nutrir, fortalecer e incrementar los estados benéficos"
    },
    grammar: "nt., upa + √brūh + ana",
    root: "upa + √brūh (crescer/aumentar) + ana"
  },
  {
    pali: "palobhitassa",
    meaning: {
      en: "of one who is seduced / allured by greed and sensual objects (genitive singular)",
      pt: "daquele que é seduzido, atraído e iludido pela cobiça e pelos objetos sensoriais (genitivo singular)",
      es: "de aquel que es seducido por la codicia y los objetos sensoriales"
    },
    grammar: "part. pass. gen. sg., pa + √lubh + ita + assa",
    root: "pa + √lubh (cobiçar) + ita + assa"
  },
  {
    pali: "paribbhamanaṃ",
    meaning: {
      en: "wandering; revolving; turning round in the continuous cycle of saṃsāra",
      pt: "o vagar; o giro contínuo e a transmigração incessante na roda de saṃsāra",
      es: "el vagar o girar incesante en la rueda del saṃsāra"
    },
    grammar: "nt., pari + √bham + ana",
    root: "pari + √bham (girar/vagar) + ana"
  },
  {
    pali: "paribbhamantassa",
    meaning: {
      en: "of one wandering / revolving through existence (genitive singular participle)",
      pt: "daquele que vaga e gira na transmigração (genitivo singular do particípio presente)",
      es: "de aquel que vaga en la transmigración de existencias"
    },
    grammar: "part. pres. gen. sg., pari + √bham + anta + assa",
    root: "pari + √bham + nta + assa"
  },
  {
    pali: "duvaṅgikanti",
    meaning: {
      en: "two-factored, thus (duvaṅgikaṃ + iti)",
      pt: "constituído de dois fatores, assim declarado (duvaṅgikaṃ + iti)",
      es: "constituido por dos factores, así declarado"
    },
    grammar: "sandhi, duvaṅgikaṃ + iti",
    root: "du + aṅga + ika + aṃ + iti"
  },
  {
    pali: "avisesena",
    meaning: {
      en: "without distinction; universally; generally without differentiation",
      pt: "sem distinção; universalmente; de modo geral e indistinto",
      es: "sin distinción; universalmente; de manera general"
    },
    grammar: "adv. instrumental, a + visesa + ina",
    root: "a + vi + √sis + a + ina"
  },
  {
    pali: "abhedepi",
    meaning: {
      en: "even where there is no difference / division (abhede + api)",
      pt: "mesmo na ausência de divisão ou diferenciação substancial (abhede + api)",
      es: "incluso cuando no hay división o diferencia"
    },
    grammar: "sandhi locativo, a + bheda + e + api",
    root: "a + √bhid + a + e + api"
  },
  {
    pali: "asambhavato",
    meaning: {
      en: "because of the impossibility / non-occurrence of such a condition",
      pt: "em razão da impossibilidade ontológica ou não-ocorrência da condição (ablativo causal)",
      es: "debido a la imposibilidad o no ocurrencia de tal condición"
    },
    grammar: "adv. ablativo, a + sambhava + to",
    root: "a + sam + √bhū + a + to"
  },
  {
    pali: "tammūlakānañca",
    meaning: {
      en: "and of those rooted in that (tammūlakānaṃ + ca)",
      pt: "e daqueles que têm sua raiz nisso (tammūlakānaṃ + ca)",
      es: "y de aquellos que tienen su raíz en ello"
    },
    grammar: "sandhi genitivo plural, taṃ + mūlaka + ānaṃ + ca",
    root: "tad + mūla + ka + ānaṃ + ca"
  },
  {
    pali: "kesādīnaṃ",
    meaning: {
      en: "of the 32 bodily parts beginning with hair of the head (kesa + ādi + inaṃ)",
      pt: "das partes corpóreas encabeçadas pelos cabelos (kesa + ādi + inaṃ; objeto clássico de meditação das 32 partes)",
      es: "de las partes corporales encabezadas por los cabellos (meditación de las 32 partes)"
    },
    grammar: "gen. pl., kesa + ādi + inaṃ",
    root: "kesa (cabelo) + ādi (e outros) + inaṃ"
  },
  {
    pali: "parihāpetvā",
    meaning: {
      en: "having caused to decline; having omitted or set aside",
      pt: "tendo feito declinar; tendo excluído ou deixado de lado",
      es: "habiendo hecho declinar; habiendo omitido o apartado"
    },
    grammar: "absolutivo causativo, pari + √hā + ape + tvā",
    root: "pari + √hā (abandonar/diminuir) + tvā"
  },
  {
    pali: "anuravo",
    meaning: {
      en: "reverberation; echo; resonance (in auditory sensory process)",
      pt: "ressonância; eco sonoro (no processo perceptivo da audição / sota-dvāra-vīthi)",
      es: "resonancia; eco (en el proceso de percepción auditiva)"
    },
    grammar: "m. nom. sg., anu + √ru + a + o",
    root: "anu + √ru (ressoar/fazer som) + a"
  },
  {
    pali: "anusañcaraṇaṃ",
    meaning: {
      en: "traversing; moving across sequentially through the cognitive doors",
      pt: "o percorrer sucessivo; o trânsito da mente através das portas cognitivas",
      es: "el transitar sucesivo a través de las puertas cognitivas"
    },
    grammar: "nt., anu + sam + √car + ana",
    root: "anu + sam + √car (caminhar) + ana"
  },
  {
    pali: "āraṇanumajjanalakkhaṇo",
    meaning: {
      en: "having the characteristic of repeatedly touching and stroking the object (definition of vicāra)",
      pt: "que possui a característica de examinar e acariciar continuamente o objeto (definição canônica de vicāra na Vibhāvinī)",
      es: "que tiene la característica de examinar y recorrer continuamente el objeto (definición de vicāra)"
    },
    grammar: "composto bahubbīhi, āraṇa + anumajjana + lakkhaṇa + o",
    root: "ā + √ram + anu + √majj + ana + lakkhaṇa"
  },
  {
    pali: "saṅghaṭṭitampi",
    meaning: {
      en: "even when struck / impacted against the sense-base (saṅghaṭṭita + api)",
      pt: "mesmo quando impactado / atingido contra a base sensorial (saṅghaṭṭita + api, como o som no ouvido)",
      es: "incluso cuando impacta contra la base sensorial"
    },
    grammar: "sandhi, saṅghaṭṭita + api",
    root: "sam + √ghaṭṭ (golpear/chocar) + ita + api"
  },
  {
    pali: "visesitabbāni",
    meaning: {
      en: "which ought to be specially distinguished and classified (gerundive neuter plural)",
      pt: "que devem ser especialmente distinguidos e categorizados (gerundivo neutro plural)",
      es: "que deben ser distinguidos y categorizados especialmente"
    },
    grammar: "gerundivo nt. pl., vi + √sis + e + tabba + āni",
    root: "vi + √sis (distinguir) + tabba + āni"
  },
  {
    pali: "niddisanto",
    meaning: {
      en: "pointing out; demonstrating; illustrating canonically (present participle)",
      pt: "apontando; demonstrando e esclarecendo canonicamente (particípio presente)",
      es: "señalando; demostrando y aclarando canónicamente"
    },
    grammar: "part. pres. m. nom. sg., ni + √dis + a + nta",
    root: "ni + √dis (mostrar) + nta"
  },
  {
    pali: "niddisīyatīti",
    meaning: {
      en: "is demonstrated, thus quoted (niddisīyati + iti)",
      pt: "é demonstrado / exposto, assim citado (niddisīyati + iti)",
      es: "es demostrado, así citado"
    },
    grammar: "sandhi passivo, ni + √dis + ya + ti + iti",
    root: "ni + √dis + ya + ti + iti"
  },
  {
    pali: "vandathā",
    meaning: {
      en: "revere; pay homage to (imperative/optative)",
      pt: "prestai reverência; venerai com devoção",
      es: "venerad; rendid homenaje con devoción"
    },
    grammar: "v. 2ª pl. imperativo, √vand",
    root: "√vand (venerar) + a + thā"
  },
  {
    pali: "kamuddiseyya",
    meaning: {
      en: "whom would one point to; what would one indicate (kaṃ + uddiseyya)",
      pt: "a quem se apontaria; o que se indicaria doutrinariamente (kaṃ + uddiseyya)",
      es: "¿a quién señalaría uno?; ¿qué se indicaría?"
    },
    grammar: "sandhi de verso, kaṃ + ud + √dis + eyya",
    root: "kaṃ + ud + √dis (apontar) + eyya"
  },
  {
    pali: "vikāsamanuppattotyattho",
    meaning: {
      en: "having arrived at full expansion, that is the meaning (vikāsaṃ + anuppatto + iti + attho)",
      pt: "tendo alcançado plena expansão e desabrochar, este é o significado pretendido (vikāsaṃ + anuppatto + iti + attho)",
      es: "habiendo alcanzado plena expansión, tal es el significado"
    },
    grammar: "frase exegética condensada",
    root: "vi + √kas + anu + pra + √āp + iti + attha"
  },
  {
    pali: "pavatthānantaruppanna",
    meaning: {
      en: "arisen immediately contiguous to that very state without interval (pavatta + anantara + uppanna)",
      pt: "surgido imediatamente contíguo àquele estado sem qualquer intervalo de tempo (pavatta + anantara + uppanna)",
      es: "surgido inmediatamente contiguo a ese estado sin intervalo"
    },
    grammar: "composto adverbial de contiguidade",
    root: "pa + √vatt + an + antara + ud + √pad"
  },
  {
    pali: "byabhicāre",
    meaning: {
      en: "in deviation; in irregularity; in variable exception",
      pt: "no desvio; na exceção ou irregularidade condicional (locativo singular)",
      es: "en la desviación o excepción condicional"
    },
    grammar: "m. loc. sg., vi + ati + √car + a + e",
    root: "vi + ati + √car (desviar) + e"
  },
  {
    pali: "vippaṭipattiyopi",
    meaning: {
      en: "even wrong practices; even erroneous interpretations (vippaṭipattiyo + api)",
      pt: "mesmo as práticas errôneas ou desvios de conduta e interpretação (vippaṭipattiyo + api)",
      es: "incluso las prácticas erróneas o desviaciones"
    },
    grammar: "sandhi nom. pl. fem., vi + paṭi + √pad + ti + api",
    root: "vi + paṭi + √pad + ti + api"
  },
  {
    pali: "virodhisattesupi",
    meaning: {
      en: "even toward hostile or opposing beings (locative plural)",
      pt: "mesmo para com os seres adversos ou hostis (como na prática do amor-bondade / mettā, locativo plural)",
      es: "incluso hacia los seres adversos u hostiles"
    },
    grammar: "composto sandhi loc. pl., virodhi + satta + esu + api",
    root: "vi + √rudh + in + satta + esu + api"
  },
  {
    pali: "āgatoti",
    meaning: {
      en: "arrived; passed down in canonical transmission, thus (āgato + iti)",
      pt: "transmitido; registrado na linhagem textual canônica, assim citado (āgato + iti)",
      es: "transmitido; registrado en la tradición textual, así citado"
    },
    grammar: "sandhi, āgata + o + iti",
    root: "ā + √gam > gata + iti"
  },
  {
    pali: "apatamāne",
    meaning: {
      en: "in that which does not fall down / does not lapse (locative singular)",
      pt: "naquilo que não decai nem tomba na degradação (locativo singular)",
      es: "en aquello que no decae ni cae en degradación"
    },
    grammar: "part. pres. loc. sg., a + √pat + a + māna + e",
    root: "a + √pat (cair) + māna + e"
  },
  {
    pali: "niyuttaṃ",
    meaning: {
      en: "appointed; assigned; attached to a duty",
      pt: "designado; atribuído; encarregado de uma função cognitiva específica",
      es: "designado; asignado a una función cognoscitiva"
    },
    grammar: "part. pass. nt., ni + √yuj + ta",
    root: "ni + √yuj (ligar/designar) + ta"
  },
  {
    pali: "vinanato",
    meaning: {
      en: "by bowing; by bending in humility and reverent homage (ablative/adverbial)",
      pt: "pela inclinação humilde e prostração de reverência ao Tríplice Refúgio",
      es: "mediante la inclinación reverente y postración devota"
    },
    grammar: "adv. ablativo, vi + √nam + ana + to",
    root: "vi + √nam (curvar/inclinar) + ana + to"
  },
  {
    pali: "pothiyamāno",
    meaning: {
      en: "being beaten; being crushed by suffering or defilements (present passive participle)",
      pt: "sendo afligido; sendo esmagado pelas tribulações do ciclo existencial",
      es: "siendo afligido; siendo golpeado por los sufrimientos"
    },
    grammar: "part. pres. pass. m. nom. sg., √puth / √poth + iya + māna",
    root: "√puth (golpear) + iya + māna + o"
  },
  {
    pali: "paṭippaharituṃ",
    meaning: {
      en: "to strike back; to counteract; to ward off assaults",
      pt: "para contra-atacar; para neutralizar as investidas de Māra e das contaminações",
      es: "para contraatacar; para neutralizar los asaltos de las impurezas"
    },
    grammar: "infinitivo, paṭi + pra + √har + ituṃ",
    root: "paṭi + pa + √har (golpear) + ituṃ"
  },
  {
    pali: "paridubbalabhāvato",
    meaning: {
      en: "due to extreme feebleness / weakness of mental faculties",
      pt: "em razão da extrema debilidade e fraqueza das faculdades mentais (ablativo causal)",
      es: "debido a la extrema debilidad de las facultades mentales"
    },
    grammar: "adv. ablativo, pari + dubbala + bhāva + to",
    root: "pari + dur + bala + bhāva + to"
  },
  {
    pali: "tiṭṭhantampī",
    meaning: {
      en: "even that which is persisting / enduring (tiṭṭhantaṃ + api)",
      pt: "mesmo aquilo que está presente e persistindo temporariamente (tiṭṭhantaṃ + api)",
      es: "incluso lo que permanece o persiste temporalmente"
    },
    grammar: "sandhi, tiṭṭhantaṃ + api",
    root: "√ṭhā > tiṭṭha + nta + api"
  },
  {
    pali: "sānato",
    meaning: {
      en: "from attachment; from craving that binds (sāna + to)",
      pt: "a partir do apego e da afeição que ata a consciência ao ciclo (ablativo)",
      es: "a partir del apego y aferramiento que ata al ciclo"
    },
    grammar: "ablativo, sāna + to",
    root: "√sā (atar) + ana + to"
  },
  {
    pali: "vibha",
    meaning: {
      en: "radiance; splendor; analytical division (abbreviation/root form in compounds)",
      pt: "esplendor; radiância luminosa; divisão analítica (forma raiz de vibhā / vibhatti)",
      es: "esplendor; fulgor; división analítica"
    },
    grammar: "f. / prefixo, vi + √bhā",
    root: "vi + √bhā (brilhar/iluminar)"
  }
];

let added3 = 0;
for (const item of batch3) {
  const key = item.pali.toLowerCase().trim();
  if (!existingPali.has(key)) {
    dict.push(item);
    existingPali.add(key);
    added3++;
  }
}

fs.writeFileSync(dictPath, JSON.stringify(dict, null, 2), 'utf8');
console.log(`Lote 3 adicionado: ${added3} verbetes. Total no dicionário: ${dict.length}`);

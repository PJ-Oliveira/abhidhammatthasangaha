import fs from 'fs';

const dictPath = './src/data/paliDictionary.json';
const dict = JSON.parse(fs.readFileSync(dictPath, 'utf8'));
const existingPali = new Set(dict.map((d) => d.pali.toLowerCase().trim()));

const batch2 = [
  {
    pali: "vikkhittakaṃ",
    meaning: {
      en: "a scattered corpse; one of the ten foul/decayed bodily subjects of meditation (asubha-kammaṭṭhāna) in Chapter 9",
      pt: "o cadáver disperso / esquartejado; um dos dez objetos de contemplação da impureza corpórea (asubha-kammaṭṭhāna) no Capítulo 9",
      es: "el cadáver esparcido; uno de los diez objetos de impureza corporal en la meditación (asubha-kammaṭṭhāna) del Capítulo 9"
    },
    grammar: "nt. nom./acc. sg., vi + √khip + ta + ka",
    root: "vi + √khip (espalhar/dispersar) + ta + ka"
  },
  {
    pali: "vikkhāyitakaṃ",
    meaning: {
      en: "a gnawed/worm-eaten corpse; one of the ten foul subjects of meditation (asubha-kammaṭṭhāna) in Chapter 9",
      pt: "o cadáver roído / devorado por vermes e feras; um dos dez objetos de meditação sobre a impureza (asubha-kammaṭṭhāna) no Capítulo 9",
      es: "el cadáver roído o devorado por alimañas; uno de los diez objetos de impureza (asubha-kammaṭṭhāna)"
    },
    grammar: "nt. nom./acc. sg., vi + √khāy + ita + ka",
    root: "vi + √khād (comer/roer) + ita + ka"
  },
  {
    pali: "samuggahitaṃ",
    meaning: {
      en: "thoroughly grasped; masterfully acquired and comprehended (sam + ud + √gah)",
      pt: "perfeitamente apreendido; adquirido e compreendido com domínio completo (sam + ud + √gah)",
      es: "completamente aprehendido; adquirido y comprendido con maestría"
    },
    grammar: "part. pass. nt., sam + ud + √gah + ita",
    root: "sam + ud + √gah (segurar/aprender) + ita"
  },
  {
    pali: "saṅkhipitvā",
    meaning: {
      en: "having summarized; having condensed concisely into a compendium",
      pt: "tendo sintetizado; tendo condensado de forma concisa em compêndio (saṅkhepa)",
      es: "habiendo sintetizado; habiendo condensado en un compendio"
    },
    grammar: "absolutivo, sam + √khip + tvā",
    root: "sam + √khip (lançar/resumir) + tvā"
  },
  {
    pali: "paridīpitā",
    meaning: {
      en: "illuminated; clearly explained and expounded (past participle nominative plural/feminine)",
      pt: "elucidados; claramente expostos e clarificados (particípio passado passivo)",
      es: "esclarecidos; claramente explicados y expuestos"
    },
    grammar: "part. pass., pari + √dīp + ita + ā",
    root: "pari + √dīp (iluminar/explicar) + ita"
  },
  {
    pali: "parikappiyamānā",
    meaning: {
      en: "being conceptualized; being conceptually constructed or imagined",
      pt: "sendo concebidos mentalmente; imaginados ou construídos como conceitos (paññatti)",
      es: "siendo conceptualizados o imaginados como construcciones mentales"
    },
    grammar: "part. pres. pass., pari + √kapp + iya + māna + ā",
    root: "pari + √kapp (construir/imaginar) + māna"
  },
  {
    pali: "vocchijjitvā",
    meaning: {
      en: "having been cut off; having been terminated in continuity",
      pt: "tendo sido cortado; interrompido na sua continuidade",
      es: "habiendo sido cortado o interrumpido en su flujo"
    },
    grammar: "absolutivo passivo, vi + ud + √chid + ya + tvā",
    root: "vi + ud + √chid (cortar) + tvā"
  },
  {
    pali: "vibhāvento",
    meaning: {
      en: "elucidating; explaining distinctly (the celebrated function of the Abhidhammatthavibhāvinī-ṭīkā)",
      pt: "elucidando; tornando manifesto com profunda clareza explicativa (verbo clássico da Abhidhammatthavibhāvinī-ṭīkā)",
      es: "elucidando; tornando manifiesto con claridad explicativa"
    },
    grammar: "part. pres. m. nom. sg., vi + √bhū + ape + nta",
    root: "vi + √bhū (tornar-se/manifestar) + ape + nta"
  },
  {
    pali: "vibhāvetīti",
    meaning: {
      en: "elucidates; makes clear, thus quoted",
      pt: "elucida; torna claro e inteligível, assim citado",
      es: "elucida; torna claro e inteligible, así citado"
    },
    grammar: "sandhi, vibhāveti + iti",
    root: "vi + √bhū + e + ti + iti"
  },
  {
    pali: "racitaṃ",
    meaning: {
      en: "composed; authored; written (past participle neuter)",
      pt: "composto; redigido; escrito (particípio passado neutro)",
      es: "compuesto; redactado; escrito (participio pasado)"
    },
    grammar: "part. pass. nt., √rac + ita",
    root: "√rac (compor) + ita"
  },
  {
    pali: "samuditena",
    meaning: {
      en: "by that which has arisen; through combined origination",
      pt: "por aquilo que se originou conjuntamente; pela gênese concomitante",
      es: "por lo que se ha originado conjuntamente; por la génesis conjunta"
    },
    grammar: "instr. sg., sam + ud + √i + ta + ina",
    root: "sam + ud + √i (surgir) + ta + ina"
  },
  {
    pali: "tammūlikāya",
    meaning: {
      en: "having that as its root cause (instrumental/dative feminine)",
      pt: "tendo aquilo como sua causa raiz originária (feminino instrumental/dativo)",
      es: "que tiene aquello como su causa raíz originaria"
    },
    grammar: "adj. f. instr., taṃ + mūla + ika + āya",
    root: "taṃ + mūla (raiz) + ika + āya"
  },
  {
    pali: "tassānubhāvena",
    meaning: {
      en: "by the power/potency of that (tassa + ānubhāvena)",
      pt: "pelo poder / pela eficácia intrínseca daquilo (tassa + ānubhāvena)",
      es: "por el poder o eficacia intrínseca de aquello"
    },
    grammar: "composto sandhi, tassa + ānubhāvena",
    root: "tad (aquilo) + ā + anu + √bhū + a + ena"
  },
  {
    pali: "paṭibāhitvā",
    meaning: {
      en: "having warded off; having repelled or eliminated obstacles",
      pt: "tendo repelido; tendo afastado ou eliminado os obstáculos e impedimentos mentais",
      es: "habiendo repelido o eliminado los obstáculos"
    },
    grammar: "absolutivo, paṭi + √bāh + e + tvā",
    root: "paṭi + √bāh (afastar) + tvā"
  },
  {
    pali: "anaññapaṭibodhito",
    meaning: {
      en: "due to direct awakening without relying on another; independently enlightened",
      pt: "devido à iluminação direta sem dependência alheia; por autorrealização soberana do Buda",
      es: "debido a la iluminación directa sin depender de otro"
    },
    grammar: "adv. ablativo, an + añña + paṭibodha + to",
    root: "na + añña (outro) + paṭi + √budh (despertar) + to"
  },
  {
    pali: "vikasitamiva",
    meaning: {
      en: "as if blossomed / unfolded like a blooming lotus (vikasita + iva)",
      pt: "como se desabrochasse; qual lótus plenamente aberto e florescido (vikasita + iva)",
      es: "como si floreciera; como un loto abierto (vikasita + iva)"
    },
    grammar: "sandhi comparativo, vikasita + iva",
    root: "vi + √kas (florescer) + ita + iva"
  },
  {
    pali: "vikasito",
    meaning: {
      en: "blossomed; fully opened; expanded (nominative singular masculine)",
      pt: "desabrochado; plenamente aberto e expandido (nominativo masculino)",
      es: "florecido; plenamente abierto y expandido"
    },
    grammar: "part. pass. m. nom. sg., vi + √kas + ita + o",
    root: "vi + √kas (abrir/florescer) + ita"
  },
  {
    pali: "asārakaṭṭhenā",
    meaning: {
      en: "in the sense of being unsubstantial / devoid of core (asāraka + aṭṭhena)",
      pt: "no sentido de ser desprovido de substância própria ou núcleo duradouro (asāraka + aṭṭhena, anattā)",
      es: "en el sentido de carecer de esencia o sustancia duradera (anattā)"
    },
    grammar: "sandhi instrumental, asāraka + atthena",
    root: "a + sāra (essência/núcleo) + ka + attha + ena"
  },
  {
    pali: "vhayena",
    meaning: {
      en: "by the name of; called; named (avhaya + ina)",
      pt: "chamado; designado pelo nome de (avhaya + ina)",
      es: "llamado; nombrado con la designación de"
    },
    grammar: "instr. sg., avhaya + ina",
    root: "ā + √hve (chamar) + a + ina"
  },
  {
    pali: "viññātave",
    meaning: {
      en: "to be understood; for the purpose of full comprehension (infinitive/gerundive)",
      pt: "para ser compreendido; a fim de se discernir plenamente",
      es: "para ser comprendido; con el fin de discernir plenamente"
    },
    grammar: "infinitivo védico / arcaico, vi + √ñā + tave",
    root: "vi + √ñā (conhecer) + tave"
  },
  {
    pali: "sādhippāyamahāpayaṃ",
    meaning: {
      en: "fulfilling the intended noble purpose with great clarity (opening/closing dedication)",
      pt: "realizando com grande clareza e magnitude a nobre intenção doutrinária do compêndio",
      es: "cumpliendo la noble intención con gran claridad y profundidad"
    },
    grammar: "composto acusativo de verso, sa + adhippāya + mahā + apaya",
    root: "sa + adhi + pra + √i + mahā + apaya"
  },
  {
    pali: "sotujanasamussāhajananatthaṃ",
    meaning: {
      en: "for the purpose of inspiring enthusiasm in the minds of hearers/students of Dhamma",
      pt: "com o propósito de inspirar entusiasmo e júbilo no coração dos ouvintes e estudantes do Nobre Dhamma",
      es: "con el fin de inspirar entusiasmo en los oyentes y estudiantes del Dhamma"
    },
    grammar: "composto final dativo/acusativo, sotujana + samussāha + janana + atthaṃ",
    root: "su (ouvir) + jana + sam + ud + √sah + √jan + attha"
  },
  {
    pali: "rogādiantarāyānamappavattiṃ",
    meaning: {
      en: "the non-occurrence of obstacles such as diseases and perils (blessing of protection)",
      pt: "a não-ocorrência de doenças, perigos e impedimentos à transmissão do Dhamma (bênção protetora)",
      es: "la no ocurrencia de enfermedades y peligros (bendición de protección)"
    },
    grammar: "composto acusativo de proteção, roga + ādi + antarāya + na + pavattiṃ",
    root: "roga + ādi + antarāya + a + pa + √vatt + ti"
  },
  {
    pali: "vicārādisukhumaṅgupattiyā",
    meaning: {
      en: "due to the arising of subtle factors such as discursive examination (vicāra) in meditative absorption",
      pt: "devido ao surgimento de fatores meditativos sutis como a sustentação reflexiva (vicāra) nos jhānas",
      es: "debido al surgimiento de factores meditativos sutiles como vicāra en los jhānas"
    },
    grammar: "composto causal ablativo/instrumental, vicāra + ādi + sukhuma + aṅga + uppatti + yā",
    root: "vi + √car + ādi + sukhuma + aṅga + ud + √pad + ti + yā"
  },
  {
    pali: "tathevekavisayañcekajātiyaṃ",
    meaning: {
      en: "likewise possessing a single object and belonging to a single class (tatheva + eka-visayaṃ + ca + eka-jātiyaṃ)",
      pt: "igualmente possuindo um único objeto cognitivo e pertencendo à mesma classe de consciência (tatheva + eka-visayaṃ + ca + eka-jātiyaṃ)",
      es: "asimismo teniendo un único objeto cognitivo y perteneciendo a la misma clase de conciencia"
    },
    grammar: "frase sintética de verso abhidhâmmico, tathā + eva + eka + visaya + ca + eka + jāti + yaṃ",
    root: "tathā + eva + eka + visaya + ca + eka + jāti"
  },
  {
    pali: "rūpādikamupaladdhapubbamupakaraṇabhūtañca",
    meaning: {
      en: "matter and other objects previously experienced that serve as auxiliary instruments/supports (complex samāsa)",
      pt: "a matéria e outros objetos cognitivos precedentemente apreendidos que atuam como instrumentos e suportes auxiliares (samāsa composto de condicionamento)",
      es: "la materia y otros objetos previamente percibidos que funcionan como soportes e instrumentos"
    },
    grammar: "composto abhidhâmmico extensivo, rūpādikaṃ + upaladdha-pubbaṃ + upakaraṇa-bhūtaṃ + ca",
    root: "rūpa + ādi + upa + √labh + pubba + upakaraṇa + √bhū + ca"
  },
  {
    pali: "hīnukkaṭṭhukkaṭṭhataratamānukkamena",
    meaning: {
      en: "by gradual sequence of inferior, superior, more superior, and supreme qualities (hīna + ukkaṭṭha + tara + tama + anukkamena)",
      pt: "pela gradação sucessiva de qualidades inferiores, superiores, mais superiores e supremas (hīna + ukkaṭṭha + tara + tama + anukkamena, classificação canônica do kamma)",
      es: "por la secuencia gradual de calidades inferiores, superiores y supremas en la maduración del kamma"
    },
    grammar: "composto classificatório instrumental, hīna + ukkaṭṭha + tara + tama + anukkamena",
    root: "√hā > hīna + ud + √kas > ukkaṭṭha + tara + tama + anu + √kram + ena"
  },
  {
    pali: "hotyāsaṅkhārikāditā",
    meaning: {
      en: "the nature of being unprompted (asaṅkhārika) etc. exists (hoti + asaṅkhārika + āditā)",
      pt: "existe a natureza de ser espontâneo / não induzido (asaṅkhārika), etc. (hoti + asaṅkhārika + āditā)",
      es: "se da la naturaleza de ser no inducido / espontáneo (asaṅkhārika), etc."
    },
    grammar: "sandhi oracional, hoti + asaṅkhārika + ādi + tā",
    root: "√hū > hoti + a + saṅkhāra + ika + ādi + tā"
  },
  {
    pali: "idamatthitāya",
    meaning: {
      en: "due to this-conditionality (idappaccayatā); by virtue of the causal principle that 'this being, that arises'",
      pt: "em virtude da condicionalidade específica (idappaccayatā); pelo princípio da originação interdependente segundo o qual 'quando isto existe, aquilo surge'",
      es: "en virtud de la condicionalidad específica (idappaccayatā); 'al existir esto, aquello surge'"
    },
    grammar: "f. instr./dat., idaṃ + atthi + tā + ya",
    root: "idaṃ (isto) + as > atthi (existe) + tā + yā"
  }
];

let added2 = 0;
for (const item of batch2) {
  const key = item.pali.toLowerCase().trim();
  if (!existingPali.has(key)) {
    dict.push(item);
    existingPali.add(key);
    added2++;
  }
}

fs.writeFileSync(dictPath, JSON.stringify(dict, null, 2), 'utf8');
console.log(`Lote 2 adicionado: ${added2} verbetes. Total no dicionário: ${dict.length}`);

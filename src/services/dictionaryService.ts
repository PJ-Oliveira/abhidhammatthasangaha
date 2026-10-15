// src/services/dictionaryService.ts
import type { DictionaryEntry } from '../types/models';
import rawDictionary from '../data/paliDictionary.json';

export type { DictionaryEntry };

/**
 * Normaliza o texto em Pāli removendo marcas diacríticas (macrons, pontos, tis)
 * e convertendo para minúsculas para busca flexível insensível a maiúsculas e diacríticos.
 */
export function normalizePali(text: string): string {
  if (!text) return '';
  return text
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .trim();
}

interface IndexedDictionaryEntry extends DictionaryEntry {
  _searchKeyPali: string;
  _searchKeyEn: string;
  _searchKeyPt: string;
  _searchKeyEs: string;
}

const indexedDictionary: IndexedDictionaryEntry[] = (rawDictionary as DictionaryEntry[]).map((entry) => ({
  ...entry,
  _searchKeyPali: normalizePali(entry.pali),
  _searchKeyEn: normalizePali(entry.meaning?.en || ''),
  _searchKeyPt: normalizePali(entry.meaning?.pt || ''),
  _searchKeyEs: normalizePali(entry.meaning?.es || ''),
}));

export const paliDictionary: DictionaryEntry[] = indexedDictionary;

// Índices rápidos O(1) para lookups instantâneos
const exactPaliMap = new Map<string, IndexedDictionaryEntry>();
const normalizedPaliMap = new Map<string, IndexedDictionaryEntry>();

indexedDictionary.forEach((entry) => {
  const lower = entry.pali.toLowerCase().trim();
  if (!exactPaliMap.has(lower)) {
    exactPaliMap.set(lower, entry);
  }
  const norm = entry._searchKeyPali;
  if (!normalizedPaliMap.has(norm)) {
    normalizedPaliMap.set(norm, entry);
  }
});

/**
 * Remove pontuação não alfanumérica das pontas do token.
 */
export function cleanPaliToken(text: string): string {
  if (!text) return '';
  return text
    .replace(/^[^a-zA-ZāīūñṅṭḍṇḷṃĀĪŪÑṄṬḌṆḶṂ0-9]+|[^a-zA-ZāīūñṅṭḍṇḷṃĀĪŪÑṄṬḌṆḶṂ0-9]+$/g, '')
    .trim();
}

/**
 * Gera candidatos de radicais e formas base para palavras flexionadas em Pāli.
 */
function getCandidateStems(word: string): string[] {
  const candidates: string[] = [word];
  const norm = normalizePali(word);
  if (norm !== word) {
    candidates.push(norm);
  }

  // Desinências nominais, verbais e de sandhi canônicas em Pāli
  const endings: [string, string][] = [
    // Sandhis frequentes nos tratados do Abhidhamma
    ['tīti', 'ti'],
    ['tīti', ''],
    ['ñceti', 'a'],
    ['ñceti', ''],
    ['ñca', 'a'],
    ['ñca', ''],
    ['cāti', ''],
    ['tveva', ''],
    ['totyattho', 'to'],
    ['totyattho', 'a'],
    ['mpī', 'a'],
    ['mpī', ''],
    ['mpi', 'a'],
    ['mpi', ''],
    ['tassa', 'ta'],
    ['tassa', ''],
    ['māna', 'ati'],
    ['mānā', 'ati'],
    ['mānaṃ', 'ati'],
    // Desinências de caso / número
    ['assa', 'a'],   // Genitivo/dativo sg
    ['ānaṃ', 'a'],   // Genitivo pl (-a)
    ['ānaṃ', 'i'],   // Genitivo pl (-i)
    ['ānaṃ', 'u'],   // Genitivo pl (-u)
    ['anam', 'a'],
    ['ena', 'a'],    // Instrumental sg
    ['ehi', 'a'],    // Instrumental/ablativo pl
    ['āya', 'a'],    // Dativo/ablativo sg (-a)
    ['āya', 'ā'],    // Dativo/ablativo sg (-ā)
    ['aya', 'a'],
    ['aya', 'ā'],
    ['aṃ', 'a'],     // Acusativo sg / nominativo nt
    ['am', 'a'],
    ['esu', 'a'],    // Locativo pl
    ['esu', ''],
    ['āni', 'a'],    // Nom./acc. pl nt
    ['āni', ''],
    ['o', 'a'],      // Nominativo sg masc
    ['e', 'a'],      // Locativo sg
    ['ā', 'a'],      // Nominativo pl / ablativo
    ['ī', 'i'],      // Sandhi / fem
    ['ū', 'u'],      // Sandhi
    ['to', 'a'],     // Ablativo / adverbial
    ['to', ''],
    // Desinências verbais
    ['anti', 'ati'], // 3ª pl -> 3ª sg
    ['anti', 'a'],
    ['nti', ''],     // 3a pessoa pl
    ['ti', ''],      // 3a pessoa sg ou aspa 'iti'
    ['eyya', 'ati'], // Optativo
    ['eyya', 'eti'],
    ['ituṃ', 'eti'], // Infinitivo
    ['ituṃ', 'ā'],
    ['tvā', 'ti'],   // Absolutivo
    ['tvā', 'ati'],
    ['tvā', 'eti'],
    ['pi', ''],      // api
    ['ca', ''],      // ca
    ['eva', ''],     // eva
  ];

  for (const [suffix, replacement] of endings) {
    if (word.endsWith(suffix) && word.length > suffix.length + 1) {
      candidates.push(word.slice(0, -suffix.length) + replacement);
    }
    if (norm.endsWith(suffix) && norm.length > suffix.length + 1) {
      candidates.push(norm.slice(0, -suffix.length) + replacement);
    }
  }

  return Array.from(new Set(candidates));
}

// Cache de memória global para lookups O(1)
const lookupCache = new Map<string, DictionaryEntry | null>();

// Grafias alternativas → forma canônica no dicionário
const PALI_ALIASES: Record<string, string> = {
  'voṭṭhapana': 'voṭṭhabbana',
  'votthapana': 'votthabbana',
};

/**
 * Consulta uma palavra em Pāli no dicionário offline do Abhidhamma.
 * Executa correspondência exata O(1), diacrítico-flexível e morfológica.
 *
 * @param word Palavra ou token em Pāli.
 * @returns DictionaryEntry correspondente ou undefined.
 */
export function lookupWord(word: string): DictionaryEntry | undefined {
  if (!word) return undefined;
  const clean = cleanPaliToken(word);
  if (!clean) return undefined;

  const cacheKey = clean.toLowerCase();
  const canonical = PALI_ALIASES[cacheKey] || PALI_ALIASES[normalizePali(cacheKey)];
  if (canonical) return lookupWord(canonical);

  if (lookupCache.has(cacheKey)) {
    const cached = lookupCache.get(cacheKey);
    return cached ? cached : undefined;
  }

  const resolve = (entry?: DictionaryEntry) => {
    lookupCache.set(cacheKey, entry || null);
    return entry;
  };

  // Fase 1: Correspondência exata insensível a maiúsculas (O(1))
  const exact = exactPaliMap.get(cacheKey);
  if (exact) return resolve(exact);

  // Fase 2: Correspondência diacrítico-flexível (O(1))
  const normWord = normalizePali(clean);
  const diacriticMatch = normalizedPaliMap.get(normWord);
  if (diacriticMatch) return resolve(diacriticMatch);

  // Fase 3: Morfologia / desinências e radicais candidatos
  const stems = getCandidateStems(clean);
  for (const stem of stems) {
    const stemLower = stem.toLowerCase();
    const stemMatch = exactPaliMap.get(stemLower) || normalizedPaliMap.get(normalizePali(stem));
    if (stemMatch) return resolve(stemMatch);
  }

  // Fase 4: Decomposição de compostos (prefix match de lemas conhecidos)
  for (let len = clean.length - 1; len >= 3; len--) {
    const sub = clean.slice(0, len).toLowerCase();
    const subMatch = exactPaliMap.get(sub);
    if (subMatch) return resolve(subMatch);
  }

  return resolve(undefined);
}

/**
 * Pesquisa no dicionário em Pāli e em todas as traduções (EN, PT, ES).
 * Resultados ordenados por relevância e limitados aos 50 melhores.
 */
export function searchDictionary(query: string): DictionaryEntry[] {
  if (!query) return [];
  const clean = cleanPaliToken(query);
  const normQuery = normalizePali(clean || query);
  if (!normQuery) return [];

  const matched = indexedDictionary.filter((entry) => {
    return (
      entry._searchKeyPali.includes(normQuery) ||
      entry._searchKeyEn.includes(normQuery) ||
      entry._searchKeyPt.includes(normQuery) ||
      entry._searchKeyEs.includes(normQuery)
    );
  });

  // Relevância: correspondência exata > prefixo Pāli > substring Pāli > significado
  const sorted = matched.sort((a, b) => {
    const score = (entry: IndexedDictionaryEntry): number => {
      const pNorm = entry._searchKeyPali;
      if (pNorm === normQuery) return 100;
      if (pNorm.startsWith(normQuery)) return 80;
      if (pNorm.includes(normQuery)) return 60;
      return 20;
    };
    return score(b) - score(a);
  });

  return sorted.slice(0, 50);
}

/**
 * Retorna todos os verbetes do dicionário Pāli.
 */
export function getAllEntries(): DictionaryEntry[] {
  return paliDictionary;
}

/**
 * Retorna a quantidade total de verbetes no dicionário Pāli.
 */
export function getDictionaryCount(): number {
  return paliDictionary.length;
}

export default {
  lookupWord,
  searchDictionary,
  getAllEntries,
  getDictionaryCount,
  normalizePali,
  cleanPaliToken,
  paliDictionary,
};

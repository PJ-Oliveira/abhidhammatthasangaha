import { buildSearchIndex, searchSegments, highlightMatch } from '../../services/textSearch';

describe('Text Search Service — Real 9-Chapter Corpus Integration Tests (No Mocks)', () => {
  beforeAll(async () => {
    await buildSearchIndex();
  });

  it('indexes all 9 chapters and finds real segments containing "nibbana" (diacritic-insensitive for nibbāna)', () => {
    const results = searchSegments('nibbana');
    expect(Array.isArray(results)).toBe(true);
    expect(results.length).toBeGreaterThan(5);
    expect(results.every((id) => id.startsWith('abhm-'))).toBe(true);
  });

  it('finds real segments by Pāli terms with and without diacritics (cetasika, rupaparicchedo, paticcasamuppada)', () => {
    const cetasikaResults = searchSegments('cetasikaparicchedo');
    expect(cetasikaResults).toContain('abhm-2.1');

    const rupaResults = searchSegments('rupaparicchedo');
    expect(rupaResults).toContain('abhm-6.1');

    const kammatthanaResults = searchSegments('kammatthanaparicchedo');
    expect(kammatthanaResults).toContain('abhm-9.1');
  });

  it('finds real segments across Portuguese, English, and Spanish translations', () => {
    const ptResults = searchSegments('Fatores Mentais');
    expect(ptResults).toContain('abhm-2.1');

    const enResults = searchSegments('Mental Factors');
    expect(enResults).toContain('abhm-2.1');

    const esResults = searchSegments('Factores Mentales');
    expect(esResults).toContain('abhm-2.1');
  });

  it('returns empty array for empty or whitespace query', () => {
    expect(searchSegments('')).toEqual([]);
    expect(searchSegments('   ')).toEqual([]);
  });

  it('highlights matching terms accurately in highlightMatch and safely escapes regex metacharacters', () => {
    const text = 'Tattha cittati sabbamalavirahitaṃ (89 / 121) [52]';
    expect(highlightMatch(text, 'citta')).toBe('Tattha **citta**ti sabbamalavirahitaṃ (89 / 121) [52]');
    expect(highlightMatch(text, '(89 / 121)')).toBe('Tattha cittati sabbamalavirahitaṃ **(89 / 121)** [52]');
    expect(highlightMatch(text, '[52]')).toBe('Tattha cittati sabbamalavirahitaṃ (89 / 121) **[52]**');
    expect(() => highlightMatch(text, 'citta?([*+')).not.toThrow();
    expect(highlightMatch(text, 'nibbana')).toBe(text);
    expect(highlightMatch(text, '')).toBe(text);
  });
});

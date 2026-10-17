import { lookupWord, searchDictionary } from '../../services/dictionaryService';
import type { AbhidhammaEntryData } from '../../types/models';

describe('Dictionary Service (Unit Tests)', () => {
  it('should find exact pali word', () => {
    const result = lookupWord('sīla');
    expect(result).toBeDefined();
    expect(result?.pali).toBe('sīla');
  });

  it('should be diacritical insensitive', () => {
    const result = lookupWord('sila');
    expect(result).toBeDefined();
    expect(result?.pali).toBe('sīla');
  });

  it('should return undefined for non-existent word', () => {
    const result = lookupWord('not-a-pali-word');
    expect(result).toBeUndefined();
  });

  it('should search meanings containing string', () => {
    const results = searchDictionary('virtue');
    expect(results.length).toBeGreaterThan(0);
    expect(results[0].meaning.en.toLowerCase()).toContain('virtue');
  });

  it('should sort results by relevancy', () => {
    const results = searchDictionary('kamma');
    expect(results[0].pali.toLowerCase()).toBe('kamma');
  });

  it('provides full canonical Abhidhamma dossier and Lakkhaṇādi-catukka for Paramattha Dhammas', () => {
    for (const term of ['citta', 'cetasika', 'rūpa', 'nibbāna', 'phassa', 'vedanā', 'paṭhavī', 'bhavaṅga', 'javana']) {
      const entry = lookupWord(term);
      expect(entry).toBeDefined();
      expect(entry?.abhidhamma).toBeDefined();
      const abhi = entry?.abhidhamma as AbhidhammaEntryData;
      expect(abhi.ontology.pt).toBeTruthy();
      expect(abhi.ontology.en).toBeTruthy();
      expect(abhi.ontology.es).toBeTruthy();
      expect(abhi.lakkhanaCatukka?.lakkhana.pt).toBeTruthy();
      expect(abhi.lakkhanaCatukka?.rasa.pt).toBeTruthy();
      expect(abhi.lakkhanaCatukka?.paccupatthana.pt).toBeTruthy();
      expect(abhi.lakkhanaCatukka?.padatthana.pt).toBeTruthy();
      expect(abhi.bodhiRef).toContain('CMA');
    }
  });

  it('provides pedagogical Samāsa decomposition and Viggaha for compounds and inflected forms', () => {
    const comp = lookupWord('somanassasahagataṃ');
    expect(comp).toBeDefined();
    expect(comp?.samasa).toBeDefined();
    expect(comp?.samasa?.viggaha).toBeTruthy();
    expect(comp?.samasa?.parts.length).toBeGreaterThanOrEqual(2);
    expect(comp?.abhidhamma).toBeDefined();

    const sandhi = lookupWord('asaṅkhārikamekaṃ');
    expect(sandhi).toBeDefined();
    expect(sandhi?.baseLemma).toBe('asaṅkhārika');
    expect(sandhi?.samasa).toBeDefined();
    expect(sandhi?.abhidhamma).toBeDefined();
  });
});

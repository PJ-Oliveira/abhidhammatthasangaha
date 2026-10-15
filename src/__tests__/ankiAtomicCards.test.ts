// src/__tests__/ankiAtomicCards.test.ts
import { ANKI_CARDS, CAPSTONE_CARDS } from '../data/ankiCards';
import { ATOMIC_CARDS, CURRICULUM_ORDER } from '../data/ankiAtomicCards';

const byId = new Map(ANKI_CARDS.map((c) => [c.id, c]));
const pos = new Map(CURRICULUM_ORDER.map((id, i) => [id, i]));

describe('Single bottom-up deck (prerequisite graph)', () => {
  it('has one curriculum containing every atomic and synthesis card exactly once', () => {
    expect(CURRICULUM_ORDER.length).toBe(new Set(CURRICULUM_ORDER).size);
    expect(ANKI_CARDS.length).toBe(ATOMIC_CARDS.length + CAPSTONE_CARDS.length);
    expect(ANKI_CARDS.map((c) => c.id)).toEqual(CURRICULUM_ORDER);
  });

  it('only requires existing cards that come earlier (acyclic, always learnable in order)', () => {
    ANKI_CARDS.forEach((card) => {
      (card.requires ?? []).forEach((r) => {
        expect(byId.has(r)).toBe(true);
        expect(pos.get(r)!).toBeLessThan(pos.get(card.id)!);
      });
    });
  });

  it('starts from a single foundation card and everything else descends from it', () => {
    const roots = ANKI_CARDS.filter((c) => (c.requires ?? []).length === 0);
    expect(roots.map((c) => c.id)).toEqual(['at-t01']);
    // Every card is reachable from the root by following `requires` upwards.
    const reachesRoot = (id: string, seen = new Set<string>()): boolean => {
      if (id === 'at-t01') return true;
      if (seen.has(id)) return false;
      seen.add(id);
      return (byId.get(id)!.requires ?? []).some((r) => reachesRoot(r, seen));
    };
    ANKI_CARDS.forEach((c) => expect(reachesRoot(c.id)).toBe(true));
  });

  it('builds composite cards from at least two building blocks (sum cards)', () => {
    ['at-a17', 'at-k16', 'at-s10', 'at-s12', 'at-r16', 'at-u06', 'at-u07', 'at-l05', 'at-l06', 'at-l07', 'at-c04', 'at-c05'].forEach((id) => {
      expect((byId.get(id)!.requires ?? []).length).toBeGreaterThanOrEqual(2);
    });
  });

  it('keeps the old rich cards behind their building blocks (no synthesis before its parts)', () => {
    const cap = (id: string) => byId.get(id)!;
    expect(cap('ch1-03').requires).toEqual(expect.arrayContaining(['at-a17', 'at-a16']));
    expect(cap('ch1-04').requires).toEqual(expect.arrayContaining(['at-k16']));
    expect(cap('ch1-02').requires).toEqual(expect.arrayContaining(['at-l06', 'at-l07']));
    // Chapters not yet decomposed open only after the previous chapter
    expect((cap('ch2-01').requires ?? []).length).toBeGreaterThan(0);
  });

  it('has complete trilingual question/answer for every atomic card', () => {
    ATOMIC_CARDS.forEach((card) => {
      (['en', 'pt', 'es'] as const).forEach((lang) => {
        expect(card[lang].question.trim().length).toBeGreaterThan(5);
        expect(card[lang].answer.trim().length).toBeGreaterThan(0);
      });
    });
  });

  it('encodes the canonical arithmetic of the citta classification', () => {
    const ans = (id: string) => byId.get(id)!.pt.answer;
    expect(ans('at-a17')).toContain('= 12');
    expect(ans('at-k16')).toContain('= 18');
    expect(ans('at-s10')).toContain('24 = 8');
    expect(ans('at-s12')).toContain('54 = 12 akusala + 18 ahetuka + 24 sobhana');
    expect(ans('at-r16')).toContain('15 = 5');
    expect(ans('at-u06')).toContain('12 = 4');
    expect(ans('at-u07')).toContain('27 = 15');
    expect(ans('at-l05')).toContain('81 = 54 kāmāvacara + 27');
    expect(ans('at-l06')).toContain('89 = 81 lokiya + 8');
    expect(ans('at-l07')).toContain('121 = 81 lokiya + 40');
    expect(ans('at-c04')).toContain('71 = 2 ekahetuka + 22 dvihetuka + 47');
    expect(ans('at-c05')).toContain('89 = 18 ahetuka + 71');
  });
});

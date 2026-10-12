// src/__tests__/ankiCards.test.ts
import { ANKI_CARDS } from '../data/ankiCards';

describe('Anki Cards Rigorous Dataset Unit Tests', () => {
  it('contains 63 comprehensive master flashcards with unique IDs', () => {
    expect(ANKI_CARDS.length).toBe(63);
    const ids = new Set(ANKI_CARDS.map((c) => c.id));
    expect(ids.size).toBe(ANKI_CARDS.length);
  });

  it('covers all 9 Paricchedas (Chapters 1 to 9) exhaustively', () => {
    const chaptersPresent = new Set(ANKI_CARDS.map((c) => c.chapter));
    for (let ch = 1; ch <= 9; ch++) {
      expect(chaptersPresent.has(ch)).toBe(true);
      const cardsInChapter = ANKI_CARDS.filter((c) => c.chapter === ch);
      expect(cardsInChapter.length).toBeGreaterThanOrEqual(4);
    }
  });

  it('has complete trilingual content (EN, PT, ES) for every single card', () => {
    ANKI_CARDS.forEach((card) => {
      (['en', 'pt', 'es'] as const).forEach((lang) => {
        expect(card[lang]).toBeDefined();
        expect(card[lang].question.trim().length).toBeGreaterThan(5);
        expect(card[lang].answer.trim().length).toBeGreaterThan(5);
        expect(Array.isArray(card[lang].breakdown)).toBe(true);
        expect(card[lang].breakdown.length).toBeGreaterThanOrEqual(1);
        expect(card[lang].explanation.trim().length).toBeGreaterThan(5);
        expect(card[lang].mnemonicOrExamTip.trim().length).toBeGreaterThan(5);
        expect(card[lang].examQuestionType.trim().length).toBeGreaterThan(2);
      });

      // Canonical Pāḷi Term
      expect(card.paliTerm.trim().length).toBeGreaterThan(2);
      expect(card.id).toBeDefined();
      expect(card.chapterName.pali.trim().length).toBeGreaterThan(2);
    });
  });

  it('verifies all essential pedagogical categories are represented', () => {
    const categories = new Set(ANKI_CARDS.map((c) => c.category));
    expect(categories.has('quantities')).toBe(true);
    expect(categories.has('structures')).toBe(true);
    expect(categories.has('relations')).toBe(true);
    expect(categories.has('philosophy')).toBe(true);
    expect(categories.has('exam_traps')).toBe(true);
  });

  it('verifies crucial core numbers and doctrinal accuracy tested in Abhidhamma examinations', () => {
    // 4 Paramattha Dhammas (1, 89/121, 52, 28, 1)
    const ch1_01 = ANKI_CARDS.find((c) => c.id === 'ch1-01');
    expect(ch1_01?.pt.answer).toContain('89');
    expect(ch1_01?.pt.answer).toContain('121');
    expect(ch1_01?.pt.answer).toContain('52');
    expect(ch1_01?.pt.answer).toContain('28');

    // 89 / 121 Cittas
    const cittaCard = ANKI_CARDS.find((c) => c.id === 'ch1-02');
    expect(cittaCard).toBeDefined();
    expect(cittaCard?.pt.answer).toContain('89');
    expect(cittaCard?.pt.answer).toContain('121');

    // Somanassa 62 Cittas (4 jhānas × 3 classes = 12 Rūpāvacara, distinct from 51 Sapītika)
    const ch1_09 = ANKI_CARDS.find((c) => c.id === 'ch1-09');
    expect(ch1_09?.en.breakdown[0]).toContain('12 rūpāvacara (1st–4th jhānas × 3 classes');
    expect(ch1_09?.pt.breakdown[0]).toContain('12 rūpāvacara (1º ao 4º jhānas × 3 classes');
    expect(ch1_09?.es.breakdown[0]).toContain('12 rūpāvacara (1º al 4º jhānas × 3 clases)');

    const ch1_15 = ANKI_CARDS.find((c) => c.id === 'ch1-15');
    expect(ch1_15?.en.answer).toContain('4 jhānas × 3 classes');
    expect(ch1_15?.en.breakdown[1]).toContain('51 cittas');
    expect(ch1_15?.pt.answer).toContain('4 jhānas × 3 classes');
    expect(ch1_15?.es.answer).toContain('4 jhānas × 3 clases = 12');

    // 52 Cetasikas
    const cetasikaCard = ANKI_CARDS.find((c) => c.id === 'ch2-02');
    expect(cetasikaCard?.pt.answer).toContain('52');

    // 14 Kiccas & 6 Bases (10 + 33 + 42 + 4 = 89)
    const kiccaCard = ANKI_CARDS.find((c) => c.id === 'ch3-01');
    expect(kiccaCard?.pt.answer).toContain('14');
    const vatthuCard = ANKI_CARDS.find((c) => c.id === 'ch3-02');
    expect(vatthuCard?.pt.answer).toContain('10 + 33 + 42 + 4 = 89');

    // 17 Thought-moments in a five-door cognitive process & 5 Javanas at death
    const vithiCard = ANKI_CARDS.find((c) => c.id === 'ch4-01');
    expect(vithiCard?.pt.answer).toContain('17');
    const deathJavanaCard = ANKI_CARDS.find((c) => c.id === 'ch4-05');
    expect(deathJavanaCard?.pt.answer).toContain('5 momentos de Javana');

    // 31 Planes & 19 Patisandhi Cittas
    const bhumiCard = ANKI_CARDS.find((c) => c.id === 'ch5-05');
    expect(bhumiCard?.pt.answer).toContain('31');
    const patisandhiCard = ANKI_CARDS.find((c) => c.id === 'ch5-06');
    expect(patisandhiCard?.pt.answer).toContain('19');

    // 28 Rupas (18 Nipphanna + 10 Anipphanna), 30 Rūpas at conception & 21 Kalāpas (9+6+4+2)
    const rupaCard = ANKI_CARDS.find((c) => c.id === 'ch6-01');
    expect(rupaCard?.pt.answer).toContain('18');
    expect(rupaCard?.pt.answer).toContain('10');
    const kalapaCard = ANKI_CARDS.find((c) => c.id === 'ch6-03');
    expect(kalapaCard?.pt.answer).toContain('30');
    expect(kalapaCard?.pt.breakdown[1]).toContain('21');

    // Chapter 7: 6 Nīvaraṇas (ch7-02) & Nibbāna as Khandhavimutta (ch7-03)
    const nivaranaCard = ANKI_CARDS.find((c) => c.id === 'ch7-02');
    expect(nivaranaCard?.pt.answer).toContain('6 Nīvaraṇas');
    const khandhavimuttaCard = ANKI_CARDS.find((c) => c.id === 'ch7-03');
    expect(khandhavimuttaCard?.pt.answer).toContain('Khandhavimutta');

    // Chapter 8: 12 Links of Paticcasamuppada (ch8-01), 2 Paññattis (ch8-02), 3 Sandhis (ch8-03) & 24 Paccayas
    const paticcaCard = ANKI_CARDS.find((c) => c.id === 'ch8-01');
    expect(paticcaCard?.pt.answer).toContain('12');
    const pannattiCard = ANKI_CARDS.find((c) => c.id === 'ch8-02');
    expect(pannattiCard?.pt.answer).toContain('Atthapaññatti');
    const sandhiCard = ANKI_CARDS.find((c) => c.id === 'ch8-03');
    expect(sandhiCard?.pt.answer).toContain('3 Conexões');
    const paccayaCard = ANKI_CARDS.find((c) => c.chapter === 8 && c.pt.answer.includes('24'));
    expect(paccayaCard).toBeDefined();

    // Chapter 9: 40 Samatha Kammatthanas & 10 Vipassanā Ñāṇas
    const samathaCard = ANKI_CARDS.find((c) => c.id === 'ch9-01');
    expect(samathaCard?.pt.answer).toContain('40');
    const vipassanaCard = ANKI_CARDS.find((c) => c.id === 'ch9-02');
    expect(vipassanaCard?.pt.answer).toContain('10');
  });

  it('guarantees cross-language breakdown and canonical numeric parity across EN, PT, and ES for all 63 cards', () => {
    const KEY_ABHIDHAMMA_NUMBERS = [
      '89', '121', '52', '28', '18', '24', '31', '40', '37', '17',
      '47', '79', '55', '62', '54', '27', '15', '12', '13', '14', '25', '19', '30',
    ];

    ANKI_CARDS.forEach((card) => {
      expect(card.en.breakdown.length).toBe(card.pt.breakdown.length);
      expect(card.en.breakdown.length).toBe(card.es.breakdown.length);

      const enText = `${card.en.answer} ${card.en.breakdown.join(' ')}`;
      const ptText = `${card.pt.answer} ${card.pt.breakdown.join(' ')}`;
      const esText = `${card.es.answer} ${card.es.breakdown.join(' ')}`;

      KEY_ABHIDHAMMA_NUMBERS.forEach((num) => {
        const re = new RegExp(`\\b${num}(?:th|st|nd|rd|º|ª)?\\b`);
        if (re.test(enText)) {
          expect(re.test(ptText)).toBe(true);
          expect(re.test(esText)).toBe(true);
        }
      });
    });
  });
});

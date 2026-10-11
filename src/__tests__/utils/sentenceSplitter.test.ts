import { splitIntoSentences, sanitizeHtmlText } from '../../utils/sentenceSplitter';

describe('sentenceSplitter', () => {
  it('correctly splits abhm-1.5 question and subsequent sentence on question mark', () => {
    const pali = 'Tattha katamaṃ <b>kāmāvacaraṃ</b>? Somanassasahagataṃ diṭṭhigatasampayuttaṃ asaṅkhārikamekaṃ.';
    const sentences = splitIntoSentences(pali);
    expect(sentences).toHaveLength(2);
    expect(sentences[0]).toBe('Tattha katamaṃ <b>kāmāvacaraṃ</b>?');
    expect(sentences[1]).toBe('Somanassasahagataṃ diṭṭhigatasampayuttaṃ asaṅkhārikamekaṃ.');
  });

  it('correctly splits translation without breaking the leading number prefix', () => {
    const en = '4. Among these, what is sense-sphere consciousness? One consciousness accompanied by joy.';
    const sentences = splitIntoSentences(en);
    expect(sentences).toHaveLength(2);
    expect(sentences[0]).toBe('4. Among these, what is sense-sphere consciousness?');
    expect(sentences[1]).toBe('One consciousness accompanied by joy.');
  });

  it('correctly splits sentences on periods', () => {
    const pt = '4. Nisso, qual é a da esfera sensorial? Uma acompanhada de alegria. Essas oito são conhecidas.';
    const sentences = splitIntoSentences(pt);
    expect(sentences).toHaveLength(3);
    expect(sentences[0]).toBe('4. Nisso, qual é a da esfera sensorial?');
    expect(sentences[1]).toBe('Uma acompanhada de alegria.');
    expect(sentences[2]).toBe('Essas oito são conhecidas.');
  });

  it('handles single sentences without altering content', () => {
    const text = 'Akusalacittaṃ.';
    expect(splitIntoSentences(text)).toEqual(['Akusalacittaṃ.']);
  });

  it('sanitizes HTML tags from translations', () => {
    const messy = '4. <span class="lead">Nisso</span>, qual é? <p rend="gatha1">Uma acompanhada.</p>';
    expect(sanitizeHtmlText(messy)).toBe('4. Nisso, qual é? Uma acompanhada.');
  });
});

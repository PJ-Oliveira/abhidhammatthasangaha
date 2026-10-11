import { parsePaliMarkup, stripMarkup, decodeEntities } from '../../utils/paliMarkup';

const text = (lines: ReturnType<typeof parsePaliMarkup>) =>
  lines.map((line) => line.map((run) => run.text).join(''));

describe('parsePaliMarkup', () => {
  it('returns plain text unchanged as a single non-bold line', () => {
    expect(parsePaliMarkup('Evaṃ me sutaṃ.')).toEqual([[{ text: 'Evaṃ me sutaṃ.', bold: false }]]);
  });

  it('turns <b> into bold runs and removes the tags (the bug seen in the reader)', () => {
    const lines = parsePaliMarkup('Tattha <b>kāmāvacaraṃ</b>? Somanassa');
    expect(lines).toEqual([
      [
        { text: 'Tattha ', bold: false },
        { text: 'kāmāvacaraṃ', bold: true },
        { text: '? Somanassa', bold: false },
      ],
    ]);
    expect(JSON.stringify(lines)).not.toMatch(/[<>]/);
  });

  it('splits verse paragraphs (</p><p rend="gathaN">) into separate lines', () => {
    const lines = parsePaliMarkup(
      'Lobhamūle tayo gatā;</p><p rend="gatha3">Dosamūlesu cattāro,</p><p rend="gathalast">Sasaṅkhāre dvayaṃ tathā.',
    );
    expect(text(lines)).toEqual(['Lobhamūle tayo gatā;', 'Dosamūlesu cattāro,', 'Sasaṅkhāre dvayaṃ tathā.']);
  });

  it('does not create empty lines for leading/trailing paragraph tags', () => {
    expect(text(parsePaliMarkup('<p rend="gatha1">Chando ca;</p>'))).toEqual(['Chando ca;']);
  });

  it('handles <br> and drops unknown tags but keeps their content', () => {
    expect(text(parsePaliMarkup('um<br/>dois <span class="x">três</span>'))).toEqual(['um', 'dois três']);
  });

  it('keeps bold state across a closing tag only until it is closed', () => {
    const [line] = parsePaliMarkup('<b>a</b> b <strong>c</strong>');
    expect(line.map((r) => [r.text, r.bold])).toEqual([
      ['a', true],
      [' b ', false],
      ['c', true],
    ]);
  });

  it('is safe with empty or undefined-like input', () => {
    expect(parsePaliMarkup('')).toEqual([]);
    expect(parsePaliMarkup(undefined as unknown as string)).toEqual([]);
  });

  it('does not treat a lone "<" as a tag', () => {
    expect(text(parsePaliMarkup('a < b'))).toEqual(['a < b']);
  });

  it('normalizes decomposed diacritics to precomposed (NFC)', () => {
    const decomposed = 'ṃ'.normalize('NFD'); // m + U+0323 + ... style sequence
    const [[run]] = parsePaliMarkup(`ka${decomposed}`);
    expect(run.text).toBe('kaṃ');
    expect(run.text.length).toBe(3);
  });
});

describe('stripMarkup', () => {
  it('returns plain searchable text', () => {
    expect(stripMarkup('Tattha <b>cittaṃ</b> tāva')).toBe('Tattha cittaṃ tāva');
    expect(stripMarkup('a;</p><p rend="gathalast">b.')).toBe('a; b.');
  });
});

describe('decodeEntities', () => {
  it('decodes named and numeric entities and leaves unknown ones alone', () => {
    expect(decodeEntities('a &amp; b &lt;c&gt; &#257; &#x1E43; &foo;')).toBe('a & b <c> ā ṃ &foo;');
  });
});

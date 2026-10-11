import React from 'react';
import { render, fireEvent } from '@testing-library/react-native';
import { Provider } from 'react-redux';
import { store } from '../../store/store';
import { InteractivePaliText } from '../../components/Reader/InteractivePaliText';
import { parsePaliMarkup } from '../../utils/paliMarkup';
import { CHAPTERS } from '../../data/chapters/chapterIndex';
import { loadChapter } from '../../data/chapters/chapterLoader';
import type { Segment } from '../../types/models';

const renderPali = (text: string) =>
  render(
    <Provider store={store}>
      <InteractivePaliText text={text} />
    </Provider>,
  );

describe('InteractivePaliText with source markup', () => {
  it('never shows raw tags on screen', () => {
    const { toJSON } = renderPali('Tattha <b>kāmāvacaraṃ</b>? Somanassasahagataṃ.');
    const dump = JSON.stringify(toJSON());
    expect(dump).not.toMatch(/<b>|<\/b>|<p|<\/p>|rend=/);
    expect(dump).toContain('kāmāvacaraṃ');
  });

  it('renders bold terms as bold and verse lines on separate lines', () => {
    const { getByText, toJSON } = renderPali('Tattha <b>cittaṃ</b> tāva;</p><p rend="gathalast">Jhānamekekamante.');
    const bold = getByText('cittaṃ');
    expect(JSON.stringify(bold.props.style)).toContain('bold');
    expect(JSON.stringify(toJSON())).toContain('\\n');
  });

  it('keeps dictionary words clickable inside bold text', () => {
    const { getByText } = renderPali('<b>citta</b>');
    const word = getByText('citta');
    fireEvent.press(word);
    expect(store.getState().reading.dictionaryWord).toBeTruthy();
  });
});

// Teste de regressão sobre os DADOS REAIS: nenhuma tag pode sobrar em nenhum segmento.
describe('real chapter data', () => {
  it('leaves no markup in any Pali segment of any chapter after parsing', async () => {
    let checked = 0;
    let withBold = 0;
    let withVerse = 0;
    let rawWithBold = 0;
    let rawWithVerse = 0;
    for (const chapter of CHAPTERS) {
      const segments: Segment[] = await loadChapter(chapter.id);
      for (const segment of segments) {
        const lines = parsePaliMarkup(segment.pali);
        const flatText = lines.map((l) => l.map((r) => r.text).join('')).join('\n');
        expect({ id: segment.id, hasTag: /[<>]|rend=/.test(flatText) }).toEqual({
          id: segment.id,
          hasTag: false,
        });
        if (lines.some((l) => l.some((r) => r.bold))) withBold++;
        if (lines.length > 1) withVerse++;
        if (/<b>/.test(segment.pali)) rawWithBold++;
        if (/<\/p>\s*<p/.test(segment.pali)) rawWithVerse++;
        checked++;
      }
    }
    expect(checked).toBeGreaterThan(500);
    // Todo segmento com <b> no dado bruto vira negrito; todo verso vira várias linhas.
    expect(rawWithBold).toBeGreaterThan(0);
    expect(withBold).toBe(rawWithBold);
    expect(rawWithVerse).toBeGreaterThan(0);
    expect(withVerse).toBe(rawWithVerse);
  });
});

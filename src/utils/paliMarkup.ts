// src/utils/paliMarkup.ts
//
// Os textos em Pali vêm com marcação de origem (<b>termo</b>, versos como
// `</p><p rend="gatha2">`). Esse módulo converte a marcação em estrutura de
// linhas/trechos para renderização nativa — nenhuma tag chega à tela.

export interface MarkupRun {
  text: string;
  bold: boolean;
}

export type MarkupLine = MarkupRun[];

const TAG_PATTERN = /(<\/?[A-Za-z][^>]*>)/g;
const TAG_NAME_PATTERN = /^<(\/?)([A-Za-z][A-Za-z0-9]*)/;

const NAMED_ENTITIES: Record<string, string> = {
  amp: '&',
  lt: '<',
  gt: '>',
  quot: '"',
  apos: "'",
  nbsp: '\u00A0',
};

export function decodeEntities(input: string): string {
  return input.replace(/&(#x[0-9a-fA-F]+|#\d+|[A-Za-z]+);/g, (match, body: string) => {
    if (body.startsWith('#x') || body.startsWith('#X')) {
      return String.fromCodePoint(parseInt(body.slice(2), 16));
    }
    if (body.startsWith('#')) {
      return String.fromCodePoint(parseInt(body.slice(1), 10));
    }
    return NAMED_ENTITIES[body.toLowerCase()] ?? match;
  });
}

/**
 * Converte o texto marcado em linhas de trechos (negrito ou normal).
 *  - <b>/<strong> → negrito
 *  - fim de <p> seguido de mais conteúdo, e <br> → nova linha (versos)
 *  - qualquer outra tag é descartada
 * Também normaliza para NFC, para que diacríticos combinantes virem letras únicas.
 */
export function parsePaliMarkup(input: string): MarkupLine[] {
  const source = (input ?? '').normalize('NFC');
  const lines: MarkupLine[] = [[]];
  let bold = false;
  let breakPending = false;

  const current = (): MarkupLine => lines[lines.length - 1];
  const startNewLine = (): void => {
    if (current().length > 0) lines.push([]);
    breakPending = false;
  };

  for (const part of source.split(TAG_PATTERN)) {
    if (part === '') continue;

    const tag = TAG_NAME_PATTERN.exec(part);
    if (tag && part.startsWith('<') && part.endsWith('>')) {
      const closing = tag[1] === '/';
      const name = tag[2].toLowerCase();
      if (name === 'b' || name === 'strong') {
        bold = !closing;
      } else if (name === 'p') {
        if (closing) breakPending = true;
        else if (breakPending) startNewLine();
      } else if (name === 'br') {
        startNewLine();
      }
      continue;
    }

    const text = decodeEntities(part);
    if (text.trim() === '' && current().length === 0) continue;
    if (breakPending) startNewLine();
    current().push({ text, bold });
  }

  // Remove espaços nas pontas de cada linha e linhas vazias.
  return lines
    .map((line) => {
      const runs = line.map((run) => ({ ...run }));
      if (runs.length > 0) runs[0].text = runs[0].text.replace(/^\s+/, '');
      if (runs.length > 0) runs[runs.length - 1].text = runs[runs.length - 1].text.replace(/\s+$/, '');
      return runs.filter((run) => run.text !== '');
    })
    .filter((line) => line.length > 0);
}

/** Texto puro (sem tags), com versos separados por espaço — para busca e exportação. */
export function stripMarkup(input: string): string {
  return parsePaliMarkup(input)
    .map((line) => line.map((run) => run.text).join(''))
    .join(' ');
}

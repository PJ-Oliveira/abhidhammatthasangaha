// src/utils/sentenceSplitter.ts
/**
 * Utilitário para divisão granular de sentenças em Pāli e Traduções (EN, PT, ES).
 * Identifica quebras de sentença estritamente em ponto final ('.') ou interrogação ('?'),
 * preservando numerações de lista (ex: '4. ') e formatação interna.
 */

import { decodeEntities } from './paliMarkup';

/**
 * Remove quaisquer tags HTML indesejadas que possam estar em traduções ou textos.
 */
export function sanitizeHtmlText(text: string): string {
  if (!text) return '';
  return decodeEntities(text)
    .replace(/<[^>]+>/g, '')
    .trim();
}

/**
 * Divide um bloco de texto em sentenças individuais com base em '.' e '?'.
 * Preserva o prefixo numérico no início do segmento (ex: '4. ') sem fragmentá-lo.
 */
export function splitIntoSentences(text: string): string[] {
  if (!text) return [];
  const trimmed = text.trim();
  if (!trimmed) return [];

  // Preserva prefixos de numeração do tipo '4. ' ou '12. '
  const leadMatch = trimmed.match(/^(\d+\.\s*)/);
  const leadPrefix = leadMatch ? leadMatch[1] : '';
  const body = leadMatch ? trimmed.slice(leadPrefix.length) : trimmed;

  // Regex que busca fim de sentença (. ou ?) seguido de espaço ou fim de texto,
  // permitindo tags de fechamento intermediárias como </b> ou </i>
  const pattern = /(.*?[.?](?:<\/[^>]+>)*)(?:\s+|$)/gs;
  const sentences: string[] = [];
  let pos = 0;

  while (pos < body.length) {
    pattern.lastIndex = pos;
    const match = pattern.exec(body);
    if (match && match.index === pos) {
      const sentence = match[1].trim();
      if (sentence) {
        if (sentences.length === 0) {
          sentences.push(leadPrefix + sentence);
        } else {
          sentences.push(sentence);
        }
      }
      pos = pattern.lastIndex;
    } else {
      const remainder = body.slice(pos).trim();
      if (remainder) {
        if (sentences.length === 0) {
          sentences.push(leadPrefix + remainder);
        } else {
          sentences.push(remainder);
        }
      }
      break;
    }
  }

  return sentences.filter((s) => s.length > 0);
}

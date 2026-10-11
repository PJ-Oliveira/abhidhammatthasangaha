// src/utils/urlRouter.ts
import { CHAPTERS } from '../data/chapters/chapterIndex';

export interface ParsedRoute {
  chapterId: string;
  chapterNumber: number;
  segmentId: string | null;
}

/**
 * Normaliza o número do capítulo (1 a 9) para o ID canônico ('ch01' a 'ch09').
 */
export function chapterNumberToId(num: number): string {
  const pad = num < 10 ? `0${num}` : `${num}`;
  const id = `ch${pad}`;
  const exists = CHAPTERS.some((c) => c.id === id);
  return exists ? id : 'ch01';
}

/**
 * Converte o ID canônico ('ch01') para número do capítulo (1).
 */
export function chapterIdToNumber(id: string): number {
  const match = id.match(/ch0?(\d+)/i);
  return match ? parseInt(match[1], 10) : 1;
}

/**
 * Analisa a rota atual do navegador e extrai capítulo e id do parágrafo/âncora.
 * Suporta formatos:
 * - /abhidhammatthasaṅgaha/:chapterNumber
 * - /abhidhammatthasaṅgaha/:chapterNumber/:segmentId
 * - /abhidhammatthasangaha/:chapterNumber/:segmentId
 * - /:chapterNumber/:segmentId
 * - /#seg-:segmentId
 */
export function parseRoute(pathname: string, hash: string = ''): ParsedRoute {
  let decodedPath = '';
  try {
    decodedPath = decodeURIComponent(pathname || '');
  } catch {
    decodedPath = pathname || '';
  }

  // Remove barras iniciais e finais
  const cleanPath = decodedPath.replace(/^\/+|\/+$/g, '');
  const segments = cleanPath.split('/').filter(Boolean);

  let chapterNum = 1;
  let segmentId: string | null = null;

  // Caso: /abhidhammatthasaṅgaha/1 ou /abhidhammatthasangaha/1/abhm-1.3
  const isNamedBase =
    segments.length > 0 &&
    (segments[0].toLowerCase().includes('abhidhammatthasa') ||
      segments[0].toLowerCase().includes('abhidhammatthasangaha'));

  if (isNamedBase) {
    if (segments.length >= 2) {
      const numCandidate = parseInt(segments[1], 10);
      if (!isNaN(numCandidate) && numCandidate >= 1 && numCandidate <= 9) {
        chapterNum = numCandidate;
      }
    }
    if (segments.length >= 3) {
      segmentId = segments[2];
    }
  } else if (segments.length > 0) {
    // Caso direto: /1 ou /1/abhm-1.3
    const numCandidate = parseInt(segments[0], 10);
    if (!isNaN(numCandidate) && numCandidate >= 1 && numCandidate <= 9) {
      chapterNum = numCandidate;
      if (segments.length >= 2) {
        segmentId = segments[1];
      }
    }
  }

  // Verifica se há âncora no hash (ex: #abhm-1.3 ou #seg-abhm-1.3)
  if (!segmentId && hash) {
    const cleanHash = hash.replace(/^#/, '').replace(/^seg-/, '');
    if (cleanHash) {
      segmentId = cleanHash;
    }
  }

  return {
    chapterId: chapterNumberToId(chapterNum),
    chapterNumber: chapterNum,
    segmentId,
  };
}

/**
 * Lê a rota atual diretamente do ambiente do navegador (se disponível).
 */
export function getCurrentRoute(): ParsedRoute {
  if (typeof window === 'undefined' || !window.location) {
    return {
      chapterId: 'ch01',
      chapterNumber: 1,
      segmentId: null,
    };
  }
  return parseRoute(window.location.pathname, window.location.hash);
}

/**
 * Atualiza a URL na barra de navegação sem recarregar a página (pushState).
 * Formato padrão: /abhidhammatthasaṅgaha/:chapterNum ou /abhidhammatthasaṅgaha/:chapterNum/:segmentId
 */
export function updateBrowserRoute(
  chapterNumber: number,
  segmentId?: string | null,
  replace: boolean = false
): void {
  if (typeof window === 'undefined' || !window.history) return;

  const basePath = '/abhidhammatthasaṅgaha';
  const targetPath = segmentId
    ? `${basePath}/${chapterNumber}/${encodeURIComponent(segmentId)}`
    : `${basePath}/${chapterNumber}`;

  if (window.location.pathname !== targetPath) {
    if (replace) {
      window.history.replaceState({ chapterNumber, segmentId }, '', targetPath);
    } else {
      window.history.pushState({ chapterNumber, segmentId }, '', targetPath);
    }
  }
}

/**
 * Gera o link absoluto completo para compartilhamento de parágrafo específico.
 */
export function getParagraphDirectUrl(
  chapterNumber: number,
  segmentId: string
): string {
  if (typeof window !== 'undefined' && window.location) {
    const origin = window.location.origin;
    return `${origin}/abhidhammatthasaṅgaha/${chapterNumber}/${segmentId}`;
  }
  return `http://localhost:8081/abhidhammatthasaṅgaha/${chapterNumber}/${segmentId}`;
}

/**
 * Copia texto para a área de transferência de forma universal.
 */
export async function copyTextToClipboard(text: string): Promise<boolean> {
  if (typeof navigator !== 'undefined' && navigator.clipboard) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch {
      // fallback
    }
  }

  if (typeof document !== 'undefined') {
    try {
      const textarea = document.createElement('textarea');
      textarea.value = text;
      textarea.style.position = 'fixed';
      textarea.style.opacity = '0';
      document.body.appendChild(textarea);
      textarea.select();
      const success = document.execCommand('copy');
      document.body.removeChild(textarea);
      return success;
    } catch {
      return false;
    }
  }
  return false;
}

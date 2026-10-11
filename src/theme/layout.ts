// src/theme/layout.ts
//
// Regras de responsividade em um único lugar. `computeLayout` é uma função pura
// (testável); `useLayout` a liga ao tamanho real da janela.
//
//   < 600     celular (retrato)          1 coluna + abas
//   600–719   celular grande / tablet pequeno   1 coluna + abas
//   720–1023  iPad / tablet              leitor + dicionário lado a lado
//   1024–1439 notebook / iPad Pro        idem, painel maior
//   ≥ 1440    desktop / monitor grande   conteúdo centralizado, fonte maior

import { useWindowDimensions } from 'react-native';

export type Breakpoint = 'phone' | 'phoneWide' | 'tablet' | 'laptop' | 'desktop';

export interface Layout {
  width: number;
  height: number;
  breakpoint: Breakpoint;
  /** Leitor e dicionário lado a lado (em vez de abas). */
  isSplit: boolean;
  /** Celular deitado ou janela muito baixa: reduz espaçamentos. */
  isShortHeight: boolean;
  /** Título em cima, seletor de idioma embaixo. */
  headerStacked: boolean;
  sidePanelWidth: number;
  sidebarWidth: number;
  /** Largura máxima de todo o app (centraliza em monitores enormes). */
  contentMaxWidth: number;
  /** Largura máxima da coluna de leitura (comprimento de linha confortável). */
  readerMaxWidth: number;
  pagePadding: number;
  /** Pontos somados ao tamanho de fonte escolhido pelo usuário. */
  fontBoost: number;
  /** Largura máxima do painel inferior (bottom sheet) do dicionário. */
  sheetMaxWidth: number;
  sheetMaxHeight: number;
}

const clamp = (value: number, min: number, max: number): number =>
  Math.min(Math.max(value, min), max);

export function computeLayout(width: number, height: number): Layout {
  const w = Math.max(0, width);
  const h = Math.max(0, height);

  const breakpoint: Breakpoint =
    w >= 1440 ? 'desktop' : w >= 1024 ? 'laptop' : w >= 720 ? 'tablet' : w >= 600 ? 'phoneWide' : 'phone';

  const isShortHeight = h > 0 && h < 500;
  const isSplit = w >= 720;

  let fontBoost = 0;
  if (w >= 1920) fontBoost = 3;
  else if (w >= 1440) fontBoost = 2;
  else if (w >= 1024) fontBoost = 1;
  else if (w < 360) fontBoost = -1;

  return {
    width: w,
    height: h,
    breakpoint,
    isSplit,
    isShortHeight,
    headerStacked: w < 600 && !isShortHeight,
    sidePanelWidth: isSplit ? Math.round(clamp(w * 0.34, 280, 440)) : 0,
    sidebarWidth: Math.round(Math.min(w >= 1440 ? 380 : 340, w * 0.85)),
    contentMaxWidth: 1680,
    readerMaxWidth: 880,
    pagePadding: isShortHeight ? 8 : w < 400 ? 10 : w < 720 ? 14 : 20,
    fontBoost,
    sheetMaxWidth: 720,
    sheetMaxHeight: Math.round(h * (isShortHeight ? 0.9 : 0.7)),
  };
}

export function useLayout(): Layout {
  const { width, height } = useWindowDimensions();
  return computeLayout(width, height);
}

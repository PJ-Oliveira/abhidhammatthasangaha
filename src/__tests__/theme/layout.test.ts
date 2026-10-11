import { computeLayout } from '../../theme/layout';

// Larguras/alturas reais de dispositivos comuns (retrato e paisagem).
const DEVICES: Array<[string, number, number]> = [
  ['iPhone SE 1ª ger. (retrato)', 320, 568],
  ['iPhone SE (retrato)', 375, 667],
  ['iPhone 15 (retrato)', 393, 852],
  ['iPhone 15 Pro Max (retrato)', 430, 932],
  ['Android pequeno (retrato)', 360, 640],
  ['iPhone SE (paisagem)', 667, 375],
  ['iPhone 15 (paisagem)', 852, 393],
  ['iPad mini (retrato)', 744, 1133],
  ['iPad (retrato)', 810, 1080],
  ['iPad Air (retrato)', 820, 1180],
  ['iPad Pro 11 (retrato)', 834, 1194],
  ['iPad (paisagem)', 1080, 810],
  ['iPad Pro 12.9 (paisagem)', 1366, 1024],
  ['Notebook pequeno', 1280, 720],
  ['MacBook Air 13', 1440, 900],
  ['MacBook Pro 16', 1728, 1117],
  ['Full HD', 1920, 1080],
  ['Monitor 4K (escalado)', 2560, 1440],
  ['Ultrawide', 3440, 1440],
];

describe('computeLayout', () => {
  it.each(DEVICES)('%s (%ix%i) gives a coherent layout', (_name, width, height) => {
    const l = computeLayout(width, height);

    // O painel lateral nunca deixa a coluna de leitura apertada demais.
    if (l.isSplit) {
      expect(l.width - l.sidePanelWidth).toBeGreaterThanOrEqual(420);
      expect(l.sidePanelWidth).toBeGreaterThanOrEqual(280);
      expect(l.sidePanelWidth).toBeLessThanOrEqual(440);
    } else {
      expect(l.sidePanelWidth).toBe(0);
    }

    // A barra lateral de capítulos nunca passa de 85% da tela.
    expect(l.sidebarWidth).toBeLessThanOrEqual(Math.floor(width * 0.85) + 1);
    expect(l.sidebarWidth).toBeGreaterThan(0);

    // O painel inferior do dicionário cabe na tela.
    expect(l.sheetMaxHeight).toBeLessThan(height);
    expect(l.sheetMaxWidth).toBeLessThanOrEqual(720);

    expect(l.pagePadding).toBeGreaterThanOrEqual(8);
    expect(l.readerMaxWidth).toBeLessThanOrEqual(l.contentMaxWidth);
  });

  it('uses tabs (single column) on phones and split view from 720px', () => {
    expect(computeLayout(390, 844).isSplit).toBe(false);
    expect(computeLayout(719, 900).isSplit).toBe(false);
    expect(computeLayout(720, 900).isSplit).toBe(true);
    expect(computeLayout(1024, 768).isSplit).toBe(true);
  });

  it('stacks the header only on narrow AND tall screens (not on landscape phones)', () => {
    expect(computeLayout(390, 844).headerStacked).toBe(true);
    expect(computeLayout(568, 320).headerStacked).toBe(false);
    expect(computeLayout(768, 1024).headerStacked).toBe(false);
  });

  it('flags short heights (landscape phones) and shrinks spacing', () => {
    const landscape = computeLayout(844, 390);
    expect(landscape.isShortHeight).toBe(true);
    expect(landscape.pagePadding).toBe(8);
    expect(computeLayout(844, 390).sheetMaxHeight).toBe(Math.round(390 * 0.9));
    expect(computeLayout(390, 844).isShortHeight).toBe(false);
  });

  it('scales the reading font with screen size (never negative for the user setting)', () => {
    expect(computeLayout(320, 568).fontBoost).toBe(-1);
    expect(computeLayout(390, 844).fontBoost).toBe(0);
    expect(computeLayout(1280, 720).fontBoost).toBe(1);
    expect(computeLayout(1440, 900).fontBoost).toBe(2);
    expect(computeLayout(1920, 1080).fontBoost).toBe(3);
  });

  it('classifies breakpoints', () => {
    expect(computeLayout(390, 844).breakpoint).toBe('phone');
    expect(computeLayout(650, 900).breakpoint).toBe('phoneWide');
    expect(computeLayout(820, 1180).breakpoint).toBe('tablet');
    expect(computeLayout(1280, 720).breakpoint).toBe('laptop');
    expect(computeLayout(1920, 1080).breakpoint).toBe('desktop');
  });

  it('does not blow up with zero/negative sizes (first render before layout)', () => {
    expect(() => computeLayout(0, 0)).not.toThrow();
    expect(() => computeLayout(-10, -10)).not.toThrow();
  });
});

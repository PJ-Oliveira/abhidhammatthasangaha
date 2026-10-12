// src/__tests__/responsiveness_viewports.test.ts
import { computeLayout } from '../theme/layout';

describe('Exhaustive Multi-Device Responsiveness & Viewport Matrix Test', () => {
  describe('📱 1. Celular Pequeno (Small Mobile: 320px - 375px)', () => {
    it('iPhone SE 1st Gen (320 x 568)', () => {
      const layout = computeLayout(320, 568);
      expect(layout.breakpoint).toBe('phone');
      expect(layout.isSplit).toBe(false);
      expect(layout.headerStacked).toBe(true);
      expect(layout.pagePadding).toBe(10);
      expect(layout.sidebarWidth).toBe(Math.round(320 * 0.85));
      expect(layout.fontBoost).toBe(-1);
      expect(layout.isShortHeight).toBe(false);
    });

    it('Small Android (360 x 640)', () => {
      const layout = computeLayout(360, 640);
      expect(layout.breakpoint).toBe('phone');
      expect(layout.isSplit).toBe(false);
      expect(layout.headerStacked).toBe(true);
      expect(layout.pagePadding).toBe(10);
      expect(layout.fontBoost).toBe(0);
    });

    it('iPhone SE 2nd/3rd Gen (375 x 667)', () => {
      const layout = computeLayout(375, 667);
      expect(layout.breakpoint).toBe('phone');
      expect(layout.isSplit).toBe(false);
      expect(layout.headerStacked).toBe(true);
      expect(layout.pagePadding).toBe(10);
      expect(layout.fontBoost).toBe(0);
    });
  });

  describe('📱 2. Celular Grande (Large Mobile: 412px - 430px)', () => {
    it('iPhone XR / 11 (414 x 896)', () => {
      const layout = computeLayout(414, 896);
      expect(layout.breakpoint).toBe('phone');
      expect(layout.isSplit).toBe(false);
      expect(layout.headerStacked).toBe(true);
      expect(layout.pagePadding).toBe(14);
      expect(layout.isShortHeight).toBe(false);
    });

    it('iPhone 14 / 15 / 16 Pro Max (430 x 932)', () => {
      const layout = computeLayout(430, 932);
      expect(layout.breakpoint).toBe('phone');
      expect(layout.isSplit).toBe(false);
      expect(layout.headerStacked).toBe(true);
      expect(layout.pagePadding).toBe(14);
    });

    it('Samsung Galaxy S Ultra / Google Pixel (412 x 915)', () => {
      const layout = computeLayout(412, 915);
      expect(layout.breakpoint).toBe('phone');
      expect(layout.isSplit).toBe(false);
      expect(layout.headerStacked).toBe(true);
      expect(layout.pagePadding).toBe(14);
    });
  });

  describe('📱 3. Celular em Modo Paisagem (Mobile Landscape: short height)', () => {
    it('iPhone Landscape (667 x 375)', () => {
      const layout = computeLayout(667, 375);
      expect(layout.breakpoint).toBe('phoneWide');
      expect(layout.isShortHeight).toBe(true);
      expect(layout.pagePadding).toBe(8);
      expect(layout.headerStacked).toBe(false);
    });
  });

  describe('📟 4. iPad Pequeno / Tablet 8-10" (768px - 820px)', () => {
    it('iPad Mini / iPad 9.7" / 10.2" (768 x 1024)', () => {
      const layout = computeLayout(768, 1024);
      expect(layout.breakpoint).toBe('tablet');
      expect(layout.isSplit).toBe(true); // Split view active
      expect(layout.headerStacked).toBe(false);
      expect(layout.sidePanelWidth).toBe(280);
      expect(layout.pagePadding).toBe(20);
    });

    it('iPad Air / Pro 11" (820 x 1180)', () => {
      const layout = computeLayout(820, 1180);
      expect(layout.breakpoint).toBe('tablet');
      expect(layout.isSplit).toBe(true);
      expect(layout.headerStacked).toBe(false);
      expect(layout.sidePanelWidth).toBe(280);
      expect(layout.pagePadding).toBe(20);
    });
  });

  describe('📟 5. iPad Grande / Tablet 12.9" (1024px)', () => {
    it('iPad Pro 12.9" Portrait (1024 x 1366)', () => {
      const layout = computeLayout(1024, 1366);
      expect(layout.breakpoint).toBe('laptop');
      expect(layout.isSplit).toBe(true);
      expect(layout.headerStacked).toBe(false);
      expect(layout.sidePanelWidth).toBe(348);
      expect(layout.pagePadding).toBe(20);
      expect(layout.fontBoost).toBe(1);
    });

    it('iPad Pro 12.9" Landscape (1366 x 1024)', () => {
      const layout = computeLayout(1366, 1024);
      expect(layout.breakpoint).toBe('laptop');
      expect(layout.isSplit).toBe(true);
      expect(layout.headerStacked).toBe(false);
      expect(layout.sidePanelWidth).toBe(440);
      expect(layout.pagePadding).toBe(20);
      expect(layout.fontBoost).toBe(1);
    });
  });

  describe('💻 6. Notebook (1280px - 1366px)', () => {
    it('Standard 13" Laptop (1280 x 800)', () => {
      const layout = computeLayout(1280, 800);
      expect(layout.breakpoint).toBe('laptop');
      expect(layout.isSplit).toBe(true);
      expect(layout.headerStacked).toBe(false);
      expect(layout.sidePanelWidth).toBe(435);
      expect(layout.pagePadding).toBe(20);
      expect(layout.fontBoost).toBe(1);
    });

    it('HD Laptop (1366 x 768)', () => {
      const layout = computeLayout(1366, 768);
      expect(layout.breakpoint).toBe('laptop');
      expect(layout.isSplit).toBe(true);
      expect(layout.headerStacked).toBe(false);
      expect(layout.sidePanelWidth).toBe(440);
      expect(layout.pagePadding).toBe(20);
      expect(layout.fontBoost).toBe(1);
    });
  });

  describe('💻 7. MacBook (1440px - 1512px)', () => {
    it('MacBook Air 13" Retina (1440 x 900)', () => {
      const layout = computeLayout(1440, 900);
      expect(layout.breakpoint).toBe('desktop');
      expect(layout.isSplit).toBe(true);
      expect(layout.headerStacked).toBe(false);
      expect(layout.sidePanelWidth).toBe(440); // clamp limit max 440
      expect(layout.pagePadding).toBe(20);
      expect(layout.fontBoost).toBe(2);
    });

    it('MacBook Pro 14" / 16" (1512 x 982)', () => {
      const layout = computeLayout(1512, 982);
      expect(layout.breakpoint).toBe('desktop');
      expect(layout.isSplit).toBe(true);
      expect(layout.headerStacked).toBe(false);
      expect(layout.sidePanelWidth).toBe(440);
      expect(layout.pagePadding).toBe(20);
      expect(layout.fontBoost).toBe(2);
    });
  });

  describe('🖥️ 8. Desktop (1920px - 2560px)', () => {
    it('Full HD 1080p Monitor (1920 x 1080)', () => {
      const layout = computeLayout(1920, 1080);
      expect(layout.breakpoint).toBe('desktop');
      expect(layout.isSplit).toBe(true);
      expect(layout.headerStacked).toBe(false);
      expect(layout.sidePanelWidth).toBe(440);
      expect(layout.pagePadding).toBe(20);
      expect(layout.contentMaxWidth).toBe(1680); // Content max width prevents excessive stretching
      expect(layout.fontBoost).toBe(3);
    });

    it('2K / QHD Ultrawide Monitor (2560 x 1440)', () => {
      const layout = computeLayout(2560, 1440);
      expect(layout.breakpoint).toBe('desktop');
      expect(layout.isSplit).toBe(true);
      expect(layout.contentMaxWidth).toBe(1680);
      expect(layout.sidePanelWidth).toBe(440);
      expect(layout.pagePadding).toBe(20);
      expect(layout.fontBoost).toBe(3);
    });
  });
});

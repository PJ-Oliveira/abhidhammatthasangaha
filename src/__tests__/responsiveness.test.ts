// src/__tests__/responsiveness.test.ts
import { computeLayout } from '../theme/layout';

describe('Multi-Resolution Responsiveness Layout Suite', () => {
  describe('Mobile Devices (Narrow Screens: < 720px)', () => {
    it('handles iPhone SE (375 x 667) correctly', () => {
      const layout = computeLayout(375, 667);
      expect(layout.breakpoint).toBe('phone');
      expect(layout.isSplit).toBe(false); // Mobile uses tab bar, not split panel
      expect(layout.headerStacked).toBe(true);
      expect(layout.pagePadding).toBe(10);
      expect(layout.fontBoost).toBe(0);
      expect(layout.sidebarWidth).toBe(Math.round(375 * 0.85));
    });

    it('handles Android Pixel / Galaxy (412 x 915) correctly', () => {
      const layout = computeLayout(412, 915);
      expect(layout.breakpoint).toBe('phone');
      expect(layout.isSplit).toBe(false);
      expect(layout.headerStacked).toBe(true);
      expect(layout.pagePadding).toBe(14);
      expect(layout.isShortHeight).toBe(false);
    });

    it('detects short landscape mobile screen correctly', () => {
      const layout = computeLayout(667, 375);
      expect(layout.breakpoint).toBe('phoneWide');
      expect(layout.isShortHeight).toBe(true);
      expect(layout.pagePadding).toBe(8);
    });
  });

  describe('Tablets and iPads (720px <= width < 1024px)', () => {
    it('handles iPad 10.2" / Mini (768 x 1024) with split-panel study mode', () => {
      const layout = computeLayout(768, 1024);
      expect(layout.breakpoint).toBe('tablet');
      expect(layout.isSplit).toBe(true); // Split view active for side-by-side dictionary!
      expect(layout.headerStacked).toBe(false);
      expect(layout.sidePanelWidth).toBe(280);
      expect(layout.pagePadding).toBe(20);
      expect(layout.fontBoost).toBe(0);
    });

    it('handles iPad Air / Pro 11" (820 x 1180) with split panel', () => {
      const layout = computeLayout(820, 1180);
      expect(layout.breakpoint).toBe('tablet');
      expect(layout.isSplit).toBe(true);
      expect(layout.headerStacked).toBe(false);
      expect(layout.pagePadding).toBe(20);
      expect(layout.sidePanelWidth).toBe(280);
    });
  });

  describe('Desktop and Laptop Screens (width >= 1024px)', () => {
    it('handles 13" Laptop (1280 x 800) with generous side panel', () => {
      const layout = computeLayout(1280, 800);
      expect(layout.breakpoint).toBe('laptop');
      expect(layout.isSplit).toBe(true);
      expect(layout.headerStacked).toBe(false);
      expect(layout.sidePanelWidth).toBe(435);
      expect(layout.pagePadding).toBe(20);
      expect(layout.fontBoost).toBe(1);
    });

    it('handles Full HD Desktop (1920 x 1080) with centered frame and max-width restraint', () => {
      const layout = computeLayout(1920, 1080);
      expect(layout.breakpoint).toBe('desktop');
      expect(layout.isSplit).toBe(true);
      expect(layout.sidePanelWidth).toBe(440);
      expect(layout.contentMaxWidth).toBe(1680);
      expect(layout.readerMaxWidth).toBe(880);
      expect(layout.pagePadding).toBe(20);
      expect(layout.fontBoost).toBe(3);
    });
  });
});

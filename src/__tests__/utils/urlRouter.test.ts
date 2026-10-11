// src/__tests__/utils/urlRouter.test.ts
import {
  chapterNumberToId,
  chapterIdToNumber,
  parseRoute,
  getParagraphDirectUrl,
} from '../../utils/urlRouter';

describe('urlRouter Utility', () => {
  describe('chapterNumberToId', () => {
    it('maps numbers 1 to 9 to canonical IDs', () => {
      expect(chapterNumberToId(1)).toBe('ch01');
      expect(chapterNumberToId(5)).toBe('ch05');
      expect(chapterNumberToId(9)).toBe('ch09');
    });

    it('falls back to ch01 for out of bounds numbers', () => {
      expect(chapterNumberToId(0)).toBe('ch01');
      expect(chapterNumberToId(10)).toBe('ch01');
      expect(chapterNumberToId(-5)).toBe('ch01');
    });
  });

  describe('chapterIdToNumber', () => {
    it('converts canonical chapter IDs to numbers', () => {
      expect(chapterIdToNumber('ch01')).toBe(1);
      expect(chapterIdToNumber('ch05')).toBe(5);
      expect(chapterIdToNumber('ch09')).toBe(9);
      expect(chapterIdToNumber('CH03')).toBe(3);
    });

    it('falls back to 1 for unparseable strings', () => {
      expect(chapterIdToNumber('')).toBe(1);
      expect(chapterIdToNumber('invalid')).toBe(1);
    });
  });

  describe('parseRoute', () => {
    it('parses standard chapter route /abhidhammatthasaṅgaha/1', () => {
      const parsed = parseRoute('/abhidhammatthasaṅgaha/1');
      expect(parsed.chapterId).toBe('ch01');
      expect(parsed.chapterNumber).toBe(1);
      expect(parsed.segmentId).toBeNull();
    });

    it('parses paragraph anchor route /abhidhammatthasaṅgaha/1/abhm-1.3', () => {
      const parsed = parseRoute('/abhidhammatthasaṅgaha/1/abhm-1.3');
      expect(parsed.chapterId).toBe('ch01');
      expect(parsed.chapterNumber).toBe(1);
      expect(parsed.segmentId).toBe('abhm-1.3');
    });

    it('parses normalized ASCII URL /abhidhammatthasangaha/2/abhm-2.5', () => {
      const parsed = parseRoute('/abhidhammatthasangaha/2/abhm-2.5');
      expect(parsed.chapterId).toBe('ch02');
      expect(parsed.chapterNumber).toBe(2);
      expect(parsed.segmentId).toBe('abhm-2.5');
    });

    it('parses direct short route /3/abhm-3.1', () => {
      const parsed = parseRoute('/3/abhm-3.1');
      expect(parsed.chapterId).toBe('ch03');
      expect(parsed.chapterNumber).toBe(3);
      expect(parsed.segmentId).toBe('abhm-3.1');
    });

    it('extracts hash anchor if segmentId is not in path', () => {
      const parsed = parseRoute('/abhidhammatthasaṅgaha/1', '#seg-abhm-1.8');
      expect(parsed.segmentId).toBe('abhm-1.8');
    });

    it('defaults to chapter 1 when root or empty', () => {
      const parsed = parseRoute('/');
      expect(parsed.chapterId).toBe('ch01');
      expect(parsed.chapterNumber).toBe(1);
      expect(parsed.segmentId).toBeNull();
    });
  });

  describe('getParagraphDirectUrl', () => {
    it('generates standard deep link URL', () => {
      const url = getParagraphDirectUrl(1, 'abhm-1.3');
      expect(url).toContain('/abhidhammatthasaṅgaha/1/abhm-1.3');
    });
  });
});

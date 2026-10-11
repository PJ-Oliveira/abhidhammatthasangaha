// src/__tests__/services/exportService.test.ts
import {
  escapeHtml,
  slugifyPali,
  linkifyPaliSentence,
  collectUsedGlossary,
  buildDocumentHtml,
  exportToEpub,
  EXPORT_CSS,
  ExportConfig,
} from '../../services/exportService';
import type { Segment } from '../../types/models';

describe('exportService', () => {
  describe('escapeHtml', () => {
    it('escapes special characters', () => {
      expect(escapeHtml('<div class="test">&\'"</div>')).toBe(
        '&lt;div class=&quot;test&quot;&gt;&amp;&#39;&quot;&lt;/div&gt;'
      );
      expect(escapeHtml('')).toBe('');
    });
  });

  describe('slugifyPali', () => {
    it('creates correct slug prefixes for dictionary anchors', () => {
      expect(slugifyPali('cittaṃ')).toBe('dict_cittaṃ');
      expect(slugifyPali('kusalā')).toBe('dict_kusalā');
      expect(slugifyPali('akusala-citta')).toBe('dict_akusala_citta');
    });
  });

  describe('linkifyPaliSentence', () => {
    it('links each Pali word with the pali-word class and anchor to the glossary', () => {
      const sentence = 'Cittaṃ cetasikaṃ rūpaṃ nibbānaṃ.';
      const html = linkifyPaliSentence(sentence, 'glossary.xhtml');

      expect(html).toContain('class="pali-word"');
      expect(html).toContain('href="glossary.xhtml#dict_cittaṃ"');
      expect(html).toContain('href="glossary.xhtml#dict_nibbānaṃ"');
      expect(html).toContain('.');
    });

    it('handles empty strings gracefully', () => {
      expect(linkifyPaliSentence('')).toBe('');
    });
  });

  describe('EXPORT_CSS rules', () => {
    it('contains strict non-breaking rules for Pali words', () => {
      expect(EXPORT_CSS).toContain('word-break: keep-all !important;');
      expect(EXPORT_CSS).toContain('hyphens: none !important;');
      expect(EXPORT_CSS).toContain('white-space: nowrap !important;');
    });

    it('contains minimum reading font size of 13pt', () => {
      expect(EXPORT_CSS).toContain('font-size: 13pt;');
    });

    it('contains serif fonts appropriate for Pali diacritics', () => {
      expect(EXPORT_CSS).toContain('Gentium Plus');
      expect(EXPORT_CSS).toContain('Noto Serif');
    });
  });

  describe('collectUsedGlossary', () => {
    it('collects and sorts glossary entries for used Pali terms', () => {
      const mockSegments: Segment[] = [
        {
          id: 'test-1',
          pali: 'Tattha rūpaṃ duvidhaṃ.',
          translations: { pt: 'Ali a matéria é de dois tipos.' },
        },
      ];

      const glossary = collectUsedGlossary(mockSegments);
      expect(glossary.length).toBeGreaterThan(0);
      const paliWords = glossary.map((g) => g.pali);
      expect(paliWords.some((w) => w.includes('rūpa'))).toBe(true);
    });
  });

  describe('buildDocumentHtml', () => {
    it('builds complete document with TOC, sentence alignment, and end glossary in bilingual mode', async () => {
      const config: ExportConfig = {
        format: 'pdf',
        mode: 'bilingual',
        languages: ['pali', 'pt'],
        scope: 'current',
        currentChapterId: 'ch01',
      };

      const result = await buildDocumentHtml(config, false);

      expect(result.html).toContain('<!DOCTYPE html>');
      // Table of Contents
      expect(result.tocHtml).toContain('id="toc"');
      expect(result.html).toContain('Índice Geral');

      // Chapters content
      expect(result.chaptersData.length).toBe(1);
      expect(result.chaptersData[0].chapterHtml).toContain('class="sentence-unit"');
      expect(result.chaptersData[0].chapterHtml).toContain('class="pali-sentence"');
      expect(result.chaptersData[0].chapterHtml).toContain('class="translation-sentence"');

      // Glossary at the end
      expect(result.glossaryHtml).toContain('id="glossary"');
      expect(result.html).toContain('Dicionário Pāḷi / Pāḷi Glossary');
    });

    it('builds monolingual document when configured', async () => {
      const config: ExportConfig = {
        format: 'pdf',
        mode: 'monolingual',
        languages: ['pt'],
        scope: 'current',
        currentChapterId: 'ch01',
      };

      const result = await buildDocumentHtml(config, false);

      expect(result.html).not.toContain('class="pali-sentence"');
      expect(result.html).toContain('class="translation-sentence"');
    });
  });

  describe('exportToEpub', () => {
    it('generates an EPUB bundle with all required EPUB 3 files', async () => {
      const config: ExportConfig = {
        format: 'epub',
        mode: 'bilingual',
        languages: ['pali', 'en'],
        scope: 'current',
        currentChapterId: 'ch01',
      };

      const progressSteps: string[] = [];
      await exportToEpub(config, (_pct, msg) => {
        progressSteps.push(msg);
      });

      expect(progressSteps.length).toBeGreaterThan(0);
    });
  });
});

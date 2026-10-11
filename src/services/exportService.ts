// src/services/exportService.ts
import JSZip from 'jszip';
import { CHAPTERS, ChapterMeta } from '../data/chapters/chapterIndex';
import { loadChapter } from '../data/chapters/chapterLoader';
import { splitIntoSentences, sanitizeHtmlText } from '../utils/sentenceSplitter';
import { lookupWord, cleanPaliToken } from './dictionaryService';
import type { Segment, Language, DictionaryEntry } from '../types/models';

export type ExportFormat = 'epub' | 'pdf';
export type ExportMode = 'bilingual' | 'monolingual';

export interface ExportConfig {
  format: ExportFormat;
  mode: ExportMode;
  languages: Language[];
  scope: 'all' | 'current';
  currentChapterId: string;
}

export function escapeHtml(str: string): string {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

export function slugifyPali(word: string): string {
  const clean = cleanPaliToken(word).toLowerCase();
  return 'dict_' + clean.replace(/[^a-zA-Z0-9āīūñṅṭḍṇḷṃĀĪŪÑṄṬḌṆḶṂ]/g, '_');
}

const WORD_CHARS = 'A-Za-z\\u00C0-\\u024F\\u1E00-\\u1EFF';
const WORD_PATTERN = new RegExp(`([^${WORD_CHARS}]+)`, 'g');
const SEPARATOR_ONLY = new RegExp(`^[^${WORD_CHARS}]+$`);

/**
 * Converte uma sentença em Pāli em HTML com cada palavra em Pāli ligada ao seu verbete
 * no dicionário no final do tratado, e com regra estrita contra quebra de linha nas palavras.
 */
export function linkifyPaliSentence(
  paliSentence: string,
  targetFilePrefix: string = ''
): string {
  if (!paliSentence) return '';
  // Remove marcações HTML brutas mantendo apenas o texto para tokenização
  const cleanText = paliSentence.replace(/<[^>]+>/g, '');
  const tokens = cleanText.split(WORD_PATTERN);

  let html = '';
  for (const token of tokens) {
    if (!token) continue;
    if (SEPARATOR_ONLY.test(token)) {
      html += escapeHtml(token);
      continue;
    }

    const clean = cleanPaliToken(token);
    const entry = lookupWord(clean);
    const slug = slugifyPali(entry ? entry.pali : clean);

    // Palavras em Pāli não podem quebrar linha (white-space: nowrap e word-break: keep-all)
    html += `<a href="${targetFilePrefix}#${slug}" class="pali-word" title="Ver no dicionário">${escapeHtml(
      token
    )}</a>`;
  }

  return html;
}

/**
 * Coleta todos os termos em Pāli utilizados nos capítulos selecionados
 * e retorna seus verbetes catalogados no dicionário.
 */
export function collectUsedGlossary(
  allSegments: Segment[]
): DictionaryEntry[] {
  const seenSlugs = new Set<string>();
  const glossaryEntries: DictionaryEntry[] = [];

  for (const seg of allSegments) {
    const cleanText = seg.pali.replace(/<[^>]+>/g, '');
    const tokens = cleanText.split(WORD_PATTERN);

    for (const token of tokens) {
      if (!token || SEPARATOR_ONLY.test(token)) continue;
      const clean = cleanPaliToken(token);
      const entry = lookupWord(clean);
      const headword = entry ? entry.pali : clean;
      const slug = slugifyPali(headword);

      if (!seenSlugs.has(slug)) {
        seenSlugs.add(slug);
        if (entry) {
          glossaryEntries.push(entry);
        } else {
          // Cria verbete de fallback caso não esteja catalogado
          glossaryEntries.push({
            pali: headword,
            grammar: 'termo em Pāli',
            meaning: {
              en: `Pāli term: ${headword}`,
              pt: `Termo em Pāli: ${headword}`,
              es: `Término en Pāli: ${headword}`,
            },
          });
        }
      }
    }
  }

  // Ordena alfabeticamente
  return glossaryEntries.sort((a, b) => a.pali.localeCompare(b.pali, 'pi'));
}

/**
 * CSS tipográfico de alta qualidade para leitura (tamanho mínimo 13, fontes serigrafadas,
 * regra de não quebra de palavras em Pāli, e alinhamento linha por linha).
 */
export const EXPORT_CSS = `
@import url('https://fonts.googleapis.com/css2?family=Gentium+Plus:ital,wght@0,400;0,700;1,400;1,700&family=Noto+Serif:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap');

@page {
  size: A4;
  margin: 24mm 20mm 24mm 20mm;
  @top-left {
    content: "Abhidhammatthasaṅgaha";
    font-family: 'Gentium Plus', 'Noto Serif', Georgia, serif;
    font-size: 9pt;
    color: #8C7355;
    font-style: italic;
  }
  @top-right {
    content: "Anuruddhācariya";
    font-family: 'Gentium Plus', 'Noto Serif', Georgia, serif;
    font-size: 9pt;
    color: #8C7355;
  }
  @bottom-right {
    content: "Página " counter(page);
    font-family: 'Gentium Plus', 'Noto Serif', Georgia, serif;
    font-size: 9.5pt;
    color: #6A5B4C;
  }
  @bottom-left {
    content: "Edição de Estudo Theravāda";
    font-family: 'Gentium Plus', 'Noto Serif', Georgia, serif;
    font-size: 8.5pt;
    color: #A08C75;
  }
}

@page :first {
  @top-left { content: normal; }
  @top-right { content: normal; }
  @bottom-left { content: normal; }
  @bottom-right { content: normal; }
}

body {
  margin: 0;
  padding: 0;
  font-family: 'Gentium Plus', 'Noto Serif', Georgia, 'Times New Roman', serif;
  font-size: 13pt;
  line-height: 1.65;
  color: #2B2118;
  background-color: #FFFFFF;
}

.book-title-page {
  text-align: center;
  page-break-after: always;
  padding-top: 15%;
  padding-bottom: 20%;
}

.main-title {
  font-size: 28pt;
  font-weight: 700;
  color: #4B2E2A;
  margin-bottom: 12px;
  line-height: 1.25;
}

.sub-title {
  font-size: 16pt;
  font-style: italic;
  color: #705335;
  margin-bottom: 30px;
}

.meta-author {
  font-size: 13pt;
  color: #554433;
  margin-top: 40px;
}

.meta-lang {
  font-size: 11pt;
  color: #8C7355;
  margin-top: 10px;
}

/* Índice de Capítulos (Table of Contents) */
.toc-section {
  page-break-before: always;
  page-break-after: always;
  margin-bottom: 30px;
}

.toc-title {
  font-size: 20pt;
  font-weight: 700;
  color: #4B2E2A;
  border-bottom: 2px solid #E8DCC8;
  padding-bottom: 8px;
  margin-bottom: 20px;
  text-align: center;
}

.toc-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.toc-item {
  margin-bottom: 12px;
  border-bottom: 1px dotted #D8C7B0;
  padding-bottom: 4px;
}

.toc-link {
  text-decoration: none;
  color: #4B2E2A;
  display: flex;
  justify-content: space-between;
  font-size: 13pt;
}

.toc-link:hover {
  color: #8B4513;
}

/* Capítulos */
.chapter-section {
  page-break-before: always;
  margin-top: 24px;
  margin-bottom: 36px;
}

.chapter-header {
  border-bottom: 2px solid #4B2E2A;
  padding-bottom: 10px;
  margin-bottom: 24px;
}

.chapter-number {
  font-size: 13pt;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: #8C7355;
  font-weight: 700;
}

.chapter-pali-title {
  font-size: 20pt;
  color: #4B2E2A;
  margin: 4px 0;
  font-weight: 700;
}

.chapter-trans-title {
  font-size: 14pt;
  font-style: italic;
  color: #5D4E37;
  margin: 0;
}

/* Segmentos e Sentenças alinhadas linha por linha */
.segment-container {
  margin-bottom: 20px;
  page-break-inside: avoid;
}

.segment-id {
  font-size: 9.5pt;
  color: #9C8262;
  font-weight: 700;
  margin-bottom: 4px;
  letter-spacing: 0.5px;
}

.sentence-unit {
  margin-bottom: 10px;
  padding-bottom: 8px;
  border-bottom: 1px solid #F4EFE6;
}

.sentence-unit:last-child {
  border-bottom: none;
}

/* Regra estrita: Palavras em Pāli NÃO podem quebrar linha */
.pali-sentence {
  color: #4B2E2A;
  font-size: 13.5pt;
  line-height: 1.7;
  margin-bottom: 4px;
  word-break: keep-all !important;
  hyphens: none !important;
  -webkit-hyphens: none !important;
}

.pali-word {
  white-space: nowrap !important;
  word-break: keep-all !important;
  hyphens: none !important;
  -webkit-hyphens: none !important;
  color: #4B2E2A;
  text-decoration: none;
  border-bottom: 1px dotted rgba(75, 46, 42, 0.45);
}

.pali-word:hover {
  background-color: #F8F2E4;
  color: #8B4513;
}

.translation-sentence {
  color: #4A3E2D;
  font-size: 13pt;
  font-style: italic;
  line-height: 1.6;
  margin-top: 2px;
  margin-bottom: 4px;
}

.lang-badge {
  font-size: 8.5pt;
  font-style: normal;
  font-weight: 700;
  color: #8C7355;
  background: #EFE6D6;
  padding: 1px 4px;
  border-radius: 3px;
  margin-right: 6px;
  vertical-align: middle;
}

/* Dicionário no final do tratado */
.glossary-section {
  page-break-before: always;
  margin-top: 30px;
}

.glossary-title {
  font-size: 22pt;
  color: #4B2E2A;
  font-weight: 700;
  border-bottom: 2px solid #4B2E2A;
  padding-bottom: 8px;
  margin-bottom: 24px;
  text-align: center;
}

.glossary-intro {
  font-size: 12pt;
  color: #705B45;
  font-style: italic;
  margin-bottom: 24px;
  text-align: center;
}

.glossary-entry {
  margin-bottom: 14px;
  padding-bottom: 10px;
  border-bottom: 1px solid #EFE6D6;
  page-break-inside: avoid;
}

.glossary-headword {
  font-size: 14pt;
  color: #4B2E2A;
  font-weight: 700;
}

.glossary-grammar {
  font-size: 11pt;
  font-style: italic;
  color: #7A624A;
  margin-left: 6px;
}

.glossary-root {
  font-size: 10.5pt;
  color: #8C7355;
  margin-top: 2px;
}

.glossary-meaning {
  font-size: 12.5pt;
  color: #2E2E2E;
  margin-top: 3px;
  line-height: 1.5;
}
`;

/**
 * Constrói o HTML completo do documento estruturado e formatado linha a linha.
 */
export async function buildDocumentHtml(
  config: ExportConfig,
  isForEpub: boolean = false
): Promise<{
  html: string;
  chaptersData: Array<{
    meta: ChapterMeta;
    segments: Segment[];
    chapterHtml: string;
  }>;
  glossaryHtml: string;
  tocHtml: string;
}> {
  const targetChapters =
    config.scope === 'all'
      ? CHAPTERS
      : CHAPTERS.filter((c) => c.id === config.currentChapterId);

  const chaptersData = [];
  const allSegments: Segment[] = [];

  const showPali =
    config.mode === 'bilingual' || config.languages.includes('pali');
  const targetLanguages = config.languages.filter(
    (l): l is 'en' | 'pt' | 'es' => l !== 'pali'
  );
  // Se for bilíngue mas nenhuma língua de tradução estiver explicitada, usa PT por padrão
  if (config.mode === 'bilingual' && targetLanguages.length === 0) {
    targetLanguages.push('pt');
  }

  const primaryTranslationLang = targetLanguages[0] || 'pt';

  for (const ch of targetChapters) {
    const segments = await loadChapter(ch.id);
    allSegments.push(...segments);

    let chBody = '';

    for (const seg of segments) {
      const paliSentences = showPali ? splitIntoSentences(seg.pali) : [];
      const transMap: Record<string, string[]> = {};

      for (const lang of targetLanguages) {
        const raw = seg.translations[lang] || '';
        const clean = sanitizeHtmlText(raw);
        transMap[lang] = splitIntoSentences(clean);
      }

      const count = Math.max(
        paliSentences.length,
        ...targetLanguages.map((l) => (transMap[l] ? transMap[l].length : 0)),
        1
      );

      let segHtml = `<div class="segment-container" id="seg-${escapeHtml(
        seg.id
      )}">`;
      segHtml += `<div class="segment-id">${escapeHtml(seg.id)}</div>`;

      for (let i = 0; i < count; i++) {
        segHtml += `<div class="sentence-unit">`;

        // 1. Sentença em Pāli com links para o glossário
        if (showPali && i < paliSentences.length) {
          const pSent = paliSentences[i];
          const prefix = isForEpub ? 'glossary.xhtml' : '';
          const linkedPali = linkifyPaliSentence(pSent, prefix);
          segHtml += `<div class="pali-sentence">${linkedPali}</div>`;
        }

        // 2. Sentenças de tradução correspondentes (compulsoriamente em nova linha)
        for (const lang of targetLanguages) {
          const tList = transMap[lang];
          if (tList && i < tList.length) {
            const badge =
              targetLanguages.length > 1
                ? `<span class="lang-badge">${lang.toUpperCase()}</span>`
                : '';
            segHtml += `<div class="translation-sentence">${badge}${escapeHtml(
              tList[i]
            )}</div>`;
          }
        }

        segHtml += `</div>`; // .sentence-unit
      }

      segHtml += `</div>`; // .segment-container
      chBody += segHtml;
    }

    const chapterHtml = `
      <section class="chapter-section" id="${ch.id}">
        <div class="chapter-header">
          <div class="chapter-number">Capítulo ${ch.number}</div>
          <h2 class="chapter-pali-title">${escapeHtml(ch.paliTitle)}</h2>
          <h3 class="chapter-trans-title">${escapeHtml(
            ch.titles[primaryTranslationLang] || ch.titles.en
          )}</h3>
        </div>
        <div class="chapter-content">
          ${chBody}
        </div>
      </section>
    `;

    chaptersData.push({
      meta: ch,
      segments,
      chapterHtml,
    });
  }

  // Coleta o glossário de todos os termos utilizados
  const usedGlossary = collectUsedGlossary(allSegments);

  let glossaryHtml = `
    <section class="glossary-section" id="glossary">
      <h2 class="glossary-title">Dicionário Pāḷi / Pāḷi Glossary</h2>
      <div class="glossary-intro">
        Léxico do Abhidhammatthasaṅgaha compilado com o Digital Pāli Dictionary (DPD).
      </div>
      <div class="glossary-entries">
  `;

  for (const entry of usedGlossary) {
    const slug = slugifyPali(entry.pali);
    const meaning =
      entry.meaning[primaryTranslationLang] ||
      entry.meaning.pt ||
      entry.meaning.en;

    glossaryHtml += `
      <div class="glossary-entry" id="${slug}">
        <div class="glossary-headword">
          ${escapeHtml(entry.pali)}
          ${
            entry.grammar
              ? `<span class="glossary-grammar">(${escapeHtml(
                  entry.grammar
                )})</span>`
              : ''
          }
        </div>
        ${
          entry.root
            ? `<div class="glossary-root">Raiz/Construção: ${escapeHtml(
                entry.root
              )}</div>`
            : ''
        }
        <div class="glossary-meaning">${escapeHtml(meaning)}</div>
      </div>
    `;
  }

  glossaryHtml += `
      </div>
    </section>
  `;

  // Índice de Capítulos (TOC)
  let tocHtml = `
    <section class="toc-section" id="toc">
      <h2 class="toc-title">Índice Geral</h2>
      <ul class="toc-list">
  `;

  for (const ch of targetChapters) {
    const prefix = isForEpub ? `${ch.id}.xhtml` : '';
    tocHtml += `
      <li class="toc-item">
        <a class="toc-link" href="${prefix}#${ch.id}">
          <span>${ch.number}. ${escapeHtml(ch.paliTitle)}</span>
          <span style="font-style:italic;color:#705335;">${escapeHtml(
            ch.titles[primaryTranslationLang] || ch.titles.en
          )}</span>
        </a>
      </li>
    `;
  }

  const glossPrefix = isForEpub ? 'glossary.xhtml' : '';
  tocHtml += `
      <li class="toc-item">
        <a class="toc-link" href="${glossPrefix}#glossary">
          <span>📚 Dicionário Pāḷi (Glossário)</span>
          <span style="font-style:italic;color:#705335;">Vocabulário do Tratado</span>
        </a>
      </li>
    </ul>
  </section>
  `;

  const fullHtml = `<!DOCTYPE html>
<html lang="pi">
<head>
  <meta charset="UTF-8">
  <title>Abhidhammatthasaṅgaha</title>
  <style>
    ${EXPORT_CSS}
  </style>
</head>
<body>
  <div class="book-title-page">
    <h1 class="main-title">Abhidhammatthasaṅgaha</h1>
    <div class="sub-title">Compêndio das Matérias do Abhidhamma</div>
    <div class="meta-author">Ācariya Anuruddha</div>
    <div class="meta-lang">Edição Digital Trilíngue</div>
  </div>

  ${tocHtml}

  ${chaptersData.map((c) => c.chapterHtml).join('\n')}

  ${glossaryHtml}
</body>
</html>`;

  return {
    html: fullHtml,
    chaptersData,
    glossaryHtml,
    tocHtml,
  };
}

/**
 * Dispara o download de um Blob no navegador.
 */
export function downloadBlob(
  blob: Blob,
  filename: string
): void {
  if (typeof document === 'undefined') return;
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  setTimeout(() => URL.revokeObjectURL(url), 10000);
}

/**
 * Gera e baixa o arquivo EPUB do Abhidhammatthasaṅgaha.
 */
export async function exportToEpub(
  config: ExportConfig,
  onProgress?: (percent: number, msg: string) => void
): Promise<void> {
  onProgress?.(10, 'Compilando capítulos e sentenças...');

  const { chaptersData, glossaryHtml, tocHtml } = await buildDocumentHtml(
    config,
    true
  );

  onProgress?.(40, 'Empacotando estrutura EPUB 3...');

  const zip = new JSZip();

  // 1. mimetype (não comprimido)
  zip.file('mimetype', 'application/epub+zip', { compression: 'STORE' });

  // 2. container.xml
  zip.file(
    'META-INF/container.xml',
    `<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>`
  );

  // 3. CSS
  zip.file('OEBPS/style.css', EXPORT_CSS);

  // 4. Página de Rosto (Title)
  const titleXhtml = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="pi">
<head>
  <meta charset="utf-8"/>
  <title>Abhidhammatthasaṅgaha</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
  <div class="book-title-page">
    <h1 class="main-title">Abhidhammatthasaṅgaha</h1>
    <div class="sub-title">Compêndio das Matérias do Abhidhamma</div>
    <div class="meta-author">Ācariya Anuruddha</div>
    <div class="meta-lang">Edição Digital Trilíngue</div>
  </div>
</body>
</html>`;
  zip.file('OEBPS/title.xhtml', titleXhtml);

  // 5. Índice (TOC XHTML)
  const tocXhtml = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="pi">
<head>
  <meta charset="utf-8"/>
  <title>Índice Geral</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
  ${tocHtml}
</body>
</html>`;
  zip.file('OEBPS/toc.xhtml', tocXhtml);

  // 6. Capítulos
  for (const ch of chaptersData) {
    const chXhtml = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="pi">
<head>
  <meta charset="utf-8"/>
  <title>${escapeHtml(ch.meta.paliTitle)}</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
  ${ch.chapterHtml}
</body>
</html>`;
    zip.file(`OEBPS/${ch.meta.id}.xhtml`, chXhtml);
  }

  // 7. Glossário no final
  const glossaryXhtml = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="pi">
<head>
  <meta charset="utf-8"/>
  <title>Dicionário Pāḷi</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
  ${glossaryHtml}
</body>
</html>`;
  zip.file('OEBPS/glossary.xhtml', glossaryXhtml);

  // 8. nav.xhtml (EPUB 3 Navigation Document)
  const navXhtml = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="pi">
<head>
  <meta charset="utf-8"/>
  <title>Navegação</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>Índice de Capítulos</h1>
    <ol>
      <li><a href="title.xhtml">Capa / Título</a></li>
      <li><a href="toc.xhtml">Índice Geral</a></li>
      ${chaptersData
        .map(
          (c) =>
            `<li><a href="${c.meta.id}.xhtml">${c.meta.number}. ${escapeHtml(
              c.meta.paliTitle
            )}</a></li>`
        )
        .join('\n')}
      <li><a href="glossary.xhtml">📚 Dicionário Pāḷi</a></li>
    </ol>
  </nav>
</body>
</html>`;
  zip.file('OEBPS/nav.xhtml', navXhtml);

  // 9. toc.ncx (EPUB 2 / Compatibilidade universal)
  const ncx = `<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head>
  <meta name="dtb:uid" content="urn:uuid:abhidhammatthasangaha-reader"/>
  <meta name="dtb:depth" content="2"/>
  <meta name="dtb:totalPageCount" content="0"/>
  <meta name="dtb:maxPageNumber" content="0"/>
</head>
<docTitle><text>Abhidhammatthasaṅgaha</text></docTitle>
<navMap>
  <navPoint id="np-title" playOrder="1">
    <navLabel><text>Capa / Rosto</text></navLabel>
    <content src="title.xhtml"/>
  </navPoint>
  <navPoint id="np-toc" playOrder="2">
    <navLabel><text>Índice Geral</text></navLabel>
    <content src="toc.xhtml"/>
  </navPoint>
  ${chaptersData
    .map(
      (c, i) => `
    <navPoint id="np-${c.meta.id}" playOrder="${i + 3}">
      <navLabel><text>${c.meta.number}. ${escapeHtml(
        c.meta.paliTitle
      )}</text></navLabel>
      <content src="${c.meta.id}.xhtml"/>
    </navPoint>`
    )
    .join('')}
  <navPoint id="np-glossary" playOrder="${chaptersData.length + 3}">
    <navLabel><text>📚 Dicionário Pāḷi</text></navLabel>
    <content src="glossary.xhtml"/>
  </navPoint>
</navMap>
</ncx>`;
  zip.file('OEBPS/toc.ncx', ncx);

  // 10. content.opf
  const opf = `<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="3.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>Abhidhammatthasaṅgaha</dc:title>
    <dc:creator>Ācariya Anuruddha</dc:creator>
    <dc:language>pi</dc:language>
    <dc:identifier id="BookId">urn:uuid:abhidhammatthasangaha-reader</dc:identifier>
    <meta property="dcterms:modified">${new Date().toISOString().replace(/\.[0-9]+Z$/, 'Z')}</meta>
  </metadata>
  <manifest>
    <item id="style" href="style.css" media-type="text/css"/>
    <item id="toc-ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="title" href="title.xhtml" media-type="application/xhtml+xml"/>
    <item id="toc" href="toc.xhtml" media-type="application/xhtml+xml"/>
    ${chaptersData
      .map(
        (c) =>
          `<item id="${c.meta.id}" href="${c.meta.id}.xhtml" media-type="application/xhtml+xml"/>`
      )
      .join('\n    ')}
    <item id="glossary" href="glossary.xhtml" media-type="application/xhtml+xml"/>
  </manifest>
  <spine toc="toc-ncx">
    <itemref idref="title"/>
    <itemref idref="toc"/>
    ${chaptersData.map((c) => `<itemref idref="${c.meta.id}"/>`).join('\n    ')}
    <itemref idref="glossary"/>
  </spine>
</package>`;
  zip.file('OEBPS/content.opf', opf);

  onProgress?.(75, 'Gerando arquivo binário...');

  const blob = await zip.generateAsync({
    type: 'blob',
    mimeType: 'application/epub+zip',
  });

  onProgress?.(100, 'Download concluído!');

  const filename =
    config.scope === 'all'
      ? 'Abhidhammatthasangaha_Completo.epub'
      : `Abhidhammatthasangaha_${config.currentChapterId}.epub`;

  downloadBlob(blob, filename);
}

/**
 * Abre a janela de impressão com formatação estrita de PDF, sumário de capítulos,
 * dicionário ao final com âncoras ativas e disparo automático de diálogo de impressão/salvar como PDF.
 */
export async function exportToPdf(
  config: ExportConfig,
  onProgress?: (percent: number, msg: string) => void
): Promise<void> {
  onProgress?.(20, 'Gerando documento formatado em PDF...');

  const { html } = await buildDocumentHtml(config, false);

  onProgress?.(60, 'Preparando janela de impressão...');

  if (typeof window !== 'undefined') {
    const printWindow = window.open('', '_blank');
    if (printWindow) {
      printWindow.document.open();
      printWindow.document.write(html);
      printWindow.document.close();

      onProgress?.(100, 'Janela aberta para impressão/salvar PDF!');

      // Aguarda carregamento de estilos e fontes antes de disparar o print dialog
      setTimeout(() => {
        try {
          printWindow.focus();
          printWindow.print();
        } catch {
          // Ignora se o navegador bloquear o foco
        }
      }, 600);
    } else {
      // Fallback: se pop-up for bloqueado, faz download do arquivo HTML para impressão
      const blob = new Blob([html], { type: 'text/html;charset=utf-8' });
      downloadBlob(blob, 'Abhidhammatthasangaha_Documento_PDF.html');
      onProgress?.(100, 'Arquivo HTML pronto para impressão!');
    }
  }
}

const exportService = {
  exportToEpub,
  exportToPdf,
  buildDocumentHtml,
  collectUsedGlossary,
  linkifyPaliSentence,
  EXPORT_CSS,
};

if (typeof window !== 'undefined') {
  (window as unknown as { __exportService: typeof exportService }).__exportService = exportService;
}

export default exportService;

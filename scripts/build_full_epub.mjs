// scripts/build_full_epub.mjs
import JSZip from 'jszip';
import { readFileSync, writeFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const projectRoot = join(__dirname, '..');

const ARTIFACT_DIR = '/Users/pauloo/.gemini/antigravity/brain/134555de-9249-4384-b949-48418bc73dd8';

// Carrega dicionário
const dictRaw = readFileSync(join(projectRoot, 'src/data/paliDictionary.json'), 'utf-8');
const dictEntries = JSON.parse(dictRaw);
const dictMap = new Map();
for (const entry of dictEntries) {
  dictMap.set(entry.pali.toLowerCase(), entry);
}

function cleanPaliToken(word) {
  if (!word) return '';
  return word
    .replace(/^[^a-zA-Z0-9āīūñṅṭḍṇḷṃĀĪŪÑṄṬḌṆḶṂ]+/, '')
    .replace(/[^a-zA-Z0-9āīūñṅṭḍṇḷṃĀĪŪÑṄṬḌṆḶṂ]+$/, '');
}

function lookupWord(token) {
  if (!token) return null;
  const clean = cleanPaliToken(token).toLowerCase();
  if (dictMap.has(clean)) return dictMap.get(clean);
  // fallback sem diacríticos ou stem
  return null;
}

function slugifyPali(word) {
  const clean = cleanPaliToken(word).toLowerCase();
  return 'dict_' + clean.replace(/[^a-zA-Z0-9āīūñṅṭḍṇḷṃĀĪŪÑṄṬḌṆḶṂ]/g, '_');
}

function escapeHtml(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

const WORD_CHARS = 'A-Za-z\\u00C0-\\u024F\\u1E00-\\u1EFF';
const WORD_PATTERN = new RegExp(`([^${WORD_CHARS}]+)`, 'g');
const SEPARATOR_ONLY = new RegExp(`^[^${WORD_CHARS}]+$`);

function linkifyPaliSentence(paliSentence, targetFilePrefix = '') {
  if (!paliSentence) return '';
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

    html += `<a href="${targetFilePrefix}#${slug}" class="pali-word" title="Dicionário">${escapeHtml(
      token
    )}</a>`;
  }
  return html;
}

function splitIntoSentences(text) {
  if (!text) return [];
  const clean = text.replace(/<[^>]+>/g, '').trim();
  if (!clean) return [];

  const rawTokens = clean.split(/([.?]+)/);
  const sentences = [];
  let buffer = '';

  for (let i = 0; i < rawTokens.length; i++) {
    const token = rawTokens[i];
    if (token === '.' || token === '?') {
      const isListNumber = /^\s*\d+$/.test(buffer);
      if (isListNumber) {
        buffer += token;
      } else {
        const full = (buffer + token).trim();
        if (full) sentences.push(full);
        buffer = '';
      }
    } else {
      buffer += token;
    }
  }

  const remainder = buffer.trim();
  if (remainder) sentences.push(remainder);
  return sentences;
}

const CHAPTER_METAS = [
  { id: 'ch01', number: 1, paliTitle: 'Cittaparicchedo', titlePt: 'Compêndio da Consciência' },
  { id: 'ch02', number: 2, paliTitle: 'Cetasikaparicchedo', titlePt: 'Compêndio dos Fatores Mentais' },
  { id: 'ch03', number: 3, paliTitle: 'Pakiṇṇakaparicchedo', titlePt: 'Compêndio dos Diversos' },
  { id: 'ch04', number: 4, paliTitle: 'Vīthiparicchedo', titlePt: 'Compêndio do Processo Cognitivo' },
  { id: 'ch05', number: 5, paliTitle: 'Vīthimuttaparicchedo', titlePt: 'Compêndio dos Estados Livres de Processo' },
  { id: 'ch06', number: 6, paliTitle: 'Rūpaparicchedo', titlePt: 'Compêndio da Matéria e Nibbāna' },
  { id: 'ch07', number: 7, paliTitle: 'Samuccayaparicchedo', titlePt: 'Compêndio das Categorias' },
  { id: 'ch08', number: 8, paliTitle: 'Paccayaparicchedo', titlePt: 'Compêndio da Condicionalidade' },
  { id: 'ch09', number: 9, paliTitle: 'Kammaṭṭhānaparicchedo', titlePt: 'Compêndio dos Temas de Meditação' },
];

const CSS = `
@import url('https://fonts.googleapis.com/css2?family=Gentium+Plus:ital,wght@0,400;0,700;1,400;1,700&family=Noto+Serif:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap');

body {
  font-family: 'Gentium Plus', 'Noto Serif', Georgia, serif;
  font-size: 13pt;
  line-height: 1.65;
  color: #2B2118;
  margin: 20px;
}

.book-title-page { text-align: center; margin: 40px 0; }
.main-title { font-size: 26pt; color: #4B2E2A; margin-bottom: 8px; font-weight: 700; }
.sub-title { font-size: 15pt; font-style: italic; color: #705335; margin-bottom: 20px; }
.meta-author { font-size: 13pt; color: #554433; margin-top: 24px; }
.meta-lang { font-size: 11pt; color: #8C7355; margin-top: 8px; }

.toc-title { font-size: 20pt; color: #4B2E2A; text-align: center; border-bottom: 2px solid #E8DCC8; padding-bottom: 8px; }
.toc-list { list-style: none; padding: 0; }
.toc-item { margin-bottom: 12px; border-bottom: 1px dotted #D8C7B0; padding-bottom: 4px; }
.toc-link { text-decoration: none; color: #4B2E2A; display: flex; justify-content: space-between; font-size: 13pt; }

.chapter-header { border-bottom: 2px solid #4B2E2A; padding-bottom: 8px; margin-bottom: 20px; }
.chapter-number { font-size: 12pt; text-transform: uppercase; color: #8C7355; font-weight: 700; }
.chapter-pali-title { font-size: 20pt; color: #4B2E2A; margin: 4px 0; font-weight: 700; }
.chapter-trans-title { font-size: 14pt; font-style: italic; color: #5D4E37; margin: 0; }

.segment-container { margin-bottom: 20px; }
.segment-id { font-size: 9.5pt; color: #9C8262; font-weight: 700; margin-bottom: 4px; }
.sentence-unit { margin-bottom: 10px; padding-bottom: 6px; border-bottom: 1px solid #F4EFE6; }
.sentence-unit:last-child { border-bottom: none; }

.pali-sentence {
  color: #4B2E2A;
  font-size: 13.5pt;
  line-height: 1.7;
  margin-bottom: 4px;
  word-break: keep-all !important;
  hyphens: none !important;
}

.pali-word {
  white-space: nowrap !important;
  word-break: keep-all !important;
  hyphens: none !important;
  color: #4B2E2A;
  text-decoration: none;
  border-bottom: 1px dotted rgba(75, 46, 42, 0.45);
}

.translation-sentence {
  color: #4A3E2D;
  font-size: 13pt;
  font-style: italic;
  line-height: 1.6;
  margin-top: 2px;
  margin-bottom: 4px;
}

.glossary-title { font-size: 22pt; color: #4B2E2A; text-align: center; border-bottom: 2px solid #4B2E2A; padding-bottom: 8px; margin-bottom: 20px; }
.glossary-intro { font-size: 12pt; font-style: italic; color: #705B45; text-align: center; margin-bottom: 20px; }
.glossary-entry { margin-bottom: 14px; padding-bottom: 10px; border-bottom: 1px solid #EFE6D6; }
.glossary-headword { font-size: 14pt; color: #4B2E2A; font-weight: 700; }
.glossary-grammar { font-size: 11pt; font-style: italic; color: #7A624A; margin-left: 6px; }
.glossary-root { font-size: 10.5pt; color: #8C7355; margin-top: 2px; }
.glossary-meaning { font-size: 12.5pt; color: #2E2E2E; margin-top: 3px; line-height: 1.5; }
`;

(async () => {
  console.log('📚 Building complete EPUB 3 document...');
  const zip = new JSZip();

  zip.file('mimetype', 'application/epub+zip', { compression: 'STORE' });
  zip.file(
    'META-INF/container.xml',
    `<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>`
  );
  zip.file('OEBPS/style.css', CSS);

  // Title
  zip.file(
    'OEBPS/title.xhtml',
    `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="pi">
<head>
  <meta charset="utf-8"/>
  <title>Abhidhammatthasaṅgaha</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body class="book-title-page">
  <h1 class="main-title">Abhidhammatthasaṅgaha</h1>
  <div class="sub-title">Compêndio das Matérias do Abhidhamma</div>
  <div class="meta-author">Ācariya Anuruddha</div>
  <div class="meta-lang">Edição Digital Trilíngue (Pāli • Português)</div>
</body>
</html>`
  );

  const seenSlugs = new Set();
  const usedGlossary = [];
  const chaptersData = [];

  for (const meta of CHAPTER_METAS) {
    const rawData = readFileSync(join(projectRoot, `src/data/chapters/${meta.id}.json`), 'utf-8');
    const segments = JSON.parse(rawData);

    let chBody = '';

    for (const seg of segments) {
      const paliSentences = splitIntoSentences(seg.pali);
      const ptClean = seg.translations?.pt || seg.translations?.en || '';
      const ptSentences = splitIntoSentences(ptClean);

      // Coleta termos Pali para o glossário
      const cleanPali = seg.pali.replace(/<[^>]+>/g, '');
      const tokens = cleanPali.split(WORD_PATTERN);
      for (const tok of tokens) {
        if (!tok || SEPARATOR_ONLY.test(tok)) continue;
        const clean = cleanPaliToken(tok);
        const entry = lookupWord(clean);
        const headword = entry ? entry.pali : clean;
        const slug = slugifyPali(headword);
        if (!seenSlugs.has(slug)) {
          seenSlugs.add(slug);
          if (entry) {
            usedGlossary.push(entry);
          } else {
            usedGlossary.push({
              pali: headword,
              grammar: 'termo em Pāli',
              meaning: { pt: `Termo em Pāli: ${headword}`, en: `Pāli term: ${headword}` },
            });
          }
        }
      }

      const count = Math.max(paliSentences.length, ptSentences.length, 1);
      chBody += `<div class="segment-container" id="seg-${escapeHtml(seg.id)}">`;
      chBody += `<div class="segment-id">${escapeHtml(seg.id)}</div>`;

      for (let i = 0; i < count; i++) {
        chBody += `<div class="sentence-unit">`;
        if (i < paliSentences.length) {
          const linked = linkifyPaliSentence(paliSentences[i], 'glossary.xhtml');
          chBody += `<div class="pali-sentence">${linked}</div>`;
        }
        if (i < ptSentences.length) {
          chBody += `<div class="translation-sentence">${escapeHtml(ptSentences[i])}</div>`;
        }
        chBody += `</div>`;
      }
      chBody += `</div>`;
    }

    const chHtml = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="pi">
<head>
  <meta charset="utf-8"/>
  <title>${escapeHtml(meta.number + '. ' + meta.paliTitle)}</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
  <div class="chapter-header">
    <div class="chapter-number">Capítulo ${meta.number}</div>
    <h2 class="chapter-pali-title">${escapeHtml(meta.paliTitle)}</h2>
    <h3 class="chapter-trans-title">${escapeHtml(meta.titlePt)}</h3>
  </div>
  ${chBody}
</body>
</html>`;

    zip.file(`OEBPS/${meta.id}.xhtml`, chHtml);
    chaptersData.push({ meta, html: chHtml });
  }

  // Ordena glossário
  usedGlossary.sort((a, b) => a.pali.localeCompare(b.pali, 'pi'));

  let glossBody = `
  <h2 class="glossary-title">Dicionário Pāḷi / Glossário Geral</h2>
  <div class="glossary-intro">Léxico canônico do Abhidhammatthasaṅgaha compilado diretamente do Digital Pāli Dictionary (DPD).</div>
  <div class="glossary-entries">
  `;

  for (const entry of usedGlossary) {
    const slug = slugifyPali(entry.pali);
    const meaning = entry.meaning?.pt || entry.meaning?.en || '';
    glossBody += `
    <div class="glossary-entry" id="${slug}">
      <div class="glossary-headword">
        ${escapeHtml(entry.pali)}
        ${entry.grammar ? `<span class="glossary-grammar">(${escapeHtml(entry.grammar)})</span>` : ''}
      </div>
      ${entry.root ? `<div class="glossary-root">Raiz/Construção: ${escapeHtml(entry.root)}</div>` : ''}
      <div class="glossary-meaning">${escapeHtml(meaning)}</div>
    </div>
    `;
  }
  glossBody += `</div>`;

  const glossHtml = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="pi">
<head>
  <meta charset="utf-8"/>
  <title>Dicionário Pāḷi</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
  ${glossBody}
</body>
</html>`;
  zip.file('OEBPS/glossary.xhtml', glossHtml);

  // TOC
  let tocItems = '';
  for (const ch of CHAPTER_METAS) {
    tocItems += `<li class="toc-item"><a class="toc-link" href="${ch.id}.xhtml"><span>${ch.number}. ${escapeHtml(ch.paliTitle)}</span><span style="font-style:italic;">${escapeHtml(ch.titlePt)}</span></a></li>\n`;
  }
  tocItems += `<li class="toc-item"><a class="toc-link" href="glossary.xhtml"><span>📚 Dicionário Pāḷi (Glossário)</span><span style="font-style:italic;">${usedGlossary.length} verbetes</span></a></li>\n`;

  const tocHtml = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="pi">
<head>
  <meta charset="utf-8"/>
  <title>Índice Geral</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
  <h2 class="toc-title">Índice Geral dos Capítulos</h2>
  <ul class="toc-list">
    ${tocItems}
  </ul>
</body>
</html>`;
  zip.file('OEBPS/toc.xhtml', tocHtml);

  // nav.xhtml
  const navHtml = `<?xml version="1.0" encoding="UTF-8"?>
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
      <li><a href="title.xhtml">Página de Rosto</a></li>
      <li><a href="toc.xhtml">Índice Geral</a></li>
      ${CHAPTER_METAS.map((c) => `<li><a href="${c.id}.xhtml">${c.number}. ${escapeHtml(c.paliTitle)}</a></li>`).join('\n      ')}
      <li><a href="glossary.xhtml">Dicionário Pāḷi (Glossário)</a></li>
    </ol>
  </nav>
</body>
</html>`;
  zip.file('OEBPS/nav.xhtml', navHtml);

  // toc.ncx
  let playOrder = 1;
  const ncx = `<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head>
  <meta name="dtb:uid" content="urn:uuid:abhidhammatthasangaha-full"/>
  <meta name="dtb:depth" content="1"/>
  <meta name="dtb:totalPageCount" content="0"/>
  <meta name="dtb:maxPageNumber" content="0"/>
</head>
<docTitle><text>Abhidhammatthasaṅgaha</text></docTitle>
<navMap>
  <navPoint id="np-title" playOrder="${playOrder++}"><navLabel><text>Página de Rosto</text></navLabel><content src="title.xhtml"/></navPoint>
  <navPoint id="np-toc" playOrder="${playOrder++}"><navLabel><text>Índice Geral</text></navLabel><content src="toc.xhtml"/></navPoint>
  ${CHAPTER_METAS.map((c) => `<navPoint id="np-${c.id}" playOrder="${playOrder++}"><navLabel><text>${c.number}. ${escapeHtml(c.paliTitle)}</text></navLabel><content src="${c.id}.xhtml"/></navPoint>`).join('\n  ')}
  <navPoint id="np-glossary" playOrder="${playOrder++}"><navLabel><text>Dicionário Pāḷi (Glossário)</text></navLabel><content src="glossary.xhtml"/></navPoint>
</navMap>
</ncx>`;
  zip.file('OEBPS/toc.ncx', ncx);

  // content.opf
  const opf = `<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="3.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>Abhidhammatthasaṅgaha</dc:title>
    <dc:creator>Ācariya Anuruddha</dc:creator>
    <dc:language>pi</dc:language>
    <dc:identifier id="BookId">urn:uuid:abhidhammatthasangaha-full</dc:identifier>
    <meta property="dcterms:modified">${new Date().toISOString().replace(/\.[0-9]+Z$/, 'Z')}</meta>
  </metadata>
  <manifest>
    <item id="style" href="style.css" media-type="text/css"/>
    <item id="toc-ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="title" href="title.xhtml" media-type="application/xhtml+xml"/>
    <item id="toc" href="toc.xhtml" media-type="application/xhtml+xml"/>
    ${CHAPTER_METAS.map((c) => `<item id="${c.id}" href="${c.id}.xhtml" media-type="application/xhtml+xml"/>`).join('\n    ')}
    <item id="glossary" href="glossary.xhtml" media-type="application/xhtml+xml"/>
  </manifest>
  <spine toc="toc-ncx">
    <itemref idref="title"/>
    <itemref idref="toc"/>
    ${CHAPTER_METAS.map((c) => `<itemref idref="${c.id}"/>`).join('\n    ')}
    <itemref idref="glossary"/>
  </spine>
</package>`;
  zip.file('OEBPS/content.opf', opf);

  const epubBuffer = await zip.generateAsync({ type: 'nodebuffer', mimeType: 'application/epub+zip' });
  const outPath = `${ARTIFACT_DIR}/Abhidhammatthasangaha_Completo.epub`;
  writeFileSync(outPath, epubBuffer);
  console.log(`🎉 EPUB successfully generated and saved: ${outPath} (${(epubBuffer.length / 1024 / 1024).toFixed(2)} MB)`);
  console.log(`📊 Total glossary terms cataloged at end: ${usedGlossary.length}`);
})();

import puppeteer from 'puppeteer';

async function main() {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  
  // Mobile View: 375x667
  await page.setViewport({ width: 375, height: 667 });
  await page.goto('http://localhost:8081/abhidhammatthasaṅgaha/1', { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 2000));

  // Toca em qualquer palavra interativa Pāli (com cursor: pointer)
  const clickedText = await page.evaluate(() => {
    const interactive = Array.from(document.querySelectorAll('*')).filter(el => {
      const style = window.getComputedStyle(el);
      return style.cursor === 'pointer' && el.textContent && el.textContent.trim().length > 2;
    });
    
    // Tenta encontrar uma palavra do corpo do texto
    for (const el of interactive) {
      const txt = el.textContent.trim();
      if (txt === 'Cittaparicchedo' || txt === 'cittam' || txt.includes('citta')) {
        el.click();
        return txt;
      }
    }
    if (interactive.length > 0) {
      interactive[0].click();
      return interactive[0].textContent.trim();
    }
    return null;
  });

  console.log('Clicked element text:', clickedText);
  await new Promise(r => setTimeout(r, 1500));

  await page.screenshot({ path: '/Users/pauloo/.gemini/antigravity/brain/134555de-9249-4384-b949-48418bc73dd8/sangaho_feat_04_mobile_sheet.png' });
  console.log('Mobile sheet screenshot taken!');

  await browser.close();
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});

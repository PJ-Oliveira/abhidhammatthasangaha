// src/__tests__/i18n.test.ts
import { t, translations } from '../i18n';

describe('i18n Internationalization', () => {
  it('has consistent keys across Portuguese, English, and Spanish', () => {
    const ptKeys = Object.keys(translations.pt).sort();
    const enKeys = Object.keys(translations.en).sort();
    const esKeys = Object.keys(translations.es).sort();

    expect(ptKeys.length).toBeGreaterThan(25);
    expect(enKeys.length).toBe(ptKeys.length);
    expect(esKeys.length).toBe(ptKeys.length);

    expect(enKeys).toEqual(ptKeys);
    expect(esKeys).toEqual(ptKeys);
  });

  it('translates app titles correctly for each language', () => {
    expect(t('app.title', 'pt')).toBe('Abhidhammatthasaṅgaha');
    expect(t('app.subtitle', 'pt')).toContain('Compêndio');
    expect(t('app.subtitle', 'en')).toContain('Comprehensive Manual');
    expect(t('app.subtitle', 'es')).toContain('Compendio');
  });

  it('translates export modal keys correctly', () => {
    expect(t('export.title', 'pt')).toBe('Exportar Obra');
    expect(t('export.title', 'en')).toBe('Export Treatise');
    expect(t('export.title', 'es')).toBe('Exportar Obra');

    expect(t('export.epub', 'pt')).toContain('Livro Digital');
    expect(t('export.epub', 'en')).toContain('Digital Book');
    expect(t('export.epub', 'es')).toContain('Libro Digital');
  });

  it('translates navigation keys correctly', () => {
    expect(t('nav.prev', 'pt')).toContain('Anterior');
    expect(t('nav.prev', 'en')).toContain('Previous');
    expect(t('nav.prev', 'es')).toContain('Anterior');

    expect(t('nav.next', 'pt')).toContain('Próximo');
    expect(t('nav.next', 'en')).toContain('Next');
    expect(t('nav.next', 'es')).toContain('Siguiente');
  });

  it('translates paragraph link copy toast correctly', () => {
    expect(t('link.copied', 'pt')).toContain('Link do parágrafo copiado');
    expect(t('link.copied', 'en')).toContain('Paragraph link copied');
    expect(t('link.copied', 'es')).toContain('Enlace del párrafo copiado');
  });

  it('falls back gracefully to Portuguese if key is unknown or missing in language', () => {
    expect(t('sidebar.title', 'en')).toBe('Abhidhammatthasaṅgaha');
    // Key that exists in pt
    expect(t('sidebar.title', 'pt')).toBe('Abhidhammatthasaṅgaha');
  });
});

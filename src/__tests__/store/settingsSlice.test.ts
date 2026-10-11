import settingsReducer, { setFontSize, setTheme, setUiLanguage } from '../../store/slices/settingsSlice';

describe('settingsSlice', () => {
  const initial = { fontSize: 16, theme: 'light' as const, uiLanguage: 'pt' as const };

  it('should return initial state', () => {
    expect(settingsReducer(undefined, { type: 'unknown' })).toEqual(initial);
  });

  it('should handle setFontSize', () => {
    const actual = settingsReducer(initial, setFontSize(24));
    expect(actual.fontSize).toEqual(24);
  });

  it('should handle setTheme', () => {
    const actual = settingsReducer(initial, setTheme('dark'));
    expect(actual.theme).toEqual('dark');
  });

  it('should handle setUiLanguage', () => {
    const actual = settingsReducer(initial, setUiLanguage('en'));
    expect(actual.uiLanguage).toEqual('en');

    const es = settingsReducer(actual, setUiLanguage('es'));
    expect(es.uiLanguage).toEqual('es');
  });
});

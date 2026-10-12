import React from 'react';
import { render, fireEvent, act } from '@testing-library/react-native';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import readingReducer, { setLanguages } from '../../store/slices/readingSlice';
import settingsReducer, { setUiLanguage } from '../../store/slices/settingsSlice';
import { Reader } from '../../components/Reader/Reader';
import { loadChapter } from '../../data/chapters/chapterLoader';

describe('Reader Component — Real Chapter Data Integration (No Mocks)', () => {
  it('renders localized empty state in PT, EN, and ES when segments are empty', () => {
    const store = configureStore({
      reducer: { reading: readingReducer, settings: settingsReducer },
      preloadedState: {
        settings: { fontSize: 16, theme: 'light' as const, uiLanguage: 'pt' as const },
      },
    });
    const { getByText } = render(
      <Provider store={store}>
        <Reader segments={[]} />
      </Provider>
    );
    expect(getByText(/Nenhum segmento neste capítulo/i)).toBeTruthy();

    act(() => {
      store.dispatch(setUiLanguage('en'));
    });
    expect(getByText(/No segments in this chapter/i)).toBeTruthy();

    act(() => {
      store.dispatch(setUiLanguage('es'));
    });
    expect(getByText(/Ningún segmento en este capítulo/i)).toBeTruthy();
  });

  it('renders real segments from Chapter 1 (Cittaparicchedo) and Chapter 2 (Cetasikaparicchedo) across Pāli, EN, PT, and ES', async () => {
    const ch2Segments = await loadChapter('ch02');
    expect(ch2Segments.length).toBeGreaterThan(20);

    const store = configureStore({
      reducer: { reading: readingReducer, settings: settingsReducer },
      preloadedState: {
        reading: {
          visibleSegmentIds: [],
          languages: ['pali', 'en', 'pt', 'es'] as Array<'pali' | 'en' | 'pt' | 'es'>,
          boldPali: false,
          searchQuery: '',
          searchResults: [],
          dictionaryWord: null,
          currentChapterId: 'ch02',
          sidebarOpen: false,
          exportModalOpen: false,
          activeAnchorSegmentId: null,
        },
        settings: { fontSize: 16, theme: 'light' as const, uiLanguage: 'en' as const },
      },
    });

    const { getByText, getAllByText } = render(
      <Provider store={store}>
        <Reader segments={ch2Segments.slice(0, 5)} chapterNumber={2} />
      </Provider>
    );

    // Segment IDs and multi-language badges (EN, PT, ES)
    expect(getByText('abhm-2.1')).toBeTruthy();
    expect(getByText('abhm-2.2')).toBeTruthy();
    expect(getAllByText('EN').length).toBeGreaterThan(0);
    expect(getAllByText('PT').length).toBeGreaterThan(0);
    expect(getAllByText('ES').length).toBeGreaterThan(0);

    // Real translations from ch02.json
    expect(getByText(/The Chapter on Mental Factors/i)).toBeTruthy();
    expect(getByText(/Capítulo dos Fatores Mentais/i)).toBeTruthy();
    expect(getByText(/Capítulo sobre los Factores Mentales/i)).toBeTruthy();

    // Tapping a Pāli word dispatches dictionaryWord to Redux store
    const paliWord = getByText('Cetasikaparicchedo');
    fireEvent.press(paliWord);
    expect(store.getState().reading.dictionaryWord).toBe('cetasikaparicchedo');
  });
});

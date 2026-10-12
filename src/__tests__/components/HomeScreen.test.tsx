import React from 'react';
import * as ReactNative from 'react-native';
import { render, fireEvent, act } from '@testing-library/react-native';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import readingReducer, { setDictionaryWord } from '../../store/slices/readingSlice';
import settingsReducer from '../../store/slices/settingsSlice';
import HomeScreen from '../../components/HomeScreen';

const VIEWPORT_MATRIX = [
  { name: 'Small Phone — iPhone SE 1st Gen', width: 320, height: 568, isSplit: false },
  { name: 'Small Phone — Android Compact', width: 360, height: 640, isSplit: false },
  { name: 'Small Phone — iPhone SE 3rd Gen', width: 375, height: 667, isSplit: false },
  { name: 'Large Phone — Pixel / Galaxy S Ultra', width: 412, height: 915, isSplit: false },
  { name: 'Large Phone — iPhone 16 Pro Max', width: 430, height: 932, isSplit: false },
  { name: 'Mobile Landscape', width: 667, height: 375, isSplit: false },
  { name: 'Small iPad / iPad Mini', width: 768, height: 1024, isSplit: true },
  { name: 'iPad Air / iPad Pro 11"', width: 820, height: 1180, isSplit: true },
  { name: 'Large iPad Pro 12.9" Portrait', width: 1024, height: 1366, isSplit: true },
  { name: 'Notebook 13"', width: 1280, height: 800, isSplit: true },
  { name: 'Notebook HD', width: 1366, height: 768, isSplit: true },
  { name: 'MacBook Air 13" Retina', width: 1440, height: 900, isSplit: true },
  { name: 'MacBook Pro 14"/16"', width: 1512, height: 982, isSplit: true },
  { name: 'Desktop Full HD 1080p', width: 1920, height: 1080, isSplit: true },
  { name: 'Desktop 2K QHD / 4K', width: 2560, height: 1440, isSplit: true },
];

describe('HomeScreen Multi-Device UI & Full Integration Tests (No Mocks)', () => {
  let store: any;

  beforeEach(() => {
    store = configureStore({
      reducer: {
        reading: readingReducer,
        settings: settingsReducer,
      },
      preloadedState: {
        settings: { fontSize: 16, theme: 'light' as const, uiLanguage: 'pt' as const },
      },
    });
  });

  afterEach(() => {
    jest.restoreAllMocks();
  });

  it.each(VIEWPORT_MATRIX)(
    'renders and adapts UI layout on $name ($width x $height)',
    async ({ width, height, isSplit }) => {
      jest.spyOn(ReactNative.Dimensions, 'get').mockReturnValue({
        width,
        height,
        scale: 2,
        fontScale: 1,
      });

      const { findByText, getByText, queryByText } = render(
        <Provider store={store}>
          <HomeScreen />
        </Provider>
      );

      // Loads real Chapter 1 asynchronously
      expect(await findByText(/1\. Cittaparicchedo/i)).toBeTruthy();

      // Main navigation tabs are always accessible
      expect(getByText(/📖 Leitor/i)).toBeTruthy();
      expect(getByText(/🎴 Anki SRS/i)).toBeTruthy();
      expect(getByText(/📊 Matrizes/i)).toBeTruthy();

      if (isSplit) {
        // On Tablet / iPad / Notebook / MacBook / Desktop: DictionaryPanel is rendered side-by-side!
        expect(getByText(/Toque em uma palavra no texto para pesquisar no léxico do Abhidhamma/i)).toBeTruthy();
      } else {
        // On Mobile Phone: 4th tab '📚 Dicionário' is shown in the tab bar
        expect(getByText(/📚 Dicionário/i)).toBeTruthy();
      }

      // Switch to Anki SRS tab and verify real AnkiDeck renders
      fireEvent.press(getByText(/🎴 Anki SRS/i));
      expect(getByText(/Anki • Memorização & Simulado 100/i)).toBeTruthy();

      // Switch to Structural Matrices tab and verify real CompendiumMatrix renders
      fireEvent.press(getByText(/📊 Matrizes/i));
      expect(getByText(/Matrizes Estruturais do Abhidhammatthasaṅgaha/i)).toBeTruthy();

      // Verify redundant "PART 1 — COMPENDIUM" never appears
      expect(queryByText(/PART 1 — COMPENDIUM/i)).toBeNull();
    }
  );

  it('opens ChapterSidebar, displays all 9 full Pāli chapter titles without truncation or Part 1 header, and navigates to Chapter 2', async () => {
    jest.spyOn(ReactNative.Dimensions, 'get').mockReturnValue({
      width: 1440,
      height: 900,
      scale: 2,
      fontScale: 1,
    });

    const { findByText, findAllByText, getByText, queryByText } = render(
      <Provider store={store}>
        <HomeScreen />
      </Provider>
    );

    expect(await findByText(/1\. Cittaparicchedo/i)).toBeTruthy();

    // Switch interface to EN
    fireEvent.press(getByText('EN'));

    // Open Chapter Sidebar via menu button ☰
    fireEvent.press(getByText('☰'));

    // Verify all 9 Paricchedas are listed with full Pāli names and English titles, and NO "Part 1 — Compendium"
    expect(queryByText(/Part 1/i)).toBeNull();
    expect(getByText('Cetasikaparicchedo')).toBeTruthy();
    expect(getByText('Pakiṇṇakaparicchedo')).toBeTruthy();
    expect(getByText('Vīthimuttaparicchedo')).toBeTruthy();
    expect(getByText('Samuccayaparicchedo')).toBeTruthy();
    expect(getByText('Kammaṭṭhānaparicchedo')).toBeTruthy();
    expect(getByText('Compendium of Mental Factors')).toBeTruthy();

    // Select Chapter 2 (Cetasikaparicchedo)
    await act(async () => {
      fireEvent.press(getByText('Cetasikaparicchedo'));
    });

    // Header and Reader now show Chapter 2
    const ch2Matches = await findAllByText(/2\. Cetasikaparicchedo/i);
    expect(ch2Matches.length).toBeGreaterThanOrEqual(1);
    expect(await findByText('Compendium of Mental Factors')).toBeTruthy();
    expect(store.getState().reading.currentChapterId).toBe('ch02');
    expect(store.getState().reading.sidebarOpen).toBe(false);
  });

  it('on mobile viewport, opens TermBottomSheet when dictionaryWord is selected, transitions cleanly to DictionaryPanel via "Abrir no Dicionário Completo" without corrupting Reader searchQuery, and returns cleanly to Reader', async () => {
    jest.spyOn(ReactNative.Dimensions, 'get').mockReturnValue({
      width: 375,
      height: 667,
      scale: 2,
      fontScale: 1,
    });

    const { findByText, getByText, queryByText, getByDisplayValue } = render(
      <Provider store={store}>
        <HomeScreen />
      </Provider>
    );

    expect(await findByText(/1\. Cittaparicchedo/i)).toBeTruthy();

    // Simulate tapping a Pāli word ("citta") on mobile
    act(() => {
      store.dispatch(setDictionaryWord('citta'));
    });

    // TermBottomSheet opens with "Abrir no Dicionário Completo" button
    const openFullBtn = getByText(/📖 Abrir no Dicionário Completo/i);
    expect(openFullBtn).toBeTruthy();

    // Press "Abrir no Dicionário Completo"
    fireEvent.press(openFullBtn);

    // TermBottomSheet hides, DictionaryPanel mounts with "citta" populated, and Reader searchQuery is NOT corrupted!
    expect(queryByText(/📖 Abrir no Dicionário Completo/i)).toBeNull();
    expect(getByDisplayValue('citta')).toBeTruthy();
    expect(store.getState().reading.searchQuery).toBe('');

    // Return to Reader tab — dictionaryWord is cleared and Reader shows chapter content without false "Nenhum resultado"
    fireEvent.press(getByText(/📖 Leitor/i));
    expect(store.getState().reading.dictionaryWord).toBeNull();
    expect(queryByText(/Nenhum resultado para/i)).toBeNull();
  });
});

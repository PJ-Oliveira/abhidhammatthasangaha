import React from 'react';
import { render, fireEvent, act } from '@testing-library/react-native';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import readingReducer, { setDictionaryWord } from '../../store/slices/readingSlice';
import settingsReducer, { setUiLanguage } from '../../store/slices/settingsSlice';
import { DictionaryPanel } from '../../components/Dictionary/DictionaryPanel';
import { lookupWord } from '../../services/dictionaryService';

describe('DictionaryPanel Component — Real Offline Pāli Lexicon Integration (No Mocks)', () => {
  it('renders quick-lookup terms and looks up real Pāli entries when clicked', () => {
    const store = configureStore({
      reducer: { reading: readingReducer, settings: settingsReducer },
      preloadedState: {
        settings: { fontSize: 16, theme: 'light' as const, uiLanguage: 'pt' as const },
      },
    });
    const { getByText, getAllByText } = render(
      <Provider store={store}>
        <DictionaryPanel />
      </Provider>
    );

    // Quick lookup pill 'citta'
    const cittaPill = getAllByText('citta')[0];
    fireEvent.press(cittaPill);

    const realEntry = lookupWord('citta');
    expect(realEntry).toBeDefined();
    expect(getByText(realEntry!.meaning.pt)).toBeTruthy();

    // Switch UI language to EN -> definition dynamically switches to English!
    act(() => {
      store.dispatch(setUiLanguage('en'));
    });
    expect(getByText(realEntry!.meaning.en)).toBeTruthy();

    // Switch UI language to ES -> definition dynamically switches to Spanish!
    act(() => {
      store.dispatch(setUiLanguage('es'));
    });
    expect(getByText(realEntry!.meaning.es)).toBeTruthy();
  });

  it('automatically looks up a word when dictionaryWord is dispatched from the Reader', () => {
    const store = configureStore({
      reducer: { reading: readingReducer, settings: settingsReducer },
      preloadedState: {
        settings: { fontSize: 16, theme: 'light' as const, uiLanguage: 'en' as const },
      },
    });
    const { getByText } = render(
      <Provider store={store}>
        <DictionaryPanel />
      </Provider>
    );

    act(() => {
      store.dispatch(setDictionaryWord('nibbāna'));
    });

    const nibbanaEntry = lookupWord('nibbāna');
    expect(nibbanaEntry).toBeDefined();
    expect(getByText(nibbanaEntry!.meaning.en)).toBeTruthy();
  });

  it('renders Samāsa decomposition, Viggaha, Lakkhaṇādi-catukka, and CMA references in the selected UI language', () => {
    const store = configureStore({
      reducer: { reading: readingReducer, settings: settingsReducer },
      preloadedState: {
        settings: { fontSize: 16, theme: 'light' as const, uiLanguage: 'pt' as const },
      },
    });
    const { getAllByText } = render(
      <Provider store={store}>
        <DictionaryPanel />
      </Provider>
    );

    act(() => {
      store.dispatch(setDictionaryWord('somanassasahagata'));
    });

    // Verifies Samāsa pedagogical breakdown and Viggaha in Portuguese
    expect(getAllByText(/Decomposição Pedagógica de Composto/i).length).toBeGreaterThan(0);
    expect(getAllByText(/somanassena saha gataṃ/i).length).toBeGreaterThan(0);
    expect(getAllByText(/Referência CMA/i).length).toBeGreaterThan(0);

    // Verifies 4-fold Lakkhaṇādi-catukka on Paramattha Dhamma 'phassa'
    act(() => {
      store.dispatch(setDictionaryWord('phassa'));
    });
    expect(getAllByText(/1\. Lakkhaṇa/i).length).toBeGreaterThan(0);
    expect(getAllByText(/2\. Rasa/i).length).toBeGreaterThan(0);
    expect(getAllByText(/3\. Paccupaṭṭhāna/i).length).toBeGreaterThan(0);
    expect(getAllByText(/4\. Padaṭṭhāna/i).length).toBeGreaterThan(0);
  });
});


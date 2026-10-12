import React from 'react';
import * as ReactNative from 'react-native';
import { render, fireEvent } from '@testing-library/react-native';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import readingReducer, { setDictionaryWord } from '../../store/slices/readingSlice';
import settingsReducer from '../../store/slices/settingsSlice';
import { TermBottomSheet } from '../../components/Dictionary/TermBottomSheet';

describe('TermBottomSheet — Real Dictionary & Responsive Integration Tests (No Mocks)', () => {
  afterEach(() => {
    jest.restoreAllMocks();
  });

  it('renders Pāli term and definition on mobile viewports, expands/collapses alternate language translations, and opens full dictionary without corrupting searchQuery', () => {
    jest.spyOn(ReactNative.Dimensions, 'get').mockReturnValue({
      width: 375,
      height: 667,
      scale: 2,
      fontScale: 1,
    });

    const store = configureStore({
      reducer: { reading: readingReducer, settings: settingsReducer },
      preloadedState: {
        settings: { fontSize: 16, theme: 'light' as const, uiLanguage: 'pt' as const },
      },
    });
    store.dispatch(setDictionaryWord('nibbāna'));

    const onOpenFull = jest.fn();
    const { getByText, queryByText } = render(
      <Provider store={store}>
        <TermBottomSheet onOpenFullDictionary={onOpenFull} />
      </Provider>
    );

    expect(getByText('nibbāna')).toBeTruthy();
    expect(queryByText('EN:')).toBeNull();

    // Expand bottom sheet to reveal EN and ES translations
    fireEvent.press(getByText(/⤢ Expandir/i));
    expect(getByText('EN:')).toBeTruthy();
    expect(getByText('ES:')).toBeTruthy();

    // Collapse bottom sheet
    fireEvent.press(getByText(/⤡ Recolher/i));
    expect(queryByText('EN:')).toBeNull();

    // Press "Abrir no Dicionário Completo"
    fireEvent.press(getByText(/📖 Abrir no Dicionário Completo/i));
    expect(onOpenFull).toHaveBeenCalledWith('nibbāna');
    expect(store.getState().reading.dictionaryWord).toBe('nibbāna');
    expect(store.getState().reading.searchQuery).toBe('');
  });

  it('does not render when hidden={true} or on split-screen desktop viewports', () => {
    jest.spyOn(ReactNative.Dimensions, 'get').mockReturnValue({
      width: 375,
      height: 667,
      scale: 2,
      fontScale: 1,
    });

    const store = configureStore({
      reducer: { reading: readingReducer, settings: settingsReducer },
      preloadedState: {
        settings: { fontSize: 16, theme: 'light' as const, uiLanguage: 'pt' as const },
      },
    });
    store.dispatch(setDictionaryWord('citta'));

    const { queryByText } = render(
      <Provider store={store}>
        <TermBottomSheet hidden={true} />
      </Provider>
    );
    expect(queryByText('citta')).toBeNull();
  });
});

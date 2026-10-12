import React from 'react';
import { render, fireEvent, act } from '@testing-library/react-native';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import readingReducer, { setCurrentChapter } from '../../store/slices/readingSlice';
import settingsReducer from '../../store/slices/settingsSlice';
import { SearchBar } from '../../components/SearchBar/SearchBar';
import { buildSearchIndex } from '../../services/textSearch';

describe('SearchBar Component — Real Corpus Integration (No Mocks)', () => {
  beforeAll(async () => {
    await buildSearchIndex();
  }, 15000);

  it(
    'updates input, executes real search over the 9 chapters, and clears results when pressing Clear',
    async () => {
      const store = configureStore({
        reducer: { reading: readingReducer, settings: settingsReducer },
        preloadedState: {
          settings: { fontSize: 16, theme: 'light' as const, uiLanguage: 'pt' as const },
        },
      });
      const { getByPlaceholderText, getByRole } = render(
        <Provider store={store}>
          <SearchBar />
        </Provider>
      );

      const input = getByPlaceholderText(/Pesquisar em Pāli, Português, Inglês, Espanhol/i);
      fireEvent.changeText(input, 'Cetasikaparicchedo');

      const btn = getByRole('button', { name: 'Search' });
      await act(async () => {
        fireEvent.press(btn);
      });

      const stateAfterSearch = store.getState().reading;
      expect(stateAfterSearch.searchQuery).toBe('Cetasikaparicchedo');
      expect(stateAfterSearch.searchResults).toContain('abhm-2.1');

      // Clear button appears and resets search state
      const clearBtn = getByRole('button', { name: 'Clear' });
      await act(async () => {
        fireEvent.press(clearBtn);
      });
      expect(store.getState().reading.searchQuery).toBe('');
      expect(store.getState().reading.searchResults).toEqual([]);
    },
    15000
  );

  it(
    'syncs input value with Redux searchQuery when remounted or when chapter changes',
    async () => {
      const store = configureStore({
        reducer: { reading: readingReducer, settings: settingsReducer },
        preloadedState: {
          settings: { fontSize: 16, theme: 'light' as const, uiLanguage: 'pt' as const },
        },
      });
      const { getByPlaceholderText, getByRole, unmount } = render(
        <Provider store={store}>
          <SearchBar />
        </Provider>
      );

      const input = getByPlaceholderText(/Pesquisar em Pāli, Português, Inglês, Espanhol/i);
      fireEvent.changeText(input, 'Nibbāna');
      await act(async () => {
        fireEvent.press(getByRole('button', { name: 'Search' }));
      });
      expect(store.getState().reading.searchQuery).toBe('Nibbāna');

      // Simulate switching away from Reader tab (unmount) and returning (remount)
      unmount();
      const remounted = render(
        <Provider store={store}>
          <SearchBar />
        </Provider>
      );
      expect(remounted.getByDisplayValue('Nibbāna')).toBeTruthy();

      // Simulate changing chapters -> setCurrentChapter resets Redux searchQuery to ''
      act(() => {
        store.dispatch(setCurrentChapter('ch02'));
      });
      expect(remounted.queryByDisplayValue('Nibbāna')).toBeNull();
    },
    15000
  );
});

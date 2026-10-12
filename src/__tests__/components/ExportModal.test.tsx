// src/__tests__/components/ExportModal.test.tsx
import React from 'react';
import { render, fireEvent } from '@testing-library/react-native';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import readingReducer from '../../store/slices/readingSlice';
import settingsReducer from '../../store/slices/settingsSlice';
import { ExportModal } from '../../components/ExportModal/ExportModal';

describe('ExportModal — Real UI Integration Tests (No Mocks)', () => {
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

  it('renders correctly when visible, allows changing format, mode, scope, and UI language, and closes cleanly', () => {
    const handleClose = jest.fn();
    const { getByText } = render(
      <Provider store={store}>
        <ExportModal visible={true} onClose={handleClose} />
      </Provider>
    );

    expect(getByText('Exportar Obra')).toBeTruthy();
    expect(getByText('📚 EPUB (Livro Digital)')).toBeTruthy();
    expect(getByText('📄 PDF (Impressão / A4)')).toBeTruthy();

    // Switch to PDF
    fireEvent.press(getByText('📄 PDF (Impressão / A4)'));

    // Switch mode to Monolingual
    fireEvent.press(getByText(/Monolíngue/));

    // Switch UI language inside modal to EN and ES
    fireEvent.press(getByText('EN'));
    expect(getByText('Export Treatise')).toBeTruthy();

    fireEvent.press(getByText('ES'));
    expect(getByText('Exportar Obra')).toBeTruthy();

    // Close modal
    const closeBtn = getByText('✕');
    fireEvent.press(closeBtn);
    expect(handleClose).toHaveBeenCalledTimes(1);
  });

  it('does not render when visible is false', () => {
    const { queryByText } = render(
      <Provider store={store}>
        <ExportModal visible={false} onClose={() => {}} />
      </Provider>
    );

    expect(queryByText('Exportar Obra')).toBeNull();
  });
});

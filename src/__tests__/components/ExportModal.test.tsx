// src/__tests__/components/ExportModal.test.tsx
import React from 'react';
import { render, fireEvent } from '@testing-library/react-native';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import readingReducer from '../../store/slices/readingSlice';
import settingsReducer from '../../store/slices/settingsSlice';
import { ExportModal } from '../../components/ExportModal/ExportModal';

jest.mock('../../services/exportService', () => ({
  exportToEpub: jest.fn().mockImplementation((_cfg, cb) => {
    cb?.(100, 'Concluído');
    return Promise.resolve();
  }),
  exportToPdf: jest.fn().mockImplementation((_cfg, cb) => {
    cb?.(100, 'Concluído');
    return Promise.resolve();
  }),
}));

describe('ExportModal', () => {
  let store: any;

  beforeEach(() => {
    store = configureStore({
      reducer: {
        reading: readingReducer,
        settings: settingsReducer,
      },
    });
  });

  it('renders correctly when visible and allows changing format and mode', () => {
    const handleClose = jest.fn();
    const { getByText } = render(
      <Provider store={store}>
        <ExportModal visible={true} onClose={handleClose} />
      </Provider>
    );

    expect(getByText('Exportar Obra')).toBeTruthy();
    expect(getByText('📚 EPUB (Livro Digital)')).toBeTruthy();
    expect(getByText('📄 PDF (Impressão / A4)')).toBeTruthy();

    // Alterna para PDF
    const pdfBtn = getByText('📄 PDF (Impressão / A4)');
    fireEvent.press(pdfBtn);

    // Alterna modo para monolíngue
    const monoBtn = getByText(/Monolíngue/);
    fireEvent.press(monoBtn);

    // Fecha o modal
    const closeBtn = getByText('✕');
    fireEvent.press(closeBtn);
    expect(handleClose).toHaveBeenCalledTimes(1);
  });

  it('does not render when visible is false', () => {
    const { queryByText } = render(
      <Provider store={store}>
        <ExportModal visible={false} onClose={jest.fn()} />
      </Provider>
    );

    expect(queryByText('Exportar Obra')).toBeNull();
  });
});

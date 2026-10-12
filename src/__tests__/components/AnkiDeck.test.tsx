// src/__tests__/components/AnkiDeck.test.tsx
import React from 'react';
import { render, fireEvent } from '@testing-library/react-native';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import readingReducer from '../../store/slices/readingSlice';
import settingsReducer from '../../store/slices/settingsSlice';
import { AnkiDeck } from '../../components/AnkiDeck/AnkiDeck';

describe('AnkiDeck Component Integration Tests', () => {
  let store: any;

  beforeEach(() => {
    if (typeof window !== 'undefined' && window.localStorage) {
      window.localStorage.clear();
    }
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

  it('renders AnkiDeck initially in study mode with progress, chapter filters, and category filters', () => {
    const { getByText } = render(
      <Provider store={store}>
        <AnkiDeck />
      </Provider>
    );

    // Header title and study tabs
    expect(getByText(/Anki • Memorização & Simulado 100/i)).toBeTruthy();
    expect(getByText(/🎴 Estudo SRS/i)).toBeTruthy();
    expect(getByText(/💯 Simulado Prova 100/i)).toBeTruthy();
    expect(getByText(/🔍 Navegador de Cards/i)).toBeTruthy();
    expect(getByText(/📥 Exportar Anki/i)).toBeTruthy();

    // Category filter chips
    expect(getByText(/Todas as Categorias/i)).toBeTruthy();
    expect(getByText(/🔢 Quantidades/i)).toBeTruthy();
    expect(getByText(/⚠️ Pegadinhas de Prova/i)).toBeTruthy();

    // First card front content
    expect(getByText(/Mostrar Resposta \(Espaço\)/i)).toBeTruthy();
  });

  it('flips card to reveal answer, breakdown and rating buttons, advances on rating, and shows reset cache button', () => {
    const { getByText } = render(
      <Provider store={store}>
        <AnkiDeck />
      </Provider>
    );

    expect(getByText(/Card 1 de 63/i)).toBeTruthy();

    const flipBtn = getByText(/Mostrar Resposta \(Espaço\)/i);
    fireEvent.press(flipBtn);

    // Rating buttons appear
    expect(getByText(/Repetir \(1\)/i)).toBeTruthy();
    expect(getByText(/Difícil \(2\)/i)).toBeTruthy();
    const easyBtn = getByText(/Fácil \(4\)/i);
    expect(easyBtn).toBeTruthy();

    // Rate card Easy -> marks as mastered and advances to Card 2
    fireEvent.press(easyBtn);
    expect(getByText(/Card 2 de 63/i)).toBeTruthy();

    // Reset cache button appears after rating
    const resetBtn = getByText(/↺ Zerar Progresso/i);
    expect(resetBtn).toBeTruthy();
    fireEvent.press(resetBtn);
    expect(getByText(/Card 1 de 63/i)).toBeTruthy();
  });

  it('switches to exam mode, starts a practice exam, and dynamically translates options when switching languages mid-exam', () => {
    const { getByText, queryByText } = render(
      <Provider store={store}>
        <AnkiDeck />
      </Provider>
    );

    const examTab = getByText(/💯 Simulado Prova 100/i);
    fireEvent.press(examTab);

    // Exam start button
    const startBtn = getByText(/📝 10 Questões Rápidas/i);
    expect(startBtn).toBeTruthy();
    fireEvent.press(startBtn);

    // Now in exam mode with questions in PT
    expect(getByText(/Questão 1 de 10/i)).toBeTruthy();
    expect(getByText(/Simulado em Andamento:/i)).toBeTruthy();

    // Switch language to EN mid-exam!
    fireEvent.press(getByText('EN'));
    expect(getByText(/Question 1 of 10/i)).toBeTruthy();
    expect(getByText(/Exam in Progress:/i)).toBeTruthy();
    expect(queryByText(/Simulado em Andamento:/i)).toBeNull();

    // Switch language to ES mid-exam!
    fireEvent.press(getByText('ES'));
    expect(getByText(/Pregunta 1 de 10/i)).toBeTruthy();
    expect(getByText(/Examen en Curso:/i)).toBeTruthy();
  });

  it('allows filtering by category and jumping from Browser mode to Study mode', () => {
    const { getByText, getAllByText } = render(
      <Provider store={store}>
        <AnkiDeck />
      </Provider>
    );

    // Switch to Browser mode
    fireEvent.press(getByText(/🔍 Navegador de Cards/i));
    expect(getByText(/63 cards encontrados/i)).toBeTruthy();

    // Filter by Exam Traps
    fireEvent.press(getByText(/⚠️ Pegadinhas de Prova/i));

    // Click the first card in browser to jump to Study mode
    const studyBadges = getAllByText(/🎴 Estudar Card/i);
    expect(studyBadges.length).toBeGreaterThan(0);
    fireEvent.press(studyBadges[0]);

    // Back in Study mode showing the filtered deck
    expect(getByText(/Mostrar Resposta \(Espaço\)/i)).toBeTruthy();
  });

  it('switches language to English and Spanish and localizes all study UI elements', () => {
    const { getByText, queryByText } = render(
      <Provider store={store}>
        <AnkiDeck />
      </Provider>
    );

    fireEvent.press(getByText('EN'));
    expect(getByText(/🎴 SRS Study/i)).toBeTruthy();
    expect(getByText(/💯 100-Score Exam/i)).toBeTruthy();
    expect(getByText(/◀ Previous/i)).toBeTruthy();
    expect(getByText(/Next ▶/i)).toBeTruthy();
    expect(queryByText(/◀ Anterior/i)).toBeNull();

    fireEvent.press(getByText('ES'));
    expect(getByText(/🎴 Estudio SRS/i)).toBeTruthy();
    expect(getByText(/Siguiente ▶/i)).toBeTruthy();
  });
});

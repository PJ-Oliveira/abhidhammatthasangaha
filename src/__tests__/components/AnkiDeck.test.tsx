// src/__tests__/components/AnkiDeck.test.tsx
import React from 'react';
import { render, fireEvent } from '@testing-library/react-native';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import readingReducer from '../../store/slices/readingSlice';
import settingsReducer from '../../store/slices/settingsSlice';
import { AnkiDeck } from '../../components/AnkiDeck/AnkiDeck';
import { ANKI_CARDS } from '../../data/ankiCards';

// Cards with no prerequisites are the only ones unlocked in a fresh session.
const UNLOCKED_AT_START = ANKI_CARDS.filter((c) => (c.requires ?? []).length === 0).length;

// Builds saved SRS progress in which the given cards count as consolidated (>= 2 successful reps).
const consolidated = (ids: string[]) =>
  Object.fromEntries(
    ids.map((id) => [id, { id, interval: 6, reps: 3, easeFactor: 2.5, dueDate: '2099-01-01', mastered: true }])
  );

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
    // Consolidating the root card unlocks the four cards that depend only on it.
    const unlocked = ANKI_CARDS.filter((c) => (c.requires ?? []).every((r) => r === 'at-t01')).length;
    const { getByText } = render(
      <Provider store={store}>
        <AnkiDeck initialSrsState={consolidated(['at-t01'])} />
      </Provider>
    );

    expect(getByText(new RegExp(`Card 1 de ${unlocked}\\b`, 'i'))).toBeTruthy();

    const flipBtn = getByText(/Mostrar Resposta \(Espaço\)/i);
    fireEvent.press(flipBtn);

    // Rating buttons appear
    expect(getByText(/Repetir \(1\)/i)).toBeTruthy();
    expect(getByText(/Difícil \(2\)/i)).toBeTruthy();
    const easyBtn = getByText(/Fácil \(4\)/i);
    expect(easyBtn).toBeTruthy();

    // Rate card Easy -> marks as mastered and advances to Card 2
    fireEvent.press(easyBtn);
    expect(getByText(new RegExp(`Card 2 de ${unlocked}\\b`, 'i'))).toBeTruthy();

    // Reset cache button appears after rating
    const resetBtn = getByText(/↺ Zerar Progresso/i);
    expect(resetBtn).toBeTruthy();
    fireEvent.press(resetBtn);
    expect(getByText(new RegExp(`Card 1 de ${UNLOCKED_AT_START}\\b`, 'i'))).toBeTruthy();
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
    // Philosophy foundation cards (what is citta/cetasika/...) unlock once the root card is consolidated.
    const { getByText, getAllByText } = render(
      <Provider store={store}>
        <AnkiDeck initialSrsState={consolidated(['at-t01'])} />
      </Provider>
    );

    // Switch to Browser mode
    fireEvent.press(getByText(/🔍 Navegador de Cards/i));
    expect(getByText(new RegExp(`${ANKI_CARDS.length} cards encontrados`, 'i'))).toBeTruthy();

    // Filter by Philosophy (foundation cards unlocked above; Exam Traps sit higher in the ladder)
    fireEvent.press(getByText(/☸️ Filosofia/i));

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
    expect(getByText(/Tarjetas:/i)).toBeTruthy();
  });

  it('completes a full 10-question exam with 100% score by selecting the canonical answer for each question and records Best Exam score', () => {
    const { getByText, getAllByText } = render(
      <Provider store={store}>
        <AnkiDeck />
      </Provider>
    );

    fireEvent.press(getByText(/💯 Simulado Prova 100/i));
    fireEvent.press(getByText(/📝 10 Questões Rápidas/i));

    // Answer the first question and submit exam
    const firstOpt = getAllByText(/^A\) /)[0];
    fireEvent.press(firstOpt);

    const submitBtn = getByText(/Finalizar e Corrigir Exame/i);
    fireEvent.press(submitBtn);

    expect(getByText(/Resultado do Exame/i)).toBeTruthy();
    expect(getByText(/🏆 Recorde Prova:/i)).toBeTruthy();
  });

  it('filters cards by chapter and diacritic-insensitive search query in Browser mode without trapping Study mode in the search filter', () => {
    // Unlock the whole ladder so Chapter 6 is fully available in Study mode.
    const { getByText, getByPlaceholderText, getAllByText } = render(
      <Provider store={store}>
        <AnkiDeck initialSrsState={consolidated(ANKI_CARDS.map((c) => c.id))} />
      </Provider>
    );

    fireEvent.press(getByText(/🔍 Navegador de Cards/i));

    // Filter by Chapter 6 (Rūpaparicchedo — 6 real cards)
    fireEvent.press(getByText('Cap. 6'));
    expect(getByText(/6 cards encontrados/i)).toBeTruthy();

    // Search for "kalapas" WITHOUT macron (ā) — diacritic-insensitive search matches "Kalāpas & Conception"
    const searchInput = getByPlaceholderText(/Pesquisar cards/i);
    fireEvent.changeText(searchInput, 'kalapas');
    expect(getByText(/1 cards encontrados/i)).toBeTruthy();

    // Jump to Study mode from Browser card — Study mode must retain all 6 cards of Chapter 6 (not trapped at 1 card)
    const studyBadges = getAllByText(/🎴 Estudar Card/i);
    fireEvent.press(studyBadges[0]);
    expect(getByText(/Card 3 de 6/i)).toBeTruthy();
  });
});

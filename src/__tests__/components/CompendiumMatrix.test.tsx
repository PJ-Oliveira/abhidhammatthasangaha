// src/__tests__/components/CompendiumMatrix.test.tsx
import React from 'react';
import { render, fireEvent } from '@testing-library/react-native';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import settingsReducer from '../../store/slices/settingsSlice';
import { CompendiumMatrix } from '../../components/Matrix/CompendiumMatrix';

describe('CompendiumMatrix Component Integration Tests', () => {
  let store: any;

  beforeEach(() => {
    store = configureStore({
      reducer: {
        settings: settingsReducer,
      },
      preloadedState: {
        settings: { fontSize: 16, theme: 'light' as const, uiLanguage: 'pt' as const },
      },
    });
  });

  it('renders CompendiumMatrix with structural tables and tabs in Portuguese', () => {
    const { getByText } = render(
      <Provider store={store}>
        <CompendiumMatrix />
      </Provider>
    );

    expect(getByText(/Matrizes Estruturais do Abhidhammatthasaṅgaha/i)).toBeTruthy();
    expect(getByText(/Consciência \(89 \/ 121\)/i)).toBeTruthy();
    expect(getByText(/Fatores Mentais \(52\)/i)).toBeTruthy();
    expect(getByText(/Matéria \(28\)/i)).toBeTruthy();
    expect(getByText(/14 Funções Mentais/i)).toBeTruthy();
    expect(getByText(/24 Condições \(Paccayas\)/i)).toBeTruthy();
  });

  it('switches to 24 Paccayas tab and renders conditional relations', () => {
    const { getByText } = render(
      <Provider store={store}>
        <CompendiumMatrix />
      </Provider>
    );

    const paccayaTab = getByText(/24 Condições \(Paccayas\)/i);
    fireEvent.press(paccayaTab);

    expect(getByText(/1\. Hetu-paccaya/i)).toBeTruthy();
    expect(getByText(/Condição de Raiz/i)).toBeTruthy();
  });

  it('translates all matrix tabs and body content when switching to English and Spanish', () => {
    const { getByText } = render(
      <Provider store={store}>
        <CompendiumMatrix />
      </Provider>
    );

    // Switch to English
    fireEvent.press(getByText('EN'));
    expect(getByText(/Structural Matrices of Abhidhammatthasaṅgaha/i)).toBeTruthy();
    expect(getByText(/Unwholesome consciousnesses rooted in greed, hatred, and delusion/i)).toBeTruthy();

    // Check Paccaya tab in English
    fireEvent.press(getByText(/24 Conditions \(Paccayas\)/i));
    expect(getByText(/Root Condition/i)).toBeTruthy();

    // Switch to Spanish
    fireEvent.press(getByText('ES'));
    expect(getByText(/Matrices Estructurales del Abhidhammatthasaṅgaha/i)).toBeTruthy();
    expect(getByText(/Condición de Raíz/i)).toBeTruthy();
  });

  it('verifies canonical 55 Javana breakdown (10 rūpa + 8 arūpa) and Phoṭṭhabba orthography across PT, EN, and ES', () => {
    const { getByText, queryByText } = render(
      <Provider store={store}>
        <CompendiumMatrix />
      </Provider>
    );

    // Check Rūpa (28) tab in PT
    fireEvent.press(getByText(/Matéria \(28\)/i));
    expect(getByText(/Phoṭṭhabba = 3 elementos: terra, fogo, ar/i)).toBeTruthy();
    expect(queryByText(/Photṭhabba/i)).toBeNull();

    // Check 14 Mental Functions (Kicca) tab in PT
    fireEvent.press(getByText(/14 Funções Mentais/i));
    expect(getByText(/12 akusala \+ 1 hasituppāda \+ 8 mahākusala \+ 8 mahākiriya \+ 10 rūpa \+ 8 arūpa \+ 8\/40 lokuttara/i)).toBeTruthy();
    expect(queryByText(/9 rūpa \+ 9 arūpa/i)).toBeNull();

    // Switch to EN and verify both Kicca and Rūpa
    fireEvent.press(getByText('EN'));
    expect(getByText(/12 akusala \+ 1 hasituppāda \+ 8 mahākusala \+ 8 mahākiriya \+ 10 rūpa \+ 8 arūpa \+ 8\/40 lokuttara/i)).toBeTruthy();
    fireEvent.press(getByText(/Matter \(28\)/i));
    expect(getByText(/Phoṭṭhabba = 3 essentials: earth, fire, air/i)).toBeTruthy();

    // Switch to ES and verify both Rūpa and Kicca
    fireEvent.press(getByText('ES'));
    expect(getByText(/Phoṭṭhabba = 3 elementos: tierra, fuego, aire/i)).toBeTruthy();
    fireEvent.press(getByText(/14 Funciones Mentales/i));
    expect(getByText(/12 akusala \+ 1 hasituppāda \+ 8 mahākusala \+ 8 mahākiriya \+ 10 rūpa \+ 8 arūpa \+ 8\/40 lokuttara/i)).toBeTruthy();
  });
});

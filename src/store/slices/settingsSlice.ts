import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { Platform } from 'react-native';
import { SettingsState, UiLanguage } from '../../types/models';

const SETTINGS_STORAGE_KEY = 'abhidhamma_settings_v1';

const loadSavedSettings = (): SettingsState => {
  const defaults: SettingsState = {
    fontSize: 16,
    theme: 'light',
    uiLanguage: 'pt',
  };
  if (Platform.OS === 'web' && typeof window !== 'undefined' && window.localStorage) {
    try {
      const raw = window.localStorage.getItem(SETTINGS_STORAGE_KEY);
      if (raw) {
        const parsed = JSON.parse(raw);
        return {
          fontSize: typeof parsed.fontSize === 'number' ? parsed.fontSize : defaults.fontSize,
          theme: parsed.theme === 'dark' || parsed.theme === 'light' ? parsed.theme : defaults.theme,
          uiLanguage: parsed.uiLanguage === 'pt' || parsed.uiLanguage === 'en' || parsed.uiLanguage === 'es' ? parsed.uiLanguage : defaults.uiLanguage,
        };
      }
    } catch {
      // ignore storage errors
    }
  }
  return defaults;
};

const saveSettings = (state: SettingsState) => {
  if (Platform.OS === 'web' && typeof window !== 'undefined' && window.localStorage) {
    try {
      window.localStorage.setItem(SETTINGS_STORAGE_KEY, JSON.stringify(state));
    } catch {
      // ignore storage errors
    }
  }
};

const initialState: SettingsState = loadSavedSettings();

const settingsSlice = createSlice({
  name: 'settings',
  initialState,
  reducers: {
    setFontSize(state, action: PayloadAction<number>) {
      state.fontSize = action.payload;
      saveSettings(state);
    },
    setTheme(state, action: PayloadAction<'light' | 'dark'>) {
      state.theme = action.payload;
      saveSettings(state);
    },
    setUiLanguage(state, action: PayloadAction<UiLanguage>) {
      state.uiLanguage = action.payload;
      saveSettings(state);
    },
  },
});

export const { setFontSize, setTheme, setUiLanguage } = settingsSlice.actions;
export default settingsSlice.reducer;

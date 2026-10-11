import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { SettingsState, UiLanguage } from '../../types/models';

const initialState: SettingsState = {
  fontSize: 16,
  theme: 'light',
  uiLanguage: 'pt',
};

const settingsSlice = createSlice({
  name: 'settings',
  initialState,
  reducers: {
    setFontSize(state, action: PayloadAction<number>) {
      state.fontSize = action.payload;
    },
    setTheme(state, action: PayloadAction<'light' | 'dark'>) {
      state.theme = action.payload;
    },
    setUiLanguage(state, action: PayloadAction<UiLanguage>) {
      state.uiLanguage = action.payload;
    },
  },
});

export const { setFontSize, setTheme, setUiLanguage } = settingsSlice.actions;
export default settingsSlice.reducer;

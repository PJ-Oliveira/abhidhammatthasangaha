// src/store/slices/readingSlice.ts
import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { Language, ReadingState } from '../../types/models';

const initialState: ReadingState = {
  visibleSegmentIds: [],
  languages: ['pali', 'en'],
  boldPali: false,
  searchQuery: '',
  searchResults: [],
  dictionaryWord: null,
  currentChapterId: 'ch01',
  sidebarOpen: false,
  exportModalOpen: false,
  activeAnchorSegmentId: null,
};

const readingSlice = createSlice({
  name: 'reading',
  initialState,
  reducers: {
    setVisibleSegments(state, action: PayloadAction<string[]>) {
      state.visibleSegmentIds = action.payload;
    },
    setLanguages(state, action: PayloadAction<Language[]>) {
      if (action.payload && action.payload.length > 0) {
        state.languages = action.payload;
      }
    },
    toggleBoldPali(state) {
      state.boldPali = !state.boldPali;
    },
    setSearchQuery(state, action: PayloadAction<string>) {
      state.searchQuery = action.payload;
    },
    setSearchResults(state, action: PayloadAction<string[]>) {
      state.searchResults = action.payload;
    },
    setDictionaryWord(state, action: PayloadAction<string | null>) {
      state.dictionaryWord = action.payload;
    },
    setCurrentChapter(state, action: PayloadAction<string>) {
      state.currentChapterId = action.payload;
      state.searchQuery = '';
      state.searchResults = [];
    },
    toggleSidebar(state) {
      state.sidebarOpen = !state.sidebarOpen;
    },
    setSidebarOpen(state, action: PayloadAction<boolean>) {
      state.sidebarOpen = action.payload;
    },
    setExportModalOpen(state, action: PayloadAction<boolean>) {
      state.exportModalOpen = action.payload;
    },
    setActiveAnchorSegmentId(state, action: PayloadAction<string | null>) {
      state.activeAnchorSegmentId = action.payload;
    },
  },
});

export const {
  setVisibleSegments,
  setLanguages,
  toggleBoldPali,
  setSearchQuery,
  setSearchResults,
  setDictionaryWord,
  setCurrentChapter,
  toggleSidebar,
  setSidebarOpen,
  setExportModalOpen,
  setActiveAnchorSegmentId,
} = readingSlice.actions;
export default readingSlice.reducer;

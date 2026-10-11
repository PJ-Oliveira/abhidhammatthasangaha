// src/types/models.ts
export type Language = 'pali' | 'en' | 'pt' | 'es';
export type UiLanguage = 'pt' | 'en' | 'es';

export interface Segment {
  id: string;
  pali: string;
  translations: Partial<Record<Exclude<Language, 'pali'>, string>>;
}

export interface ReadingState {
  visibleSegmentIds: string[];
  languages: Language[];
  boldPali: boolean;
  searchQuery: string;
  searchResults: string[];
  dictionaryWord: string | null;
  currentChapterId: string;
  sidebarOpen: boolean;
  exportModalOpen: boolean;
  activeAnchorSegmentId: string | null;
}

export interface SettingsState {
  fontSize: number;
  theme: 'light' | 'dark';
  uiLanguage: UiLanguage;
}

export interface DictionaryEntry {
  pali: string;
  meaning: Record<Exclude<Language, 'pali'>, string>;
  grammar?: string;
  root?: string;
  examples?: string[];
}

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

export interface TriLingual {
  en: string;
  pt: string;
  es: string;
}

export interface SamasaPart {
  part: string;
  gloss: TriLingual;
  grammar?: TriLingual;
}

export interface SamasaAnalysis {
  type: TriLingual;
  viggaha?: string;
  literal: TriLingual;
  parts: SamasaPart[];
}

export interface LakkhanaCatukka {
  lakkhana: TriLingual;
  rasa: TriLingual;
  paccupatthana: TriLingual;
  padatthana: TriLingual;
}

export interface AbhidhammaEntryData {
  ontology: TriLingual;
  category: TriLingual;
  lakkhanaCatukka?: LakkhanaCatukka;
  philosophy: TriLingual;
  bodhiRef: string;
}

export interface DictionaryEntry {
  pali: string;
  baseLemma?: string;
  meaning: Record<Exclude<Language, 'pali'>, string>;
  grammar?: string;
  grammarLocalized?: TriLingual;
  root?: string;
  etymology?: TriLingual;
  samasa?: SamasaAnalysis;
  abhidhamma?: TriLingual | AbhidhammaEntryData;
  decomposition?: { parts: string[]; analysis: TriLingual };
  examples?: string[];
  tier?: 1 | 2 | 3;
  seeAlso?: string[];
  source?: string;
}


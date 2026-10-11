// src/components/Dictionary/DictionaryPanel.tsx
import React, { useState, useEffect, useCallback, useRef } from 'react';
import {
  View,
  TouchableOpacity,
  FlatList,
  StyleSheet,
  ScrollView,
} from 'react-native';
import { Text, TextInput } from '../ui/AppText';
import { lookupWord, searchDictionary, cleanPaliToken } from '../../services/dictionaryService';
import type { DictionaryEntry } from '../../types/models';
import { useAppSelector } from '../../store/hooks';
import { t } from '../../i18n';

const QUICK_TERMS = ['citta', 'cetasika', 'rūpa', 'nibbāna', 'kāmāvacara', 'kusala', 'akusala'];

export const DictionaryPanel: React.FC = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<DictionaryEntry[]>([]);
  const flatListRef = useRef<FlatList<DictionaryEntry>>(null);

  // Redux reading state
  const languages = useAppSelector((s) => s.reading.languages);
  const dictionaryWord = useAppSelector((s) => s.reading.dictionaryWord);
  const uiLanguage = useAppSelector((s) => s.settings.uiLanguage);

  // Active translation language: non-pali language if a single one is selected
  const nonPaliLanguages = (languages || []).filter(
    (lang): lang is 'en' | 'pt' | 'es' => lang === 'en' || lang === 'pt' || lang === 'es'
  );
  const activeLanguage = nonPaliLanguages.length === 1 ? nonPaliLanguages[0] : null;
  const lang = (languages.find((l) => l !== 'pali') || 'en') as 'en' | 'pt' | 'es';

  const executeSearch = useCallback((searchTerm: string) => {
    const trimmed = cleanPaliToken(searchTerm).trim();
    if (!trimmed) {
      setResults([]);
      return;
    }
    const exact = lookupWord(trimmed);
    const searchRes = searchDictionary(trimmed) || [];
    if (exact) {
      // Garante que o verbete exato fica no topo
      const filtered = searchRes.filter(
        (r) => r.pali.toLowerCase() !== exact.pali.toLowerCase()
      );
      setResults([exact, ...filtered]);
    } else {
      setResults(searchRes);
    }
    // Rola para o topo dos resultados
    flatListRef.current?.scrollToOffset({ offset: 0, animated: true });
  }, []);

  // Busca imediata quando uma palavra for clicada no leitor
  useEffect(() => {
    if (dictionaryWord) {
      setQuery(dictionaryWord);
      executeSearch(dictionaryWord);
    }
  }, [dictionaryWord, executeSearch]);

  const handleSearchChange = (text: string) => {
    setQuery(text);
  };

  // Debounce para busca digitada manualmente
  useEffect(() => {
    const timerId = setTimeout(() => {
      if (query.trim() !== '') {
        executeSearch(query);
      } else {
        setResults([]);
      }
    }, 200);
    return () => clearTimeout(timerId);
  }, [query, executeSearch]);

  const handleClear = () => {
    setQuery('');
    setResults([]);
  };

  const handleQuickTermPress = (term: string) => {
    setQuery(term);
    executeSearch(term);
  };

  const renderTranslations = (entry: DictionaryEntry) => {
    // Se um idioma específico estiver ativo, mostra ele
    if (activeLanguage && entry.meaning?.[activeLanguage]) {
      return (
        <View style={styles.translationContainer}>
          <Text style={styles.meaningText}>{entry.meaning[activeLanguage]}</Text>
        </View>
      );
    }

    // Se nenhum ou vários idiomas estiverem ativos, mostra os três (EN, PT, ES)
    const availableLangs: Array<'en' | 'pt' | 'es'> = ['en', 'pt', 'es'];
    return (
      <View style={styles.multiTranslationContainer}>
        {availableLangs.map((langKey) => {
          const text = entry.meaning?.[langKey];
          if (!text) return null;
          return (
            <View key={langKey} style={styles.langRow}>
              <View style={styles.langBadge}>
                <Text style={styles.langBadgeText}>{langKey.toUpperCase()}</Text>
              </View>
              <Text style={styles.multiMeaningText}>{text}</Text>
            </View>
          );
        })}
      </View>
    );
  };

  const renderCard = ({ item }: { item: DictionaryEntry }) => {
    return (
      <View style={styles.card}>
        <Text style={styles.paliWord}>{item.pali}</Text>

        {item.grammar ? (
          <Text style={styles.grammarText}>{item.grammar}</Text>
        ) : null}

        {item.root ? (
          <View style={styles.rootContainer}>
            <Text style={styles.rootLabel}>
              {t('dict.root', uiLanguage)}:{' '}
            </Text>
            <Text style={styles.rootText}>{item.root}</Text>
          </View>
        ) : null}

        {renderTranslations(item)}
      </View>
    );
  };

  const renderEmpty = () => {
    if (!query) {
      return (
        <View style={styles.emptyContainer}>
          <Text style={styles.emptyPrompt}>
            {t('dict.tapWord', uiLanguage)}
          </Text>
        </View>
      );
    }
    return (
      <View style={styles.emptyContainer}>
        <Text style={styles.emptyText}>
          {t('dict.notFound', uiLanguage)}
        </Text>
      </View>
    );
  };

  return (
    <View style={styles.container}>
      {/* Search Input Container */}
      <View style={styles.searchContainer}>
        <Text style={styles.searchIcon}>🔍</Text>
        <TextInput
          style={styles.input}
          placeholder={t('dict.searchPlaceholder', uiLanguage)}
          placeholderTextColor="#A89B8C"
          value={query}
          onChangeText={handleSearchChange}
          autoCapitalize="none"
          autoCorrect={false}
          returnKeyType="search"
        />
        {query.length > 0 && (
          <TouchableOpacity
            style={styles.clearButton}
            onPress={handleClear}
            accessibilityRole="button"
            accessibilityLabel="Limpar busca"
          >
            <Text style={styles.clearText}>✕</Text>
          </TouchableOpacity>
        )}
      </View>

      {/* Suggested Quick Terms */}
      <View style={styles.quickTermsContainer}>
        <ScrollView
          horizontal
          showsHorizontalScrollIndicator={false}
          contentContainerStyle={styles.quickTermsList}
        >
          {QUICK_TERMS.map((term) => (
            <TouchableOpacity
              key={term}
              style={styles.quickTermChip}
              onPress={() => handleQuickTermPress(term)}
            >
              <Text style={styles.quickTermText}>{term}</Text>
            </TouchableOpacity>
          ))}
        </ScrollView>
      </View>

      {/* Results List */}
      <FlatList
        ref={flatListRef}
        data={results}
        keyExtractor={(item, index) => `${item.pali}-${index}`}
        renderItem={renderCard}
        contentContainerStyle={styles.listContent}
        ListEmptyComponent={renderEmpty}
        keyboardShouldPersistTaps="handled"
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FAF5E4',
  },
  searchContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFDF7',
    borderRadius: 8,
    marginHorizontal: 16,
    marginTop: 12,
    marginBottom: 8,
    paddingHorizontal: 12,
    borderWidth: 1,
    borderColor: '#E8DCC8',
  },
  searchIcon: {
    fontSize: 16,
    marginRight: 8,
  },
  input: {
    flex: 1,
    height: 44,
    color: '#4B2E2A',
    fontSize: 15,
  },
  clearButton: {
    padding: 6,
  },
  clearText: {
    color: '#8B7355',
    fontSize: 16,
    fontWeight: 'bold',
  },
  quickTermsContainer: {
    marginBottom: 8,
    paddingVertical: 4,
  },
  quickTermsList: {
    paddingHorizontal: 16,
    gap: 8,
  },
  quickTermChip: {
    backgroundColor: '#E8DCC8',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 14,
  },
  quickTermText: {
    color: '#4B2E2A',
    fontSize: 13,
    fontWeight: '500',
  },
  listContent: {
    paddingHorizontal: 16,
    paddingBottom: 24,
  },
  card: {
    backgroundColor: '#FFFDF7',
    borderRadius: 10,
    padding: 16,
    marginBottom: 12,
    borderWidth: 1,
    borderColor: '#E8DCC8',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.05,
    shadowRadius: 3,
    elevation: 1,
  },
  paliWord: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#4B2E2A',
    marginBottom: 4,
  },
  grammarText: {
    fontSize: 13,
    fontStyle: 'italic',
    color: '#706050',
    marginBottom: 6,
  },
  rootContainer: {
    flexDirection: 'row',
    marginBottom: 8,
    flexWrap: 'wrap',
  },
  rootLabel: {
    fontSize: 12,
    color: '#8B7355',
    fontWeight: '600',
  },
  rootText: {
    fontSize: 12,
    color: '#5D4E37',
  },
  translationContainer: {
    marginTop: 4,
    paddingTop: 8,
    borderTopWidth: 1,
    borderTopColor: '#F0E8D8',
  },
  meaningText: {
    fontSize: 15,
    color: '#2B2B2B',
    lineHeight: 22,
  },
  multiTranslationContainer: {
    marginTop: 6,
    paddingTop: 8,
    borderTopWidth: 1,
    borderTopColor: '#F0E8D8',
    gap: 6,
  },
  langRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: 8,
  },
  langBadge: {
    backgroundColor: '#E8DCC8',
    paddingHorizontal: 6,
    paddingVertical: 2,
    borderRadius: 4,
    marginTop: 2,
  },
  langBadgeText: {
    fontSize: 10,
    fontWeight: 'bold',
    color: '#4B2E2A',
  },
  multiMeaningText: {
    flex: 1,
    fontSize: 14,
    color: '#3B3B3B',
    lineHeight: 20,
  },
  emptyContainer: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 48,
    paddingHorizontal: 20,
  },
  emptyText: {
    fontSize: 15,
    color: '#8B7355',
    fontStyle: 'italic',
  },
  emptyPrompt: {
    fontSize: 14,
    color: '#8B7355',
    textAlign: 'center',
    lineHeight: 20,
  },
});

export default DictionaryPanel;

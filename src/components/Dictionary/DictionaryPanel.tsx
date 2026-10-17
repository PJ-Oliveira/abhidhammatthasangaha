// src/components/Dictionary/DictionaryPanel.tsx
import React, { useState, useEffect, useCallback, useRef } from 'react';
import {
  View,
  TouchableOpacity,
  FlatList,
  StyleSheet,
} from 'react-native';
import { Text, TextInput } from '../ui/AppText';
import { lookupWord, searchDictionary, cleanPaliToken } from '../../services/dictionaryService';
import type { DictionaryEntry, AbhidhammaEntryData } from '../../types/models';
import { useAppSelector, useAppDispatch } from '../../store/hooks';
import { setDictionaryWord } from '../../store/slices/readingSlice';
import { t } from '../../i18n';

const QUICK_TERMS = [
  'paramattha',
  'citta',
  'cetasika',
  'rūpa',
  'nibbāna',
  'kāmāvacara',
  'kusala',
  'akusala',
  'somanassasahagata',
  'asaṅkhārika',
  'bhavaṅga',
  'javana',
  'paṭṭhāna',
  'vipassanā',
];

function isStructuredAbhidhamma(
  abhi: DictionaryEntry['abhidhamma']
): abhi is AbhidhammaEntryData {
  return Boolean(abhi && typeof abhi === 'object' && 'ontology' in abhi);
}

export const DictionaryPanel: React.FC = () => {
  const dispatch = useAppDispatch();
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<DictionaryEntry[]>([]);
  const flatListRef = useRef<FlatList<DictionaryEntry>>(null);

  // Redux reading & settings state
  const languages = useAppSelector((s) => s.reading.languages);
  const dictionaryWord = useAppSelector((s) => s.reading.dictionaryWord);
  const uiLanguage = useAppSelector((s) => s.settings.uiLanguage);

  const nonPaliLanguages = (languages || []).filter(
    (lang): lang is 'en' | 'pt' | 'es' => lang === 'en' || lang === 'pt' || lang === 'es'
  );
  const activeLanguage: 'en' | 'pt' | 'es' | null =
    uiLanguage || (nonPaliLanguages.length === 1 ? nonPaliLanguages[0] : null);
  const displayLang: 'pt' | 'en' | 'es' = activeLanguage || 'pt';

  const executeSearch = useCallback((searchTerm: string) => {
    const trimmed = cleanPaliToken(searchTerm).trim();
    if (!trimmed) {
      setResults([]);
      return;
    }
    const exact = lookupWord(trimmed);
    const searchRes = searchDictionary(trimmed) || [];
    if (exact) {
      const filtered = searchRes.filter(
        (r) => r.pali.toLowerCase() !== exact.pali.toLowerCase()
      );
      setResults([exact, ...filtered]);
    } else {
      setResults(searchRes);
    }
    flatListRef.current?.scrollToOffset({ offset: 0, animated: true });
  }, []);

  useEffect(() => {
    if (dictionaryWord) {
      setQuery(dictionaryWord);
      executeSearch(dictionaryWord);
    }
  }, [dictionaryWord, executeSearch]);

  const handleSearchChange = (text: string) => {
    setQuery(text);
  };

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
    dispatch(setDictionaryWord(null));
  };

  const handleTermNavigate = (term: string) => {
    setQuery(term);
    dispatch(setDictionaryWord(term));
    executeSearch(term);
  };

  const renderTranslations = (entry: DictionaryEntry) => {
    if (activeLanguage && entry.meaning?.[activeLanguage]) {
      return (
        <View style={styles.translationContainer}>
          <Text style={styles.meaningText}>{entry.meaning[activeLanguage]}</Text>
        </View>
      );
    }

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

  const renderSamasaSection = (entry: DictionaryEntry) => {
    const samasa = entry.samasa;
    if (!samasa) return null;

    return (
      <View style={styles.samasaBox}>
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.samasaHeaderTitle}>
            🧩 {t('dict.samasaTitle', displayLang)}
          </Text>
          {samasa.type?.[displayLang] ? (
            <View style={styles.samasaTypeBadge}>
              <Text style={styles.samasaTypeBadgeText}>
                {samasa.type[displayLang]}
              </Text>
            </View>
          ) : null}
        </View>

        {samasa.viggaha ? (
          <View style={styles.viggahaContainer}>
            <Text style={styles.subFieldLabel}>
              {t('dict.viggaha', displayLang)}:{' '}
            </Text>
            <Text style={styles.viggahaText}>{samasa.viggaha}</Text>
          </View>
        ) : null}

        {samasa.literal?.[displayLang] ? (
          <View style={styles.literalContainer}>
            <Text style={styles.subFieldLabel}>
              {t('dict.literal', displayLang)}:{' '}
            </Text>
            <Text style={styles.literalText}>{samasa.literal[displayLang]}</Text>
          </View>
        ) : null}

        {samasa.parts && samasa.parts.length > 0 ? (
          <View style={styles.samasaPartsGrid}>
            {samasa.parts.map((p, idx) => (
              <TouchableOpacity
                key={`${p.part}-${idx}`}
                style={styles.samasaPartCard}
                onPress={() => handleTermNavigate(p.part)}
              >
                <Text style={styles.samasaPartPali}>{p.part}</Text>
                {p.grammar?.[displayLang] ? (
                  <Text style={styles.samasaPartGrammar}>
                    {p.grammar[displayLang]}
                  </Text>
                ) : null}
                <Text style={styles.samasaPartGloss}>
                  {p.gloss?.[displayLang] || p.gloss?.en}
                </Text>
              </TouchableOpacity>
            ))}
          </View>
        ) : null}
      </View>
    );
  };

  const renderAbhidhammaSection = (entry: DictionaryEntry) => {
    if (!entry.abhidhamma) return null;

    if (!isStructuredAbhidhamma(entry.abhidhamma)) {
      const text = entry.abhidhamma[displayLang] || entry.abhidhamma.en;
      if (!text) return null;
      return (
        <View style={styles.abhidhammaBox}>
          <Text style={styles.abhidhammaHeaderTitle}>
            ☸ {t('dict.abhidhammaTitle', displayLang)}
          </Text>
          <Text style={styles.philosophyText}>{text}</Text>
        </View>
      );
    }

    const abhi = entry.abhidhamma;
    const catukka = abhi.lakkhanaCatukka;

    return (
      <View style={styles.abhidhammaBox}>
        <Text style={styles.abhidhammaHeaderTitle}>
          ☸ {t('dict.abhidhammaTitle', displayLang)}
        </Text>

        {/* Ontology & Category Badges */}
        <View style={styles.metaBadgesContainer}>
          {abhi.ontology?.[displayLang] ? (
            <View style={styles.ontologyBadge}>
              <Text style={styles.metaBadgeLabel}>
                {t('dict.ontology', displayLang)}:
              </Text>
              <Text style={styles.ontologyBadgeText}>
                {abhi.ontology[displayLang]}
              </Text>
            </View>
          ) : null}

          {abhi.category?.[displayLang] ? (
            <View style={styles.categoryBadge}>
              <Text style={styles.metaBadgeLabel}>
                {t('dict.category', displayLang)}:
              </Text>
              <Text style={styles.categoryBadgeText}>
                {abhi.category[displayLang]}
              </Text>
            </View>
          ) : null}
        </View>

        {/* Lakkhaṇādi-catukka (4-fold Defining Tetrad) */}
        {catukka ? (
          <View style={styles.catukkaContainer}>
            <Text style={styles.catukkaTitle}>
              {t('dict.lakkhanaTitle', displayLang)}
            </Text>
            <View style={styles.catukkaGrid}>
              <View style={styles.catukkaCard}>
                <Text style={styles.catukkaCardLabel}>
                  {t('dict.lakkhana', displayLang)}
                </Text>
                <Text style={styles.catukkaCardValue}>
                  {catukka.lakkhana[displayLang]}
                </Text>
              </View>
              <View style={styles.catukkaCard}>
                <Text style={styles.catukkaCardLabel}>
                  {t('dict.rasa', displayLang)}
                </Text>
                <Text style={styles.catukkaCardValue}>
                  {catukka.rasa[displayLang]}
                </Text>
              </View>
              <View style={styles.catukkaCard}>
                <Text style={styles.catukkaCardLabel}>
                  {t('dict.paccupatthana', displayLang)}
                </Text>
                <Text style={styles.catukkaCardValue}>
                  {catukka.paccupatthana[displayLang]}
                </Text>
              </View>
              <View style={styles.catukkaCard}>
                <Text style={styles.catukkaCardLabel}>
                  {t('dict.padatthana', displayLang)}
                </Text>
                <Text style={styles.catukkaCardValue}>
                  {catukka.padatthana[displayLang]}
                </Text>
              </View>
            </View>
          </View>
        ) : null}

        {/* Philosophical Synthesis */}
        {abhi.philosophy?.[displayLang] ? (
          <View style={styles.philosophySection}>
            <Text style={styles.subFieldLabel}>
              {t('dict.philosophy', displayLang)}:
            </Text>
            <Text style={styles.philosophyText}>
              {abhi.philosophy[displayLang]}
            </Text>
          </View>
        ) : null}

        {/* Bhikkhu Bodhi CMA Reference */}
        {abhi.bodhiRef ? (
          <View style={styles.bodhiRefRow}>
            <Text style={styles.bodhiRefLabel}>
              📖 {t('dict.bodhiRef', displayLang)}:{' '}
            </Text>
            <Text style={styles.bodhiRefText}>{abhi.bodhiRef}</Text>
          </View>
        ) : null}
      </View>
    );
  };

  const renderCard = ({ item }: { item: DictionaryEntry }) => {
    const localizedGrammar =
      item.grammarLocalized?.[displayLang] || item.grammar;

    return (
      <View style={styles.card}>
        <View style={styles.cardHeaderRow}>
          <Text style={styles.paliWord}>{item.pali}</Text>
          {item.baseLemma && item.baseLemma !== item.pali ? (
            <TouchableOpacity
              style={styles.baseLemmaChip}
              onPress={() => handleTermNavigate(item.baseLemma!)}
            >
              <Text style={styles.baseLemmaChipText}>
                {t('dict.baseLemma', displayLang)}: {item.baseLemma} ↗
              </Text>
            </TouchableOpacity>
          ) : null}
        </View>

        {localizedGrammar ? (
          <Text style={styles.grammarText}>{localizedGrammar}</Text>
        ) : null}

        {item.root ? (
          <View style={styles.rootContainer}>
            <Text style={styles.rootLabel}>
              {t('dict.root', displayLang)}:{' '}
            </Text>
            <Text style={styles.rootText}>{item.root}</Text>
          </View>
        ) : null}

        {item.etymology?.[displayLang] ? (
          <View style={styles.etymologyContainer}>
            <Text style={styles.rootLabel}>
              {t('dict.etymology', displayLang)}:{' '}
            </Text>
            <Text style={styles.etymologyText}>
              {item.etymology[displayLang]}
            </Text>
          </View>
        ) : null}

        {renderTranslations(item)}
        {renderSamasaSection(item)}
        {renderAbhidhammaSection(item)}

        {item.seeAlso && item.seeAlso.length > 0 ? (
          <View style={styles.seeAlsoContainer}>
            <Text style={styles.seeAlsoLabel}>
              {t('dict.seeAlso', displayLang)}:
            </Text>
            <View style={styles.seeAlsoChipsRow}>
              {item.seeAlso.map((rel) => (
                <TouchableOpacity
                  key={rel}
                  style={styles.seeAlsoChip}
                  onPress={() => handleTermNavigate(rel)}
                >
                  <Text style={styles.seeAlsoChipText}>{rel}</Text>
                </TouchableOpacity>
              ))}
            </View>
          </View>
        ) : null}
      </View>
    );
  };

  const renderEmpty = () => {
    if (!query) {
      return (
        <View style={styles.emptyContainer}>
          <Text style={styles.emptyPrompt}>
            {t('dict.tapWord', displayLang)}
          </Text>
        </View>
      );
    }
    return (
      <View style={styles.emptyContainer}>
        <Text style={styles.emptyText}>
          {t('dict.notFound', displayLang)}
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
          placeholder={t('dict.searchPlaceholder', displayLang)}
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
        <View style={styles.quickTermsList}>
          {QUICK_TERMS.map((term) => (
            <TouchableOpacity
              key={term}
              style={styles.quickTermChip}
              onPress={() => handleTermNavigate(term)}
            >
              <Text style={styles.quickTermText}>{term}</Text>
            </TouchableOpacity>
          ))}
        </View>
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
    flexDirection: 'row',
    flexWrap: 'wrap',
    paddingHorizontal: 16,
    gap: 6,
  },
  quickTermChip: {
    backgroundColor: '#E8DCC8',
    paddingHorizontal: 11,
    paddingVertical: 5,
    borderRadius: 14,
    marginBottom: 2,
  },
  quickTermText: {
    color: '#4B2E2A',
    fontSize: 12.5,
    fontWeight: '500',
  },
  listContent: {
    paddingHorizontal: 16,
    paddingBottom: 28,
  },
  card: {
    backgroundColor: '#FFFDF7',
    borderRadius: 12,
    padding: 16,
    marginBottom: 14,
    borderWidth: 1,
    borderColor: '#E8DCC8',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.06,
    shadowRadius: 4,
    elevation: 2,
  },
  cardHeaderRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    flexWrap: 'wrap',
    gap: 8,
    marginBottom: 4,
  },
  paliWord: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#4B2E2A',
  },
  baseLemmaChip: {
    backgroundColor: '#EFE6D5',
    paddingHorizontal: 9,
    paddingVertical: 3,
    borderRadius: 6,
    borderWidth: 1,
    borderColor: '#D8C7B0',
  },
  baseLemmaChipText: {
    fontSize: 11.5,
    color: '#5A3E2B',
    fontWeight: '600',
  },
  grammarText: {
    fontSize: 13,
    fontStyle: 'italic',
    color: '#706050',
    marginBottom: 6,
  },
  rootContainer: {
    flexDirection: 'row',
    marginBottom: 6,
    flexWrap: 'wrap',
  },
  rootLabel: {
    fontSize: 12,
    color: '#8B7355',
    fontWeight: '700',
  },
  rootText: {
    fontSize: 12,
    color: '#5D4E37',
    fontWeight: '500',
  },
  etymologyContainer: {
    marginBottom: 8,
    backgroundColor: '#FBF7EE',
    padding: 8,
    borderRadius: 6,
    borderLeftWidth: 3,
    borderLeftColor: '#C8B08C',
  },
  etymologyText: {
    fontSize: 12.5,
    color: '#524332',
    lineHeight: 18,
    marginTop: 2,
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
  samasaBox: {
    marginTop: 12,
    padding: 12,
    backgroundColor: '#F8F2E4',
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#E2D3B8',
  },
  sectionHeaderRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    flexWrap: 'wrap',
    gap: 6,
    marginBottom: 8,
  },
  samasaHeaderTitle: {
    fontSize: 13,
    fontWeight: '700',
    color: '#5C3A21',
  },
  samasaTypeBadge: {
    backgroundColor: '#E6D6BC',
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 5,
  },
  samasaTypeBadgeText: {
    fontSize: 11,
    fontWeight: '600',
    color: '#4B2E2A',
  },
  viggahaContainer: {
    marginBottom: 6,
  },
  literalContainer: {
    marginBottom: 8,
  },
  subFieldLabel: {
    fontSize: 12,
    fontWeight: '700',
    color: '#6E553C',
  },
  viggahaText: {
    fontSize: 13,
    fontStyle: 'italic',
    color: '#3F2B1D',
    marginTop: 2,
  },
  literalText: {
    fontSize: 13,
    color: '#3A3026',
    marginTop: 2,
  },
  samasaPartsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
    marginTop: 4,
  },
  samasaPartCard: {
    backgroundColor: '#FFFDF9',
    paddingHorizontal: 10,
    paddingVertical: 7,
    borderRadius: 6,
    borderWidth: 1,
    borderColor: '#DFCFAE',
    minWidth: 110,
    flexGrow: 1,
  },
  samasaPartPali: {
    fontSize: 13.5,
    fontWeight: '700',
    color: '#4B2E2A',
  },
  samasaPartGrammar: {
    fontSize: 10.5,
    fontStyle: 'italic',
    color: '#856D52',
  },
  samasaPartGloss: {
    fontSize: 12,
    color: '#3B3026',
    marginTop: 2,
  },
  abhidhammaBox: {
    marginTop: 12,
    padding: 12,
    backgroundColor: '#F4EFE6',
    borderRadius: 8,
    borderLeftWidth: 4,
    borderLeftColor: '#8B5A2B',
  },
  abhidhammaHeaderTitle: {
    fontSize: 13.5,
    fontWeight: '700',
    color: '#4B2E2A',
    marginBottom: 8,
  },
  metaBadgesContainer: {
    gap: 6,
    marginBottom: 10,
  },
  ontologyBadge: {
    backgroundColor: '#EAE0CE',
    padding: 8,
    borderRadius: 6,
  },
  categoryBadge: {
    backgroundColor: '#EFE7DA',
    padding: 8,
    borderRadius: 6,
  },
  metaBadgeLabel: {
    fontSize: 11,
    fontWeight: '700',
    color: '#6E553C',
    marginBottom: 2,
  },
  ontologyBadgeText: {
    fontSize: 12.5,
    fontWeight: '600',
    color: '#3B2314',
  },
  categoryBadgeText: {
    fontSize: 12.5,
    color: '#4A3525',
  },
  catukkaContainer: {
    marginTop: 4,
    marginBottom: 10,
  },
  catukkaTitle: {
    fontSize: 12,
    fontWeight: '700',
    color: '#5C3A21',
    marginBottom: 6,
  },
  catukkaGrid: {
    gap: 6,
  },
  catukkaCard: {
    backgroundColor: '#FFFDF8',
    padding: 8,
    borderRadius: 6,
    borderWidth: 1,
    borderColor: '#E2D5C1',
  },
  catukkaCardLabel: {
    fontSize: 11.5,
    fontWeight: '700',
    color: '#7A4B24',
    marginBottom: 2,
  },
  catukkaCardValue: {
    fontSize: 12.5,
    color: '#2F241B',
    lineHeight: 18,
  },
  philosophySection: {
    marginTop: 4,
    marginBottom: 8,
  },
  philosophyText: {
    fontSize: 13,
    color: '#2D231A',
    lineHeight: 19.5,
    marginTop: 3,
  },
  bodhiRefRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    alignItems: 'center',
    paddingTop: 6,
    borderTopWidth: 1,
    borderTopColor: '#E2D6C3',
  },
  bodhiRefLabel: {
    fontSize: 11.5,
    fontWeight: '700',
    color: '#6E553C',
  },
  bodhiRefText: {
    fontSize: 11.5,
    fontWeight: '600',
    color: '#4B2E2A',
  },
  seeAlsoContainer: {
    marginTop: 12,
    paddingTop: 8,
    borderTopWidth: 1,
    borderTopColor: '#F0E8D8',
  },
  seeAlsoLabel: {
    fontSize: 11.5,
    fontWeight: '700',
    color: '#8B7355',
    marginBottom: 6,
  },
  seeAlsoChipsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 6,
  },
  seeAlsoChip: {
    backgroundColor: '#EFE6D5',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
  },
  seeAlsoChipText: {
    fontSize: 12,
    color: '#4B2E2A',
    fontWeight: '600',
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

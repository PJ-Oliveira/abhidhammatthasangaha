// src/components/Dictionary/TermBottomSheet.tsx
import React, { useState } from 'react';
import {
  View,
  Modal,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
} from 'react-native';
import { Text } from '../ui/AppText';
import { useLayout } from '../../theme/layout';
import { useAppSelector, useAppDispatch } from '../../store/hooks';
import { setDictionaryWord } from '../../store/slices/readingSlice';
import { lookupWord, searchDictionary, cleanPaliToken } from '../../services/dictionaryService';
import type { DictionaryEntry, AbhidhammaEntryData } from '../../types/models';
import { t } from '../../i18n';

interface TermBottomSheetProps {
  onOpenFullDictionary?: (word: string) => void;
  hidden?: boolean;
}

function isStructuredAbhidhamma(
  abhi: DictionaryEntry['abhidhamma']
): abhi is AbhidhammaEntryData {
  return Boolean(abhi && typeof abhi === 'object' && 'ontology' in abhi);
}

export const TermBottomSheet: React.FC<TermBottomSheetProps> = ({
  onOpenFullDictionary,
  hidden = false,
}) => {
  const dispatch = useAppDispatch();
  const layout = useLayout();
  const dictionaryWord = useAppSelector((s) => s.reading.dictionaryWord);
  const languages = useAppSelector((s) => s.reading.languages);
  const uiLanguage = useAppSelector((s) => s.settings.uiLanguage);
  const translationLang: 'pt' | 'en' | 'es' =
    uiLanguage ||
    (languages.includes('pt')
      ? 'pt'
      : languages.includes('es')
      ? 'es'
      : 'en');

  const [isExpanded, setIsExpanded] = useState(false);

  const close = () => {
    dispatch(setDictionaryWord(null));
    setIsExpanded(false);
  };

  if (layout.isSplit || hidden || !dictionaryWord) {
    return null;
  }

  const cleanWord = cleanPaliToken(dictionaryWord).toLowerCase();
  const exactEntry = lookupWord(dictionaryWord);
  const searchResults = !exactEntry ? searchDictionary(cleanWord) : [];
  const entry = exactEntry || (searchResults.length > 0 ? searchResults[0] : null);

  const handleOpenFull = () => {
    setIsExpanded(false);
    dispatch(setDictionaryWord(cleanWord));
    onOpenFullDictionary?.(cleanWord);
  };

  const sheetHeight = isExpanded
    ? Math.min(layout.height * 0.78, 620)
    : Math.min(layout.height * 0.42, 340);

  const localizedGrammar =
    entry?.grammarLocalized?.[translationLang] || entry?.grammar;
  const structuredAbhi =
    entry && isStructuredAbhidhamma(entry.abhidhamma) ? entry.abhidhamma : null;

  return (
    <Modal
      transparent={true}
      visible={true}
      animationType="slide"
      onRequestClose={close}
    >
      <View style={styles.overlay}>
        <TouchableOpacity
          style={styles.backdrop}
          activeOpacity={1}
          onPress={close}
        />

        <View
          style={[
            styles.sheet,
            {
              height: sheetHeight,
              maxHeight: layout.height * 0.88,
              paddingHorizontal: layout.width < 380 ? 14 : 20,
            },
          ]}
        >
          {/* Pill handle */}
          <View style={styles.handleContainer}>
            <TouchableOpacity
              style={styles.handleBar}
              onPress={() => setIsExpanded((prev) => !prev)}
              accessibilityRole="button"
              accessibilityLabel={isExpanded ? t('dict.collapse', uiLanguage) : t('dict.expand', uiLanguage)}
            />
          </View>

          {/* Header */}
          <View style={styles.header}>
            <View style={styles.headerInfo}>
              <View style={styles.titleRow}>
                <Text style={styles.paliTitle} numberOfLines={1}>
                  {entry?.pali || cleanWord}
                </Text>
                {localizedGrammar ? (
                  <View style={styles.grammarBadge}>
                    <Text style={styles.grammarBadgeText}>{localizedGrammar}</Text>
                  </View>
                ) : null}
              </View>
              {entry?.root ? (
                <Text style={styles.rootText} numberOfLines={1}>
                  {t('dict.root', uiLanguage)}: {entry.root}
                </Text>
              ) : null}
            </View>

            <View style={styles.headerActions}>
              <TouchableOpacity
                style={styles.expandBtn}
                onPress={() => setIsExpanded((prev) => !prev)}
                accessibilityRole="button"
                accessibilityLabel={isExpanded ? t('dict.collapse', uiLanguage) : t('dict.expand', uiLanguage)}
              >
                <Text style={styles.expandBtnText}>
                  {isExpanded ? t('dict.collapse', uiLanguage) : t('dict.expand', uiLanguage)}
                </Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={styles.closeBtn}
                onPress={close}
                accessibilityRole="button"
                accessibilityLabel="Fechar"
              >
                <Text style={styles.closeBtnText}>✕</Text>
              </TouchableOpacity>
            </View>
          </View>

          {/* Definition Body */}
          <ScrollView
            style={styles.definitionScroll}
            contentContainerStyle={styles.definitionContent}
            showsVerticalScrollIndicator={true}
          >
            {entry ? (
              <>
                {structuredAbhi?.ontology?.[translationLang] ? (
                  <View style={styles.ontologyPill}>
                    <Text style={styles.ontologyPillText}>
                      ☸ {structuredAbhi.ontology[translationLang]}
                    </Text>
                  </View>
                ) : null}

                <Text style={styles.meaningText}>
                  {entry.meaning[translationLang] || entry.meaning.en}
                </Text>

                {/* Samāsa summary */}
                {entry.samasa ? (
                  <View style={styles.samasaCompactBox}>
                    <Text style={styles.samasaCompactTitle}>
                      🧩 {entry.samasa.type?.[translationLang]}
                    </Text>
                    {entry.samasa.viggaha ? (
                      <Text style={styles.viggahaCompactText}>
                        {entry.samasa.viggaha}
                      </Text>
                    ) : null}
                    {entry.samasa.parts && entry.samasa.parts.length > 0 ? (
                      <View style={styles.samasaPartsRow}>
                        {entry.samasa.parts.map((p, idx) => (
                          <TouchableOpacity
                            key={`${p.part}-${idx}`}
                            style={styles.samasaPartChip}
                            onPress={() => dispatch(setDictionaryWord(p.part))}
                          >
                            <Text style={styles.samasaPartChipText}>
                              {p.part}: {p.gloss?.[translationLang] || p.gloss?.en}
                            </Text>
                          </TouchableOpacity>
                        ))}
                      </View>
                    ) : null}
                  </View>
                ) : null}

                {/* Expanded scholarly details & alternate translations */}
                {isExpanded && (
                  <View style={styles.expandedDetails}>
                    {structuredAbhi?.lakkhanaCatukka ? (
                      <View style={styles.catukkaBox}>
                        <Text style={styles.catukkaHeader}>
                          {t('dict.lakkhanaTitle', translationLang)}
                        </Text>
                        <Text style={styles.catukkaItem}>
                          • {t('dict.lakkhana', translationLang)}:{' '}
                          {structuredAbhi.lakkhanaCatukka.lakkhana[translationLang]}
                        </Text>
                        <Text style={styles.catukkaItem}>
                          • {t('dict.rasa', translationLang)}:{' '}
                          {structuredAbhi.lakkhanaCatukka.rasa[translationLang]}
                        </Text>
                        <Text style={styles.catukkaItem}>
                          • {t('dict.paccupatthana', translationLang)}:{' '}
                          {structuredAbhi.lakkhanaCatukka.paccupatthana[translationLang]}
                        </Text>
                        <Text style={styles.catukkaItem}>
                          • {t('dict.padatthana', translationLang)}:{' '}
                          {structuredAbhi.lakkhanaCatukka.padatthana[translationLang]}
                        </Text>
                      </View>
                    ) : null}

                    {structuredAbhi?.philosophy?.[translationLang] ? (
                      <View style={styles.philosophyCompactBox}>
                        <Text style={styles.philosophyCompactText}>
                          {structuredAbhi.philosophy[translationLang]}
                        </Text>
                        {structuredAbhi.bodhiRef ? (
                          <Text style={styles.bodhiRefCompact}>
                            📖 {structuredAbhi.bodhiRef}
                          </Text>
                        ) : null}
                      </View>
                    ) : null}

                    {translationLang !== 'pt' && entry.meaning.pt && (
                      <View style={styles.altLangRow}>
                        <Text style={styles.altLangLabel}>PT:</Text>
                        <Text style={styles.altLangText}>{entry.meaning.pt}</Text>
                      </View>
                    )}
                    {translationLang !== 'en' && entry.meaning.en && (
                      <View style={styles.altLangRow}>
                        <Text style={styles.altLangLabel}>EN:</Text>
                        <Text style={styles.altLangText}>{entry.meaning.en}</Text>
                      </View>
                    )}
                    {translationLang !== 'es' && entry.meaning.es && (
                      <View style={styles.altLangRow}>
                        <Text style={styles.altLangLabel}>ES:</Text>
                        <Text style={styles.altLangText}>{entry.meaning.es}</Text>
                      </View>
                    )}
                  </View>
                )}
              </>
            ) : (
              <Text style={styles.notFoundText}>
                {t('dict.notFound', uiLanguage)} ({cleanWord})
              </Text>
            )}
          </ScrollView>

          {/* Footer */}
          <View style={styles.footer}>
            <TouchableOpacity
              style={styles.fullDictBtn}
              onPress={handleOpenFull}
              accessibilityRole="button"
              accessibilityLabel={t('dict.openFull', uiLanguage)}
            >
              <Text style={styles.fullDictBtnText}>
                📖 {t('dict.openFull', uiLanguage)}
              </Text>
            </TouchableOpacity>
          </View>
        </View>
      </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  overlay: {
    flex: 1,
    justifyContent: 'flex-end',
    backgroundColor: 'transparent',
  },
  backdrop: {
    ...StyleSheet.absoluteFillObject,
    backgroundColor: 'rgba(0, 0, 0, 0.35)',
  },
  sheet: {
    width: '100%',
    backgroundColor: '#FFFDF7',
    borderTopLeftRadius: 22,
    borderTopRightRadius: 22,
    borderTopWidth: 2,
    borderTopColor: '#D4A574',
    paddingBottom: 14,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: -6 },
    shadowOpacity: 0.15,
    shadowRadius: 14,
    elevation: 24,
  },
  handleContainer: {
    width: '100%',
    alignItems: 'center',
    paddingVertical: 8,
  },
  handleBar: {
    width: 44,
    height: 5,
    borderRadius: 3,
    backgroundColor: '#D8C7B0',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderBottomWidth: 1,
    borderBottomColor: '#F0E8D8',
    paddingBottom: 10,
    marginBottom: 8,
  },
  headerInfo: {
    flex: 1,
    paddingRight: 10,
  },
  titleRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    flexWrap: 'wrap',
  },
  paliTitle: {
    fontWeight: '700',
    fontSize: 20,
    color: '#4B2E2A',
  },
  grammarBadge: {
    backgroundColor: '#EFE6D6',
    paddingHorizontal: 7,
    paddingVertical: 2,
    borderRadius: 6,
  },
  grammarBadgeText: {
    fontSize: 11,
    color: '#7A624A',
    fontWeight: '600',
    fontStyle: 'italic',
  },
  rootText: {
    fontSize: 11.5,
    color: '#8C7355',
    marginTop: 2,
  },
  headerActions: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  expandBtn: {
    backgroundColor: '#EFE6D6',
    paddingHorizontal: 9,
    paddingVertical: 5,
    borderRadius: 6,
  },
  expandBtnText: {
    fontSize: 11.5,
    color: '#4B2E2A',
    fontWeight: '600',
  },
  closeBtn: {
    width: 30,
    height: 30,
    borderRadius: 15,
    backgroundColor: '#E8DCC8',
    alignItems: 'center',
    justifyContent: 'center',
  },
  closeBtnText: {
    fontSize: 14,
    color: '#4B2E2A',
    fontWeight: 'bold',
  },
  definitionScroll: {
    flex: 1,
  },
  definitionContent: {
    paddingVertical: 4,
  },
  ontologyPill: {
    backgroundColor: '#EFE6D5',
    paddingHorizontal: 9,
    paddingVertical: 4,
    borderRadius: 6,
    alignSelf: 'flex-start',
    marginBottom: 6,
  },
  ontologyPillText: {
    fontSize: 11.5,
    fontWeight: '700',
    color: '#5C3A21',
  },
  meaningText: {
    fontSize: 15,
    color: '#2C2219',
    lineHeight: 22,
  },
  samasaCompactBox: {
    marginTop: 8,
    padding: 8,
    backgroundColor: '#F8F2E4',
    borderRadius: 7,
    borderWidth: 1,
    borderColor: '#E2D3B8',
  },
  samasaCompactTitle: {
    fontSize: 11.5,
    fontWeight: '700',
    color: '#5C3A21',
  },
  viggahaCompactText: {
    fontSize: 12,
    fontStyle: 'italic',
    color: '#4A3525',
    marginTop: 2,
  },
  samasaPartsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 6,
    marginTop: 5,
  },
  samasaPartChip: {
    backgroundColor: '#FFFDF8',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 5,
    borderWidth: 1,
    borderColor: '#DFCFAE',
  },
  samasaPartChipText: {
    fontSize: 11.5,
    color: '#3B2B1E',
  },
  expandedDetails: {
    marginTop: 12,
    paddingTop: 10,
    borderTopWidth: 1,
    borderTopColor: '#F4ECE0',
    gap: 8,
  },
  catukkaBox: {
    backgroundColor: '#F6F0E4',
    padding: 9,
    borderRadius: 7,
    gap: 4,
  },
  catukkaHeader: {
    fontSize: 12,
    fontWeight: '700',
    color: '#5C3A21',
    marginBottom: 2,
  },
  catukkaItem: {
    fontSize: 12,
    color: '#2F241B',
    lineHeight: 17.5,
  },
  philosophyCompactBox: {
    backgroundColor: '#F4EFE6',
    padding: 9,
    borderRadius: 7,
    borderLeftWidth: 3,
    borderLeftColor: '#8B5A2B',
  },
  philosophyCompactText: {
    fontSize: 12.5,
    color: '#2D231A',
    lineHeight: 18,
  },
  bodhiRefCompact: {
    fontSize: 11,
    fontWeight: '700',
    color: '#6E553C',
    marginTop: 4,
  },
  altLangRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: 6,
  },
  altLangLabel: {
    fontSize: 12,
    fontWeight: '700',
    color: '#8C7355',
    width: 26,
  },
  altLangText: {
    flex: 1,
    fontSize: 13,
    color: '#4A3E2D',
    fontStyle: 'italic',
  },
  notFoundText: {
    fontSize: 13.5,
    color: '#8B7355',
    fontStyle: 'italic',
    textAlign: 'center',
    paddingVertical: 12,
  },
  footer: {
    marginTop: 6,
    paddingTop: 8,
    borderTopWidth: 1,
    borderTopColor: '#F4ECE0',
  },
  fullDictBtn: {
    backgroundColor: '#4B2E2A',
    paddingVertical: 8,
    borderRadius: 7,
    alignItems: 'center',
    justifyContent: 'center',
  },
  fullDictBtnText: {
    color: '#FAF5E4',
    fontSize: 13,
    fontWeight: '600',
  },
});

export default TermBottomSheet;

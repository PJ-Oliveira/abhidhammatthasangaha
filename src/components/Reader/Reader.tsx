// src/components/Reader/Reader.tsx
import React, { useMemo, useRef, useEffect, useState, useCallback } from 'react';
import { View, FlatList, StyleSheet, TouchableOpacity } from 'react-native';
import { useAppSelector, useAppDispatch } from '../../store/hooks';
import { setActiveAnchorSegmentId } from '../../store/slices/readingSlice';
import { updateBrowserRoute, getParagraphDirectUrl, copyTextToClipboard, chapterIdToNumber } from '../../utils/urlRouter';
import { t } from '../../i18n';
import { InteractivePaliText } from './InteractivePaliText';
import { Text } from '../ui/AppText';
import { useLayout } from '../../theme/layout';
import { splitIntoSentences, sanitizeHtmlText } from '../../utils/sentenceSplitter';
import type { Segment, Language } from '../../types/models';

interface ReaderProps {
  segments: Segment[];
  chapterNumber?: number;
}

export const Reader: React.FC<ReaderProps> = ({ segments, chapterNumber }) => {
  const dispatch = useAppDispatch();
  const layout = useLayout();
  const languages = useAppSelector((s) => s.reading.languages);
  const boldPali = useAppSelector((s) => s.reading.boldPali);
  const baseFontSize = useAppSelector((s) => s.settings.fontSize);
  const searchResults = useAppSelector((s) => s.reading.searchResults);
  const searchQuery = useAppSelector((s) => s.reading.searchQuery);
  const activeAnchorSegmentId = useAppSelector((s) => s.reading.activeAnchorSegmentId);
  const currentChapterId = useAppSelector((s) => s.reading.currentChapterId);
  const uiLanguage = useAppSelector((s) => s.settings.uiLanguage);

  const [toastMessage, setToastMessage] = useState<string | null>(null);
  const flatListRef = useRef<FlatList<Segment>>(null);

  const effectiveChapterNumber = chapterNumber ?? chapterIdToNumber(currentChapterId);

  const showPali = languages.includes('pali');
  const targetLanguages = useMemo(
    () => languages.filter((l): l is 'en' | 'pt' | 'es' => l !== 'pali'),
    [languages]
  );

  // Tamanho de fonte responsivo e ajustável pelo usuário
  const fontSize = baseFontSize + layout.fontBoost;
  const translationSize = fontSize - 1;

  // Filtra por busca se estiver ativa
  const visibleSegments = useMemo(() => {
    if (searchQuery && searchResults.length > 0) {
      return segments.filter((seg) => searchResults.includes(seg.id));
    } else if (searchQuery && searchResults.length === 0) {
      return [];
    } else {
      return segments;
    }
  }, [segments, searchQuery, searchResults]);

  const renderSegmentSentences = (item: Segment) => {
    // 1. Divide Pāli em sentenças por '.' ou '?'
    const paliSentences = showPali ? splitIntoSentences(item.pali) : [];

    // 2. Divide cada tradução ativa em sentenças por '.' ou '?'
    const translationSentencesMap: Record<'en' | 'pt' | 'es', string[]> = {
      en: [],
      pt: [],
      es: [],
    };

    targetLanguages.forEach((lang) => {
      const rawText = item.translations[lang] || '';
      const cleanText = sanitizeHtmlText(rawText);
      translationSentencesMap[lang] = splitIntoSentences(cleanText);
    });

    // 3. Determina o número total de unidades de sentença
    const sentenceCount = Math.max(
      paliSentences.length,
      ...targetLanguages.map((lang) => translationSentencesMap[lang].length),
      1
    );

    const sentenceBlocks = [];

    for (let i = 0; i < sentenceCount; i++) {
      const paliSent = paliSentences[i];
      const isLastBlock = i === sentenceCount - 1;

      sentenceBlocks.push(
        <View
          key={`sent-${i}`}
          style={[
            styles.sentenceUnit,
            !isLastBlock && styles.sentenceUnitBorder,
          ]}
        >
          {/* Sentença em Pāli (se Pāli estiver ativo e houver texto neste índice) */}
          {showPali && paliSent ? (
            <InteractivePaliText
              text={paliSent}
              style={[
                styles.paliText,
                boldPali ? styles.bold : null,
                { fontSize, lineHeight: Math.round(fontSize * 1.7) },
              ]}
            />
          ) : null}

          {/* Traduções correspondentes (cada sentença compulsoriamente em nova linha) */}
          {targetLanguages.map((lang) => {
            const transSent = translationSentencesMap[lang][i];
            if (!transSent) return null;

            return (
              <View key={lang} style={styles.translationRow}>
                {targetLanguages.length > 1 ? (
                  <View style={styles.langBadge}>
                    <Text style={styles.langBadgeText}>{lang.toUpperCase()}</Text>
                  </View>
                ) : null}
                <Text
                  style={[
                    styles.translationText,
                    {
                      fontSize: translationSize,
                      lineHeight: Math.round(translationSize * 1.6),
                    },
                  ]}
                >
                  {transSent}
                </Text>
              </View>
            );
          })}
        </View>
      );
    }

    return sentenceBlocks;
  };

  const handleAnchorClick = useCallback(
    async (segmentId: string) => {
      const url = getParagraphDirectUrl(effectiveChapterNumber, segmentId);
      await copyTextToClipboard(url);
      updateBrowserRoute(effectiveChapterNumber, segmentId, false);
      dispatch(setActiveAnchorSegmentId(segmentId));
      setToastMessage(t('link.copied', uiLanguage));
      setTimeout(() => {
        setToastMessage(null);
      }, 2600);
    },
    [dispatch, effectiveChapterNumber, uiLanguage]
  );

  // Rolagem suave para o parágrafo âncora se especificado na URL
  useEffect(() => {
    if (activeAnchorSegmentId && visibleSegments.length > 0) {
      const targetIndex = visibleSegments.findIndex((s) => s.id === activeAnchorSegmentId);
      if (targetIndex >= 0) {
        const timer = setTimeout(() => {
          try {
            flatListRef.current?.scrollToIndex({
              index: targetIndex,
              animated: true,
              viewPosition: 0.15,
            });
          } catch {
            // Ignorar caso a medição de células ainda esteja em andamento
          }
        }, 250);
        return () => clearTimeout(timer);
      }
    }
    return undefined;
  }, [activeAnchorSegmentId, visibleSegments]);

  const renderItem = React.useCallback(
    ({ item }: { item: Segment }) => {
      const isActive = activeAnchorSegmentId === item.id;
      return (
        <View
          style={[
            styles.segmentCard,
            isActive && styles.segmentCardActive,
            { padding: layout.pagePadding + 4 },
          ]}
        >
          <View style={styles.segmentHeaderRow}>
            <View style={styles.segmentNumber}>
              <Text
                style={[
                  styles.segmentNumberText,
                  isActive && styles.segmentNumberTextActive,
                ]}
              >
                {item.id}
              </Text>
            </View>
            <TouchableOpacity
              style={[styles.anchorBtn, isActive && styles.anchorBtnActive]}
              onPress={() => handleAnchorClick(item.id)}
              accessibilityRole="button"
              accessibilityLabel={t('link.copyAria', uiLanguage)}
              hitSlop={{ top: 8, bottom: 8, left: 8, right: 8 }}
            >
              <Text style={styles.anchorIcon}>🔗</Text>
              <Text
                style={[
                  styles.anchorText,
                  isActive && styles.anchorTextActive,
                ]}
              >
                Link
              </Text>
            </TouchableOpacity>
          </View>
          {renderSegmentSentences(item)}
        </View>
      );
    },
    [
      activeAnchorSegmentId,
      showPali,
      targetLanguages,
      boldPali,
      fontSize,
      translationSize,
      layout.pagePadding,
      handleAnchorClick,
      uiLanguage,
    ]
  );

  if (visibleSegments.length === 0) {
    return (
      <View style={styles.empty}>
        <Text style={styles.emptyIcon}>{searchQuery ? '🔍' : '📖'}</Text>
        <Text style={styles.emptyText}>
          {searchQuery
            ? `Nenhum resultado para "${searchQuery}"`
            : 'Nenhum segmento neste capítulo.'}
        </Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <FlatList
        ref={flatListRef}
        data={visibleSegments}
        keyExtractor={(item) => item.id}
        renderItem={renderItem}
        contentContainerStyle={[
          styles.list,
          {
            paddingHorizontal: layout.pagePadding,
            paddingTop: layout.pagePadding,
            maxWidth: layout.readerMaxWidth,
          },
        ]}
        ItemSeparatorComponent={Separator}
        initialNumToRender={8}
        maxToRenderPerBatch={10}
        windowSize={5}
        removeClippedSubviews={true}
        updateCellsBatchingPeriod={50}
        onScrollToIndexFailed={(info) => {
          setTimeout(() => {
            flatListRef.current?.scrollToIndex({
              index: info.index,
              animated: true,
              viewPosition: 0.15,
            });
          }, 350);
        }}
      />

      {toastMessage && (
        <View style={styles.toastContainer}>
          <Text style={styles.toastText}>✓ {toastMessage}</Text>
        </View>
      )}
    </View>
  );
};

const Separator: React.FC = () => <View style={styles.separator} />;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    position: 'relative',
  },
  list: {
    width: '100%',
    alignSelf: 'center',
    paddingBottom: 24,
  },
  segmentCard: {
    backgroundColor: '#FFFDF7',
    borderRadius: 12,
    shadowColor: '#000',
    shadowOpacity: 0.05,
    shadowRadius: 5,
    shadowOffset: { width: 0, height: 2 },
    elevation: 2,
    borderWidth: 1,
    borderColor: '#EFE6D4',
  },
  segmentCardActive: {
    borderColor: '#C59B27',
    borderWidth: 2,
    backgroundColor: '#FFFDF0',
    shadowColor: '#C59B27',
    shadowOpacity: 0.18,
    shadowRadius: 8,
  },
  segmentHeaderRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  segmentNumber: {},
  segmentNumberText: {
    fontSize: 11,
    color: '#A89274',
    fontWeight: '600',
    letterSpacing: 0.5,
  },
  segmentNumberTextActive: {
    color: '#8A5D00',
    fontWeight: '700',
  },
  anchorBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
    backgroundColor: '#F3EBDD',
    gap: 4,
  },
  anchorBtnActive: {
    backgroundColor: '#E8D296',
  },
  anchorIcon: {
    fontSize: 11,
  },
  anchorText: {
    fontSize: 11,
    color: '#7C674E',
    fontWeight: '600',
  },
  anchorTextActive: {
    color: '#654300',
    fontWeight: '700',
  },
  toastContainer: {
    position: 'absolute',
    bottom: 24,
    alignSelf: 'center',
    backgroundColor: '#2C1810',
    paddingHorizontal: 18,
    paddingVertical: 10,
    borderRadius: 24,
    shadowColor: '#000',
    shadowOpacity: 0.25,
    shadowRadius: 8,
    elevation: 6,
    zIndex: 999,
  },
  toastText: {
    color: '#FBF8F1',
    fontSize: 13,
    fontWeight: '600',
  },
  sentenceUnit: {
    paddingVertical: 6,
  },
  sentenceUnitBorder: {
    borderBottomWidth: 1,
    borderBottomColor: '#F3EBDD',
    marginBottom: 6,
    paddingBottom: 10,
  },
  paliText: {
    color: '#4B2E2A',
    marginBottom: 4,
  },
  bold: {
    fontWeight: 'bold',
  },
  translationRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginTop: 4,
    gap: 6,
  },
  langBadge: {
    backgroundColor: '#E8DCC8',
    paddingHorizontal: 5,
    paddingVertical: 1,
    borderRadius: 4,
    marginTop: 3,
  },
  langBadgeText: {
    fontSize: 10,
    fontWeight: 'bold',
    color: '#4B2E2A',
  },
  translationText: {
    flex: 1,
    color: '#5D4E37',
    fontStyle: 'italic',
  },
  separator: {
    height: 14,
  },
  empty: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 32,
  },
  emptyIcon: {
    fontSize: 40,
    marginBottom: 12,
  },
  emptyText: {
    fontSize: 15,
    color: '#8B7355',
    textAlign: 'center',
  },
});

export default Reader;

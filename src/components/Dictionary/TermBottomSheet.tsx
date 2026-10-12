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
import { t } from '../../i18n';

interface TermBottomSheetProps {
  onOpenFullDictionary?: (word: string) => void;
  hidden?: boolean;
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
  const translationLang =
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

  // No modo split (tablet, desktop), o dicionário já está aberto ao lado na tela.
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
    ? Math.min(layout.height * 0.68, 560)
    : Math.min(layout.height * 0.32, 260);

  return (
    <Modal
      transparent={true}
      visible={true}
      animationType="slide"
      onRequestClose={close}
    >
      <View style={styles.overlay}>
        {/* Backdrop suave que fecha ao tocar fora */}
        <TouchableOpacity
          style={styles.backdrop}
          activeOpacity={1}
          onPress={close}
        />

        {/* Card deslizante dinâmico e responsivo */}
        <View
          style={[
            styles.sheet,
            {
              height: sheetHeight,
              maxHeight: layout.height * 0.85,
              paddingHorizontal: layout.width < 380 ? 14 : 20,
            },
          ]}
        >
          {/* Alça visual de toque (Pill handle) */}
          <View style={styles.handleContainer}>
            <TouchableOpacity
              style={styles.handleBar}
              onPress={() => setIsExpanded((prev) => !prev)}
              accessibilityRole="button"
              accessibilityLabel={isExpanded ? t('dict.collapse', uiLanguage) : t('dict.expand', uiLanguage)}
            />
          </View>

          {/* Cabeçalho do Verbete */}
          <View style={styles.header}>
            <View style={styles.headerInfo}>
              <View style={styles.titleRow}>
                <Text style={styles.paliTitle} numberOfLines={1}>
                  {entry?.pali || cleanWord}
                </Text>
                {entry?.grammar ? (
                  <View style={styles.grammarBadge}>
                    <Text style={styles.grammarBadgeText}>{entry.grammar}</Text>
                  </View>
                ) : null}
              </View>
              {entry?.root ? (
                <Text style={styles.rootText} numberOfLines={1}>
                  {t('dict.root', uiLanguage)}: {entry.root}
                </Text>
              ) : null}
            </View>

            {/* Ações rápidas superiores: Expandir/Recolher e Fechar */}
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

          {/* Corpo da Definição */}
          <ScrollView
            style={styles.definitionScroll}
            contentContainerStyle={styles.definitionContent}
            showsVerticalScrollIndicator={true}
          >
            {entry ? (
              <>
                <Text style={styles.meaningText}>
                  {entry.meaning[translationLang] || entry.meaning.en}
                </Text>

                {/* Se expandido, mostra traduções alternativas caso existam */}
                {isExpanded && (
                  <View style={styles.expandedDetails}>
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

          {/* Rodapé com botão para o dicionário completo */}
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
  meaningText: {
    fontSize: 15,
    color: '#2C2219',
    lineHeight: 22,
  },
  expandedDetails: {
    marginTop: 12,
    paddingTop: 10,
    borderTopWidth: 1,
    borderTopColor: '#F4ECE0',
    gap: 6,
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

// src/components/HomeScreen.tsx
import React, { useEffect, useState, useCallback } from 'react';
import { View, StyleSheet, SafeAreaView, TouchableOpacity, ActivityIndicator, Platform, StatusBar } from 'react-native';
import { Reader } from './Reader/Reader';
import { LanguageSelector } from './LanguageSelector/LanguageSelector';
import { SearchBar } from './SearchBar/SearchBar';
import { DictionaryPanel } from './Dictionary/DictionaryPanel';
import { TermBottomSheet } from './Dictionary/TermBottomSheet';
import { ChapterSidebar } from './ChapterSidebar/ChapterSidebar';
import { ExportModal } from './ExportModal/ExportModal';
import { Text } from './ui/AppText';
import { useAppDispatch, useAppSelector } from '../store/hooks';
import { toggleSidebar, setCurrentChapter, setExportModalOpen, setActiveAnchorSegmentId } from '../store/slices/readingSlice';
import { setUiLanguage } from '../store/slices/settingsSlice';
import { CHAPTERS, getChapter } from '../data/chapters/chapterIndex';
import { loadChapter } from '../data/chapters/chapterLoader';
import { buildSearchIndex } from '../services/textSearch';
import { useLayout } from '../theme/layout';
import { getCurrentRoute, updateBrowserRoute, chapterIdToNumber } from '../utils/urlRouter';
import { AnkiDeck } from './AnkiDeck/AnkiDeck';
import { CompendiumMatrix } from './Matrix/CompendiumMatrix';
import { t } from '../i18n';
import type { Segment, UiLanguage } from '../types/models';

type Tab = 'reader' | 'anki' | 'matrix' | 'dictionary';

const HomeScreen = () => {
  const dispatch = useAppDispatch();
  const currentChapterId = useAppSelector((s) => s.reading.currentChapterId);
  const languages = useAppSelector((s) => s.reading.languages);
  const exportModalOpen = useAppSelector((s) => s.reading.exportModalOpen);
  const uiLanguage = useAppSelector((s) => s.settings.uiLanguage);
  const translationLang = languages.includes('pt') ? 'pt' : languages.includes('es') ? 'es' : 'en';
  const layout = useLayout();

  const [activeTab, setActiveTab] = useState<Tab>('reader');
  const [segments, setSegments] = useState<Segment[]>([]);
  const [loading, setLoading] = useState(true);

  const chapter = getChapter(currentChapterId);
  const chapterIndex = CHAPTERS.findIndex((c) => c.id === currentChapterId);

  // 1. Sincronização inicial de URL e histórico do navegador (popstate)
  useEffect(() => {
    const initialRoute = getCurrentRoute();
    if (initialRoute.chapterId && initialRoute.chapterId !== currentChapterId) {
      dispatch(setCurrentChapter(initialRoute.chapterId));
    }
    if (initialRoute.segmentId) {
      dispatch(setActiveAnchorSegmentId(initialRoute.segmentId));
    }

    const handlePopState = () => {
      const route = getCurrentRoute();
      dispatch(setCurrentChapter(route.chapterId));
      dispatch(setActiveAnchorSegmentId(route.segmentId));
    };

    if (typeof window !== 'undefined' && typeof window.addEventListener === 'function') {
      window.addEventListener('popstate', handlePopState);
      return () => {
        if (typeof window.removeEventListener === 'function') {
          window.removeEventListener('popstate', handlePopState);
        }
      };
    }
    return undefined;
  }, [dispatch]);

  // 2. Atualiza a URL do navegador sempre que o capítulo muda
  useEffect(() => {
    const num = chapterIdToNumber(currentChapterId);
    const cur = getCurrentRoute();
    if (cur.chapterNumber !== num) {
      updateBrowserRoute(num, null, false);
    }
  }, [currentChapterId]);

  // 3. Carrega dados do capítulo ao mudar
  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    loadChapter(currentChapterId).then((data) => {
      if (!cancelled) {
        setSegments(data);
        setLoading(false);
      }
    });
    // Fire and forget: carrega índice de pesquisa
    buildSearchIndex();
    return () => { cancelled = true; };
  }, [currentChapterId]);

  const goToPrev = () => {
    if (chapterIndex > 0) {
      const prevChap = CHAPTERS[chapterIndex - 1];
      dispatch(setCurrentChapter(prevChap.id));
      updateBrowserRoute(prevChap.number, null, false);
    }
  };

  const goToNext = () => {
    if (chapterIndex < CHAPTERS.length - 1) {
      const nextChap = CHAPTERS[chapterIndex + 1];
      dispatch(setCurrentChapter(nextChap.id));
      updateBrowserRoute(nextChap.number, null, false);
    }
  };

  const padX = layout.pagePadding;
  const navPadY = layout.isShortHeight ? 6 : 10;

  const renderReader = () => (
    <View style={styles.content}>
      <SearchBar />
      {loading ? (
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#4B2E2A" />
          <Text style={styles.loadingText}>{t('loading.chapter', uiLanguage)}</Text>
        </View>
      ) : (
        <Reader segments={segments} chapterNumber={chapter?.number ?? chapterIndex + 1} />
      )}

      {/* Chapter navigation */}
      <View style={[styles.chapterNav, { paddingHorizontal: padX, paddingVertical: navPadY }]}>
        <TouchableOpacity
          style={[styles.navBtn, chapterIndex <= 0 && styles.navBtnDisabled]}
          onPress={goToPrev}
          disabled={chapterIndex <= 0}
        >
          <Text style={[styles.navBtnText, chapterIndex <= 0 && styles.navBtnTextDisabled]}>
            {t('nav.prev', uiLanguage)}
          </Text>
        </TouchableOpacity>
        <Text style={styles.navChapter}>
          {chapter?.number} {t('nav.chapterOf', uiLanguage)} {CHAPTERS.length}
        </Text>
        <TouchableOpacity
          style={[styles.navBtn, chapterIndex >= CHAPTERS.length - 1 && styles.navBtnDisabled]}
          onPress={goToNext}
          disabled={chapterIndex >= CHAPTERS.length - 1}
        >
          <Text style={[styles.navBtnText, chapterIndex >= CHAPTERS.length - 1 && styles.navBtnTextDisabled]}>
            {t('nav.next', uiLanguage)}
          </Text>
        </TouchableOpacity>
      </View>
    </View>
  );

  const renderDictionary = () => (
    <View style={styles.content}>
      <DictionaryPanel />
    </View>
  );

  return (
    <SafeAreaView style={styles.container}>
      {/* `frame` centraliza e limita a largura em monitores muito grandes */}
      <View style={[styles.frame, { maxWidth: layout.contentMaxWidth }]}>
        {/* Header */}
        <View
          style={[
            styles.header,
            { paddingHorizontal: padX, paddingVertical: layout.isShortHeight ? 6 : 12 },
            layout.headerStacked && styles.headerStacked,
          ]}
        >
          <View style={[styles.headerLeft, !layout.headerStacked && styles.headerLeftWide]}>
            <TouchableOpacity
              style={styles.menuBtn}
              onPress={() => dispatch(toggleSidebar())}
              accessibilityRole="button"
              accessibilityLabel={t('header.menu', uiLanguage)}
            >
              <Text style={styles.menuIcon}>☰</Text>
            </TouchableOpacity>
            <View style={styles.titleBlock}>
              <Text style={[styles.title, layout.width >= 1024 && styles.titleLarge]} numberOfLines={1}>
                {chapter ? `${chapter.number}. ${chapter.paliTitle}` : t('app.title', uiLanguage)}
              </Text>
              <Text style={styles.titleTranslation} numberOfLines={1}>
                {chapter?.titles[uiLanguage] || chapter?.titles[translationLang]}
              </Text>
            </View>
          </View>
          {layout.headerStacked ? (
            <View style={styles.headerStackedControls}>
              <View style={styles.headerActionsRow}>
                {/* Seletor de Idioma da Interface (PT | EN | ES) */}
                <View style={styles.uiLangSwitcher}>
                  {(['pt', 'en', 'es'] as UiLanguage[]).map((langCode) => {
                    const active = uiLanguage === langCode;
                    return (
                      <TouchableOpacity
                        key={langCode}
                        style={[styles.uiLangBtn, active && styles.uiLangBtnActive]}
                        onPress={() => dispatch(setUiLanguage(langCode))}
                        accessibilityRole="button"
                        accessibilityLabel={`Interface ${langCode.toUpperCase()}`}
                      >
                        <Text style={[styles.uiLangBtnText, active && styles.uiLangBtnTextActive]}>
                          {langCode.toUpperCase()}
                        </Text>
                      </TouchableOpacity>
                    );
                  })}
                </View>

                {/* Botão de Exportação */}
                <TouchableOpacity
                  style={styles.exportHeaderBtn}
                  onPress={() => dispatch(setExportModalOpen(true))}
                  accessibilityRole="button"
                  accessibilityLabel={t('header.exportAria', uiLanguage)}
                  activeOpacity={0.8}
                >
                  <Text style={styles.exportHeaderBtnText}>{t('header.export', uiLanguage)}</Text>
                </TouchableOpacity>
              </View>

              {/* Seletor de Idiomas do Leitor (Pāli, English, Português, Español) */}
              <View style={styles.languageSelectorRow}>
                <LanguageSelector />
              </View>
            </View>
          ) : (
            <View style={styles.headerRight}>
              {/* Seletor de Idioma da Interface (PT | EN | ES) */}
              <View style={styles.uiLangSwitcher}>
                {(['pt', 'en', 'es'] as UiLanguage[]).map((langCode) => {
                  const active = uiLanguage === langCode;
                  return (
                    <TouchableOpacity
                      key={langCode}
                      style={[styles.uiLangBtn, active && styles.uiLangBtnActive]}
                      onPress={() => dispatch(setUiLanguage(langCode))}
                      accessibilityRole="button"
                      accessibilityLabel={`Interface ${langCode.toUpperCase()}`}
                    >
                      <Text style={[styles.uiLangBtnText, active && styles.uiLangBtnTextActive]}>
                        {langCode.toUpperCase()}
                      </Text>
                    </TouchableOpacity>
                  );
                })}
              </View>

              {/* Botão de Exportação */}
              <TouchableOpacity
                style={styles.exportHeaderBtn}
                onPress={() => dispatch(setExportModalOpen(true))}
                accessibilityRole="button"
                accessibilityLabel={t('header.exportAria', uiLanguage)}
                activeOpacity={0.8}
              >
                <Text style={styles.exportHeaderBtnText}>{t('header.export', uiLanguage)}</Text>
              </TouchableOpacity>

              <View style={styles.languageSelectorContainer}>
                <LanguageSelector />
              </View>
            </View>
          )}
        </View>

        {/* Content Area */}
        {layout.isSplit ? (
          // Split view para tablet / iPad / notebook / desktop
          <View style={{ flex: 1 }}>
            {/* Top Navigation Tabs for Desktop / Tablet */}
            <View style={[styles.tabBar, { paddingHorizontal: padX, marginBottom: 8 }]}>
              <TouchableOpacity
                style={[styles.tab, activeTab === 'reader' && styles.tabActive]}
                onPress={() => setActiveTab('reader')}
              >
                <Text style={[styles.tabText, activeTab === 'reader' && styles.tabTextActive]}>
                  {t('tabs.reader', uiLanguage)}
                </Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.tab, activeTab === 'anki' && styles.tabActive]}
                onPress={() => setActiveTab('anki')}
              >
                <Text style={[styles.tabText, activeTab === 'anki' && styles.tabTextActive]}>
                  {t('tabs.anki', uiLanguage)}
                </Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.tab, activeTab === 'matrix' && styles.tabActive]}
                onPress={() => setActiveTab('matrix')}
              >
                <Text style={[styles.tabText, activeTab === 'matrix' && styles.tabTextActive]}>
                  {t('tabs.matrix', uiLanguage)}
                </Text>
              </TouchableOpacity>
            </View>

            <View style={styles.splitContainer}>
              <View style={styles.splitMain}>
                {activeTab === 'anki' ? (
                  <AnkiDeck />
                ) : activeTab === 'matrix' ? (
                  <CompendiumMatrix />
                ) : (
                  renderReader()
                )}
              </View>
              <View style={[styles.splitSide, { width: layout.sidePanelWidth }]}>
                {renderDictionary()}
              </View>
            </View>
          </View>
        ) : (
          // Abas para celular com rolagem horizontal fluida
          <>
            <View style={[styles.tabBar, { paddingHorizontal: padX }]}>
              <TouchableOpacity
                style={[styles.tab, activeTab === 'reader' && styles.tabActive]}
                onPress={() => setActiveTab('reader')}
              >
                <Text style={[styles.tabText, activeTab === 'reader' && styles.tabTextActive]}>
                  {t('tabs.reader', uiLanguage)}
                </Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.tab, activeTab === 'anki' && styles.tabActive]}
                onPress={() => setActiveTab('anki')}
              >
                <Text style={[styles.tabText, activeTab === 'anki' && styles.tabTextActive]}>
                  {t('tabs.anki', uiLanguage)}
                </Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.tab, activeTab === 'matrix' && styles.tabActive]}
                onPress={() => setActiveTab('matrix')}
              >
                <Text style={[styles.tabText, activeTab === 'matrix' && styles.tabTextActive]}>
                  {t('tabs.matrix', uiLanguage)}
                </Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.tab, activeTab === 'dictionary' && styles.tabActive]}
                onPress={() => setActiveTab('dictionary')}
              >
                <Text style={[styles.tabText, activeTab === 'dictionary' && styles.tabTextActive]}>
                  {t('tabs.dictionary', uiLanguage)}
                </Text>
              </TouchableOpacity>
            </View>

            {activeTab === 'reader' && renderReader()}
            {activeTab === 'anki' && <AnkiDeck />}
            {activeTab === 'matrix' && <CompendiumMatrix />}
            {activeTab === 'dictionary' && renderDictionary()}
          </>
        )}
      </View>

      {/* Sidebar overlay, Dicionário Modal e Modal de Exportação */}
      <ChapterSidebar />
      <TermBottomSheet
        onOpenFullDictionary={() => {
          setActiveTab('dictionary');
        }}
      />
      <ExportModal
        visible={exportModalOpen}
        onClose={() => dispatch(setExportModalOpen(false))}
      />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FAF5E4',
    paddingTop: Platform.OS === 'android' ? StatusBar.currentHeight : 0,
    overflow: 'hidden',
  },
  frame: {
    flex: 1,
    width: '100%',
    alignSelf: 'center',
    overflow: 'hidden',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderBottomWidth: 1,
    borderBottomColor: '#E8DCC8',
  },
  headerStacked: {
    flexDirection: 'column',
    alignItems: 'flex-start',
    paddingBottom: 12,
  },
  headerLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    width: '100%', // Evita colapso
  },
  headerLeftWide: {
    flex: 1,
    width: 'auto',
    marginRight: 12,
    minWidth: 0, // permite o título truncar em vez de empurrar o seletor de idioma
  },
  headerRight: {
    flexDirection: 'row',
    alignItems: 'center',
    flexShrink: 0,
    gap: 8,
  },
  headerStackedControls: {
    width: '100%',
    marginTop: 10,
    gap: 8,
  },
  headerActionsRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    width: '100%',
  },
  languageSelectorRow: {
    width: '100%',
    alignItems: 'center',
    justifyContent: 'center',
  },
  uiLangSwitcher: {
    flexDirection: 'row',
    backgroundColor: '#E8DCC8',
    borderRadius: 8,
    padding: 2,
    gap: 2,
  },
  uiLangBtn: {
    paddingHorizontal: 8,
    paddingVertical: 5,
    borderRadius: 6,
    justifyContent: 'center',
    alignItems: 'center',
  },
  uiLangBtnActive: {
    backgroundColor: '#4B2E2A',
  },
  uiLangBtnText: {
    fontSize: 11,
    fontWeight: '600',
    color: '#654C38',
  },
  uiLangBtnTextActive: {
    color: '#FAF5E4',
    fontWeight: '700',
  },
  exportHeaderBtn: {
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: 8,
    backgroundColor: '#4B2E2A',
    alignItems: 'center',
    justifyContent: 'center',
  },
  exportHeaderBtnText: {
    color: '#F5E6D0',
    fontSize: 13,
    fontWeight: '700',
  },
  languageSelectorContainer: {
    flexShrink: 0,
  },
  menuBtn: {
    width: 44,
    height: 44,
    borderRadius: 10,
    backgroundColor: '#4B2E2A',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 12,
  },
  menuIcon: { color: '#FAF5E4', fontSize: 20 },
  titleBlock: { flex: 1, minWidth: 0 },
  title: { fontSize: 16, fontWeight: 'bold', color: '#4B2E2A' },
  titleLarge: { fontSize: 20 },
  titleTranslation: { fontSize: 12, color: '#8B7355', fontStyle: 'italic', marginTop: 1 },
  tabBar: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    paddingVertical: 6,
    gap: 6,
  },
  tab: {
    flex: 1,
    minWidth: 70,
    minHeight: 42,
    paddingHorizontal: 6,
    justifyContent: 'center',
    borderRadius: 8,
    backgroundColor: '#E8DCC8',
    alignItems: 'center',
  },
  tabActive: { backgroundColor: '#4B2E2A' },
  tabText: { fontSize: 13, color: '#4B2E2A', fontWeight: '500', textAlign: 'center' },
  tabTextActive: { color: '#FAF5E4', fontWeight: '700' },
  content: { flex: 1, minHeight: 0 },
  loadingContainer: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  loadingText: { marginTop: 12, fontSize: 14, color: '#8B7355' },
  chapterNav: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderTopWidth: 1,
    borderTopColor: '#E8DCC8',
    backgroundColor: '#F5EDD8',
  },
  navBtn: {
    minHeight: 44,
    minWidth: 96,
    paddingHorizontal: 16,
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 8,
    backgroundColor: '#4B2E2A',
  },
  navBtnDisabled: { backgroundColor: '#D4C8B0', opacity: 0.5 },
  navBtnText: { color: '#FAF5E4', fontSize: 14, fontWeight: '600' },
  navBtnTextDisabled: { color: '#9A8A70' },
  navChapter: { fontSize: 14, color: '#8B7355', fontWeight: '600' },
  splitContainer: {
    flex: 1,
    flexDirection: 'row',
    minHeight: 0,
  },
  splitMain: {
    flex: 1,
    minWidth: 0,
    borderRightWidth: 1,
    borderRightColor: '#E8DCC8',
  },
  splitSide: {
    backgroundColor: '#FAF5E4',
  },
});

export default HomeScreen;

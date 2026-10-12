// src/components/ChapterSidebar/ChapterSidebar.tsx
import React from 'react';
import {
  View,
  TouchableOpacity,
  ScrollView,
  StyleSheet,
  Pressable,
} from 'react-native';
import { Text } from '../ui/AppText';
import { useLayout } from '../../theme/layout';
import { useAppSelector, useAppDispatch } from '../../store/hooks';
import { setCurrentChapter, setSidebarOpen, setExportModalOpen } from '../../store/slices/readingSlice';
import { CHAPTERS } from '../../data/chapters/chapterIndex';
import { updateBrowserRoute, chapterIdToNumber } from '../../utils/urlRouter';
import { t } from '../../i18n';

export const ChapterSidebar: React.FC = () => {
  const layout = useLayout();
  const dispatch = useAppDispatch();
  const sidebarOpen = useAppSelector((s) => s.reading.sidebarOpen);
  const currentChapterId = useAppSelector((s) => s.reading.currentChapterId);
  const languages = useAppSelector((s) => s.reading.languages);
  const uiLanguage = useAppSelector((s) => s.settings.uiLanguage);
  const translationLang = languages.includes('pt') ? 'pt' : languages.includes('es') ? 'es' : 'en';

  const handleSelectChapter = (chapterId: string) => {
    dispatch(setCurrentChapter(chapterId));
    updateBrowserRoute(chapterIdToNumber(chapterId), null, false);
    dispatch(setSidebarOpen(false));
  };

  const handleClose = () => {
    dispatch(setSidebarOpen(false));
  };

  if (!sidebarOpen) return null;

  return (
    <View style={styles.overlay}>
      {/* Backdrop */}
      <Pressable style={styles.backdrop} onPress={handleClose} />

      {/* Sidebar panel */}
      <View style={[styles.sidebar, { width: layout.sidebarWidth }]}>
        {/* Header */}
        <View style={styles.header}>
          <View style={{ flex: 1, marginRight: 8 }}>
            <Text style={styles.headerTitle}>{t('sidebar.title', uiLanguage)}</Text>
            <Text style={styles.subtitle}>{t('app.subtitle', uiLanguage)}</Text>
          </View>
          <TouchableOpacity onPress={handleClose} style={styles.closeBtn}>
            <Text style={styles.closeBtnText}>✕</Text>
          </TouchableOpacity>
        </View>

        {/* Chapter list (9 Paricchedas) */}
        <ScrollView style={styles.scrollView} showsVerticalScrollIndicator={false}>
          <View style={styles.partSection}>
            {CHAPTERS.map((ch) => {
              const isActive = ch.id === currentChapterId;
              return (
                <TouchableOpacity
                  key={ch.id}
                  style={[styles.chapterRow, isActive && styles.chapterRowActive]}
                  onPress={() => handleSelectChapter(ch.id)}
                  activeOpacity={0.7}
                >
                  <View style={[styles.chapterBadge, isActive && styles.chapterBadgeActive]}>
                    <Text style={[styles.chapterNumber, isActive && styles.chapterTextActive]}>
                      {ch.number}
                    </Text>
                  </View>
                  <View style={styles.chapterTextColumn}>
                    <Text style={[styles.chapterPali, isActive && styles.chapterTextActive]}>
                      {ch.paliTitle}
                    </Text>
                    <Text
                      style={[styles.chapterTranslation, isActive && styles.chapterTranslationActive]}
                    >
                      {ch.titles[uiLanguage] || ch.titles[translationLang]}
                    </Text>
                  </View>
                </TouchableOpacity>
              );
            })}
          </View>
          <View style={{ height: 20 }} />
        </ScrollView>

        {/* Footer com botão de exportação */}
        <View style={styles.footer}>
          <TouchableOpacity
            style={styles.exportSidebarBtn}
            onPress={() => {
              dispatch(setSidebarOpen(false));
              dispatch(setExportModalOpen(true));
            }}
            activeOpacity={0.8}
          >
            <Text style={styles.exportSidebarBtnText}>{t('sidebar.exportBtn', uiLanguage)}</Text>
          </TouchableOpacity>
        </View>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  overlay: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    zIndex: 1000,
    flexDirection: 'row',
  },
  backdrop: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(0,0,0,0.4)',
  },
  sidebar: {
    backgroundColor: '#2C1810',
    height: '100%',
    shadowColor: '#000',
    shadowOpacity: 0.3,
    shadowRadius: 20,
    shadowOffset: { width: 4, height: 0 },
    elevation: 10,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingTop: 22,
    paddingBottom: 14,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255,255,255,0.1)',
  },
  headerTitle: {
    fontSize: 19,
    fontWeight: 'bold',
    color: '#F5E6D0',
    letterSpacing: 0.4,
  },
  subtitle: {
    fontSize: 12,
    color: '#B8956A',
    marginTop: 2,
    fontStyle: 'italic',
  },
  closeBtn: {
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: 'rgba(255,255,255,0.1)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  closeBtnText: { color: '#E8D5B8', fontSize: 16 },
  scrollView: { flex: 1 },
  partSection: { marginTop: 4, marginBottom: 8 },
  chapterRow: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 12,
    paddingHorizontal: 18,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255,255,255,0.06)',
  },
  chapterRowActive: {
    backgroundColor: '#D4A574',
  },
  chapterBadge: {
    width: 28,
    height: 28,
    borderRadius: 14,
    backgroundColor: 'rgba(255,255,255,0.08)',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 12,
  },
  chapterBadgeActive: {
    backgroundColor: 'rgba(44,24,16,0.18)',
  },
  chapterNumber: {
    fontSize: 13,
    fontWeight: '700',
    color: '#D4A574',
    textAlign: 'center',
  },
  chapterTextColumn: {
    flex: 1,
  },
  chapterPali: {
    fontSize: 14,
    color: '#F5E6D0',
    fontWeight: '600',
    marginBottom: 2,
  },
  chapterTextActive: {
    color: '#2C1810',
    fontWeight: '700',
  },
  chapterTranslation: {
    fontSize: 12,
    color: '#B8956A',
    fontStyle: 'italic',
    lineHeight: 16,
  },
  chapterTranslationActive: {
    color: '#3D2218',
    fontWeight: '600',
  },
  footer: {
    paddingHorizontal: 16,
    paddingVertical: 14,
    borderTopWidth: 1,
    borderTopColor: 'rgba(255,255,255,0.08)',
    backgroundColor: '#24130C',
  },
  exportSidebarBtn: {
    backgroundColor: '#D4A574',
    paddingVertical: 12,
    paddingHorizontal: 16,
    borderRadius: 8,
    alignItems: 'center',
    justifyContent: 'center',
  },
  exportSidebarBtnText: {
    color: '#2C1810',
    fontSize: 14,
    fontWeight: '700',
  },
});

export default ChapterSidebar;

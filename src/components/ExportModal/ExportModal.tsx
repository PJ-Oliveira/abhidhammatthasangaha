// src/components/ExportModal/ExportModal.tsx
import React, { useState, useEffect } from 'react';
import {
  View,
  Modal,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  ActivityIndicator,
  Platform,
} from 'react-native';
import { Text } from '../ui/AppText';
import { useLayout } from '../../theme/layout';
import { useAppSelector, useAppDispatch } from '../../store/hooks';
import { setUiLanguage } from '../../store/slices/settingsSlice';
import {
  exportToEpub,
  exportToPdf,
  ExportConfig,
  ExportFormat,
  ExportMode,
} from '../../services/exportService';
import type { Language, UiLanguage } from '../../types/models';
import { t } from '../../i18n';

interface Props {
  visible: boolean;
  onClose: () => void;
}

export const ExportModal: React.FC<Props> = ({ visible, onClose }) => {
  const dispatch = useAppDispatch();
  const layout = useLayout();
  const currentChapterId = useAppSelector((s) => s.reading.currentChapterId);
  const uiLanguage = useAppSelector((s) => s.settings.uiLanguage);

  const [format, setFormat] = useState<ExportFormat>('epub');
  const [mode, setMode] = useState<ExportMode>('bilingual');
  const [targetLang, setTargetLang] = useState<'pt' | 'en' | 'es'>(uiLanguage);
  const [monoLang, setMonoLang] = useState<Language>('pali');
  const [scope, setScope] = useState<'all' | 'current'>('all');
  const [loading, setLoading] = useState(false);
  const [progressMsg, setProgressMsg] = useState('');

  useEffect(() => {
    setTargetLang(uiLanguage);
  }, [uiLanguage]);

  if (!visible) return null;

  const handleExport = async () => {
    setLoading(true);
    setProgressMsg(t('export.progressInit', uiLanguage));

    const languages: Language[] =
      mode === 'bilingual' ? ['pali', targetLang] : [monoLang];

    const config: ExportConfig = {
      format,
      mode,
      languages,
      scope,
      currentChapterId,
    };

    try {
      if (format === 'epub') {
        await exportToEpub(config, (_pct, msg) => {
          setProgressMsg(msg);
        });
      } else {
        await exportToPdf(config, (_pct, msg) => {
          setProgressMsg(msg);
        });
      }
      setTimeout(() => {
        setLoading(false);
        setProgressMsg('');
        onClose();
      }, 800);
    } catch (e) {
      console.error('Export failed:', e);
      setProgressMsg(t('export.progressError', uiLanguage));
      setLoading(false);
    }
  };

  return (
    <Modal
      transparent={true}
      visible={visible}
      animationType="fade"
      onRequestClose={onClose}
    >
      <View style={styles.overlay}>
        <View
          style={[
            styles.modalCard,
            {
              maxWidth: Math.min(layout.width - 28, 540),
              maxHeight: layout.height * 0.92,
            },
          ]}
        >
          {/* Header */}
          <View style={styles.header}>
            <View style={styles.headerTitleBlock}>
              <Text style={styles.title}>{t('export.title', uiLanguage)}</Text>
              <Text style={styles.subtitle} numberOfLines={1}>
                {t('export.subtitle', uiLanguage)}
              </Text>
            </View>

            <View style={styles.headerRightRow}>
              {/* Seletor dinâmico de idioma da interface dentro da própria janela */}
              <View style={styles.langSelectorRow}>
                {(['pt', 'en', 'es'] as const).map((lang) => (
                  <TouchableOpacity
                    key={lang}
                    style={[
                      styles.langChip,
                      uiLanguage === lang && styles.langChipActive,
                    ]}
                    onPress={() => dispatch(setUiLanguage(lang))}
                    accessibilityRole="button"
                    accessibilityLabel={`Mudar interface para ${lang.toUpperCase()}`}
                    {...(Platform.OS === 'web'
                      ? { onClick: () => dispatch(setUiLanguage(lang)) }
                      : {})}
                  >
                    <Text
                      style={[
                        styles.langChipText,
                        uiLanguage === lang && styles.langChipTextActive,
                      ]}
                    >
                      {lang.toUpperCase()}
                    </Text>
                  </TouchableOpacity>
                ))}
              </View>

              <TouchableOpacity
                style={styles.closeBtn}
                onPress={onClose}
                accessibilityRole="button"
                accessibilityLabel="Fechar"
                {...(Platform.OS === 'web' ? { onClick: onClose } : {})}
              >
                <Text style={styles.closeBtnText}>✕</Text>
              </TouchableOpacity>
            </View>
          </View>

          <ScrollView style={styles.body} showsVerticalScrollIndicator={false}>
            {/* 1. Escolha de Formato */}
            <Text style={styles.sectionTitle}>
              {t('export.secFormat', uiLanguage)}
            </Text>
            <View style={styles.optionsRow}>
              <TouchableOpacity
                style={[styles.chip, format === 'epub' && styles.chipActive]}
                onPress={() => setFormat('epub')}
                accessibilityRole="button"
                accessibilityLabel="chip-format-epub"
                {...(Platform.OS === 'web'
                  ? { onClick: () => setFormat('epub') }
                  : {})}
              >
                <Text
                  style={[
                    styles.chipText,
                    format === 'epub' && styles.chipTextActive,
                  ]}
                >
                  {t('export.epub', uiLanguage)}
                </Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.chip, format === 'pdf' && styles.chipActive]}
                onPress={() => setFormat('pdf')}
                accessibilityRole="button"
                accessibilityLabel="chip-format-pdf"
                {...(Platform.OS === 'web'
                  ? { onClick: () => setFormat('pdf') }
                  : {})}
              >
                <Text
                  style={[
                    styles.chipText,
                    format === 'pdf' && styles.chipTextActive,
                  ]}
                >
                  {t('export.pdf', uiLanguage)}
                </Text>
              </TouchableOpacity>
            </View>

            {/* 2. Escolha de Modo (Monolíngue ou Bilíngue) */}
            <Text style={styles.sectionTitle}>
              {t('export.secMode', uiLanguage)}
            </Text>
            <View style={styles.optionsRow}>
              <TouchableOpacity
                style={[styles.chip, mode === 'bilingual' && styles.chipActive]}
                onPress={() => setMode('bilingual')}
                accessibilityRole="button"
                accessibilityLabel="chip-mode-bilingual"
                {...(Platform.OS === 'web'
                  ? { onClick: () => setMode('bilingual') }
                  : {})}
              >
                <Text
                  style={[
                    styles.chipText,
                    mode === 'bilingual' && styles.chipTextActive,
                  ]}
                >
                  {t('export.bilingual', uiLanguage)}
                </Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.chip, mode === 'monolingual' && styles.chipActive]}
                onPress={() => setMode('monolingual')}
                accessibilityRole="button"
                accessibilityLabel="chip-mode-monolingual"
                {...(Platform.OS === 'web'
                  ? { onClick: () => setMode('monolingual') }
                  : {})}
              >
                <Text
                  style={[
                    styles.chipText,
                    mode === 'monolingual' && styles.chipTextActive,
                  ]}
                >
                  {t('export.monolingual', uiLanguage)}
                </Text>
              </TouchableOpacity>
            </View>

            {/* 3. Seleção de Idioma */}
            <Text style={styles.sectionTitle}>
              {t('export.secLang', uiLanguage)}
            </Text>
            {mode === 'bilingual' ? (
              <View style={styles.optionsRow}>
                <TouchableOpacity
                  style={[
                    styles.chipSmall,
                    targetLang === 'pt' && styles.chipActive,
                  ]}
                  onPress={() => setTargetLang('pt')}
                  {...(Platform.OS === 'web'
                    ? { onClick: () => setTargetLang('pt') }
                    : {})}
                >
                  <Text
                    style={[
                      styles.chipText,
                      targetLang === 'pt' && styles.chipTextActive,
                    ]}
                  >
                    Pāli + Português
                  </Text>
                </TouchableOpacity>
                <TouchableOpacity
                  style={[
                    styles.chipSmall,
                    targetLang === 'en' && styles.chipActive,
                  ]}
                  onPress={() => setTargetLang('en')}
                  {...(Platform.OS === 'web'
                    ? { onClick: () => setTargetLang('en') }
                    : {})}
                >
                  <Text
                    style={[
                      styles.chipText,
                      targetLang === 'en' && styles.chipTextActive,
                    ]}
                  >
                    Pāli + English
                  </Text>
                </TouchableOpacity>
                <TouchableOpacity
                  style={[
                    styles.chipSmall,
                    targetLang === 'es' && styles.chipActive,
                  ]}
                  onPress={() => setTargetLang('es')}
                  {...(Platform.OS === 'web'
                    ? { onClick: () => setTargetLang('es') }
                    : {})}
                >
                  <Text
                    style={[
                      styles.chipText,
                      targetLang === 'es' && styles.chipTextActive,
                    ]}
                  >
                    Pāli + Español
                  </Text>
                </TouchableOpacity>
              </View>
            ) : (
              <View style={styles.optionsRow}>
                <TouchableOpacity
                  style={[
                    styles.chipSmall,
                    monoLang === 'pali' && styles.chipActive,
                  ]}
                  onPress={() => setMonoLang('pali')}
                  {...(Platform.OS === 'web'
                    ? { onClick: () => setMonoLang('pali') }
                    : {})}
                >
                  <Text
                    style={[
                      styles.chipText,
                      monoLang === 'pali' && styles.chipTextActive,
                    ]}
                  >
                    Pāli
                  </Text>
                </TouchableOpacity>
                <TouchableOpacity
                  style={[
                    styles.chipSmall,
                    monoLang === 'pt' && styles.chipActive,
                  ]}
                  onPress={() => setMonoLang('pt')}
                  {...(Platform.OS === 'web'
                    ? { onClick: () => setMonoLang('pt') }
                    : {})}
                >
                  <Text
                    style={[
                      styles.chipText,
                      monoLang === 'pt' && styles.chipTextActive,
                    ]}
                  >
                    Português
                  </Text>
                </TouchableOpacity>
                <TouchableOpacity
                  style={[
                    styles.chipSmall,
                    monoLang === 'en' && styles.chipActive,
                  ]}
                  onPress={() => setMonoLang('en')}
                  {...(Platform.OS === 'web'
                    ? { onClick: () => setMonoLang('en') }
                    : {})}
                >
                  <Text
                    style={[
                      styles.chipText,
                      monoLang === 'en' && styles.chipTextActive,
                    ]}
                  >
                    English
                  </Text>
                </TouchableOpacity>
                <TouchableOpacity
                  style={[
                    styles.chipSmall,
                    monoLang === 'es' && styles.chipActive,
                  ]}
                  onPress={() => setMonoLang('es')}
                  {...(Platform.OS === 'web'
                    ? { onClick: () => setMonoLang('es') }
                    : {})}
                >
                  <Text
                    style={[
                      styles.chipText,
                      monoLang === 'es' && styles.chipTextActive,
                    ]}
                  >
                    Español
                  </Text>
                </TouchableOpacity>
              </View>
            )}

            {/* 4. Escopo */}
            <Text style={styles.sectionTitle}>
              {t('export.secScope', uiLanguage)}
            </Text>
            <View style={styles.optionsRow}>
              <TouchableOpacity
                style={[styles.chip, scope === 'all' && styles.chipActive]}
                onPress={() => setScope('all')}
                {...(Platform.OS === 'web'
                  ? { onClick: () => setScope('all') }
                  : {})}
              >
                <Text
                  style={[
                    styles.chipText,
                    scope === 'all' && styles.chipTextActive,
                  ]}
                >
                  {t('export.scopeAll', uiLanguage)}
                </Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.chip, scope === 'current' && styles.chipActive]}
                onPress={() => setScope('current')}
                {...(Platform.OS === 'web'
                  ? { onClick: () => setScope('current') }
                  : {})}
              >
                <Text
                  style={[
                    styles.chipText,
                    scope === 'current' && styles.chipTextActive,
                  ]}
                >
                  {t('export.scopeCurrent', uiLanguage)}
                </Text>
              </TouchableOpacity>
            </View>

            {/* Recursos incluídos */}
            <View style={styles.featuresBox}>
              <Text style={styles.featureItem}>
                {t('export.featDict', uiLanguage)}
              </Text>
              <Text style={styles.featureItem}>
                {t('export.featLinks', uiLanguage)}
              </Text>
              <Text style={styles.featureItem}>
                {t('export.featNoBreak', uiLanguage)}
              </Text>
              <Text style={styles.featureItem}>
                {t('export.featToc', uiLanguage)}
              </Text>
              <Text style={styles.featureItem}>
                {t('export.featType', uiLanguage)}
              </Text>
              <Text style={styles.featureItem}>
                {t('export.featPages', uiLanguage)}
              </Text>
            </View>

            {/* Feedback / Progresso */}
            {loading && (
              <View style={styles.loadingContainer}>
                <ActivityIndicator size="small" color="#4B2E2A" />
                <Text style={styles.loadingText}>{progressMsg}</Text>
              </View>
            )}
          </ScrollView>

          {/* Botão de Ação */}
          <View style={styles.footer}>
            <TouchableOpacity
              style={[styles.exportBtn, loading && styles.exportBtnDisabled]}
              onPress={handleExport}
              {...(Platform.OS === 'web' ? { onClick: handleExport } : {})}
              disabled={loading}
              accessibilityRole="button"
              accessibilityLabel="btn-generate-export"
              activeOpacity={0.8}
            >
              <Text style={styles.exportBtnText}>
                {loading
                  ? t('export.compiling', uiLanguage)
                  : format === 'pdf'
                  ? t('export.btnPdf', uiLanguage)
                  : t('export.btnEpub', uiLanguage)}
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
    backgroundColor: 'rgba(0,0,0,0.5)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
  modalCard: {
    width: '100%',
    backgroundColor: '#FAF5E4',
    borderRadius: 16,
    padding: 24,
    shadowColor: '#000',
    shadowOpacity: 0.25,
    shadowRadius: 20,
    shadowOffset: { width: 0, height: 8 },
    elevation: 20,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderBottomWidth: 1,
    borderBottomColor: '#E8DCC8',
    paddingBottom: 14,
    marginBottom: 14,
  },
  headerTitleBlock: {
    flex: 1,
    paddingRight: 8,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#4B2E2A',
  },
  subtitle: {
    fontSize: 12,
    color: '#8B7355',
    fontStyle: 'italic',
    marginTop: 2,
  },
  headerRightRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  langSelectorRow: {
    flexDirection: 'row',
    backgroundColor: '#E8DCC8',
    borderRadius: 14,
    padding: 2,
  },
  langChip: {
    paddingHorizontal: 7,
    paddingVertical: 3,
    borderRadius: 12,
  },
  langChipActive: {
    backgroundColor: '#4B2E2A',
  },
  langChipText: {
    fontSize: 11,
    color: '#4B2E2A',
    fontWeight: '700',
  },
  langChipTextActive: {
    color: '#FAF5E4',
  },
  closeBtn: {
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: '#E8DCC8',
    alignItems: 'center',
    justifyContent: 'center',
  },
  closeBtnText: {
    fontSize: 16,
    color: '#4B2E2A',
    fontWeight: 'bold',
  },
  body: {
    maxHeight: 460,
  },
  sectionTitle: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#4B2E2A',
    marginTop: 12,
    marginBottom: 8,
  },
  optionsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
    marginBottom: 6,
  },
  chip: {
    flex: 1,
    minWidth: 140,
    backgroundColor: '#E8DCC8',
    paddingVertical: 10,
    paddingHorizontal: 12,
    borderRadius: 8,
    alignItems: 'center',
    justifyContent: 'center',
  },
  chipSmall: {
    backgroundColor: '#E8DCC8',
    paddingVertical: 8,
    paddingHorizontal: 12,
    borderRadius: 8,
    alignItems: 'center',
    justifyContent: 'center',
  },
  chipActive: {
    backgroundColor: '#4B2E2A',
  },
  chipText: {
    color: '#4B2E2A',
    fontSize: 13,
    fontWeight: '600',
  },
  chipTextActive: {
    color: '#FAF5E4',
  },
  featuresBox: {
    backgroundColor: '#F3ECD8',
    borderRadius: 8,
    padding: 12,
    marginTop: 12,
    gap: 6,
  },
  featureItem: {
    fontSize: 12,
    color: '#6E563B',
    lineHeight: 18,
  },
  loadingContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    paddingVertical: 10,
  },
  loadingText: {
    fontSize: 13,
    color: '#4B2E2A',
    fontStyle: 'italic',
  },
  footer: {
    marginTop: 14,
    borderTopWidth: 1,
    borderTopColor: '#F0E8D8',
    paddingTop: 12,
  },
  exportBtn: {
    backgroundColor: '#4B2E2A',
    paddingVertical: 14,
    borderRadius: 8,
    alignItems: 'center',
    justifyContent: 'center',
  },
  exportBtnDisabled: {
    opacity: 0.6,
  },
  exportBtnText: {
    color: '#FAF5E4',
    fontSize: 15,
    fontWeight: 'bold',
  },
});

export default ExportModal;

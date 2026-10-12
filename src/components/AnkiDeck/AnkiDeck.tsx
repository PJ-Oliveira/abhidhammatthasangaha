// src/components/AnkiDeck/AnkiDeck.tsx
import React, { useState, useEffect, useMemo, useCallback } from 'react';
import {
  View,
  TouchableOpacity,
  ScrollView,
  StyleSheet,
  Platform,
  Alert,
  StyleProp,
  ViewStyle,
  TextStyle,
} from 'react-native';
import { Text, TextInput } from '../ui/AppText';
import { ANKI_CARDS, AnkiCard, Language } from '../../data/ankiCards';
import { useAppSelector, useAppDispatch } from '../../store/hooks';
import { setUiLanguage } from '../../store/slices/settingsSlice';
import { useLayout } from '../../theme/layout';

interface SRSItem {
  id: string;
  interval: number;
  reps: number;
  easeFactor: number;
  dueDate: string;
  lastReviewed?: string;
  mastered: boolean;
}

type SRSState = Record<string, SRSItem>;

type CardCategory = AnkiCard['category'] | 'all';

const STORAGE_KEY = 'abhidhamma_anki_srs_v2';

export const AnkiDeck: React.FC = () => {
  const dispatch = useAppDispatch();
  const reduxUiLanguage = useAppSelector((s) => s.settings.uiLanguage);
  const layout = useLayout();

  // Local language synced with Redux UI language
  const [lang, setLang] = useState<Language>(reduxUiLanguage);

  useEffect(() => {
    if (reduxUiLanguage !== lang) {
      setLang(reduxUiLanguage);
    }
  }, [reduxUiLanguage]);

  const handleSetLang = (newLang: Language) => {
    setLang(newLang);
    dispatch(setUiLanguage(newLang));
  };

  const [mode, setMode] = useState<'study' | 'exam' | 'browser' | 'export'>('study');

  // Filters
  const [selectedChapter, setSelectedChapter] = useState<number | 'all'>('all');
  const [selectedCategory, setSelectedCategory] = useState<CardCategory>('all');
  const [searchQuery, setSearchQuery] = useState<string>('');

  // Study card state
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [isFlipped, setIsFlipped] = useState<boolean>(false);

  // SRS state
  const [srsState, setSrsState] = useState<SRSState>(() => {
    if (Platform.OS === 'web' && typeof window !== 'undefined' && window.localStorage) {
      try {
        const saved = window.localStorage.getItem(STORAGE_KEY);
        return saved ? JSON.parse(saved) : {};
      } catch {
        return {};
      }
    }
    return {};
  });

  useEffect(() => {
    if (Platform.OS === 'web' && typeof window !== 'undefined' && window.localStorage) {
      try {
        window.localStorage.setItem(STORAGE_KEY, JSON.stringify(srsState));
      } catch (e) {
        console.error('Failed to save SRS state', e);
      }
    }
  }, [srsState]);

  // Exam state — stores optionCards (AnkiCard[]) so switching language mid-exam dynamically translates options!
  const [examStarted, setExamStarted] = useState<boolean>(false);
  const [examQuestions, setExamQuestions] = useState<Array<{
    card: AnkiCard;
    optionCards: AnkiCard[];
    correctIndex: number;
  }>>([]);
  const [examAnswers, setExamAnswers] = useState<Record<number, number>>({});
  const [examSubmitted, setExamSubmitted] = useState<boolean>(false);

  // Filter cards
  const filteredCards = useMemo(() => {
    return ANKI_CARDS.filter((card) => {
      if (selectedChapter !== 'all' && card.chapter !== selectedChapter) return false;
      if (selectedCategory !== 'all' && card.category !== selectedCategory) return false;
      if (searchQuery.trim() !== '') {
        const query = searchQuery.toLowerCase();
        const content = card[lang];
        const inQuestion = content.question.toLowerCase().includes(query);
        const inAnswer = content.answer.toLowerCase().includes(query);
        const inPali = card.paliTerm.toLowerCase().includes(query);
        const inSection = card.section.toLowerCase().includes(query);
        const inTags = card.tags.some((tag) => tag.toLowerCase().includes(query));
        return inQuestion || inAnswer || inPali || inSection || inTags;
      }
      return true;
    });
  }, [selectedChapter, selectedCategory, searchQuery, lang]);

  const currentCard: AnkiCard | undefined = filteredCards[currentIndex];

  useEffect(() => {
    setCurrentIndex(0);
    setIsFlipped(false);
  }, [selectedChapter, selectedCategory, searchQuery]);

  const handleNextCard = useCallback(() => {
    if (currentIndex < filteredCards.length - 1) {
      setCurrentIndex((i) => i + 1);
      setIsFlipped(false);
    }
  }, [currentIndex, filteredCards.length]);

  const handlePrevCard = useCallback(() => {
    if (currentIndex > 0) {
      setCurrentIndex((i) => i - 1);
      setIsFlipped(false);
    }
  }, [currentIndex]);

  // SM-2 Spaced Repetition Rating
  const handleRate = useCallback((rating: 'again' | 'hard' | 'good' | 'easy') => {
    if (!currentCard) return;
    const id = currentCard.id;
    const currentItem: SRSItem = srsState[id] || {
      id,
      interval: 0,
      reps: 0,
      easeFactor: 2.5,
      dueDate: new Date().toISOString(),
      mastered: false,
    };

    let newInterval = 1;
    let newEase = currentItem.easeFactor;
    let newReps = currentItem.reps;
    let mastered = currentItem.mastered;

    switch (rating) {
      case 'again':
        newInterval = 1;
        newReps = 0;
        newEase = Math.max(1.3, newEase - 0.2);
        mastered = false;
        break;
      case 'hard':
        newInterval = Math.max(1, Math.round(currentItem.interval * 1.2));
        newEase = Math.max(1.3, newEase - 0.15);
        newReps += 1;
        break;
      case 'good':
        if (currentItem.reps === 0) newInterval = 1;
        else if (currentItem.reps === 1) newInterval = 6;
        else newInterval = Math.round(currentItem.interval * newEase);
        newReps += 1;
        if (newReps >= 3) mastered = true;
        break;
      case 'easy':
        if (currentItem.reps === 0) newInterval = 4;
        else if (currentItem.reps === 1) newInterval = 10;
        else newInterval = Math.round(currentItem.interval * newEase * 1.3);
        newEase = newEase + 0.15;
        newReps += 1;
        mastered = true;
        break;
    }

    const nextDue = new Date();
    nextDue.setDate(nextDue.getDate() + newInterval);

    setSrsState((curr) => ({
      ...curr,
      [id]: {
        id,
        interval: newInterval,
        reps: newReps,
        easeFactor: newEase,
        dueDate: nextDue.toISOString(),
        lastReviewed: new Date().toISOString(),
        mastered,
      },
    }));

    // Advance to next card, or wrap around to 0 if on the last card, and always reset flip state
    setIsFlipped(false);
    if (filteredCards.length > 0) {
      setCurrentIndex((i) => (i < filteredCards.length - 1 ? i + 1 : 0));
    }
  }, [currentCard, srsState, filteredCards.length]);

  // Keyboard navigation on Web
  useEffect(() => {
    if (Platform.OS !== 'web' || typeof window === 'undefined') return;

    const handleKeyDown = (e: KeyboardEvent) => {
      if (mode !== 'study') return;
      if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) return;

      if (e.code === 'Space' || e.key === ' ') {
        e.preventDefault();
        setIsFlipped((f) => !f);
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        handleNextCard();
      } else if (e.key === 'ArrowLeft') {
        e.preventDefault();
        handlePrevCard();
      } else if (isFlipped) {
        if (e.key === '1') handleRate('again');
        else if (e.key === '2') handleRate('hard');
        else if (e.key === '3') handleRate('good');
        else if (e.key === '4') handleRate('easy');
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [mode, isFlipped, handleNextCard, handlePrevCard, handleRate]);

  // Exam Generator — prioritizes same-chapter / same-category distractors for rigorous testing
  const startExam = (questionCount: number = 20) => {
    const sourcePool = filteredCards.length >= 4 ? [...filteredCards] : [...ANKI_CARDS];
    for (let i = sourcePool.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [sourcePool[i], sourcePool[j]] = [sourcePool[j], sourcePool[i]];
    }

    const selected = sourcePool.slice(0, Math.min(questionCount, sourcePool.length));
    const generated = selected.map((card) => {
      const otherCards = ANKI_CARDS.filter((c) => c.id !== card.id);
      const sameChapterOrCategory = otherCards.filter(
        (c) => c.chapter === card.chapter || c.category === card.category
      );
      const remainingOthers = otherCards.filter(
        (c) => c.chapter !== card.chapter && c.category !== card.category
      );

      const shuffledRelated = [...sameChapterOrCategory].sort(() => Math.random() - 0.5);
      const shuffledRemaining = [...remainingOthers].sort(() => Math.random() - 0.5);
      const distractorCards = [...shuffledRelated, ...shuffledRemaining].slice(0, 3);

      const optionCards = [card, ...distractorCards].sort(() => Math.random() - 0.5);
      const correctIndex = optionCards.findIndex((c) => c.id === card.id);

      return {
        card,
        optionCards,
        correctIndex,
      };
    });

    setExamQuestions(generated);
    setExamAnswers({});
    setExamSubmitted(false);
    setExamStarted(true);
  };

  const handleExamOptionSelect = (qIdx: number, optIdx: number) => {
    if (examSubmitted) return;
    setExamAnswers((prev) => ({
      ...prev,
      [qIdx]: optIdx,
    }));
  };

  const calculateExamScore = () => {
    if (examQuestions.length === 0) return 0;
    let correct = 0;
    examQuestions.forEach((q, idx) => {
      if (examAnswers[idx] === q.correctIndex) {
        correct++;
      }
    });
    return Math.round((correct / examQuestions.length) * 100);
  };

  const t = {
    pt: {
      title: 'Anki • Memorização & Simulado 100',
      subtitle: 'Estruturas, Relações e Conceitos Filosóficos do Abhidhammatthasaṅgaha',
      studyTab: '🎴 Estudo SRS',
      examTab: '💯 Simulado Prova 100',
      browserTab: '🔍 Navegador de Cards',
      exportTab: '📥 Exportar Anki',
      allChapters: 'Todos os 9 Capítulos',
      chapterPrefix: 'Cap.',
      chapterFull: 'Capítulo',
      allCategories: 'Todas as Categorias',
      cat_quantities: '🔢 Quantidades',
      cat_structures: '🏛️ Estruturas',
      cat_relations: '🔗 Relações',
      cat_philosophy: '☸️ Filosofia',
      cat_exam_traps: '⚠️ Pegadinhas de Prova',
      emptyFilter: 'Nenhum card encontrado para o filtro selecionado.',
      prevBtn: '◀ Anterior',
      nextBtn: 'Próximo ▶',
      listenBtn: '🔊 Ouvir',
      formatLabel: 'Formato:',
      breakdownLabel: '📋 Estrutura & Classificação:',
      foundationLabel: '📖 Fundamento:',
      ratingPrompt: 'Avalie para agendamento de repetição (SRS):',
      flipPrompt: 'Clique ou pressione Espaço para virar',
      showAnswer: 'Mostrar Resposta (Espaço)',
      again: 'Repetir (1)',
      hard: 'Difícil (2)',
      good: 'Bom (3)',
      easy: 'Fácil (4)',
      mnemonicTip: '💡 Dica de Prova & Mnemônica',
      cardProgress: 'Card',
      of: 'de',
      mastery: 'Taxa de Domínio',
      reviewed: 'Revisados',
      startExam: 'Iniciar Simulado Prova 100',
      examDesc: 'Simulador autêntico com questões de múltipla escolha para testar sua retenção de 0 a 100%.',
      exam10Btn: '📝 10 Questões Rápidas',
      exam20Btn: '🏆 20 Questões (Padrão)',
      examFullBtn: '📚 Simulado Completo',
      examInProgress: 'Simulado em Andamento:',
      answeredLabel: 'respondidas',
      restartBtn: 'Recomeçar',
      questionLabel: 'Questão',
      correctLabel: '✅ Correto!',
      incorrectLabel: '❌ Incorreto!',
      examTipPrefix: 'Dica de Prova:',
      submitExam: 'Finalizar e Corrigir Exame',
      examResult: 'Resultado do Exame',
      score: 'Nota Final',
      perfectScore: '🏆 100% NOTA MÁXIMA! Domínio absoluto do Abhidhammatthasaṅgaha!',
      highScore: '🥇 NÍVEL DE EXCELÊNCIA! Quase 100. Revise as questões abaixo para gabaritar!',
      passScore: '🥈 APROVADO! Revise os cartões marcados para alcançar 100%.',
      failScore: '📖 CONTINUE ESTUDANDO! Revise os flashcards no modo SRS para atingir a nota máxima.',
      searchPlaceholder: 'Pesquisar cards (termo Pāḷi, conceito, pergunta)...',
      cardsFound: 'cards encontrados',
      studyThisCard: '🎴 Estudar Card',
      exportTitle: 'Exportar para o Aplicativo Anki Oficial',
      exportDesc: 'Baixe o baralho completo com 63 cards formatados com HTML, termos em Pāḷi e dicas.',
      downloadBtn: 'Baixar Baralho Anki (.txt / TSV)',
      exportAlertTitle: 'Exportação',
      exportAlertMsg: 'Exportação concluída. Arquivo pronto para importação no Anki.',
    },
    en: {
      title: 'Anki • Memorization & 100-Point Exam',
      subtitle: 'Structures, Relations and Philosophical Concepts of Abhidhammatthasaṅgaha',
      studyTab: '🎴 SRS Study',
      examTab: '💯 100-Score Exam',
      browserTab: '🔍 Deck Browser',
      exportTab: '📥 Export Anki',
      allChapters: 'All 9 Chapters',
      chapterPrefix: 'Ch.',
      chapterFull: 'Chapter',
      allCategories: 'All Categories',
      cat_quantities: '🔢 Quantities',
      cat_structures: '🏛️ Structures',
      cat_relations: '🔗 Relations',
      cat_philosophy: '☸️ Philosophy',
      cat_exam_traps: '⚠️ Exam Traps',
      emptyFilter: 'No cards found for the selected filter.',
      prevBtn: '◀ Previous',
      nextBtn: 'Next ▶',
      listenBtn: '🔊 Listen',
      formatLabel: 'Format:',
      breakdownLabel: '📋 Structure & Classification:',
      foundationLabel: '📖 Foundation:',
      ratingPrompt: 'Rate recall for Spaced Repetition (SRS):',
      flipPrompt: 'Click or press Space to flip',
      showAnswer: 'Show Answer (Space)',
      again: 'Again (1)',
      hard: 'Hard (2)',
      good: 'Good (3)',
      easy: 'Easy (4)',
      mnemonicTip: '💡 Exam Tip & Mnemonic',
      cardProgress: 'Card',
      of: 'of',
      mastery: 'Mastery Rate',
      reviewed: 'Reviewed',
      startExam: 'Start 100-Score Practice Exam',
      examDesc: 'Authentic exam simulation testing full conceptual, quantitative, and relational mastery.',
      exam10Btn: '📝 10 Quick Questions',
      exam20Btn: '🏆 20 Questions (Standard)',
      examFullBtn: '📚 Full Exam',
      examInProgress: 'Exam in Progress:',
      answeredLabel: 'answered',
      restartBtn: 'Restart',
      questionLabel: 'Question',
      correctLabel: '✅ Correct!',
      incorrectLabel: '❌ Incorrect!',
      examTipPrefix: 'Exam Tip:',
      submitExam: 'Submit & Grade Exam',
      examResult: 'Your Exam Result',
      score: 'Final Score',
      perfectScore: '🏆 100% PERFECT SCORE! Absolute mastery of the Abhidhammatthasaṅgaha!',
      highScore: '🥇 EXCELLENCE LEVEL! Review missed items below to get 100%.',
      passScore: '🥈 PASSED! Review missed flashcards to achieve 100%.',
      failScore: '📖 KEEP STUDYING! Review flashcards in SRS mode to reach the maximum score.',
      searchPlaceholder: 'Search cards (Pāḷi term, concept, question)...',
      cardsFound: 'cards found',
      studyThisCard: '🎴 Study Card',
      exportTitle: 'Export to Official Anki App',
      exportDesc: 'Download formatted deck ready for 1-click import into Anki Desktop or Mobile.',
      downloadBtn: 'Download Anki Deck (.txt / TSV)',
      exportAlertTitle: 'Export',
      exportAlertMsg: 'Export complete. File ready for import into Anki.',
    },
    es: {
      title: 'Anki • Memorización y Simulado 100',
      subtitle: 'Estructuras, Relaciones y Conceptos Filosóficos del Abhidhammatthasaṅgaha',
      studyTab: '🎴 Estudio SRS',
      examTab: '💯 Simulado Examen 100',
      browserTab: '🔍 Explorador de Tarjetas',
      exportTab: '📥 Exportar Anki',
      allChapters: 'Los 9 Capítulos',
      chapterPrefix: 'Cap.',
      chapterFull: 'Capítulo',
      allCategories: 'Todas las Categorías',
      cat_quantities: '🔢 Cantidades',
      cat_structures: '🏛️ Estructuras',
      cat_relations: '🔗 Relaciones',
      cat_philosophy: '☸️ Filosofía',
      cat_exam_traps: '⚠️ Trampas de Examen',
      emptyFilter: 'No se encontraron tarjetas para el filtro seleccionado.',
      prevBtn: '◀ Anterior',
      nextBtn: 'Siguiente ▶',
      listenBtn: '🔊 Escuchar',
      formatLabel: 'Formato:',
      breakdownLabel: '📋 Estructura y Clasificación:',
      foundationLabel: '📖 Fundamento:',
      ratingPrompt: 'Califica tu recuerdo para Repetición Espaciada (SRS):',
      flipPrompt: 'Haz clic o presiona Espacio para voltear',
      showAnswer: 'Mostrar Respuesta (Espacio)',
      again: 'Otra vez (1)',
      hard: 'Difícil (2)',
      good: 'Bien (3)',
      easy: 'Fácil (4)',
      mnemonicTip: '💡 Consejo de Examen y Mnemónico',
      cardProgress: 'Tarjeta',
      of: 'de',
      mastery: 'Tasa de Dominio',
      reviewed: 'Repasadas',
      startExam: 'Iniciar Simulado para Sacar 100',
      examDesc: 'Simulador riguroso diseñado para certificar que obtendrás una nota de 100.',
      exam10Btn: '📝 10 Preguntas Rápidas',
      exam20Btn: '🏆 20 Preguntas (Estándar)',
      examFullBtn: '📚 Examen Completo',
      examInProgress: 'Examen en Curso:',
      answeredLabel: 'respondidas',
      restartBtn: 'Reiniciar',
      questionLabel: 'Pregunta',
      correctLabel: '✅ ¡Correcto!',
      incorrectLabel: '❌ ¡Incorrecto!',
      examTipPrefix: 'Consejo de Examen:',
      submitExam: 'Finalizar y Calificar Examen',
      examResult: 'Resultado de tu Examen',
      score: 'Calificación Final',
      perfectScore: '🏆 ¡FELICITACIONES! ¡SACASTE 100! ¡Dominio absoluto!',
      highScore: '🥇 ¡NIVEL DE EXCELENCIA! Casi 100. Repasa los detalles a continuación.',
      passScore: '🥈 ¡APROBADO! Repasa las tarjetas erradas para lograr el 100.',
      failScore: '📖 ¡SIGUE PRACTICANDO! Repasa los flashcards para alcanzar la nota máxima.',
      searchPlaceholder: 'Buscar tarjetas (término Pāḷi, concepto, pregunta)...',
      cardsFound: 'tarjetas encontradas',
      studyThisCard: '🎴 Estudiar Tarjeta',
      exportTitle: 'Exportar a la Aplicación Anki Oficial',
      exportDesc: 'Descarga el mazo formateado para Anki Desktop, AnkiMobile o AnkiDroid.',
      downloadBtn: 'Descargar Mazo Anki (.txt / TSV)',
      exportAlertTitle: 'Exportación',
      exportAlertMsg: 'Exportación completada. Archivo listo para importar en Anki.',
    },
  }[lang];

  // Export to Anki TSV
  const handleExportAnki = () => {
    const header = '#separator:tab\n#html:true\n#tags column:5\n';
    const rows = ANKI_CARDS.map((c) => {
      const content = c[lang];
      const front = `<b>[${t.chapterPrefix} ${c.chapter} - ${c.chapterName[lang]}]</b><br/><span style="color:#b45309;font-size:1.2em;">${c.paliTerm}</span><br/><br/><b>${content.question}</b><br/><small style="color:#64748b;">${c.section} | ${content.examQuestionType}</small>`;
      const breakdownHtml = content.breakdown.length > 0 ? `<ul>${content.breakdown.map(b => `<li>${b}</li>`).join('')}</ul>` : '';
      const back = `<b>${content.answer}</b><br/><br/>${breakdownHtml}<br/><i>${content.explanation}</i><br/><br/><div style="background:#f0fdf4;padding:8px;border-left:4px solid #16a34a;"><b>${t.examTipPrefix}</b> ${content.mnemonicOrExamTip}</div>`;
      const tags = `Abhidhamma Pariccheda_${c.chapter} ${c.category}`;
      return `${front.replace(/\t/g, ' ')}\t${back.replace(/\t/g, ' ')}\t${c.chapter}\t${c.paliTerm}\t${tags}`;
    });

    const fileContent = header + rows.join('\n');
    if (Platform.OS === 'web' && typeof window !== 'undefined' && typeof document !== 'undefined') {
      const blob = new Blob([fileContent], { type: 'text/tab-separated-values;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', `Abhidhammatthasangaha_Anki_${lang.toUpperCase()}.txt`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
    } else {
      Alert.alert(t.exportAlertTitle, t.exportAlertMsg);
    }
  };

  // Stats
  const totalReviewed = Object.keys(srsState).length;
  const totalMastered = Object.values(srsState).filter((s) => s.mastered).length;
  const masteryPercentage = Math.round((totalMastered / ANKI_CARDS.length) * 100);

  const categories: Array<{ key: CardCategory; label: string }> = [
    { key: 'all', label: t.allCategories },
    { key: 'quantities', label: t.cat_quantities },
    { key: 'structures', label: t.cat_structures },
    { key: 'relations', label: t.cat_relations },
    { key: 'philosophy', label: t.cat_philosophy },
    { key: 'exam_traps', label: t.cat_exam_traps },
  ];

  const handleJumpToCardInStudy = (cardId: string) => {
    const idx = filteredCards.findIndex((c) => c.id === cardId);
    if (idx >= 0) {
      setCurrentIndex(idx);
      setIsFlipped(false);
      setMode('study');
    }
  };

  const renderFilterRows = () => (
    <View style={styles.filterBar}>
      <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.filterScroll}>
        <TouchableOpacity
          style={[styles.filterChip, selectedChapter === 'all' && styles.filterChipActive]}
          onPress={() => setSelectedChapter('all')}
        >
          <Text style={[styles.filterChipText, selectedChapter === 'all' && styles.filterChipTextActive]}>
            {t.allChapters}
          </Text>
        </TouchableOpacity>
        {[1, 2, 3, 4, 5, 6, 7, 8, 9].map((ch) => (
          <TouchableOpacity
            key={ch}
            style={[styles.filterChip, selectedChapter === ch && styles.filterChipActive]}
            onPress={() => setSelectedChapter(ch)}
          >
            <Text style={[styles.filterChipText, selectedChapter === ch && styles.filterChipTextActive]}>
              {t.chapterPrefix} {ch}
            </Text>
          </TouchableOpacity>
        ))}
      </ScrollView>

      <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={[styles.filterScroll, { marginTop: 6 }]}>
        {categories.map((cat) => (
          <TouchableOpacity
            key={cat.key}
            style={[styles.filterChipSecondary, selectedCategory === cat.key && styles.filterChipSecondaryActive]}
            onPress={() => setSelectedCategory(cat.key)}
          >
            <Text style={[styles.filterChipText, selectedCategory === cat.key && styles.filterChipTextActive]}>
              {cat.label}
            </Text>
          </TouchableOpacity>
        ))}
      </ScrollView>
    </View>
  );

  return (
    <ScrollView style={styles.container} contentContainerStyle={[styles.contentContainer, { paddingHorizontal: layout.pagePadding }]}>
      {/* Banner */}
      <View style={styles.banner}>
        <View style={styles.bannerHeader}>
          <View style={{ flex: 1, minWidth: 200 }}>
            <View style={{ flexDirection: 'row', alignItems: 'center', marginBottom: 4 }}>
              <Text style={{ fontSize: 24, marginRight: 8 }}>☸️</Text>
              <Text style={styles.bannerTitle}>{t.title}</Text>
            </View>
            <Text style={styles.bannerSubtitle}>{t.subtitle}</Text>
          </View>

          {/* Lang Selector */}
          <View style={styles.langSelector}>
            {(['pt', 'en', 'es'] as Language[]).map((l) => (
              <TouchableOpacity
                key={l}
                style={[styles.langBtn, lang === l && styles.langBtnActive]}
                onPress={() => handleSetLang(l)}
              >
                <Text style={[styles.langBtnText, lang === l && styles.langBtnTextActive]}>
                  {l.toUpperCase()}
                </Text>
              </TouchableOpacity>
            ))}
          </View>
        </View>

        {/* Stats */}
        <View style={styles.statsRow}>
          <Text style={styles.statText}>
            Cards: <Text style={styles.statBold}>{ANKI_CARDS.length}</Text>
          </Text>
          <Text style={styles.statText}>
            {t.reviewed}: <Text style={styles.statBold}>{totalReviewed}</Text>
          </Text>
          <Text style={styles.statText}>
            {t.mastery}: <Text style={styles.statGold}>{masteryPercentage}%</Text> ({totalMastered})
          </Text>
        </View>
      </View>

      {/* Mode Tabs */}
      <View style={styles.modeTabBar}>
        <TouchableOpacity
          style={[styles.modeTab, mode === 'study' && styles.modeTabActive]}
          onPress={() => setMode('study')}
        >
          <Text style={[styles.modeTabText, mode === 'study' && styles.modeTabTextActive]}>
            {t.studyTab}
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.modeTab, mode === 'exam' && styles.modeTabActive]}
          onPress={() => setMode('exam')}
        >
          <Text style={[styles.modeTabText, mode === 'exam' && styles.modeTabTextActive]}>
            {t.examTab}
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.modeTab, mode === 'browser' && styles.modeTabActive]}
          onPress={() => setMode('browser')}
        >
          <Text style={[styles.modeTabText, mode === 'browser' && styles.modeTabTextActive]}>
            {t.browserTab}
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.modeTab, mode === 'export' && styles.modeTabActive]}
          onPress={() => setMode('export')}
        >
          <Text style={[styles.modeTabText, mode === 'export' && styles.modeTabTextActive]}>
            {t.exportTab}
          </Text>
        </TouchableOpacity>
      </View>

      {/* STUDY MODE */}
      {mode === 'study' && (
        <View>
          {renderFilterRows()}

          {filteredCards.length === 0 ? (
            <View style={styles.emptyState}>
              <Text style={styles.emptyText}>{t.emptyFilter}</Text>
            </View>
          ) : currentCard && (
            <View>
              {/* Counter & Nav */}
              <View style={styles.navRow}>
                <Text style={styles.counterText}>
                  {t.cardProgress} {currentIndex + 1} {t.of} {filteredCards.length}
                </Text>
                <View style={{ flexDirection: 'row', gap: 8 }}>
                  <TouchableOpacity
                    style={[styles.smallBtn, currentIndex === 0 && styles.smallBtnDisabled]}
                    onPress={handlePrevCard}
                    disabled={currentIndex === 0}
                  >
                    <Text style={styles.smallBtnText}>{t.prevBtn}</Text>
                  </TouchableOpacity>
                  <TouchableOpacity
                    style={[styles.smallBtn, currentIndex === filteredCards.length - 1 && styles.smallBtnDisabled]}
                    onPress={handleNextCard}
                    disabled={currentIndex === filteredCards.length - 1}
                  >
                    <Text style={styles.smallBtnText}>{t.nextBtn}</Text>
                  </TouchableOpacity>
                </View>
              </View>

              {/* CARD BOX */}
              <TouchableOpacity
                activeOpacity={0.95}
                onPress={() => setIsFlipped((f) => !f)}
                style={styles.cardBox}
              >
                {/* Badges */}
                <View style={styles.badgeRow}>
                  <View style={styles.badgeChapter}>
                    <Text style={styles.badgeChapterText}>
                      {currentCard.chapterName[lang]} ({currentCard.chapterName.pali})
                    </Text>
                  </View>
                  <View style={styles.badgeSection}>
                    <Text style={styles.badgeSectionText}>{currentCard[lang].examQuestionType}</Text>
                  </View>
                </View>

                {/* FRONT */}
                <View style={styles.frontContent}>
                  <Text style={styles.paliTerm}>{currentCard.paliTerm}</Text>
                  <Text style={styles.questionText}>{currentCard[lang].question}</Text>
                  <Text style={styles.examTypeText}>
                    {t.formatLabel} {currentCard[lang].examQuestionType}
                  </Text>
                </View>

                {/* BACK (Revealed) */}
                {isFlipped && (
                  <View style={styles.backContent}>
                    <View style={styles.answerBox}>
                      <Text style={styles.answerText}>{currentCard[lang].answer}</Text>
                    </View>

                    {currentCard[lang].breakdown.length > 0 && (
                      <View style={{ marginBottom: 14 }}>
                        <Text style={styles.breakdownTitle}>{t.breakdownLabel}</Text>
                        {currentCard[lang].breakdown.map((item, idx) => (
                          <View key={idx} style={styles.breakdownItem}>
                            <Text style={styles.bullet}>•</Text>
                            <Text style={styles.breakdownText}>{item}</Text>
                          </View>
                        ))}
                      </View>
                    )}

                    <View style={styles.explanationBox}>
                      <Text style={styles.explanationText}>
                        <Text style={{ fontWeight: 'bold' }}>{t.foundationLabel} </Text>
                        {currentCard[lang].explanation}
                      </Text>
                    </View>

                    <View style={styles.mnemonicBox}>
                      <Text style={styles.mnemonicText}>
                        <Text style={{ fontWeight: 'bold' }}>{t.mnemonicTip}: </Text>
                        {currentCard[lang].mnemonicOrExamTip}
                      </Text>
                    </View>
                  </View>
                )}

                {/* ACTION AREA */}
                <View style={styles.cardActions}>
                  {!isFlipped ? (
                    <View style={{ alignItems: 'center' }}>
                      <View style={styles.flipBtn}>
                        <Text style={styles.flipBtnText}>{t.showAnswer}</Text>
                      </View>
                      <Text style={styles.flipPromptText}>{t.flipPrompt}</Text>
                    </View>
                  ) : (
                    <View style={{ width: '100%' }}>
                      <Text style={styles.ratingPrompt}>{t.ratingPrompt}</Text>
                      <View style={styles.ratingGrid}>
                        <TouchableOpacity
                          style={[styles.rateBtn, { backgroundColor: '#DC2626' }]}
                          onPress={(e) => { e?.stopPropagation?.(); handleRate('again'); }}
                        >
                          <Text style={styles.rateBtnText}>{t.again}</Text>
                        </TouchableOpacity>
                        <TouchableOpacity
                          style={[styles.rateBtn, { backgroundColor: '#EA580C' }]}
                          onPress={(e) => { e?.stopPropagation?.(); handleRate('hard'); }}
                        >
                          <Text style={styles.rateBtnText}>{t.hard}</Text>
                        </TouchableOpacity>
                        <TouchableOpacity
                          style={[styles.rateBtn, { backgroundColor: '#16A34A' }]}
                          onPress={(e) => { e?.stopPropagation?.(); handleRate('good'); }}
                        >
                          <Text style={styles.rateBtnText}>{t.good}</Text>
                        </TouchableOpacity>
                        <TouchableOpacity
                          style={[styles.rateBtn, { backgroundColor: '#2563EB' }]}
                          onPress={(e) => { e?.stopPropagation?.(); handleRate('easy'); }}
                        >
                          <Text style={styles.rateBtnText}>{t.easy}</Text>
                        </TouchableOpacity>
                      </View>
                    </View>
                  )}
                </View>
              </TouchableOpacity>
            </View>
          )}
        </View>
      )}

      {/* EXAM SIMULATOR */}
      {mode === 'exam' && (
        <View style={styles.examContainer}>
          {!examStarted ? (
            <View style={styles.examStartBox}>
              <Text style={{ fontSize: 44, textAlign: 'center', marginBottom: 12 }}>💯</Text>
              <Text style={styles.examTitle}>{t.startExam}</Text>
              <Text style={styles.examDesc}>{t.examDesc}</Text>

              <View style={styles.examButtonsRow}>
                <TouchableOpacity style={styles.examOptionBtn} onPress={() => startExam(10)}>
                  <Text style={styles.examOptionBtnText}>{t.exam10Btn}</Text>
                </TouchableOpacity>
                <TouchableOpacity style={[styles.examOptionBtn, styles.examOptionBtnPrimary]} onPress={() => startExam(20)}>
                  <Text style={[styles.examOptionBtnText, { color: '#FFF' }]}>{t.exam20Btn}</Text>
                </TouchableOpacity>
                <TouchableOpacity style={styles.examOptionBtn} onPress={() => startExam(ANKI_CARDS.length)}>
                  <Text style={styles.examOptionBtnText}>{t.examFullBtn} ({ANKI_CARDS.length} Qs)</Text>
                </TouchableOpacity>
              </View>
            </View>
          ) : (
            <View>
              <View style={styles.examHeader}>
                <Text style={styles.examHeaderText}>
                  {t.examInProgress} {Object.keys(examAnswers).length} {t.of} {examQuestions.length} {t.answeredLabel}
                </Text>
                <TouchableOpacity style={styles.examResetBtn} onPress={() => setExamStarted(false)}>
                  <Text style={styles.examResetBtnText}>{t.restartBtn}</Text>
                </TouchableOpacity>
              </View>

              {examQuestions.map((q, qIdx) => {
                const selectedOpt = examAnswers[qIdx];

                return (
                  <View key={qIdx} style={styles.questionCard}>
                    <View style={{ flexDirection: 'row', justifyContent: 'space-between', marginBottom: 8 }}>
                      <Text style={styles.questionNum}>{t.questionLabel} {qIdx + 1} {t.of} {examQuestions.length}</Text>
                      <Text style={styles.questionChap}>{t.chapterFull} {q.card.chapter}</Text>
                    </View>

                    <Text style={styles.questionBody}>{q.card[lang].question}</Text>

                    <View style={{ marginTop: 12, gap: 8 }}>
                      {q.optionCards.map((optCard, optIdx) => {
                        let btnStyle: StyleProp<ViewStyle> = styles.optionBtn;
                        let textStyle: StyleProp<TextStyle> = styles.optionText;

                        if (selectedOpt === optIdx) {
                          btnStyle = [styles.optionBtn, styles.optionBtnSelected];
                          textStyle = [styles.optionText, styles.optionTextSelected];
                        }

                        if (examSubmitted) {
                          if (optIdx === q.correctIndex) {
                            btnStyle = [styles.optionBtn, styles.optionBtnCorrect];
                            textStyle = [styles.optionText, styles.optionTextCorrect];
                          } else if (selectedOpt === optIdx) {
                            btnStyle = [styles.optionBtn, styles.optionBtnWrong];
                            textStyle = [styles.optionText, styles.optionTextWrong];
                          }
                        }

                        return (
                          <TouchableOpacity
                            key={optCard.id}
                            style={btnStyle}
                            onPress={() => handleExamOptionSelect(qIdx, optIdx)}
                            disabled={examSubmitted}
                          >
                            <Text style={textStyle}>
                              {String.fromCharCode(65 + optIdx)}) {optCard[lang].answer}
                            </Text>
                          </TouchableOpacity>
                        );
                      })}
                    </View>

                    {examSubmitted && (
                      <View style={styles.feedbackBox}>
                        <Text style={styles.feedbackTitle}>
                          {selectedOpt === q.correctIndex ? t.correctLabel : t.incorrectLabel}
                        </Text>
                        <Text style={styles.feedbackTip}>
                          <Text style={{ fontWeight: 'bold' }}>{t.examTipPrefix} </Text>
                          {q.card[lang].mnemonicOrExamTip}
                        </Text>
                      </View>
                    )}
                  </View>
                );
              })}

              {!examSubmitted ? (
                <TouchableOpacity
                  style={[
                    styles.submitExamBtn,
                    Object.keys(examAnswers).length === 0 && { opacity: 0.6 },
                  ]}
                  onPress={() => setExamSubmitted(true)}
                  disabled={Object.keys(examAnswers).length === 0}
                >
                  <Text style={styles.submitExamBtnText}>{t.submitExam}</Text>
                </TouchableOpacity>
              ) : (
                <View style={styles.resultBox}>
                  <Text style={styles.resultTitle}>{t.examResult}</Text>
                  <Text style={styles.resultScore}>{calculateExamScore()}%</Text>
                  <Text style={styles.resultMessage}>
                    {calculateExamScore() === 100
                      ? t.perfectScore
                      : calculateExamScore() >= 80
                      ? t.highScore
                      : calculateExamScore() >= 60
                      ? t.passScore
                      : t.failScore}
                  </Text>
                </View>
              )}
            </View>
          )}
        </View>
      )}

      {/* BROWSER */}
      {mode === 'browser' && (
        <View style={styles.browserContainer}>
          {renderFilterRows()}
          <TextInput
            style={styles.searchInput}
            placeholder={t.searchPlaceholder}
            value={searchQuery}
            onChangeText={setSearchQuery}
          />
          <View style={{ marginTop: 12 }}>
            <Text style={{ fontSize: 13, color: '#64748B', marginBottom: 8 }}>
              {filteredCards.length} {t.cardsFound}
            </Text>
            {filteredCards.map((card) => (
              <TouchableOpacity
                key={card.id}
                style={styles.browserCard}
                activeOpacity={0.85}
                onPress={() => handleJumpToCardInStudy(card.id)}
              >
                <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 4, marginBottom: 4 }}>
                  <Text style={styles.browserPali}>{card.paliTerm}</Text>
                  <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
                    <Text style={styles.browserMeta}>{card.chapterName[lang]} | {card[lang].examQuestionType}</Text>
                    <Text style={styles.browserJumpBadge}>{t.studyThisCard}</Text>
                  </View>
                </View>
                <Text style={styles.browserQuestion}>{card[lang].question}</Text>
                <Text style={styles.browserAnswer}>{card[lang].answer}</Text>
              </TouchableOpacity>
            ))}
          </View>
        </View>
      )}

      {/* EXPORT */}
      {mode === 'export' && (
        <View style={styles.exportContainer}>
          <Text style={styles.exportTitle}>{t.exportTitle}</Text>
          <Text style={styles.exportDesc}>{t.exportDesc}</Text>
          <TouchableOpacity style={styles.downloadBtn} onPress={handleExportAnki}>
            <Text style={styles.downloadBtnText}>{t.downloadBtn}</Text>
          </TouchableOpacity>
        </View>
      )}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FAF5E4',
  },
  contentContainer: {
    paddingVertical: 16,
    maxWidth: 1050,
    width: '100%',
    alignSelf: 'center',
  },
  banner: {
    backgroundColor: '#4B2E2A',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  bannerHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    flexWrap: 'wrap',
    gap: 12,
  },
  bannerTitle: {
    color: '#FFF',
    fontSize: 18,
    fontWeight: 'bold',
  },
  bannerSubtitle: {
    color: '#EADFC9',
    fontSize: 13,
  },
  langSelector: {
    flexDirection: 'row',
    backgroundColor: 'rgba(255,255,255,0.15)',
    borderRadius: 8,
    padding: 2,
    gap: 4,
  },
  langBtn: {
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 6,
  },
  langBtnActive: {
    backgroundColor: '#D4A373',
  },
  langBtnText: {
    color: '#FFF',
    fontSize: 12,
    fontWeight: 'bold',
  },
  langBtnTextActive: {
    color: '#4B2E2A',
  },
  statsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 16,
    marginTop: 12,
    paddingTop: 10,
    borderTopWidth: 1,
    borderTopColor: 'rgba(255,255,255,0.15)',
  },
  statText: {
    color: '#EADFC9',
    fontSize: 13,
  },
  statBold: {
    color: '#FFF',
    fontWeight: 'bold',
  },
  statGold: {
    color: '#FDE047',
    fontWeight: 'bold',
  },
  modeTabBar: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 6,
    borderBottomWidth: 2,
    borderBottomColor: '#D8CBB5',
    paddingBottom: 10,
    marginBottom: 16,
  },
  modeTab: {
    paddingVertical: 9,
    paddingHorizontal: 12,
    borderRadius: 8,
    backgroundColor: '#EADFC9',
  },
  modeTabActive: {
    backgroundColor: '#4B2E2A',
  },
  modeTabText: {
    color: '#4B2E2A',
    fontWeight: 'bold',
    fontSize: 13,
  },
  modeTabTextActive: {
    color: '#FFF',
  },
  filterBar: {
    marginBottom: 12,
  },
  filterScroll: {
    gap: 6,
    paddingBottom: 4,
  },
  filterChip: {
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 16,
    backgroundColor: '#EADFC9',
    borderWidth: 1,
    borderColor: '#D8CBB5',
  },
  filterChipActive: {
    backgroundColor: '#8C2D19',
    borderColor: '#8C2D19',
  },
  filterChipSecondary: {
    paddingHorizontal: 11,
    paddingVertical: 5,
    borderRadius: 14,
    backgroundColor: '#F4ECE1',
    borderWidth: 1,
    borderColor: '#D8CBB5',
  },
  filterChipSecondaryActive: {
    backgroundColor: '#4B2E2A',
    borderColor: '#4B2E2A',
  },
  filterChipText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#4B2E2A',
  },
  filterChipTextActive: {
    color: '#FFF',
  },
  emptyState: {
    padding: 32,
    alignItems: 'center',
    backgroundColor: '#FFFDF7',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#D8CBB5',
  },
  emptyText: {
    color: '#8C7E6C',
    fontSize: 14,
  },
  navRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  counterText: {
    fontSize: 13,
    color: '#6B5A4B',
    fontWeight: '600',
  },
  smallBtn: {
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 6,
    backgroundColor: '#EADFC9',
  },
  smallBtnDisabled: {
    opacity: 0.4,
  },
  smallBtnText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#4B2E2A',
  },
  cardBox: {
    backgroundColor: '#FFFDF7',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#D8CBB5',
    padding: 20,
    minHeight: 340,
    shadowColor: '#000',
    shadowOpacity: 0.05,
    shadowRadius: 6,
    elevation: 2,
  },
  badgeRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    alignItems: 'center',
    justifyContent: 'space-between',
    gap: 6,
    borderBottomWidth: 1,
    borderBottomColor: '#EADFC9',
    paddingBottom: 10,
    marginBottom: 14,
  },
  badgeChapter: {
    backgroundColor: '#F3E8FF',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 6,
  },
  badgeChapterText: {
    color: '#6B21A8',
    fontSize: 11,
    fontWeight: '700',
  },
  badgeSection: {
    backgroundColor: '#FEF3C7',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 6,
  },
  badgeSectionText: {
    color: '#B45309',
    fontSize: 11,
    fontWeight: '700',
  },
  audioBtn: {
    backgroundColor: '#EADFC9',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 6,
  },
  audioBtnText: {
    fontSize: 11,
    fontWeight: '600',
    color: '#4B2E2A',
  },
  frontContent: {
    alignItems: 'center',
    paddingVertical: 14,
  },
  paliTerm: {
    color: '#8C2D19',
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 8,
    textAlign: 'center',
  },
  questionText: {
    color: '#2D1E1B',
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 8,
    lineHeight: 24,
  },
  examTypeText: {
    color: '#8C7E6C',
    fontSize: 12,
  },
  backContent: {
    marginTop: 14,
    paddingTop: 14,
    borderTopWidth: 1,
    borderTopColor: '#D8CBB5',
    borderStyle: 'dashed',
  },
  answerBox: {
    backgroundColor: '#F4ECE1',
    borderLeftWidth: 4,
    borderLeftColor: '#8C2D19',
    padding: 12,
    borderRadius: 6,
    marginBottom: 12,
  },
  answerText: {
    color: '#2D1E1B',
    fontSize: 15,
    fontWeight: '600',
    lineHeight: 22,
  },
  breakdownTitle: {
    color: '#4B2E2A',
    fontSize: 13,
    fontWeight: 'bold',
    marginBottom: 6,
  },
  breakdownItem: {
    flexDirection: 'row',
    marginBottom: 4,
  },
  bullet: {
    color: '#8C2D19',
    marginRight: 6,
    fontSize: 14,
  },
  breakdownText: {
    color: '#4A3B32',
    fontSize: 13,
    lineHeight: 18,
    flex: 1,
  },
  explanationBox: {
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#BFDBFE',
    padding: 10,
    borderRadius: 8,
    marginBottom: 10,
  },
  explanationText: {
    color: '#1E40AF',
    fontSize: 13,
    lineHeight: 18,
  },
  mnemonicBox: {
    backgroundColor: '#F0FDF4',
    borderWidth: 1,
    borderColor: '#BBF7D0',
    padding: 10,
    borderRadius: 8,
  },
  mnemonicText: {
    color: '#166534',
    fontSize: 13,
    lineHeight: 18,
  },
  cardActions: {
    marginTop: 20,
    alignItems: 'center',
  },
  flipBtn: {
    backgroundColor: '#4B2E2A',
    paddingVertical: 12,
    paddingHorizontal: 28,
    borderRadius: 8,
  },
  flipBtnText: {
    color: '#FFF',
    fontSize: 15,
    fontWeight: 'bold',
  },
  flipPromptText: {
    color: '#8C7E6C',
    fontSize: 12,
    marginTop: 6,
  },
  ratingPrompt: {
    color: '#6B5A4B',
    fontSize: 12,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 8,
  },
  ratingGrid: {
    flexDirection: 'row',
    gap: 8,
    justifyContent: 'center',
    flexWrap: 'wrap',
  },
  rateBtn: {
    paddingVertical: 10,
    paddingHorizontal: 14,
    borderRadius: 6,
    minWidth: 70,
    alignItems: 'center',
  },
  rateBtnText: {
    color: '#FFF',
    fontSize: 13,
    fontWeight: 'bold',
  },
  examContainer: {
    backgroundColor: '#FFFDF7',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#D8CBB5',
    padding: 20,
  },
  examStartBox: {
    alignItems: 'center',
    paddingVertical: 24,
  },
  examTitle: {
    color: '#4B2E2A',
    fontSize: 22,
    fontWeight: 'bold',
    marginBottom: 8,
    textAlign: 'center',
  },
  examDesc: {
    color: '#6B5A4B',
    fontSize: 14,
    textAlign: 'center',
    maxWidth: 550,
    lineHeight: 20,
    marginBottom: 20,
  },
  examButtonsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 12,
    justifyContent: 'center',
  },
  examOptionBtn: {
    paddingHorizontal: 16,
    paddingVertical: 12,
    borderRadius: 8,
    backgroundColor: '#EADFC9',
    borderWidth: 1,
    borderColor: '#D8CBB5',
  },
  examOptionBtnPrimary: {
    backgroundColor: '#8C2D19',
    borderColor: '#8C2D19',
  },
  examOptionBtnText: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#4B2E2A',
  },
  examHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    flexWrap: 'wrap',
    gap: 8,
    marginBottom: 16,
    paddingBottom: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#D8CBB5',
  },
  examHeaderText: {
    color: '#4B2E2A',
    fontSize: 14,
    fontWeight: 'bold',
  },
  examResetBtn: {
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 6,
    backgroundColor: '#EADFC9',
  },
  examResetBtnText: {
    color: '#4B2E2A',
    fontSize: 12,
    fontWeight: 'bold',
  },
  questionCard: {
    backgroundColor: '#FAF5E4',
    padding: 16,
    borderRadius: 10,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#D8CBB5',
  },
  questionNum: {
    color: '#8C2D19',
    fontSize: 12,
    fontWeight: 'bold',
  },
  questionChap: {
    color: '#6B5A4B',
    fontSize: 12,
  },
  questionBody: {
    color: '#2D1E1B',
    fontSize: 16,
    fontWeight: 'bold',
    lineHeight: 22,
  },
  optionBtn: {
    backgroundColor: '#FFFDF7',
    padding: 12,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#D8CBB5',
  },
  optionBtnSelected: {
    backgroundColor: '#EADFC9',
    borderColor: '#8C2D19',
  },
  optionBtnCorrect: {
    backgroundColor: '#DCFCE7',
    borderColor: '#16A34A',
  },
  optionBtnWrong: {
    backgroundColor: '#FEE2E2',
    borderColor: '#DC2626',
  },
  optionText: {
    color: '#4B2E2A',
    fontSize: 14,
  },
  optionTextSelected: {
    fontWeight: 'bold',
    color: '#8C2D19',
  },
  optionTextCorrect: {
    fontWeight: 'bold',
    color: '#15803D',
  },
  optionTextWrong: {
    fontWeight: 'bold',
    color: '#B91C1C',
  },
  feedbackBox: {
    marginTop: 12,
    padding: 12,
    borderRadius: 8,
    backgroundColor: '#FFFDF7',
    borderWidth: 1,
    borderColor: '#D8CBB5',
  },
  feedbackTitle: {
    fontSize: 14,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  feedbackTip: {
    fontSize: 13,
    color: '#4B2E2A',
    lineHeight: 18,
  },
  submitExamBtn: {
    backgroundColor: '#8C2D19',
    padding: 16,
    borderRadius: 10,
    alignItems: 'center',
    marginVertical: 16,
  },
  submitExamBtnText: {
    color: '#FFF',
    fontSize: 16,
    fontWeight: 'bold',
  },
  resultBox: {
    backgroundColor: '#FFFDF7',
    padding: 24,
    borderRadius: 12,
    alignItems: 'center',
    borderWidth: 2,
    borderColor: '#D4A373',
    marginVertical: 16,
  },
  resultTitle: {
    color: '#4B2E2A',
    fontSize: 20,
    fontWeight: 'bold',
  },
  resultScore: {
    fontSize: 48,
    fontWeight: 'bold',
    color: '#8C2D19',
    marginVertical: 8,
  },
  resultMessage: {
    color: '#4A3B32',
    fontSize: 15,
    textAlign: 'center',
    lineHeight: 22,
    maxWidth: 500,
  },
  browserContainer: {
    backgroundColor: '#FFFDF7',
    padding: 16,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#D8CBB5',
  },
  searchInput: {
    backgroundColor: '#FAF5E4',
    padding: 12,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#D8CBB5',
    fontSize: 14,
    color: '#2D1E1B',
  },
  browserCard: {
    backgroundColor: '#FAF5E4',
    padding: 12,
    borderRadius: 8,
    marginBottom: 10,
    borderWidth: 1,
    borderColor: '#EADFC9',
  },
  browserPali: {
    color: '#8C2D19',
    fontSize: 14,
    fontWeight: 'bold',
  },
  browserMeta: {
    color: '#8C7E6C',
    fontSize: 11,
  },
  browserJumpBadge: {
    fontSize: 11,
    fontWeight: '700',
    color: '#4B2E2A',
    backgroundColor: '#EADFC9',
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 6,
  },
  browserQuestion: {
    color: '#2D1E1B',
    fontSize: 14,
    fontWeight: 'bold',
    marginVertical: 4,
  },
  browserAnswer: {
    color: '#4B2E2A',
    fontSize: 13,
  },
  exportContainer: {
    backgroundColor: '#FFFDF7',
    padding: 24,
    borderRadius: 12,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#D8CBB5',
  },
  exportTitle: {
    color: '#4B2E2A',
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 8,
    textAlign: 'center',
  },
  exportDesc: {
    color: '#6B5A4B',
    fontSize: 14,
    textAlign: 'center',
    maxWidth: 500,
    lineHeight: 20,
    marginBottom: 20,
  },
  downloadBtn: {
    backgroundColor: '#4B2E2A',
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 8,
  },
  downloadBtnText: {
    color: '#FFF',
    fontSize: 15,
    fontWeight: 'bold',
  },
});

import React, { useMemo } from 'react';
import { StyleSheet, StyleProp, TextStyle, Platform } from 'react-native';
import { useAppDispatch } from '../../store/hooks';
import { setDictionaryWord } from '../../store/slices/readingSlice';
import { lookupWord, cleanPaliToken } from '../../services/dictionaryService';
import { parsePaliMarkup } from '../../utils/paliMarkup';
import { Text } from '../ui/AppText';

interface Props {
  text: string;
  style?: StyleProp<TextStyle>;
  onWordPress?: (word: string) => void;
}

interface Token {
  key: string;
  text: string;
  bold: boolean;
  paliWord?: string;
}

// Qualquer letra latina (inclui todo o bloco "Latin Extended Additional", onde ficam
// ṃ ṅ ṇ ṭ ḍ ḷ ḥ ś ṣ ṛ ...).
const WORD_CHARS = 'A-Za-z\\u00C0-\\u024F\\u1E00-\\u1EFF';
const SPLIT_PATTERN = new RegExp(`([^${WORD_CHARS}]+)`, 'g');
const SEPARATOR_ONLY = new RegExp(`^[^${WORD_CHARS}]+$`);

export const InteractivePaliText: React.FC<Props> = ({ text, style, onWordPress }) => {
  const dispatch = useAppDispatch();

  // Converte a marcação (<b>, versos) em linhas e torna todas as palavras em Pāli interativas.
  const lines = useMemo<Token[][]>(() => {
    return parsePaliMarkup(text).map((line, lineIndex) => {
      const tokens: Token[] = [];
      line.forEach((run, runIndex) => {
        run.text.split(SPLIT_PATTERN).forEach((piece, pieceIndex) => {
          if (!piece) return;
          const key = `${lineIndex}-${runIndex}-${pieceIndex}`;
          if (SEPARATOR_ONLY.test(piece)) {
            tokens.push({ key, text: piece, bold: run.bold });
            return;
          }
          const clean = cleanPaliToken(piece);
          const entry = lookupWord(piece);
          const paliWord = entry ? entry.pali : clean;
          tokens.push({
            key,
            text: piece,
            bold: run.bold,
            paliWord: paliWord || clean,
          });
        });
      });
      return tokens;
    });
  }, [text]);

  const handleWordPress = (word: string) => {
    dispatch(setDictionaryWord(word));
    if (onWordPress) {
      onWordPress(word);
    }
  };

  return (
    <Text style={style}>
      {lines.map((tokens, lineIndex) => (
        <React.Fragment key={lineIndex}>
          {lineIndex > 0 ? <Text>{'\n'}</Text> : null}
          {tokens.map((token) => {
            if (token.paliWord) {
              const wordToLookup = token.paliWord;
              return (
                <Text
                  key={token.key}
                  style={[
                    token.bold ? styles.bold : null,
                    styles.interactiveWord,
                    Platform.OS === 'web' ? ({ cursor: 'pointer' } as unknown as TextStyle) : null,
                  ]}
                  onPress={() => handleWordPress(wordToLookup)}
                >
                  {token.text}
                </Text>
              );
            }
            return (
              <Text key={token.key} style={token.bold ? styles.bold : null}>
                {token.text}
              </Text>
            );
          })}
        </React.Fragment>
      ))}
    </Text>
  );
};

const styles = StyleSheet.create({
  bold: {
    fontWeight: 'bold',
  },
  interactiveWord: {
    color: '#4B2E2A',
    textDecorationLine: 'underline',
    textDecorationColor: 'rgba(75, 46, 42, 0.35)',
    textDecorationStyle: 'dotted',
  },
});

export default InteractivePaliText;

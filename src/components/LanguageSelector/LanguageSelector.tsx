// src/components/LanguageSelector/LanguageSelector.tsx
import React from 'react';
import { View, TouchableOpacity, StyleSheet } from 'react-native';
import { Text } from '../ui/AppText';
import { useAppDispatch, useAppSelector } from '../../store/hooks';
import { setLanguages } from '../../store/slices/readingSlice';
import type { Language } from '../../types/models';

const LANGUAGES: { code: Language; label: string }[] = [
  { code: 'pali', label: 'Pāli' },
  { code: 'en', label: 'English' },
  { code: 'pt', label: 'Português' },
  { code: 'es', label: 'Español' },
];

export const LanguageSelector: React.FC = () => {
  const dispatch = useAppDispatch();
  const currentLanguages = useAppSelector((s) => s.reading.languages);

  const handleToggle = (lang: Language) => {
    const isSelected = currentLanguages.includes(lang);
    if (isSelected) {
      // Impede desselecionar todos os idiomas (mantém pelo menos 1)
      if (currentLanguages.length > 1) {
        dispatch(setLanguages(currentLanguages.filter((l) => l !== lang)));
      }
    } else {
      // Mantém ordem consistente: pali -> en -> pt -> es
      const order: Language[] = ['pali', 'en', 'pt', 'es'];
      const updated = [...currentLanguages, lang].sort(
        (a, b) => order.indexOf(a) - order.indexOf(b)
      );
      dispatch(setLanguages(updated));
    }
  };

  return (
    <View style={styles.container}>
      {LANGUAGES.map(({ code, label }) => {
        const active = currentLanguages.includes(code);
        return (
          <TouchableOpacity
            key={code}
            style={[styles.btn, active && styles.btnActive]}
            onPress={() => handleToggle(code)}
            accessibilityRole="button"
            accessibilityLabel={`Alternar ${label}`}
          >
            <Text style={[styles.label, active && styles.labelActive]}>
              {label}
            </Text>
          </TouchableOpacity>
        );
      })}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    gap: 6,
    flexWrap: 'wrap',
    justifyContent: 'center',
    maxWidth: '100%',
  },
  btn: {
    minHeight: 32,
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 16,
    justifyContent: 'center',
    backgroundColor: '#E8DCC8',
  },
  btnActive: {
    backgroundColor: '#4B2E2A',
  },
  label: {
    fontSize: 12.5,
    color: '#4B2E2A',
  },
  labelActive: {
    color: '#FAF5E4',
    fontWeight: '600',
  },
});

export default LanguageSelector;

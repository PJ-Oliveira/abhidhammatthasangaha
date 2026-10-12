// src/components/SearchBar/SearchBar.tsx
import React, { useState, useCallback, useRef, useEffect } from 'react';
import { View, TouchableOpacity, StyleSheet } from 'react-native';
import { Text, TextInput } from '../ui/AppText';
import { useAppDispatch, useAppSelector } from '../../store/hooks';
import { setSearchQuery, setSearchResults } from '../../store/slices/readingSlice';
import { searchSegments } from '../../services/textSearch';
import { t } from '../../i18n';

export const SearchBar: React.FC = () => {
  const dispatch = useAppDispatch();
  const uiLanguage = useAppSelector((s) => s.settings.uiLanguage);
  const reduxSearchQuery = useAppSelector((s) => s.reading.searchQuery);
  const [query, setQuery] = useState(reduxSearchQuery);
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    setQuery(reduxSearchQuery);
  }, [reduxSearchQuery]);

  const executeSearch = useCallback(
    async (textToSearch: string) => {
      dispatch(setSearchQuery(textToSearch));
      if (!textToSearch.trim()) {
        dispatch(setSearchResults([]));
        return;
      }
      try {
        const results = await searchSegments(textToSearch);
        if (Array.isArray(results)) {
          if (results.length > 0 && typeof results[0] === 'object' && results[0] !== null) {
            const ids = results.map((r: any) => r.segmentId ?? r.id ?? String(r));
            dispatch(setSearchResults(ids));
          } else {
            dispatch(setSearchResults(results as string[]));
          }
        } else {
          dispatch(setSearchResults([]));
        }
      } catch (error) {
        console.error('Search error:', error);
        dispatch(setSearchResults([]));
      }
    },
    [dispatch]
  );

  const handleChangeText = (text: string) => {
    setQuery(text);
    if (timerRef.current) {
      clearTimeout(timerRef.current);
    }
    timerRef.current = setTimeout(() => {
      executeSearch(text);
    }, 300);
  };

  const handleSearchPress = () => {
    if (timerRef.current) {
      clearTimeout(timerRef.current);
    }
    executeSearch(query);
  };

  const handleClear = () => {
    setQuery('');
    if (timerRef.current) {
      clearTimeout(timerRef.current);
    }
    executeSearch('');
  };

  useEffect(() => {
    return () => {
      if (timerRef.current) {
        clearTimeout(timerRef.current);
      }
    };
  }, []);

  return (
    <View style={styles.container}>
      <View style={styles.inputWrapper}>
        <TouchableOpacity
          style={styles.searchButton}
          onPress={handleSearchPress}
          accessibilityRole="button"
          accessibilityLabel="Search"
          hitSlop={{ top: 8, bottom: 8, left: 8, right: 8 }}
        >
          <Text style={styles.searchIcon}>🔍</Text>
        </TouchableOpacity>

        <TextInput
          style={styles.input}
          placeholder={t('search.placeholder', uiLanguage)}
          placeholderTextColor="#A89F91"
          value={query}
          onChangeText={handleChangeText}
          onSubmitEditing={handleSearchPress}
          returnKeyType="search"
          autoCapitalize="none"
          autoCorrect={false}
        />

        {query.length > 0 && (
          <TouchableOpacity
            style={styles.clearButton}
            onPress={handleClear}
            accessibilityRole="button"
            accessibilityLabel="Clear"
            hitSlop={{ top: 8, bottom: 8, left: 8, right: 8 }}
          >
            <Text style={styles.clearIcon}>✕</Text>
          </TouchableOpacity>
        )}
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    paddingHorizontal: 16,
    paddingVertical: 8,
  },
  inputWrapper: {
    flexDirection: 'row',
    alignItems: 'center',
    height: 44,
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#C4A882',
    borderRadius: 22,
    paddingHorizontal: 12,
  },
  searchButton: {
    marginRight: 8,
    justifyContent: 'center',
    alignItems: 'center',
  },
  searchIcon: {
    fontSize: 16,
  },
  input: {
    flex: 1,
    height: 44,
    color: '#4B2E2A',
    fontSize: 16, // >= 16px: o iOS Safari não dá zoom automático ao focar
    paddingVertical: 0,
  },
  clearButton: {
    marginLeft: 8,
    padding: 4,
    justifyContent: 'center',
    alignItems: 'center',
  },
  clearIcon: {
    fontSize: 14,
    color: '#8B7355',
    fontWeight: 'bold',
  },
});

export default SearchBar;

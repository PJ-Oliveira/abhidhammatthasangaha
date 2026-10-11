// src/components/ui/AppText.tsx
//
// Substitutos de <Text> e <TextInput> que aplicam a fonte do app (completa para Pali)
// em TODO texto — Pali, traduções, dicionário e interface — escolhendo a variante
// certa (regular/negrito/itálico) pela família, nunca por síntese do navegador.

import React, { createContext, useContext, useMemo } from 'react';
import {
  Text as RNText,
  TextInput as RNTextInput,
  StyleSheet,
  TextProps,
  TextInputProps,
  TextStyle,
} from 'react-native';
import { FontFlavor, areFontsAvailable, resolveFontFamily } from '../../theme/typography';

const REGULAR: FontFlavor = { bold: false, italic: false };
const BOLD: FontFlavor = { bold: true, italic: false };
const ITALIC: FontFlavor = { bold: false, italic: true };
const BOLD_ITALIC: FontFlavor = { bold: true, italic: true };

function pickFlavor(bold: boolean, italic: boolean): FontFlavor {
  if (bold && italic) return BOLD_ITALIC;
  if (bold) return BOLD;
  if (italic) return ITALIC;
  return REGULAR;
}

// Texto aninhado herda negrito/itálico do pai (como no comportamento nativo).
const FlavorContext = createContext<FontFlavor>(REGULAR);

/** `undefined` = o estilo não diz nada sobre peso (herda). */
export function weightIsBold(weight: TextStyle['fontWeight']): boolean | undefined {
  if (weight === undefined) return undefined;
  if (weight === 'bold') return true;
  if (weight === 'normal') return false;
  const numeric = parseInt(String(weight), 10);
  return Number.isNaN(numeric) ? undefined : numeric >= 600;
}

interface Resolved {
  style: TextStyle;
  flavor: FontFlavor;
}

export function resolveTextStyle(
  rawStyle: TextProps['style'] | TextInputProps['style'],
  inherited: FontFlavor,
): Resolved {
  const flat: TextStyle = (StyleSheet.flatten(rawStyle) as TextStyle | undefined) ?? {};
  const bold = weightIsBold(flat.fontWeight) ?? inherited.bold;
  const italic = flat.fontStyle !== undefined ? flat.fontStyle === 'italic' : inherited.italic;
  const flavor = pickFlavor(bold, italic);

  // Fontes não carregadas: mantém fontWeight/fontStyle originais (fallback seguro).
  if (!areFontsAvailable()) {
    return { style: flat, flavor };
  }

  const { fontWeight: _fontWeight, fontStyle: _fontStyle, ...rest } = flat;
  return {
    style: {
      ...rest,
      fontFamily: flat.fontFamily ?? resolveFontFamily(flavor),
      // 'normal' explícito impede que um ancestral reintroduza negrito sintético.
      fontWeight: 'normal',
      fontStyle: 'normal',
    },
    flavor,
  };
}

export const Text = React.forwardRef<RNText, TextProps>(function AppText(props, ref) {
  const inherited = useContext(FlavorContext);
  const { style, ...rest } = props;
  const resolved = useMemo(() => resolveTextStyle(style, inherited), [style, inherited]);

  return (
    <FlavorContext.Provider value={resolved.flavor}>
      <RNText ref={ref} {...rest} style={resolved.style} />
    </FlavorContext.Provider>
  );
});

export const TextInput = React.forwardRef<RNTextInput, TextInputProps>(function AppTextInput(
  props,
  ref,
) {
  const { style, ...rest } = props;
  const resolved = useMemo(() => resolveTextStyle(style, REGULAR), [style]);
  return <RNTextInput ref={ref} {...rest} style={resolved.style} />;
});

// src/theme/typography.ts
//
// Fonte única do app. O Noto Serif foi escolhido porque cobre todas as letras do
// Pali (ā ī ū ṃ ṁ ṅ ñ ṇ ṭ ḍ ḷ ḹ ṛ ṝ ś ṣ ḥ e maiúsculas) em regular, itálico, negrito e
// negrito-itálico, e é empacotada com o app (funciona offline).
//
// IMPORTANTE: em fontes customizadas, negrito/itálico devem ser escolhidos pela
// *família* (um arquivo por variante) e não por fontWeight/fontStyle — senão o
// navegador "sintetiza" o estilo e os diacríticos ficam deformados.

import { Platform } from 'react-native';

export interface FontFlavor {
  bold: boolean;
  italic: boolean;
}

/** Nomes registrados em `Font.loadAsync` (ver App.tsx). */
export const FONT_FILES = {
  regular: 'NotoSerif_400Regular',
  bold: 'NotoSerif_700Bold',
  italic: 'NotoSerif_400Regular_Italic',
  boldItalic: 'NotoSerif_700Bold_Italic',
} as const;

// Na web damos uma pilha de reserva (a mesma fonte instalada no sistema, depois
// serifas com bom suporte a Latim Estendido). No nativo precisa ser um único nome.
const WEB_FALLBACK = '"Noto Serif", Georgia, "Times New Roman", serif';

function family(name: string): string {
  return Platform.OS === 'web' ? `${name}, ${WEB_FALLBACK}` : name;
}

export function resolveFontFamily({ bold, italic }: FontFlavor): string {
  if (bold && italic) return family(FONT_FILES.boldItalic);
  if (bold) return family(FONT_FILES.bold);
  if (italic) return family(FONT_FILES.italic);
  return family(FONT_FILES.regular);
}

// Se o carregamento falhar, voltamos ao comportamento nativo (fontWeight/fontStyle),
// para que negrito e itálico não desapareçam.
let fontsAvailable = false;

export function setFontsAvailable(value: boolean): void {
  fontsAvailable = value;
}

export function areFontsAvailable(): boolean {
  return fontsAvailable;
}

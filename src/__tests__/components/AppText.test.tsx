import React from 'react';
import { StyleSheet } from 'react-native';
import { render } from '@testing-library/react-native';
import { Text, TextInput, weightIsBold } from '../../components/ui/AppText';
import { setFontsAvailable } from '../../theme/typography';

const familyOf = (node: { props: { style?: unknown } }): string | undefined =>
  (StyleSheet.flatten(node.props.style as never) as { fontFamily?: string } | undefined)?.fontFamily;
const flat = (node: { props: { style?: unknown } }) =>
  StyleSheet.flatten(node.props.style as never) as Record<string, unknown>;

describe('AppText (fonts loaded)', () => {
  beforeAll(() => setFontsAvailable(true));
  afterAll(() => setFontsAvailable(false));

  it('applies the regular Pali-complete font by default', () => {
    const { getByText } = render(<Text>kammaṭṭhāna</Text>);
    expect(familyOf(getByText('kammaṭṭhāna'))).toBe('NotoSerif_400Regular');
  });

  it('picks real bold/italic files and strips fontWeight/fontStyle (no synthetic styles)', () => {
    const { getByText } = render(
      <>
        <Text style={{ fontWeight: 'bold' }}>b</Text>
        <Text style={{ fontWeight: '700' }}>b7</Text>
        <Text style={{ fontStyle: 'italic' }}>i</Text>
        <Text style={{ fontWeight: '600', fontStyle: 'italic' }}>bi</Text>
      </>,
    );
    expect(familyOf(getByText('b'))).toBe('NotoSerif_700Bold');
    expect(familyOf(getByText('b7'))).toBe('NotoSerif_700Bold');
    expect(familyOf(getByText('i'))).toBe('NotoSerif_400Regular_Italic');
    expect(familyOf(getByText('bi'))).toBe('NotoSerif_700Bold_Italic');
    expect(flat(getByText('b')).fontWeight).toBe('normal');
    expect(flat(getByText('i')).fontStyle).toBe('normal');
  });

  it('treats weights below 600 as regular', () => {
    expect(weightIsBold('500')).toBe(false);
    expect(weightIsBold('600')).toBe(true);
    expect(weightIsBold('normal')).toBe(false);
    expect(weightIsBold(undefined)).toBeUndefined();
  });

  it('nested text inherits italic/bold from its parent (e.g. a Pali word inside an italic translation)', () => {
    const { getByText } = render(
      <Text style={{ fontStyle: 'italic' }}>
        Among these, <Text>kāmāvacara</Text> is
      </Text>,
    );
    expect(familyOf(getByText('kāmāvacara'))).toBe('NotoSerif_400Regular_Italic');
  });

  it('a nested bold span inside regular text becomes bold without affecting siblings', () => {
    const { getByText } = render(
      <Text>
        <Text style={{ fontWeight: 'bold' }}>cittaṃ</Text>
        <Text>tāva</Text>
      </Text>,
    );
    expect(familyOf(getByText('cittaṃ'))).toBe('NotoSerif_700Bold');
    expect(familyOf(getByText('tāva'))).toBe('NotoSerif_400Regular');
  });

  it('respects an explicitly provided fontFamily', () => {
    const { getByText } = render(<Text style={{ fontFamily: 'Menlo' }}>x</Text>);
    expect(familyOf(getByText('x'))).toBe('Menlo');
  });

  it('TextInput also uses the app font', () => {
    const { getByPlaceholderText } = render(<TextInput placeholder="Search Pali term..." />);
    expect(familyOf(getByPlaceholderText('Search Pali term...'))).toBe('NotoSerif_400Regular');
  });
});

describe('AppText (fonts NOT loaded: safe fallback)', () => {
  beforeAll(() => setFontsAvailable(false));

  it('keeps native fontWeight/fontStyle so bold and italic do not disappear', () => {
    const { getByText } = render(<Text style={{ fontWeight: 'bold', fontStyle: 'italic' }}>x</Text>);
    const style = flat(getByText('x'));
    expect(style.fontWeight).toBe('bold');
    expect(style.fontStyle).toBe('italic');
    expect(style.fontFamily).toBeUndefined();
  });
});

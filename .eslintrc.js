module.exports = {
  root: true,
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 2020,
    sourceType: 'module',
    ecmaFeatures: { jsx: true },
  },
  plugins: ['react'],
  extends: [
    'eslint:recommended',
    'plugin:react/recommended',
    'prettier',
  ],
  settings: {
    react: { version: 'detect' },
  },
  env: {
    browser: true,
    node: true,
    es6: true,
  },
  rules: {
    'react/react-in-jsx-scope': 'off',
    // TypeScript handles type checking; no-undef is noisy for TS globals
    'no-undef': 'off',
    'no-unused-vars': 'off',
  },
};

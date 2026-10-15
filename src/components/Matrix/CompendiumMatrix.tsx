// src/components/Matrix/CompendiumMatrix.tsx
import React, { useState } from 'react';
import { View, TouchableOpacity, ScrollView, StyleSheet } from 'react-native';
import { Text } from '../ui/AppText';
import { Language } from '../../data/ankiCards';
import { useAppSelector, useAppDispatch } from '../../store/hooks';
import { setUiLanguage } from '../../store/slices/settingsSlice';
import { useLayout } from '../../theme/layout';

interface MatrixGroupCard {
  title: string;
  color: string;
  desc: string;
  items: Array<{ bold?: string; text: string }>;
}

interface KiccaItem {
  num: number;
  name: string;
  count: string;
  desc: string;
}

interface PaccayaItem {
  id: number;
  pali: string;
  name: string;
  desc: string;
}

const MATRIX_DATA: Record<
  Language,
  {
    title: string;
    subtitle: string;
    cittaTab: string;
    cetasikaTab: string;
    rupaTab: string;
    kiccaTab: string;
    paccayaTab: string;
    kiccaCountLabel: string;
    cittaCards: MatrixGroupCard[];
    cetasikaCards: MatrixGroupCard[];
    rupaCards: MatrixGroupCard[];
    kiccas: KiccaItem[];
    paccayas: PaccayaItem[];
  }
> = {
  pt: {
    title: 'Matrizes Estruturais do Abhidhammatthasaṅgaha',
    subtitle: 'Síntese completa de contagens canônicas, estruturas e relações',
    cittaTab: 'Consciência (89 / 121)',
    cetasikaTab: 'Fatores Mentais (52)',
    rupaTab: 'Matéria (28)',
    kiccaTab: '14 Funções Mentais',
    paccayaTab: '24 Condições (Paccayas)',
    kiccaCountLabel: 'Cittas capazes:',
    cittaCards: [
      {
        title: '1. Akusala Citta (12)',
        color: '#DC2626',
        desc: 'Consciências Inábeis causadas por raízes impuras (lobha, dosa, moha).',
        items: [
          { bold: 'Lobha-mūla (8):', text: ' 4 com somanassa, 4 com upekkhā; 4 com diṭṭhi, 4 sem diṭṭhi; 4 asaṅkhārika, 4 sasaṅkhārika.' },
          { bold: 'Dosa-mūla (2):', text: ' Ambas com domanassa e paṭigha; 1 asaṅkhārika, 1 sasaṅkhārika.' },
          { bold: 'Moha-mūla (2):', text: ' Ambas com upekkhā; 1 com vicikicchā (dúvida), 1 com uddhacca (agitação).' },
        ],
      },
      {
        title: '2. Ahetuka Citta (18)',
        color: '#64748B',
        desc: 'Consciências sem raízes (hetu) associadas.',
        items: [
          { bold: 'Akusala-vipāka (7):', text: ' 5 sentidos sensoriais inábeis + 1 sampaṭicchana (recepção) + 1 santīraṇa neutro.' },
          { bold: 'Kusala-vipāka (8):', text: ' 5 sentidos hábeis + 1 sampaṭicchana + 2 santīraṇa (1 neutro com upekkhā, 1 alegre com somanassa).' },
          { bold: 'Ahetuka-kiriya (3):', text: ' Pañcadvārāvajjana (5 portas), Manodvārāvajjana (porta mental / voṭṭhabbana), Hasituppāda (sorriso do Arahant).' },
        ],
      },
      {
        title: '3. Kāmāvacara Sobhana (24)',
        color: '#16A34A',
        desc: 'Belas consciências da esfera dos sentidos (8 × 3 classes = 24).',
        items: [
          { bold: 'Mahā-kusala (8):', text: ' Ações salutares da esfera sensorial (4 somanassa / 4 upekkhā; 4 ñāṇasampayutta / 4 ñāṇavippayutta).' },
          { bold: 'Mahā-vipāka (8):', text: ' Frutos salutares sensoriais (atuam em paṭisandhi, bhavaṅga, cuti e tadārammaṇa).' },
          { bold: 'Mahā-kiriya (8):', text: ' Consciências funcionais belas exclusivas de Arahants.' },
        ],
      },
      {
        title: '4. Mahaggata & Lokuttara (35 ou 67)',
        color: '#7C3AED',
        desc: 'Consciências sublimes (27) e supramundanas (8 ou 40).',
        items: [
          { bold: 'Rūpāvacara (15):', text: ' 5 Kusala + 5 Vipāka + 5 Kiriya (5 Jhānas da forma sutil no sistema quíntuplo).' },
          { bold: 'Arūpāvacara (12):', text: ' 4 Kusala + 4 Vipāka + 4 Kiriya (4 absorções imateriais, todas com fatores do 5º Jhāna).' },
          { bold: 'Lokuttara (8 ou 40):', text: ' 4 Magga (Caminhos) + 4 Phala (Frutos). Multiplicados pelos 5 níveis de Jhāna = 40.' },
        ],
      },
    ],
    cetasikaCards: [
      {
        title: '1. Aññasamāna (13)',
        color: '#0284C7',
        desc: 'Fatores eticamente variáveis (assumem a qualidade moral do citta).',
        items: [
          { bold: 'Sabbacittasādhāraṇa (7 Universais):', text: ' Phassa, Vedanā, Saññā, Cetanā, Ekaggatā, Jīvitindriya, Manasikāra.' },
          { bold: 'Pakiṇṇaka (6 Ocasionais):', text: ' Vitakka, Vicāra, Adhimokkha, Vīriya, Pīti, Chanda.' },
        ],
      },
      {
        title: '2. Akusala (14)',
        color: '#DC2626',
        desc: 'Fatores mentais inábeis (exclusivos dos 12 Akusala Cittas).',
        items: [
          { bold: 'Mohacatukka (4 Universais Inábeis):', text: ' Moha, Ahirika, Anottappa, Uddhacca (presentes em todos os 12 akusalas).' },
          { bold: 'Lobhatika (3 da Cobiça):', text: ' Lobha, Diṭṭhi, Māna (diṭṭhi e māna nunca surgem juntos).' },
          { bold: 'Dosacatukka (4 da Aversão):', text: ' Dosa, Issā (inveja), Macchariya (avareza), Kukkucca (remorso).' },
          { bold: 'Thīnaduka (2) & Vicikicchā (1):', text: ' Thīna (torpor), Middha (letargia) nos 5 sasaṅkhārika; Vicikicchā (dúvida).' },
        ],
      },
      {
        title: '3. Sobhana (25)',
        color: '#16A34A',
        desc: 'Fatores mentais belos e puros (nos 59 ou 91 Sobhana Cittas).',
        items: [
          { bold: 'Sobhanasādhāraṇa (19 Universais Belos):', text: ' Saddhā, Sati, Hiri, Ottappa, Alobha, Adosa, Tatramajjhattatā e os 6 pares (kāya/citta passaddhi, lahutā, mudutā, kammaññatā, pāguññatā, ujukatā).' },
          { bold: 'Virati (3 Abstenções):', text: ' Sammāvācā, Sammākammanta, Sammā-ājīva (simultâneas no Lokuttara).' },
          { bold: 'Appamaññā (2 Ilimitados) & Paññā (1):', text: ' Karuṇā (compaixão), Muditā (alegria altruísta) e Paññindriya (sabedoria, nos 47/79 tihetuka).' },
        ],
      },
    ],
    rupaCards: [
      {
        title: '1. Nipphanna Rūpa (18 Concretas)',
        color: '#B45309',
        desc: 'Matéria com natureza intrínseca própria (Sabhāvarūpa), apta para contemplação de insight (Sammasanarūpa).',
        items: [
          { bold: '4 Mahābhūta (Elementos Primários):', text: ' Paṭhavī (terra/solidez), Āpo (água/coesão - intangível!), Tejo (fogo/temperatura), Vāyo (ar/distensão).' },
          { bold: '5 Pasādarūpa (Sensibilidades):', text: ' Cakkhu (olho), Sota (ouvido), Ghāna (nariz), Jivhā (língua), Kāya (corpo).' },
          { bold: '4 Gocararūpa (7 Objetos):', text: ' Rūpa (cor/forma), Sadda (som), Gandha (odor), Rasa (sabor) [+ Phoṭṭhabba = 3 elementos: terra, fogo, ar].' },
          { bold: '2 Bhāvarūpa (Sexos):', text: ' Itthatta (feminilidade) e Purisatta (masculinidade).' },
          { bold: '1 Hadayarūpa, 1 Jīvitarūpa, 1 Āhārarūpa:', text: ' Base do coração (hadayavatthu), faculdade vital física (jīvitindriya) e essência nutritiva (ojā).' },
        ],
      },
      {
        title: '2. Anipphanna Rūpa (10 Não-Concretas)',
        color: '#0369A1',
        desc: 'Modos, limites, comunicações e fases das 18 matérias concretas.',
        items: [
          { bold: '1 Paricchedarūpa (Espaço):', text: ' Ākāsadhātu (espaço delimitador entre grupos materiais / kalāpas).' },
          { bold: '2 Viññattirūpa (Comunicações):', text: ' Kāyaviññatti (expressão corporal) e Vacīviññatti (expressão vocal).' },
          { bold: '3 Vikārarūpa (Mutabilidades):', text: ' Lahutā (leveza), Mudutā (maleabilidade), Kammaññatā (adaptabilidade).' },
          { bold: '4 Lakkhaṇarūpa (Características):', text: ' Upacaya (surgimento inicial), Santati (continuidade), Jarā (envelhecimento) e Aniccatā (dissolução).' },
        ],
      },
    ],
    kiccas: [
      { num: 1, name: 'Paṭisandhi (Consciência de Renascimento)', count: '19', desc: 'Conecta a existência passada à nova vida (2 santīraṇa upekkhā + 8 mahāvipāka + 5 rūpavipāka + 4 arūpavipāka).' },
      { num: 2, name: 'Bhavaṅga (Fluxo Vital Subjacente)', count: '19', desc: 'Mantém a continuidade passiva da vida entre processos cognitivos (mesmos 19 cittas do paṭisandhi).' },
      { num: 3, name: 'Āvajjana (Advertência)', count: '2', desc: 'Volta a atenção para o objeto: Pañcadvārāvajjana (nas 5 portas) e Manodvārāvajjana (na porta mental).' },
      { num: 4, name: 'Dassana (Ver)', count: '2', desc: 'Consciência visual (2 cakkhuviññāṇa: akusalavipāka e kusalavipāka).' },
      { num: 5, name: 'Savana (Ouvir)', count: '2', desc: 'Consciência auditiva (2 sotaviññāṇa).' },
      { num: 6, name: 'Ghāyana (Cheirar)', count: '2', desc: 'Consciência olfativa (2 ghānaviññāṇa).' },
      { num: 7, name: 'Sāyana (Saborear)', count: '2', desc: 'Consciência gustativa (2 jivhāviññāṇa).' },
      { num: 8, name: 'Phusana (Tocar)', count: '2', desc: 'Consciência tátil (2 kāyaviññāṇa: com dukkha ou sukha).' },
      { num: 9, name: 'Sampaṭicchana (Recepção)', count: '2', desc: 'Recebe o objeto sensorial imediatamente após a percepção nos 5 sentidos.' },
      { num: 10, name: 'Santīraṇa (Investigação)', count: '3', desc: 'Examina e investiga o objeto recebido pelos sentidos (3 santīraṇacittas).' },
      { num: 11, name: 'Voṭṭhabbana (Determinação)', count: '1', desc: 'Determina o objeto nas 5 portas antes do javana (executada pelo Manodvārāvajjana).' },
      { num: 12, name: 'Javana (Impulso Kammaico)', count: '55 (ou 87)', desc: 'Fase ativa volitiva: 12 akusala + 1 hasituppāda + 8 mahākusala + 8 mahākiriya + 10 rūpa + 8 arūpa + 8/40 lokuttara.' },
      { num: 13, name: 'Tadārammaṇa (Registro / Retenção)', count: '11', desc: 'Registra objetos muito nítidos na esfera sensorial por 2 momentos após o javana (3 santīraṇa + 8 mahāvipāka).' },
      { num: 14, name: 'Cuti (Consciência de Morte)', count: '19', desc: 'Último momento mental que encerra uma existência (idêntico ao paṭisandhi e bhavaṅga daquela vida).' },
    ],
    paccayas: [
      { id: 1, pali: 'Hetu-paccaya', name: 'Condição de Raiz', desc: 'As 6 raízes (lobha, dosa, moha, alobha, adosa, amoha) firmando mente e matéria co-nascida como raízes de uma árvore.' },
      { id: 2, pali: 'Ārammaṇa-paccaya', name: 'Condição de Objeto', desc: 'Todo objeto cognoscível sustentando o surgimento de citta e cetasikas como bengala que apoia um idoso.' },
      { id: 3, pali: 'Adhipati-paccaya', name: 'Condição de Predominância', desc: '4 fatores soberanos (chanda, vīriya, citta, vīmaṃsā) ou objeto supremo governando a mente.' },
      { id: 4, pali: 'Anantara-paccaya', name: 'Condição de Proximidade', desc: 'Cada citta que cessa dá lugar imediatamente ao citta seguinte no fluxo contínuo.' },
      { id: 5, pali: 'Samanantara-paccaya', name: 'Condição de Proximidade Imediata', desc: 'Continuidade contígua absoluta sem qualquer hiato temporal entre dois momentos mentais.' },
      { id: 6, pali: 'Sahajāta-paccaya', name: 'Condição de Co-nascimento', desc: 'Fenômenos que auxiliam uns aos outros surgindo exatamente no mesmo instante (como chama e luz).' },
      { id: 7, pali: 'Aññamañña-paccaya', name: 'Condição de Mutualidade', desc: 'Fenômenos co-nascidos que sustentam-se reciprocamente (como um tripé de três bastões).' },
      { id: 8, pali: 'Nissaya-paccaya', name: 'Condição de Suporte / Dependência', desc: 'Serve de fundação ou ponto de apoio físico/mental (como a terra para as árvores ou tela para pintura).' },
      { id: 9, pali: 'Upanissaya-paccaya', name: 'Condição de Suporte Decisivo', desc: 'Indução poderosa (por objeto predominante, proximidade imediata ou condição natural/pakatūpanissaya).' },
      { id: 10, pali: 'Purejāta-paccaya', name: 'Condição de Pré-nascimento', desc: 'Matéria surgida antes (as 6 bases físicas e os 5 objetos sensoriais presentes) apoiando a mente que surge depois.' },
      { id: 11, pali: 'Pacchājāta-paccaya', name: 'Condição de Pós-nascimento', desc: 'Citta e cetasikas posteriores sustentando e preservando o corpo físico surgido anteriormente.' },
      { id: 12, pali: 'Āsevana-paccaya', name: 'Condição de Repetição', desc: 'Cada momento de javana fortalece e intensifica o javana seguinte da mesma qualidade ética.' },
      { id: 13, pali: 'Kamma-paccaya', name: 'Condição de Kamma', desc: 'Volição (cetanā) coordenando estados co-nascidos (sahajāta) ou produzindo frutos futuros (nānākkhaṇika).' },
      { id: 14, pali: 'Vipāka-paccaya', name: 'Condição de Resultante', desc: 'Cittas e cetasikas resultantes acalmando-se mutuamente em quietude passiva sem esforço.' },
      { id: 15, pali: 'Āhāra-paccaya', name: 'Condição de Nutriente', desc: 'Os 4 nutrientes (ojā material, phassa, manosañcetanā e viññāṇa) sustentando mente e corpo.' },
      { id: 16, pali: 'Indriya-paccaya', name: 'Condição de Faculdade', desc: 'As 22 faculdades (indriyas) exercendo maestria e controle em suas respectivas esferas (5 físicas + mana + itthi + purisa + jīvita + 5 vedanā + 5 espirituais + 3 supramundanas).' },
      { id: 17, pali: 'Jhāna-paccaya', name: 'Condição de Jhāna', desc: 'Os 7 fatores de jhāna fixando a mente na observação absorvida do objeto.' },
      { id: 18, pali: 'Magga-paccaya', name: 'Condição de Caminho', desc: 'Os 12 fatores de caminho (8 corretos + 4 incorretos) conduzindo a destinos nobres ou inferiores.' },
      { id: 19, pali: 'Sampayutta-paccaya', name: 'Condição de Associação', desc: 'Citta e cetasikas fundidos inseparavelmente (mesmo nascimento, cessação, objeto e base).' },
      { id: 20, pali: 'Vippayutta-paccaya', name: 'Condição de Dissociação', desc: 'Fenômenos mentais e materiais apoiando-se mutuamente mantendo suas naturezas distintas.' },
      { id: 21, pali: 'Atthi-paccaya', name: 'Condição de Presença', desc: 'Fenômeno que apoia outro permanecendo existente no momento presente.' },
      { id: 22, pali: 'Natthi-paccaya', name: 'Condição de Ausência', desc: 'Citta anterior que, ao extinguir-se completamente, abre espaço para o surgimento do próximo.' },
      { id: 23, pali: 'Vigata-paccaya', name: 'Condição de Desaparecimento', desc: 'O desaparecimento completo do estado mental anterior permitindo a sucessão cognitiva.' },
      { id: 24, pali: 'Avigata-paccaya', name: 'Condição de Não-Desaparecimento', desc: 'Fenômeno que sustenta outro enquanto ainda não desapareceu (idêntico em alcance ao Atthi-paccaya).' },
    ],
  },
  en: {
    title: 'Structural Matrices of Abhidhammatthasaṅgaha',
    subtitle: 'Complete synthesis of canonical counts, structures, and relations',
    cittaTab: 'Consciousness (89 / 121)',
    cetasikaTab: 'Mental Factors (52)',
    rupaTab: 'Matter (28)',
    kiccaTab: '14 Mental Functions',
    paccayaTab: '24 Conditions (Paccayas)',
    kiccaCountLabel: 'Capable Cittas:',
    cittaCards: [
      {
        title: '1. Akusala Citta (12)',
        color: '#DC2626',
        desc: 'Unwholesome consciousnesses rooted in greed, hatred, and delusion (lobha, dosa, moha).',
        items: [
          { bold: 'Lobha-mūla (8):', text: ' 4 with somanassa, 4 with upekkhā; 4 with diṭṭhi, 4 without diṭṭhi; 4 asaṅkhārika (unprompted), 4 sasaṅkhārika (prompted).' },
          { bold: 'Dosa-mūla (2):', text: ' Both with domanassa and paṭigha (aversion); 1 asaṅkhārika, 1 sasaṅkhārika.' },
          { bold: 'Moha-mūla (2):', text: ' Both with upekkhā; 1 with vicikicchā (doubt), 1 with uddhacca (restlessness).' },
        ],
      },
      {
        title: '2. Ahetuka Citta (18)',
        color: '#64748B',
        desc: 'Rootless consciousnesses devoid of concomitant ethical roots (hetu).',
        items: [
          { bold: 'Akusala-vipāka (7):', text: ' 5 unwholesome-resultant sense consciousnesses + 1 sampaṭicchana (receiving) + 1 neutral santīraṇa (investigating).' },
          { bold: 'Kusala-vipāka (8):', text: ' 5 wholesome-resultant sense consciousnesses + 1 sampaṭicchana + 2 santīraṇa (1 upekkhā, 1 somanassa).' },
          { bold: 'Ahetuka-kiriya (3):', text: ' Pañcadvārāvajjana (5-door adverting), Manodvārāvajjana (mind-door adverting / determining), Hasituppāda (Arahant smile).' },
        ],
      },
      {
        title: '3. Kāmāvacara Sobhana (24)',
        color: '#16A34A',
        desc: ' Sense-sphere Beautiful consciousnesses (8 × 3 classes = 24).',
        items: [
          { bold: 'Mahā-kusala (8):', text: ' Sense-sphere wholesome actions (4 somanassa / 4 upekkhā; 4 ñāṇasampayutta / 4 ñāṇavippayutta).' },
          { bold: 'Mahā-vipāka (8):', text: ' Sense-sphere wholesome resultants (perform paṭisandhi, bhavaṅga, cuti, and tadārammaṇa).' },
          { bold: 'Mahā-kiriya (8):', text: ' Sense-sphere beautiful functional consciousnesses exclusive to Arahants.' },
        ],
      },
      {
        title: '4. Mahaggata & Lokuttara (35 or 67)',
        color: '#7C3AED',
        desc: 'Sublime (27) and Supramundane (8 or 40) consciousnesses.',
        items: [
          { bold: 'Rūpāvacara (15):', text: ' 5 Kusala + 5 Vipāka + 5 Kiriya (5 Fine-material Jhānas in the 5-fold system).' },
          { bold: 'Arūpāvacara (12):', text: ' 4 Kusala + 4 Vipāka + 4 Kiriya (4 Immaterial absorptions, all sharing 5th Jhāna factors).' },
          { bold: 'Lokuttara (8 or 40):', text: ' 4 Magga (Paths) + 4 Phala (Fruits). Multiplied across the 5 Jhāna levels = 40.' },
        ],
      },
    ],
    cetasikaCards: [
      {
        title: '1. Aññasamāna (13)',
        color: '#0284C7',
        desc: 'Ethically variable factors (take on the moral tone of the associated citta).',
        items: [
          { bold: 'Sabbacittasādhāraṇa (7 Universals):', text: ' Phassa, Vedanā, Saññā, Cetanā, Ekaggatā, Jīvitindriya, Manasikāra.' },
          { bold: 'Pakiṇṇaka (6 Occasionals):', text: ' Vitakka, Vicāra, Adhimokkha, Vīriya, Pīti, Chanda.' },
        ],
      },
      {
        title: '2. Akusala (14)',
        color: '#DC2626',
        desc: 'Unwholesome mental factors (exclusive to the 12 Akusala Cittas).',
        items: [
          { bold: 'Mohacatukka (4 Unwholesome Universals):', text: ' Moha, Ahirika, Anottappa, Uddhacca (present in all 12 akusala cittas).' },
          { bold: 'Lobhatika (3 Greed Triad):', text: ' Lobha, Diṭṭhi (wrong view), Māna (conceit — never arises together with diṭṭhi).' },
          { bold: 'Dosacatukka (4 Hatred Tetrad):', text: ' Dosa, Issā (envy), Macchariya (avarice), Kukkucca (remorse).' },
          { bold: 'Thīnaduka (2) & Vicikicchā (1):', text: ' Thīna (sloth), Middha (torpor) in the 5 sasaṅkhārika cittas; Vicikicchā (doubt).' },
        ],
      },
      {
        title: '3. Sobhana (25)',
        color: '#16A34A',
        desc: 'Beautiful mental factors (in the 59 or 91 Sobhana Cittas).',
        items: [
          { bold: 'Sobhanasādhāraṇa (19 Beautiful Universals):', text: ' Saddhā, Sati, Hiri, Ottappa, Alobha, Adosa, Tatramajjhattatā, plus 6 pairs (kāya/citta passaddhi, lahutā, mudutā, kammaññatā, pāguññatā, ujukatā).' },
          { bold: 'Virati (3 Abstinences):', text: ' Sammāvācā (Right Speech), Sammākammanta (Right Action), Sammā-ājīva (Right Livelihood — arise together in Lokuttara).' },
          { bold: 'Appamaññā (2 Illimitables) & Paññā (1):', text: ' Karuṇā (compassion), Muditā (appreciative joy), and Paññindriya (wisdom, in 47/79 tihetuka cittas).' },
        ],
      },
    ],
    rupaCards: [
      {
        title: '1. Nipphanna Rūpa (18 Concretely Produced)',
        color: '#B45309',
        desc: 'Matter possessing intrinsic nature (Sabhāvarūpa), suitable for insight contemplation (Sammasanarūpa).',
        items: [
          { bold: '4 Mahābhūta (Great Essentials):', text: ' Paṭhavī (earth/solidity), Āpo (water/cohesion — intangible!), Tejo (fire/temperature), Vāyo (air/distension).' },
          { bold: '5 Pasādarūpa (Sensitive Phenomena):', text: ' Cakkhu (eye), Sota (ear), Ghāna (nose), Jivhā (tongue), Kāya (body).' },
          { bold: '4 Gocararūpa (7 Objective Fields):', text: ' Rūpa (visible form), Sadda (sound), Gandha (odor), Rasa (taste) [+ Phoṭṭhabba = 3 essentials: earth, fire, air].' },
          { bold: '2 Bhāvarūpa (Sex Faculties):', text: ' Itthatta (femininity) and Purisatta (masculinity).' },
          { bold: '1 Hadayarūpa, 1 Jīvitarūpa, 1 Āhārarūpa:', text: ' Heart-base (hadayavatthu), material life faculty (jīvitindriya), and nutritive essence (ojā).' },
        ],
      },
      {
        title: '2. Anipphanna Rūpa (10 Non-Concrete)',
        color: '#0369A1',
        desc: 'Modes, boundaries, intimations, and temporal phases of the 18 concrete material phenomena.',
        items: [
          { bold: '1 Paricchedarūpa (Space Element):', text: ' Ākāsadhātu (delimiting space bounding material groups / kalāpas).' },
          { bold: '2 Viññattirūpa (Intimations):', text: ' Kāyaviññatti (bodily intimation) and Vacīviññatti (vocal intimation).' },
          { bold: '3 Vikārarūpa (Mutabilities):', text: ' Lahutā (lightness), Mudutā (malleability), Kammaññatā (wieldiness).' },
          { bold: '4 Lakkhaṇarūpa (Characteristics):', text: ' Upacaya (production), Santati (continuity), Jarā (decay), and Aniccatā (impermanence).' },
        ],
      },
    ],
    kiccas: [
      { num: 1, name: 'Paṭisandhi (Rebirth-Linking)', count: '19', desc: 'Links the new existence to the previous life (2 upekkhā santīraṇa + 8 mahāvipāka + 5 rūpavipāka + 4 arūpavipāka).' },
      { num: 2, name: 'Bhavaṅga (Life-Continuum)', count: '19', desc: 'Preserves passive mental continuity between cognitive processes (same 19 cittas as paṭisandhi).' },
      { num: 3, name: 'Āvajjana (Adverting)', count: '2', desc: 'Turns attention toward an impinging object: Pañcadvārāvajjana (5 doors) and Manodvārāvajjana (mind door).' },
      { num: 4, name: 'Dassana (Seeing)', count: '2', desc: 'Visual cognition at the eye door (2 cakkhuviññāṇa: akusalavipāka and kusalavipāka).' },
      { num: 5, name: 'Savana (Hearing)', count: '2', desc: 'Auditory cognition at the ear door (2 sotaviññāṇa).' },
      { num: 6, name: 'Ghāyana (Smelling)', count: '2', desc: 'Olfactory cognition at the nose door (2 ghānaviññāṇa).' },
      { num: 7, name: 'Sāyana (Tasting)', count: '2', desc: 'Gustatory cognition at the tongue door (2 jivhāviññāṇa).' },
      { num: 8, name: 'Phusana (Touching)', count: '2', desc: 'Tactile cognition at the body door (2 kāyaviññāṇa: accompanied by dukkha or sukha).' },
      { num: 9, name: 'Sampaṭicchana (Receiving)', count: '2', desc: 'Receives the sense object immediately after sense-consciousness in the 5 doors.' },
      { num: 10, name: 'Santīraṇa (Investigating)', count: '3', desc: 'Investigates the object received by sampaṭicchana (3 santīraṇacittas).' },
      { num: 11, name: 'Voṭṭhabbana (Determining)', count: '1', desc: 'Determines or defines the object in the 5 sense doors prior to javana (performed by Manodvārāvajjana).' },
      { num: 12, name: 'Javana (Impulsion)', count: '55 (or 87)', desc: 'Active volitional phase: 12 akusala + 1 hasituppāda + 8 mahākusala + 8 mahākiriya + 10 rūpa + 8 arūpa + 8/40 lokuttara.' },
      { num: 13, name: 'Tadārammaṇa (Registration)', count: '11', desc: 'Registers vivid sense-sphere objects for 2 moments after javana (3 santīraṇa + 8 mahāvipāka).' },
      { num: 14, name: 'Cuti (Death Consciousness)', count: '19', desc: 'Final thought-moment terminating a lifespan (identical in type to paṭisandhi and bhavaṅga of that life).' },
    ],
    paccayas: [
      { id: 1, pali: 'Hetu-paccaya', name: 'Root Condition', desc: 'The 6 roots (lobha, dosa, moha, alobha, adosa, amoha) firmly establishing mind and co-nascent matter like tree roots.' },
      { id: 2, pali: 'Ārammaṇa-paccaya', name: 'Object Condition', desc: 'Any cognizable phenomenon supporting the arising of citta and cetasikas like a staff supporting an elderly person.' },
      { id: 3, pali: 'Adhipati-paccaya', name: 'Predominance Condition', desc: '4 predominant factors (chanda, vīriya, citta, vīmaṃsā) or an esteemed object dominating cognition.' },
      { id: 4, pali: 'Anantara-paccaya', name: 'Proximity Condition', desc: 'Each ceasing citta immediately giving rise to its successor in the cognitive stream.' },
      { id: 5, pali: 'Samanantara-paccaya', name: 'Contiguity Condition', desc: 'Seamless, uninterrupted succession between consecutive moments of consciousness.' },
      { id: 6, pali: 'Sahajāta-paccaya', name: 'Co-nascence Condition', desc: 'Phenomena conditioning one another by arising simultaneously (like a candle flame and its light).' },
      { id: 7, pali: 'Aññamañña-paccaya', name: 'Mutuality Condition', desc: 'Co-nascent states that mutually and reciprocally support each other (like three sticks leaning together).' },
      { id: 8, pali: 'Nissaya-paccaya', name: 'Dependence / Support Condition', desc: 'Serves as the foundation or ground for another state (like earth supporting trees or canvas supporting a painting).' },
      { id: 9, pali: 'Upanissaya-paccaya', name: 'Decisive Support Condition', desc: 'Powerful inducement (by object predominance, proximity, or natural decisive support / pakatūpanissaya).' },
      { id: 10, pali: 'Purejāta-paccaya', name: 'Pre-nascence Condition', desc: 'Previously arisen matter (the 6 physical bases and 5 present sense objects) supporting subsequently arising mind.' },
      { id: 11, pali: 'Pacchājāta-paccaya', name: 'Post-nascence Condition', desc: 'Subsequently arising citta and cetasikas sustaining and vitalizing the previously arisen physical body.' },
      { id: 12, pali: 'Āsevana-paccaya', name: 'Repetition Condition', desc: 'Each javana moment imparting greater proficiency and momentum to the succeeding javana of the same ethical quality.' },
      { id: 13, pali: 'Kamma-paccaya', name: 'Kamma Condition', desc: 'Volition (cetanā) coordinating co-nascent states (sahajāta) or producing future resultant fruits (nānākkhaṇika).' },
      { id: 14, pali: 'Vipāka-paccaya', name: 'Resultant Condition', desc: 'Resultant cittas and cetasikas mutually tranquilizing each other in effortless, passive maturation.' },
      { id: 15, pali: 'Āhāra-paccaya', name: 'Nutriment Condition', desc: 'The 4 nutriments (material ojā, phassa, manosañcetanā, and viññāṇa) sustaining mind and body.' },
      { id: 16, pali: 'Indriya-paccaya', name: 'Faculty Condition', desc: 'The 22 faculties (indriyas) exercising sovereignty and control within their respective domains (5 physical + mana + itthi + purisa + jīvita + 5 vedanā + 5 spiritual + 3 supramundane).' },
      { id: 17, pali: 'Jhāna-paccaya', name: 'Jhāna Condition', desc: 'The 7 jhāna factors closely examining and absorbing the mind into its object.' },
      { id: 18, pali: 'Magga-paccaya', name: 'Path Condition', desc: 'The 12 path factors (8 right + 4 wrong) leading to noble liberation or woeful states.' },
      { id: 19, pali: 'Sampayutta-paccaya', name: 'Association Condition', desc: 'Citta and cetasikas inseparably blended (sharing the same arising, cessation, object, and base).' },
      { id: 20, pali: 'Vippayutta-paccaya', name: 'Dissociation Condition', desc: 'Mental and material phenomena assisting one another while remaining distinct in nature.' },
      { id: 21, pali: 'Atthi-paccaya', name: 'Presence Condition', desc: 'A phenomenon supporting another by remaining present at the same time.' },
      { id: 22, pali: 'Natthi-paccaya', name: 'Absence Condition', desc: 'A preceding citta that, by completely ceasing, makes room for the succeeding citta to arise.' },
      { id: 23, pali: 'Vigata-paccaya', name: 'Disappearance Condition', desc: 'The complete disappearance of the preceding mental state enabling cognitive succession.' },
      { id: 24, pali: 'Avigata-paccaya', name: 'Non-Disappearance Condition', desc: 'A phenomenon supporting another so long as it has not yet disappeared (co-extensive with Atthi-paccaya).' },
    ],
  },
  es: {
    title: 'Matrices Estructurales del Abhidhammatthasaṅgaha',
    subtitle: 'Síntesis completa de conteos canónicos, estructuras y relaciones',
    cittaTab: 'Conciencia (89 / 121)',
    cetasikaTab: 'Factores Mentales (52)',
    rupaTab: 'Materia (28)',
    kiccaTab: '14 Funciones Mentales',
    paccayaTab: '24 Condiciones (Paccayas)',
    kiccaCountLabel: 'Cittas capaces:',
    cittaCards: [
      {
        title: '1. Akusala Citta (12)',
        color: '#DC2626',
        desc: 'Conciencias perjudiciales enraizadas en codicia, aversión e ignorancia (lobha, dosa, moha).',
        items: [
          { bold: 'Lobha-mūla (8):', text: ' 4 con somanassa, 4 con upekkhā; 4 con diṭṭhi, 4 sin diṭṭhi; 4 asaṅkhārika (espontáneas), 4 sasaṅkhārika (inducidas).' },
          { bold: 'Dosa-mūla (2):', text: ' Ambas con domanassa y paṭigha (aversión); 1 asaṅkhārika, 1 sasaṅkhārika.' },
          { bold: 'Moha-mūla (2):', text: ' Ambas con upekkhā; 1 con vicikicchā (duda), 1 con uddhacca (agitación).' },
        ],
      },
      {
        title: '2. Ahetuka Citta (18)',
        color: '#64748B',
        desc: 'Conciencias sin raíces éticas (hetu) asociadas.',
        items: [
          { bold: 'Akusala-vipāka (7):', text: ' 5 sentidos resultantes perjudiciales + 1 sampaṭicchana (recepción) + 1 santīraṇa neutro.' },
          { bold: 'Kusala-vipāka (8):', text: ' 5 sentidos resultantes saludables + 1 sampaṭicchana + 2 santīraṇa (1 upekkhā, 1 somanassa).' },
          { bold: 'Ahetuka-kiriya (3):', text: ' Pañcadvārāvajjana (5 puertas), Manodvārāvajjana (puerta mental / determinación), Hasituppāda (sonrisa del Arahant).' },
        ],
      },
      {
        title: '3. Kāmāvacara Sobhana (24)',
        color: '#16A34A',
        desc: 'Conciencias bellas de la esfera sensorial (8 × 3 clases = 24).',
        items: [
          { bold: 'Mahā-kusala (8):', text: ' Acciones saludables de la esfera sensorial (4 somanassa / 4 upekkhā; 4 ñāṇasampayutta / 4 ñāṇavippayutta).' },
          { bold: 'Mahā-vipāka (8):', text: ' Resultantes saludables sensoriales (operan en paṭisandhi, bhavaṅga, cuti y tadārammaṇa).' },
          { bold: 'Mahā-kiriya (8):', text: ' Conciencias funcionales bellas exclusivas de los Arahants.' },
        ],
      },
      {
        title: '4. Mahaggata & Lokuttara (35 o 67)',
        color: '#7C3AED',
        desc: 'Conciencias sublimes (27) y supramundanas (8 o 40).',
        items: [
          { bold: 'Rūpāvacara (15):', text: ' 5 Kusala + 5 Vipāka + 5 Kiriya (5 Jhānas de la materia sutil en el sistema quíntuple).' },
          { bold: 'Arūpāvacara (12):', text: ' 4 Kusala + 4 Vipāka + 4 Kiriya (4 absorciones inmateriales, todas con factores del 5º Jhāna).' },
          { bold: 'Lokuttara (8 o 40):', text: ' 4 Magga (Caminos) + 4 Phala (Frutos). Multiplicados por los 5 niveles de Jhāna = 40.' },
        ],
      },
    ],
    cetasikaCards: [
      {
        title: '1. Aññasamāna (13)',
        color: '#0284C7',
        desc: 'Factores éticamente variables (adoptan la cualidad moral del citta).',
        items: [
          { bold: 'Sabbacittasādhāraṇa (7 Universales):', text: ' Phassa, Vedanā, Saññā, Cetanā, Ekaggatā, Jīvitindriya, Manasikāra.' },
          { bold: 'Pakiṇṇaka (6 Ocasionales):', text: ' Vitakka, Vicāra, Adhimokkha, Vīriya, Pīti, Chanda.' },
        ],
      },
      {
        title: '2. Akusala (14)',
        color: '#DC2626',
        desc: 'Factores mentales perjudiciales (exclusivos de los 12 Akusala Cittas).',
        items: [
          { bold: 'Mohacatukka (4 Universales Perjudiciales):', text: ' Moha, Ahirika, Anottappa, Uddhacca (presentes en los 12 akusalas).' },
          { bold: 'Lobhatika (3 Tríada de Codicia):', text: ' Lobha, Diṭṭhi (visión errónea), Māna (orgullo — nunca surge junto con diṭṭhi).' },
          { bold: 'Dosacatukka (4 Tétrada de Aversión):', text: ' Dosa, Issā (envidia), Macchariya (avaricia), Kukkucca (remordimiento).' },
          { bold: 'Thīnaduka (2) & Vicikicchā (1):', text: ' Thīna (pereza), Middha (torpor) en los 5 sasaṅkhārika; Vicikicchā (duda).' },
        ],
      },
      {
        title: '3. Sobhana (25)',
        color: '#16A34A',
        desc: 'Factores mentales bellos y puros (en los 59 o 91 Sobhana Cittas).',
        items: [
          { bold: 'Sobhanasādhāraṇa (19 Universales Bellos):', text: ' Saddhā, Sati, Hiri, Ottappa, Alobha, Adosa, Tatramajjhattatā y los 6 pares (kāya/citta passaddhi, lahutā, mudutā, kammaññatā, pāguññatā, ujukatā).' },
          { bold: 'Virati (3 Abstinencias):', text: ' Sammāvācā (Recta Palabra), Sammākammanta (Recta Acción), Sammā-ājīva (Recto Medio de Vida — simultáneas en Lokuttara).' },
          { bold: 'Appamaññā (2 Ilimitados) & Paññā (1):', text: ' Karuṇā (compasión), Muditā (alegría altruista) y Paññindriya (sabiduría, en los 47/79 tihetuka).' },
        ],
      },
    ],
    rupaCards: [
      {
        title: '1. Nipphanna Rūpa (18 Concretas)',
        color: '#B45309',
        desc: 'Materia con esencia intrínseca propia (Sabhāvarūpa), apta para la contemplación de insight (Sammasanarūpa).',
        items: [
          { bold: '4 Mahābhūta (Grandes Elementos):', text: ' Paṭhavī (tierra/solidez), Āpo (agua/cohesión — ¡intangible!), Tejo (fuego/temperatura), Vāyo (aire/distensión).' },
          { bold: '5 Pasādarūpa (Sensibilidades):', text: ' Cakkhu (ojo), Sota (oído), Ghāna (nariz), Jivhā (lengua), Kāya (cuerpo).' },
          { bold: '4 Gocararūpa (7 Objetos Sensoriales):', text: ' Rūpa (color/forma), Sadda (sonido), Gandha (olor), Rasa (sabor) [+ Phoṭṭhabba = 3 elementos: tierra, fuego, aire].' },
          { bold: '2 Bhāvarūpa (Sexos):', text: ' Itthatta (feminidad) y Purisatta (masculinidad).' },
          { bold: '1 Hadayarūpa, 1 Jīvitarūpa, 1 Āhārarūpa:', text: ' Base del corazón (hadayavatthu), facultad vital material (jīvitindriya) y esencia nutritiva (ojā).' },
        ],
      },
      {
        title: '2. Anipphanna Rūpa (10 No-Concretas)',
        color: '#0369A1',
        desc: 'Modos, límites, expresiones y fases temporales de las 18 materias concretas.',
        items: [
          { bold: '1 Paricchedarūpa (Espacio):', text: ' Ākāsadhātu (espacio delimitador entre grupos materiales / kalāpas).' },
          { bold: '2 Viññattirūpa (Expresiones):', text: ' Kāyaviññatti (expresión corporal) y Vacīviññatti (expresión vocal).' },
          { bold: '3 Vikārarūpa (Mutabilidades):', text: ' Lahutā (ligereza), Mudutā (maleabilidad), Kammaññatā (adaptabilidad).' },
          { bold: '4 Lakkhaṇarūpa (Características):', text: ' Upacaya (surgimiento), Santati (continuidad), Jarā (envejecimiento) y Aniccatā (disolución).' },
        ],
      },
    ],
    kiccas: [
      { num: 1, name: 'Paṭisandhi (Renacimiento)', count: '19', desc: 'Conecta la vida anterior con la nueva existencia (2 santīraṇa upekkhā + 8 mahāvipāka + 5 rūpavipāka + 4 arūpavipāka).' },
      { num: 2, name: 'Bhavaṅga (Continuo Vital)', count: '19', desc: 'Mantiene la continuidad pasiva de la vida entre procesos cognitivos (los mismos 19 cittas de paṭisandhi).' },
      { num: 3, name: 'Āvajjana (Advertencia)', count: '2', desc: 'Dirige la atención al objeto: Pañcadvārāvajjana (5 puertas) y Manodvārāvajjana (puerta mental).' },
      { num: 4, name: 'Dassana (Ver)', count: '2', desc: 'Conciencia visual del ojo (2 cakkhuviññāṇa: akusalavipāka y kusalavipāka).' },
      { num: 5, name: 'Savana (Oír)', count: '2', desc: 'Conciencia auditiva del oído (2 sotaviññāṇa).' },
      { num: 6, name: 'Ghāyana (Oler)', count: '2', desc: 'Conciencia olfativa de la nariz (2 ghānaviññāṇa).' },
      { num: 7, name: 'Sāyana (Saborear)', count: '2', desc: 'Conciencia gustativa de la lengua (2 jivhāviññāṇa).' },
      { num: 8, name: 'Phusana (Tocar)', count: '2', desc: 'Conciencia táctil del cuerpo (2 kāyaviññāṇa: con dukkha o sukha).' },
      { num: 9, name: 'Sampaṭicchana (Recepción)', count: '2', desc: 'Recibe el objeto sensorial en las 5 puertas inmediatamente después del sentido.' },
      { num: 10, name: 'Santīraṇa (Investigación)', count: '3', desc: 'Examina e investiga el objeto recibido (3 santīraṇacittas).' },
      { num: 11, name: 'Voṭṭhabbana (Determinación)', count: '1', desc: 'Determina el objeto en las 5 puertas antes del javana (realizada por el Manodvārāvajjana).' },
      { num: 12, name: 'Javana (Impulso Kámmico)', count: '55 (u 87)', desc: 'Fase activa volitiva: 12 akusala + 1 hasituppāda + 8 mahākusala + 8 mahākiriya + 10 rūpa + 8 arūpa + 8/40 lokuttara.' },
      { num: 13, name: 'Tadārammaṇa (Registro)', count: '11', desc: 'Registra el objeto muy claro en la esfera sensorial por 2 momentos tras el javana (3 santīraṇa + 8 mahāvipāka).' },
      { num: 14, name: 'Cuti (Muerte)', count: '19', desc: 'Último momento mental que cierra una existencia (idéntico al paṭisandhi y bhavaṅga de esa vida).' },
    ],
    paccayas: [
      { id: 1, pali: 'Hetu-paccaya', name: 'Condición de Raíz', desc: 'Las 6 raíces éticas sosteniendo mente y materia co-nacida como las raíces de un árbol.' },
      { id: 2, pali: 'Ārammaṇa-paccaya', name: 'Condición de Objeto', desc: 'Todo objeto cognoscible que sostiene el surgimiento de citta y cetasikas como el bastón que apoya a un anciano.' },
      { id: 3, pali: 'Adhipati-paccaya', name: 'Condición de Predominancia', desc: 'Los 4 factores soberanos (chanda, vīriya, citta, vīmaṃsā) o un objeto supremo gobernando la mente.' },
      { id: 4, pali: 'Anantara-paccaya', name: 'Condición de Proximidad', desc: 'Cesa para dar paso inmediato al siguiente citta sin intervalo.' },
      { id: 5, pali: 'Samanantara-paccaya', name: 'Condición de Contigüidad Inmediata', desc: 'Continuidad perfecta e ininterrumpida del flujo mental.' },
      { id: 6, pali: 'Sahajāta-paccaya', name: 'Condición de Co-nacimiento', desc: 'Como la llama y la luz surgiendo exactamente al mismo tiempo.' },
      { id: 7, pali: 'Aññamañña-paccaya', name: 'Condición de Mutualidad', desc: 'Como 3 bastones apoyados recíprocamente en un trípode.' },
      { id: 8, pali: 'Nissaya-paccaya', name: 'Condición de Soporte / Dependencia', desc: 'Como la tierra que sostiene los árboles o el lienzo para una pintura.' },
      { id: 9, pali: 'Upanissaya-paccaya', name: 'Condición de Soporte Decisivo', desc: 'Inducción poderosa por objeto, proximidad o soporte natural (pakatūpanissaya).' },
      { id: 10, pali: 'Purejāta-paccaya', name: 'Condición Pre-nacida', desc: 'Materia surgida antes (las 6 bases y 5 objetos sensoriales presentes) apoyando a la mente.' },
      { id: 11, pali: 'Pacchājāta-paccaya', name: 'Condición Post-nacida', desc: 'Mente posterior sosteniendo el cuerpo físico previamente nacido.' },
      { id: 12, pali: 'Āsevana-paccaya', name: 'Condición de Repetición', desc: 'Cada momento de javana fortalece e intensifica al siguiente javana de igual cualidad ética.' },
      { id: 13, pali: 'Kamma-paccaya', name: 'Condición de Kamma', desc: 'Volición (cetanā) simultánea (sahajāta) o asíncrona (nānākkhaṇika) generando frutos.' },
      { id: 14, pali: 'Vipāka-paccaya', name: 'Condición de Resultante', desc: 'Estados mentales pasivos de maduración que se calman mutuamente.' },
      { id: 15, pali: 'Āhāra-paccaya', name: 'Condición de Nutriente', desc: 'Los 4 alimentos (ojā material, phassa, manosañcetanā y viññāṇa) que sostienen cuerpo y mente.' },
      { id: 16, pali: 'Indriya-paccaya', name: 'Condición de Facultad', desc: 'Las 22 facultades (indriyas) ejerciendo soberanía en su respectivo dominio (5 físicas + mana + itthi + purisa + jīvita + 5 vedanā + 5 espirituales + 3 supramundanas).' },
      { id: 17, pali: 'Jhāna-paccaya', name: 'Condición de Jhāna', desc: 'Los 7 factores de jhāna fijando la mente en la absorción del objeto.' },
      { id: 18, pali: 'Magga-paccaya', name: 'Condición de Camino', desc: 'Los 12 factores de camino conduciendo hacia destinos nobles o inferiores.' },
      { id: 19, pali: 'Sampayutta-paccaya', name: 'Condición de Asociación', desc: 'Citta y cetasikas fusionados inseparablemente (como agua y leche).' },
      { id: 20, pali: 'Vippayutta-paccaya', name: 'Condición de Disociación', desc: 'Mente y materia operando juntas sin confundir sus naturalezas.' },
      { id: 21, pali: 'Atthi-paccaya', name: 'Condición de Presencia', desc: 'Auxilia existiendo en el momento presente.' },
      { id: 22, pali: 'Natthi-paccaya', name: 'Condición de Ausencia', desc: 'Auxilia cesando para dar lugar al siguiente citta.' },
      { id: 23, pali: 'Vigata-paccaya', name: 'Condición de Desaparición', desc: 'La desaparición del estado anterior condicionando el surgimiento del siguiente.' },
      { id: 24, pali: 'Avigata-paccaya', name: 'Condición de No-Desaparición', desc: 'La no-cesación manteniendo el soporte activo (co-extensivo con Atthi-paccaya).' },
    ],
  },
};

export const CompendiumMatrix: React.FC = () => {
  const dispatch = useAppDispatch();
  const reduxLang = useAppSelector((s) => s.settings.uiLanguage);
  const layout = useLayout();
  const lang: Language = reduxLang;

  const [activeTab, setActiveTab] = useState<'citta' | 'cetasika' | 'rupa' | 'kicca' | 'paccaya'>('citta');

  const t = MATRIX_DATA[lang];

  const renderGroupCards = (cards: MatrixGroupCard[]) => (
    <View style={styles.cardGrid}>
      {cards.map((card, idx) => (
        <View key={idx} style={styles.card}>
          <Text style={[styles.cardTitle, { color: card.color }]}>{card.title}</Text>
          <Text style={styles.cardDesc}>{card.desc}</Text>
          {card.items.map((item, iIdx) => (
            <Text key={iIdx} style={styles.cardItem}>
              • {item.bold ? <Text style={{ fontWeight: 'bold' }}>{item.bold}</Text> : null}
              {item.text}
            </Text>
          ))}
        </View>
      ))}
    </View>
  );

  return (
    <ScrollView style={styles.container} contentContainerStyle={[styles.contentContainer, { paddingHorizontal: layout.pagePadding }]}>
      {/* Header */}
      <View style={styles.header}>
        <View style={{ flex: 1, minWidth: 200 }}>
          <Text style={styles.headerTitle}>📊 {t.title}</Text>
          <Text style={styles.headerSubtitle}>{t.subtitle}</Text>
        </View>

        <View style={styles.langSelector}>
          {(['pt', 'en', 'es'] as Language[]).map((l) => (
            <TouchableOpacity
              key={l}
              style={[styles.langBtn, lang === l && styles.langBtnActive]}
              onPress={() => dispatch(setUiLanguage(l))}
            >
              <Text style={[styles.langBtnText, lang === l && styles.langBtnTextActive]}>
                {l.toUpperCase()}
              </Text>
            </TouchableOpacity>
          ))}
        </View>
      </View>

      {/* Tabs */}
      <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.tabsScroll}>
        <TouchableOpacity
          style={[styles.tab, activeTab === 'citta' && styles.tabActive]}
          onPress={() => setActiveTab('citta')}
        >
          <Text style={[styles.tabText, activeTab === 'citta' && styles.tabTextActive]}>
            {t.cittaTab}
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.tab, activeTab === 'cetasika' && styles.tabActive]}
          onPress={() => setActiveTab('cetasika')}
        >
          <Text style={[styles.tabText, activeTab === 'cetasika' && styles.tabTextActive]}>
            {t.cetasikaTab}
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.tab, activeTab === 'rupa' && styles.tabActive]}
          onPress={() => setActiveTab('rupa')}
        >
          <Text style={[styles.tabText, activeTab === 'rupa' && styles.tabTextActive]}>
            {t.rupaTab}
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.tab, activeTab === 'kicca' && styles.tabActive]}
          onPress={() => setActiveTab('kicca')}
        >
          <Text style={[styles.tabText, activeTab === 'kicca' && styles.tabTextActive]}>
            {t.kiccaTab}
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.tab, activeTab === 'paccaya' && styles.tabActive]}
          onPress={() => setActiveTab('paccaya')}
        >
          <Text style={[styles.tabText, activeTab === 'paccaya' && styles.tabTextActive]}>
            {t.paccayaTab}
          </Text>
        </TouchableOpacity>
      </ScrollView>

      {/* CITTA */}
      {activeTab === 'citta' && renderGroupCards(t.cittaCards)}

      {/* CETASIKA */}
      {activeTab === 'cetasika' && renderGroupCards(t.cetasikaCards)}

      {/* RUPA */}
      {activeTab === 'rupa' && renderGroupCards(t.rupaCards)}

      {/* KICCA */}
      {activeTab === 'kicca' && (
        <View style={styles.listContainer}>
          {t.kiccas.map((k) => (
            <View key={k.num} style={styles.kiccaCard}>
              <Text style={styles.kiccaTitle}>{k.num}. {k.name}</Text>
              <Text style={styles.kiccaCount}>{t.kiccaCountLabel} {k.count}</Text>
              <Text style={styles.kiccaDesc}>{k.desc}</Text>
            </View>
          ))}
        </View>
      )}

      {/* PACCAYA */}
      {activeTab === 'paccaya' && (
        <View style={styles.listContainer}>
          {t.paccayas.map((p) => (
            <View key={p.id} style={styles.paccayaCard}>
              <Text style={styles.paccayaPali}>{p.id}. {p.pali}</Text>
              <Text style={styles.paccayaName}>{p.name}</Text>
              <Text style={styles.paccayaDesc}>{p.desc}</Text>
            </View>
          ))}
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
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    flexWrap: 'wrap',
    gap: 12,
    marginBottom: 16,
    paddingBottom: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#D8CBB5',
  },
  headerTitle: {
    color: '#4B2E2A',
    fontSize: 20,
    fontWeight: 'bold',
  },
  headerSubtitle: {
    color: '#6B5A4B',
    fontSize: 13,
  },
  langSelector: {
    flexDirection: 'row',
    backgroundColor: '#EADFC9',
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
    backgroundColor: '#4B2E2A',
  },
  langBtnText: {
    color: '#4B2E2A',
    fontSize: 12,
    fontWeight: 'bold',
  },
  langBtnTextActive: {
    color: '#FFF',
  },
  tabsScroll: {
    gap: 8,
    paddingBottom: 12,
  },
  tab: {
    paddingHorizontal: 14,
    paddingVertical: 8,
    borderRadius: 8,
    backgroundColor: '#EADFC9',
  },
  tabActive: {
    backgroundColor: '#4B2E2A',
  },
  tabText: {
    color: '#4B2E2A',
    fontSize: 13,
    fontWeight: 'bold',
  },
  tabTextActive: {
    color: '#FFF',
  },
  cardGrid: {
    gap: 12,
  },
  card: {
    backgroundColor: '#FFFDF7',
    borderRadius: 10,
    padding: 16,
    borderWidth: 1,
    borderColor: '#D8CBB5',
  },
  cardTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  cardDesc: {
    color: '#6B5A4B',
    fontSize: 13,
    marginBottom: 10,
  },
  cardItem: {
    color: '#2D1E1B',
    fontSize: 13,
    lineHeight: 20,
    marginBottom: 4,
  },
  listContainer: {
    gap: 10,
  },
  kiccaCard: {
    backgroundColor: '#FFFDF7',
    padding: 12,
    borderRadius: 8,
    borderLeftWidth: 4,
    borderLeftColor: '#8C2D19',
    borderWidth: 1,
    borderColor: '#D8CBB5',
  },
  kiccaTitle: {
    color: '#4B2E2A',
    fontSize: 14,
    fontWeight: 'bold',
  },
  kiccaCount: {
    color: '#8C2D19',
    fontSize: 12,
    fontWeight: '600',
    marginVertical: 2,
  },
  kiccaDesc: {
    color: '#4A3B32',
    fontSize: 13,
  },
  paccayaCard: {
    backgroundColor: '#FFFDF7',
    padding: 12,
    borderRadius: 8,
    borderLeftWidth: 4,
    borderLeftColor: '#4B2E2A',
    borderWidth: 1,
    borderColor: '#D8CBB5',
  },
  paccayaPali: {
    color: '#8C2D19',
    fontSize: 14,
    fontWeight: 'bold',
  },
  paccayaName: {
    color: '#4B2E2A',
    fontSize: 13,
    fontWeight: '600',
    marginVertical: 2,
  },
  paccayaDesc: {
    color: '#4A3B32',
    fontSize: 13,
  },
});

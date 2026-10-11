# Guia Completo de Implantação (Deploy) com GitHub Desktop e GitHub Actions

Este documento orienta o processo de implantação (*deploy*) do leitor canônico **Abhidhammatthasaṅgaha**, utilizando o **GitHub Desktop** e o pipeline de CI/CD automatizado via **GitHub Actions**.

---

## 1. Dados e Credenciais do Projeto

* **Diretório Local:** `/Users/pauloo/Desktop/abhidhammatthasangaha`
* **Usuário GitHub:** `PJ-Oliveira` (Paulo)
* **Email Git Configurado:** `84526032+PJ-Oliveira@users.noreply.github.com`
* **Repositório Remoto:** `https://github.com/PJ-Oliveira/abhidhammatthasangaha.git`
* **Branch Principal:** `main`
* **Branch de Deploy do GitHub Pages:** `gh-pages`

---

## 2. Como Adicionar o Projeto no GitHub Desktop

Como o repositório Git local já foi inicializado e configurado com a `origin` apontando para `https://github.com/PJ-Oliveira/abhidhammatthasangaha.git`:

1. Abra o aplicativo **GitHub Desktop** no seu Mac.
2. No menu superior, clique em **File** → **Add Local Repository...** (ou pressione `Cmd + O`).
3. Clique em **Choose...** e selecione a pasta:
   ```
   /Users/pauloo/Desktop/abhidhammatthasangaha
   ```
4. Clique no botão **Add Repository**.
5. O GitHub Desktop reconhecerá imediatamente o repositório `abhidhammatthasangaha` com a branch `main`.

---

## 3. Realizando o Primeiro Commit e Push no GitHub Desktop

1. No painel esquerdo do **GitHub Desktop**, você verá os arquivos do projeto listados na aba **Changes**.
2. No canto inferior esquerdo (Summary):
   * Digite o título do commit:
     ```
     feat: leitor canônico Abhidhammatthasaṅgaha com alinhamento por sentença, i18n, rotas URL e exportação
     ```
   * No campo de descrição opcional:
     ```
     - Suporte a 4 idiomas (Pāli, EN, PT, ES)
     - Dicionário offline embutido com navegação e peek card mobile
     - Rotas canônicas (/1, /1/abhm-1.3) com âncoras e cópia de link
     - Exportação completa em EPUB 3 e PDF com numeração de páginas
     - CI/CD automatizado para GitHub Pages
     ```
3. Clique no botão azul **Commit to main**.
4. No topo da barra superior do GitHub Desktop, clique em **Publish branch** (ou **Push origin**).
   * O GitHub Desktop utilizará automaticamente a autenticação e credenciais já salvas na sua conta (`PJ-Oliveira`).

---

## 4. Deploy Automatizado via CI/CD (GitHub Actions)

Assim que o push for concluído na branch `main`, a automação configurada em `.github/workflows/deploy.yml` será disparada automaticamente no GitHub:

1. **Instalação e Validação:** Executa `npm ci`, verificação estrita de tipos com TypeScript (`tsc --noEmit`) e todos os 122 testes automatizados (`npm test`).
2. **Build Estático:** Compila a aplicação para a web (`npm run build:web`).
3. **Publicação no GitHub Pages:** Publica a pasta `./dist` na branch `gh-pages`.

### Como Ativar o GitHub Pages no Repositório (Única vez)
1. Acesse o seu repositório no navegador: `https://github.com/PJ-Oliveira/abhidhammatthasangaha/settings/pages`
2. Na seção **Build and deployment**:
   * Em **Source**, selecione: **Deploy from a branch**.
   * Em **Branch**, selecione: `gh-pages` e a pasta `/ (root)`.
   * Clique em **Save**.
3. O site estará disponível publicamente em:
   ```
   https://pj-oliveira.github.io/abhidhammatthasangaha/
   ```

---

## 5. Como Testar Localmente

Para rodar a aplicação localmente no seu computador:
```bash
cd /Users/pauloo/Desktop/abhidhammatthasangaha
npx expo start --web --port 8081
```
Acesse no navegador:
* Tratado completo / Capítulo 1: `http://localhost:8081/abhidhammatthasaṅgaha/1`
* Link direto para parágrafo: `http://localhost:8081/abhidhammatthasaṅgaha/1/abhm-1.3`
* Capítulo 2: `http://localhost:8081/abhidhammatthasaṅgaha/2`

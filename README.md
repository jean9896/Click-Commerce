# Click Commerce — Landing

Esta pasta contém a versão estática da landing page da Click Commerce.

Instruções rápidas (desenvolvimento e produção):

- Instalar dependências de desenvolvimento (Tailwind CLI):

```bash
npm ci
```


- Gerar site para produção (gera `dist/`):

```bash
npm ci
npm run build
```

- Gerar HTML limpo (script Python) e saída em `dist/`:

```bash
npm run clean-html
```

- Rodar servidor local (serve `dist/`):

```bash
npm start
```

Sugestões de deploy: GitHub Pages (apenas arquivos estáticos), Netlify ou Vercel. O workflow do CI (GitHub Actions) já executa `npm ci` e `npm run build` no push para `main`.

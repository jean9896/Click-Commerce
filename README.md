Projeto reorganizado — pronto para produção

- Arquivos principais:
  - `index.html` — página de entrada (movida e caminhos ajustados para `assets/...`).
  - `assets/css/index-CWxZw2E6.css` — stylesheet principal.
  - `assets/css/css2` — declarations de fontes (Google Fonts salvadas).
  - `assets/js/index-uNm_3oIC.js.baixados` — bundle JS (não modificado).
  - `assets/html/saved_resource.html` — HTML salvo de referência.
  - `backup/` — backup dos arquivos originais antes das alterações.

- Testar localmente:
  1. Abra `index.html` no navegador para uma verificação rápida.
  2. Para servir via HTTP (recomendado), execute no diretório do projeto:

```powershell
python -m http.server 8000
# ou (se preferir PowerShell):
# Start-Process -NoNewWindow -FilePath python -ArgumentList '-m http.server 8000'
```

Em seguida abra `http://localhost:8000/` e verifique a interface (pressione Ctrl+S para validar o salvamento do front-end).

- Observações importantes:
  - O bundle JS é grande e foi mantido sem alterações para preservar exatamente a interface.
  - Arquivos removidos: `config.js.baixados` e `8e98006f77.js.baixados` (backup em `backup/`).
  - Se houver diferenças visuais, restaure os originais de `backup/` e me avise quais recursos falharam.

Se quiser, eu posso:
- criar um zip de distribuição,
- inicializar um repositório Git e commitar as mudanças,
- ou gerar um script de deploy (FTP/SCP).

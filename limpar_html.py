import re
import html

def limpar_site(arquivo_entrada, arquivo_saida):
    print("Iniciando a limpeza do HTML...")
    
    with open(arquivo_entrada, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    # ==========================================
    # FASE 1: Desencapsulamento
    # ==========================================
    # Captura o texto gigante dentro do srcdoc="..."
    match = re.search(r'srcdoc="(.*?)"\s+style=', conteudo, re.DOTALL)
    if not match:
        print("Aviso: atributo srcdoc não encontrado — copiando arquivo de origem para saída.")
        # fallback: simplesmente copiar o arquivo de entrada para a saída
        import shutil, os
        os.makedirs(os.path.dirname(arquivo_saida) or '.', exist_ok=True)
        shutil.copy2(arquivo_entrada, arquivo_saida)
        print(f"✓ Arquivo copiado: {arquivo_entrada} -> {arquivo_saida}")
        return
    else:
        html_encodado = match.group(1)
        # Decodifica as entidades HTML (&lt; para <, &quot; para ", etc.)
        html_limpo = html.unescape(html_encodado)
        print("✓ Fase 1 concluída: HTML desencapsulado e decodificado.")

    # ==========================================
    # FASE 2: Limpeza de "Lixo" do Editor
    # ==========================================
    # Remove o script do editor no final do arquivo
    html_limpo = re.sub(r'<script src="/embed/main\.umd\.js"></script>', '', html_limpo)
    
    # Remove o bloco de CSS de edição (hovered-element, etc)
    html_limpo = re.sub(r'<style>\s*\.hovered-element.*?</style>', '', html_limpo, flags=re.DOTALL)
    
    # Remove os atributos data- de rastreamento e edição
    html_limpo = re.sub(r'\sdata-(update-id|media|logo|landingsite-[a-z-]+)(="[^"]*")?', '', html_limpo)
    print("✓ Fase 2 concluída: Lixo do construtor visual removido.")

    # ==========================================
    # FASE 3: Performance e Otimização
    # ==========================================
    # Substitui o Tailwind CDN por uma chamada de CSS local
    tag_tailwind = '<script src="https://cdn.tailwindcss.com"></script>'
    tag_css_local = '\n    <link rel="stylesheet" href="style.css">'
    html_limpo = html_limpo.replace(tag_tailwind, tag_css_local)
    
    # Adiciona loading="lazy" em todas as tags <img> que ainda não possuem
    html_limpo = re.sub(r'(<img\b(?![^>]*\bloading=)[^>]*?)(\/?>)', r'\1 loading="lazy"\2', html_limpo)
    print("✓ Fase 3 concluída: Otimizações de performance aplicadas.")

    # ==========================================
    # FASE 4: Funcionalidade Real
    # ==========================================
    # Ajusta o Formulário de Contato
    # (Como o data-landingsite já foi removido na Fase 2, buscamos pela classe que sobrou)
    html_limpo = html_limpo.replace(
        '<form class="space-y-4">', 
        '<form action="https://formsubmit.co/contato@digitalhubmarket.com" method="POST" class="space-y-4">'
    )
    
    # Ajusta os Links de Navegação (Transformando em âncoras da Single Page)
    html_limpo = html_limpo.replace('href="/sobre"', 'href="#su0a1l"')
    html_limpo = html_limpo.replace('href="/fornecedores"', 'href="#spjeg53"')
    html_limpo = html_limpo.replace('href="/contato"', 'href="#contact-section"')
    html_limpo = html_limpo.replace('href="/"', 'href="#global-header"') # Faz o logo voltar ao topo
    
    # Corrige link que estava apenas como /politica-de-privacidade (Opcional: apontar para topo ou manter como hashtag vazia caso não exista a página ainda)
    html_limpo = html_limpo.replace('href="/politica-de-privacidade"', 'href="#"')
    html_limpo = html_limpo.replace('href="/termos-de-uso"', 'href="#"')
    
    print("✓ Fase 4 concluída: Formulário e links internos ajustados.")

    # ==========================================
    # Salvar o arquivo
    # ==========================================
    # Garantir pasta de saída
    import os
    os.makedirs(os.path.dirname(arquivo_saida) or '.', exist_ok=True)
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        f.write(html_limpo)

    print(f"\n🚀 Sucesso! O arquivo otimizado foi salvo como: {arquivo_saida}")

    # ==========================================
    # FASE 5: Gerar o CSS com Tailwind
    # ==========================================
    print("\nIniciando o Tailwind para gerar o style.css (saída: dist/style.css)...")
    import subprocess
    try:
        subprocess.run(["npx", "tailwindcss", "-i", "./src/index.css", "-o", "./dist/style.css", "--minify"], check=True)
    except Exception:
        # Fallback para sistemas onde npx não esteja disponível no PATH
        subprocess.run("npx tailwindcss -i ./src/index.css -o ./dist/style.css --minify", shell=True)
    print("✨ Processo 100% concluído! Pode abrir o index_limpo.html")

# Executa a função
limpar_site('src/index.html', 'dist/index.html')
# Portfólio Profissional — Rickelme Gouveia

Site de página única para apresentar a trajetória, os estudos e os projetos digitais de Rickelme Gouveia para recrutadores de vagas de Jovem Aprendiz em tecnologia, desenvolvimento, administração, operações e automação.

## Conteúdo atual

O portfólio inclui uma apresentação baseada no currículo confirmado, uma seção de habilidades com distinção entre prática e estudos, o projeto DOMINÓ 2, a descrição do uso responsável de ferramentas de IA, a apresentação Canva **Dominó 2** (7 páginas), uma área reservada para os dois sites do CIEE e projetos futuros, além de contato por GitHub e e-mail. O LinkedIn fica como campo pendente até que seja fornecida a URL direta do perfil.

Também inclui uma seção de evolução técnica e três experimentos originais em pixel art: um personagem com caminhada curta, um terminal com cursor e um ambiente com estrelas. Os movimentos são leves, usam SVG/CSS sem dependências adicionais e são desativados quando o sistema indica preferência por redução de movimento.

A descrição do DOMINÓ 2 foi limitada ao que está disponível no repositório [CIEE-EDN/CIEE-Rickelme](https://github.com/CIEE-EDN/CIEE-Rickelme) e na demonstração publicada em [ciee-edn.github.io/CIEE-Rickelme](https://ciee-edn.github.io/CIEE-Rickelme/). As outras oito apresentações do Canva foram analisadas, mas não são publicadas sem aprovação.

## Executar localmente

O projeto é estático e não possui dependências externas de build. Em um terminal na raiz do projeto, execute:

```bash
python3 -m http.server 3000 --bind 0.0.0.0
```

Depois acesse `http://localhost:3000/`.

## Estrutura

- `index.html` — conteúdo semântico da página única.
- `styles.css` — identidade visual, responsividade, acessibilidade e animações.
- `script.js` — menu móvel e entradas suaves com suporte a `prefers-reduced-motion`.
- `assets/curriculo-rickelme-publico.pdf` (após aprovação) — versão pública redigida do currículo, sem endereço e contatos de responsáveis.
- `manus-routes.json` — declaração da rota pública `/`.
- `assets/rg-mark.svg` — monograma RG e favicon em SVG.
- `TODO.md` — escopo, pendências e critérios de conclusão.
- `.github/workflows/pages.yml` — tentativa automatizada de publicação no GitHub Pages, dependente da habilitação inicial do Pages.

## Publicação no GitHub Pages

O destino solicitado é o repositório público `CIEE-EDN/portfolio-rickelme`. O workflow `.github/workflows/pages.yml` já está preparado para publicar a raiz do projeto pela branch `main`, mas a habilitação inicial do Pages exige permissão administrativa que não estava disponível para a integração usada nesta sessão. Para concluir no GitHub, abra **Settings → Pages**, selecione **GitHub Actions** como fonte e aguarde o workflow `Deploy portfolio to GitHub Pages`. A URL esperada é `https://ciee-edn.github.io/portfolio-rickelme/`; ela só deve ser divulgada como publicada depois de responder corretamente.

Antes da publicação, revisar a aprovação da versão redigida do currículo. Não adicionar o endereço residencial ou contatos de responsáveis ao conteúdo visível do site.

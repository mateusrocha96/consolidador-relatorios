# Consolidador de Relatórios

Script Python que lê múltiplos relatórios de vendas em Excel, consolida tudo em uma única tabela e gera agregações por região e produto.

Esse foi meu primeiro projeto saindo de SQL/Excel para automação com Python.

## O que ele faz

1. Lê todos os arquivos `.xlsx` da pasta `dados/entrada`
2. Junta tudo em uma única tabela
3. Agrupa os dados por Região e Produto, somando a quantidade vendida
4. Exporta o resultado para `saida/relatorio_consolidado.xlsx`

## Como rodar

\`\`\`bash
pip install pandas openpyxl
python consolidador.py
\`\`\`

Coloque seus arquivos `.xlsx` dentro de `dados/entrada` antes de rodar.

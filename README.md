# Requisitos & observações.

# Utilities Library
  - Python 3.9.7;
  - Django 3.2.7;
  - Bootstrap 4;
  - Crispy-Forms;
 
# Requisitos
  - Aba Adicionar Produtos:
    - Adicionar projeto (Part, Asembly, Drawing);
    - Adicionar eDrawing .dwg;
    - Adicionar Dxf;
    - Adicionar PDF;
    - Adicionar Lista de Materiais (BOM) .xlsx;

# Notes:
  - 28/10/2021:  
    - Incluir label na aba de Produtos para que seja possível ter as escolhas de Ordenar; OK
    - "Classe" -> "Categoria"; OK
    - "Dureza" -> "Classe de aplicação"; OK
    - Criar novo módulo: Número de Série:
      - Botão de pesquisa de Produto; OK
      - Botão de Gerar Número de Série; OK
      - Gerar o Número de Série automaticamente após selecionar o Produto;
      - Label de pesquisa de Número de Série;
      - Deve Conter as informações do cadastro;

  - 29/10/2021:
    - Número de série contém um produto;
    - Número de série relaciona uma OS ao produto;
    - Histórico de OS aberta para "X" número de série;
    - Tabela na aba Número de série específica para tal;
    - Cadastro do número da OS para a relação com o produto;
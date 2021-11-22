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

# Serial Number:
  - 21cg3021001
  - Ano - produto - lamina - código numeral
# Notes:
  # 28/10/2021:  
    - Incluir label na aba de Produtos para que seja possível ter as escolhas de Ordenar; OK
    - "Classe" -> "Categoria"; OK
    - "Dureza" -> "Classe de aplicação"; OK
    - Criar novo módulo: Número de Série:
      - Botão de pesquisa de Produto; OK
      - Botão de Gerar Número de Série; OK
      - Gerar o Número de Série automaticamente após selecionar o Produto; OK
      - Label de pesquisa de Número de Série;
      - Deve Conter as informações do cadastro; OK

  # 29/10/2021:
    - Número de série contém um produto; OK
    - Número de série relaciona uma OS ao produto; OK
    - Histórico de OS aberta para "X" número de série; OK
    - Tabela na aba Número de série específica para tal; OK
    - Cadastro do número da OS para a relação com o produto; OK

  # 04/11/2021:
    - "Lâmina" = "Expessura"; OK
    - Cadastro e edição de categoria; OK
    - "Código" = "Tipo de Produto" - Cadastro e edição; OK
    - Cadastro e edição de classes; OK

  # 17/11/2021:
    - Remover e editar Segmentos, Tipo de Produto, Categoria e Classe de Aplicação; OK
    - Unidade de medida; OK
    - Trocar o nome "Lâmina" para Expessura; OK
    - Categoria pode ser Nulo; OK
    - Caixa de diálogo para Deletar e Editar Produto;
    - Em "Número de Série" a Ordem de Serviço deve ser digitável e não lista;
    - O mesmo para o Produto;
    - Selecionar quantos números de série por produto e OS;
    - Em "Produtos" criar coluna Descontinuado; OK

    - Dashboard:
      - Ter a quantidade de produtos cadastrados e cadastrados por segmento;
      - Relatório por tipo de produto também;

  # 22/11/2021:
    - Página inicial: "Este software não substitui o Asana. serve apenas como controle de arquivos: SLDW, PDF, DXF, NOS, PN e NS"
    - Gerar botão de PartNumber;
    - Preços server AWS;
    - Botão BackUp;
    - Relatório de Produtos que foi feito BackUp;
    - Filtro de BackUp;
    - PartNumber:
      - Botão número de PN do fabricante e quantidade;
      - Botão de selecionar o produto;
      - Botão de quantidade de itens;
    
    - Relatório do PartNumber (Acertar os detalhes assim que acabar as demandas que faltam): 
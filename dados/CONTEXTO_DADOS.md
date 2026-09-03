# Contexto dos Dados — Regras de Negócio e Fluxo de Dados

Este documento descreve o domínio de negócio, o fluxo de dados e as regras de
validade/classificação usadas em todas as bases do exercício. Ele serve como
**fonte de referência única** (single source of truth) para:

- decidir o que é um **dado vazio** vs. um **dado inválido** (Exercício 4);
- servir de **Fonte de Referência** para os testes de **acurácia** (Exercício 5);
- padronizar **categorias** e **faixas de classificação** usadas nos gráficos do
  Power BI e nos widgets de distribuição do Orange.

## 1. Fluxo de dados (pipeline do exercício)

```
criar dados → armazenar dados → integrar dados → visualizar → avaliar qualidade → tratar dados → minerar dados
   (Excel)        (CSV)        (Power BI /        (Power BI)      (Orange)      (Orange /      (Orange)
                                 MariaDB)                                        Excel)
```

| Etapa | Ferramenta | Artefato gerado | Onde fica |
|---|---|---|---|
| Criar dados | Excel | tabelas fictícias | `dados/` |
| Armazenar dados | CSV / MariaDB | arquivos `.csv`, tabelas SQL | `dados/`, banco `mineracao_dados` |
| Integrar dados | Power BI | relacionamentos entre tabelas | `.pbix` |
| Visualizar | Power BI | cartões, gráficos | `.pbix` |
| Avaliar qualidade | Orange | widgets (Data Table, Distributions, Box Plot) | `.ows` |
| Tratar dados | Orange / Excel | base corrigida | `dados/*_tratado.csv` |
| Minerar dados | Orange | correlações, clusters, distribuições | `.ows` |

## 2. Domínio de negócio

Simula uma pequena **loja/varejo fictício** com clientes em todo o Brasil, que
também mantém uma frente de **gestão acadêmica** (Exercício 2) e é investigada,
mais adiante, via um banco **MariaDB** (Exercício 6). Todas as entidades
compartilham os mesmos domínios de valores válidos abaixo, para manter
consistência entre exercícios.

## 3. Dicionário de dados e regras de validade

### 3.1 Vendas (Exercício 1 — `dados/exercicio1_vendas.csv`)

| Campo | Tipo | Regra de validade (domínio aceito) | Observação |
|---|---|---|---|
| `id_venda` | texto | único, padrão `V###` | chave primária |
| `data` | data | `dd/mm/aaaa`, entre 01/01/2020 e hoje | não pode ser data futura |
| `produto` | texto | ver tabela 3.5 (Catálogo de Produtos) | deve existir no catálogo |
| `categoria` | categórico | `Eletrônicos`, `Móveis`, `Livros`, `Papelaria`, `Acessórios` | derivada do produto (não deve divergir do catálogo) |
| `quantidade` | inteiro | > 0 (tipicamente 1–10) | negativo ou zero = inválido |
| `valor_unitario` | decimal (vírgula) | > 0, deve bater com o catálogo (±0 na versão correta) | negativo = inválido; divergente do catálogo = problema de acurácia |
| `estado_cliente` | categórico | sigla de UF válida (ver 3.6) | fora da lista = inválido (ex.: `XX`) |

### 3.2 Clientes (Exercício 3/4/5 — `dados/exercicio3_clientes.csv`)

| Campo | Tipo | Regra de validade | Observação |
|---|---|---|---|
| `id_cliente` | texto | único, padrão `C###` | chave primária |
| `idade` | inteiro | 0 a 110 | `250`, `-5` etc. = inválido (Exercício 4) |
| `cidade` | texto | cidade compatível com o `estado` informado | incompatibilidade = inconsistência (Exercício 5) |
| `estado` | categórico | sigla de UF válida (ver 3.6) | `XX` = inválido |
| `renda` | decimal | ≥ 0 | negativo = inválido |
| `quantidade_compras` | inteiro | ≥ 0 | negativo = inválido |
| `valor_total_compras` | decimal | ≥ 0, e ≈ `quantidade_compras × ticket médio` | muito fora da faixa esperada = problema de acurácia |
| `data_nascimento` | data | coerente com `idade` (ano atual − ano nascimento ≈ idade) | divergente = inconsistência (Exercício 5) |

### 3.3 Gestão acadêmica (Exercício 2)

| Tabela | Chave | Regras principais |
|---|---|---|
| `Alunos` | `id_aluno` | 1 aluno pertence a 1 `id_curso` válido |
| `Cursos` | `id_curso` | nomes únicos |
| `Disciplinas` | `id_disciplina` | associada a 1 `id_curso` válido |
| `Matriculas` | `id_matricula` | `id_aluno` e `id_disciplina` devem existir nas tabelas correspondentes (integridade referencial) |

### 3.4 Classificação — faixas etárias (usadas nos gráficos de distribuição)

| Faixa | Intervalo |
|---|---|
| Jovem | 18–25 |
| Adulto jovem | 26–35 |
| Adulto | 36–50 |
| Meia-idade | 51–65 |
| Idoso | 66+ |

### 3.5 Catálogo de produtos (Fonte de Referência de preço/categoria)

| Produto | Categoria | Valor unitário de referência (R$) |
|---|---|---|
| Notebook Dell Inspiron 15 | Eletrônicos | 3500,00 |
| Mouse sem fio Logitech | Eletrônicos | 89,90 |
| Teclado mecânico Redragon | Eletrônicos | 249,90 |
| Monitor LG 24 polegadas | Eletrônicos | 899,00 |
| Cadeira de escritório ergonômica | Móveis | 650,00 |
| Mesa de escritório | Móveis | 480,00 |
| Smartphone Samsung Galaxy A55 | Eletrônicos | 1899,00 |
| Fone de ouvido Bluetooth JBL | Eletrônicos | 199,90 |
| Impressora HP DeskJet | Eletrônicos | 550,00 |
| Livro Clean Code | Livros | 89,90 |
| Caderno universitário 10 matérias | Papelaria | 32,50 |
| Caixa de canetas esferográficas | Papelaria | 15,90 |
| Mochila para notebook | Acessórios | 129,90 |
| Carregador portátil 10000mAh | Eletrônicos | 99,90 |
| Webcam Full HD | Eletrônicos | 179,90 |

Este catálogo é o que o Exercício 5 chama de **"Fonte de Referência"**: qualquer
`valor_unitario` ou `categoria` que não bata com esta tabela é um problema de
**acurácia**, não de validade (o valor pode ser um número positivo perfeitamente
"válido", mas ainda assim estar **errado**).

### 3.6 Regiões e UFs válidas (classificação geográfica)

| Região | UFs |
|---|---|
| Sudeste | SP, RJ, MG, ES |
| Sul | PR, SC, RS |
| Nordeste | BA, PE, CE, MA, PB, RN, AL, SE, PI |
| Centro-Oeste | DF, GO, MT, MS |
| Norte | AM, PA, AC, RO, RR, AP, TO |

Qualquer sigla fora desta lista (ex.: `XX`) é **inválida**. Esta tabela também
serve para os gráficos de "vendas por região" no Power BI (agrupando por UF).

## 4. Regras de normalização (Exercício 2)

- `Alunos`, `Cursos`, `Disciplinas` e `Matriculas` são mantidas como tabelas
  separadas (3ª Forma Normal) em vez de uma única tabela plana, porque:
  1. evita **redundância** (nome do curso não se repete em cada matrícula);
  2. evita **anomalias de atualização** (mudar o nome de um curso é 1 update,
     não N updates);
  3. permite **integridade referencial** (uma matrícula só pode referenciar
     alunos/disciplinas que existem).
- `Matriculas` é a tabela fato (grão = 1 aluno + 1 disciplina); `Alunos`,
  `Cursos` e `Disciplinas` são tabelas dimensão.

## 5. Como este contexto é usado nos exercícios seguintes

- **Exercício 3**: gera `dados/exercicio3_clientes.csv` seguindo as regras da
  seção 3.2 (base correta, sem vazios/inválidos).
- **Exercício 4**: cria uma cópia da base do Exercício 3 e injeta vazios/valores
  fora do domínio definido na seção 3.2 (ex.: `idade = 250`, `estado = XX`).
- **Exercício 5**: usa o Catálogo de Produtos (3.5) ou uma cópia íntegra da base
  de clientes como "Fonte de Referência" para os testes de acurácia, mais
  duplicidade de registros e inconsistência `idade` × `data_nascimento`.
- **Exercício 6**: replica as mesmas entidades (clientes, produtos, vendas) e as
  mesmas regras de validade dentro do MariaDB.

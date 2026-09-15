# mineração-outlier-iqr

Exercícios de detecção de outliers com a **Regra do IQR** (`numpy` e `pandas`).

Todos os comandos devem ser executados dentro da pasta `exercicios iqr`.

## Instalação

**Requisitos:** Python 3.10 ou superior.

### 1. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar o ambiente

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

Se aparecer erro de política de execução:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

**Windows (cmd):**

```cmd
.venv\Scripts\activate.bat
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 3. Instalar as dependências

Com o ambiente ativado:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Sair do ambiente

```bash
deactivate
```

## Como rodar

Com o venv ativado, execute o script do exercício desejado:

```bash
python exercicio1.py
python exercicio2.py
...
python exercicio11.py
```

## Dependências

- numpy
- pandas
- matplotlib

## Exercícios

1. **Quartis com NumPy** — calcular Q1, Q2 e Q3 de um vetor com `np.percentile()`.
2. **IQR e limites** — calcular IQR, limite inferior e superior, e verificar se o 150 é candidato a outlier.
3. **Q1 e Q3 sem funções prontas** — separar os dados em duas metades manualmente e calcular os quartis pela mediana de cada metade.
4. **Outliers em uma lista** — calcular Q1, Q3, IQR e limites, e listar os candidatos a outlier nas tensões.
5. **Função `detectar_anomalias`** — função reutilizável que recebe dados e um multiplicador e retorna Q1, Q3, IQR, limites e candidatos.
6. **Testando a função** — usar `detectar_anomalias` num novo conjunto e explicar por que cada candidato foi sinalizado.
7. **IQR em um DataFrame** — calcular Q1, Q3, IQR e limites numa coluna de um DataFrame com `.quantile()`.
8. **Coluna de outlier** — criar uma coluna `Outlier` (True/False) num DataFrame com base nos limites do IQR.
9. **Corrigindo um erro confirmado** — substituir um valor confirmado como erro de leitura pela mediana, usando `np.where()`.
10. **Comparando dispersão de dois grupos** — calcular o IQR de dois grupos e discutir o que um IQR maior significa.
11. **Boxplot** — visualizar outliers com boxplot e comparar com o resultado calculado pela Regra do IQR.

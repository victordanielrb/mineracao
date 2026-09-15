# mineração-zscore

Exercícios de detecção de valores incomuns com o **Z-Score** (`numpy` e `pandas`).

Todos os comandos devem ser executados dentro da pasta `exercicios-zscore`.

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
python exercicio10.py
```

## Dependências

- numpy
- pandas

## Exercícios

1. **Distância em passos de desvio-padrão** — calcular a distância até a média, quantos desvios-padrão ela representa e o Z-Score.
2. **Acima ou abaixo da média?** — calcular o Z-Score de três valores e interpretar o sinal do resultado.
3. **Qual leitura é mais incomum?** — calcular o Z-Score de várias temperaturas e identificar a mais distante da média.
4. **Latência de uma API** — calcular média, desvio-padrão e o Z-Score de um valor específico, avaliando se merece investigação (`|Z| > 3`).
5. **Monitoramento de CPU com classificação** — calcular o Z-Score de cada leitura e classificar como `Comum` ou `Investigar`.
6. **O mesmo valor em dois contextos** — comparar o Z-Score do mesmo valor em grupos com desvios-padrão diferentes.
7. **Função de interpretação** — implementar `interpretar_z()` para classificar um Z-Score em texto.
8. **Z-Score em um DataFrame** — criar as colunas `Z_Score` e `Status` num DataFrame e filtrar os casos para investigação.
9. **Comparação entre IQR e Z-Score** — calcular IQR e Z-Score para o mesmo conjunto de dados e comparar o que cada técnica indica.
10. **Mini análise de eventos de segurança** — calcular o Z-Score de tentativas de login e identificar eventos incomuns (`|Z| > 3`).

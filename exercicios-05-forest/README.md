# mineração-isolation-forest

Exercícios de detecção de anomalias com **Isolation Forest** (`scikit-learn`).

Todos os comandos devem ser executados dentro da pasta `exercicios-05-forest`.

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
python exercicio8.py
```

## Dependências

- numpy
- pandas
- matplotlib
- scikit-learn

## Exercícios

1. **Vendas de uma mercearia** — classificar as vendas diárias e apontar o valor sinalizado. Vale discutir se o 400 deve ser removido automaticamente.
2. **Latência de uma conexão de internet** — classificar as medições de tempo de resposta e discutir se latência alta sempre indica falha.
3. **Consumo de combustível** — identificar a combinação incomum de distância e litros.
4. **Viagens de ônibus urbano** — identificar a viagem candidata e levantar possíveis causas.
5. **Regra fixa versus Isolation Forest** — comparar os dois métodos e discutir as limitações de um limite definido manualmente.
6. **Problema completo** — montar um cenário próprio com anomalias e definir os critérios do que é incomum.
7. **Sensores ambientais (CSV)** — ler o arquivo com pandas e sinalizar leituras incomuns.
8. **Vendas de e-commerce (CSV)** — apontar as vendas candidatas e avaliar se são erro, promoção ou caso a investigar.

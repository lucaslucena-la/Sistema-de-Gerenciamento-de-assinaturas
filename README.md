# 💰 Gerenciador de Assinaturas - Python Puro

Este projeto é uma aplicação para **gerenciamento de assinaturas** utilizando **Python puro** e **SQLModel**. 
Ele permite adicionar, remover e visualizar assinaturas, calcular custos mensais e gerar gráficos de gastos dos últimos 12 meses.

## 🚀 Tecnologias Utilizadas

- **Python** (linguagem principal)
- **SQLModel** (manipulação do banco de dados SQLite)
- **Matplotlib** (geração de gráficos)

## 📌 Funcionalidades

- 📋 **Cadastro de assinaturas**
- 💳 **Registro de pagamentos**
- 📊 **Visualização de custos mensais**
- 📈 **Geração de gráficos de gastos**
- ❌ **Remoção de assinaturas**

## 📦 Instalação e Execução

### 1️⃣ Clone o repositório
```bash
 git clone https://github.com/seu-usuario/projeto-gerenciador-assinaturas.git
 cd projeto-gerenciador-assinaturas
```

### 2️⃣ Criação e ativação do ambiente virtual
#### Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
#### Windows:
```bash
python -m venv venv
venv\Scripts\Activate
```

### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Execute as migrações do banco de dados
```bash
python models/database.py
```

### 5️⃣ Inicie o sistema
```bash
python app.py
```

## 🏗️ Estrutura do Projeto
```
📂 projeto-gerenciador-assinaturas
 ├── models/               # Modelos e banco de dados
 │   ├── database.py       # Configuração do banco de dados
 │   ├── model.py          # Definição das tabelas
 ├── views/                # Lógica da aplicação
 │   ├── view.py           # Serviço de assinaturas
 ├── templates/            # Interface da aplicação
 │   ├── app.py            # Interface em terminal
 ├── app.py                # Arquivo principal
 ├── requirements.txt      # Dependências
 ├── database.db           # Banco de dados SQLite
```

## 🔧 Funcionalidades Detalhadas

### 📌 Modelos do Banco de Dados

#### `Subscription`
```python
class Subscription(SQLModel, table=True):
    id: int = Field(primary_key=True)
    empresa: str
    site: Optional[str] = None
    data_assinatura: date
    valor: Decimal
```
#### `Payments`
```python
class Payments(SQLModel, table=True):
    id: int = Field(primary_key=True)
    subscription_id: int = Field(foreign_key="subscription.id")
    date: date
```

### 📊 Geração de Gráficos
A aplicação utiliza **Matplotlib** para exibir o histórico de pagamentos dos últimos 12 meses.
```python
import matplotlib.pyplot as plt
plt.plot(last_12_months, values_for_months)
plt.show()
```

## 📜 Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

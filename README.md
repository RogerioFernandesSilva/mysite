# 🚀 Projeto Django - Python & PostgreSQL

> Repositório criado como parte do módulo de Python Back-End da EBAC (2024-2026). 
>Trata-se de uma aplicação web desenvolvida em **Python** utilizando o framework **Django** e integrada com um banco de dados **PostgreSQL**.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11+**
* **Django 5.2+**
* **PostgreSQL 18**
* **psycopg2-binary** (Driver de conexão PostgreSQL para Python)
* **Git & GitHub**

---

## ⚙️ Pré-requisitos

Certifique-se de ter instalado em sua máquina:

* Python (versão 3.11 ou superior)
* PostgreSQL
* Git

Siga os passos abaixo para clonar e executar o projeto na sua máquina:

### 1. Clonar o repositório

```
bash
git clone https://github.com/RogerioFernandesSilva/mysite
cd mysite

```

### 2. Criar e ativar o ambiente virtual (venv)

No **Windows (PowerShell)**:

```powershell
python -m venv venv
.\venv\Scripts\Activate

```

No **Linux / macOS**:

```bash
python3 -m venv venv
source venv/bin/activate

```

### 3. Instalar as dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt

```

*(Caso o arquivo `requirements.txt` não exista, instale manualmente os pacotes principais: `pip install django psycopg2-binary`)*

#### 4. Configurar o Banco de Dados

Certifique-se de que o seu servidor PostgreSQL está rodando e crie um banco de dados local. Em seguida, configure as credenciais no arquivo `mysite/settings.py` na seção `DATABASES`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_seu_banco',
        'USER': 'postgres',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```

### 5. Executar as Migrações

```bash
python manage.py makemigrations
python manage.py migrate

```

### 6. Iniciar o Servidor de Desenvolvimento

```bash
python manage.py runserver

```

Agora, abra o seu navegador e acesse: `[http://127.0.0.1:8000/](http://127.0.0.1:8000/)`

---

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Faça o commit das alterações (`git commit -m 'Adiciona nova feature'`)
4. Faça o push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um **Pull Request**.

---

## 📥 Como Rodar o Projeto Localmente

Siga os passos abaixo para clonar e executar o projeto na sua máquina:

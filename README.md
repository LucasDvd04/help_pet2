# HelpPet 🐾

> Plataforma criada para ajudar pessoas a encontrarem pets perdidos, cadastrar pets encontrados e facilitar processos de adoção de maneira simples e acessível.

O **HelpPet** centraliza informações sobre animais perdidos, encontrados e disponíveis para adoção. O projeto nasce da necessidade de ampliar o alcance das buscas físicas, conectando rapidamente tutores, voluntários e protetores.

---

## 📌 Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Público-alvo](#público-alvo)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Rodar Localmente](#como-rodar-localmente)
- [Configuração do Banco de Dados (SQL Server)](#configuração-do-banco-de-dados-sql-server)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Testar](#como-testar)
- [Roadmap](#roadmap)
- [Contribuições](#contribuições)
- [Licença](#licença)
- [Contato](#contato)

---

## 🐶 Visão Geral

O **HelpPet** tem como objetivo centralizar informações sobre pets perdidos ou encontrados, ajudando na comunicação entre usuários e aumentando a chance de reencontros e adoções.

### Problema que resolve  
A busca física por pets perdidos geralmente é limitada ao bairro ou região. O HelpPet amplia esse alcance, permitindo que pessoas compartilhem informações de maneira rápida e organizada.

---

## ⚙️ Funcionalidades

- Cadastro de pets perdidos, encontrados ou disponíveis para adoção.
- Sistema de **comentários** em cada anúncio.
- **Autenticação completa de usuários** (cadastro, login e logout).
- **Perfil de usuário** contendo:
  - Pets cadastrados
  - Informações pessoais
  - Histórico de interações
- Visualização de detalhes do pet com fotos, descrição e status.
- Filtros e busca por categoria (perdido / encontrado / adoção).

---

## 🎯 Público-alvo

- Tutores que perderam seus animais
- Pessoas que encontraram pets na rua
- Protetores e voluntários
- ONGs e abrigos
- Público geral interessado em adoção

---

## 🛠️ Tecnologias Utilizadas

**Frontend**
- HTML
- CSS
- Bootstrap

**Backend**
- Python
- Django Framework

**Banco de Dados**
- SQL Server

**Outros**
- Sistema de templates do Django
- ORM do Django

---

## 🚀 Como Rodar Localmente

### 📌 Pré-requisitos
- Python 3.8+
- Git
- SQL Server instalado (ou acesso a uma instância remota)
- Virtualenv (opcional, mas recomendado)

---

### 📥 Instalação

```bash
# 1. Clonar o repositório
git clone <URL_DO_SEU_REPOSITORIO>
cd help-pet

# 2. Criar e ativar ambiente virtual
python -m venv .venv

# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Criar migrações e aplicar
python manage.py makemigrations
python manage.py migrate

# 5. Criar superusuário (opcional)
python manage.py createsuperuser

# 6. Rodar o servidor
python manage.py runserver




📫 Contato

Autor: Lucas David
E-mail: lucas_david04@outlook.com

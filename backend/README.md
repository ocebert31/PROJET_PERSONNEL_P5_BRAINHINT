# BrainHint — Backend

API REST en architecture en couches avec **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Pydantic** et **Alembic**.

## Stack

- FastAPI + Uvicorn
- PostgreSQL (installation locale)
- SQLAlchemy 2 (ORM)
- Pydantic v2 (schémas API)
- Alembic (migrations)

## Architecture

```
app/
├── main.py                 # Point d'entrée
├── routers/                # Routes HTTP
│   ├── health.py
│   └── contacts.py
├── schemas/                # Modèles Pydantic (JSON)
│   └── contact.py
├── models/                 # Modèles SQLAlchemy (BDD)
│   └── contact.py
├── services/               # Logique métier
│   └── contact_service.py
├── repositories/           # Accès base de données
│   └── contact_repository.py
├── database/               # Connexion PostgreSQL
│   ├── connection.py
│   └── session.py
├── dependencies/           # Injection FastAPI (Depends)
│   └── database.py
└── core/                   # Configuration
    └── settings.py
```

## Installation

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## PostgreSQL (local)

### macOS (Homebrew)

```bash
brew install postgresql@16
brew services start postgresql@16
```

### Créer la base et l'utilisateur

```bash
psql postgres
```

```sql
CREATE USER brainhint WITH PASSWORD 'brainhint';
CREATE DATABASE brainhint OWNER brainhint;
\q
```

Adapte `DATABASE_URL` dans `.env` si tu utilises d'autres identifiants.

## Migrations

```bash
alembic upgrade head
```

## Démarrage

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- API : http://localhost:8000
- Swagger : http://localhost:8000/docs

## Endpoints

| Méthode | Route                  | Description        |
|---------|------------------------|--------------------|
| GET     | `/`                    | Bienvenue          |
| GET     | `/api/health`          | Health check       |
| POST    | `/api/contacts/`       | Créer un contact   |
| GET     | `/api/contacts/`       | Lister les contacts|
| GET     | `/api/contacts/{id}`   | Détail d'un contact|

## Exemple

```bash
curl -X POST http://localhost:8000/api/contacts/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Bertrand","email":"bertrand@example.com","message":"Hello BrainHint!"}'
```

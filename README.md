# BrainHint

Monorepo **frontend Angular** + **API FastAPI** avec PostgreSQL.

## Structure

```
BrainHint/
├── frontend/     # Angular 19, Material, Reactive Forms
└── backend/      # FastAPI, SQLAlchemy, Pydantic, Alembic
```

## Prérequis

- Node.js 18+ et npm
- Python 3.9+
- PostgreSQL 16 (installation locale)

## Démarrage rapide

### 1. Base de données (PostgreSQL)

```bash
brew install postgresql@16
brew services start postgresql@16
psql postgres
```

```sql
CREATE USER brainhint WITH PASSWORD 'brainhint';
CREATE DATABASE brainhint OWNER brainhint;
\q
```

### 2. Backend (API)

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```

- API : http://localhost:8000
- Swagger : http://localhost:8000/docs

### 3. Frontend (Angular)

Dans un autre terminal :

```bash
cd frontend
npm install
npm start
```

- App : http://localhost:4200

## Tests

```bash
# Backend
cd backend && pytest

# Frontend
cd frontend && npm run test:ci
```

## CI (GitHub Actions)

À chaque push ou PR sur `main`, la CI exécute :
- **backend** : `pytest`
- **frontend** : `npm run build` + `npm run test:ci`

Workflow : `.github/workflows/ci.yml`

## Documentation détaillée

- [Frontend](frontend/README.md)
- [Backend](backend/README.md)

## Stack

| Partie   | Technologies |
|----------|--------------|
| Frontend | Angular 19, Angular Material, Reactive Forms, CSS |
| Backend  | FastAPI, Uvicorn, Pydantic, SQLAlchemy, Alembic |
| BDD      | PostgreSQL |
# PROJET_PERSONNEL_P5_BRAINHINT

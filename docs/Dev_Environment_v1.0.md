# Dev_Environment_v1.0

Thread: 6-Pre | Date: 2026-09-16 | Status: Complete

## Stack

| Layer | Technology | Details |
|-------|-----------|---------|
| Backend | FastAPI (Python) | Port 8002, systemd: dna-api |
| Database | PostgreSQL 18 | dna_db, user: dna_app |
| Migrations | Alembic | First migration: a5849f937fe5 |
| Frontend | React + Vite 8 | Port 5173, systemd: dna-frontend |
| Tunnel | Cloudflare Tunnel | b53631ff-ffdc-48e2-83d9-aa31e31fbdda |
| Reverse proxy | nginx | Shared with ICU/Universe_SS |
| Process mgmt | systemd | dna-api, dna-frontend |
| Alerts | Pushover | Deferred to SIT/UAT |

## Ports

| Service | Port |
|---------|------|
| Galaxy FastAPI (dna-api) | 8002 |
| Galaxy React (dna-frontend) | 5173 |
| ICU uvicorn | 8000 |
| ICU nginx | 8080 |

## URLs

| Endpoint | URL |
|----------|-----|
| Health | https://dna.krhub.uk/api/health |
| Frontend | https://dna.krhub.uk |

## Database

- Host: localhost
- Database: dna_db
- User: dna_app
- Schemas: dna, mi, logging, fintiq

## Repo

- GitHub: krhub-uk/dna
- Branch strategy: main only (single developer)
- Local path: /opt/dev/dna

## Environment variables

- backend/.env (gitignored) — see backend/.env.example
- frontend/.env (gitignored) — see frontend/.env.example

## Dev tooling

- Linter: ruff
- Formatter: black
- Tests: pytest
- Pre-commit hooks: installed

## Key decisions

1. Docker: Compose for local dev only, bare systemd on ubuntu-server
2. nginx: reverse proxy, Galaxy on port 80 server block
3. Branches: main only
4. Env vars: separate backend/.env and frontend/.env
5. Migrations: one per logical thread/phase

## Verification checklist

- [x] krhub-uk/dna repo scaffold committed
- [x] Postgres running, four schemas in dna_db
- [x] GET /health returns {"status":"ok"} via dna.krhub.uk/api/health
- [x] Alembic migration history shows first migration applied
- [x] React app loads at dna.krhub.uk
- [ ] Pushover test notification — deferred to SIT/UAT
- [x] Google OAuth redirect URI registered
- [x] Dev_Environment_v1.0.md committed to repo and saved to GDrive

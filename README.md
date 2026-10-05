@'
# ProofStack

ProofStack is an AI-powered proof and verification platform.

## Project Status

ProofStack is currently in the foundation/development stage.

The project is being developed as a modular monorepo with:

- FastAPI backend
- Next.js frontend
- PostgreSQL database
- Redis
- RQ background job infrastructure
- Docker Compose for local infrastructure
- GitHub Actions for CI validation

## Repository Structure

```text
ProofStack/
├── .github/
│   └── workflows/
│       └── ci.yml
├── backend/
│   ├── app/
│   ├── alembic/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── app/
│   ├── components/
│   ├── features/
│   ├── hooks/
│   ├── lib/
│   ├── public/
│   ├── tests/
│   └── package.json
├── infrastructure/
├── scripts/
├── tests/
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
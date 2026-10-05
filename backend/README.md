
# ProofStack Backend

The ProofStack backend is built with FastAPI and provides the server-side application foundation.

## Stack

- Python 3.11
- FastAPI
- Uvicorn
- Pydantic
- Pydantic Settings
- SQLAlchemy
- Alembic
- PostgreSQL via Psycopg
- Redis
- RQ
- Pytest
- Ruff
- Mypy

## Local Setup

From the backend directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
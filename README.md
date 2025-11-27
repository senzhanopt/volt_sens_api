# VoltSens API Demo

A `FastAPI` application for power grid measurements using `SQLAlchemy`, `Alembic`, and `PostgreSQL`.

# Getting Started


Install `uv` with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, restart your shell or reload:

```bash
source ~/.profile
```

Install and start PostgreSQL:
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install postgresql postgresql-contrib -y
sudo service postgresql start
```

Switch to the PostgreSQL user:
```bash
sudo -i -u postgres
createdb demo
```

Create a user:
```bash
psql
# Inside psql shell:
CREATE USER postgres WITH PASSWORD 'your_password';
\q
exit
```

Create a `.env` file in the project root:
```env
DATABASE_URL=postgresql+psycopg2://postgres:<your_password>@localhost:5432/demo
```

Clone the repo:
```bash
git clone https://github.com/senzhanopt/volt_sens_api.git
cd volt_sens_api
```

Set up environment with:
```bash
uv sync
```

Run Alembic migrations:
```bash
uv run alembic upgrade head
```

Start the FastAPI application:
```bash
uv run uvicorn app.main:app --reload --reload-dir app
```

API is available at: 

http://127.0.0.1:8000

Interactive docs:

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/redoc

Run tests:
```bash
uv run tests/test_request.py get
```
replacing `get` with `post`, `del_one`, `del`, `update`, or `index`.

# Development

Update SQLAlchemy models, create Alembic revision, and apply it:
```bash
uv run alembic revision --autogenerate -m "description"
uv run alembic upgrade head
```

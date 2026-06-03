# AI Research Assistant

An AI-powered research platform that helps users generate, manage, and organize research reports using Large Language Models (LLMs), agent workflows, and modern full-stack technologies.

## Features

### Authentication

* User Registration
* User Login
* JWT Authentication
* Protected Routes
* Persistent Login Sessions
* Logout Functionality

### Research Management (In Progress)

* Create Research Sessions
* Research History
* User-specific Research Records

### AI Capabilities (Planned)

* OpenAI Integration
* Automated Research Summaries
* Multi-Agent Research Workflow (LangGraph)
* MCP (Model Context Protocol) Integrations
* PDF Report Export

---

## Tech Stack

### Frontend

* React
* TypeScript
* Vite
* React Router
* Axios

### Backend

* FastAPI
* SQLAlchemy
* Alembic
* JWT Authentication

### Database

* PostgreSQL

### AI & Agent Frameworks (Planned)

* OpenAI API
* LangGraph
* MCP (Model Context Protocol)

---

## Project Structure

```text
ai-research-assistant/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── agents/
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   │
│   ├── alembic/
│   ├── main.py
│   └── requirements.txt
│
└── README.md
```

---

## Current Progress

### Completed

* [x] Project Setup
* [x] FastAPI Backend
* [x] React Frontend
* [x] PostgreSQL Integration
* [x] SQLAlchemy Models
* [x] Alembic Migrations
* [x] JWT Authentication
* [x] Protected Routes
* [x] User Session Persistence

### In Progress

* [ ] Research Session Management
* [ ] Research History

### Planned

* [ ] OpenAI Integration
* [ ] LangGraph Agents
* [ ] MCP Integrations
* [ ] PDF Export
* [ ] UI Improvements

---

## Getting Started

### Backend

```bash
cd backend

python -m venv .venv

source .venv/bin/activate
# Windows:
# .venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

## Database Migration

Create a new migration:

```bash
alembic revision --autogenerate -m "migration_name"
```

Apply migrations:

```bash
alembic upgrade head
```

---

## Roadmap

### Phase 1

* Authentication System
* User Management

### Phase 2

* Research Session CRUD
* Research History

### Phase 3

* OpenAI Research Generation

### Phase 4

* LangGraph Multi-Agent Workflow

### Phase 5

* MCP Tool Integrations

### Phase 6

* PDF Export & UI Polish

---

## Author

Hendri Jonathan

Built as a portfolio project to demonstrate full-stack development, backend architecture, authentication systems, database design, and AI application development.

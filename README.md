# AI Research Analyzer — Docker-ready

Multi-agent research assistant built with Agno, Groq, Streamlit and FastAPI.

## Prerequisites
- Docker Desktop installed and running
- A Groq API key

## Setup on Windows PowerShell
1. Extract the ZIP.
2. Open PowerShell in the extracted `ResearchAnalyzerFull` folder.
3. Create `.env` from the example:
   ```powershell
   Copy-Item .env.example .env
   ```
4. Open `.env` and replace `put_your_new_groq_api_key_here` with your newly generated Groq API key.
5. Build and start:
   ```powershell
   docker compose up --build
   ```
6. Open:
   - Streamlit: http://localhost:8501
   - API docs: http://localhost:8000/docs
   - Health: http://localhost:8000/health

## Useful commands
```powershell
docker compose ps
docker compose logs --tail=100 ui
docker compose logs --tail=100 api
docker compose down
docker compose up -d --build
```

## API example
Send a POST request to `http://localhost:8000/research` with JSON:
```json
{"topic":"Impact of Artificial Intelligence on Education"}
```

## Security
Never commit `.env` or share your API key. The ZIP includes only `.env.example`, not a working secret.

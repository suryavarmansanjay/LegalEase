# LegalEase - AI Legal Document Generator

LegalEase is a college-project web application for generating editable
legal document drafts with Gemini, using a FastAPI backend and Streamlit
frontend.

## Architecture

Streamlit frontend
        |
        | POST /generate
        v
FastAPI backend
        |
        v
Gemini API
        |
        v
Generated legal document
        |
        +--> Editable preview
        +--> TXT
        +--> DOCX
        +--> PDF

## Project structure

```text
LegalEase/
├── main.py
├── routes.py
├── requirements.txt
├── Procfile
├── Dockerfile
├── .env.example
├── .gitignore
├── README.md
├── ai_core/
│   ├── __init__.py
│   └── gemini_generator.py
├── frontend/
│   └── app.py
└── utils/
    └── document_export.py
```

## Local setup

1. Install Python 3.11+.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env`.
4. Add your Gemini API key to `.env`.
5. Set a supported Gemini model in `GEMINI_MODEL`.
6. Start FastAPI:

```bash
uvicorn main:app --reload
```

7. In another terminal start Streamlit:

```bash
streamlit run frontend/app.py
```

8. Open the Streamlit URL shown in the terminal.

## API

### POST `/generate`

Example request:

```json
{
  "document_type": "Rental Agreement",
  "parties": "Landlord: John Doe; Tenant: David Kumar",
  "terms": "Monthly rent is Rs. 15,000.",
  "dates": "01-10-2026 to 30-09-2027"
}
```

Example response:

```json
{
  "document": "Generated legal document..."
}
```

FastAPI Swagger documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Deployment

Recommended project deployment architecture:

- FastAPI backend: Render, Railway, Fly.io, or a VPS.
- Streamlit frontend: Streamlit Community Cloud.
- Put `GEMINI_API_KEY` in the deployment platform's secret/environment
  settings.
- Set `BACKEND_URL` in the Streamlit deployment to the public FastAPI URL.

## Important

Do not commit `.env` or expose your Gemini API key.

The generated content is a draft and should be reviewed by a qualified
legal professional before signing or use.

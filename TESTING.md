# LegalEase Testing Checklist

## Epic 1 - Architecture
- [ ] Gemini API key stored as a secret/environment variable.
- [ ] FastAPI backend starts successfully.
- [ ] Streamlit frontend starts successfully.
- [ ] Frontend can reach backend.

## Epic 2 - Core Functionality
- [ ] Rental Agreement generation works.
- [ ] Employment Agreement generation works.
- [ ] NDA generation works.
- [ ] Service Agreement generation works.
- [ ] Custom document generation works.
- [ ] Generated text is editable.
- [ ] TXT download works.
- [ ] DOCX download works.
- [ ] PDF download works.

## Epic 3 - API
- [ ] GET / returns API status.
- [ ] POST /generate accepts valid JSON.
- [ ] Missing fields are rejected.
- [ ] Gemini errors are returned as API errors.

## Epic 4 - Frontend
- [ ] Inputs are visible.
- [ ] Generate button works.
- [ ] Preview appears.
- [ ] Editing works.
- [ ] Download buttons work.

## Epic 5 - Deployment
- [ ] requirements.txt is present.
- [ ] Procfile/Dockerfile is present.
- [ ] Backend deployed.
- [ ] Frontend deployed.
- [ ] Secrets configured.
- [ ] BACKEND_URL configured.

## Epic 6 - Final Test
- [ ] End-to-end test completed.
- [ ] Multiple input combinations tested.
- [ ] Invalid inputs tested.
- [ ] API key is not exposed in GitHub.

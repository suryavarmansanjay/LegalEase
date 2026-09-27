import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. Add it to your environment/secrets."
    )

client = genai.Client(api_key=API_KEY)


class GeminiDocumentGenerator:
    def generate_document(
        self,
        document_type: str,
        parties: str,
        terms: str,
        dates: str,
    ) -> str:
        prompt = f"""
You are LegalEase, an AI assistant for creating legal document DRAFTS.

Document type:
{document_type}

Parties:
{parties}

Terms and conditions:
{terms}

Dates:
{dates}

Create a professional, clearly structured legal document draft.

Rules:
1. Use headings and numbered clauses where appropriate.
2. Do not invent facts, names, addresses, amounts, laws, or dates that were not provided.
3. If important information is missing, write [TO BE PROVIDED] instead of guessing.
4. Use plain, professional legal language.
5. Include a final section titled "Review Notice".
6. The Review Notice must state that this is an AI-generated draft and should be reviewed by a qualified legal professional before signing or use.
7. Return only the document draft.
"""

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        if not response.text:
            raise RuntimeError("Gemini returned an empty response.")

        return response.text

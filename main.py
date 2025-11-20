import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv

# Load env
load_dotenv()

# Setup API
app = FastAPI(title="Secure PII Sanitizer API")

# Configure Gemini (Get key from aistudio.google.com)
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

class TextRequest(BaseModel):
    content: str

@app.post("/sanitize")
async def sanitize_text(request: TextRequest):
    """
    Accepts text, detects PII (Names, Emails, Phones), and replaces them with [REDACTED].
    """
    if not request.content:
        raise HTTPException(status_code=400, detail="No content provided")

    # The Prompt Engineering
    prompt = f"""
    Act as a Data Loss Prevention (DLP) security tool. 
    Analyze the following text. Replace any PII (Names, Phone Numbers, Emails, Addresses, SSNs) with the tag [REDACTED_TYPE].
    Example: "Call Bob at 555-0199" -> "Call [REDACTED_NAME] at [REDACTED_PHONE]"
    
    Text to sanitize:
    "{request.content}"
    Return ONLY the sanitized text. No markdown, no explanations.
    """

    try:
        response = model.generate_content(prompt)
        return {"original_length": len(request.content), "sanitized_text": response.text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

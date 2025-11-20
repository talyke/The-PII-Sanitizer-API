# 🛡️ AI-Powered PII Sanitizer API (DLP Tool)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-High%20Performance-green)
![Security](https://img.shields.io/badge/Focus-Data%20Privacy-red)

## 📋 Project Overview
The **PII Sanitizer API** is a security-focused microservice designed to prevent **Data Loss Prevention (DLP)** incidents. It leverages Large Language Models (LLM) via the Google Gemini API to contextually identify and redact **Personally Identifiable Information (PII)** from unstructured text streams.

Unlike robust regex patterns which often fail on context (e.g., distinguishing a phone number from an ID number), this API uses semantic understanding to scrub sensitive data, making it ideal for chat logs, support tickets, and user-generated content sanitization.

**Why this matters:** As part of my path toward **CISSP certification**, this tool demonstrates the practical application of **Software Development Security** principles to ensure compliance with regulations like **GDPR**, **CCPA**, and **HIPAA**.

## 🚀 Key Features
*   **AI-Driven Detection:** Uses `Gemini 1.5 Flash` for context-aware Entity Recognition (NER).
*   **High-Performance Backend:** Built on **FastAPI** for asynchronous request handling.
*   **Granular Redaction:** Replaces sensitive data with specific tags (e.g., `[REDACTED_PHONE]`, `[REDACTED_NAME]`) rather than generic masking.
*   **Scalable Architecture:** Designed to be containerized (Docker) and deployed as a serverless function.

## 🛠️ Tech Stack
*   **Language:** Python 3.11+
*   **Framework:** FastAPI + Uvicorn
*   **AI/LLM:** Google Generative AI (Gemini)
*   **Environment:** python-dotenv

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/pii-sanitizer-api.git
cd pii-sanitizer-api
```
### 2. SETUP
```
pip install -r requirements.txt
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### run code via Bash
```
uvicorn main:app --reload
```
## example request/response:
### Request:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/sanitize' \
  -H 'Content-Type: application/json' \
  -d '{
  "content": "Please contact Jane Doe at 123-456-7890 or email janedoe@somethingmail.com regarding the server outage."
}'
```
### Response(JSON):
""
{
  "original_length": 105,
  "sanitized_text": "Please contact [REDACTED_NAME] at [REDACTED_PHONE] or email [REDACTED_EMAIL] regarding the server outage."
}
""

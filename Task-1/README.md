# Task 1: Structured LLM Prompt Pipeline & JSON Extractor

## Project Description
I built a Python-based AI system that uses Google's Gemini AI to extract important information from invoice text files.

The system reads invoice text, sends it to Gemini AI, validates the extracted information using Pydantic, and returns structured JSON output.

## What I Built
- Python program to read invoice text files.
- Connection with Google's Gemini AI API.
- Reusable prompt function.
- Automatic invoice information extraction.
- Pydantic model for data validation.
- Structured JSON output.
- Error handling for missing files and invalid responses.

## Technologies Used
- Python
- Google Gemini AI
- Google GenAI SDK
- Pydantic
- JSON
- Python Dotenv

## Project Files
- `main.py` – Main Python program.
- `sample_invoice.txt` – Sample invoice data.
- `requirements.txt` – Required Python libraries.
- `README.md` – Project documentation.

## Setup
1. Install Python.
2. Install dependencies using `pip install -r requirements.txt`.
3. Create a `.env` file and add your own Gemini API key:

   `GEMINI_API_KEY=your_gemini_api_key_here`

4. Run the program using `python main.py`.

**Important:** Never upload your real `.env` file or API key to GitHub.

## Sample Output
```json
{
  "invoice_number": "INV-2050",
  "customer": "Ahmed Khan",
  "date": "2026-11-01",
  "total_amount": 25000.0,
  "payment_status": "Unpaid"
}
```

## What I Learned
- Python programming.
- Using Gemini AI API.
- Writing reusable prompts.
- Extracting structured data.
- JSON handling.
- Pydantic validation.
- Error handling.

## Author
**Musadiq Mehmood Qureshi**

- LinkedIn: https://www.linkedin.com/in/musadiq-qureshi-32271936a
- GitHub: https://github.com/musadiq-qureshi

## Internship
- Organization: Datheon
- Program: AI & ML Internship
- Task: Task 1 – Structured LLM Prompt Pipeline & JSON Extractor

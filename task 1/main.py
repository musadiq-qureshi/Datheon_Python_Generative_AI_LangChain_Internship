import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

# Load API key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Define invoice structure
class Invoice(BaseModel):
    invoice_number: str
    customer: str
    date: str
    total_amount: float
    payment_status: str

# Read invoice file
try:
    with open("sample_invoice.txt", "r") as file:
        invoice_text = file.read()

except FileNotFoundError:
    print("Error: Invoice file not found!")
    exit()
# Create extraction prompt
def create_invoice_prompt(invoice_text):
    return f"""
    Extract the following information from this invoice.

    Return only valid JSON with these fields:
    invoice_number, customer, date, total_amount, payment_status.

    Invoice:
    {invoice_text}
    """

prompt = create_invoice_prompt(invoice_text)
print("Sending invoice to Gemini...")

# Get information from Gemini
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_schema": Invoice
    }
)

# Validate Gemini response
try:
    invoice = Invoice.model_validate_json(response.text)

except Exception as e:
    print("Error: Invoice data validation failed!")
    print(e)
    exit()

# Display final result
print("\nInvoice Extraction Successful!")
print(invoice.model_dump_json(indent=4))
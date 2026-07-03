import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def rule_based_strategy():
    return """
Negotiation Strategy

• Explain your financial hardship.
• Request a lower settlement amount.
• Ask for EMI restructuring if settlement is not possible.
• Maintain polite and professional communication.
"""


def generate_strategy():

    if not GOOGLE_API_KEY:
        print("Gemini API Key not found.")
        print("Using Rule-Based Strategy...\n")
        return rule_based_strategy()

    try:
        import google.generativeai as genai

        genai.configure(api_key=GOOGLE_API_KEY)

        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = """
Generate a professional loan settlement negotiation strategy
for a borrower with financial hardship.
"""

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        print("Gemini API Error:", e)
        print("\nUsing Rule-Based Strategy...\n")
        return rule_based_strategy()


print(generate_strategy())
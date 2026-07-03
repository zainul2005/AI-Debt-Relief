import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def call_ai(prompt: str):

    if not GOOGLE_API_KEY:
        return "Gemini API key not found. Using fallback response."

    try:
        import google.generativeai as genai

        genai.configure(api_key=GOOGLE_API_KEY)

        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(prompt)

        return response.text

    except ImportError:
        return "Gemini package is not installed. Using fallback response."

    except Exception:
        return "AI service is temporarily unavailable. Using rule-based recommendation."
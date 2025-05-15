from flask import Flask, render_template, request
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

# Replace with your actual Gemini API key
client = genai.Client(api_key="AIzaSyDNiBsbqkhe-nmze0uRwr80taQLCYfxpYo")

def ask_gemini(user_prompt, temperature=0.5):
    response = client.models.generate_content(
        model="gemini-2.0-pro",
        contents=[
            {
                "role": "system",
                "parts": [
                    "You are a helpful and concise code assistant. "
                    "You explain, generate, and debug code for the user in simple, clear terms."
                ],
            },
            {
                "role": "user",
                "parts": [user_prompt],
            },
        ],
        generation_config={
            "temperature": temperature
        }
    )
    return response.text.strip()

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    temperature = 0.5
    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        try:
            temperature = float(request.form.get("temperature", 0.5))
        except ValueError:
            temperature = 0.5
        output = ask_gemini(prompt, temperature)
    return render_template("index.html", output=output, temperature=temperature)

if __name__ == "__main__":
    app.run(debug=True)
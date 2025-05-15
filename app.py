from flask import Flask, render_template, request
from google import genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Set model
model = client.models.get("gemini-2.0-pro")

app = Flask(__name__)

def ask_gemini(user_prompt, temperature=0.5):
    response = model.generate_content(
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
        generation_config=genai.types.GenerationConfig(
            temperature=temperature
        )
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
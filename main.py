import google.generativeai as genai

genai.configure(api_key="AIzaSyDNiBsbqkhe-nmze0uRwr80taQLCYfxpYo")

response = genai.generate_text(
    model="gemini-pro",
    prompt="Explain how AI works in a few words",
)

print(response.text)
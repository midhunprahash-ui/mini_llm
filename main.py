import google.generativeai as genai

genai.configure(api_key="AIzaSyDNiBsbqkhe-nmze0uRwr80taQLCYfxpYo")

# Initialize the model with safety settings
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

# Initialize the model
model = genai.GenerativeModel(model_name='gemini-pro', safety_settings=safety_settings)

# Generate the response
response = model.generate_content("Explain how AI works in a few words")

# Print the response
print(response.text)
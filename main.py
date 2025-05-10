import google.generativeai as genai

# Configure the client
genai.configure(api_key="AIzaSyDNiBsbqkhe-nmze0uRwr80taQLCYfxpYo")

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# Generate the response
response = model.generate_content("Explain how AI works in a few words")

# Print the response
print(response.text)
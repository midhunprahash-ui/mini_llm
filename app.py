from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    temperature = 0.5
    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        output = f"Received prompt: {prompt}"  # TEMP TEST LINE
    return render_template("index.html", output=output, temperature=temperature)

if __name__ == "__main__":
    app.run(debug=True)
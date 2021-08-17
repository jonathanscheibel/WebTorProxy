from app import app


@app.route("/")
def home():
    return {"Proprietario": "https://jonathanscheibel.github.io"}

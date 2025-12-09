from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/example")
def example():
    return jsonify(message="Example endpoint works")

if __name__ == "__main__":
    app.run(debug=True)


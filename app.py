from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!doctype html>
    <html>
      <head><title>Student Management</title></head>
      <body style="font-family: Arial; max-width: 700px; margin: 50px auto; line-height: 1.6;">
        <h1>Student Management Application</h1>
        <h2>Welcome to Kubernetes!</h2>
        <p><b>Student:</b> Rahul</p>
        <p><b>Course:</b> DevOps</p>
        <p><b>Status:</b> Active</p>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

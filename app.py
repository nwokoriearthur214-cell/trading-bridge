import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bridge is active"

if __name__ == '__main__':
    # Use the PORT environment variable provided by Render, default to 10000
    port = int(os.environ.get("PORT", 10000))
    # Bind to 0.0.0.0 so Render can reach the app
    app.run(host='0.0.0.0', port=port)

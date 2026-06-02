import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bridge is active"

if __name__ == '__main__':
    # This specifically tells the server to stay open
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

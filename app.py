import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bridge is active"

# We are hard-coding the port to 10000 to match exactly what Render expects
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

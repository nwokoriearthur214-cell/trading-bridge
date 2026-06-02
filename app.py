import os
from flask import Flask

app = Flask(__name__)

# This line ensures Render stays happy
@app.route('/')
def home():
    return "Bridge is active"

# This forces the app to listen on the port Render requires
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

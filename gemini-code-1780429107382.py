from flask import Flask, request, jsonify
import httpx

app = Flask(__name__)

# This is the "doorway" where your signals arrive
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received signal: {data}")
    
    # Logic to talk to TopstepX goes here
    # Example: Send the order to TopstepX API
    # response = httpx.post("TOPSTEP_API_URL", json=data)
    
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
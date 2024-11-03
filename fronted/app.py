from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/frontend-hello')
def frontend_hello():
    backend_response = requests.get('http://13.233.151.229/hello')
    return jsonify(message="Hello from the frontend!", backend_message=backend_response.text)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=5000)


from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/frontend-hello')
def frontend_hello():
    backend_response = requests.get('http://localhost:8081/hello')
    return jsonify(message="Hello from the frontend!", backend_message=backend_response.text)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def root():
    return 'Сервер запущен'

@app.route('/api/ping')
def ping():
    return jsonify({
        "message": "pong",
        "delay": "10ms"
    })

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
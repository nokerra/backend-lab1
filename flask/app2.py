from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def root():
    return 'Сервер запущен'

@app.route('/api/songs')
def songs():
    return jsonify({
        "Shaman": "Ya russkii",
        "temnii princ": "utekai",
        "EGOR KRID": "Malo 2.0"
    })

@app.route('/api/albums')
def albums():
    return jsonify({
        "Shaman": "ROSSIYA",
        "temnii princ": "MILITANTUM",
        "EGOR KRID": "<3"
    })

@app.errorhandler(404) 
def error404(error): 
    return jsonify({ "error": "Not Found" }), 404 

if __name__ == '__main__':
    app.run(port = 3000, debug = True)

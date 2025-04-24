from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({"result": a + b})

@app.route('/subtract')
def subtract():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({"result": a - b})

@app.route('/multiply')
def multiply():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({"result": a * b})

@app.route('/divide')
def divide():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    if b == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400
    return jsonify({"result": a / b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

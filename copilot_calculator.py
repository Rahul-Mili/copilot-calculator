from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Define calculator operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def exponent(a, b):
    return a ** b

# Define API endpoints
@app.route('/add/', methods=['GET'])
def add_endpoint():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = add(a, b)
        return jsonify({"operation": "add", "a": a, "b": b, "result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide numeric values for 'a' and 'b'."}), 400

@app.route('/subtract/', methods=['GET'])
def subtract_endpoint():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = subtract(a, b)
        return jsonify({"operation": "subtract", "a": a, "b": b, "result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide numeric values for 'a' and 'b'."}), 400

@app.route('/multiply/', methods=['GET'])
def multiply_endpoint():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = multiply(a, b)
        return jsonify({"operation": "multiply", "a": a, "b": b, "result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide numeric values for 'a' and 'b'."}), 400

@app.route('/divide/', methods=['GET'])
def divide_endpoint():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        if b == 0:
            return jsonify({"error": "Division by zero is not allowed."}), 400
        result = divide(a, b)
        return jsonify({"operation": "divide", "a": a, "b": b, "result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide numeric values for 'a' and 'b'."}), 400

@app.route('/exponent/', methods=['GET'])
def exponent_endpoint():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = exponent(a, b)
        return jsonify({"operation": "exponent", "a": a, "b": b, "result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide numeric values for 'a' and 'b'."}), 400

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
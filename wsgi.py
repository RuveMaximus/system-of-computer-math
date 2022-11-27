from flask import Flask, request, render_template, jsonify
from modules.vectors import vector
from modules.matrices import matrix
import functions

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html', result="")

@app.route("/vector/")
def vector_template():
    return render_template('vector.html', result="")

@app.route("/matrix/")
def matrix_template():
    return render_template('matrix.html', result="")

@app.route('/functions/', methods=['POST'])
def send_functions():
    request_data = request.get_json()

    return jsonify({
        'status': 'ok',
        'functions': functions.functions.get(request_data['type'])
    })

@app.route("/vector/calc/")
def calc_vector():
    functions = {
        "plus": vector.plus,
        "minus": vector.minus,
        "multi": vector.multi,
        "multi_scalar": vector.multi_scalar,
        "dev_scalar": vector.dev_scalar,
        "is_coliniar": vector.is_coliniar,
        "is_codirected": vector.is_codirected,
        "is_not_codirected": vector.is_not_codirected,
        "is_equal": vector.is_equal,
        "is_orthogonal": vector.is_orthogonal,
        "length": vector.length,
        "ration": vector.ration,
        "reverse": vector.reverse,
        "angle": vector.angle,
        "cos": vector.cos,
    }
    
    func = str(request.args.get("func"))

    v1 = list(map(float, request.args.get("v1").split(';')))
    v2 = list(map(float, request.args.get("v2").split(';')))

    if "scalar" in func: 
        v2 = float(request.args.get("v2").split(';')[0])
    try:
        return str(functions.get(func)(v1, v2)) if functions.get(func) else 'Неизвестная операция'

    except Exception as e:
        print(e)
        return 'Сервер лег, но бригада фиксиков уже выехала!'


@app.route('/matrix/calc/', methods=['POST'])
def calc_matrix():
    functions = {
        'sum': matrix.summ,
        'dif': matrix.dif,
    }
    request_data = request.get_json()

    func = functions.get(request_data['func'])
    m1 = request_data['first_matrix']
    m2 = request_data['second_matrix']

    return jsonify({
        'status': 'ok', 
        'result': func(m1, m2)
    })

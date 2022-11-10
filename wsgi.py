from flask import Flask, request, render_template
from vectors import vector

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html', result="")


@app.route("/calc/vector/")
def calc():
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


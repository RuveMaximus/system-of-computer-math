from flask import Flask, request, render_template, send_from_directory
from vectors import vector

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html', result="")


@app.route("/calc/")
def calc():
    func = str(request.args.get("func"))

    v1 = list(map(float, request.args.get("v1").split(';')))
    v2 = list(map(float, request.args.get("v2").split(';')))

    try:
        result = []
        if func == 'plus':
            result = vector.plus(v1, v2)

        elif func == 'minus':
            result = vector.minus(v1, v2)

        elif func == 'multi':
            result = vector.multi(v1, v2)
        
        elif func == 'multi_scalar':
            result = vector.multi_scalar(v1, v2[0])

        elif func == 'dev_scalar':
            result = vector.dev_scalar(v1, v2[0])

        elif func == 'coliniar':
            result = vector.coliniar(v1, v2)

        else: 
            return "Неизвестная операция!"

        return str(result)

    except Exception as e:
        return str(e)


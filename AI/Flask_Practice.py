from flask import Flask,render_template
from flask import request

from ClassPractice import Chaotic_AI



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hiszpan"

@app.route("/Burak")
def hello2():
    return "Burak"


@app.route("/x3")
def mnoz3():
    given_int = request.args.get('given_int', default=0, type=int)
    return str(given_int*3)

@app.route("/xy")
def mnozsiebie():
    given_x = request.args.get('given_x', default =0, type=int)
    given_y = request.args.get('given_y', default =0, type=int)
    return str(given_x*given_y)


@app.route("/AI_turn")
def AI_turn():
    random_int = Chaotic_AI.random_spot(None)
    return str(random_int)

if __name__ == '__main__':
    app.run()

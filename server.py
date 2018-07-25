from flask import Flask, render_template, request, redirect, session

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

METHODS = ['GET', 'POST', 'PUT', 'DELETE']
counts= {}

@app.route('/')
def welcome():
    note="Welcome"
    return render_template('index.html', note=note, counts=counts)

@app.route('/request_counter')
def visit_counter():
    global counts
    for item in METHODS:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1
    return redirect('/')

if __name__ == '__main__':
    app.secret_key = 'visit'
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
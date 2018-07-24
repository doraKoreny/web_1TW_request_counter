from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)

counts= 0

@app.route('/')
def welcome():
    note="Welcome"
    return render_template('index.html', note=note, counts=counts)

@app.route('/request_counter')
def visit_counter():
    global counts
    counts += 1
    return redirect('/')

if __name__ == '__main__':
    app.secret_key = 'visit'
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
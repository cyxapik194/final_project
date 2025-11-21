from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', mathods=['POST', 'GET'])
def index():
    name = request.form['button_python']
    return render_template('index.html', button_python=name)










app.run(debug=True)
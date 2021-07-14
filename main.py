from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_home():
    return '<p>Hello, World!</p>'


@app.route('/hidden_element', methods=['GET'])
def get_hidden_element():
    return render_template('hidden_element.html')

from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_home():
    return '<p>Hello, World!</p>'


@app.route('/hidden_element', methods=['GET'])
def get_hidden_element():
    return render_template('hidden_element.html')


@app.route('/hidden_element2', methods=['GET'])
def get_hidden_element2():
    page_no = request.args.get('p', 1, type=int)
    clear = request.args.get('clear')
    return render_template('hidden_element2.html', page_no=page_no, clear=clear,
                           current_url=url_for('get_hidden_element2'))

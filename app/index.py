from flask import render_template, request
from app import app

count = 0
@app.route('/')
def index():
    gibberish = "this is gibberish"
    return render_template('index.html', latex=gibberish)


@app.route('/submit_latex', methods=['POST'])
def submit_latex():
    latex = request.form['Latex']
    return render_template('index.html', latex=latex)

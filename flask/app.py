# app.py

from flask import Flask, render_template

app = Flask(__name__)
app.template_folder = 'templates'
@app.route('/')
def hello():
    return render_template('index.html', message1='Hello, World!')
@app.route('/1')
def hello2():
    return render_template('index.html', message1='Hello, World2!')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root_page():
    return 'Hello World'


@app.route('/content')
def content_page():
    return '<h1>Testing the flask app</h1>'


@app.route('/about')
def about_page():
    return '<b>Эта страница, описывающая модель машинного обучения</b>'


@app.route('/index/<int:num>')
def index_page(num):
    return render_template('index.html', n=num)


if __name__ == '__main__':
    app.run(debug=True)

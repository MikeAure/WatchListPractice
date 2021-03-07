from flask import Flask, escape

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to my watchlist!'


@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)


if __name__ == '__main__':
    app.run()

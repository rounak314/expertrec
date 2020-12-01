import sys
from MyPlexer import MyPlexer

app = MyPlexer()

@app.route('hello')
def hello():
    return 'Hello, World!'


@app.route('bye')
def bye():
    return 'bye'


eval(sys.argv[1])()
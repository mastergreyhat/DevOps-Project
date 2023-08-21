from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'First DevOps Project! Git integration successful'

if __name__ == '__main__':
    app.run(debug=True)

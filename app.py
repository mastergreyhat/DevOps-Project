from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'iFirst DevOps Project!<br>Git integration success'

if __name__ == '__main__':
    app.run(debug=True)

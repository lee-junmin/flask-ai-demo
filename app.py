from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Flask Application Insights Demo 😊</h1>'

@app.route('/fail')
def fail():
    a = 1
    b = 0
    c = a / b

if __name__ == '__main__':
    app.run(host='localhost', port=8080, threaded=True)
    
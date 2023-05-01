from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask Application Insights demo 😊'

@app.route('/fail')
def fail():
    a = 1
    b = 0
    c = a / b

if __name__ == '__main__':
   app.run()
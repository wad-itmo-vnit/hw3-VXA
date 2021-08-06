from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/img/<number>')
def image(number):
    filename = './static/images/dota' + str(number) + '.jpg'
    return send_file(filename)

app.run(host="localhost", port=5000)

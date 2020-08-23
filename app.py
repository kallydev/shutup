from flask import Flask, request
from jinja2 import FileSystemLoader, Environment

from obfuscation import obfuscation

app = Flask(__name__)
environment = Environment(loader=FileSystemLoader('template'))


@app.route('/result', methods=['POST'])
def result():
    template = environment.get_template('result.html')
    return template.render(result=obfuscation(request.form["content"]))


@app.route('/')
def index():
    template = environment.get_template('index.html')
    return template.render()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=443, ssl_context=('ssl/cert.pem', 'ssl/key.pem'))

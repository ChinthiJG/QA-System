from flask import Flask,request,render_template
import os


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('from_my1.html')

@app.route('/',methods=['POST'])
def my():
    text = request.form['u']
    processed_text = text.upper()

    return processed_text

if  __name__=='__main__':
    app.run()
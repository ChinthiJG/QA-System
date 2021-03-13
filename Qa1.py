
from flask import Flask,request,jsonify,render_template
from flask_cors import CORS

from bert import QA

app = Flask(__name__)
CORS(app)

model = QA("model")

#def do_something(doc,q):
   #doc = text1.upper() 
   #q = text2.upper()
   #out = model.predict(doc,q)
   #return combine

@app.route('/')
def index():
    return render_template('from_ex.html')

@app.route('/api',methods=['POST'])
def predict():
    
    doc = "chinthaka born in 1996."
    input_data = request.json['input']
    app.logger.info("api_input: " + str(input_data))
    answer = model.predict(doc,input_data)
    app.logger.info("api_output: " + str(answer))
    response = jsonify(answer)
    #return render_template('from_ex.html',response=response)
    return response
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

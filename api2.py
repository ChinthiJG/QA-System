import os  
from flask import Flask,request,jsonify
from flask_cors import CORS

from bert import QA

app = Flask(__name__)
CORS(app)

model = QA("model")

@app.route("/predict",methods=['POST'])
def predict():
    doc = request.json["document"]
    q = request.json["question"]
    try:
        out = model.predict(doc,q)
        return jsonify({"result":out})
    except Exception as e:
        print(e)
        return jsonify({"result":"Model Failed"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))

    if port == 8000:
        app.debug = True

    app.run(host='localhost', port=port)

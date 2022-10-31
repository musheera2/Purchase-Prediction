from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import matplotlib
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('classifier.pkl', 'rb'))
@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        Age= int(request.form["Age"])
        Estimated_Salary=float(request.form["EstimatedSalary"])
        Gender = int(request.form["Gender"])
        
        prediction=model.predict([[Gender,Age,Estimated_Salary]])

    if prediction==1:
        return render_template('index.html', prediction_text="The Customer will purchase")

    else:
        return render_template('index.html', prediction_text="The The Customer will not purchase")
                
if __name__=="__main__":
    app.run(debug=True)

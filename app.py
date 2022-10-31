# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 19:32:11 2020

@author: Praveen Bhargav
"""

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import matplotlib
from sklearn.preprocessing import StandardScaler


app= Flask(__name__)
model= pickle.load(open("classifier.pkl", "rb"))

@app.route('/', methods=['POST'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method=="POST":
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

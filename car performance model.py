# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 19:19:02 2021

@author: Mrinmoi
"""

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app=Flask(__name__)
pickle_in=open('multi.pkl','rb')
model=pickle.load(pickle_in)
Swagger(app)

@app.route('/')
def welcome():
    return "Welcome. Please type apidocs after the link"

@app.route('/predict',methods=['Get'])
def predict_performance():
    """
    Let's find Car performance
    ---
    parameters:
        - name: cylinders
          in: query
          type: number
          required: True
        - name: displacement
          in: query
          type: number
          required: True
        - name: horsepower
          in: query
          type: number
          required: True
        - name: weight
          in: query
          type: number
          required: True
        - name: acceleration
          in: query
          type: number
          required: True
        - name: model_year
          in: query
          type: number
          required: True
        - name: origin
          in: query
          type: number
          required: True
    responses:
        200:
            description: the output values
    """
    cylinders=request.args.get('cylinders')
    displacement=request.args.get('displacement')
    horsepower=request.args.get('horsepower')
    weight=request.args.get('weight')
    acceleration=request.args.get('acceleration')
    model_year=request.args.get('model_year')
    origin=request.args.get('origin') 
    prediction=model.predict([[cylinders,displacement,horsepower,weight,acceleration,model_year,origin]])
    return "The predicted value is {}".format(prediction)

if __name__=='__main__':
    app.run()

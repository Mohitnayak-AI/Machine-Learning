# Import library --

import uvicorn
from fastapi import FastAPI
from banknote import BankNote
import numpy as np
import pandas as pd
import pickle

# create API --

app = FastAPI()
pickle_in = open("classifier.pkl","rb")
model = pickle.load(pickle_in)

# Index page - automaticaly opens on http://127.0.0.1:8000

@app.get('/')
def index():
    return {'message':'Hello, Stranger'}

# Route with a single parameters

@app.get('/{name}')
def get_name(name:str):
    return {'message':f'Hello {name}'}

# Expose the preiction fun, make a prediction from the passed JSON data and return a prediction

@app.post('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    print(data)
    print('Hello')
    variance = data['variance']
    print(variance)
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    print(model.predict([[variance,skewness,curtosis,entropy]]))
    print('Hello')
    prediction = model.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction = 'Fake Note'
    else:
        prediction = 'Its a Bank Note'
    return{
        'prediction' : prediction
    }

# Run the API

if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    age:float
    sex:float
    cp:float
    trestbps:float
    chol: float
    fbs:float
    restecg:float
    thalach:float
    exang:float
    oldpeak:float
    slope:float
    ca:float
    thal:float



# loading the saved model
model = pickle.load(open('heart.sav', 'rb'))


@app.post('/heart_prediction')
def diabetes_pred(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    age= input_dictionary['age']
    sex= input_dictionary['sex']
    cp= input_dictionary['cp']
    trestps= input_dictionary['trestps']
    chol= input_dictionary['chol']
    fbs= input_dictionary['fbs']
    restecq=input_dictinary['restecg']
    thalach=input_dictionary['thalach']
    exang=input_dictionary['exang']
    oldpeak=input_dictionary['oldpeak']
    slope=input_dictionary['slope']
    ca=input_dictionary['ca']
    thal=input_dictionary['thal']

    input_list = [age,sex,cp,trestps,chol,fbs,restecq,thalach,exang,oldpeak,slope,ca,thal]

    prediction =model.predict([input_list])

    if prediction[0] == 0:
        return 'Healthy Heart'

    else:
        return 'Defective Heart'



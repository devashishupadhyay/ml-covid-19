#importing pakages
import pickle as pkl
import numpy as np
import pandas as pd

class pred :

    def __init__(self,model,covid_19):
        self.model=pkl.load(open(model,'rb'))
        self.covid_19=pd.read_pickle(covid_19)
    
    def predict(self):
        pred = self.model.predict(self.covid_19.values)
        return pred
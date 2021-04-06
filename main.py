from core.covid import pred

model = pred('Model/model.sav','covid19-features-df/covid_19_strain.pkl')

print(model.predict())
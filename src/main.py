import pickle as pk
import numpy as np


with open("model_rdfs","rb") as f:
    model = pk.load(f)

def Predcition(age, sex, cp, trestbps, chol, fbs, restecg, thalag, examg, oldpeak, slope, ca ,thal):
    x = np.zeros(13)
    x[0] = age
    x[1] = sex
    x[2] = cp
    x[3] = trestbps
    x[4] = chol
    x[5] = fbs
    x[6] = restecg
    x[7] = thalag
    x[8] = examg
    x[9] = oldpeak
    x[10] = slope
    x[11] = ca
    x[12] = thal
    return model.predict([x])[0]

pre = Predcition(20, 1, 0, 100, 100, 0, 0, 150, 0, 3, 2, 1, 2)
print(pre)
import pickle as pi
import sklearn as sk
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
import os 
import uuid 
import urllib
from PIL import Image
from flask import Flask, render_template, request , jsonify, send_file
import base64

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
loaded_model_svm = pi.load(open('model/svm.pickle', "rb"))
loaded_model_knn = pi.load(open('model/knn.pickle',"rb"))
loaded_model_dst = pi.load(open('model/dst.pickle',"rb"))
loaded_model_rdfs = pi.load(open('model/rdfs.pickle',"rb"))

def Predcition(age, sex, cp, trestbps, chol, fbs, restecg, thalag, examg, oldpeak, slope, ca ,thal , model):
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
    model = model
    return round(model.predict([x])[0])



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index', methods=["POST"])
def predict():
    if request.method == "POST" :
        us_name = request.form["name"]
        tuoi = request.form["age"]
        gt = request.form["sex"].lower()
        if gt == 'nam' or gt == 'trai':
            gt = 1
        if gt == "nữ" or gt =='gái' or gt =='nu' or gt =='gai' :
            gt = 0
        tucnguc = request.form["cp"]
        if tucnguc == "Typical angina" :
            tucnguc = 0
        if tucnguc == "Atypical angina" :
            tucnguc = 1
        if tucnguc == "Non-anginal pain" :
            tucnguc = 2
        if tucnguc == "Asymptomatic" :
            tucnguc = 3
        huyetap = request.form["trestbps"]
        cholestoral = request.form["chol"]
        luongduong = request.form["fbs"].lower()
        if luongduong == 'có' or luongduong=='co' :
            luongduong = 1
        if luongduong == 'không'or luongduong =='khong':
            luongduong = 0
        nhiptim = request.form["thalach"]
        dientamdo = request.form["restecg"]
        if dientamdo == "Không có gì đáng lưu ý":
            dientamdo = 0
        if dientamdo == "Sóng ST-T bất thường":
            dientamdo = 1
        if dientamdo == "Phì đại thất trái có thể hoặc chắc chắn":
            dientamdo = 2
        daunguc = request.form["exang"].lower()
        if daunguc == "co" or daunguc == "có":
            daunguc = 1
        if daunguc == "khong" or daunguc == "không":
            daunguc = 0
        chechlech = request.form["oldpeak"]
        dodoc = request.form["slope"]
        if dodoc == "Upsloping" :
            dodoc = 0
        if dodoc == "Flatsloping" :
            dodoc = 1
        if dodoc == "Downslopins" :
            dodoc = 2
        machchinh = request.form["ca"]
        song = request.form["thal"]
        model = request.form["md"]
        if model == "K-Nearest Neighbors":
            model = loaded_model_knn
        if model == "Support Vector Machine":
            model = loaded_model_svm
        if model == "Decision Tree":
            model = loaded_model_dst
        if model == "Random Forest":
            model = loaded_model_rdfs
        if Predcition(tuoi,gt,tucnguc,huyetap,cholestoral,luongduong,dientamdo,nhiptim,daunguc,chechlech,dodoc,machchinh,song,model) == 1:
            return render_template("index2.html")
        if Predcition(tuoi,gt,tucnguc,huyetap,cholestoral,luongduong,dientamdo,nhiptim,daunguc,chechlech,dodoc,machchinh,song,model) == 0:
            return render_template("index3.html")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
    
# save this as app.py
from flask import Flask, request, render_template
import joblib
#import numpy as np

app = Flask(__name__)
model = joblib.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")

['cereal_yield', 'fdi_perc_gdp', 'gni_per_cap', 'en_per_cap', 'pop_urb_aggl_perc', 'prot_area_perc', 'pop_growth_perc', 'urb_pop_growth_perc']
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method ==  'POST':
        
        try:
            cereal_yield = float(request.form['cereal_yield'])
        except:
            cereal_yield = 0
        try:
            fdi_perc_gdp= float(request.form['fdi_perc_gdp'])
        except (ValueError):
            fdi_perc_gdp = 0
        try:
            gni_per_cap = float(request.form['gni_per_cap'])
        except (ValueError):
            gni_per_cap = 0
        try:
            en_per_cap = float(request.form['en_per_cap'])
        except (ValueError):
            en_per_cap = 0
        try:
            pop_urb_aggl_perc = float(request.form['pop_urb_aggl_perc'])
        except (ValueError):
            pop_urb_aggl_perc = 0
        try:
            prot_area_perc = float(request.form['prot_area_perc'])
        except (ValueError):
            prot_area_perc = 0
        try:
            pop_growth_perc = float(request.form['pop_growth_perc'])
        except (ValueError):
            pop_growth_perc = 0
        try:
            urb_pop_growth_perc = float(request.form['urb_pop_growth_perc'])
        except (ValueError):
            urb_pop_growth_perc = 0
        





        prediction = model.predict([[cereal_yield, fdi_perc_gdp, gni_per_cap, en_per_cap, pop_urb_aggl_perc, prot_area_perc, pop_growth_perc, urb_pop_growth_perc]])

        # print(prediction)

        if 0 in [cereal_yield, fdi_perc_gdp, gni_per_cap, en_per_cap, pop_urb_aggl_perc, prot_area_perc, pop_growth_perc, urb_pop_growth_perc]:
           return render_template("prediction.html", prediction_text="recheck values provided")
        else: 
            return render_template("prediction.html", prediction_text="{}".format(prediction[0]))




    else:
        return render_template("prediction.html")



if __name__ == "__main__":
    app.run(debug=True)
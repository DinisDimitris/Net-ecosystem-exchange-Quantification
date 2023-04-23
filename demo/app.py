from flask import Flask, request, render_template
import xgboost as xg
import numpy as np
import pandas as pd

# Load the xgboost model
xgb_r = xg.XGBRegressor()
xgb_r.load_model("xgb_final.json")

mdays=[31,28,31,30,31,30,31,31,30,31,30,31]

def isleap(year):
    leap=False
    if year % 4 == 0 and year % 100 != 0:
        leap=True
    elif year % 100 == 0:
        leap=False
    elif year % 400 ==0:
        leap=True
    else:
        leap=False
    return leap
def dayofyear(year,month,day):
    doy=0
    for mm in range(0,month):
        days=mdays[mm]
        if mm==1:
            if isleap(year):
                days=29
        for dd in range(0,days):
            if mm < month-1:
                doy=doy+1
            else:
                if dd < day:
                    doy=doy+1
    return doy

def get_season_by_date(month: int):
    season_map = {
    1 :'WINTER' ,
    2:'SPRING',
    3:'SUMMER',
    4:'AUTUMN'
    }
    season_index = month %12 // 3 + 1
    
    return season_map[season_index]


def interpret_predictions(nee: float, date: np.datetime64):
    season_nee_means = {
    "AUTUMN": 4.314248,
    "SPRING": 0.696710,
    "SUMMER": 2.887943,
    "WINTER": 1.484983
    }
    
    result = {}
    
    if (nee > 0):
        result["message1"] = "The agroecosystem is estimated to be a net carbon sink, with a net ecosystem exchange of %0.4f g C m-2 day-1" % nee
    else:
        result["message1"] = "The agroecosystem is estimated to be a net carbon source, with a net ecosystem exchange of %0.4f g C m-2 day-1" % nee
    
    season = get_season_by_date(date.month)
    
    season = season
    result["message2"] = "The season is " + season.lower()
    
    result["message3"] = "Average agroecosystem NEE in " + season.lower() + " is: " + str(season_nee_means[season]) + " g C m-2 day-1"
    
    if (nee > season_nee_means[season]):
        result["message4"] = "Your agroecosystem is estimated to have a higher carbon absorbtion capability than an average agroecosystem in " + season.lower()
    else:
        result["message4"] = "Your agroecosystem is estimated to have a lower carbon absorbtion capability than an average agroecosystem in " + season.lower()
    
    return result
    

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':    
        # Get the form data
        date = request.form['date']
        solar_rad = float(request.form['solar_rad'])
        init_density = float(request.form['init_density'])
        max_temp = float(request.form['max_temp'])
        min_temp = float(request.form['min_temp'])
        max_soil_temp = float(request.form['max_soil_temp'])
        min_soil_temp = float(request.form['min_soil_temp'])
        min_humidity = float(request.form['min_humidity'])
        max_humidity = float(request.form['max_humidity'])
        precipitation = float(request.form['precipitation'])
        wind_speed = float(request.form['wind_speed'])

        # Create a Pandas DataFrame from the form data
        df = pd.DataFrame({
            'TMAX_AIR': [max_temp],
            'TMAX_SOIL': [max_soil_temp],
            'TMIN_AIR': [min_temp],
            'D_W_PRECN': [precipitation],
            'WIND': [wind_speed],
            'HMAX_AIR': [max_humidity],
            'HMIN_AIR': [min_humidity],
            'TMIN_SOIL': [min_soil_temp],
            'RADN': [solar_rad],
            'initial planting density (m-2)1': [init_density]
        })

        date =pd.to_datetime(date)

        df['DOY'] = dayofyear(date.year, date.month, date.day)

        # Make the prediction using the loaded model
        pred_nee = xgb_r.predict(df)

        # Render the results page with the prediction
        return render_template('results.html', result=interpret_predictions(pred_nee, date))

    # Render the home page with the form
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
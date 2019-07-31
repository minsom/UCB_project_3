import os
import pandas as pd
import numpy as np
import csv

from flask import (Flask, jsonify, render_template, Response, request,redirect)

app = Flask(__name__)

##################################################
## Main Homepage
##################################################
@app.route("/")
def index():
    """Return the homepage."""
    return render_template('index.html')


@app.route("/survey")
def survey():
    return render_template('survey.html')

##################################################
## Soyoung and Elise's : /jsonShootingData
##################################################
# def to_json(row):
#     try:
#         return json.loads(row)
#     except:
#         return {}

# @app.route('/jsonShootingData')
# def getShooting():
#     data_file = './db/schoolShootingData_withGeoCoordinates_delrow811.csv'
#     data_file_pd = pd.read_csv(data_file, encoding='utf8')
#     df = pd.DataFrame(data_file_pd)

#     # fill empty values(NaN) to prevent SyntaxError in browser
#     df.fillna('NaN',inplace=True)
#     df["location"] = df["location"].map(lambda l: to_json(l.replace("'", '"')))

#     return jsonify(df.to_dict(orient="records"))




if __name__ == "__main__":
    app.run(debug=True)

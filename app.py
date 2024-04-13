import altair as alt
import pandas as pd
import ast
import json
from actions_and_services import load_services_data, get_services, get_suggested_actions
from collections import defaultdict
import requests
from integrate import parse_inputs, features_finder, calculate_risk_scores, get_life_data, get_life_expectancy_risks, get_health_data, get_health_risks
from flask_ngrok import run_with_ngrok
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/<string:zip_code>/<string:age>/<string:address>/<string:income>/<string:gender>/<string:race>/<string:veteran_status>/<string:education>")

def home(zip_code, age, address, income, gender, race, veteran_status, education):
    inputs={}
    inputs['zip_code'] = zip_code
    inputs['age'] = age
    inputs['address'] = address
    inputs['income'] = income
    inputs['gender'] = gender
    inputs['race'] = race
    inputs['veteran_status'] = veteran_status
    inputs['education'] = education
    parse_data=parse_inputs(inputs)
    feature_data=features_finder(**parse_data)
    # print(feature_data)
    calculate_risks,valid_variable_cnt, category_risks, cluster_risks = calculate_risk_scores(feature_data)
    return calculate_risks

# if __name__ == "__main__":
#     app.run()

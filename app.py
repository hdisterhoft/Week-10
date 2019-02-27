import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

app = Flask(__name__)

import prcp_data
import stations
tobs = [(85.0, 54.0, 71.66378066378067)]
start = [(62.0, 69.57142857142857, 74.0)]
end = [(62.0, 69.88636363636364, 80.0)]

@app.route("/api/v1.0/precipitation")
def something():
    return jsonify(prcp_data.precipitation)

@app.route("/api/v1.0/stations")
def station():
    return jsonify(stations.stations)

@app.route("/api/v1.0/tobs")
def tob():
    return jsonify(tobs)

@app.route("/api/v1.0/<start>")
def starts():
    return jsonify(start)

@app.route("/api/v1.0/<start>/<end>")
def ends(): 
    return jsonify(end)

if __name__ == '__main__':
    app.run(debug=True)

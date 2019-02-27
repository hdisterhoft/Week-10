import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

app = Flask(__name__)

import prcp_data
import stations


engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

@app.route("/api/v1.0/precipitation")
def something():
    return jsonify(prcp_data.precipitation)

@app.route("/api/v1.0/stations")
def station():
    return jsonify(stations.stations)

@app.route("/api/v1.0/tobs")
def tob():
    tobss = session.query(Measurement.tobs).filter(Measurement.date >= "2016-06-23").all()
    return jsonify(tobss)

@app.route("/api/v1.0/<start>")
def starts(start):
    starts_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    return jsonify(starts_results)

@app.route("/api/v1.0/<start>/<end>")
def ends(start,end): 
    start_end = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    return jsonify(start_end)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import pandas as pd
import geopandas as gd

#Set up Flask
app = Flask(__name__)

#Set up app routes
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")
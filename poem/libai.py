#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:43:30 2021

@author: ledi
"""
from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("qjq.html")
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True)

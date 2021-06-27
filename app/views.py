# coding: utf8
from app import app
from flask import render_template, request, abort, redirect, url_for
import datetime
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from app import models




# C'est ici qu'on demande à notre appli flask d'acheminer toutes les demandes d'URL à la racine vers la fonction index()
# A chaque fois qu'on ouvrira un navigateur pour accéder à l'indexe, c'est cette fonction qui sera appelé
# @app.route est un décorateur de la varibale app qui va encapsuler la fonction index() et acheminer les demande vers cette fonction

@app.route('/')
def index():
    date = datetime.datetime.now().strftime("%x %X")
    return render_template( 'index.html', date=date)

@app.route('/dashboard',  methods = ['POST', 'GET'])
def dashboard():
    rq = request.form
    near_ocean = False
    island = False
    inland = False
    min = rq["min-value"]
    max = rq["max-value"]

    if "near-ocean" in rq:
        near_ocean = True
    if "island" in rq:
        island = True
    if "inland" in rq:
        inland = True                

    models.graphique(min,max,inland,near_ocean,island)
    date = datetime.datetime.now().strftime("%x %X")
    return render_template( 'dashboard.html', date=date)


@app.route('/prediction')
def prediction():
    date = datetime.datetime.now().strftime("%x %X")
    return render_template( 'prediction.html', date=date)
    

@app.route('/visualisation')
def visualisation():
    date = datetime.datetime.now().strftime("%x %X")
    return render_template( 'visualisation.html', date=date)

@app.route('/accueil')
def accueil():
    date = datetime.datetime.now().strftime("%x %X")
    return render_template( 'accueil.html', date=date)

@app.route('/about')
def about():
    date = datetime.datetime.now().strftime("%x %X")
    return render_template( 'about.html', date=date)



@app.route('/predicted', methods = ['POST', 'GET'])
def predicted():
    print("---------")
    print(request)
    print("---------")
    longitude = request.form['longitude']
    print(longitude)
    print("---------")
    latitude = request.form['latitude']
    hma = request.form['median_age']
    rooms = request.form['total_rooms']
    bedrooms = request.form['total_bedrooms']
    population = request.form['population']
    households = request.form['households']
    income = request.form['median_income']
    ocean_prox = request.form['ocean_proximity']
    predict, rooms_house, bedrooms_rooms, bedrooms_house, pop_house = models.predict(longitude, latitude, hma, rooms, bedrooms, population, households, income, ocean_prox)
    print(predict)
    #longitude = 3
    #latitude = 3
    #hma = 3
    #rooms = 3
    #bedrooms = 3
    #population = 3
    #households = 3
    #income = 3
    #ocean_prox = 3
    #predict = 3 
    #rooms_house = 3
    #bedrooms_rooms = 3
    #bedrooms_house = 3 
    #pop_house = 3
    print("---------")
    date = datetime.datetime.now().strftime("%x %X")
    return render_template( 'predicted.html',date=date, longitude=longitude, latitude=latitude, hma=hma, rooms=rooms, bedrooms=bedrooms, population=population, households=households,  income=income,  ocean_prox=ocean_prox, predict=predict, 
    rooms_house=rooms_house, bedrooms_rooms=bedrooms_rooms, bedrooms_house=bedrooms_house, pop_house=pop_house)

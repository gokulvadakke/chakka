#!/usr/bin/python
# -*- coding: utf-8 -*-

import flask
from flask import request, jsonify
import requests
from datetime import datetime

app = flask.Flask(__name__)
app.config['DEBUG'] = True


# A route to return all of the available entries in our catalog.

@app.route('/', methods=['GET'])
def api_all():
    return 'You are not welcome here'


@app.route('/country', methods=['GET'])
def api_country():
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    country = ' '

    if 'country' in request.args:
        country = str(request.args['country'])
    else:
        return 'Error: No country field provided. Please specify a country .'

    # api-endpoint

    URL = 'https://api.covid19api.com/country/' + country + '?from=' \
        + str(currentYear) + '-' + str(currentMonth) + '-' \
        + str(currentDay) + 'T00:00:00Z&to=2020-07-21T00:00:00Z'

    # defining a params dict for the parameters to be sent to the API
    # PARAMS = {'address':location}

    # sending get request and saving the response as response object

    try:
        r = requests.get(url=URL)
        data = r.json()
        return jsonify(data[-1])
    except Exception as e:
        return 'Looks like there is no country by that name:' + repr(e)

    return 'Something is fishy'

@app.route('/global', methods=['GET'])
def api_global():
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    # api-endpoint

    URL = 'https://api.covid19api.com/summary'

    # defining a params dict for the parameters to be sent to the API
    # PARAMS = {'address':location}

    # sending get request and saving the response as response object

    
    r = requests.get(url=URL)
    data = r.json()
    return jsonify(data['Global'])

app.run()


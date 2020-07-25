#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'cases total' in incoming_msg:

        # return a quote

        r = requests.get('http://13.127.240.238:5000/global')
        if r.status_code == 200:
            data = r.json()
            quote = str(data['TotalConfirmed'])
        else:
            quote = 'I could not retrieve data at this time, sorry.'
        msg.body(quote)
        responded = True
    elif 'deaths total' in incoming_msg:

        # return a quote

        r = requests.get('http://13.127.240.238:5000/global')
        if r.status_code == 200:
            data = r.json()
            quote = str(data['TotalDeaths'])
        else:
            quote = 'I could not retrieve data at this time, sorry.'
        msg.body(quote)
        responded = True
    elif 'cases' in incoming_msg:

        # return a quote

        word_list = incoming_msg.split()

        if len(word_list) == 1:
            quote = 'Please type a country dude'
        else:
            country = word_list[-1]

            r = \
                requests.get('http://13.127.240.238:5000/country?country='
                              + country)
            if r.status_code == 200:
                data = r.json()
                quote = str(data['Confirmed'])
            else:
                quote = 'I could not retrieve data at this time, sorry.'
        msg.body(quote)
        responded = True
    elif 'deaths' in incoming_msg:

        # return a quote

        word_list = incoming_msg.split()

        if len(word_list) == 1:
            quote = 'Please type a country dude'
        else:
            country = word_list[-1]

            r = \
                requests.get('http://13.127.240.238:5000/country?country='
                              + country)
            if r.status_code == 200:
                data = r.json()
                quote = str(data['Deaths'])
            else:
                quote = 'I could not retrieve data at this time, sorry.'
        msg.body(quote)
        responded = True

    if not responded:
        msg.body('I dont understand your input, sorry!')
    return str(resp)

if __name__ == '__main__':
    app.run()

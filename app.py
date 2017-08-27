import os
import time
from instagram.client import InstagramAPI
from flask import Flask, request, render_template, session, redirect, abort, flash, jsonify
from fromTwitter import getTwitter

app = Flask(__name__)   # create our flask app
app.secret_key = 'f840e957109e4f1c2e1ca42cf96e710ad61209feeeecbf47'

CUR_HASHTAG = ''

@app.route('/')
def hastag_form():
  return render_template("index.html")

@app.route('/', metods['POST'])
def serve_hashtag():
  hashtag= request.form['text']
  CUR_HASHTAG = hashtag
  count = 5
  data = getTwitter(hashtag, count)

  return render_template('slider.html', data=data)

@app.route('/update_tweets')
def update_tweets():
  hashtag=CUR_HASHTAG
  count = 5
  data = getTwitter(hashtag, count)

  jsonify(data=data)

if __name__ == "__main__":
  app.debug = True
  
  port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
  app.run(host='0.0.0.0', port=port)


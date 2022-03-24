#!/usr/bin/env python
import flask

app = flask.Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello Bro or Sis!\n'

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    return 'How are you my friend %s?\n' % username

if __name__ == '__main__':
    app.run(host='0.0.0.0')     # open for everyone

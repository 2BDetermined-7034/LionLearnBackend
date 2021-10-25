from os import environ

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



password = 'supernova7034'
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ScoutingUser:'+ password + '@wlhsfrc.com/LionLearnDB'
#   if you don't do this, the sqlalchemy gods get mad and give you errors
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def main():  # put application's code here
    return 'Hello World!'

@app.route('/scouting')
def altmain():
    return 'Hello World!'





if __name__ == '__main__':
    app.run()

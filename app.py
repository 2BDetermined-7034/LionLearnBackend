# ============================================================================================================================================ #
# =================================================================={Imports}================================================================= #
# ============================================================================================================================================ #
import json
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# ============================================================================================================================================ #
# ==================================================================={Config}================================================================= #
# ============================================================================================================================================ #

password = 'supernova7034'
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ScoutingUser:'+ password + '@wlhsfrc.com/LionLearnDB'
#   if you don't do this, the sqlalchemy gods get mad and give you errors
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
loadGame = True

# ============================================================================================================================================ #
# ============================================================={Database classes}============================================================= #
# ============================================================================================================================================ #


class Teams(db.Model):
    __tablename__ = 'teamData'
    id = db.Column(db.Integer, primary_key=True)
    teamName = db.Column(db.String(200))
    teamNumber = db.Column(db.Integer)
    location = db.Column(db.String(200))
    teamLogo = db.Column(db.LargeBinary)

    def __init__(self, teamName, teamNumber, location, teamLogo):
        # General Data
        if teamLogo == "":
            teamLogo = "bm8gaW1hZ2UK"

        self.id = teamNumber
        self.teamName = teamName
        self.teamNumber = teamNumber
        self.location = location
        self.teamLogo = teamLogo


class Events(db.Model):
    __tablename__ = "eventData"
    id = db.Column(db.Integer, primary_key=True)
    eventName = db.Column(db.String(200))
    eventLocation = db.Column(db.String(200))
    eventDate = db.Column(db.Date)

    def __init__(self, Eid, eventName, eventLocation, eventDate):
        if Eid != 0:
            self.id = Eid  # If the event has an ID already (IE editing an event) then it'll re-use it
        self.eventName = eventName
        self.eventLocation = eventLocation
        self.eventDate = eventDate


class Robots(db.Model):
    __tablename__ = "robotData"
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.Integer)
    event = db.Column(db.String)
    wheels = db.Column(db.String(200))
    motor = db.Column(db.String(200))
    powerTrans = db.Column(db.String(200))
    driveTrain = db.Column(db.String(200))
    ODR = db.Column(db.Integer)

    def __init__(self, Rid, team, event, wheels, motor, powerTrans, driveTrain, ODR):
        if Rid != 0:
            self.id = Rid  # If the event has an ID already (IE editing an event) then it'll re-use it
        self.team = team
        self.event = event
        self.wheels = wheels
        self.motor = motor
        self.powerTrans = powerTrans
        self.driveTrain = driveTrain
        self.ODR = ODR


class Games(db.Model):
    __tablename__ = "gameData"
    id = db.Column(db.Integer, primary_key=True)

    eventID = db.Column(db.Integer)

    blueScore = db.Column(db.Integer)
    B1robotID = db.Column(db.Integer)
    B2robotID = db.Column(db.Integer)
    B3robotID = db.Column(db.Integer)

    redScore = db.Column(db.Integer)
    R1robotID = db.Column(db.Integer)
    R2robotID = db.Column(db.Integer)
    R3robotID = db.Column(db.Integer)

    if loadGame:
###START_OF_AUTOGAMESCLASS###
      R1IntLineExt = db.Column(db.Integer)
      R2IntLineExt = db.Column(db.Integer)
      R3IntLineExt = db.Column(db.Integer)
      B1IntLineExt = db.Column(db.Integer)
      B2IntLineExt = db.Column(db.Integer)
      B3IntLineExt = db.Column(db.Integer)

      R1Auto = db.Column(db.Integer)
      R2Auto = db.Column(db.Integer)
      R3Auto = db.Column(db.Integer)
      B1Auto = db.Column(db.Integer)
      B2Auto = db.Column(db.Integer)
      B3Auto = db.Column(db.Integer)

      R1TeloPowerPoints = db.Column(db.Integer)
      R2TeloPowerPoints = db.Column(db.Integer)
      R3TeloPowerPoints = db.Column(db.Integer)
      B1TeloPowerPoints = db.Column(db.Integer)
      B2TeloPowerPoints = db.Column(db.Integer)
      B3TeloPowerPoints = db.Column(db.Integer)

      R1CPP = db.Column(db.Integer)
      R2CPP = db.Column(db.Integer)
      R3CPP = db.Column(db.Integer)
      B1CPP = db.Column(db.Integer)
      B2CPP = db.Column(db.Integer)
      B3CPP = db.Column(db.Integer)

      R1EndGame = db.Column(db.Integer)
      R2EndGame = db.Column(db.Integer)
      R3EndGame = db.Column(db.Integer)
      B1EndGame = db.Column(db.Integer)
      B2EndGame = db.Column(db.Integer)
      B3EndGame = db.Column(db.Integer)

      R1ShieldSwitch = db.Column(db.Integer)
      R2ShieldSwitch = db.Column(db.Integer)
      R3ShieldSwitch = db.Column(db.Integer)
      B1ShieldSwitch = db.Column(db.Integer)
      B2ShieldSwitch = db.Column(db.Integer)
      B3ShieldSwitch = db.Column(db.Integer)

      R1Adjustments = db.Column(db.Integer)
      R2Adjustments = db.Column(db.Integer)
      R3Adjustments = db.Column(db.Integer)
      B1Adjustments = db.Column(db.Integer)
      B2Adjustments = db.Column(db.Integer)
      B3Adjustments = db.Column(db.Integer)

      R1Total = db.Column(db.Integer)
      R2Total = db.Column(db.Integer)
      R3Total = db.Column(db.Integer)
      B1Total = db.Column(db.Integer)
      B2Total = db.Column(db.Integer)
      B3Total = db.Column(db.Integer)
    ###END_OF_AUTOGAMESCLASS###

    #   2020 data
    def __init__(self, Gid, eventID, blueScore, B1robotID, B2robotID, B3robotID, redScore, R1robotID, R2robotID,
                 R3robotID
###START_OF_AUTOGAMESINIT###
, R1IntLineExt, R2IntLineExt, R3IntLineExt, B1IntLineExt, B2IntLineExt, B3IntLineExt, R1Auto, R2Auto, R3Auto, B1Auto, B2Auto, B3Auto, R1TeloPowerPoints, R2TeloPowerPoints, R3TeloPowerPoints, B1TeloPowerPoints, B2TeloPowerPoints, B3TeloPowerPoints, R1CPP, R2CPP, R3CPP, B1CPP, B2CPP, B3CPP, R1EndGame, R2EndGame, R3EndGame, B1EndGame, B2EndGame, B3EndGame, R1ShieldSwitch, R2ShieldSwitch, R3ShieldSwitch, B1ShieldSwitch, B2ShieldSwitch, B3ShieldSwitch, R1Adjustments, R2Adjustments, R3Adjustments, B1Adjustments, B2Adjustments, B3Adjustments, R1Total, R2Total, R3Total, B1Total, B2Total, B3Total
                 ###END_OF_AUTOGAMESINIT###
                 ):
        if Gid != 0:
            self.id = Gid
        self.eventID = eventID
        self.blueScore = blueScore
        self.B1robotID = B1robotID
        self.B2robotID = B2robotID
        self.B3robotID = B3robotID

        self.redScore = redScore
        self.R1robotID = R1robotID
        self.R2robotID = R2robotID
        self.R3robotID = R3robotID

        if loadGame:
###START_OF_AUTOGAMESPROP###
            self.R1IntLineExt = R1IntLineExt
            self.R2IntLineExt = R2IntLineExt
            self.R3IntLineExt = R3IntLineExt
            self.B1IntLineExt = B1IntLineExt
            self.B2IntLineExt = B2IntLineExt
            self.B3IntLineExt = B3IntLineExt

            self.R1Auto = R1Auto
            self.R2Auto = R2Auto
            self.R3Auto = R3Auto
            self.B1Auto = B1Auto
            self.B2Auto = B2Auto
            self.B3Auto = B3Auto

            self.R1TeloPowerPoints = R1TeloPowerPoints
            self.R2TeloPowerPoints = R2TeloPowerPoints
            self.R3TeloPowerPoints = R3TeloPowerPoints
            self.B1TeloPowerPoints = B1TeloPowerPoints
            self.B2TeloPowerPoints = B2TeloPowerPoints
            self.B3TeloPowerPoints = B3TeloPowerPoints

            self.R1CPP = R1CPP
            self.R2CPP = R2CPP
            self.R3CPP = R3CPP
            self.B1CPP = B1CPP
            self.B2CPP = B2CPP
            self.B3CPP = B3CPP

            self.R1EndGame = R1EndGame
            self.R2EndGame = R2EndGame
            self.R3EndGame = R3EndGame
            self.B1EndGame = B1EndGame
            self.B2EndGame = B2EndGame
            self.B3EndGame = B3EndGame

            self.R1ShieldSwitch = R1ShieldSwitch
            self.R2ShieldSwitch = R2ShieldSwitch
            self.R3ShieldSwitch = R3ShieldSwitch
            self.B1ShieldSwitch = B1ShieldSwitch
            self.B2ShieldSwitch = B2ShieldSwitch
            self.B3ShieldSwitch = B3ShieldSwitch

            self.R1Adjustments = R1Adjustments
            self.R2Adjustments = R2Adjustments
            self.R3Adjustments = R3Adjustments
            self.B1Adjustments = B1Adjustments
            self.B2Adjustments = B2Adjustments
            self.B3Adjustments = B3Adjustments

            self.R1Total = R1Total
            self.R2Total = R2Total
            self.R3Total = R3Total
            self.B1Total = B1Total
            self.B2Total = B2Total
            self.B3Total = B3Total
###END_OF_AUTOGAMESPROP###


@app.route('/')
def main():
    return '1 Connected'

@app.route('/scouting')
def altmain():
    return '1 Connected'





if __name__ == '__main__':
    app.run()

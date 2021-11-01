# ============================================================================================================================================ #
# =================================================================={Imports}================================================================= #
# ============================================================================================================================================ #
import datetime
import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# ============================================================================================================================================ #
# ==================================================================={Config}================================================================= #
# ============================================================================================================================================ #

app.debug = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
password = 'supernova7034'
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ScoutingUser:' + password + '@wlhsfrc.com/LionLearnDB'
loadGame = True
if os.environ.get('FLASK_ENV') != 'development':
    app.config['SERVER_NAME'] = 'wlhsfrc.com'

db = SQLAlchemy(app)


# ============================================================================================================================================ #
# ============================================================={Database classes}============================================================= #
# ============================================================================================================================================ #


class Teams(db.Model):
    __tablename__ = 'teamData'
    id = db.Column(db.Integer, primary_key=True)
    teamName = db.Column(db.String(200))
    teamNumber = db.Column(db.Integer)
    teamlocation = db.Column(db.String(200))
    teamLogo = db.Column(db.LargeBinary)

    def __init__(self, teamName, teamNumber, location, teamLogo):
        # General Data
        if teamLogo == "":
            teamLogo = "bm8gaW1hZ2UK"

        self.id = teamNumber
        self.teamName = teamName
        self.teamNumber = teamNumber
        self.teamlocation = location
        self.teamLogo = teamLogo


class Events(db.Model):
    __tablename__ = "eventData"
    id = db.Column(db.Integer, primary_key=True)
    eventName = db.Column(db.String(200))
    eventLocation = db.Column(db.String(200))
    eventDate = db.Column(db.Date)
    eventTeams = db.Column(db.String(20000))

    def __init__(self, eventName, eventLocation, eventDate, eventTeams):
        self.eventName = eventName
        self.eventLocation = eventLocation
        self.eventDate = eventDate
        self.eventTeams = eventTeams


class Robots(db.Model):
    __tablename__ = "robotData"
    id = db.Column(db.Integer, primary_key=True)
    teamID = db.Column(db.Integer)
    seasonID = db.Column(db.Integer)
    eventID = db.Column(db.Integer)

    driveBase = db.Column(db.String(20))
    isReliable = db.Column(db.BOOLEAN)

    climbPercent = db.Column(db.FLOAT)

    def __init__(self, team, season, event, drive, reliable, climb):
        self.teamID = team
        self.seasonID = season
        self.eventID = event

        self.driveBase = drive
        self.isReliable = reliable
        self.climbPercent = climb


# noinspection DuplicatedCode
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
                 ##START_OF_AUTOGAMESINIT###
                 , R1IntLineExt, R2IntLineExt, R3IntLineExt, B1IntLineExt, B2IntLineExt, B3IntLineExt, R1Auto, R2Auto,
                 R3Auto, B1Auto, B2Auto, B3Auto, R1TeloPowerPoints, R2TeloPowerPoints, R3TeloPowerPoints,
                 B1TeloPowerPoints, B2TeloPowerPoints, B3TeloPowerPoints, R1CPP, R2CPP, R3CPP, B1CPP, B2CPP, B3CPP,
                 R1EndGame, R2EndGame, R3EndGame, B1EndGame, B2EndGame, B3EndGame, R1ShieldSwitch, R2ShieldSwitch,
                 R3ShieldSwitch, B1ShieldSwitch, B2ShieldSwitch, B3ShieldSwitch, R1Adjustments, R2Adjustments,
                 R3Adjustments, B1Adjustments, B2Adjustments, B3Adjustments, R1Total, R2Total, R3Total, B1Total,
                 B2Total, B3Total
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


# ============================================================================================================================================ #
# ================================================================={routing}================================================================== #
# ============================================================================================================================================ #

@app.route('/scouting')
def altmain():
    return '0.5 somewhat connected'


@app.route('/scouting', subdomain='scouting')
def altsubmain():
    return '1 connected via subdomain'


@app.route('/', subdomain="scouting")
def submain():
    return '1 Connected'


@app.route('/inputTeam', subdomain='scouting', methods=["POST"])
def inputTeam():
    parameters = request.args

    name = parameters.get('teamName') or ''
    number = int(parameters.get('teamNumber') or -1)
    location = parameters.get('teamLocation') or ''
    logo = str.encode(parameters.get('teamLogo')) or str.encode('')

    # If you are editing, pass the ID of the object, else -1
    editID = int(parameters.get("editID") or -1)
    if editID > -1 and editID != number:
        return '0 edit ID must be equal to your team number'
    # Edit team
    elif editID == number and db.session.query(Teams).filter(Teams.id == number).count() > 0:
        if name != '':
            db.session.query(Teams).filter(Teams.id == editID).update({'teamName': name})
        if location != '':
            db.session.query(Teams).filter(Teams.id == editID).update({'teamlocation': location})
        if logo != '':
            db.session.query(Teams).filter(Teams.id == editID).update({'teamLogo': logo})  # Logos are stored in base64
        db.session.commit()
        return '1 Team updated'
    # submit team
    if number > 0:
        if db.session.query(Teams).filter(Teams.id == number).count() > 0:
            return '0 Team already exists, please add an editID param'
        data = Teams(name, number, location, logo)
        db.session.add(data)
        db.session.commit()
        return '1 Team entered'
    else:
        return '0 no valid team ID'


@app.route('/deleteTeam', subdomain='scouting', methods=["POST"])
def deleteTeam():
    teamID = request.args.get('id')
    item = Teams.query.get(teamID)
    if item:
        db.session.delete(item)
        db.session.commit()
        return '1 team deleted'
    return '0 team not on server'


@app.route('/getTeam', subdomain='scouting', methods=['POST'])
def getTeam():
    teamID = request.args.get('id')
    item = Teams.query.get(teamID)
    if item:
        team = {'teamNumber': item.teamNumber, 'teamName': item.teamName, 'teamlocation': item.teamlocation,
                'teamLogo': item.teamLogo.decode()}
        return team
    return '0 team not on server'


@app.route('/inputEvent', methods=['POST'])
def inputEvent():
    parameters = request.args

    name = parameters.get('eventName') or ''
    location = parameters.get('eventLocation') or ''
    date = parameters.get('eventDate') or datetime.date.today()
    teams = parameters.get('eventTeams') or ''

    editID = int(parameters.get('editID') or -1)

    if editID > -1:
        if db.session.query(Events).filter(Events.id == editID).count() == 0:
            return '0 event does not exist'
        if name != '':
            db.session.query(Events).filter(Events.id == editID).update({'eventName': name})
        if location != '':
            db.session.query(Events).filter(Events.id == editID).update({'eventLocation': location})
        if date != '':
            db.session.query(Events).filter(Events.id == editID).update({'eventDate': date})
        if teams != '':
            db.session.query(Events).filter(Events.id == editID).update({'eventTeams': teams})
        db.session.commit()
        return '1 event updated'

    data = Events(name, location, date, teams)
    db.session.add(data)
    db.session.commit()
    return '1 event added'


@app.route('/searchEventID', methods=["POST"])
def searchEventID():
    parameters = request.args

    name = parameters.get('eventName') or ''
    date = parameters.get('eventDate') or ''

    if name == '':
        return '0 you need a name'
    event = Events.query.filter(Events.eventName.like(Events.eventName + "%")).order_by(Events.eventDate.desc()).all()
    if date != '':
        event = Events.query.filter(Events.eventName.like(Events.eventName + "%"), Events.eventDate == date).all()
    return str(event[0].id)


@app.route('/getEvent', subdomain='scouting', methods=['POST'])
def returnEvent():
    eventID = request.args.get('id')
    item = Events.query.get(eventID)
    if item:
        event = {'eventName': item.eventName, 'eventLocation': item.eventLocation, 'eventDate': item.eventDate,
                 'eventTeams': item.eventTeams}
        return event
    return '0 event not on server'


@app.route('/deleteEvent', subdomain='scouting', methods=['POST'])
def deleteEvent():
    eventID = request.args.get('id')
    item = Events.query.get(eventID)
    if item:
        db.session.delete(item)
        db.session.commit()
        return '1 event deleted'
    return '0 event not on server'


@app.route('/inputRobot', methods=["POST"])
def inputRobot():
    parameters = request.args

    teamID = int(parameters.get('teamID') or -1)
    seasonID = int(parameters.get('seasonID') or -1)
    eventID = int(parameters.get('eventID') or -1)

    driveBase = parameters.get('driveBase') or ''
    isReliable = bool(parameters.get('isReliable') or False)
    climbPercent = float(parameters.get('climbPercent') or -1.0)

    editID = int(parameters.get('editID') or -1)

    if db.session.query(Teams).filter(Teams.id == teamID).count() == 0 or db.session.query(Events).filter(
            Events.id == eventID).count() == 0:
        return '0 Error, season or team not in database, please create these first'
    if db.session.query(Robots).filter(Robots.teamID == teamID, Robots.eventID == eventID).count() > 0:
        return '0 Robot exist already at this event, please edit it instead'

    if editID > -1:
        if db.session.query(Robots).filter(Robots.id == editID).count() == 0:
            return '0 event does not exist'
        if teamID != -1:
            db.session.query(Robots).filter(Robots.id == editID).update({'teamID': teamID})
        if seasonID != -1:
            db.session.query(Robots).filter(Robots.id == editID).update({'seasonID': seasonID})
        if eventID != -1:
            db.session.query(Robots).filter(Robots.id == editID).update({'eventID': eventID})
        if driveBase != '':
            db.session.query(Robots).filter(Robots.id == editID).update({'driveBase': driveBase})
        db.session.query(Robots).filter(Robots.id == editID).update({'isReliable': isReliable})
        if climbPercent != -1:
            db.session.query(Robots).filter(Robots.id == editID).update({'climbPercent': climbPercent})

        db.session.commit()
        return '1 robot updated'

    data = Robots(teamID, seasonID, eventID, driveBase, isReliable, climbPercent)
    db.session.add(data)
    db.session.commit()
    return '1 robot added'


@app.route('/getRobot')
def getRobot():

    return ''

@app.route('/searchRobotID', methods=["POST"])
def searchRobotID():
    parameters = request.args

    teamID = int(parameters.get('teamID') or -1)
    eventID = int(parameters.get('eventID') or -1)

    if teamID == -1 or eventID == -1:
        return '0 you need a team ID and an event ID'

    robot = db.session.query(Robots).filter(Robots.teamID == teamID, Robots.eventID == eventID)
    return str(robot[0].id)


if __name__ == '__main__':
    app.run()

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


class Games(db.Model):
    __tablename__ = "gameData"
    id = db.Column(db.Integer, primary_key=True)

    eventID = db.Column(db.Integer)
    matchID = db.Column(db.Integer)

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
        R1InnerCellsScored = db.Column(db.Integer)
        R2InnerCellsScored = db.Column(db.Integer)
        R3InnerCellsScored = db.Column(db.Integer)
        B1InnerCellsScored = db.Column(db.Integer)
        B2InnerCellsScored = db.Column(db.Integer)
        B3InnerCellsScored = db.Column(db.Integer)

        R1UpperCellsScored = db.Column(db.Integer)
        R2UpperCellsScored = db.Column(db.Integer)
        R3UpperCellsScored = db.Column(db.Integer)
        B1UpperCellsScored = db.Column(db.Integer)
        B2UpperCellsScored = db.Column(db.Integer)
        B3UpperCellsScored = db.Column(db.Integer)

        R1LowerCellsScored = db.Column(db.Integer)
        R2LowerCellsScored = db.Column(db.Integer)
        R3LowerCellsScored = db.Column(db.Integer)
        B1LowerCellsScored = db.Column(db.Integer)
        B2LowerCellsScored = db.Column(db.Integer)
        B3LowerCellsScored = db.Column(db.Integer)

        R1LeftAutoLine = db.Column(db.Boolean)
        R2LeftAutoLine = db.Column(db.Boolean)
        R3LeftAutoLine = db.Column(db.Boolean)
        B1LeftAutoLine = db.Column(db.Boolean)
        B2LeftAutoLine = db.Column(db.Boolean)
        B3LeftAutoLine = db.Column(db.Boolean)

        R1Defense = db.Column(db.Boolean)
        R2Defense = db.Column(db.Boolean)
        R3Defense = db.Column(db.Boolean)
        B1Defense = db.Column(db.Boolean)
        B2Defense = db.Column(db.Boolean)
        B3Defense = db.Column(db.Boolean)

        R1Trench = db.Column(db.Boolean)
        R2Trench = db.Column(db.Boolean)
        R3Trench = db.Column(db.Boolean)
        B1Trench = db.Column(db.Boolean)
        B2Trench = db.Column(db.Boolean)
        B3Trench = db.Column(db.Boolean)

        R1ClimbAttempt = db.Column(db.Boolean)
        R2ClimbAttempt = db.Column(db.Boolean)
        R3ClimbAttempt = db.Column(db.Boolean)
        B1ClimbAttempt = db.Column(db.Boolean)
        B2ClimbAttempt = db.Column(db.Boolean)
        B3ClimbAttempt = db.Column(db.Boolean)

        R1Climb = db.Column(db.Boolean)
        R2Climb = db.Column(db.Boolean)
        R3Climb = db.Column(db.Boolean)
        B1Climb = db.Column(db.Boolean)
        B2Climb = db.Column(db.Boolean)
        B3Climb = db.Column(db.Boolean)

        R1BuddyClimbAttempt = db.Column(db.Boolean)
        R2BuddyClimbAttempt = db.Column(db.Boolean)
        R3BuddyClimbAttempt = db.Column(db.Boolean)
        B1BuddyClimbAttempt = db.Column(db.Boolean)
        B2BuddyClimbAttempt = db.Column(db.Boolean)
        B3BuddyClimbAttempt = db.Column(db.Boolean)

        R1BuddyClimb = db.Column(db.Boolean)
        R2BuddyClimb = db.Column(db.Boolean)
        R3BuddyClimb = db.Column(db.Boolean)
        B1BuddyClimb = db.Column(db.Boolean)
        B2BuddyClimb = db.Column(db.Boolean)
        B3BuddyClimb = db.Column(db.Boolean)

        R1ParkedEG = db.Column(db.Boolean)
        R2ParkedEG = db.Column(db.Boolean)
        R3ParkedEG = db.Column(db.Boolean)
        B1ParkedEG = db.Column(db.Boolean)
        B2ParkedEG = db.Column(db.Boolean)
        B3ParkedEG = db.Column(db.Boolean)

        R1SpunCP = db.Column(db.Boolean)
        R2SpunCP = db.Column(db.Boolean)
        R3SpunCP = db.Column(db.Boolean)
        B1SpunCP = db.Column(db.Boolean)
        B2SpunCP = db.Column(db.Boolean)
        B3SpunCP = db.Column(db.Boolean)

        R1SetCPAttempt = db.Column(db.Boolean)
        R2SetCPAttempt = db.Column(db.Boolean)
        R3SetCPAttempt = db.Column(db.Boolean)
        B1SetCPAttempt = db.Column(db.Boolean)
        B2SetCPAttempt = db.Column(db.Boolean)
        B3SetCPAttempt = db.Column(db.Boolean)

        R1SetCP = db.Column(db.Boolean)
        R2SetCP = db.Column(db.Boolean)
        R3SetCP = db.Column(db.Boolean)
        B1SetCP = db.Column(db.Boolean)
        B2SetCP = db.Column(db.Boolean)
        B3SetCP = db.Column(db.Boolean)

        R1SetCPColorAttempt = db.Column(db.Boolean)
        R2SetCPColorAttempt = db.Column(db.Boolean)
        R3SetCPColorAttempt = db.Column(db.Boolean)
        B1SetCPColorAttempt = db.Column(db.Boolean)
        B2SetCPColorAttempt = db.Column(db.Boolean)
        B3SetCPColorAttempt = db.Column(db.Boolean)

        R1SetCPColor = db.Column(db.Boolean)
        R2SetCPColor = db.Column(db.Boolean)
        R3SetCPColor = db.Column(db.Boolean)
        B1SetCPColor = db.Column(db.Boolean)
        B2SetCPColor = db.Column(db.Boolean)
        B3SetCPColor = db.Column(db.Boolean)

        R1GroundIntake = db.Column(db.Boolean)
        R2GroundIntake = db.Column(db.Boolean)
        R3GroundIntake = db.Column(db.Boolean)
        B1GroundIntake = db.Column(db.Boolean)
        B2GroundIntake = db.Column(db.Boolean)
        B3GroundIntake = db.Column(db.Boolean)

        R1Disabled = db.Column(db.Boolean)
        R2Disabled = db.Column(db.Boolean)
        R3Disabled = db.Column(db.Boolean)
        B1Disabled = db.Column(db.Boolean)
        B2Disabled = db.Column(db.Boolean)
        B3Disabled = db.Column(db.Boolean)

        R1Brownout = db.Column(db.Boolean)
        R2Brownout = db.Column(db.Boolean)
        R3Brownout = db.Column(db.Boolean)
        B1Brownout = db.Column(db.Boolean)
        B2Brownout = db.Column(db.Boolean)
        B3Brownout = db.Column(db.Boolean)
    ###END_OF_AUTOGAMESCLASS###

    #   2020 data
    def __init__(self, eventID, matchID, blueScore, B1robotID, B2robotID, B3robotID, redScore, R1robotID, R2robotID, R3robotID
###START_OF_AUTOGAMESINIT###
, R1InnerCellsScored, R2InnerCellsScored, R3InnerCellsScored, B1InnerCellsScored, B2InnerCellsScored, B3InnerCellsScored
, R1UpperCellsScored, R2UpperCellsScored, R3UpperCellsScored, B1UpperCellsScored, B2UpperCellsScored, B3UpperCellsScored
, R1LowerCellsScored, R2LowerCellsScored, R3LowerCellsScored, B1LowerCellsScored, B2LowerCellsScored, B3LowerCellsScored
, R1LeftAutoLine, R2LeftAutoLine, R3LeftAutoLine, B1LeftAutoLine, B2LeftAutoLine, B3LeftAutoLine
, R1Defense, R2Defense, R3Defense, B1Defense, B2Defense, B3Defense
, R1Trench, R2Trench, R3Trench, B1Trench, B2Trench, B3Trench
, R1ClimbAttempt, R2ClimbAttempt, R3ClimbAttempt, B1ClimbAttempt, B2ClimbAttempt, B3ClimbAttempt
, R1Climb, R2Climb, R3Climb, B1Climb, B2Climb, B3Climb
, R1BuddyClimbAttempt, R2BuddyClimbAttempt, R3BuddyClimbAttempt, B1BuddyClimbAttempt, B2BuddyClimbAttempt, B3BuddyClimbAttempt
, R1BuddyClimb, R2BuddyClimb, R3BuddyClimb, B1BuddyClimb, B2BuddyClimb, B3BuddyClimb
, R1ParkedEG, R2ParkedEG, R3ParkedEG, B1ParkedEG, B2ParkedEG, B3ParkedEG
, R1SpunCP, R2SpunCP, R3SpunCP, B1SpunCP, B2SpunCP, B3SpunCP
, R1SetCPAttempt, R2SetCPAttempt, R3SetCPAttempt, B1SetCPAttempt, B2SetCPAttempt, B3SetCPAttempt
, R1SetCP, R2SetCP, R3SetCP, B1SetCP, B2SetCP, B3SetCP
, R1SetCPColorAttempt, R2SetCPColorAttempt, R3SetCPColorAttempt, B1SetCPColorAttempt, B2SetCPColorAttempt, B3SetCPColorAttempt
, R1SetCPColor, R2SetCPColor, R3SetCPColor, B1SetCPColor, B2SetCPColor, B3SetCPColor
, R1GroundIntake, R2GroundIntake, R3GroundIntake, B1GroundIntake, B2GroundIntake, B3GroundIntake
, R1Disabled, R2Disabled, R3Disabled, B1Disabled, B2Disabled, B3Disabled
, R1Brownout, R2Brownout, R3Brownout, B1Brownout, B2Brownout, B3Brownout

###END_OF_AUTOGAMESINIT###
                 ):
        self.eventID = eventID
        self.matchID = matchID
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
            self.R1InnerCellsScored = R1InnerCellsScored
            self.R2InnerCellsScored = R2InnerCellsScored
            self.R3InnerCellsScored = R3InnerCellsScored
            self.B1InnerCellsScored = B1InnerCellsScored
            self.B2InnerCellsScored = B2InnerCellsScored
            self.B3InnerCellsScored = B3InnerCellsScored

            self.R1UpperCellsScored = R1UpperCellsScored
            self.R2UpperCellsScored = R2UpperCellsScored
            self.R3UpperCellsScored = R3UpperCellsScored
            self.B1UpperCellsScored = B1UpperCellsScored
            self.B2UpperCellsScored = B2UpperCellsScored
            self.B3UpperCellsScored = B3UpperCellsScored

            self.R1LowerCellsScored = R1LowerCellsScored
            self.R2LowerCellsScored = R2LowerCellsScored
            self.R3LowerCellsScored = R3LowerCellsScored
            self.B1LowerCellsScored = B1LowerCellsScored
            self.B2LowerCellsScored = B2LowerCellsScored
            self.B3LowerCellsScored = B3LowerCellsScored

            self.R1LeftAutoLine = R1LeftAutoLine
            self.R2LeftAutoLine = R2LeftAutoLine
            self.R3LeftAutoLine = R3LeftAutoLine
            self.B1LeftAutoLine = B1LeftAutoLine
            self.B2LeftAutoLine = B2LeftAutoLine
            self.B3LeftAutoLine = B3LeftAutoLine

            self.R1Defense = R1Defense
            self.R2Defense = R2Defense
            self.R3Defense = R3Defense
            self.B1Defense = B1Defense
            self.B2Defense = B2Defense
            self.B3Defense = B3Defense

            self.R1Trench = R1Trench
            self.R2Trench = R2Trench
            self.R3Trench = R3Trench
            self.B1Trench = B1Trench
            self.B2Trench = B2Trench
            self.B3Trench = B3Trench

            self.R1ClimbAttempt = R1ClimbAttempt
            self.R2ClimbAttempt = R2ClimbAttempt
            self.R3ClimbAttempt = R3ClimbAttempt
            self.B1ClimbAttempt = B1ClimbAttempt
            self.B2ClimbAttempt = B2ClimbAttempt
            self.B3ClimbAttempt = B3ClimbAttempt

            self.R1Climb = R1Climb
            self.R2Climb = R2Climb
            self.R3Climb = R3Climb
            self.B1Climb = B1Climb
            self.B2Climb = B2Climb
            self.B3Climb = B3Climb

            self.R1BuddyClimbAttempt = R1BuddyClimbAttempt
            self.R2BuddyClimbAttempt = R2BuddyClimbAttempt
            self.R3BuddyClimbAttempt = R3BuddyClimbAttempt
            self.B1BuddyClimbAttempt = B1BuddyClimbAttempt
            self.B2BuddyClimbAttempt = B2BuddyClimbAttempt
            self.B3BuddyClimbAttempt = B3BuddyClimbAttempt

            self.R1BuddyClimb = R1BuddyClimb
            self.R2BuddyClimb = R2BuddyClimb
            self.R3BuddyClimb = R3BuddyClimb
            self.B1BuddyClimb = B1BuddyClimb
            self.B2BuddyClimb = B2BuddyClimb
            self.B3BuddyClimb = B3BuddyClimb

            self.R1ParkedEG = R1ParkedEG
            self.R2ParkedEG = R2ParkedEG
            self.R3ParkedEG = R3ParkedEG
            self.B1ParkedEG = B1ParkedEG
            self.B2ParkedEG = B2ParkedEG
            self.B3ParkedEG = B3ParkedEG

            self.R1SpunCP = R1SpunCP
            self.R2SpunCP = R2SpunCP
            self.R3SpunCP = R3SpunCP
            self.B1SpunCP = B1SpunCP
            self.B2SpunCP = B2SpunCP
            self.B3SpunCP = B3SpunCP

            self.R1SetCPAttempt = R1SetCPAttempt
            self.R2SetCPAttempt = R2SetCPAttempt
            self.R3SetCPAttempt = R3SetCPAttempt
            self.B1SetCPAttempt = B1SetCPAttempt
            self.B2SetCPAttempt = B2SetCPAttempt
            self.B3SetCPAttempt = B3SetCPAttempt

            self.R1SetCP = R1SetCP
            self.R2SetCP = R2SetCP
            self.R3SetCP = R3SetCP
            self.B1SetCP = B1SetCP
            self.B2SetCP = B2SetCP
            self.B3SetCP = B3SetCP

            self.R1SetCPColorAttempt = R1SetCPColorAttempt
            self.R2SetCPColorAttempt = R2SetCPColorAttempt
            self.R3SetCPColorAttempt = R3SetCPColorAttempt
            self.B1SetCPColorAttempt = B1SetCPColorAttempt
            self.B2SetCPColorAttempt = B2SetCPColorAttempt
            self.B3SetCPColorAttempt = B3SetCPColorAttempt

            self.R1SetCPColor = R1SetCPColor
            self.R2SetCPColor = R2SetCPColor
            self.R3SetCPColor = R3SetCPColor
            self.B1SetCPColor = B1SetCPColor
            self.B2SetCPColor = B2SetCPColor
            self.B3SetCPColor = B3SetCPColor

            self.R1GroundIntake = R1GroundIntake
            self.R2GroundIntake = R2GroundIntake
            self.R3GroundIntake = R3GroundIntake
            self.B1GroundIntake = B1GroundIntake
            self.B2GroundIntake = B2GroundIntake
            self.B3GroundIntake = B3GroundIntake

            self.R1Disabled = R1Disabled
            self.R2Disabled = R2Disabled
            self.R3Disabled = R3Disabled
            self.B1Disabled = B1Disabled
            self.B2Disabled = B2Disabled
            self.B3Disabled = B3Disabled

            self.R1Brownout = R1Brownout
            self.R2Brownout = R2Brownout
            self.R3Brownout = R3Brownout
            self.B1Brownout = B1Brownout
            self.B2Brownout = B2Brownout
            self.B3Brownout = B3Brownout
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


@app.route('/getTeam', subdomain='scouting', methods=['GET'])
def getTeam():
    teamID = request.args.get('id')
    item = Teams.query.get(teamID)
    if item:
        team = {'teamNumber': item.teamNumber, 'teamName': item.teamName, 'teamlocation': item.teamlocation,
                'teamLogo': item.teamLogo.decode()}
        return team
    return '0 team not on server'


@app.route('/inputEvent', subdomain='scouting', methods=['POST'])
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


@app.route('/searchEventID', subdomain='scouting', methods=["GET"])
def searchEventID():
    parameters = request.args

    name = parameters.get('eventName') or ''
    date = parameters.get('eventDate') or ''

    if name == '':
        return '0 you need a name'

    if Events.query.filter(Events.eventName.like(Events.eventName + "%")).count() < 1:
        return '0 no event found'

    event = Events.query.filter(Events.eventName.like(Events.eventName + "%")).order_by(Events.eventDate.desc()).all()
    if date != '':
        event = Events.query.filter(Events.eventName.like(Events.eventName + "%"), Events.eventDate == date).all()
    return str(event[0].id)


@app.route('/getEvent', subdomain='scouting', methods=['GET'])
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


@app.route('/inputRobot', subdomain='scouting', methods=["POST"])
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


@app.route('/getRobot', subdomain='scouting', methods=['GET'])
def getRobot():
    robotID = request.args.get('id')
    item = Robots.query.get(robotID)

    if item:
        robot = {'teamID': item.teamID, 'seasonID': item.seasonID, 'eventID': item.eventID,
                 'driveBase': item.driveBase, 'isReliable': item.isReliable, 'climbPercent': item.climbPercent}
        return robot
    return '0 robot not on server'


@app.route('/searchRobotID', subdomain='scouting', methods=["GET"])
def searchRobotID():
    parameters = request.args

    teamID = int(parameters.get('teamID') or -1)
    eventID = int(parameters.get('eventID') or -1)

    if teamID == -1 or eventID == -1:
        return '0 you need a team ID and an event ID'

    robot = db.session.query(Robots).filter(Robots.teamID == teamID, Robots.eventID == eventID)
    if db.session.query(Robots).filter(Robots.teamID == teamID, Robots.eventID == eventID).count() < 1:
        return '0 no robot found'
    return str(robot[0].id)


@app.route('/inputGame', methods=["POST"])
def inputGame():
    # There is no way to edit a game, if you must, delete the game and re add it
    parameters = request.args

    eventID = parameters.get('eventID') or -1
    matchID = parameters.get('matchID') or -1

    blueScore = parameters.get('blueScore') or -1
    B1robotID = parameters.get('B1robotID') or -1
    B2robotID = parameters.get('B2robotID') or -1
    B3robotID = parameters.get('B3robotID') or -1

    redScore = parameters.get('redScore') or -1
    R1robotID = parameters.get('R1robotID') or -1
    R2robotID = parameters.get('R2robotID') or -1
    R3robotID = parameters.get('R3robotID') or -1

###START_OF_AUTOINPUT###
    R1InnerCellsScored = parameters.get('R1InnerCellsScored') or -1
    R2InnerCellsScored = parameters.get('R2InnerCellsScored') or -1
    R3InnerCellsScored = parameters.get('R3InnerCellsScored') or -1
    B1InnerCellsScored = parameters.get('B1InnerCellsScored') or -1
    B2InnerCellsScored = parameters.get('B2InnerCellsScored') or -1
    B3InnerCellsScored = parameters.get('B3InnerCellsScored') or -1

    R1UpperCellsScored = parameters.get('R1UpperCellsScored') or -1
    R2UpperCellsScored = parameters.get('R2UpperCellsScored') or -1
    R3UpperCellsScored = parameters.get('R3UpperCellsScored') or -1
    B1UpperCellsScored = parameters.get('B1UpperCellsScored') or -1
    B2UpperCellsScored = parameters.get('B2UpperCellsScored') or -1
    B3UpperCellsScored = parameters.get('B3UpperCellsScored') or -1

    R1LowerCellsScored = parameters.get('R1LowerCellsScored') or -1
    R2LowerCellsScored = parameters.get('R2LowerCellsScored') or -1
    R3LowerCellsScored = parameters.get('R3LowerCellsScored') or -1
    B1LowerCellsScored = parameters.get('B1LowerCellsScored') or -1
    B2LowerCellsScored = parameters.get('B2LowerCellsScored') or -1
    B3LowerCellsScored = parameters.get('B3LowerCellsScored') or -1

    R1LeftAutoLine = parameters.get('R1LeftAutoLine') or False
    R2LeftAutoLine = parameters.get('R2LeftAutoLine') or False
    R3LeftAutoLine = parameters.get('R3LeftAutoLine') or False
    B1LeftAutoLine = parameters.get('B1LeftAutoLine') or False
    B2LeftAutoLine = parameters.get('B2LeftAutoLine') or False
    B3LeftAutoLine = parameters.get('B3LeftAutoLine') or False

    R1Defense = parameters.get('R1Defense') or False
    R2Defense = parameters.get('R2Defense') or False
    R3Defense = parameters.get('R3Defense') or False
    B1Defense = parameters.get('B1Defense') or False
    B2Defense = parameters.get('B2Defense') or False
    B3Defense = parameters.get('B3Defense') or False

    R1Trench = parameters.get('R1Trench') or False
    R2Trench = parameters.get('R2Trench') or False
    R3Trench = parameters.get('R3Trench') or False
    B1Trench = parameters.get('B1Trench') or False
    B2Trench = parameters.get('B2Trench') or False
    B3Trench = parameters.get('B3Trench') or False

    R1ClimbAttempt = parameters.get('R1ClimbAttempt') or False
    R2ClimbAttempt = parameters.get('R2ClimbAttempt') or False
    R3ClimbAttempt = parameters.get('R3ClimbAttempt') or False
    B1ClimbAttempt = parameters.get('B1ClimbAttempt') or False
    B2ClimbAttempt = parameters.get('B2ClimbAttempt') or False
    B3ClimbAttempt = parameters.get('B3ClimbAttempt') or False

    R1Climb = parameters.get('R1Climb') or False
    R2Climb = parameters.get('R2Climb') or False
    R3Climb = parameters.get('R3Climb') or False
    B1Climb = parameters.get('B1Climb') or False
    B2Climb = parameters.get('B2Climb') or False
    B3Climb = parameters.get('B3Climb') or False

    R1BuddyClimbAttempt = parameters.get('R1BuddyClimbAttempt') or False
    R2BuddyClimbAttempt = parameters.get('R2BuddyClimbAttempt') or False
    R3BuddyClimbAttempt = parameters.get('R3BuddyClimbAttempt') or False
    B1BuddyClimbAttempt = parameters.get('B1BuddyClimbAttempt') or False
    B2BuddyClimbAttempt = parameters.get('B2BuddyClimbAttempt') or False
    B3BuddyClimbAttempt = parameters.get('B3BuddyClimbAttempt') or False

    R1BuddyClimb = parameters.get('R1BuddyClimb') or False
    R2BuddyClimb = parameters.get('R2BuddyClimb') or False
    R3BuddyClimb = parameters.get('R3BuddyClimb') or False
    B1BuddyClimb = parameters.get('B1BuddyClimb') or False
    B2BuddyClimb = parameters.get('B2BuddyClimb') or False
    B3BuddyClimb = parameters.get('B3BuddyClimb') or False

    R1ParkedEG = parameters.get('R1ParkedEG') or False
    R2ParkedEG = parameters.get('R2ParkedEG') or False
    R3ParkedEG = parameters.get('R3ParkedEG') or False
    B1ParkedEG = parameters.get('B1ParkedEG') or False
    B2ParkedEG = parameters.get('B2ParkedEG') or False
    B3ParkedEG = parameters.get('B3ParkedEG') or False

    R1SpunCP = parameters.get('R1SpunCP') or False
    R2SpunCP = parameters.get('R2SpunCP') or False
    R3SpunCP = parameters.get('R3SpunCP') or False
    B1SpunCP = parameters.get('B1SpunCP') or False
    B2SpunCP = parameters.get('B2SpunCP') or False
    B3SpunCP = parameters.get('B3SpunCP') or False

    R1SetCPAttempt = parameters.get('R1SetCPAttempt') or False
    R2SetCPAttempt = parameters.get('R2SetCPAttempt') or False
    R3SetCPAttempt = parameters.get('R3SetCPAttempt') or False
    B1SetCPAttempt = parameters.get('B1SetCPAttempt') or False
    B2SetCPAttempt = parameters.get('B2SetCPAttempt') or False
    B3SetCPAttempt = parameters.get('B3SetCPAttempt') or False

    R1SetCP = parameters.get('R1SetCP') or False
    R2SetCP = parameters.get('R2SetCP') or False
    R3SetCP = parameters.get('R3SetCP') or False
    B1SetCP = parameters.get('B1SetCP') or False
    B2SetCP = parameters.get('B2SetCP') or False
    B3SetCP = parameters.get('B3SetCP') or False

    R1SetCPColorAttempt = parameters.get('R1SetCPColorAttempt') or False
    R2SetCPColorAttempt = parameters.get('R2SetCPColorAttempt') or False
    R3SetCPColorAttempt = parameters.get('R3SetCPColorAttempt') or False
    B1SetCPColorAttempt = parameters.get('B1SetCPColorAttempt') or False
    B2SetCPColorAttempt = parameters.get('B2SetCPColorAttempt') or False
    B3SetCPColorAttempt = parameters.get('B3SetCPColorAttempt') or False

    R1SetCPColor = parameters.get('R1SetCPColor') or False
    R2SetCPColor = parameters.get('R2SetCPColor') or False
    R3SetCPColor = parameters.get('R3SetCPColor') or False
    B1SetCPColor = parameters.get('B1SetCPColor') or False
    B2SetCPColor = parameters.get('B2SetCPColor') or False
    B3SetCPColor = parameters.get('B3SetCPColor') or False

    R1GroundIntake = parameters.get('R1GroundIntake') or False
    R2GroundIntake = parameters.get('R2GroundIntake') or False
    R3GroundIntake = parameters.get('R3GroundIntake') or False
    B1GroundIntake = parameters.get('B1GroundIntake') or False
    B2GroundIntake = parameters.get('B2GroundIntake') or False
    B3GroundIntake = parameters.get('B3GroundIntake') or False

    R1Disabled = parameters.get('R1Disabled') or False
    R2Disabled = parameters.get('R2Disabled') or False
    R3Disabled = parameters.get('R3Disabled') or False
    B1Disabled = parameters.get('B1Disabled') or False
    B2Disabled = parameters.get('B2Disabled') or False
    B3Disabled = parameters.get('B3Disabled') or False

    R1Brownout = parameters.get('R1Brownout') or False
    R2Brownout = parameters.get('R2Brownout') or False
    R3Brownout = parameters.get('R3Brownout') or False
    B1Brownout = parameters.get('B1Brownout') or False
    B2Brownout = parameters.get('B2Brownout') or False
    B3Brownout = parameters.get('B3Brownout') or False
    ###END_OF_AUTOINPUT###




    if db.session.query(Robots).filter(Robots.id == R1robotID).count() == 0:
        return '0 Error, R1 robot not in database, please create this first'
    if db.session.query(Robots).filter(Robots.id == R2robotID).count() == 0:
        return '0 Error, R2 robot not in database, please create this first'
    if db.session.query(Robots).filter(Robots.id == R3robotID).count() == 0:
        return '0 Error, R3 robot not in database, please create this first'

    if db.session.query(Robots).filter(Robots.id == B1robotID).count() == 0:
        return '0 Error, B1 robot not in database, please create this first'
    if db.session.query(Robots).filter(Robots.id == B2robotID).count() == 0:
        return '0 Error, B2 robot not in database, please create this first'
    if db.session.query(Robots).filter(Robots.id == B3robotID).count() == 0:
        return '0 Error, B3 robot not in database, please create this first'

    data = Games(eventID,matchID, blueScore, B1robotID, B2robotID, B3robotID, redScore, R1robotID, R2robotID, R3robotID
###START_OF_AUTOPASS###
, R1InnerCellsScored, R2InnerCellsScored, R3InnerCellsScored, B1InnerCellsScored, B2InnerCellsScored, B3InnerCellsScored
, R1UpperCellsScored, R2UpperCellsScored, R3UpperCellsScored, B1UpperCellsScored, B2UpperCellsScored, B3UpperCellsScored
, R1LowerCellsScored, R2LowerCellsScored, R3LowerCellsScored, B1LowerCellsScored, B2LowerCellsScored, B3LowerCellsScored
, R1LeftAutoLine, R2LeftAutoLine, R3LeftAutoLine, B1LeftAutoLine, B2LeftAutoLine, B3LeftAutoLine
, R1Defense, R2Defense, R3Defense, B1Defense, B2Defense, B3Defense
, R1Trench, R2Trench, R3Trench, B1Trench, B2Trench, B3Trench
, R1ClimbAttempt, R2ClimbAttempt, R3ClimbAttempt, B1ClimbAttempt, B2ClimbAttempt, B3ClimbAttempt
, R1Climb, R2Climb, R3Climb, B1Climb, B2Climb, B3Climb
, R1BuddyClimbAttempt, R2BuddyClimbAttempt, R3BuddyClimbAttempt, B1BuddyClimbAttempt, B2BuddyClimbAttempt, B3BuddyClimbAttempt
, R1BuddyClimb, R2BuddyClimb, R3BuddyClimb, B1BuddyClimb, B2BuddyClimb, B3BuddyClimb
, R1ParkedEG, R2ParkedEG, R3ParkedEG, B1ParkedEG, B2ParkedEG, B3ParkedEG
, R1SpunCP, R2SpunCP, R3SpunCP, B1SpunCP, B2SpunCP, B3SpunCP
, R1SetCPAttempt, R2SetCPAttempt, R3SetCPAttempt, B1SetCPAttempt, B2SetCPAttempt, B3SetCPAttempt
, R1SetCP, R2SetCP, R3SetCP, B1SetCP, B2SetCP, B3SetCP
, R1SetCPColorAttempt, R2SetCPColorAttempt, R3SetCPColorAttempt, B1SetCPColorAttempt, B2SetCPColorAttempt, B3SetCPColorAttempt
, R1SetCPColor, R2SetCPColor, R3SetCPColor, B1SetCPColor, B2SetCPColor, B3SetCPColor
, R1GroundIntake, R2GroundIntake, R3GroundIntake, B1GroundIntake, B2GroundIntake, B3GroundIntake
, R1Disabled, R2Disabled, R3Disabled, B1Disabled, B2Disabled, B3Disabled
, R1Brownout, R2Brownout, R3Brownout, B1Brownout, B2Brownout, B3Brownout

###END_OF_AUTOPASS###
                 )
    db.session.add(data)
    db.session.commit()
    return '1 game added'


if __name__ == '__main__':
    app.run()

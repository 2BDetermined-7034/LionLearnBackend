"""
This is a crackhead's solution for the database problem
copy and paste the results into the class
"""
import json

f = open('game.json')

extra = json.load(f)

def getAlt(type):
    if type == "Boolean":
        return 'False'
    elif type == "Integer":
        return "-1"
    else:
        return "-1"

# Function will remove data so we can write to it
def reset(data):
    writing = True
    newData = []
    for x in range(0, len(data)):
        if "###START_OF_AUTOGAMESCLASS###" in data[x]:
            writing = False
            newData.append("###START_OF_AUTOGAMESCLASS###")
        elif "##START_OF_AUTOGAMESINIT###" in data[x]:
            writing = False
            newData.append("###START_OF_AUTOGAMESINIT###")
        elif "###START_OF_AUTOGAMESPROP###" in data[x]:
            writing = False
            newData.append("###START_OF_AUTOGAMESPROP###")

        elif "###START_OF_AUTOINPUT###" in data[x]:
            writing = False
            newData.append("###START_OF_AUTOINPUT###")
        elif "###START_OF_AUTOPASS###" in data[x]:
            writing = False
            newData.append("###START_OF_AUTOPASS###")


        #END

        elif "###END_OF_AUTOGAMESCLASS###" in data[x]:
            writing = True
        elif "###END_OF_AUTOGAMESINIT###" in data[x]:
            writing = True
        elif "###END_OF_AUTOGAMESPROP###" in data[x]:
            writing = True
        elif "###END_OF_AUTOINPUT###" in data[x]:
            writing = True
        elif "###END_OF_AUTOPASS###" in data[x]:
            writing = True

        if writing:
            newData.append(data[x])

    return newData


def returnDB():
    arr = []
    for x in extra.keys():
        #   Red
        for r in range(1, 4):
            arr.append("\n        R" + str(r) + x + " = " + "db.Column(db." + extra[x]["type"] + ")")

        for b in range(1, 4):
            arr.append("\n        B" + str(b) + x + " = " + "db.Column(db." + extra[x]["type"] + ")")
        arr.append("\n")
    return arr


def returnInit():
    string = "\n"
    for x in extra.keys():
        for r in range(1, 4):
            string += ", R" + str(r) + x

        for b in range(1, 4):
            string += ", B" + str(b) + x
        string += "\n"
    string += "\n"
    return string


def returnProps():
    arr = []
    for x in extra.keys():
        #   Red
        for r in range(1, 4):
            arr.append("\n" + "            self.R" + str(r) + x + " = R" + str(r) + x)

        for b in range(1, 4):
            arr.append("\n" + "            self.B" + str(b) + x + " = B" + str(b) + x)

        arr.append("\n")
    return arr


def returnGET():
    ret = []
    for x in extra.keys():
        #   Red
        for r in range(1, 4):
            ret.append("\n" + "    R" + str(r) + x + " = parameters.get('R" + str(r) + x + "') or " + getAlt(extra[x]['type']))

        for b in range(1, 4):
            ret.append("\n" + "    B" + str(b) + x + " = parameters.get('B" + str(b) + x + "') or " + getAlt(extra[x]['type']))

        ret.append("\n")
    return ret


def returnParams():
    string = "\n"
    for x in extra.keys():
        for r in range(1, 4):
            string += ", R" + str(r) + x
        for b in range(1, 4):
            string += ", B" + str(b) + x
        string +="\n"
    string += "\n"
    return string


def editAuto(data):
    classData = returnDB()
    params = returnInit()
    propData = returnProps()
    autoGetData = returnGET()
    apiParams = returnParams()
    atBottom = False

    x = 0
    while not atBottom:
        if "###START_OF_AUTOGAMESCLASS###" in data[x]:

            for i in range((len(classData) - 1), -1, -1):
                data.insert(x + 1, classData[i])
        if "###START_OF_AUTOGAMESINIT###" in data[x]:

            data.insert(x + 1, params)
        if "###START_OF_AUTOGAMESPROP###" in data[x]:

            for i in range((len(propData) - 1), -1, -1):
                data.insert(x + 1, propData[i])

        if "###START_OF_AUTOINPUT###" in data[x]:
            for i in range((len(autoGetData) - 1), -1, -1):
                data.insert(x + 1, autoGetData[i])

        if "###START_OF_AUTOPASS###" in data[x]:
            for i in range((len(apiParams) - 1), -1, -1):
                data.insert(x + 1, apiParams[i])


        if "app.run()" in data[x]:
            atBottom = True
        x += 1

    print(str(len(data)) + " lines edited")
    return data


def runEdit():
    with open('app.py', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
        data = reset(data)
        newD = editAuto(data)
        file = open('app.py', 'w')
        file.writelines("%s" % i for i in newD)


def runDB():
    from app import Games
    from app import db

    Games.__table__.drop(db.engine)
    db.create_all()


def main():
    print("Welcome to the stupid solution wizard")
    print("Please select an option")
    print("1 | Auto edit from JSON")
    print("2 | Update database from JSON")
    print('3 | Both 1 and 2')
    inp = input()
    if inp == "1":
        runEdit()
    if inp == "2":
        runDB()
    if inp == "3":
        runEdit()
        runDB()


if __name__ == "__main__":
    main()

"""
This is a crackhead's solution for the database problem
copy and paste the results into the class
"""
import json

f = open('extra.json')

extra = json.load(f)


# Function will remove data so we can write to it
def reset(data):
    writing = True
    newData = []
    for x in range(0, len(data)):
        if "###START_OF_AUTOGAMESCLASS###" in data[x]:
            writing = False
            newData.append("###START_OF_AUTOGAMESCLASS###")
        elif "###START_OF_AUTOGAMESINIT###" in data[x]:
            writing = False
            newData.append("###START_OF_AUTOGAMESINIT###")
        elif "###START_OF_AUTOGAMESPROP###" in data[x]:
            writing = False
            newData.append("###START_OF_AUTOGAMESPROP###")

        elif "###START_OF_AUTOFORMGET###" in data[x]:
            writing = False
            newData.append("###START_OF_AUTOFORMGET###")

        elif "###END_OF_AUTOGAMESCLASS###" in data[x]:
            writing = True
        elif "###END_OF_AUTOGAMESINIT###" in data[x]:
            writing = True
        elif "###END_OF_AUTOGAMESPROP###" in data[x]:
            writing = True
        elif "###END_OF_AUTOFORMGET###" in data[x]:
            writing = True

        if writing:
            newData.append(data[x])
    return newData


def returnDB():
    arr = []
    for x in extra.keys():
        #   Red
        for r in range(1, 4):
            arr.append("\n      R" + str(r) + x + " = " + "db.Column(db.Integer)")

        for b in range(1, 4):
            arr.append("\n      B" + str(b) + x + " = " + "db.Column(db.Integer)")
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
            ret.append("\n          R" + str(r) + x + " = " + "tryGet('R" + str(r) + x + "', -1)")

        for b in range(1, 4):
            ret.append("\n          B" + str(b) + x + " = " + "tryGet('B" + str(b) + x + "', -1)")
    ret.append("\n")

    return ret


def editAuto(data):
    print(len(data))
    for x in range(0, len(data)):
        if "###START_OF_AUTOGAMESCLASS###" in data[x]:
            newData = returnDB()
            for i in range((len(newData) - 1), -1, -1):
                data.insert(x + 1, newData[i])
        if "###START_OF_AUTOGAMESINIT###" in data[x]:
            params = returnInit()
            data.insert(x + 1, params)
        if "###START_OF_AUTOGAMESPROP###" in data[x]:
            newData = returnProps()
            for i in range((len(newData) - 1), -1, -1):
                data.insert(x + 1, newData[i])
        if "###START_OF_AUTOFORMGET###" in data[x]:
            autoGetData = returnGET()
            print(autoGetData)
            for i in range((len(autoGetData) - 1), -1, -1):
                data.insert(x + 1, autoGetData[i])

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
    print('e')


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

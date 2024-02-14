import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("../service-account.json")
firebase_admin.initialize_app(cred)

# Fetching Data
db = firestore.client()

def getDocs(collection):
    docs = (
        db.collection(collection)
        .stream()
    )

    # Iterating over documents
    docList = []
    for doc in docs:
        data = doc.to_dict()
        #data["id"] = doc.id
        data["docData"] = doc._data
        #print(doc._data)
        docList.append(doc._data)

    print("Compiling analytical information...")
    optimizeInfo(docList)


# Utility
    
genres = {}
developers = {}
platforms = {}

def optimizeInfo(data):
    importantKeys = ["developer", "genre", "platform"]

    for dicts in data:
        for key, value in dicts.items():
            if (key in importantKeys):
                if (key == importantKeys[2]):
                    addorIncrementDict(value, platforms)
                elif (key == importantKeys[1]):
                    multiHandling(value, genres)
                elif (key == importantKeys[0]):
                    multiHandling(value, developers)

def addorIncrementDict(key, dictionary):
    if (key in dictionary):
        dictionary[key] += 1
    else:
        dictionary[key] = 1

def multiHandling(key, dictionary):
    if (',' in key):
        """If input is a list of multiple items"""
        multi = key.split(', ')
        for item in multi:
            addorIncrementDict(item, dictionary)
    else:
        addorIncrementDict(key, dictionary)

# For later visualizations
def setXAxis(dictionary):
    x_axis = []
    for key, value in dictionary.items():
        x_axis.append(key)
    return x_axis

def setYAxis(dictionary):
    y_axis = []
    for key, value in dictionary.items():
        y_axis.append(value)
    return y_axis


# User Inputs
print("Which data set would you like to see?")
print("    A: SeanVGO Admin User")
print("    B: SeanVGO Demo User\n")
counter = 0

while True:
    x = input("Please Enter A or B: ")

    if (x == 'a' or x == 'A'):
        print("You chose \'SeanVGO Admin User\'")
        collName = "games-list"
        break
    elif (x == 'b' or x == 'B'):
        print("You chose \'SeanVGO Demo User\'")
        #print(x)
        collName = "user-game-list"
        break
    else:
        """If not A or B is input"""
        counter += 1
        if (counter < 5):
            print(f"Invalid Input {5 - counter} attempts remaining.")
            continue
        else:
            counter = 0
            print("Program Terminated: Too Many Incorrect Inputs")
            break

#print(collName)
print(f"Fetching data from \'{collName}\'...")
getDocs(collName)


# Data Study
genreX = setXAxis(genres)
genreY = setYAxis(genres)
devsX = setXAxis(developers)
devsY = setYAxis(developers)
platsX = setXAxis(platforms)
platsY = setYAxis(platforms)

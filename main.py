import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import matplotlib.pyplot as plt

cred = credentials.Certificate("./service-account.json")
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
platforms = {}

def optimizeInfo(data):
    importantKeys = ["genre", "platform"]

    for dicts in data:
        for key, value in dicts.items():
            if (key in importantKeys):
                if (key == importantKeys[2]):
                    addorIncrementDict(value, platforms)
                elif (key == importantKeys[1]):
                    multiHandling(value, genres)

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

# Make Plots
def makePlots(x_data, y_data, y_label, filename):
    # Spacing
    plt.figure(figsize=(23, 22))
    plt.subplots_adjust(top=0.95)

    # The Actual Plot
    plt.bar(x_data, y_data)
    plt.ylabel(y_label, fontsize=18, labelpad=20)

    plt.xticks(rotation=47, ha='right', fontsize=16)
    plt.yticks(fontsize=16)

    # To Image
    savePlots(filename)

# Save the Plots as Images
def savePlots(filename):
    if (collName == "games-list"):
        plt.savefig(f"./graphs/admin-user/{filename}.png")
    elif (collName == "user-game-list"):
        plt.savefig(f"./graphs/test-user/{filename}.png")

# Data Study Function
def dataStudy():
    globYLabel = "Number of Games"
    # Genres
    genreX = setXAxis(genres)
    genreY = setYAxis(genres)
    makePlots(genreX, genreY, globYLabel, "genre-graph")

    # Platforms
    platsX = setXAxis(platforms)
    platsY = setYAxis(platforms)
    makePlots(platsX, platsY, globYLabel, "plats-graph")


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

print("Making Graphs...")
dataStudy()
print("All Processes Done!")

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import matplotlib.pyplot as plt

class SeanVGODataVisualizer:
    def __init__(self, serviceAccPath, collectionName):
        self.cred = credentials.Certificate(serviceAccPath)
        firebase_admin.initialize_app(self.cred)

        # Fetching Data
        self.db = firestore.client()
        self.collectionName = collectionName

        self.genres = {}
        self.platforms = {}

    def getDocs(self, collectionName):
        docs = (
            self.db.collection(collectionName)
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
        self.optimizeInfo(docList)

    # Utility
    def optimizeInfo(self, data):
        importantKeys = ["genre", "platform"]

        for dicts in data:
            for key, value in dicts.items():
                if (key in importantKeys):
                    if (key == importantKeys[1]):
                        self.addorIncrementDict(value, self.platforms)
                    elif (key == importantKeys[0]):
                        self.multiHandling(value, self.genres)

    def addorIncrementDict(self, key, dictionary):
        if (key in dictionary):
            dictionary[key] += 1
        else:
            dictionary[key] = 1

    def multiHandling(self, key, dictionary):
        if (',' in key):
            """If input is a list of multiple items"""
            multi = key.split(', ')
            for item in multi:
                self.addorIncrementDict(item, dictionary)
        else:
            self.addorIncrementDict(key, dictionary)

    # For later visualizations
    def setXAxis(self, dictionary):
        x_axis = [key for key in dictionary]
        return x_axis

    def setYAxis(self, dictionary):
        y_axis = [value for value in dictionary]
        return y_axis

    # Make Plots
    def makePlots(self, x_data, y_data, y_label, filename):
        # Spacing
        plt.figure(figsize=(23, 22))
        plt.subplots_adjust(top=0.95)

        # The Actual Plot
        plt.bar(x_data, y_data)
        plt.ylabel(y_label, fontsize=18, labelpad=20)

        plt.xticks(rotation=47, ha='right', fontsize=16)
        plt.yticks(fontsize=16)

        # To Image
        self.savePlots(filename)

    # Save the Plots as Images
    def savePlots(self, filename):
        if (self.collectionName == "games-list"):
            plt.savefig(f"./graphs/admin-user/{filename}.png")
        elif (self.collectionName == "user-game-list"):
            plt.savefig(f"./graphs/test-user/{filename}.png")

    # Data Study Function
    def dataStudy(self):
        globYLabel = "Number of Games"
        # Genres
        genreX = self.setXAxis(self.genres)
        genreY = self.setYAxis(self.genres)
        self.makePlots(genreX, genreY, globYLabel, "genre-graph")

        # Platforms
        platsX = self.setXAxis(self.platforms)
        platsY = self.setYAxis(self.platforms)
        self.makePlots(platsX, platsY, globYLabel, "plats-graph")


if __name__ == "__main__":
    # User Inputs
    print("Which data set would you like to see?")
    print("    A: SeanVGO Admin User")
    print("    B: SeanVGO Demo User\n")
    counter = 0

    while True:
        userInput = input("Please Enter A or B: ")

        if userInput in 'AaBb':
            break
        else:
            counter += 1
            if (counter < 5):
                print(f"Invalid Input {5 - counter} attempts remaining.")
                continue
            else:
                counter = 0
                print("Program Terminated: Too Many Incorrect Inputs")
                exit(1)

    collectionName = "games-list" if userInput in 'Aa' else "user-game-list"
    visualizer = SeanVGODataVisualizer("./service-account.json", collectionName)
    print(f"Fetching data from \'{collectionName}\'...")
    visualizer.getDocs(collectionName)

    print("Making Graphs...")
    visualizer.dataStudy()
    print("All Processes Done!")

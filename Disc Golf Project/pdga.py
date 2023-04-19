import pickle


class Player:
    def __init__(self, name, score, division, PDGAnum):
        self.name = name
        self.score = score
        self.division = division
        self.PDGAnum = PDGAnum


class Course:
    def __init__(self, courseName, holePar, courseLocation, courseLenFt):
        self.course_name = courseName
        self.holePar = holePar
        self.courseLocation = courseLocation
        self.courseLenFt = courseLenFt

    def coursePar(self):
        return sum(self.holePar)


class CourseRound:
    def __init__(
        self,
        players,
        datePlayed,
        coursePlayed,
    ):
        self.players = players
        self.datePlayed = datePlayed
        self.coursePlayed = coursePlayed

    def scoreCalc(self):
        total_score = 0
        for player in self.players:
            total_score += player.score
        return total_score


class AddPlayer:
    def __init__(self):
        self.players = []

    def addPlayer(self):
        while addMore != 0:
            name = input("Enter player name: ")
            score = int(input("Enter player score: "))
            division = input("Enter player division: ")
            PDGAnum = int(input("Enter player PDGA number: "))
            newPlayer = Player(name, score, division, PDGAnum)
            self.players.append(newPlayer)
            addMore = int(input("Enter 1 to add another player or 0 if completed: "))


class AddCourse:
    def __init__(self):
        self.courses = []

    def addCourse(self):
        name = input("Enter course name: ")
        numHoles = int(input("Enter number of holes: "))
        parList = []
        for i in range(numHoles):
            holePar = int(input(f"Enter par for hole {i+1}: "))
            parList.append(holePar)
        location = input("Enter course location: ")
        length = int(input("Enter course length (in feet): "))
        newCourse = Course(name, parList, location, length)
        self.courses.append(newCourse)

    def getCourseNames(self):
        courseNames = []
        for course in self.courses:
            courseNames.append(course.courseName)
        return courseNames


class UpdateScores:
    def __init__(self, roundObj):
        self.roundObj = roundObj

    def updateScores(self):
        for player in self.roundObj.players:
            print(f"Enter scores for {player.name}:")
            scoreCard = []
            for i, score in enumerate(player.scoreCard):
                scoreInput = int(input(f"Hole {i+1}: "))
                scoreCard.append(scoreInput)
            player.setScoreCard(scoreCard)


class EndRound:
    def __init__(self, roundObj):
        self.roundObj = roundObj

    def endRound(self):
        self.roundObj.scoreCalc()
        print("Final scores:")
        for player in self.roundObj.players:
            print(f"{player.name}: {player.score}")


class SaveLoadData:
    def __init__(self, roundObj):
        self.roundObj = roundObj

    def saveData(self):
        fileName = input("Enter file name: ")
        with open(fileName, "w") as f:
            f.write(str(self.roundObj.__dict__))
        print("Round saved!")

    def loadData(self):
        fileName = input("Enter file name: ")
        with open(fileName, "r") as f:
            roundDict = eval(f.read())
            loadedRound = RoundClass(**roundDict)
        print("Round loaded!")
        return loadedRound

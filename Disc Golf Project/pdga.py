import pickle
import unittest

class Player:
    def __init__(self,name,score,division,PDGAnum):
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
    
# currentCourse = Course("Stable Run",[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,4], "Ames, Iowa", 6174)

# coursePar = currentCourse.coursePar()

# print("Course par is:", coursePar)

class CourseRound:
    def __init__(self,players,datePlayed,coursePlayed,): 
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
        with open(fileName, "wb") as f:
            pickle.dump(self.roundObj, f)
        print("Round saved!")

    def loadData(self):
        fileName = input("Enter file name: ")
        with open(fileName, "rb") as f:
            loadedRound = pickle.load(f)
        print("Round loaded!")
        return loadedRound


 # Start Test Cases

class TestCourse(unittest.TestCase):
    def testCoursePar(self):
        course = Course("Test Course", [3, 4, 5, 4], "Test Location", 7000)
        self.assertEqual(course.coursePar(), 16, "Course par should be 16")

    def testCourseParEmptyHoles(self):
            course = Course("Empty Course", [], "Test Location", 0)
            self.assertEqual(course.coursePar(), 0, "Course par should be 0 for an empty course")

    def testCourseParNegativeHoles(self):
        course = Course("Negative Course", [-3, 4, -5, 4], "Test Location", 7000)
        with self.assertRaises(ValueError):
            course.coursePar()

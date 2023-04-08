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
    
currentCourse = Course("Stable Run",[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,4], "Ames, Iowa", 6174)

coursePar = currentCourse.coursePar()

print("Course par is:", coursePar)

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

    def add_player(self):
        while addMore != 0:
            name = input("Enter player name: ")
            score = int(input("Enter player score: "))
            division = input("Enter player division: ")
            PDGAnum = int(input("Enter player PDGA number: "))
            new_player = Player(name, score, division, PDGAnum)
            self.players.append(new_player)
            addMore = int(input("Enter 1 to add another player or 0 if completed: "))



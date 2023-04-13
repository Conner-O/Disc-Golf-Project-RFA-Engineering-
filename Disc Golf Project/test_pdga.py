import unittest

class TestCourse(unittest.TestCase):
    def test_CoursePar(self):
        course = Course("Test Course", [3, 4, 5, 4], "Test Location", 7000)
        self.assertEqual(course.coursePar(), 16, "Course par should be 16")

    def test_CourseParEmptyHoles(self):
            course = Course("Empty Course", [], "Test Location", 0)
            self.assertEqual(course.coursePar(), 0, "Course par should be 0 for an empty course")

    def test_CourseParNegativeHoles(self):
        course = Course("Negative Course", [-3, 4, -5, 4], "Test Location", 7000)
        with self.assertRaises(ValueError):
            course.coursePar()

class TestAddPlayer(unittest.TestCase):
    def testAddPlayer(self):
        addPlayer = AddPlayer()
        addPlayer.addPlayer()
        self.assertEqual(len(addPlayer.players), 1)

class TestAddCourse(unittest.TestCase):
    def testAddCourse(self):
        addCourse = AddCourse()
        addCourse.addCourse()
        self.assertEqual(len(addCourse.courses), 1)

class TestUpdateScores(unittest.TestCase):
    def testUpdateScores(self):
        player = Player("John", 0, "MPO", 12345)
        course = Course("Test Course", [3, 4, 5], "Test Location", 10000)
        roundObj = CourseRound([player], "2022-01-01", course)
        updateScores = UpdateScores(roundObj)
        updateScores.updateScores()
        self.assertEqual(player.scoreCard, [1, 2, 3])

class TestEndRound(unittest.TestCase):
    def testEndRound(self):
        player = Player("John", 0, "MPO", 12345)
        course = Course("Test Course", [3, 4, 5], "Test Location", 10000)
        roundObj = CourseRound([player], "2022-01-01", course)
        endRound = EndRound(roundObj)
        endRound.endRound()
        self.assertEqual(player.score, 12)

class TestSaveLoadData(unittest.TestCase):
    def testSaveLoadData(self):
        player = Player("John", 0, "MPO", 12345)
        course = Course("Test Course", [3, 4, 5], "Test Location", 10000)
        roundObj = CourseRound([player], "2022-01-01", course)
        saveLoadData = SaveLoadData(roundObj)
        saveLoadData.saveData()
        loadedRoundObj = saveLoadData.loadData()
        self.assertEqual(roundObj.__dict__, loadedRoundObj.__dict__)

if __name__ == '__main__':
     unittest.main()

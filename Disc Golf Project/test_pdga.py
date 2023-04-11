import unittest

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

if __name__ == '__main__':
     unittest.main()
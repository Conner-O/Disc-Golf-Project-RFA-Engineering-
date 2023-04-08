# Create a class LanguageStudent with: property languages - 
# returns all languages, as a list, that the studetn knows. method add_language(language) 
# adds a new language to the list of languages. Create a class LnaguageTeacher that inherits language 
# student and has one additional public method:  teach (student, languageToLearn) - 
# if languageToLearn exists in the languages property of the LanguageTeacher, adds languageToLearn to the student's 
# languages and returns true; otherwise it returns false. For example the following cod shows how LangaugeTeacher teaches 
# langaugeStudent the new language ('English') teacher = LanguageTeacher() teacher.add_langauge('English') 
# student = LanguageStudent() teacher.teach(student, 'English') print(student.languages)


class LanguageStudent:
    def __init__(self):
        self._languages = []

    @property
    def languages(self):
        return self._languages

    def add_language(self, language):
        if language not in self._languages:
            self._languages.append(language)


class LanguageTeacher(LanguageStudent):
    def teach(self, student, language_to_learn):
        if language_to_learn in self.languages:
            student.add_language(language_to_learn)
            return True
        else:
            return False


# Example usage:
teacher = LanguageTeacher()
teacher.add_language('English')
student = LanguageStudent()
teacher.teach(student, 'English')
print(student.languages)

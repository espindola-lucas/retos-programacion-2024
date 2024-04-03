import unittest

class pruebasUnitarias(unittest.TestCase):
    def suma(self, num1, num2):
        self.assertEqual(type(num1), int)
        self.assertEqual(type(num2), int)
        return num1 + num2

test = pruebasUnitarias()
print(f"suma: {test.suma(5, 10)}")

# Dificultad extra
class testPersonalInformation(unittest.TestCase):
    def setUpInformation(self):
        personal_information = {
            "name": "Lucas Nahuel Espindola",
            "age": 25,
            "birth_date": "13/10/1998",
            "programming_languages": ["PHP", "Python", "Bash", "JavaScript"]
        }
        
        return personal_information

    def testThatNoneOfTheValuesInDictionary(self):
        personal_information = self.setUpInformation()
        for key in personal_information:
            self.assertIsNotNone(personal_information.get(key))
        return "Todos los campos existen"

    def testInformationIsExpected(self):
        personal_information = self.setUpInformation()
        name = personal_information.get('name')
        age = personal_information.get('age')
        birth_date = personal_information.get('birth_date')
        prog_lang = personal_information.get('programming_languages')
        
        self.assertEqual(type(name), str)
        self.assertEqual(type(age), int)
        self.assertEqual(type(prog_lang), list)
        self.assertEqual(type(birth_date), str)
        
        self.assertEqual(name, "Lucas Nahuel Espindola")
        self.assertEqual(age, 25)
        self.assertEqual(birth_date, "13/10/1998")
        self.assertEqual(prog_lang, ["PHP", "Python", "Bash", "JavaScript"])

        return "Los datos son los esperados"

test2 = testPersonalInformation()
print(test2.testThatNoneOfTheValuesInDictionary())
print(test2.testInformationIsExpected())
import re

class expresionesRegulares:
    def extractsNums(self, text):
        pattern = r'\d+'
        numbers = re.findall(pattern, text)
        for number in numbers:
            print(number)
        print("\n")

    # extra
    def validateEmail(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, email):
            print(f"El mail {email} es valido")
        else:
            print(f"El mail {email} no es valido")

    def validatePhoneNumbers(self, phone):
        pattern = r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}"
        if re.match(pattern, phone):
            print(f"El numero {phone} es valido")
        else:
            print(f"El numero {phone} no es valido")

    def validateUrl(self, url):
        pattern = r'^(http|https):\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
        if re.match(pattern, url):
            print(f"La url {url} es valida")
        else:
            print(f"La url {url} no es valida")
regular_expression = expresionesRegulares()
text = "Este es un texto con números como 123, 45.6, -7 y 1000."
print("Vamos a analizar el siguiente texto:")
print("'" + text + "'\n")
regular_expression.extractsNums(text)

# extra
print('Ejericio extra:')
regular_expression.validateEmail('correo@correo.com')
regular_expression.validateEmail('correo@correo')
regular_expression.validatePhoneNumbers("+34 123456789")
regular_expression.validatePhoneNumbers("55")
regular_expression.validateUrl('https://www.google.com/')
regular_expression.validateUrl('www.google.com')
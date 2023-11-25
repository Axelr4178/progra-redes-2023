"""
    Autor:Axel Alejandro Almaguer Rodriguez
    Descripcion: Problemas Python Institute
"""
def read_int(prompt, min, max):
    userInput = input(prompt)
    isUserInputValid = False
    while isUserInputValid == False:
        try:

            userInput = int(userInput)
            assert userInput > min and userInput < max
            isUserInputValid = True

        except ValueError:
            print("Error")
            userInput = input(prompt)

        except AssertionError:
            print("El valor no esta dentro del rango ")
            userInput = input(prompt)

    return str(userInput)

v = read_int("Ingresa un numero del -10 a 10: ", -10, 10)

print("El numero es:", v)
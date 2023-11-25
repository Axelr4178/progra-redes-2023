"""
    Autor:Axel Alejandro Almaguer Rodriguez
    Descripcion: Problemas Python Institute
"""
print()
userInput = input("Ingresa cualquier numero: ")


userInputString = str(userInput)

userInputLength = len(userInputString)

one = ["  #","  #","  #","  #","  #"]
two = ["###","  #","###","#  ","###"]
three = ["###","  #","###","  #","###"]
four = ["# #","# #","###","  #","  #"]
five = ["###","#  ","###","  #","###"]
six = ["###","#  ","###","# #","###"]
seven = ["###","  #","  #","  #","  #"]
eight = ["###","# #","###","# #","###"]
nine = ["###","# #","###","  #","  #"]
zero = ["###","# #","# #","# #","###"]

userInputList = []
for i in userInputString:
    if i == '1':
        userInputList.append(one)
    elif i == '2':
        userInputList.append(two)
    elif i == '3':
        userInputList.append(three)
    elif i == '4':
        userInputList.append(four)
    elif i == '5':
        userInputList.append(five)
    elif i == '6':
        userInputList.append(six)
    elif i == '7':
        userInputList.append(seven)
    elif i == '8':
        userInputList.append(eight)
    elif i == '9':
        userInputList.append(nine)
    elif i == '0':
        userInputList.append(zero)
lineOne = []
lineTwo = []
lineThree = []
lineFour = []
lineFive = []
digitsToPrint = userInputLength
j = 0
while j < digitsToPrint:
    lineOne.append(userInputList[j][0])
    j += 1
j = 0
while j < digitsToPrint:
    lineTwo.append(userInputList[j][1])
    j += 1
j = 0
while j < digitsToPrint:
    lineThree.append(userInputList[j][2])
    j += 1
j = 0
while j < digitsToPrint:
    lineFour.append(userInputList[j][3])
    j += 1
j = 0
while j < digitsToPrint:
    lineFive.append(userInputList[j][4])
    j += 1
print(" ".join(lineOne))
print(" ".join(lineTwo))
print(" ".join(lineThree))
print(" ".join(lineFour))
print(" ".join(lineFive))
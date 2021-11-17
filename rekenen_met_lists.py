list1 = '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'
list2 = '2', '4', '6', '8', '10', '12', '14', '16', '18', '20'

def addAndDisplayLists (list1, list2):
    for i in range(len(list1)):
        plus = int(list1[i]) + int(list2[i])
        antwoord = plus
        print(str(list1[i]) + '+', str(list2[i]), '=', str(antwoord))
        
addAndDisplayLists(list1, list2)


def substractAndDisplayLists (list1, list2):
    for i in range(len(list1)):
        plus = int(list1[i]) - int(list2[i])
        antwoord = plus
        print(str(list1[i]) + '-', str(list2[i]), '=', str(antwoord))

substractAndDisplayLists(list1, list2)

def multiplyAndDisplayList (list1, list2):
    for i in range(len(list1)):
        plus = int(list1[i]) * int(list2[i])
        antwoord = plus
        print(str(list1[i]) + '*', str(list2[i]), '=', str(antwoord))

multiplyAndDisplayList(list1, list2)


def multiplyAndDisplayList (list1, list2):
    for i in range(len(list1)):
        plus = int(list1[i]) / int(list2[i])
        antwoord = plus
        print(str(list1[i]) + '/', str(list2[i]), '=', str(antwoord))

multiplyAndDisplayList(list1, list2)




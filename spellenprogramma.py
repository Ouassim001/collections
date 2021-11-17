import random
spellist = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet','Cluedo']
minimum = ['0', '1', '2']
maximum = ['3', '4', '5', '6', '7', '8', '9', '10']


def spelProgramma(spellist):

    while True:
        kies = int(input("kies een nummer tussen 3 & 10\n"))
        spellist = set(spellist)
        print(random.sample(spellist, kies ))
        weer = input("wil je nog meer spellen kiezen  ja/nee\n")
        if weer == "ja":
            continue
        else:
            print("isgood")
            break


spelProgramma(spellist)
    
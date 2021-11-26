import random
kleuren = ['oranje', 'blauw', 'groen', 'bruin']
zakmm = []

aantal = int(input("hoeveel M&M'S wil je\n"))
aantalcolor = int(input("hoeveel kleuren wil je\n"))

random.shuffle(kleuren)
for x in range(aantal):


    index = random.randint(0, aantalcolor -1)
    zakmm.append(kleuren[index])

#print(zakmm)

zakmm = {}
zakmm[kleuren[0]] = 0
zakmm[kleuren[1]] = 0
zakmm[kleuren[2]] = 0
zakmm[kleuren[3]] = 0

for x in range(aantal):

    index = random.randint(0, aantalcolor -1)

    zakmm[kleuren[index]] += 1
    
for key, value in zakmm.items():
    print(key, value)



print(zakmm)


print ("Programma 2: Berekeningen uitvoeren\n")

gebruikersnaam = input("wat is uw naam?")


def plus (aantal,getal1,getal2):
    for i in range (aantal):
        print (f"{getal1} + {getal2} = {getal1+getal2}")
getal1 = int(input(f"{gebruikersnaam},voer een getal in\n"))
getal2 = int(input(f"{gebruikersnaam},voer een getal in\n"))

print ("-----------------------------------------")

def min (aantal,getal1,getal2):
    for i in range (aantal):
        print (f"{getal1} - {getal2} = {getal1-getal2}")

getal3 = int (input(f"{gebruikersnaam},voer een getal in\n"))
getal4 = int (input(f"{gebruikersnaam},voer een getal in\n"))

print ("-----------------------------------------")

def keer (aantal,getal1,getal2):
    for i in range (aantal):
        print (f"{getal1} * {getal2} = {getal1*getal2}")

getal5 = int (input(f"{gebruikersnaam},voer een getal in\n"))
getal6 = int (input(f"{gebruikersnaam},voer een getal in\n"))

print ("-----------------------------------------")

def delendoor (aantal,getal1,getal2):
    for i in range (aantal):
        print (f"{getal1} / {getal2} = {getal1/getal2}")

getal7 = int (input(f"{gebruikersnaam},voer een getal in\n"))
getal8 = int (input(f"{gebruikersnaam},voer een getal in\n"))

print ("-----------------------------------------")

def plustwee (aantal,getal1,getal2):
    for i in range (aantal):
        print (f"{getal1} + {getal2} = {getal1+getal2}")

getal9 = int (input(f"{gebruikersnaam},voer een getal in\n"))
getal10 = int (input(f"{gebruikersnaam},voer een getal in\n"))

print ("-----------------------------------------")

def mintwee (aantal,getal1,getal2):
    for i in range (aantal):
        print (f"{getal1} - {getal2} = {getal1-getal2}")

getal11 = int (input(f"{gebruikersnaam},voer een getal in?\n"))
getal12 = int (input(f"{gebruikersnaam},voer een getal in\n"))

print ("-----------------------------------------")

bestand=input(f"{gebruikersnaam},bent u klaar voor het resultaat?")
if bestand == "ja":
    plus(1,getal1,getal2)
    min(1,getal3,getal4)
    keer(1,getal5,getal6)
    delendoor(1,getal7,getal8)
    plustwee(1,getal9,getal10)
    mintwee(1,getal11,getal12)

    print ("-----------------------------------------")

    print (f"""{gebruikersnaam},we wish you a merry Christmas
We wish you a merry Christmas
We wish you a merry Christmas and a happy new year
Good tidings we bring to you and your kin
We wish you a merry Christmas and a happy new year!""")

else:
    print ("hierbij sluiten we dit programma af!")
    print (f"""{gebruikersnaam},we wish you a merry Christmas
We wish you a merry Christmas
We wish you a merry Christmas and a happy new year
Good tidings we bring to you and your kin
We wish you a merry Christmas and a happy new year!""")

print ("-----------------------------------------")

exit()

#code review:Stijn
#probeer zo min mogelijk globale variables aan te roepen vanaf functies
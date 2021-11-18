print ("Programma 3: Namen en leeftijden")
print ("Disclaimer:")
print ("Als u wilt stoppen typ dan op de vraag waar naar uw naam gevraagd wordt op stop!")
print ("Alvast bedankt!")

def naamvraag(naamvraag):
    naamvraag=input("wat is uw naam? ")
    if naamvraag == "stop":
        return naamvraag
    leefttijd=int(input("wat is uw leeftijd? "))
    print(f"hoi {naamvraag} je bent {leefttijd} oud.")

while True:
    if naamvraag(naamvraag) == "stop":
        print ("Bedankt voor het gebruiken van Milware!")
        break



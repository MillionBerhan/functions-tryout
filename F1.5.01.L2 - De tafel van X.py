def printTafel(tafelVan):
    for i in range(1, 11):
        print (f"{i} x {tafelVan} = {i*tafelVan}")

getalvraag = int(input("Van welk getal wilt u de tafel zien?"))

printTafel(getalvraag)
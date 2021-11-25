import webbrowser
getal1=0 #variabelen
getal2=1 #variabelen

def fabonaccireeks(getal1,getal2): #functions en parameters
    for i in range (1,aantalvraag+1): #for-loop
        getal2 = (getal1+getal2) 
        getal1 = (getal1+getal2)
        print (f"{getal2},", end="")
        print (f"{getal1},",end="")


aantalvraag = int(input("hoeveel keer wilt u het Fibonacci getal zien?"))
while getal1 and getal2 >1000: #while-loop
    print("u kunt niet meer verder")
    exit()

fabonaccireeks(getal1,getal2) # function en parameter wordt opgeroepen


dubbelfris = input("Vind u dubbelfris ook zo kanka lekkah?ja/nee")

if dubbelfris == 'ja' or 'Ja':
    print ("held van de dag")
    webbrowser.open('https://www.youtube.com/watch?v=IWwqQCr52Ps')  # Go to example.com

elif dubbelfris == 'Nee' or 'nee':
    print ("je mag griep krijgen en doneer een joet aan het kwf")   
    webbrowser.open('https://www.youtube.com/watch?v=C8AsSdaDyA4') # Go to example.com


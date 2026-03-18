from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    prijs_na_korting=prijs*(1-korting)
    uitvoer=(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro.")
    return uitvoer
print(aanbieding_1("aardbei",4,0.1))

def inkomsten_totaal(inkomsten,btw):
    totaal=sum(inkomsten)
    uitvoer=(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {totaal*btw} euro btw betaald dient te worden.")
    return uitvoer
print(inkomsten_totaal([220,430,125,160,205,90,345], 0.09))

def laag_en_hoog(mijn_lijst):
    return min(mijn_lijst), max(mijn_lijst)
print(laag_en_hoog([220,430,125,160,205,90,345]))

def gemiddelde(mijn_lijst):
    bedrag=sum(mijn_lijst)/len(mijn_lijst)
    uitvoer=(f"De gemiddelde inkomsten deze week zijn {bedrag} euro.")
    return uitvoer
print(gemiddelde([220,430,125,160,205,90,345]))

def meervoudig(invoer_lijst):
    return(laag_en_hoog(invoer_lijst))
print(meervoudig([10,5,3,2,1,2,9]))

def combinatie(invoer_lijst_2):
    korte_lijst=(laag_en_hoog(invoer_lijst_2))
    return (mijn_functie_2(korte_lijst[0],korte_lijst[1]))
print(combinatie([220,430,125,160,205,90,345]))

from voertuig import Voertuig
from fiets import Fiets
from auto import Auto

# 1. Maak een lijst van voertuigen
voertuigen = [Voertuig("onbekend", 70),
              Fiets("Trek", 20),
              Auto("audi", 120, 4)]
# 2. Overloop de lijst en roep voor elk voertuig de methode beweeg() op
for voertuig in voertuigen:
    print(voertuig.beweeg())


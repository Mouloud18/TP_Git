import fight, createMob, personnage
from compteurEnnemisTues import *

compteurkills = 0
playagain = 0

while playagain == 0:

    nomperso = input("Choisissez un pseudo pour votre personnage : ")
    MonPerso = personnage.personnage(nomperso,20,6,3)

    while MonPerso[1] > 0:
        Ennemi = createMob.createMob()
        fight.fight(MonPerso, Ennemi)

        if MonPerso[1] > 0:
            compteurkills=compteurEnnemisTue(compteurkills)

    print(f"Le joueur {MonPerso[0]} a succombé à ses blessures, entrainant avec lui dans la tombe pas moins de {compteurkills} monstres !")

    rejouer = input("Voulez vous rejouer ? [o/n] : ")
    
    while rejouer != "o" and rejouer != "n":
        
        rejouer = input("Voulez vous rejouer ? [o/n] : ")
    
    if (rejouer == "o"):
        playagain = 0
    else:
        playagain = 1
        

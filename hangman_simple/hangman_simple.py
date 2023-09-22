import random
import os

# Constantes

REPRESENTATION_ASCII = [ 
    """
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    """,
    """
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    """,
    """
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    """,

    """
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    """,
    """
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    """,
    
    """
    _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    """,
    """
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """
]
LISTE_MOTS_MYSTERE = [
    "ardvark",
    "baboon",
    "camel"
]

# Fonctions

def choixMotMystere(listeMotsMystere: list[str]) -> str:
    positionMotChoisi = random.randint(0, len(listeMotsMystere) - 1)
    return listeMotsMystere[positionMotChoisi]

def demandeLettreUtilisateur() -> str:
    entreeInvalide = True

    while (entreeInvalide):
        print("Veuillez choisir une lettre à deviner")
        entreeUtilisateur = input().strip()
        entreeInvalide = not entreeUtilisateur
    return entreeUtilisateur[0].lower()

def resultatMotMystereInitial(motMystere: str) -> str:
    return '_' * len(motMystere)

def remplacerMasqueParLettre(resultatMotMystere: str, lettre: str, position: int) -> str:
    lettresResultatMotMystere = list(resultatMotMystere)
    lettresResultatMotMystere[position] = lettre
    return "".join(lettresResultatMotMystere)

def devinerLettreMotMystere(motMystere: str, lettreChoisiParUtilisateur: str, resultatMotMystere: str) -> str:
    lettreDansMotMystere = False
    positionLettre = 0

    for lettre in motMystere:
        if lettreChoisiParUtilisateur == lettre:
            lettreDansMotMystere = True
            resultatMotMystere = remplacerMasqueParLettre(resultatMotMystere, lettre, positionLettre)
        positionLettre += 1
    
    print(resultatMotMystere)

    return lettreDansMotMystere

def nettoyerConsole() -> None:
    os.system('cls' if os.name=='nt' else 'clear')

def afficherPendu(nombreVieRestant: int) -> None:
    print(REPRESENTATION_ASCII[nombreVieRestant])

def getNombreVie() -> int:
    return len(REPRESENTATION_ASCII) - 1

# Application

nombreVie = getNombreVie()
motMystere = choixMotMystere(LISTE_MOTS_MYSTERE)
resultatMotMystere = resultatMotMystereInitial(motMystere)

while(nombreVie > 0 and motMystere != resultatMotMystere):
    lettreChoisiEstValide = False
    positionLettreAVerifier = 0

    lettreChoisi = demandeLettreUtilisateur()
    nettoyerConsole()

    for lettre in motMystere:
        if lettreChoisi == lettre:
            lettreChoisiEstValide = True
            resultatMotMystere = remplacerMasqueParLettre(resultatMotMystere, lettre, positionLettreAVerifier)
        positionLettreAVerifier += 1

    if lettreChoisiEstValide:
        afficherPendu(nombreVie)
        print("Vous avez trouvé une des lettres du mot mystère !")
    else:
        nombreVie -= 1
        afficherPendu(nombreVie)
        print("Il ne vous reste plus que " + str(nombreVie) + " vies !")

    print(resultatMotMystere)

if (nombreVie == 0):
    print("Vous avez perdu !")
    print("Le mot à deviner était : " + motMystere)
else:
    print("Vous avez trouvé le mot ! Bien joué ;)")

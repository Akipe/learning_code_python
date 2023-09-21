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
NOMBRE_VIE_MAX = 6

# Fonctions

def choixMotMystere(listeMotsMystere):
    positionMotChoisi = random.randint(0, len(listeMotsMystere) - 1)
    return listeMotsMystere[positionMotChoisi]

def demandeLettreUtilisateur():
    print("Veuillez choisir une lettre à deviner")
    return input().strip()[0].lower()

def resultatMotMystereInitial(motMystere):
    return '_' * len(motMystere)

def remplacerMasqueParLettre(resultatMotMystere, lettre, position):
    lettresResultatMotMystere = list(resultatMotMystere)
    lettresResultatMotMystere[position] = lettre
    return "".join(lettresResultatMotMystere)

def devinerLettreMotMystere(motMystere, lettreChoisiParUtilisateur, resultatMotMystere):
    lettreDansMotMystere = False
    positionLettre = 0

    for lettre in motMystere:
        if lettreChoisiParUtilisateur == lettre:
            lettreDansMotMystere = True
            resultatMotMystere = remplacerMasqueParLettre(resultatMotMystere, lettre, positionLettre)
        positionLettre += 1
    
    print(resultatMotMystere)

    return lettreDansMotMystere

def nettoyerConsole():
    os.system('cls' if os.name=='nt' else 'clear')

def afficherPendu(nombreVieRestant):
    print(REPRESENTATION_ASCII[nombreVieRestant])

# Application

nombreVie = NOMBRE_VIE_MAX
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

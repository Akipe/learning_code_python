import os
from hangman.core.HangManUI import HangManUI
from hangman.core.HangManGuessWord import HangManGuessWord
from utils.StringUtils import StringUtils

class HangManUITerminal(HangManUI):
    HANG_MAN_BY_LIFE_ASCII = [ 
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
    CMD_CLEAR_WINDOWS = "cls"
    CMD_CLEAR_UNIX = "clear"

    def askUserChar(self) -> str:
        entreeInvalide = True

        while (entreeInvalide):
            print("Veuillez choisir une lettre à deviner")
            # entreeUtilisateur = StringUtils.getOnlyFirstChar(input().lower())
            entreeUtilisateur = input().strip().lower()[0]
            entreeInvalide = not entreeUtilisateur
        return entreeUtilisateur

    def sayWordContainsChar(self, char: str) -> None:
        print("Nice! The word contains " + char)

    def sayWordDoesNotContainsChar(self, char: str) -> None:
        print("Oh! The word does not contains " + char)

    def showHangMan(self, life: int) -> None:
        print(self._getHangManASCII(life))

    def showUserWin() -> None:
        print("You win !")

    def showUserLoose(self, word: HangManGuessWord) -> None:
        print("You loose ! The word was " + word.getWord())

    def _getHangManASCII(self, life: int) -> str:
        return self.HANG_MAN_BY_LIFE_ASCII[life - 1]

    def clearScreen(self) -> None:
        os.system(self.CMD_CLEAR_WINDOWS if os.name=='nt' else self.CMD_CLEAR_UNIX)

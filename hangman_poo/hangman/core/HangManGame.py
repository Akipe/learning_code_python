from utils.ListUtils import ListUtils
from .HangManGuessWord import HangManGuessWord
from .HangManUI import HangManUI

class HangManGame:
    MAX_LIFE = 6

    _life: int
    _guessWord: HangManGuessWord
    _ui: HangManUI

    def __init__(self, randomWords: list[str], ui: HangManUI) -> None:
        self._life = self.MAX_LIFE
        self._guessWord = HangManGuessWord(ListUtils.getRandomElementString(randomWords))
        self._ui = ui
    
    def play(self):
        while (not self.gameEnded()):
            char = self._ui.askUserChar()
            self._ui.clearScreen()
            
            if (self._guessWord.guessChar(char)):
                self._ui.sayWordContainsChar(char)
                self._ui.showHangMan(self._life)
            else:
                self.removeOneLife()
                self._ui.sayWordDoesNotContainsChar(char)
                self._ui.showHangMan(self._life)
        
        if (self._guessWord.successGuessed()):
            self._ui.showUserWin()
        else:
            self._ui.showUserLoose(self._guessWord)

    def removeOneLife(self) -> None:
        self._life -= 1
    
    def gameEnded(self) -> bool:
        return self._life == 0 or self._guessWord.successGuessed()
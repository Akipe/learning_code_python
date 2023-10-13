import abc
from .HangManGuessWord import HangManGuessWord

class HangManUI(abc.ABC):
    @abc.abstractclassmethod
    def askUserChar(self) -> str:
        pass

    @abc.abstractclassmethod
    def sayWordContainsChar(self, char: str) -> None:
        pass

    @abc.abstractclassmethod
    def sayWordDoesNotContainsChar(self, char: str) -> None:
        pass

    @abc.abstractclassmethod
    def showHangMan(self, life: int) -> None:
        pass

    @abc.abstractclassmethod
    def showUserWin(self) -> None:
        pass

    @abc.abstractclassmethod
    def showUserLoose(self, word: HangManGuessWord) -> None:
        pass

    @abc.abstractclassmethod
    def clearScreen(self) -> None:
        pass
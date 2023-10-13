from hangman.core.HangManGame import HangManGame
from utils.DictionaryWords import DictionaryWords
from hangman.ui.terminal.HangManUITerminal import HangManUITerminal

def main() -> None:
    dictionaryWords = DictionaryWords()
    hangManUI = HangManUITerminal()
    hangManGame = HangManGame(dictionaryWords.getWords(), hangManUI)
    hangManGame.play()

main()
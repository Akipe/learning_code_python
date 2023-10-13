from utils.StringUtils import StringUtils

class HangManGuessWord:
    _word: str
    _result: str

    def __init__(self, word: str) -> None:
        self._setWord(word)
    
    def getWord(self) -> str:
        return self._word
    
    def guessChar(self, char: str) -> bool:
        # char = StringUtils.getOnlyFirstChar(char)
        char = char.strip().lower()[0]
        hasChar = False
        charPosition = 0
        for charGuessWord in self._word:
            if charGuessWord == char:
                hasChar = True
                self._removeMaskResult(char, charPosition)
            charPosition += 1
        return hasChar

    def successGuessed(self) -> bool:
        return self._word == self._result

    def _setWord(self, word: str) -> None:
        self._word = word
        self._result = "_" * len(self._word)

    def _removeMaskResult(self, char: str, charPosition: int) -> None:
        # self._result[charPosition] = char
        resultByChars = list(self._result)
        resultByChars[charPosition] = char
        self._result = "".join(resultByChars)

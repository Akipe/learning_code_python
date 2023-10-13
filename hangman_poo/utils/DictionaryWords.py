class DictionaryWords:
    _words: list[str]

    def __init__(self) -> None:
        self._word = [
        "ardvark",
        "baboon",
        "camel"
    ]
        
    def getWords(self) -> list[str]:
        return self._word

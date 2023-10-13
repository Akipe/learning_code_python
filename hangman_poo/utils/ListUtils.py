import random

class ListUtils:
    @staticmethod
    def getRandomElementString(list: list[str]) -> str:
        return list[ListUtils.getRandomIndexString(list)]

    @staticmethod
    def getRandomIndexString(list: list[str]) -> int:
        return random.randint(0, len(list) - 1)

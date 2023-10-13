class StringUtils:
    @staticmethod
    def getOnlyFirstChar(stringToCheck: str) -> str:
        if (len(stringToCheck) > 0):
            return stringToCheck.strip[0]
        else:
            return ""

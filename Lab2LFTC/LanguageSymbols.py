operators = []
separators = []
reservedWords = []


def readFile():
    with open('tokens.in', 'r') as file:
        for i in range(11):
            separator = file.readline().strip()
            if separator == "space":
                separator = " "
            if separator == "newline":
                separator = "\n"
            separators.append(separator)
        for i in range(14):
            operators.append(file.readline().strip())
        for i in range(11):
            reservedWords.append(file.readline().strip())


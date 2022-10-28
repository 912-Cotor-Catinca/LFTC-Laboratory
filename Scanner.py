import re

from LanguageSymbols import *
from PIF import PIF
from SymbolTable import SymbolTable


class Scanner:
    def __init__(self):
        self.symbol_table = SymbolTable(20)
        self.pif = PIF()

    def isPartOfOperator(self, char):
        for op in operators:
            if char in op:
                return True
        return False

    def getOperatorToken(self, line, index):
        token = ''
        while index < len(line) and self.isPartOfOperator(line[index]):
            token += line[index]
            index += 1
        return token, index

    def getStrings(self, line, index):
        token = ''
        qoutes = 0

        while index < len(line) and qoutes < 2:
            if line[index] == '\"':
                qoutes += 1
            token += line[index]
            index += 1

        return token, index

    def tokenize(self, line):
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            if self.isPartOfOperator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.getOperatorToken(line, index)
                tokens.append(token)
                token = ''  # reset token
            elif line[index] in separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''
            elif line[index] == '\"':
                if token:
                    tokens.append(token)
                token, index = self.getStrings(line, index)
                tokens.append(token)
                token = ''
            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens

    def isIdentifier(self, token):
        return re.match(r'^[a-z]([a-zA-Z]|[0-9])*$', token) is not None

    def isConstant(self, token):
        return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^\".\"$|^\".*\"$', token) is not None

    def run_program(self):
        readFile()
        filename = "p1err"
        error_message = ""
        with open(filename, 'r') as file:
            cnt = 0
            for line in file:
                cnt += 1
                tokens = self.tokenize(line.strip())
                for i in range(len(tokens)):
                    if tokens[i] in separators + operators + reservedWords:
                        if tokens[i] == " " or tokens[i] == '\n':
                            continue
                        self.pif.add(tokens[i], (-1, -1))
                    elif self.isIdentifier(tokens[i]):
                        id = self.symbol_table.add(tokens[i])
                        self.pif.add("id", id)
                    elif self.isConstant(tokens[i]):
                        const = self.symbol_table.add(tokens[i])
                        self.pif.add("const", const)
                    else:
                        error_message += "Lexical error at token " + tokens[i] + " at line " + str(cnt) + "\n"
        with open('st.out', 'w') as file:
            file.write(str(self.symbol_table))

        with open('pif.out', 'w') as file:
            file.write(str(self.pif))

        if error_message == "":
            print("Lexically correct")
        else:
            print(error_message)

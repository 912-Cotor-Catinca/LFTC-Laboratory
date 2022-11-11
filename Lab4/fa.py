class FiniteAutomata:
    def __init__(self, Q, E, q0, F, S):
        self.Q = Q
        self.E = E
        self.q0 = q0
        self.F = F
        self.S = S

    @staticmethod
    def getLine(line):
        return line.strip().split(' ')[2:]

    @staticmethod
    def validate(Q, E, q0, F, S):
        if q0 not in Q:
            return False
        for f in F:
            if f not in Q:
                return False
        for key in S.keys():
            state = key[0]
            symbol = key[1]
            if state not in Q:
                return False
            if symbol not in E:
                return False
            for dest in S[key]:
                if dest not in Q:
                    return False
        return True

    @staticmethod
    def readFromFile(file_name):
        with open(file_name) as file:
            Q = FiniteAutomata.getLine(file.readline())
            E = FiniteAutomata.getLine(file.readline())
            q0 = FiniteAutomata.getLine(file.readline())[0]  # get the letter
            F = FiniteAutomata.getLine(file.readline())

            file.readline()

            S = {}
            for line in file:
                src = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[0]
                route = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[1]
                dest = line.strip().split('->')[1].strip()

                if (src, route) in S.keys():
                    S[(src, route)].append(dest)
                else:
                    S[(src, route)] = [dest]
            if not FiniteAutomata.validate(Q, E, q0, F, S):
                raise Exception("Wrong input")

            return FiniteAutomata(Q, E, q0, F, S)

    def isDfa(self):
        for k in self.S.keys():
            if len(self.S[k]) > 1:
                return False
        return True

    def __str__(self):
        return "Q = { " + ', '.join(self.Q) + " }\n" \
                                              "E = { " + ', '.join(self.E) + " }\n" \
                                                                             "q0 = { " + self.q0 + " }\n" \
                                                                                                   "F = { " + ', '.join(
            self.F) + " }\n" \
                        "S = " + str(self.S) + ""

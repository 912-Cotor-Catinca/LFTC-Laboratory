from fa import FiniteAutomata


class UI:
    def readFA(self):
        self.fa = FiniteAutomata.readFromFile('FA.txt.in')

    def displayALL(self):
        print(self.fa)

    def displayStates(self):
        print(self.fa.Q)

    def displayAlphabet(self):
        print(self.fa.E)

    def displayTransitions(self):
        print(self.fa.S)

    def displayFinalStates(self):
        print(self.fa.F)

    def checkDFA(self):
        print(self.fa.isDfa())

    def checkAccepted(self):
        seq = input()
        print(self.fa.isAccepted(seq))

    def menu(self):
        print("1.Read FA from file")
        print("2.Display FA")
        print("3.Display FA States")
        print("4.Display FA Alphabet")
        print("5.Display FA transitions")
        print("6.Display FA final states")
        print("7.Check DFA")
        print("8.Check accepted sequence")

    def run(self):
        commands = {'1': self.readFA,
                    '2': self.displayALL,
                    '3': self.displayStates,
                    '4': self.displayAlphabet,
                    '5': self.displayTransitions,
                    '6': self.displayFinalStates,
                    '7': self.checkDFA,
                    '8': self.checkAccepted}
        exit = False
        while not exit:
            self.menu()
            print(">>")
            cmd = input()
            if cmd in commands.keys():
                commands[cmd]()
            elif cmd == "exit":
                exit = True
            else:
                continue



class Brain:
    def __init__(self):
        self.one_variable = 42

    def think(self, stdin_input):
        print(stdin_input)
        if (stdin_input[0] == "START"):
            self.map_size = int(stdin_input[1])
            return "OK - everything is good"
        else:
            return "ERROR unknown command"
        
    def reset(self):
        self.one_variable = 0

class Scissors:

    def __init__(self):
        self.winTable = {"rock": -1,
                         "paper": 1,
                         "scissors": 0}
        
    def __repr__(self):
        return f"Scissors()"
    
    def __str__(self):
        return "scissors"
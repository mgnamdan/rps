class Paper:

    def __init__(self):
        self.winTable = {"rock": 1,
                         "paper": 0,
                         "scissors": -1}
        
    def __repr__(self):
        return f"Paper()"
    
    def __str__(self):
        return "paper"
class Rock:

    def __init__(self):
        self.winTable = {"rock": 0,
                         "paper": -1,
                         "scissors": 1}
        
    def __repr__(self):
        return f"Rock()"
    
    def __str__(self):
        return "rock"
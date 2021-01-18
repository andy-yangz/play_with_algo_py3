class Edge:
    def __init__(self, a, b, weight):
        self.a = a
        self.b = b
        self.weight = weight
    
    def v(self):
        return self.a
    
    def w(self):
        return self.b
    
    def wt(self):
        return self.weight
    
    def other(self, x):
        assert (x==self.a) or (x==self.b)
        return self.b if x==self.a else self.a
    
    def __str__(self):
        return f"{self.a}-{self.b}: {self.weight}"
    
    def __eq__(self, other):
        return self.weight == other.weight
    
    def __lt__(self, other):
        return self.weight < other.weight
    
    def __le__(self, other):
        return self.weight <= other.weight
    
    def __gt__(self, other):
        return self.weight > other.weight
    
    def __ge__(self, other):
        return self.weight >= other.weight
    
    def __ne__(self, other):
        return self.weight != other.weight

class Pendrive:
    def __init__(self, c, capacity):
        self.color = c
        self.capacity = capacity
    def __gt__(self, other):
        return self.capacity > other.capacity
    def __str__(self):
        return self.color + " " + str(self.capacity)
    def __repr__(self):
        return self.__str__()
    

souravpd = Pendrive("black", 1)
rifazpd = Pendrive("red", 2)

from __future__ import division

class Item:

    def __init__(weight, value):    
        self.weight=weight
        self.value=value

    def getWeight(self):
        return self.weight

    def getValue(self):
        return self.value

    def getRelativeBenefit(self):
        return self.value/self.weight
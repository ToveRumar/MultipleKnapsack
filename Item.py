from __future__ import division

class Item:

    def __init__(self,weight, value):    
        self.weight=weight
        self.value=value

    def getWeight(self):
        return self.weight

    def getValue(self):
        return self.value

    def getRelativeBenefit(self):
        return self.value/self.weight

    def __repr__(self):
        return "Item weight " + str(self.weight)+ "\n Item value " + str(self.value) + "\nRelative benefit " + str(self.getRelativeBenefit()) + "\n"
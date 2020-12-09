

class Knapsack:
    def __init__():
        self.content=[]
        self.maxWeight

    def getContent(self):
        return self.content

    def aboveMaxWeight(self):
        weightSum=0
        for item in self.content:
            weightSum+=item.getWeight()
        return weightSum>self.maxWeight

    def getTotalValue(self):
         valtSum=0
        for item in self.content:
            valSum+=item.getValue()
        return valSum
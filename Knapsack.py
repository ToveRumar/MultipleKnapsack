

class Knapsack:
    def __init__(self,maxWeight):
        self.content=[]
        self.maxWeight=maxWeight
        self.spaceLeft=maxWeight

    def getContent(self):
        return self.content
    def getSpaceLeft(self):
        return self.spaceLeft

    def aboveMaxWeight(self):
        weightSum=0
        for item in self.content:
            weightSum+=item.getWeight()
        return weightSum>self.maxWeight

    def getTotalValue(self):
        valSum=0
        for item in self.content:
            valSum+=item.getValue()
        return valSum

    def getTotalWeight(self):
        weightSum=0
        for item in self.content:
            weightSum+=item.getWeight()
        return weightSum

    def putItem(self,item):
        if item.getWeight()>self.spaceLeft:
            return False
        else:
            self.content.append(item)
            self.spaceLeft=self.maxWeight-self.getTotalWeight()
            return True
    def clear(self):
        self.content.clear()
    
    def __repr__(self):
        return "My maxWeight is " + str(self.maxWeight) + "\nI have "+ str(self.spaceLeft)+" Space left \nI hold the following items:\n" + str(self.content) +"\n my total value is " + str(self.getTotalValue()) + "\n"
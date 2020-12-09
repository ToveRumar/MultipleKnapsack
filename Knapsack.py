

class Knapsack:
    def __init__(self,maxWeight):
        self.content=[]
        self.maxWeight=maxWeight
        self.Capacity=maxWeight

    def getContent(self):
        return self.content
    def getCapacity(self):
        return self.Capacity

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
        if item.getWeight()>self.Capacity:
          
            return False
        else:
            self.content.append(item)
            self.Capacity=self.maxWeight-self.getTotalWeight()
            return True
    def clear(self):
        self.content.clear()
    
    def removeItem(self, item):
        
        self.content.remove(item)
        self.Capacity+=item.getWeight()
        return item

    def __repr__(self):
        return "My maxWeight is: " + str(self.maxWeight) + ", I have "+ str(self.Capacity)+" Space left ,I hold the following items: " + str(self.content) +", my total value is: " + str(self.getTotalValue()) 
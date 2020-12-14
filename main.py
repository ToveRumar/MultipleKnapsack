from Knapsack import Knapsack
from Item import Item
import random
#Main program
#allItems=[Item(1,3),Item(2,4),Item(3,1), Item(4,2), Item(1, 2), Item(3, 3), Item(2,3),Item(2,3),Item(5,6), Item(4,3), Item(2, 2), Item(4, 6)]
#allItems=[Item(5,4),Item(2,5),Item(1,5), Item(3,3), Item(3,2), Item(1,4), Item(4,1),Item(1,1),Item(1,2), Item(3,2), Item(2, 2), Item(4, 6), Item(4,4)]
allItems=[Item(6,15),Item(3,7),Item(7,10), Item(5,5), Item(3,1), Item(1,4), Item(6,8),Item(1,1),Item(4,4), Item(5,2), Item(3,3), Item(4, 6), Item(2,1)]

allKnapsacks=[Knapsack(6),Knapsack(8),Knapsack(5)]
#allKnapsacks=[Knapsack(20),Knapsack(10),Knapsack(15)]
#allKnapsacks=[Knapsack(6),Knapsack(8),Knapsack(5),Knapsack(10)]


#Returns list of items sorted by benefit in descending order
def sortItemsByBenefit():                                                            
    allItems.sort(key=Item.getRelativeBenefit,reverse=True) 

#Returns list of items sorted by weight in descending order
def sortItemsByWeight():                                                            
    allItems.sort(key=Item.getWeight,reverse=True)

#Returns list of knapsacks soted by Capacity in ascending order
def sortKnapsacksByCapacity(knapsacks):
    return sorted(knapsacks, key=Knapsack.getCapacity) 

def putItemInKnapsackLeastSpace(item):
   
    for knapsack in allKnapsacks:
        if (knapsack.putItem(item)):
            
            return True
  
    return False

def putItemInRandomKnapsack(item):
    knapsack=random.choice(allKnapsacks)
    return knapsack.putItem(item)
    

def greedyLeastSpace():
    print("Result of least space greedy search")
    sortItemsByBenefit()
    sortKnapsacksByCapacity(allKnapsacks)
    #allItems = list(sortedItems)
    itemsToRemove=[]
    for item in allItems:
        
        if putItemInKnapsackLeastSpace(item):
            itemsToRemove.append(item)
    for item in itemsToRemove:
        allItems.remove(item)
           

def greedyRandom():
    
    print("Result of random greedy search")
    sortItemsByBenefit()
   
    itemsToRemove=[]
    for item in allItems:
        if putItemInRandomKnapsack(item):
            #allItems.remove(item)
            itemsToRemove.append(item)
    for item in itemsToRemove:
        allItems.remove(item)
    


def clearAllKnapsacks():
    for knapsack in allKnapsacks:
        knapsack.clear()



def printState():
    print("============================================")
    for knapsack in allKnapsacks:
        print(knapsack)
        print("-----------------------------------")
    print("Items left: " + str(len(allItems)))
    print("Value of all knapsacks: " + str(valueOfAllKnapsacks(allKnapsacks)))
        
def printTestCase():
    print("============================================")
    print("Test Items: "+str(allItems))
    print("Test knapsacks: "+str(allKnapsacks))
    print("============================================")

def neighborhoodSearch(allKnapsacks, allItems,depth):
    
    sortItemsByWeight()
    bestNeighbor = findBestNeighbor(allKnapsacks, allItems)
    
    if bestNeighbor[0] >= valueOfAllKnapsacks(allKnapsacks) and depth != 0:

        if len(bestNeighbor) == 1:
            print("Result of neighborhood search")
            printState()   
        elif len(bestNeighbor) == 3:
            bestNeighbor[2].putItem(bestNeighbor[1])
            print("Value after puttting item:" +  str(valueOfAllKnapsacks(allKnapsacks)))
            neighborhoodSearch(allKnapsacks,allItems,depth-1)
        elif len(bestNeighbor) == 4:
           
            itemToPile=bestNeighbor[2].removeItem(bestNeighbor[3])
            allItems.append(itemToPile)
            allItems.remove(bestNeighbor[1])
            bestNeighbor[2].putItem(bestNeighbor[1])
            print("value afterswapping with pile: "+ str(valueOfAllKnapsacks(allKnapsacks)))
            neighborhoodSearch(allKnapsacks,allItems,depth-1)
        elif len(bestNeighbor) == 5:
            
            otherItem = bestNeighbor[4].removeItem(bestNeighbor[1])
            ourItem = bestNeighbor[2].removeItem(bestNeighbor[3])
            bestNeighbor[2].putItem(otherItem)
            bestNeighbor[4].putItem(ourItem)
            print("value afterswapping with other knapsack: "+ str(valueOfAllKnapsacks(allKnapsacks)))
            neighborhoodSearch(allKnapsacks,allItems,depth-1)
    else:
        print("Result of neighborhood search")
        printState()
    




def findBestNeighbor(allKnapsacks, allItems):
    bestNeighbor = [0]
    for knapsack in allKnapsacks:
        for item in allItems:
            if knapsack.getCapacity() >= item.getWeight():
                totalChildValue = valueOfAllKnapsacks(allKnapsacks) + item.getValue()
                if totalChildValue > bestNeighbor[0]:
                    bestNeighbor = [totalChildValue, item, knapsack]
            for knapItem in knapsack.getContent():
                if (item.getValue() > knapItem.getValue()) and (item.getWeight() <= (knapsack.getCapacity() + knapItem.getWeight())): 
                    #print("Creatin suggestion for swap with pile")
                    #checks if item from pile has a higher value than the item in our knapsack, and if the item can fit in the knapsack
                    totalChildValue = valueOfAllKnapsacks(allKnapsacks) - knapItem.getValue() + item.getValue()
                    if totalChildValue > bestNeighbor[0]:
                        #print("Creatin suggestion for swap with pile")
                        bestNeighbor = [totalChildValue, item, knapsack, knapItem]
        for otherKnapsack in allKnapsacks:
           
            if otherKnapsack is not knapsack:
                for ourItem in knapsack.getContent():
                    for otherItem in otherKnapsack.getContent():
                        if ourItem.getWeight() > otherItem.getWeight() and (ourItem.getWeight()<=(otherKnapsack.getCapacity()+ otherItem.getWeight())):
                        
                            bestNeighbor = [valueOfAllKnapsacks(allKnapsacks), otherItem, knapsack, ourItem, otherKnapsack]                            
                            #print("Creating suggestion for swap")
        
    return bestNeighbor
                


def valueOfAllKnapsacks(allKnapsacks):
    knapValue = 0
    for knapsack in allKnapsacks:
        knapValue += knapsack.getTotalValue()
    return knapValue


printTestCase()
#greedyLeastSpace()

greedyRandom()
printState()
neighborhoodSearch(allKnapsacks,allItems,100)

#clearAllKnapsacks()




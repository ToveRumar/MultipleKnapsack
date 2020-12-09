from Knapsack import Knapsack
from Item import Item
import random
#Main program
allItems=[Item(1,3),Item(2,4),Item(3,1), Item(4,2), Item(1, 2), Item(3, 3), Item(2,3),Item(2,3),Item(5,6), Item(4,3), Item(2, 2), Item(4, 6)]
allKnapsacks=[Knapsack(6),Knapsack(8),Knapsack(5)]


#Returns list of items soted by benefit in descending order
def sortItemsByBenefit():                                                            
    allItems.sort(key=Item.getRelativeBenefit,reverse=True) 

#Returns list of knapsacks soted by Capacity in ascending order
def sortKnapsacksByCapacity(knapsacks):
    return sorted(knapsacks, key=Knapsack.getCapacity) 

def putItemInKnapsackLeastSpace(item):
    knapsacks=sortKnapsacksByCapacity(allKnapsacks)
    return knapsacks[0].putItem(item)

def putItemInRandomKnapsack(item):
    knapsack=random.choice(allKnapsacks)
    return knapsack.putItem(item)
    

def greedyLeastSpace():
    print("Result of least space greedy search")
    sortItemsByBenefit()
    #allItems = list(sortedItems)
    for item in allItems:
        if putItemInKnapsackLeastSpace(item):
            allItems.remove(item)
            #print(str(item))

def greedyRandom():
    
    print("Result of random greedy search")
    sortItemsByBenefit()
   
    
    for item in allItems:
        if putItemInRandomKnapsack(item):
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

def neighborhoodSearch(allKnapsacks, allItems):
    
    bestNeighbor = findBestNeighbor(allKnapsacks, allItems)
    if bestNeighbor[0] > valueOfAllKnapsacks(allKnapsacks):
        if len(bestNeighbor) == 3:
            bestNeighbor[2].putItem(bestNeighbor[1])
            neighborhoodSearch(allKnapsacks,allItems)
        elif len(bestNeighbor) == 4:
            allItems.append(bestNeighbor[2].removeItem())
            bestNeighbor[2].putItem(bestNeighbor[1])
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
                if (item.getValue() > knapItem.getValue()) and (item.getWeight() < (knapsack.getCapacity() - knapItem.getWeight())): 
                    #checks if item from pile has a higher value than the item in our knapsack, and if the item can fit in the knapsack
                    totalChildValue = valueOfAllKnapsacks(allKnapsacks) - knapItem.getValue() + item.getValue()
                    if totalChildValue > bestNeighbor[0]:
                        bestNeighbor = [totalChildValue, item, knapsack, knapItem]
    return bestNeighbor
                

def valueOfAllKnapsacks(allKnapsacks):
    knapValue = 0
    for knapsack in allKnapsacks:
        knapValue += knapsack.getTotalValue()
    return knapValue


printTestCase()
greedyLeastSpace()
#greedyRandom()
printState()
neighborhoodSearch(allKnapsacks,allItems)

#clearAllKnapsacks()




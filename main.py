from Knapsack import Knapsack
from Item import Item
import random
#Main program
allItems=[Item(1,3),Item(2,4),Item(3,1)]
allKnapsacks=[Knapsack(6),Knapsack(8),Knapsack(5)]


#Returns list of items soted by benefit in descending order
def sortByBenefit(Items):                                                            
    return sorted(Items, key=Item.getRelativeBenefit,reverse=True) 

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
    sortedItems=sortByBenefit(allItems)

    for item in sortedItems:
        if putItemInKnapsackLeastSpace(item):
            sortedItems.remove(item)

def greedyRandom():
    sortedItems=sortByBenefit(allItems)

    for item in sortedItems:
        if putItemInRandomKnapsack(item):
            sortedItems.remove(item)

def clearAllKnapsacks():
    for knapsack in allKnapsacks:
        knapsack.clear()



def printState():
    for knapsack in allKnapsacks:
        print(knapsack)
        print("-----------------------------------")
        
greedyRandom()

clearAllKnapsacks()
greedyLeastSpace()
printState()



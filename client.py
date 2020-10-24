print("Welcome to the Commons Game!")

trees = 20
growthRate = 1.4
ownedTrees = 0

while(1):
    print("There are {} trees in the field!".format(trees))
    print("Enter the number of trees you will cut down")
    treesCut = int(input())
    ownedTrees = ownedTrees + treesCut
    trees = trees - treesCut
    trees = trees * growthRate
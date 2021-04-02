def addFruit(quantity, name, price):
    mlist.append([name, quantity, price])

def displayFruitList(mlist):
    for itr in mlist:
        print(itr[0],'\t--- $',itr[1]*itr[2])

mlist = [("Orange", 10, 0.25), ("Apple", 5, 0.2), ("Banana", 2, 0.3), ("Kiwi", 1, 0.5)]

addFruit(10, "Lemon", 0.1)
displayFruitList(mlist)
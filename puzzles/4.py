list = [2, 10, 3, 17]
listHold = []

for x in list:
    listHold.clear()
    listHold = listHold + [0]*(x - len(listHold)) 
    listHold[0] = x
    for y in listHold:
        if(y == x):
            continue
        listHold[listHold.index(y)] += (listHold[listHold.index(y) - 1] + 2)

    print(*listHold, sep=" ")

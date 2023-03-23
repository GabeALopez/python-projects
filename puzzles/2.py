list1 = [19, 19, 15, 5, 5, 5, 1, 2]
list2 = [19, 15, 5, 7, 5, 5, 2]
list3 = [11, 12, 14, 13, 14, 13, 15, 14]
list4 = [19, 15, 11, 7, 5, 6, 2]

listAll = [list1, list2, list3, list4]

count = 0

for x in listAll:
    for y in x:
        if(y == x[4]):
            count += 1

    if(len(x) == 8 and count % 3 == 0):
        print("true")
    else:
        print("false")
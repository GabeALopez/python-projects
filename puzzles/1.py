list = [19, 19, 15, 5, 3, 5, 5, 2]
list2 = [19, 15, 15, 5, 3, 3, 5, 2]
list3 = [19, 19, 5, 5, 5, 5, 5]
count1 = 0
count2 = 0
tag1 = 0
tag2 = 0

for x in list3:
    if(x == 19):
        if(count1 == 2):
            continue 
        count1 +=1 
    elif(x == 5):
        if(count2 == 3):
            continue
        count2 += 1


if(count1 == 2 and count2 == 3):
    print("True")
else:
    print("False")
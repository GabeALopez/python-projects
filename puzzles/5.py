list1 = ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
list2 = ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
list3 = ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
list4 = ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']

listAll = [list1, list2, list3, list4]

boolVal = False

for x in listAll:
    for y in x:
        if(x[x.index(y)-1] != None):
            if(x[x.index(y)].find(x[x.index(y) - 1])):
                
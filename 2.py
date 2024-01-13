my_list = []
pos = 0
neg = 0
for i in range(3):
    userinput = int(input("Enter a number: "))
    my_list.append(userinput)
    if userinput > 0:
        pos += 1
    elif userinput < 0:
        neg += 1
print (pos, " positive numbers",'\n',neg, " negative numbers")
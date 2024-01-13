my_list = []
pos = 0
neg = 0
min = 9999999
for i in range(3):
    userinput = int(input("Enter a number: "))
    my_list.append(userinput)
    if userinput < min:
        min = userinput
my_list.remove(min)
sum = my_list[0] + my_list[1]
print (sum)
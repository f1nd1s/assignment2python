x = float(input("Enter a number: "))
y = float(input("Enter a number: "))
if x>0 and y>0:
    print("1 quarter")
elif x<0 and y > 0:
    print("2 quarter")
elif x < 0 and y < 0:
    print("3 quarter")
elif x > 0 and y < 0:
    print("4 quarter")
x = int(input())
y = int(input())
z = int(input())
if (x != 0 and y != 0 and z != 0) :
    if ((x * x) + (y * y) == (z * z) or (x * x) + (z * z) == (y * y) or (y * y) + (z * z) == (x * x)) :
        print("Yes")
    else :
        print("No")
else :
    print("No")
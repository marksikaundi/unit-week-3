percentage = ( 60 * 100) // 55
print (percentage)

x = 5
if x % 2 == 0:
    print (x)
else:
    print (x, x%2)

percentage =  float ( 60 * 100) / 55
print (percentage)

x=1
y=2
if x == y:
    print (x, "and", y, "are equal")
else:
    if x < y:
        print (x, "is less than", y)
    else:
        print (x, "is greater than", y)

def recurse(a):
    if (a == 0):
        print(a)
    else:
        recurse(a)

recurse(1)
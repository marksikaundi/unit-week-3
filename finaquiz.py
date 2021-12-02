n = 17
print(n)
print (1,000,000)

percentage = ( 60 * 100) // 55
print (percentage)
print (2*3-1)
x=2
y=1
if x == y:
    print (x, "and", y, "are equal")
else:
    if x < y:
        print (x, "is less than", y)
    else:
        print (x, "is greater than", y)

percentage = ( 60.0 * 100.0) / 55.0
print (percentage)

def recurse(a):
    if (a == 1):
        print(a)
    else:
        recurse(a)

recurse(1)
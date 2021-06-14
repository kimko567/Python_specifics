print("Input three numbers: ")
a = int(input())
b = int(input())
c = int(input())

print("Median: ")
if a == b and b == c:
    print(a)

if (a > b and a < c) or (a > c and a < b):
    print(a)
if (b > a and b < c) or (b > c and b < a):
    print(b)
if (c > b and c < a) or (c > a and c < b):
    print(c)
    
    



def compare(a, b):
    for n in a:
        test = True
        for m in b:
            if n == m:
                test = False
        if test == True:
           print(n)

def Vinput():
    vec = []
    while True:
        x = input()
        vec.append(int(x))
        if int(x) == 0:
            break
    return vec
    
print("Input vector Nr.1 : ")
vec1 = Vinput()
    
print("Input vector Nr.2 : ")
vec2 = Vinput()
print("Compare result:")
compare(vec1, vec2)

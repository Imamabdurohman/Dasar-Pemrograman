#Deret 1
result=50
add=2

print ("Deret 1: ")
for i in range(8):
    print (result,end=", ")
    result-= add
    add+=2

print("\n=========================================\n")
#Deret 2
a,b=2,3

print ("Deret 2: ")
for i in range(8):
    print(a,end=", ")
    a,b=b,a+b

print("\n=========================================\n")
#Deret 3
result=40
add=1
loop=8

print ("Deret 3: ")
for i in range(8):
    print(result,end=", " if i<loop -1 else " ")
    result-=add
    add+=2

print("\n=========================================\n")
#Deret 4
result=100
add=1
loop=8

print ("Deret 4: ")
for i in range(8):
    print(result,end=", " if i<loop -1 else " ")
    result-=add
    add+=2

print("\n=========================================\n")
#Deret 5
a=b=c=1

print ("Deret 5: ")
for i in range(8):
    print(c,end=" ")
    if (i>=1):
        c=a+b
        a=b
        b=c
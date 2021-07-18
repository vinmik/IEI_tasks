p=7
for i in range(4):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,p):
        if k%2==0:
            print("1",end="")
        else:
            print("0",end="")
    p=p-2
    print("\n")


hor= int(input("Enter x: "))
vert= int(input("Enter y: "))
for i in range(vert):
    if i == 0 or i==vert-1:
        print("*"*hor)
    else:
        print("*"," "*(hor-4),"*")


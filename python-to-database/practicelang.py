num1= 5
num2=3
high= 1;
for i in range(1,num1+1):
    if num1%i==0 and num2%i==0:
        high=i
print(str(num2//high)+"/"+str(num1//high))

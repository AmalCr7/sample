a = int(input("Enter the current year"))
b = int(input("Enter the final year"))
if(a<b):
    print("the leap years are:", end="")
    for i in range(a,b):
        if i%4 == 0 and i%100!=0 or i%4== 0 and i%400==0:
            print(i,end=" ")
else:
    print("invalid")

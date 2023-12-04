string=input("Enter a string:")
count=0
for i in range(len(string)):
    if(string[i]!=''):
        count=count+1
print("The rtotal number op characters in the string is",count)

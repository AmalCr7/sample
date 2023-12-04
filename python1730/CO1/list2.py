list=[-5,10,0,-14,18,17]
print(list)
newlist=[x for x in list if x>0]
print("The positive numbers are:",newlist)
#square of n numbers

n=int(input("Enter the number of numbers:"))
list=[]
for i in range(n):
        a=int(input("Enter the number:"))
        list.append(a)
print(list)
list1=[x**2 for x in list]
print(list1)
#list of vowels
word=input("Enter a word:")
vowels=[x for x in word if x in['a','e','i','o','u']]
print("The vowels in the words are:",vowels)
#use of ord()
w=input("Enter a word:")
ord=[ord(x)for x in w]
print("The ordinal value is",ord)
def pypart(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("Hello World", end=" ")
        print("\r")
n = int(input("Enter the number of rows:"))
pypart(n)
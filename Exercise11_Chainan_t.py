n = int(input("Enter the number : "))
for i in range(n):
    print(" " * (n - i - 1), "*" * (n - (n - i - 1) + i))

n = int(input("Enter the number of terms for the Fibonacci series: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci series up to", n, "term:")
    print(a)
else:
    print("Fibonacci series up to", n, "terms:")
    print(a, end=" ")
    for _ in range(1, n):
        print(b, end=" ")
        a, b = b, a + b

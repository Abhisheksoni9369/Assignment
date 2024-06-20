n = int(input("Enter a positive integer: "))

if n > 0:
    sum = (n * (n + 1)) // 2
    print(f"The sum of the first {n} positive integers is: {sum}")
else:
    print("Please enter a positive integer.")

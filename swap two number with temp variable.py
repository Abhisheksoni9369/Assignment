a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print(f"Before swapping: a = {a}, b = {b}")

# Swapping using a temporary variable
temp = a
a = b
b = temp

print(f"After swapping: a = {a}, b = {b}")

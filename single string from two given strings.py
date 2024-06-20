string1 = "Hello"
string2 = "World"

swapped_str1 = string2[:2] + string1[2:]
swapped_str2 = string1[:2] + string2[2:]
combined_string = swapped_str1 + " " + swapped_str2

print(combined_string)

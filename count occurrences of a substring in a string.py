def count_substring_occurrences(main_string, substring):
    count = 0
    len_main = len(main_string)
    len_sub = len(substring)
    for i in range(len_main - len_sub + 1):
        if main_string[i:i + len_sub] == substring:
            count += 1
    return count

main_string = "hellohellohello"
substring = "hello"

result = count_substring_occurrences(main_string, substring)
print(f"The substring '{substring}' occurs {result} times in the string.")

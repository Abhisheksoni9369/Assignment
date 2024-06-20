words = ["This", "is", "a", "list", "of", "words", "with", "varying", "lengths"]

longest_length = 0
for word in words:
  if len(word) > longest_length:
    longest_length = len(word)

print(longest_length)

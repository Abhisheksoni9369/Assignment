sentence = "This is a sample sentence to test the word count."
words = sentence.lower().split()
word_counts = {}

for word in words:
  if word in word_counts:
    word_counts[word] += 1
  else:
    word_counts[word] = 1

print(word_counts)

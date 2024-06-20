word = "swim"

if len(word) >= 3:
  ending = "ing" if word[-3:] != "ing" else "ly"
  modified_word = word + ending
else:
  modified_word = word

print(modified_word)

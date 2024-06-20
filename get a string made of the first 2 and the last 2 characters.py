text = "Program"

if len(text) < 2:
  result = ""
else:
  result = text[:2] + text[-2:]

print(result)

text = "This  not a poor"

not_index = text.find("not")
poor_index = text.find("poor")

if 0 <= not_index < poor_index:
  modified_text = text[:not_index] + "good" + text[poor_index + 4:]
else:
  modified_text = text

print(modified_text)

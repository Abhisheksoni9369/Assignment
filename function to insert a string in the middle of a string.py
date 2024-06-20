text = "This is a string"
string_to_insert = "inserted"

half_index = len(text) // 2
modified_text = text[:half_index] + string_to_insert + text[half_index:]

print(modified_text)

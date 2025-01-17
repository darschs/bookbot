from collections import Counter

def count_words(content):
	words=content.split()
	return len(words)

def get_book_text(path):
	with open(path) as f:
	    return f.read()

def build_report(chars_dict, num_words):
	print("--- Begin report of books/frankenstein.txt ---")
	print(f"{num_words} words found in the document")
	print()

	for char in chars_dict:
		if char.isalpha():
		  print(f"The {char} character was found {chars_dict[char]} times")
	print("--- End report ---")

def main():
	path_to_file="books/frankenstein.txt"
	text = get_book_text(path_to_file)
	num_words=count_words(text)
	#print(f"{num_words} words found in the document")
	chars_dict = get_chars_dict(text)
	#print(chars_dict)
	build_report(chars_dict, num_words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()

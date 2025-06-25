import sys
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

from stats import word_count, character_count, dict_sort

def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
		return file_contents

def main():
	link = sys.argv[1]
	book = get_book_text(link)
	count = word_count(book)
	sorted = dict_sort(character_count(book))

	print(f"{count} words found in the document")
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {link}")
	print("----------- Word Count ----------")
	print(f"Found {count} total words")
	print("--------- Character Count -------")
	for sort in sorted:
		print(f"{sort["char"]}: {sort["num"]}")
	print("============= END ===============")
	return

main()





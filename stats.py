def sort_on(items):
        return items["num"]

def word_count(file_contents):
        num_words = len(file_contents.split())
        return num_words

def character_count(file_contents):
	character_dict = dict()
	lowercase_contents = file_contents.lower()
	letters = list(lowercase_contents)

	for letter in letters:
		if letter in character_dict:
			character_dict[letter] += 1
		else:
			character_dict[letter] = 1

	return character_dict

def sort_on(items):
    return items["num"]

def dict_sort(dicts):
	list = []
	for dict in dicts:
		if dict.isalpha():
			dict_sorted = {"char": str, "num": int}
			dict_sorted["char"] = dict
			dict_sorted["num"] = dicts[dict]
			list.append(dict_sorted)
	list.sort(reverse=True, key=sort_on)
	return list

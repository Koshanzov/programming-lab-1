russian_vowels = "аоуыэяёюие"
english_vowels = "aeiouy"

def count_vowel_letters(s: str) -> int:
	"""
	Подсчитывает количество гласных букв в
	строке на русском и английском языках
	"""
	s = s.lower()
	vowels = russian_vowels + english_vowels
	count = 0
	for char in s:
		if char in vowels:
			count += 1

	return count

my_string = input("Введите строку: ")
print(
	f"'{my_string}' содержит {count_vowel_letters(my_string)} гласных."
)
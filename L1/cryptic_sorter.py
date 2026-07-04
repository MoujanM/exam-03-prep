# Write a function that sorts a list of strings according to multiple criteria:
# 1. Primary sort: By string length (shortest first)
# 2. Secondary sort: ASCII order, except letters are compared case-insensitively
#    (for strings of same length)
# 3. Tertiary sort: By number of vowels (ascending, for same length and lexically equal)
# 4. Equal strings will appear in the same order as in the input list.


def cryptic_sorter(strings: list[str]) -> list[str]:
	# solution makes use of Schwartzian transform technique

	decorated = []
	vowels = "aeiou"
	
	for s in strings:
		length = 0
		for _ in s:
			length += 1
		
		lowered = s.lower()
		vowel_count = s.count("a") + s.count('e') + s.count('i') + s.count('u')

		decorated.append((length, lowered, vowel_count, s, s))
	
	decorated.sort()
	undecorated = [a[-1] for a in decorated]

	return undecorated


if __name__ == "__main__":
	test_cases = [
		["apple","cat","banana","dog","elephant"],
		["aaa","bbb","AAA","BBB"],
		["hello","world","hi","test"],
		[],
		[""]
	]

	for test in test_cases:
		print(f"Input: {test}\nSorted: {cryptic_sorter(test)}")
	
# Write a function that checks if two strings are anagrams.
# They must contain exactly the same letters with the same quantity,
# ignoring case and spaces.

def anagram(s1: str, s2: str) -> bool:
    clean_s1 = s1.lower()
    clean_s2 = s2.lower()
    clean_s1 = clean_s1.replace(' ', '')
    clean_s2 = clean_s2.replace(' ', '')
    if len(clean_s1) != len(clean_s2):
        return False
    for c in clean_s1:
        if c not in clean_s2 or clean_s1.count(c) != clean_s2.count(c):
            return False
    return True


if __name__ == "__main__":
    tests = [
        ("listen", "silent"),
        ("Triangle", "Integral"),
        ("Dormitory", "Dirty Room"),
        ("hello", "world"),
        ("", ""),
        ("abc", "abcc")
    ]
    for test in tests:
        print(f"test[0]}, {test[1]} --> {anagram(test[0], test[1])}")
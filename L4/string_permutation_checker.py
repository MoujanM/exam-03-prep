# Write a function that determines if two strings are permutations of each other.
# Case sensitive. Whitespace and punctuation count as regular characters.
# Empty strings are permutations of each other.
# Function signature

def string_permutation_checker(s1: str, s2: str) -> bool:
    if not s1 and not s2:
        return True
    s1_chars = []
    for c in s1:
        s1_chars.append(c)
    if s1_chars and not s2:
        return False
    for c in s2:
        if c not in s1_chars:
            return False
        else:
            return True


if __name__ == "__main__":
    tests = [
        ("abc", "def"),
        ("abc", "bca"),
        ("listen", "silent"),
        ("hello", "bello"),
        ("", ""),
        ("a", ""),
        ("Abc", "abc"),
        ("a gentleman", "elegant man")
    ]

    for test in tests:
        s1, s2 = test
        print(f"{test} --> {string_permutation_checker(s1, s2)}")
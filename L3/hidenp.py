# Write a function that checks if the string 'small' is a subsequence
# of 'big'. A subsequence means all characters of 'small' appear in 'big'
# in the same order, but not necessarily consecutively.
# Function is case-sensitive.

def hidenp(small: str, big: str) -> bool:
    if small is None:
        return True
    i = 0
    j = 0
    while (i < len(big) - 1) and j != len(small):
        if big[i] == small[j]:
            j += 1
        i += 1

    if j == len(small):
        return True
    return False


if __name__ == "__main__":
    tests = [
        ("abc", "a1b2c3"),
        ("ace", "abcde"),
        ("aec", "abcde"),
        ("", "abc"),
        ("abc", "ab"),
        ("sing","subsequence testing"),
        ("aaaa", "aaa")
    ]

    for test in tests:
        small, big = test
        print(f"Case: {small} and {big} - {hidenp(small, big)}")
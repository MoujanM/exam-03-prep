# Write a function that counts the number of valid consecutive digit pairs
# in a string. A valid pair consists of two adjacent digits where the second
# digit is exactly one greater than the first.
# A 9 followed by a 0 is NOT a valid pair.

def pattern_tracker(text: str) -> int:
    count: int = 0
    idx: int = 0
    while idx + 1 < len(text):
        if text[idx].isdigit() and text[idx + 1].isdigit():
            if int(text[idx + 1]) == int(text[idx]) + 1:
                count += 1
        idx += 1
    return count


if __name__ == "__main__":
    tests = [
        "123",
        "12a34",
        "987654321",
        "01234567",
        "abc",
        "1a2b3c4",
        "112233"
    ]
    for test in tests:
        print(f"{test} --> {pattern_tracker(test)}")
# Write a function that returns a string with the characters that appear
# in both strings, without repetitions. Characters are added in the order
# they appear in the first string.

def inter(s1: str, s2: str) -> str:
    res: str = ""
    for c in s1:
        if c in s2 and c not in res:
            res += c
    return res


if __name__ == "__main__":
    tests = [
        ("hello", "world"),
        ("banana", "band"),
        ("abcabc", "bc"),
        ("abc", "xyz"),
        ("", "abc")
    ]

    for test in tests:
        print(f'Case inter: "{inter(*test)}"')

        
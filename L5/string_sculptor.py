# Write a function that transforms a string by alternating the case of
# alphabetic characters only.
# Non-alphabetic characters remain unchanged and are NOT counted in the
# alternation index.
# The first alphabetic character should be lowercase, the second uppercase, etc.
# Spaces reset the alternation (next alpha after a space is lowercase again).

def string_sculptor(text: str) -> str:
    idx: int = 0
    res: str = ""
    next_up: bool = False

    if not text:
        return res
    while idx < len(text):
        if text[idx].isalpha():
            if idx == 0 or text[idx - 1].isspace():
                res += text[idx].lower()
                next_up = True
            elif next_up:
                res += text[idx].upper()
                next_up = False
            else:
                res += text[idx].lower()
                next_up = True
        else:
            res += text[idx]
        idx += 1
            
    return res


if __name__ == "__main__":
    tests = [
        "hello",
        "Hello World",
        "abc123def",
        "Python3.9!"
    ]

    for test in tests:
        print(f"{test} --> {string_sculptor(test)}")
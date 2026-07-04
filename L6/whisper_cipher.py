# Write a function that creates a Caesar cipher by shifting letters in a
# string by a given amount.
# Non-alphabetic characters should remain unchanged.
# The shift can be negative (shift left).

def whisper_cipher(text: str, shift: int) -> str:
    cipher = ""
    low = "abcdefghijklmnopqrstuvwxyz"
    high = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not text or shift == 0:
        return text


    for c in text:
        if c.isalpha():
            if c.islower():
                idx = (low.index(c) + shift) % len(low)
                cipher += low[idx]
            elif c.isupper():
                idx = (high.index(c) + shift) % len(low)
                cipher += high[idx]
        else:
            cipher += c
    
    return cipher


if __name__ == "__main__":
    tests = [
        ("hello", 3),
        ("Hello World!", 1),
        ("xyz", 3),
        ("ABC123def", 5),
        ("", 10),
        ("abc", -3)
    ]

    for test in tests:
        text, shift = test
        print(f"{text} ===>> {whisper_cipher(text, shift)}")
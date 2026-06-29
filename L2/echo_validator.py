# Write a function that checks if a string is a palindrome,
# ignoring spaces and case, only consider alphabetic characters
# for the comparison.

def echo_validator(text: str) -> bool:
    l_str = text.lower().strip()
    for i in range(len(l_str)):
        for j in range(len(l_str) - 1, 0, -1):
            return l_str[i] == l_str[j]


if __name__ == "__main__":
    strings = ["racecar", "A man a plan a canal Panama",
            "race a car", "hello", "Madam Im Adam", ""]
    
    for string in strings:
        print(f"str: {string} - {echo_validator(string)}")
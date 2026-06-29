
# Write a function that checks if the brackets in a string are valid.
# A string is valid if every opening bracket has a matching closing bracket
# in the correct order.
# Allowed brackets: (), [], {}

def bracket_validator(s: str) -> bool:
    str: list = []
    for char in s:
        if char == '(' or char == '[' or char == '{':
            str.append(char)
        if char == ')' or char == ']' or char == '}':
            if not str:
                return False
            if ((char == ')' and str[-1] != '(') or (char == ']'
                                                     and str[-1] != '[')
                                                     or
                                                     (char == '}' and
                                                      str[-1] != '{')):
                return False
            str.pop()
    return not str


if __name__ == "__main__":
    str_to_check: list[str] = ["()", "()[]{}", "(]", "([)]",
                               "hello(world)", "{[]}", "((())",
                               ""]
    for s in str_to_check:
        print(f"str: {s} - {bracket_validator(s)}")

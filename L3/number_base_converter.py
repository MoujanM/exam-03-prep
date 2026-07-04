# Write a function that converts a number from one base to another.
# Support bases from 2 to 36 inclusive.
# Use digits 0-9 and letters A-Z for values 10-35.
# Return "ERROR" for invalid inputs.

def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if (from_base < 2 or to_base < 2) or (from_base > 36 or to_base > 36):
        return "ERROR"

    ref_str: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    num: int = 0
    new_num_d: list[str] = []

    # convert number str to num int
    for c in number:
        c_val = ref_str.index(c)
        if c_val >= from_base:
            return "ERROR"
        num = num * from_base + c_val
    
    # convert num int to new base
    while num > 0:
        rm = num % to_base
        new_num_d.append(ref_str[rm])
        num //= to_base
    new_num_d.reverse()
    return ''.join(new_num_d)

if __name__ == "__main__":
    tests = [
        ("1010", 2, 10),
        ("FF", 16, 10),
        ("255", 10, 16),
        ("123", 10, 2),
        ("Z", 36, 10),
        ("35", 10, 36),
        ("123", 1, 10),
        ("G", 16, 10)
    ]

    for test in tests:
        print(f"{test[0]} in base {test[1]} is {number_base_converter(*test)} in base {test[2]}")
        


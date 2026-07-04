# Write a function that rotates an array to the right by k positions.
# Rotating right by k means the last k elements move to the front.

def twist_sequence(arr: list[int], k: int) -> list[int]:

    if k == 0 or k == len(arr) or not arr:
        return arr

    if k > len(arr):
        k %= len(arr)
    
    res: list[int] = []
    res = arr[-k:] + arr[:-k]

    return res

if __name__ == "__main__":
    tests = [
        ([1,2,3,4,5], 2),
        ([1,2,3], 1),
        ([1,2,3,4], 0),
        ([1,2,3], 5),
        ([], 3)
    ]

    for test in tests:
        arr, k = test
        print(f"{test} -->> {twist_sequence(arr, k)}")


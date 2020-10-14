"""

    Completed on: 14/10/2020
    Difficulty: Easy

"""


def equalizeArray(arr):
    freq = {}
    length = len(arr)

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    maximum = max(freq.values())
    return length - maximum


def main():
    arr = [3, 3, 2, 1, 3]
    print(equalizeArray(arr))


if __name__ == "__main__":
    main()

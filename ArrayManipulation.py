"""


"""


import collections


def arrayManipulation(n, queries):
    operations = collections.defaultdict(int)

    for a, b, k in queries:
        operations[a - 1] += k
        operations[b] -= k
    current_sum = max_sum = 0

    for index in sorted(operations):
        current_sum += operations[index]
        max_sum = max(max_sum, current_sum)

    return max_sum


def main():
    n = 5
    q = [
        [1, 2, 100],
        [2, 5, 100],
        [3, 4, 100]
    ]

    print(arrayManipulation(n, q))

    n = 10

    q = [
        [2, 6, 8],
        [3, 5, 7],
        [1, 8, 1],
        [5, 9, 15]
    ]

    print(arrayManipulation(n, q))


if __name__ == "__main__":
    main()

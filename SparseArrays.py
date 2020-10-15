"""

    Completed: 15/10/2020
    Difficulty: Medium
    Url: https://www.hackerrank.com/challenges/sparse-arrays/problem

"""


def sparseArrays(strings, queries):
    freqs = {}
    results = []

    for s in strings:
        if s in freqs:
            freqs[s] += 1
        else:
            freqs[s] = 1

    for q in queries:
        if q in freqs:
            results.append(freqs[q])
        else:
            results.append(0)

    return results


def main():
    s = [
        'aba',
        'baba',
        'aba',
        'xzxb'
    ]

    q = [
        'aba',
        'xzxb',
        'ab'
    ]

    print(sparseArrays(s, q))


if __name__ == "__main__":
    main()

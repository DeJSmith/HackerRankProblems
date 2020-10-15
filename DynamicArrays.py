"""
    Completed: 15/10/2020
    Difficulty: Easy
    Url: https://www.hackerrank.com/challenges/dynamic-array/problem

"""


def dynamicArray(n, queries):
    seqList = [[] for _ in range(n)]
    lastAnswer = 0
    lastAnswers = []

    for q in queries:
        if q[0] == 1:
            seq = (q[1] ^ lastAnswer) % n
            seqList[seq].append(q[2])
        elif q[0] == 2:
            seq = (q[1] ^ lastAnswer) % n
            index = q[2] % len(seqList[seq])
            lastAnswer = seqList[seq][index]
            lastAnswers.append(lastAnswer)

    return lastAnswers


def main():
    n = 2
    q = [
        [1, 0, 5],
        [1, 1, 7],
        [1, 0, 3],
        [2, 1, 0],
        [2, 1, 1]
    ]
    print(dynamicArray(n, q))


if __name__ == "__main__":
    main()

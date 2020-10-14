"""

    Completed on 14/10/2020
    Difficulty: Easy
    Url: https://www.hackerrank.com/challenges/acm-icpc-team/problem

"""

from itertools import combinations


def acmTeam(topic):
    best = 0
    count = 0

    teamList = sorted(map(sorted, combinations(set(topic), 2)))

    for pair in teamList:
        total = calculateSkills(pair[0], pair[1])
        if total == best:
            count += 1
        if total > best:
            best = total
            count = 1
    return (best, count)


def calculateSkills(x, y):
    total = 0
    for i in range(len(x)):
        if x[i] == '1' or y[i] == '1':
            total += 1
    return total


def main():
    t = [
        "10101",
        "11100",
        "11010",
        "00101"
    ]
    print(acmTeam(t))


if __name__ == "__main__":
    main()

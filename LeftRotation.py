"""
    Completed: 15/10/2020
    Difficulty: Easy
    Url: https://www.hackerrank.com/challenges/array-left-rotation/problem

"""


def leftRoatation(d, arr):
    return arr[d:] + arr[:d]


def main():
    arr = [1, 2, 3, 4, 5]
    print(leftRoatation(4, arr))


if __name__ == "__main__":
    main()

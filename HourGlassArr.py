"""

    Completed on: 14/10/2020
    Difficulty: Easy
    Url: https://www.hackerrank.com/challenges/2d-array/problem
"""


def hourGlassArr(arr):
    rows = len(arr)
    cols = len(arr[0])
    maxHourGlass = -99999
    neighbours = [
        [0, 1],
        [0, 2],
        [1, 1],
        [2, 1],
        [2, 0],
        [2, 2]
    ]

    for row in range(rows):
        for col in range(cols):
            if row < 4 and col < 4:
                total = calculateTotal(arr, row, col, neighbours)
                if total > maxHourGlass:
                    maxHourGlass = total

    return maxHourGlass

def calculateTotal(arr, row, col, neighbours):
    total = arr[row][col]

    for neighbour in neighbours:
        total += arr[row + neighbour[0]][col + neighbour[1]]

    return total


def main():
    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    print(hourGlassArr(arr))

    arr = [
        [-1, -1, 0, -9, -2, -2],
[-2, -1, -6, -8, -2, -5],
[-1, -1, -1, -2, -3, -4],
[-1, -9, -2, -4, -4, -5],
[-7, -3, -3, -2, -9, -9],
[-1, -3, -1, -2, -4, -5],
    ]

    print(hourGlassArr(arr))

if __name__ == "__main__":
    main()
"""

    Completed 14/10/2020
    Difficulty: Medium

"""

import math


def encryption(s):
    s = s.replace(" ", "")
    rows = math.floor(math.sqrt(len(s)))
    cols = math.ceil(math.sqrt(len(s)))

    if ((rows * cols) < len(s)):
        rows = cols

    char_index = 0
    mat = [["'" for _ in range(cols)] for _ in range(rows)]
    encrypted_message = ''

    #print("s: {}, rows: {}, cols: {}".format(len(s), rows, cols))
    # print(mat)

    for row in range(rows):
        for col in range(cols):
            if char_index < len(s):
                mat[row][col] = s[char_index]
                char_index += 1

    # print(mat)

    for col in range(cols):
        mes = ' '
        for row in range(rows):
            mes += mat[row][col]
        encrypted_message += mes

    encrypted_message = encrypted_message.replace("'", "")

    # print(encrypted_message.strip())
    return encrypted_message.strip()


def main():
    print(encryption("have a nice day"))


if __name__ == '__main__':
    main()

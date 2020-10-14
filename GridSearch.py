"""

    Completed on 14/10/202
    Difficulty: Medium
    Url: https://www.hackerrank.com/challenges/the-grid-search/problem

"""


def gridSearch(G, P):
    g_row = len(G)
    g_col = len(G[0])
    p_row = len(P) - 1
    p_col = len(P[0]) - 1
    res = False

    print()

    top_left = P[0][0]
    bottom_right = P[p_row][p_col]

    print(top_left)
    print(bottom_right)

    for row in range(g_row):
        for col in range(g_col):
            if G[row][col] == top_left:
                if checkBounds((g_row, g_col), (row+p_row, col+p_col)):
                    if G[row+p_row][col+p_col] == bottom_right:
                        print(" top left: {} and bottom right matched: {}".format(
                            (G[row][col]), (G[row+p_row][col+p_col])))
                        res = searchWithin(G, P, row, col)
                        if res:
                            return 'YES'

    return 'NO'


def searchWithin(G, P, row, col):
    start_col = col
    for p_r in range(len(P)):
        for p_c in range(len(P[0])):
            print('row: {}, col: {}'.format(row, col))
            print(G[row])
            print("{} ?= {}".format(P[p_r][p_c], G[row][col:]))
            if P[p_r][p_c] == G[row][col]:
                print("{} == {}".format(P[p_r][p_c], G[row][col]))
                col += 1
            else:
                return False
        row += 1
        col = start_col

    return True


def checkBounds(graph_dimensions, target_coordinates):
    print("bounds: {}, target: {}".format(
        graph_dimensions, target_coordinates))
    if target_coordinates[0] >= graph_dimensions[0] or target_coordinates[0] < 0:
        return False
    if target_coordinates[1] >= graph_dimensions[1] or target_coordinates[1] < 0:
        return False

    return True


def main():
    G = [
        "7283455864",
        "6731158619",
        "8988242643",
        "3830589324",
        "2229505813",
        "5633845374",
        "6473530293",
        "7053106601",
        "0834282956",
        "4607924137"]

    P = [
        "9505",
        "3845",
        "3530"
    ]

    print(gridSearch(G, P))

    G = [
        "400453592126560",
        "114213133098692",
        "474386082879648",
        "522356951189169",
        "887109450487496",
        "252802633388782",
        "502771484966748",
        "075975207693780",
        "511799789562806",
        "404007454272504",
        "549043809916080",
        "962410809534811",
        "445893523733475",
        "768705303214174",
        "650629270887160",
    ]

    P = [
        "99",
        "99"
    ]

    print(gridSearch(G, P))

    G = [
        "7652157548860692421022503",
        "9283597467877865303553675",
        "4160389485250089289309493",
        "2583470721457150497569300",
        "3220130778636571709490905",
        "3588873017660047694725749",
        "9288991387848870159567061",
        "4840101673383478700737237",
        "8430916536880190158229898",
        "8986106490042260460547150",
        "2591460395957631878779378",
        "1816190871689680423501920",
        "0704047294563387014281341",
        "8544774664056811258209321",
        "9609294756392563447060526",
        "0170173859593369054590795",
        "6088985673796975810221577",
        "7738800757919472437622349",
        "5474120045253009653348388",
        "3930491401877849249410013",
        "1486477041403746396925337",
        "2955579022827592919878713",
        "2625547961868100985291514",
        "3673299809851325174555652",
        "4533398973801647859680907"
    ]

    P = [
        "5250",
        "1457",
        "8636",
        "7660",
        "7848"
    ]

    print(gridSearch(G, P))

    G = [
        "123412",
        "561212",
        "123634",
        "781288"
    ]

    P = [
        '12',
        '34'
    ]

    print(gridSearch(G, P))


if __name__ == "__main__":
    main()

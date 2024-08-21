def snail(snail_map):
    n = len(snail_map[0])
    total = n*n
    count = 0
    result = []
    right_board = 0
    left_board = 0
    while count != total:
        for i in range(n):
            result.append(snail_map[right_board][left_board])
            left_board += 1
            count += 1
        n -= 1
        left_board -= 1
        right_board += 1

        for i in range(n):
            result.append(snail_map[right_board][left_board])
            right_board += 1
            count += 1
        left_board -= 1
        right_board -= 1

        for i in range(n):
            result.append(snail_map[right_board][left_board])
            left_board -= 1
            count += 1
        left_board += 1
        right_board -= 1
        n -= 1

        for i in range(n):
            result.append(snail_map[right_board][left_board])
            right_board -= 1
            count += 1
        left_board += 1
        right_board += 1

    return result


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(snail(array))

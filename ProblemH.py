def get_board(matrix):
    board = []
    n = len(matrix)
    m = len(matrix[0])
    # Put a "9" at the positions with a cheesy bread and "0" at the other ones
    for i in range(n):
        board.append([])
        for j in range(m):
            if matrix[i][j] == "1":
                board[i].append(9)
            else:
                board[i].append(0)

    for i in range(n):
        string_row = ""
        for j in range(m):
            if board[i][j] == 0:
                number_cheesy_breads = 0
                # Checks if there is a cheesy bread at the position on the left
                if (i - 1 >= 0) and (board[i-1][j] == 9):
                    number_cheesy_breads += 1
                # Checks if there is a cheesy bread at the position above
                if (j - 1 >= 0) and (board[i][j-1] == 9):
                    number_cheesy_breads += 1
                # Checks if there is a cheesy bread at the position on the right
                if (i + 1 < n) and (board[i+1][j] == 9):
                    number_cheesy_breads += 1
                # Checks if there is a cheesy bread at the position below
                if (j + 1 < m) and (board[i][j+1] == 9):
                    number_cheesy_breads += 1
                # Replace the current position of the board with number_cheesy_breads
                board[i][j] = number_cheesy_breads
            # Append the string representing this row
            string_row += str(board[i][j])
        # Print line in the output
        print(string_row)


while True:
    try:
        # Reading input
        list_inputs = input().split()
        while len(list_inputs) > 0:

            n = int(list_inputs[0])
            m = int(list_inputs[1])
            matrix = []
            for i in range(n):
                matrix.append(input().split())
            get_board(matrix)
            list_inputs = input().split()
    except EOFError:
        break


def isValidSudoku(self, board):
        # create the rows, cols, and squares to keep track of
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        # loop over each value
        for r in range(9):
            for c in range(9):
                # skip the empty squares
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[r // 3][ c // 3]):
                    # if it breaks any of the rules its not valid
                    return False
                
                # add the value to everything to keep track
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r // 3][ c // 3].add(board[r][c])

        return True
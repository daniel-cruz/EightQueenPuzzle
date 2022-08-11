# Base on https://github.com/sol-prog/N-Queens-Puzzle


class Queens:
    def __init__(self, N):
        self.size = N
        self.board = [-1] * self.size
        self.nSolutions = 0
        self.solutions = []
        self.solve(0)

    def solve(self, n):
        if n < self.size:
            for column in range(self.size):
                if self.verify(n, column):
                    self.board[n] = column
                    self.solve(n + 1)
        else:
            self.nSolutions += 1
            self.solutions.append(self.board)

    def verify(self, rows, column):
        for row in range(rows):
            if (
                self.board[row] == column
                or ((self.board[row] - row) == (column - rows))
                or ((self.board[row] + row) == (column + rows))
            ):
                return False
        return True

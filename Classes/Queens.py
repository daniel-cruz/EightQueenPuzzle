# Base on https://github.com/sol-prog/N-Queens-Puzzle


class Queens:
    def __init__(self, N):
        self.size = N
        self.board = [-1] * self.size
        self.solutions = 0
        self.solve(0)

    def solve(self, row):
        if row < self.size:
            for column in range(self.size):
                if self.verify(row, column):
                    self.board[row] = column
                    self.solve(row + 1)
        else:
            self.solutions += 1

    def verify(self, row, column):
        for cell in range(row):
            if (
                self.board[cell] == column
                or self.board[cell] - cell == column - row
                or self.board[cell] + cell == column + row
            ):
                return False
        return True

    def display(self):
        htmlString = "<div class='col-xs-1 col-sm-4'><table class='board'>"
        for row in range(self.size):
            htmlString += "<tr>"
            for col in range(self.size):
                htmlString += "<td>"
                if self.board[row] == col:
                    htmlString += "Q"
                else:
                    htmlString += " "
                htmlString += "</td>"
            htmlString += "</tr>"
        htmlString += "</table></div>"
        return htmlString

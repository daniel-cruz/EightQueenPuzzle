class Queens:

	def __init__(self,N):
		self.size = N
		self.board = [-1] * self.size
		self.solutions = 0
		self.solve()

	def solve(self):
		self.set(0)

	def set(self,row):
		if row < self.size:
			for column in range(self.size):
				if self.verify(row,column):
					self.board[row] = column
					self.set(row+1)
		else:
			self.solutions += 1
			#self.display()


	def verify(self,row,column): 
		for cell in range(row): 
			if self.board[cell] == column or self.board[cell] - cell == column - row or self.board[cell] + cell == column + row:
				return False
		return True

	def display(self):
		print("Solution " + str(self.solutions) + ": ")
		for row in range(self.size):
			for col in range(self.size):
				if self.board[row]==col:
					print("Q",end=" ")
				else:
					print("*",end = " ")
			print("\n")
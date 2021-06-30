from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

import json
import os

Base = declarative_base()

class Solution(Base):
    __tablename__ = os.environ['DATABASE_TABLE']
    id = Column(Integer, primary_key=True)
    n = Column(Integer)
    solution = Column(String)
    
    def __repr__(self):
        return "<Solutions(n='{}', solution={})>"\
                .format(self.n, self.solution)

				
class Queens:

	def __init__(self,N):
		self.size = N
		self.board = [-1] * self.size
		self.solutions = 0
		self.solve(0)

	def solve(self,row):
		if row < self.size:
			for column in range(self.size):
				if self.verify(row,column):
					self.board[row] = column
					self.solve(row+1)
		else:
			self.record()
			self.solutions += 1


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
	
	def record(self):
		engine = create_engine(os.environ['DATABASE_URI'])

		Base.metadata.create_all(engine)

		Session = sessionmaker(bind=engine)
		s = Session()

		solution = Solution(
			n=self.size,
			solution=json.dumps(self.board)
		)

		s.add(solution)
		s.commit()
		s.close()
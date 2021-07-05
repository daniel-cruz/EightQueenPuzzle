from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from Classes.Queens import Queens

import json
import os

Base = declarative_base()


class SolutionModel(Base):
    __tablename__ = "solutions"
    id = Column(Integer, primary_key=True)
    n = Column(Integer)
    solution = Column(String)

    def __repr__(self):
        return "<Solutions(n='{}', solution={})>".format(self.n, self.solution)


class Solution(Queens):

    engine = create_engine(os.environ["DATABASE_URI"])

    def __init__(self, n):
        Queens.__init__(self, n)
        Base.metadata.create_all(self.engine)

    def record(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        record = SolutionModel(n=self.size, solution=json.dumps(self.board))
        session.add(record)
        session.commit()
        session.close()
        return self

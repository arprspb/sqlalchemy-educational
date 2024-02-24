from asyncio import FastChildWatcher
from sqlalchemy import Column, ForeignKey, Integer, String
from models.base import TimeStampedModel


class User(TimeStampedModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(String(320), nullable=False, unique = True)


    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.first_name} {self.last_name}"
    

class Preference(TimeStampedModel):
    __tablename__ = "preferences"

    id = Column(Integer, primary_key=True, autoincrement=True)
    language = Column(String(80), nullable=False)
    currency = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True, unique=True)
from datetime import datetime
from sqlite3 import Date
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_base
from main import session

Model = declarative_base()
Model.query = session.query_property()

class TimeStampedModel(Model):
    __abstract__ = True
    created_at = Column(DateTime, default = datetime.utcnow())
    updated_at = Column(DateTime, onupdate =  datetime.utcnow())
    
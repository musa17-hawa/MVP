from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

#TABLE INFORMATION ARE PLACED HERE.
class Contact (Base):
	__tablename__ = 'contact'
	id = Column(Integer, primary_key=True)


class Item (Base):
	__tablename__ = 'item'
	id = Column(Integer, primary_key=True)
	itmname = Column(String(150))
	itmprice = Column(String(100))
	itmpic = Column(String(300))
	itmdis = Column(String(400))




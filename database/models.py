from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key = True)
    connection_date = Column(DateTime, default=datetime.now, nullable = false)
    tg_id = Column(BigInteger, nullable = False)
    city = Column(String)
    reports = relationship('weatherReport', backref='report', lazy = True, cascade = 'all, delete-orphan')
    
    def __repr__(self):
        return self.tg_id

class Book(Base):
    __tablename__ = 'WeatherReports'
    id = Column(Integer, primary_key = True)
    owner = Column(Integer, ForeignKey('Users.id'), nullabel = False)
    date = Column(DateTime, Default = datetime.now, nullable = False)
    temp = Column(Integer, nullable = False)
    feels_like = Column(Integer, nullable = False)
    wind_speed = Column(Integer, nullable = False)
    pressure_mm = Column(Integer, nullable = False)
    city = Column(String, nullable = False)
    def __repr__(self):
        return self.city

class Reviews(Base):
    __tablename__ = 'reviews'
    id = Column (Integer, primary_key = True)
    text = Column(String(2000), nullable = False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable = False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
    
    def __repr__(self):
        return f'От {self.reviewer}'
    

    
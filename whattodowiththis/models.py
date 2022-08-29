import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, backref

from sqlalchemy import create_engine, Column, String, Integer, Date, Table, ForeignKey, Boolean, Time

Base = declarative_base()

connection_string = 'postgresql://postgres:1234@localhost:5432/buzz'
engine = create_engine(connection_string, pool_pre_ping=True)
Session = sessionmaker(bind=engine)


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = sa.Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)

    def __init__(self, name):
        self.name = name


class Orders(Base):
    __tablename__ = 'orders'

    event_id = sa.Column(Integer, primary_key=True, autoincrement=True)
    rest_id = sa.Column(Integer, sa.ForeignKey('restaurant.id', ondelete='CASCADE'))
    order_time = sa.Column(Time, nullable=False)
    finish_time = sa.Column(Time, nullable=False)

    restaurant = relationship('Restaurant', backref = 'orders')

    def __init__(self, rest_id, order_time, finish_time):
        self.rest_id = rest_id
        self.order_time = order_time
        self.finish_time = finish_time

Base.metadata.create_all(engine)

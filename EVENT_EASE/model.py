from sqlalchemy import Column, Integer, String, Float, ForeignKey
from pydantic import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base



Base = declarative_base()

class events(Base):
    __tablename__ = 'events'
    event_id=Column(Integer, primary_key=True,autoincrement=True)
    event_name=Column(String())
    date=Column(String())
    information=Column(String())
    price =Column(Float())
    status=Column(String())
    location=Column(String())
    organizator_id=Column(Integer,ForeignKey('organizator.organizator_id'))

    organizator = relationship ("organizator",back_populates="events")

class eventsPydantic(BaseModel):  # sqlalchemy modeline göre pydantic modelini olusturdu.gelen ve giden verileri doğrulama ve dönüştürmek için kullandık
    event_id: int
    event_name: str
    date: str
    information: str
    price: float
    status: str
    location: str
    organizator_id: int

class user(Base):
        __tablename__ = 'user'
        user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        user_mail = Column(String())
        user_name = Column(String())
        user_password = Column(String())
        user_xp = Column(Integer())

class userPydantic(BaseModel):  # sqlalchemy modeline göre pydantic modelini olusturdu.gelen ve giden verileri doğrulama ve dönüştürmek için kullandık
        user_id: int
        user_mail: str
        user_name: str
        user_password: str
        user_xp: int

class organizator(Base):
        __tablename__ = 'organizator'
        organizator_id = Column(Integer, primary_key=True, autoincrement=True)
        user_id = Column(Integer(), ForeignKey('user.user_id'))
        user_name = Column(String() )  #,ForeignKey('user.user_name'))

        user = relationship("user", back_populates="organizator")

class organizatorPydantic(BaseModel):  # sqlalchemy modeline göre pydantic modelini olusturdu.gelen ve giden verileri doğrulama ve dönüştürmek için kullandık
        organizator_id: int
        user_id: int
        user_name: str


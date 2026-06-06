from sqlalchemy import Column, Integer, String, Float, JSON, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Kindergarten(Base):
    __tablename__ = "kindergartens"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, index=True)
    region = Column(String)
    district = Column(String)
    type = Column(String)
    programs = Column(JSON)
    languages = Column(JSON)
    price = Column(Integer)
    rating = Column(Float, default=0.0)
    image = Column(String)
    short_description = Column(String)

    location_address = Column(String)
    phone = Column(String)
    ages = Column(String)
    capacity = Column(Integer)
    hours = Column(JSON)
    features = Column(JSON)
    gallery = Column(JSON)
    full_description = Column(String)


    reviews = relationship("Review", back_populates="kindergarten", cascade="all, delete")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    kindergarten_id = Column(Integer, ForeignKey("kindergartens.id"))
    name = Column(String)
    text = Column(String)
    rating = Column(Float)

    kindergarten = relationship("Kindergarten", back_populates="reviews")
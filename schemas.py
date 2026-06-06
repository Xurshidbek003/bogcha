from pydantic import BaseModel
from typing import List, Optional

class WorkingHour(BaseModel):
    day: str
    time: str

class ReviewBase(BaseModel):
    name: str
    text: str
    rating: float

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    class Config:
        from_attributes = True


class KindergartenBase(BaseModel):
    name: str
    region: str
    district: str
    type: str
    programs: List[str] = []
    languages: List[str] = []
    price: int
    rating: float = 0.0
    image: str
    short_description: str
    location_address: str
    phone: str
    ages: str
    capacity: int
    hours: List[WorkingHour] = []
    features: List[str] = []
    gallery: List[str] = []
    full_description: str


class KindergartenCreate(KindergartenBase):
    pass


class KindergartenUpdate(BaseModel):
    name: Optional[str] = None
    region: Optional[str] = None
    district: Optional[str] = None
    type: Optional[str] = None
    programs: Optional[List[str]] = None
    languages: Optional[List[str]] = None
    price: Optional[int] = None
    image: Optional[str] = None
    short_description: Optional[str] = None
    location_address: Optional[str] = None
    phone: Optional[str] = None
    ages: Optional[str] = None
    capacity: Optional[int] = None
    hours: Optional[List[WorkingHour]] = None
    features: Optional[List[str]] = None
    gallery: Optional[List[str]] = None
    full_description: Optional[str] = None


class Kindergarten(KindergartenBase):
    id: int
    reviews: List[Review] = []

    class Config:
        from_attributes = True
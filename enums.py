from enum import Enum


class BookingMethod(str, Enum):
    upi = "upi"
    cash = "cash"
    card = "card"
    giftcard = "giftcard"


class BookingStatus(str, Enum):
    active = "active"
    failed = "failed"
    pending = "pending"
    cancelled = "cancelled"


class Gender(str, Enum):
    male = "male"
    female = "female"
    transgender = "transgender"


class Rating(int, Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5


class Category(str, Enum):
    hotel = "hotel"
    flight = "flight"
    cruise = "cruise"
    package = "package"


class Season(str, Enum):
    rainy = "Rainy"
    snow = "Snow"
    summer = "Summer"
    spring = "Spring"
    winter = "Winter"


class RoomCategory(str, Enum):
    silver = "silver"
    gold = "gold"
    diamond = "diamond"
    platinum = "platinum"


class HotelAmenties(str, Enum):
    pool = "pool"
    hot_water = "hot-water"


class FlightClass(str, Enum):
    economy = "economy"
    business = "business"
    first_class = "first-class"


class PackageLocation(str, Enum):
    domestic = "Domestic"
    international = "International"
    offer = "Offer"


class PackageActivities(str, Enum):
    water = "water"
    air = "air"
    none = "none"

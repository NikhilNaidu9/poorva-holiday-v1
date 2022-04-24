from datetime import date, datetime
from typing import Any, List, Optional

from pydantic import BaseModel

import enums as e


class Availabilty(BaseModel):
    start_date: date
    end_date: date


class HotelRoom(BaseModel):
    room_category: e.RoomCategory
    room_price: int
    room_bed_category: str
    room_beds: int
    room_area: int
    room_breakfast: bool
    room_lunch: bool
    room_dinner: bool
    room_recommended: bool
    room_gallery_link: List[str]
    room_amenties: List[str]
    room_availability: Availabilty


class HotelOffer(BaseModel):
    start_date: date
    end_date: date


# governemnet id,
class GuestDetail(BaseModel):
    guest_name: str
    guest_age: int
    guest_adult: bool
    guest_gender: e.Gender
    guest_requirement: List[str]


class Booking(BaseModel):
    booking_payment_status: str
    booking_date: date
    booking_rate: int
    booking_user_id: str
    booking_package_id: str
    booking_method: e.BookingMethod
    booking_status: e.BookingStatus
    booking_guest_details: List[dict]

    class Config:
        use_enum_values = True


class Landmark(BaseModel):
    name: str
    city: str
    gallery_link: List[str]


class Review(BaseModel):
    user_name: str
    user_id: str
    review: str


class Hotel(BaseModel):
    hotel_id: str
    hotel_name: str
    hotel_info: str
    hotel_brand: str
    hotel_city: str
    hotel_country: str
    hotel_address: str
    hotel_rating: e.Rating
    hotel_check_in_time: str
    hotel_check_out_time: str
    hotel_thumbnail_link: str
    hotel_privacy_policy: str
    hotel_review: List[str]
    hotel_couple_friendly: bool
    hotel_rooms: List[str]
    hotel_offer: List[str]
    hotel_gallery_link: List[str]
    hotel_cancellation_terms: str
    hotel_landmarks: List[str]
    hotel_transport_availability: bool
    hotel_availability: List[str]
    hotel_amenities: List[e.HotelAmenties]

    class Config:
        use_enum_values = True


class Flight(BaseModel):
    flight_name: str
    flight_airlines: str
    flight_duration: str
    flight_no_of_stop: int
    flight_class: e.FlightClass
    flight_source_airport: str
    flight_destination_airport: str
    flight_arrival_time: datetime
    flight_departure_time: datetime


class Cruise(BaseModel):
    cruise_name: str
    cruise_company: str
    cruise_duration: str
    cruise_no_of_stop: int
    cruise_source_port: str
    cruise_destination_port: str
    cruise_arrival_time: datetime
    cruise_departure_time: datetime


class BankDetails(BaseModel):
    bank_name: str
    bank_account_number: str
    bank_ifsc_code: str
    bank_card_number: int
    bank_cvv: int


class ItenaryExclusion(BaseModel):
    id: str
    exclusion: str
    reason: str
    availability: Availabilty


class DayActivity(BaseModel):
    day_activity_id: str
    date: date
    day: int
    plan: List[dict]
    title: str
    attraction: str
    note: str


class Itenary(BaseModel):
    itenary_id: str
    day_activites: Optional[List[str]]
    itenary_inclusion: Optional[List[str]]
    itenary_exclusion: Optional[List[str]]


class Offer(BaseModel):
    offer_name: str
    offer_percentage: int
    offer_availability: Availabilty


class Cost(BaseModel):
    cost_id: str
    cost_plan: List[dict]


# international or domestic, activites
class Package(BaseModel):
    package_id: str
    package_title: str
    package_city: str
    package_info: str
    package_lister: str
    package_country: str
    package_total_days: int
    package_total_night: int
    package_start_date: date
    package_end_date: date
    package_offers: List[str]
    package_theme: List[str]
    package_season: e.Season
    package_thumbail_link: str
    package_average_rating: int
    package_rate_per_person: int
    package_itenary: str
    package_gallery_link: List[str]
    package_cancellation_policy: List[str]
    package_location: e.PackageLocation
    package_hotel: Optional[List[str]]
    package_flight: Optional[List[str]]
    package_cruise: Optional[List[str]]
    package_activities: List[e.PackageActivities]
    package_availability: Optional[List[str]]
    package_cost: str
    package_status: str
    package_stay: List[dict]


class Favourites(BaseModel):
    hotels: List[Hotel]
    packages: List[Package]


class GovernmentID(BaseModel):
    aadhaar_card_number: Optional[str]
    pan_card_number: Optional[str]
    driving_license_number: Optional[str]
    passport_number: Optional[str]


class User(BaseModel):
    user_name: str
    user_id: str
    user_email: str
    user_phone: str
    user_age: str
    user_city: str
    user_dob: date
    user_country: str
    user_gender: e.Gender
    user_profile_pic_link: str
    user_trips: Optional[List[str]]
    user_government_id: Optional[GovernmentID]
    user_favourites: Optional[List[Favourites]]
    user_bank_details: Optional[List[BankDetails]]

    class Config:
        use_enum_values = True


class Contact(BaseModel):
    name: str
    location: str
    phone_number: int
    email_address: str


class About(BaseModel):
    name: str
    description: str
    gallery_link: Optional[List[str]]


class FAQ(BaseModel):
    question: str
    answer: str
    category: e.Category


class Term(BaseModel):
    name: str
    value: str


class Theme(BaseModel):
    fgcolor: str
    bgcolor: str


class Config(BaseModel):
    theme: Theme
    faq: List[FAQ]
    terms: List[Term]
    about_us: List[About]
    contact_us: List[Contact]


class Content(BaseModel):
    category: str
    data: Any


class PaymentOrder(BaseModel):
    amount: int
    currency: str


class PaymentVerification(BaseModel):
    orderid: str
    razorpay_payment_id: str
    razorpay_signature: str


class Newsletter(BaseModel):
    id: str
    email: str


class Service(BaseModel):
    name: str
    image_link: str
    description: str


class Contact(BaseModel):
    name: str
    email_id: str
    phone_number: int
    location: str
    message: str


class Review(BaseModel):
    name: str
    profile: str
    rating: int
    description: str


class Order(BaseModel):
    package_id: str
    cost: List[int]
    booking_id: str


class Session(BaseModel):
    session_id: str
    order_id: str
    package_id: str
    total_price: str


class Update(BaseModel):
    key: str
    value: Any


class Invoice(BaseModel):
    invoice_id: str
    user_name: str
    package_title: str
    booking_date: str
    no_of_guests: int
    payment_status: str
    package_price: int


class Authentication(BaseModel):
    user_name: str
    password: str


class Staff(BaseModel):
    staff_name: str
    staff_id: str
    staff_password: str
    staff_role: str
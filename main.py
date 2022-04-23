from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from router.activity import activity as activity
from router.booking import booking as booking
from router.config import config as config
from router.content import content as content
from router.cost import cost as cost
from router.cruise import cruise as cruise
from router.flight import flight as flight
from router.hotels import hotels as hotel
from router.itenary import itenary as itenary
from router.packages import packages as package
from router.payment import payment as payment
from router.services import services as service
from router.users import users as user
from router.top import top as top
from router.newsletter import newsletter as newsletter
from router.about import about as about
from router.contact import contact as contact
from router.reviews import reviews as review
from router.files import files as file
from router.session import session as session
from router.upload import upload as upload
from router.invoice import invoice as invoice
from router.auth import auth as auth
from router.staff import router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(package.router)
app.include_router(hotel.router)
app.include_router(flight.router)
app.include_router(cruise.router)
app.include_router(content.router)
app.include_router(booking.router)
app.include_router(service.router)
app.include_router(config.router)
app.include_router(payment.router)
app.include_router(itenary.router)
app.include_router(activity.router)
app.include_router(cost.router)
app.include_router(top.router)
app.include_router(newsletter.router)
app.include_router(about.router)
app.include_router(contact.router)
app.include_router(review.router)
app.include_router(file.router)
app.include_router(session.router)
app.include_router(upload.router)
app.include_router(invoice.router)
app.include_router(auth.router)
app.include_router(router)

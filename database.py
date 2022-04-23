import pymysql
import pymysql.cursors

import json
import boto3

from decouple import config

import datetime

password = config('PASSWORD')

session = boto3.Session(
    aws_access_key_id=config("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"),
    region_name="ap-south-1",
)


def get_date_by_number_of_days(date, count):
    return datetime.date.today() - datetime.timedelta(days=count)


def manipulate_data(data):
    return json.dumps(data)


def manipulate_load(data):
    return json.loads(data)


def create_user(user):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute("INSERT INTO user VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (user.user_id, user.user_name, user.user_email, user.user_phone, user.user_age, user.user_city,  user.user_dob,  user.user_country,  user.user_gender, user.user_profile_pic_link))
        con.commit()

    # To close the connection
    con.close()
    return "user added"


def read_user(user_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("SELECT * FROM user WHERE user_id=%s", user_id)
        output = cur.fetchone()

        con.commit()

    # To close the connection
    con.close()
    return output


def update_user(user_id, update_key, update_value):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        query = f"UPDATE user SET {update_key}='{update_value}' WHERE user_id={user_id};"

        cur.execute(query)
        output = cur.fetchone()

        con.commit()

    # To close the connection
    con.close()
    return output


def delete_user(user_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("DELETE FROM user WHERE user_id=%s", user_id)
        con.commit()

    # To close the connection
    con.close()
    return "user deleted"


def create_package(trip):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute("INSERT INTO package VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (trip.package_id, trip.package_title, trip.package_city, trip.package_info, manipulate_data(trip.package_cancellation_policy), trip.package_lister, trip.package_country, trip.package_total_days, trip.package_total_night, trip.package_start_date, trip.package_end_date, manipulate_data(trip.package_offers), manipulate_data(trip.package_theme), trip.package_season, trip.package_thumbail_link, trip.package_average_rating, trip.package_rate_per_person, manipulate_data(trip.package_itenary), manipulate_data(trip.package_gallery_link), trip.package_location, manipulate_data(trip.package_hotel), manipulate_data(trip.package_flight), manipulate_data(trip.package_cruise), manipulate_data(trip.package_activities), manipulate_data(trip.package_availability), manipulate_data(trip.package_cost), trip.package_status, manipulate_data(trip.package_stay)))

        con.commit()

    # To close the connection
    con.close()
    return "package added"


def read_package(package_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute(
            "SELECT * FROM package INNER JOIN itenary ON package.package_itenary = itenary.itenary_id WHERE package.package_id = %s", package_id)
        output = cur.fetchone()

        con.commit()

    # To close the connection
    con.close()
    return output


def read_all_package():
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute(
            "SELECT * FROM package INNER JOIN itenary ON package.package_itenary = itenary.itenary_id;")
        output = cur.fetchall()

        con.commit()

    # To close the connection
    con.close()
    return output


def update_package(id, update_key, update_value):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        query = f"UPDATE package SET {update_key}='{update_value}' WHERE package_id='{id}';"

        cur.execute(query)
        con.commit()

    # To close the connection
    con.close()
    return "package updated"


def delete_package(package_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("DELETE FROM package WHERE package_id=%s", package_id)
        con.commit()

    # To close the connection
    con.close()
    return "package deleted"


def create_hotel(hotel):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute("INSERT INTO hotel VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (hotel.hotel_id, hotel.hotel_name, hotel.hotel_info, hotel.hotel_brand, hotel.hotel_city, hotel.hotel_country, hotel.hotel_address, hotel.hotel_rating, hotel.hotel_check_in_time, hotel.hotel_check_out_time, hotel.hotel_thumbnail_link, hotel.hotel_privacy_policy, manipulate_data(hotel.hotel_review), hotel.hotel_couple_friendly, manipulate_data(hotel.hotel_rooms), manipulate_data(hotel.hotel_offer), manipulate_data(hotel.hotel_gallery_link), hotel.hotel_cancellation_terms, manipulate_data(hotel.hotel_landmarks), hotel.hotel_transport_availability, manipulate_data(hotel.hotel_availability), manipulate_data(hotel.hotel_amenities)))

        con.commit()

    # To close the connection
    con.close()
    return "hotel added"


def read_hotel(hotel_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("SELECT * FROM hotel WHERE hotel_id=%s", hotel_id)
        output = cur.fetchone()

        con.commit()

    # To close the connection
    con.close()
    return output


def read_all_hotel():
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("SELECT * FROM hotel;")
        output = cur.fetchall()

        con.commit()

    # To close the connection
    con.close()
    return output


def update_hotel(id, update_key, update_value):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        query = f"UPDATE hotel SET {update_key}='{update_value}' WHERE hotel_id='{id}';"

        cur.execute(query)
        con.commit()

    # To close the connection
    con.close()
    return "hotel updated"


def delete_hotel(hotel_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("DELETE FROM hotel WHERE hotel_id=%s", hotel_id)
        con.commit()

    # To close the connection
    con.close()
    return "hotel deleted"


def create_booking(booking, booking_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute("INSERT INTO booking VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (booking_id, booking.booking_payment_status, booking.booking_date, booking.booking_rate, booking.booking_user_id, booking.booking_package_id, booking.booking_method, booking.booking_status, manipulate_data(booking.booking_guest_details)))

        con.commit()

    # To close the connection
    con.close()
    return "booking added"


def read_booking(user_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute(
            "SELECT * FROM booking INNER JOIN package ON booking.booking_package_id = package.package_id WHERE booking_user_id=%s", user_id)
        output = cur.fetchall()

        con.commit()

    # To close the connection
    con.close()
    return output


def connect_db():
    return pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)


def read_total_booking():
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    today_date = datetime.date.today()
    one_week_date_from_start = get_date_by_number_of_days(today_date, 7)
    one_month_date_from_start = get_date_by_number_of_days(today_date, 30)
    one_year_date_from_start = get_date_by_number_of_days(today_date, 365)

    data = {}

    with con.cursor() as cur:

        query = f"SELECT COUNT(booking_id) FROM booking INNER JOIN package ON booking.booking_package_id = package.package_id WHERE booking.booking_date BETWEEN %s AND %s;"

        cur.execute(query, (today_date, today_date))

        data["today_total_booking"] = cur.fetchall()[0]["COUNT(booking_id)"]

        cur.execute(query, (one_week_date_from_start, today_date))

        data["one_week_total_booking"] = cur.fetchall()[0]["COUNT(booking_id)"]

        cur.execute(query, (one_month_date_from_start, today_date))

        data["one_month_total_booking"] = cur.fetchall()[
            0]["COUNT(booking_id)"]

        cur.execute(query, (one_year_date_from_start, today_date))

        data["one_year_total_booking"] = cur.fetchall()[0]["COUNT(booking_id)"]

    # To close the connection
    con.close()
    return data


def read_total_package_booking():
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute(
            "SELECT package_id, package_title, package_start_date, package_end_date, package_rate_per_person, package_status FROM package", ())

        outputs = cur.fetchall()

        for out in outputs:

            cur.execute(
                "SELECT COUNT(booking_package_id) FROM booking WHERE booking_package_id=%s;", out["package_id"])

            output = cur.fetchall()[0]["COUNT(booking_package_id)"]

            out["booking_count"] = output

            if out["package_start_date"].month == datetime.datetime.now().month:
                out["priority"] = True
            else:
                out["priority"] = False

    # To close the connection
    con.close()
    return outputs


def read_booking_by_package_id(package_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute(
            "SELECT booking_id, booking_date, booking_status, booking_user_id, booking_method FROM booking WHERE booking_package_id=%s;", package_id)

        outputs = cur.fetchall()

    # To close the connection
    con.close()
    return outputs


def update_booking(id, update_key, update_value):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        query = f"UPDATE booking SET {update_key}='{update_value}' WHERE booking_id='{id}';"

        cur.execute(query)
        con.commit()

    # To close the connection
    con.close()
    return "booking updated"


def delete_booking(booking_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("DELETE FROM booking WHERE booking_id=%s", booking_id)
        con.commit()

    # To close the connection
    con.close()
    return "booking deleted"


def create_itenary(itenary):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute("INSERT INTO itenary VALUES(%s, %s, %s, %s)",
                    (itenary.itenary_id, manipulate_data(itenary.day_activites), manipulate_data(itenary.itenary_inclusion), manipulate_data(itenary.itenary_exclusion)))

        con.commit()

    # To close the connection
    con.close()
    return "itenary added"


def read_itenary(itenary_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("SELECT * FROM itenary WHERE itenary_id=%s", itenary_id)
        output = cur.fetchone()

        con.commit()

    # To close the connection
    con.close()
    return output


def read_all_itenary():
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("SELECT * FROM itenary;")
        output = cur.fetchall()
        print(output)

        con.commit()

    # To close the connection
    con.close()
    return output


def update_itenary(id, update_key, update_value):
    print(update_key)
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        query = f"UPDATE itenary SET {update_key}='{update_value}' WHERE itenary_id='{id}';"

        cur.execute(query)
        con.commit()

    # To close the connection
    con.close()
    return "itenary updated"


def delete_itenary(itenary_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("DELETE FROM itenary WHERE itenary_id=%s", itenary_id)
        con.commit()

    # To close the connection
    con.close()
    return "itenary deleted"


def create_activity(day_activity):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute("INSERT INTO dayitenary VALUES(%s, %s, %s, %s, %s, %s, %s)",
                    (day_activity.day_activity_id, day_activity.date, day_activity.day, manipulate_data(day_activity.plan), day_activity.title, day_activity.attraction, day_activity.note))

        con.commit()

    # To close the connection
    con.close()
    return "activity added"


def read_activity(day_activity_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute(
            "SELECT * FROM dayitenary WHERE day_activity_id=%s", day_activity_id)
        output = cur.fetchone()

        con.commit()

    # To close the connection
    con.close()
    return output


def read_all_activity():
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("SELECT * FROM dayitenary;")
        output = cur.fetchall()

        con.commit()

    # To close the connection
    con.close()
    return output


def update_activity(id, update_key, update_value):
    print(update_key)
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        query = f"UPDATE dayitenary SET {update_key}='{update_value}' WHERE day_activity_id='{id}';"

        cur.execute(query)
        con.commit()

    # To close the connection
    con.close()
    return "activity updated"


def delete_activity(day_activity_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute(
            "DELETE FROM dayitenary WHERE day_activity_id=%s", day_activity_id)
        con.commit()

    # To close the connection
    con.close()
    return "activity deleted"


def create_cost(cost):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute("INSERT INTO cost VALUES(%s, %s)",
                    (cost.cost_id, manipulate_data(cost.cost_plan)))

        con.commit()

    # To close the connection
    con.close()
    return "cost added"


def read_cost(cost_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("SELECT * FROM cost WHERE cost_id=%s", cost_id)
        output = cur.fetchone()

        con.commit()

    # To close the connection
    con.close()
    return output


def read_all_cost():
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("SELECT * FROM cost;")
        output = cur.fetchall()

        con.commit()

    # To close the connection
    con.close()
    return output


def update_cost(id, update_key, update_value):
    print(update_key)
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        query = f"UPDATE cost SET {update_key}='{update_value}' WHERE cost_id='{id}';"

        cur.execute(query)
        con.commit()

    # To close the connection
    con.close()
    return "cost updated"


def delete_cost(cost_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("DELETE FROM cost WHERE cost_id=%s", cost_id)
        con.commit()

    # To close the connection
    con.close()
    return "cost deleted"


def read_top():
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute(
            "SELECT * FROM package INNER JOIN itenary ON package.package_itenary = itenary.itenary_id WHERE package_status='top'")
        output = cur.fetchall()

        con.commit()

    # To close the connection

    con.close()
    return output


def create_newsletter(newsletter):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute("INSERT INTO newsletter VALUES(%s, %s)",
                    (newsletter.id, newsletter.email))

        con.commit()

    # To close the connection
    con.close()
    return "newsletter added"


def read_newsletter():
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("SELECT * FROM newsletter")
        output = cur.fetchall()

        con.commit()

    # To close the connection

    con.close()
    return output


def create_service(service):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute("INSERT INTO service(name, image_link, description) VALUES(%s, %s, %s)",
                    (service.name, service.image_link, service.description))

        con.commit()

    # To close the connection
    con.close()
    return "service added"


def read_services():
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("SELECT * FROM service")
        output = cur.fetchall()

        con.commit()

    # To close the connection

    con.close()
    return output


def delete_service(id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("DELETE FROM service WHERE service_id=%s", id)
        con.commit()

    # To close the connection
    con.close()
    return "service deleted"


def create_contact(contact):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute("INSERT INTO contact VALUES(%s, %s, %s, %s, %s)",
                    (contact.name, contact.email_id, contact.phone_number, contact.location, contact.message))

        con.commit()

    # To close the connection
    con.close()
    return "contact added"


def read_contact():
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("SELECT * FROM contact")
        output = cur.fetchall()

        con.commit()

    # To close the connection

    con.close()
    return output


def create_review(review):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute("INSERT INTO review VALUES(%s, %s, %s, %s)",
                    (review.name, review.profile, review.rating, review.description))

        con.commit()

    # To close the connection
    con.close()
    return "review added"


def read_reviews():
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("SELECT * FROM review")
        output = cur.fetchall()

        con.commit()

    # To close the connection

    con.close()
    return output


def create_content(content):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute("INSERT INTO common VALUES(%s, %s)",
                    (content.category, manipulate_data(content.data)))

        con.commit()

    # To close the connection
    con.close()
    return "content added"


def read_content(category):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("SELECT * FROM common WHERE category=%s", category)
        output = cur.fetchall()

        con.commit()

    # To close the connection

    con.close()
    return output


def create_session(session_id, order_id, booking_id, price):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute("INSERT INTO session VALUES(%s, %s, %s, %s)",
                    (session_id, order_id, booking_id, price))

        con.commit()

    # To close the connection
    con.close()
    return "session added"


def read_session(session_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("SELECT * FROM session WHERE session_id=%s", session_id)
        output = cur.fetchone()

        con.commit()

    # To close the connection

    con.close()
    return output


def delete_session(session_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("DELETE FROM session WHERE session_id=%s", session_id)
        output = cur.fetchone()

        con.commit()

    # To close the connection

    con.close()
    return output


def create_payment(payment_id, booking_id, package_id, session_id, order_id, price, timestamp):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute("INSERT INTO payment VALUES(%s, %s, %s, %s, %s, %s, %s)",
                    (payment_id, booking_id, package_id, session_id, order_id, price, timestamp))

        con.commit()

    # To close the connection
    con.close()
    return "payment added"


def read_booking_id(session_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute(
            "SELECT booking_id FROM payment WHERE session_id=%s;", session_id)
        output = cur.fetchone()

        con.commit()

    # To close the connection

    con.close()
    return output[0]


def update_payment_status(booking_id):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute(
            "UPDATE booking SET booking_payment_status='captured' WHERE booking_id=%s;", booking_id)
        output = cur.fetchone()

        con.commit()

    # To close the connection

    con.close()
    return output


def upload_image(image_name, purpose):
    s3 = session.resource("s3")
    s3.meta.client.upload_file(
        image_name, "poorva-user-files", f"{purpose}/{image_name}"
    )
    url = "https://%s.s3.amazonaws.com/%s" % (
        "nestpro-user-files",
        f"/{purpose}/{image_name}",
    )

    return {"url": url, "status": "Successfully Uploaded"}


def create_staff(staff):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password)

    with con.cursor() as cur:

        cur.execute("INSERT INTO staff VALUES(%s, %s, %s)",
                    (staff.staff_name, staff.staff_id, staff.staff_password))
        con.commit()

    # To close the connection
    con.close()
    return "Staff added"


def staff_login(user_id, user_password):
    con = pymysql.connect(
        host="103.148.156.141",
        database='poorvahol_test',
        user="poorvahol_user",
        password=password,
        cursorclass=pymysql.cursors.DictCursor)

    with con.cursor() as cur:

        cur.execute("SELECT * FROM staff WHERE staff_id=%s AND staff_password=%s;",
                    (user_id, user_password))

        output = cur.fetchone()

        con.commit()

    # To close the connection
    con.close()
    return output

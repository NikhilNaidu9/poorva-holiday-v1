import datetime
import uuid
from fastapi import APIRouter
from starlette.responses import HTMLResponse, Response
from os import getcwd

import models
import razorpay
import database as db

router = APIRouter(tags=["payment"])

client = razorpay.Client(auth=("rzp_live_dBCKDWL4OU7DPm", "oEZ0p65ihF7tqFLpiE9AZhcm"))


@router.post("/payment/order")
def create_order(order: models.Order):
    
    data = db.read_package(order.package_id)
    print(data.keys())
    print(data['package_cost'])
    data['package_cost'] = db.manipulate_load(data['package_cost']) 
    
    cost = db.read_cost(data['package_cost'])
    cost_arr = db.manipulate_load(cost['cost_plan'])
    
    price = order.cost
    
    arr = []
    total = 0
    for i in cost_arr:
        arr.append(i['id'])
        
    for i in price:
        if i in arr:
            total += cost_arr[arr.index(i)]['price']
                
    
    payment_order = client.order.create(dict(amount=total*100, currency='INR', receipt="order_rcptid_11", payment_capture=1))
    
    payment_order['session_id'] = uuid.uuid4()
    
    db.create_session(payment_order['session_id'], payment_order['id'], order.package_id, total)
    
    present_date = datetime.datetime.now()
    timestamp = datetime.datetime.timestamp(present_date)*1000
    
    payment_id = uuid.uuid4()
    
    payment_order['payment_id'] = payment_id
    
    db.create_payment(payment_id, order.booking_id, order.package_id, payment_order['session_id'], payment_order['id'], total, timestamp)
    return payment_order


@router.post("/payment/verification")
def verify_payment(payment:models.PaymentVerification):
    
    params_dict = {
        "razorpay_order_id": payment.orderid,
        "razorpay_payment_id": payment.razorpay_payment_id,
        "razorpay_signature": payment.razorpay_signature
    }
    
    if client.utility.verify_payment_signature(params_dict) == None:
        return True
    

@router.get("/payment/checkout/")
def read_checkout(session_id:str, response: Response):
    
    response.set_cookie(key="session_id", value=session_id)
    
    data = db.read_session(session_id)    

    html = """
    <head>
        <meta charset="UTF-8"
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    
    <body>
            <div class="container" style="width: 400px; background-color: white;border: 1px solid #767474; max-width: 400px;margin: auto;">
            <div class="brand-name-header" style="background-color: #478BB0;width: 96%%;padding: 2%%;text-align: center;"><p class="brand-name" style="font-size: 24px;font-weight: bolder;color: white;">Poorva Holidays</p></div> 
            <div class="column" style=" padding: 24px;">
                <p class="checkout" style="font-size: 18px; font-weight: bold;">Checkout</p>
                <hr>
                <div class="row" style="display: inline-flex;flex-flow: r wrap;justify-content: space-between;background-color: white;width: 100%%;">
                    <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50%% -10px);"><p class="checkout-details-key" style="font-size: 16px;font-weight: bold;">Package Name</p></div>
                    <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50%% -10px);"><p class="checkout-details-value" style="font-size: 16px;font-weight: bold;">Andaman Nicobar</p></div>
                </div>
                <div class="row" style="display: inline-flex;flex-flow: r wrap;justify-content: space-between;background-color: white;width: 100%%;">
                    <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50%% -10px);"><p class="checkout-details-key" style="font-size: 16px;font-weight: bold;">Booking Date</p></div>
                    <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50%% -10px);"><p class="checkout-details-value" style="font-size: 16px;font-weight: bold;">01-02-2022</p></div>
                </div>
                <div class="row" style="display: inline-flex;flex-flow: r wrap;justify-content: space-between;background-color: white;width: 100%%;">
                    <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50%% -10px);"><p class="checkout-details-key" style="font-size: 16px;font-weight: bold;">Number Of Guest</p></div>
                    <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50%% -10px);"><p class="checkout-details-value" style="font-size: 16px;font-weight: bold;">6</p></div>
                </div>
                <hr>
                <div class="row" style="display: inline-flex;flex-flow: r wrap;justify-content: space-between;background-color: white;width: 100%%;">
                    <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50%% -10px);"><p class="checkout-details-key" style="font-size: 16px;font-weight: bold;">Total Price</p></div>
                    <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50%% -10px);"><p class="checkout-details-value" style="font-size: 16px;font-weight: bold;">%s</p></div>
                </div>

                <div class="button-row row" style="display: inline-flex;flex-flow: r wrap;justify-content: space-between;background-color: white;width: 100%%;  height: 100px;align-items: center;">
                    <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50%% -10px);"><button class="cancel-button" style="font-size: 22px;padding: 12px 16px;width: 150px;border-radius: 10px;box-shadow: none;background-color: white;border: 1px solid #767474;">Cancel</button></div>
                    <div class=" item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50%% -10px);"><button id="rzp-button1" class="pay-button" style="font-size: 22px;padding: 12px 16px;width: 150px;border-radius: 10px;box-shadow: none;  background-color: #478BB0;color: white;border: none;">Pay</button></div>
                </div>
                
            </div>
        </div>
                    
            <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
            <script>
            var options = {
                "key": "rzp_test_HWHEtB84KP1yJT", // Enter the Key ID generated from the Dashboard
                "amount": %s, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                "currency": "INR",
                "name": "Acme Corp",
                "description": "Test Transaction",
                "image": "https://example.com/your_logo",
                "order_id": "%s", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                "handler": function (response){
                    alert(response.razorpay_payment_id);
                    alert(response.razorpay_order_id);
                    alert(response.razorpay_signature)
                    fetch("http://ec2-35-154-148-155.ap-south-1.compute.amazonaws.com:5000/payment/verification", {
     
                    // Adding method type
                    method: "POST",
                    
                    // Adding body or contents to send
                    body: JSON.stringify({
                "orderid": response['razorpay_order_id'],
                "razorpay_payment_id": response['razorpay_payment_id'],
                "razorpay_signature": response['razorpay_signature']
                }),
                    
                    // Adding headers to the request
                    headers: {
                        "Content-type": "application/json; charset=UTF-8"
                    }
                }).then( res => res.json()).then(json => {if (json == true) {
                    var url_string = window.location.href
                    var url = new URL(url_string);
                    var session_id = url.searchParams.get("session_id");
                    base_url = "http://ec2-35-154-148-155.ap-south-1.compute.amazonaws.com:5000/session/"
                    
                    fetch(base_url.concat(session_id), {
     
                    // Adding method type
                    method: "DELETE",
                    
                    // Adding headers to the request
                    headers: {
                        "Content-type": "application/json; charset=UTF-8"
                    }
                }).then( res => res.json()).then(json => {console.log(json)})

                base_url_booking = "http://127.0.0.1:8000/payment/booking/"
                fetch(base_url_booking.concat(session_id), {
     
                    // Adding method type
                    method: "GET",
                    
                    // Adding headers to the request
                    headers: {
                        "Content-type": "application/json; charset=UTF-8"
                    }
                }).then( res => res.json()).then(json => {
                    base_url_payment_status = "http://127.0.0.1:8000/payment/status/"
                fetch(base_url_payment_status.concat(json), {
     
                    // Adding method type
                    method: "PATCH",
                    
                    // Adding headers to the request
                    headers: {
                        "Content-type": "application/json; charset=UTF-8"
                    }
                }).then( res => res.json()).then(json => {
                    console.log(json)
                    
                })

                })
                }})
                },
                "prefill": {
                    "name": "Gaurav Kumar",
                    "email": "gaurav.kumar@example.com",
                    "contact": "9999999999"
                },
                "notes": {
                    "address": "Razorpay Corporate Office"
                },
                "theme": {
                    "color": "#3399cc"
                }
            };
            var rzp1 = new Razorpay(options);
            rzp1.on('payment.failed', function (response){
                    alert(response.error.code);
                    alert(response.error.description);
                    alert(response.error.source);
                    alert(response.error.step);
                    alert(response.error.reason);
                    alert(response.error.metadata.order_id);
                    alert(response.error.metadata.payment_id);
            });
            document.getElementById('rzp-button1').onclick = function(e){
                rzp1.open();
                e.preventDefault();
                console.log(rzp1);
            }
</script>""" % (data['price'], data['price'], data['order_id'])

    return HTMLResponse(html)


@router.get("/payment/booking/{session_id}")
async def read_booking_id(session_id: str):
    return db.read_booking_id(session_id)


@router.patch("/payment/status/{booking_id}")
async def update_payment_status(booking_id: str):
    return db.update_payment_status(booking_id)
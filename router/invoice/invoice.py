from fastapi import APIRouter, File
import models
from starlette.responses import FileResponse
import pdfkit

router = APIRouter(tags=["Invoice"])


def generate_invoice(invoice):
    text = f"""
    <!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

    </head>
    <body>
        
        <div class="container" style="  height: 842px; width: 595px;margin-left: auto;margin-right: auto;background-color: white;border: 1px solid #767474;">
            <div class="brand-name-header" style="background-color: #478BB0;width: 96%;padding: 2%;text-align: center;"><p class="brand-name" style="font-size: 24px;font-weight: bolder;color: white;">Poorva Holidays</p></div> 
            <div class="column" style="text-align: center;">
                <p class="checkout-details-key" style="font-size: 16px;">Invoice {invoice.invoice_id}</p>
            </div>
            <div class="container" style="padding: 16px;">
                <div class="column" style=" background-color: #F1F9FF; padding: 24px;">
                    <div class="row" style="display: inline-flex;flex-flow: r wrap;justify-content: space-between;background-color: #F1F9FF;width: 100%;">
                        <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50% -10px);"><p class="checkout-details-key" style="font-size: 16px;font-weight: bold;">User Name</p></div>
                        <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50% -10px);"><p class="checkout-details-value" style="font-size: 16px;font-weight: bold;">{invoice.user_name}</p></div>
                    </div>
                    <div class="row" style="display: inline-flex;flex-flow: r wrap;justify-content: space-between;background-color: #F1F9FF;width: 100%;">
                        <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50% -10px);"><p class="checkout-details-key" style="font-size: 16px;font-weight: bold;">Package Title</p></div>
                        <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50% -10px);"><p class="checkout-details-value" style="font-size: 16px;font-weight: bold;">{invoice.package_title}</p></div>
                    </div>
                    <div class="row" style="display: inline-flex;flex-flow: r wrap;justify-content: space-between;background-color: #F1F9FF;width: 100%;">
                        <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50% -10px);"><p class="checkout-details-key" style="font-size: 16px;font-weight: bold;">Package Date</p></div>
                        <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50% -10px);"><p class="checkout-details-value" style="font-size: 16px;font-weight: bold;">{invoice.booking_date}</p></div>
                    </div>
                    <div class="row" style="display: inline-flex;flex-flow: r wrap;justify-content: space-between;background-color: #F1F9FF;width: 100%;">
                        <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50% -10px);"><p class="checkout-details-key" style="font-size: 16px;font-weight: bold;">Booking Date</p></div>
                        <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50% -10px);"><p class="checkout-details-value" style="font-size: 16px;font-weight: bold;">{invoice.booking_date}</p></div>
                    </div>
                    <div class="row" style="display: inline-flex;flex-flow: r wrap;justify-content: space-between;background-color: #F1F9FF;width: 100%;">
                        <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50% -10px);"><p class="checkout-details-key" style="font-size: 16px;font-weight: bold;">Total Guest</p></div>
                        <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50% -10px);"><p class="checkout-details-value" style="font-size: 16px;font-weight: bold;">{invoice.no_of_guests}</p></div>
                    </div>

                    
    
                    <div class="row" style="display: inline-flex;flex-flow: r wrap;justify-content: space-between;background-color: #F1F9FF;width: 100%;">
                        <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50% -10px);"><p class="checkout-details-key" style="font-size: 16px;font-weight: bold;">Payment Status</p></div>
                        <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50% -10px);"><p class="checkout-details-value" style="font-size: 16px;font-weight: bold;">{invoice.payment_status}</p></div>
                    </div>


                    <hr>
                    <div class="row" style="display: inline-flex;flex-flow: r wrap;justify-content: space-between;background-color: #F1F9FF;width: 100%;">
                        <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50% -10px);"><p class="checkout-details-key" style="font-size: 16px;font-weight: bold;">Total Price</p></div>
                        <div class="item" style="flex-grow: 0;flex-shrink: 0;flex-basis: calc(50% -10px);"><p class="checkout-details-value" style="font-size: 16px;font-weight: bold;">{invoice.package_price}</p></div>
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>
    """

    file = open("report.html", "w")
    file.write(text)
    file.close()

    options = {"page-size": "A4"}

    print(pdfkit.from_file("report.html", "report.pdf", options=options))

    
@router.post("/invoice")
async def generate_pdf(invoice: models.Invoice):
    
    generate_invoice(invoice)
    
    return FileResponse("report.pdf", media_type="application/pdf")
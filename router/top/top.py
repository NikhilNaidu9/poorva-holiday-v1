from fastapi import APIRouter

import database as db

router = APIRouter(tags=["top"])


@router.get("/top")
async def get_top():
    outputs = db.read_top()
    arr = []
    if outputs != None:
        for output in outputs:
            output['package_offers'] = db.manipulate_load(output['package_offers'])
            output['package_theme'] = db.manipulate_load(output['package_theme'])
            output['package_gallery_link'] = db.manipulate_load(output['package_gallery_link'])
            output['package_hotel'] = db.manipulate_load(output['package_hotel'])
            output['package_flight'] = db.manipulate_load(output['package_flight'])
            output['package_cruise'] = db.manipulate_load(output['package_cruise'])
            output['package_activities'] = db.manipulate_load(output['package_activities'])
            output['package_availability'] = db.manipulate_load(output['package_availability'])
            output['day_activites'] = db.manipulate_load(output['day_activites'])
            output['itenary_inclusion'] = db.manipulate_load(output['itenary_inclusion'])
            output['itenary_exclusion'] = db.manipulate_load(output['itenary_exclusion'])
            output['package_cost'] = db.manipulate_load(output['package_cost'])
            output['package_cancellation_policy'] = db.manipulate_load(output['package_cancellation_policy'])
            output['package_stay'] = db.manipulate_load(output['package_stay'])
            arr.append(output)
            arr.append(output)
    return arr
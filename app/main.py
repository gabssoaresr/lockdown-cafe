from typing import Dict, List, Any
from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    masks_to_buy = 0
    vaccinated = True
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except NotWearingMaskError:
            masks_to_buy += 1
        except VaccineError:
            vaccinated = False
            break

    if not vaccinated:
        return "All friends should be vaccinated"
    elif masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"

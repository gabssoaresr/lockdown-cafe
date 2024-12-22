from datetime import date
from typing import Dict, Union

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(
        self,
        visitor: Dict[str, Union[str, int, bool, Dict[str, date]]]
    ) -> str:
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError()
        elif not visitor.get("vaccine"):
            raise NotVaccinatedError()
        elif visitor["vaccine"]["expiration_date"] < date.today():
            raise OutdatedVaccineError()

        return f"Welcome to {self.name}"

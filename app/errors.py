class VaccineError(Exception):
    def __init__(self, description: str = "Client has a vaccine error."):
        self.description = description
        super().__init__(self.description)


class NotVaccinatedError(VaccineError):
    def __init__(self, description: str = "The client is not vaccinated."):
        self.description = description
        super().__init__(self.description)


class OutdatedVaccineError(VaccineError):
    def __init__(self, description: str = "Vaccine is outdated."):
        self.description = description
        super().__init__(self.description)


class NotWearingMaskError(Exception):
    def __init__(self, description: str = "Client is not wearing a mask"):
        self.description = description
        super().__init__(self.description)

from LabelService.dhl.Country import Country, DHL_GERMANY


class SimpleAddress:
    """
    Represents a simple address used by the DHL interface
    """

    name1 = ""  # Mandatory
    name2 = None  # Optional
    name3 = None  # Optional

    streetName = ""  # Mandatory
    houseNumber = ""  # Mandatory
    postCode = ""  # Mandatory
    city = ""  # Mandatory
    country = None  # Mandatory

    def __init__(
            self,
            name1: str = None,
            name2: str = None,
            name3: str = None,
            streetName: str = None,
            houseNumber: str = None,
            postCode: str = None,
            city: str = None,
            country: Country = DHL_GERMANY) -> None:

        self.name1 = name1
        self.name2 = name2
        self.name3 = name3

        self.streetName = streetName
        self.houseNumber = houseNumber
        self.postCode = postCode
        self.city = city
        self.country = country

    def valid(self) -> bool:

        # Validate name1
        if not self.name1 or self.name1 == '':
            return False

        if len(self.name1) > 35:
            return False

        # Validate name2 if set
        if self.name2 and len(self.name2) > 35:
            return False

        # Validate name3 if set
        if self.name3 and len(self.name3) > 35:
            return False

        # Validate streetName str, max 35
        if not self.streetName or self.streetName == '':
            return False

        if len(self.streetName) > 35:
            return False

        # Validate houseNumber str, max 5
        if not self.houseNumber or self.houseNumber == '':
            return False

        if len(self.houseNumber) > 5:
            return False

        # Validate postCode str, max 10
        if not self.postCode or self.postCode == '':
            return False

        if len(self.postCode) > 10:
            return False

        # Validate city str, max 35
        if not self.city or self.city == '':
            return False

        if len(self.city) > 35:
            return False

        # Validate country
        if not self.country or not self.country.valid():
            return False

        return True

    def as_dict(self) -> dict:

        simple_address_dict = {
            'name1': self.name1,
            'streetName': self.streetName,
            'houseNumber': self.houseNumber,
            'postCode': self.postCode,
            'city': self.city,
            'country': self.country.as_dict()
        }

        if self.name2:
            # Optional
            simple_address_dict['name2'] = self.name2

        if self.name3:
            # Optional
            simple_address_dict['name3'] = self.name3

        return simple_address_dict

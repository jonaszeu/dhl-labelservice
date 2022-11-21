class Country:
    """
    Represents DHL Structure of country
    """

    countryISOCode = ""
    country = None  # Optional
    state = None  # Optional

    def __init__(self, countryISOCode: str, country: str) -> None:
        self.set_countryISOCode(countryISOCode)
        self.set_country(country)

    def set_countryISOCode(self, countryISOCode: str) -> None:
        self.countryISOCode = countryISOCode

    def set_country(self, country: str) -> None:
        self.country = country

    def set_state(self, state: str) -> None:
        self.state = state

    def valid(self) -> bool:

        if not self.countryISOCode or self.countryISOCode == '':
            return False

        if len(self.countryISOCode) != 3:
            return False

        return True

    def as_dict(self) -> dict:

        country_dict = {'countryISOCode': self.countryISOCode}

        if self.country:
            # Optional
            country_dict['country'] = self.country

        if self.state:
            # Optional
            country_dict['state'] = self.state

        return country_dict


# Ready to use Countrys
DHL_GERMANY = Country(countryISOCode="DEU", country="Germany")
DHL_AUSTRIA = Country(countryISOCode="AUT", country="Österreich")
DHL_SCHWEIZ = Country(countryISOCode="CHE", country="Schweiz")

class CustomsDocumentPosition:
    """
    Represents DHL CustomsDocumentsPosition
    """

    positionDescription = ""  # Mandatory
    count = 0  # Mandatory
    weightInGrams = 0  # Mandatory
    values = 0  # Mandatory
    originCountry = None  # Optional
    articleReference = None  # Optional
    tarifNumber = None  # Optional

    def __init__(
            self,
            positionDescription: str,
            count: int,
            weightInGrams: int,
            values: int,
            originCountry: str,
            articleReference: str,
            tarifNumber: str) -> None:

        self.set_positionDescription(positionDescription)
        self.set_count(count)
        self.set_weightInGrams(weightInGrams)
        self.set_values(values)
        self.set_originCountry(originCountry)
        self.set_articleReference(articleReference)
        self.set_tarifNumber(tarifNumber)

    def set_positionDescription(self, positionDescription: str) -> None:
        # length: min 0, max 50
        self.positionDescription = positionDescription

    def set_count(self, count: int) -> None:
        # min 0
        self.count = count

    def set_weightInGrams(self, weightInGrams: int) -> None:
        # min 0
        self.weightInGrams = weightInGrams

    def set_values(self, values: int) -> None:
        # min 0
        self.values = values

    def set_originCountry(self, originCountry: str) -> None:
        # length: 3
        self.originCountry = originCountry

    def set_articleReference(self, articleReference: str) -> None:
        # length: min 0, max 40
        self.articleReference = articleReference

    def set_tarifNumber(self, tarifNumber: str) -> None:
        # length: min 0, max 8
        self.tarifNumber = tarifNumber

    def valid(self) -> bool:

        # Validate positionDescription
        if not self.positionDescription or self.positionDescription == '':
            return False

        if len(self.positionDescription) > 50:
            return False

        # Validate count
        if not self.count:
            return False

        if self.count < 0:
            return False

        # Validate weightInGrams
        if not self.weightInGrams:
            return False

        if self.weightInGrams < 0:
            return False

        # Validate originCountry if set
        if self.originCountry:
            if len(self.originCountry) != 3:
                return False

        # Validate articleReference if set
        if self.articleReference:
            if len(self.articleReference) > 40:
                return False

        # Validate tarifNumber if set
        if self.tarifNumber:
            if len(self.tarifNumber) > 8:
                return False

        return True

    def as_dict(self) -> dict:

        customs_document_position = {
            'positionDescription': self.positionDescription,
            'count': self.count,
            'weightInGrams': self.weightInGrams,
            'values': self.values
        }

        if self.originCountry:
            # Optional
            customs_document_position['originCountry'] = self.originCountry

        if self.articleReference:
            # Optional
            customs_document_position['articleReference'] = self.articleReference  # noqa

        if self.tarifNumber:
            # Optional
            customs_document_position['tarifNumber'] = self.tarifNumber

        return customs_document_position

class CustomsDocument:
    """
    Represents DHL CustomsDocument
    """

    currency = ""  # Mandatory, Enum [ EUR, GBP, CHF ]
    originalShipmentNumber = None  # Optional
    originalOperator = None  # Optional
    acompanyingDocument = None  # Optional
    originalInvoiceNumber = None  # Optional
    originalInvoiceDate = None  # Optional
    comment = None  # Optional
    positions = []  # Mandatory
    # CustomsDocumentPosition, min 1 items, max 5 items

    def __init__(self,
                 currency: str,
                 originalShipmentNumber: str,
                 originalOperator: str,
                 acompanyingDocument: str,
                 originalInvoiceNumber: str,
                 originalInvoiceDate: str,
                 comment: str,
                 positions: list) -> None:

        self.set_currency(currency)
        self.set_originalShipmentNumber(originalShipmentNumber)
        self.set_originalOperator(originalOperator)
        self.set_acompanyingDocument(acompanyingDocument)
        self.set_originalInvoiceNumber(originalInvoiceNumber)
        self.set_originalInvoiceDate(originalInvoiceDate)
        self.set_comment(comment)
        self.set_positions(positions)

    def set_currency(self, currency: str) -> None:
        # Enum [ EUR, GBP, CHF ]
        self.currency = currency

    def set_originalShipmentNumber(self, originalShipmentNumber: str) -> None:
        # length: min 0, max 35
        self.originalShipmentNumber = originalShipmentNumber

    def set_originalOperator(self, originalOperator: str) -> None:
        # length: min 0, max 40
        self.originalOperator = originalOperator

    def set_acompanyingDocument(self, acompanyingDocument: str) -> None:
        # length: min 0, max 35
        self.acompanyingDocument = acompanyingDocument

    def set_originalInvoiceNumber(self, originalInvoiceNumber: str) -> None:
        # length: min 0, max 35
        self.originalInvoiceNumber = originalInvoiceNumber

    def set_originalInvoiceDate(self, originalInvoiceDate: str) -> None:
        # length: min 0, max 35
        self.originalInvoiceDate = originalInvoiceDate

    def set_comment(self, comment: str) -> None:
        # length: min 0, max 150
        self.comment = comment

    def set_positions(self, positions: list) -> None:
        # length: min 1, max 5 items
        # CustomsDocumentPosition
        self.positions = positions

    def valid(self) -> bool:

        # Validate currency
        if not self.currency or self.currency == '':
            return False

        if self.currency not in ['EUR', 'GBP', 'CHF']:
            return False

        # Validate originalShipmentNumber if set
        if self.originalShipmentNumber:
            if len(self.originalShipmentNumber) > 35:
                return False

        # Validate originalOperator if set
        if self.originalOperator:
            if len(self.originalOperator) > 40:
                return False

        # Validate acompanyingDocument if set
        if self.acompanyingDocument:
            if len(self.acompanyingDocument) > 35:
                return False

        # Validate originalInvoiceNumber if set
        if self.originalInvoiceNumber:
            if len(self.originalInvoiceNumber) > 35:
                return False

        # Validate originalInvoiceDate if set
        if self.originalInvoiceDate:
            if len(self.originalInvoiceDate) > 35:
                return False

        # Validate comment if set
        if self.comment:
            if len(self.comment) > 150:
                return False

        # Validate positions if set
        if not self.positions or self.positions == []:
            return False

        if len(self.positions) < 1:
            return False

        return True

    def as_dict(self) -> dict:

        customs_document = {
            'currency': self.currency,
            'positions': self.positions
        }

        if self.originalShipmentNumber:
            customs_document['originalShipmentNumber'] = self.originalShipmentNumber  # noqa

        if self.originalOperator:
            customs_document['originalOperator'] = self.originalOperator

        if self.acompanyingDocument:
            customs_document['acompanyingDocument'] = self.acompanyingDocument

        if self.originalInvoiceNumber:
            customs_document['originalInvoiceNumber'] = self.originalInvoiceNumber  # noqa

        if self.originalInvoiceDate:
            customs_document['originalInvoiceDate'] = self.originalInvoiceDate

        if self.comment:
            customs_document['comment'] = self.comment

        return customs_document

from LabelService.dhl.SimpleAddress import SimpleAddress
from LabelService.dhl.CustomsDocument import CustomsDocument

ENUM_RETURNDOCUMENTTYPE = ['SHIPMENT_LABEL', 'QR_LABEL', 'BOTH']


class ReturnOrder:
    """
    The object contains the details of the sender, the returnshipment
    and references.
    """

    receiverId = ""  # Mandatory
    customerReference = None  # Optional
    shipmentReference = None  # Optional
    senderAddress = None  # Mandatory, SimpleAddress
    email = None  # Optional
    telephoneNumber = None  # Optional
    weightInGrams = None  # Optional, integer
    value = None  # Optional, number
    customsDocument = None  # Optional, CustomsDocument
    returnDocumentType = None  # Optional
    # Enum: [SHIPMENT_LABEL, QR_LABEL, BOTH]

    def __init__(
            self,
            receiverId: str = "",
            customerReference: str = None,
            shipmentReference: str = None,
            senderAddress: SimpleAddress = None,
            email: str = None,
            telephoneNumber: str = None,
            weightInGrams: int = 0,
            value: int = 0,
            customsDocument: CustomsDocument = None,
            returnDocumentType: str = "BOTH") -> None:

        self.set_receiverId(receiverId)
        self.set_customerReference(customerReference)
        self.set_shipmentReference(shipmentReference)
        self.set_senderAddress(senderAddress)
        self.set_email(email)
        self.set_telephoneNumber(telephoneNumber)
        self.set_weightInGrams(weightInGrams)
        self.set_value(value)
        self.set_customsDocument(customsDocument)
        self.set_returnDocumentType(returnDocumentType)

    def set_receiverId(self, receiverId: str) -> None:
        # length: min 0, max 30
        self.receiverId = receiverId

    def set_customerReference(self, customerReference: str) -> None:
        # length: min 0, max 30
        self.customerReference = customerReference

    def set_shipmentReference(self, shipmentReference: str) -> None:
        # length: min 0, max 30
        self.shipmentReference = shipmentReference

    def set_senderAddress(self, senderAddress: SimpleAddress) -> None:
        self.senderAddress = senderAddress

    def set_email(self, email: str) -> None:
        # length: min 0, max 70
        self.email = email

    def set_telephoneNumber(self, telephoneNumber: str) -> None:
        # length: min 0, max 35
        self.telephoneNumber = telephoneNumber

    def set_weightInGrams(self, weightInGrams: int) -> None:
        # min 0
        self.weightInGrams = weightInGrams

    def set_value(self, value: int) -> None:
        # min 0
        self.value = value

    def set_customsDocument(self, customsDocument: CustomsDocument) -> None:
        self.customsDocument = customsDocument

    def set_returnDocumentType(self, returnDocumentType: str) -> None:
        # Enum: [SHIPMENT_LABEL, QR_LABEL, BOTH]
        self.returnDocumentType = returnDocumentType

    def valid(self) -> bool:
        """
        Only validate mandotory fields
        """

        # Validate receiverId
        if not self.receiverId or self.receiverId == '':
            return False

        if len(self.receiverId > 30):
            return False

        # Validate customerReference if set
        if self.customerReference:
            if len(self.customerReference) > 30:
                return False

        # Validate shipmentReference if set
        if self.shipmentReference:
            if len(self.shipmentReference) > 30:
                return False

        # Validate senderAddress
        if not self.senderAddress:
            return False

        if not self.senderAddress.valid():
            return False

        # Validate email if set
        if self.email:
            if len(self.email) > 70:
                return False

        # Validate telephoneNumber if set
        if self.telephoneNumber:
            if len(self.telephoneNumber) > 35:
                return False

        # Validate weightInGrams if set
        if self.weightInGrams:
            if self.weightInGrams < 0:
                return False

        # Validate value if set
        if self.value:
            if self.value < 0:
                return False

        # Validate customsDocument if set
        if self.customsDocument:
            if not self.customsDocument.valid():
                return False

        # Validate returnDocumentType if set
        if self.returnDocumentType:
            if self.returnDocumentType not in ENUM_RETURNDOCUMENTTYPE:
                return False

        return True

    def as_dict(self) -> dict:

        return_order_dict = {
            'receiverId': self.receiverId,
            'senderAddress': self.senderAddress.as_dict()
        }

        if self.customerReference:
            # Optional
            return_order_dict['customerReference'] = self.customerReference

        if self.shipmentReference:
            # Optional
            return_order_dict['shipmentReference'] = self.shipmentReference

        if self.email:
            # Optional
            return_order_dict['email'] = self.email

        if self.telephoneNumber:
            # Optional
            return_order_dict['telephoneNumber'] = self.telephoneNumber

        if self.weightInGrams:
            # Optional
            return_order_dict['weightInGrams'] = self.weightInGrams

        if self.value:
            # Optional
            return_order_dict['value'] = self.value

        if self.customsDocument:
            # Optional
            return_order_dict['customsDocument'] = self.customsDocument.as_dict()  # noqa

        if self.returnDocumentType:
            # Optional
            return_order_dict['returnDocumentType'] = self.returnDocumentType

        return return_order_dict

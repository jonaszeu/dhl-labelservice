from LabelService.dhl.SimpleAddress import SimpleAddress
# from app.labelService.dhl.Country import DHL_GERMANY
from LabelService.dhl.ReturnOrder import ReturnOrder


class LabelRequestBody:
    """
        A simple class that represents the data used to create a return label.
    """

    return_order = None
    customer_address = None

    def __init__(self, receiverId: str, name1: str,
                 streetName: str, houseNumber: str,
                 postCode: str, city: str) -> None:

        self.set_customerAddress(
            name1,
            streetName,
            houseNumber,
            postCode,
            city)

        self.set_returnOrder(receiverId)

    def set_customerAddress(self, name1: str, streetName: str,
                            houseNumber: str, postCode: str,
                            city: str) -> None:

        self.customer_address = SimpleAddress(
            name1=name1,
            streetName=streetName,
            houseNumber=houseNumber,
            postCode=postCode,
            city=city
            )

    def set_returnOrder(self, receiverId: str) -> None:
        self.return_order = ReturnOrder(
            receiverId=receiverId,
            senderAddress=self.customer_address
            )

    def get_body(self) -> dict:

        if not self.return_order.valid():
            return {}

        return self.return_order.as_dict()

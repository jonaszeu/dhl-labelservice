import requests

from LabelService.LabelRequestBody import LabelRequestBody


GER_DHL_URL_AUTH_SANDBOX = 'https://cig.dhl.de/services/sandbox/rest'
GER_DHL_RUL_AUTH_PRODUCTION = 'https://cig.dhl.de/services/production/rest'

GER_DHL_URL_RETURNS_SANDBOX = 'https://cig.dhl.de/services/sandbox/rest/returns/'  # noqa
GER_DHL_URL_RETURNS_PRODUCTION = 'https://cig.dhl.de/services/production/rest/returns/'  # noqa


class LabelService:

    def __init__(self) -> None:
        pass


def get_dhl_request_header_auth(ApplikationsID: str,
                                Applikationstoken: str) -> dict:

    # TODO
    return {
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'DPDHL-User-Authentication-Token': ''
        }


def get_dhl_request_header(DPDHL_User_Authentication_Token: str) -> dict:

    return {
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'DPDHL-User-Authentication-Token': DPDHL_User_Authentication_Token
        }


def authentication(ApplikationsID: str, Applikationstoken: str):
    # Authentication at DHL
    # TODO

    response = requests.get(
        GER_DHL_URL_AUTH_SANDBOX,
        headers=get_dhl_request_header_auth(ApplikationsID, Applikationstoken)
        )

    if response.status_code != 200:
        # TODO
        # something went wrong
        # raise Exception('Request returned with status code: ',
        # response.status_code, ' and response: ', response)
        pass

    # TODO handle response

    DPDHL_User_Authentication_Token = ''
    return DPDHL_User_Authentication_Token


def request_label(DPDHL_User_Authentication_Token: str,
                  receiverId: str,
                  name1: str,
                  streetName: str,
                  houseNumber: str,
                  postCode: str,
                  city: str):

    # Create request_body with all information
    # Set requiered fields
    request_body = LabelRequestBody(
        receiverId=receiverId,
        name1=name1,
        streetName=streetName,
        houseNumber=houseNumber,
        postCode=postCode,
        city=city)

    # Get the body as dict
    body = request_body.get_body()

    # TODO make request
    response = requests.get(
        GER_DHL_URL_RETURNS_SANDBOX,
        headers=get_dhl_request_header(DPDHL_User_Authentication_Token),
        body=body)

    if response.status_code != 200:
        # TODO
        # something went wrong
        # raise Exception('Request returned with status code: ',
        # response.status_code, ' and response: ', response)
        pass

    # TODO handle result
    return response.json()

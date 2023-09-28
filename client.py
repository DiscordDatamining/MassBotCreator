from datetime import datetime

import aiohttp
import httpx
import requests
from aiohttp import (
    ClientConnectionError,
    ClientConnectorCertificateError,
    ClientConnectorError,
    ClientConnectorSSLError,
    ClientError,
    ClientHttpProxyError,
    ClientOSError,
    ClientResponse,
    ClientSession,
)
from colored import fg
from geopy.geocoders import Nominatim
from requests import (
    ConnectionError,
    JSONDecodeError,
    get,
    post,
)


class Client:
    def __init__(self: "Client") -> None:
        """
        Initialize init
        """
        now = datetime.now()
        self.hours = now.strftime("%I")
        self.minutes = now.strftime("%M")
        self.period = now.strftime("%p").upper()
        self.green = fg("#ACD8A7")
        self.red = fg("#FAA61A")
        self.yellow = fg("#ffa500")
        self.grey = fg("#2b2d31")
        self.session: ClientSession = aiohttp.ClientSession

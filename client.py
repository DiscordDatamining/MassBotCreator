import aiohttp
import httpx
import requests
from datetime import datetime
from geopy.geocoders import Nominatim
from colored import fg
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

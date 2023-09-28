"""
Author: Sipher
GitHub: https://github.com/strangevile/MassBotCreator

This Python script allows you to create multiple Discord bots using multiple tokens simultaneously. 
Simply configure your tokens and settings, and let the client do the rest.

Instructions:
1. Add your tokens to the configuration.
2. Customize your settings as needed.
3. Run this script to create and run create multiple Discord bots.

"""

from datetime import datetime
import redis
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
from redis import StrictRedis
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
        initializer
        """
        now = datetime.now()
        self.hours = now.strftime("%I")
        self.minutes = now.strftime("%M")
        self.period = now.strftime("%p").upper()
        self.green = fg("#ACD8A7")
        self.red = fg("#FAA61A")
        self.yellow = fg("#ffa500")
        self.grey = fg("#2b2d31")
        self.blue = fg("#748cdc")
        self.session: ClientSession = aiohttp.ClientSession
        self.redis = StrictRedis(
            host="localhost",
            port=6379,
            db=0,
        )

    def __sessions__(self: "Client", *args, **kwargs) -> None:
        req = get(url="https://discord.com/api/v9/experiments")
        fingerprint = req.json()["fingerprint"]
        self.redis.set(
            name="client_fingerprint",
            value=fingerprint,
        )

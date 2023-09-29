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
import json
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
from colorama import Fore
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
        self.white = Fore.RESET
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

    def error(self: "Client", message: str) -> None:
        print(
            (
                f"[{self.grey}Today {self.white}@ {self.grey}{self.hours}:{self.minutes} {self.period}{self.white}]{self.white}({self.red}Error{self.white}) "
                f"{message}"
            )
        )

    def approve(self: "Client", message: str) -> None:
        print(
            (
                f"[{self.grey}Today {self.white}@ {self.grey}{self.hours}:{self.minutes} {self.period}{self.white}]{self.white}({self.green}Success{self.white}) "
                f"{message}"
            )
        )

    def warn(self: "Client", message: str) -> None:
        print(
            (
                f"[{self.grey}Today {self.white}@ {self.grey}{self.hours}:{self.minutes} {self.period}{self.white}]{self.white}({self.yellow}WARNING!{self.white}) "
                f"{message}"
            )
        )

    # def load_tokens(self: "Client") -> None:
    #     tokens = open("helpers/tokens.txt", "r").readlines()
    #     for token in tokens:
    #         t = token.rstrip()
    #         return t

    def get_data(self: "Client", data: list or str) -> None:
        config = json.load(
            open(
                file="config.json",
                encoding="UTF-8",
            )
        )
        configs = {
            "user-agent": config.get("user-agent"),
            "request-type": config.get("request_type"),
            "threshold": config.get("threshold"),
            "names": config.get("names"),
        }

        return configs.get(data, None)

    def create(self: "Client") -> None:
        tokens = open("helpers/tokens.txt", "r").readlines()
        for token in tokens:
            t = token.rstrip()
            agent = self.get_data("user-agent")
            name = self.get_data("names")
            p = post(
                url="https://discord.com/api/v9/applications",
                json={"name": str(name)},
                headers={
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Authorization": str(t),
                    "Content-Length": "29",
                    "Content-Type": "application/json",
                    "Origin": "https://discord.com",
                    "Referer": "https://discord.com/developers/applications",
                    "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
                    "Sec-Ch-Ua-Mobile": "?0",
                    "Sec-Ch-Ua-Platform": '"Windows"',
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": str(agent),
                    "X-Track": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
                },
            )
            data = p.json()
            self.approve(message=f"Bot Account created successfuly! ({t[:1]}..)")


Client = Client().create()

import os

API_KEY = "QjahxFZbHLfRSJBehx0Sl5M4I"

API_KEY_SECRET = "kOdzJHUlZrV7B62L1jnXpHwLeb0qWHwAbnld5EV2POTO8VuZHR"

BEARER_TOKEN= "AAAAAAAAAAAAAAAAAAAAAEXgfwEAAAAAJdl35yedOI%2BLzvRS%2F2YtW0KRc4w%3DyJSDLbg5JHe5xQWsj86XgNXX67mOyq0kOnAv6nP7WgfsrF55oc"
ACCESS_TOKEN = "1065620839331241984-ce1d0X09HvpPNDxSncIeAyAcc7t3e5"
ACESS_SECRET = "pADbnRSVsCi8IJkachFuhiLc1MKgeZSl2k4ure2g6pz90"


class TwitterSceret():

    def __init__(self) -> None:
        self.CONSUMER_KEY = API_KEY
        print(self.CONSUMER_KEY)
        self.CONSUMER_SECRET = API_KEY_SECRET
        self.BEARER_TOKEN = BEARER_TOKEN
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.ACESS_SECRET = ACESS_SECRET

        for key, secret in self.__dict__.items():
            assert secret != "" f"Please Provide a valid secret for {key}"

tweeter_secrets = TwitterSceret()


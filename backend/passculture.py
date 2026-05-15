import requests
import uuid
import os
from twocaptcha import TwoCaptcha

class PassCultureClient:
    BASE_URL = "https://backend.passculture.app"

    def __init__(self):
        self.api_key = os.getenv("TWOCAPTCHA_KEY")
        self.solver = TwoCaptcha(self.api_key)
        self.device_id = str(uuid.uuid4())

    def solve_captcha(self):
        result = self.solver.recaptcha(
            sitekey="6LdWB0caAAAAAKfVe3he0FqXQXOepICF-5aZh_rQ",
            url="https://passculture.app/connexion"
        )
        return result["code"]

    def login(self, email, password):
        captcha = self.solve_captcha()

        r = requests.post(
            f"{self.BASE_URL}/native/v1/signin",
            json={
                "identifier": email,
                "password": password,
                "token": captcha
            },
            headers={"app-version": "1.390.4"}
        )

        if r.status_code != 200:
            return None

        return r.json().get("accessToken")

    def get_profile(self, token):
        r = requests.get(
            f"{self.BASE_URL}/native/v1/me",
            headers={"authorization": f"Bearer {token}"}
        )
        return r.json()

    def get_bookings(self, token):
        r = requests.get(
            f"{self.BASE_URL}/native/v2/bookings/ended",
            headers={"authorization": f"Bearer {token}"}
        )
        return r.json()
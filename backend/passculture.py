import requests
import uuid
import os
from twocaptcha import TwoCaptcha


class PassCultureClient:
    BASE_URL = "https://backend.passculture.app"

    def __init__(self):
        self.api_key = os.getenv("TWOCAPTCHA_KEY")

        if not self.api_key:
            raise ValueError("TWOCAPTCHA_KEY environment variable is missing")

        self.solver = TwoCaptcha(self.api_key)
        self.device_id = str(uuid.uuid4())

    def solve_captcha(self):
        try:
            # Fixed method name
            result = self.solver.solve_recaptcha(
                sitekey="6LdWB0caAAAAAKfVe3he0FqXQXOepICF-5aZh_rQ",
                url="https://passculture.app/connexion"
            )

            return result["code"]

        except Exception as e:
            print(f"Captcha solving failed: {e}")
            return None

    def login(self, email, password):
        captcha = self.solve_captcha()

        if not captcha:
            print("Failed to get captcha token")
            return None

        try:
            r = requests.post(
                f"{self.BASE_URL}/native/v1/signin",
                json={
                    "identifier": email,
                    "password": password,
                    "token": captcha
                },
                headers={
                    "app-version": "1.390.4",
                    "user-agent": "passculture.android",
                    "content-type": "application/json"
                },
                timeout=30
            )

            print("Status Code:", r.status_code)
            print("Response:", r.text)

            if r.status_code != 200:
                return None

            return r.json().get("accessToken")

        except Exception as e:
            print(f"Login failed: {e}")
            return None

    def get_profile(self, token):
        try:
            r = requests.get(
                f"{self.BASE_URL}/native/v1/me",
                headers={
                    "authorization": f"Bearer {token}"
                },
                timeout=30
            )

            return r.json()

        except Exception as e:
            print(f"Profile fetch failed: {e}")
            return None

    def get_bookings(self, token):
        try:
            r = requests.get(
                f"{self.BASE_URL}/native/v2/bookings/ended",
                headers={
                    "authorization": f"Bearer {token}"
                },
                timeout=30
            )

            return r.json()

        except Exception as e:
            print(f"Bookings fetch failed: {e}")
            return None
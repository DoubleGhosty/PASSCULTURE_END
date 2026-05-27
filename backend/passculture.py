import requests
import uuid
import os
import time
from twocaptcha import TwoCaptcha

MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds between retries


class PassCultureClient:
    BASE_URL = "https://backend.passculture.app"

    def __init__(self):
        self.api_key = os.getenv("TWOCAPTCHA_KEY")

        if not self.api_key:
            raise ValueError("TWOCAPTCHA_KEY environment variable is missing")

        self.solver = TwoCaptcha(self.api_key)
        self.device_id = str(uuid.uuid4())

    # -----------------------
    # CAPTCHA
    # -----------------------
    def solve_captcha(self):
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                result = self.solver.recaptcha(
                    sitekey="6LdWB0caAAAAAKfVe3he0FqXQXOepICF-5aZh_rQ",
                    url="https://passculture.app/connexion?preventCancellation=true"
                )
                return result["code"]
            except Exception as e:
                print(f"Captcha attempt {attempt}/{MAX_RETRIES} failed: {e}")
                if attempt < MAX_RETRIES:
                    time.sleep(RETRY_DELAY)
        return None

    # -----------------------
    # LOGIN
    # -----------------------
    def login(self, email, password):
        captcha = self.solve_captcha()

        if not captcha:
            print("Failed to get captcha token after retries")
            return None

        for attempt in range(1, MAX_RETRIES + 1):
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

                if r.status_code == 200:
                    return r.json().get("accessToken")

                # don't retry on 4xx (bad credentials, etc.)
                if 400 <= r.status_code < 500:
                    return None

            except requests.exceptions.Timeout:
                print(f"Login attempt {attempt}/{MAX_RETRIES} timed out")
            except Exception as e:
                print(f"Login attempt {attempt}/{MAX_RETRIES} failed: {e}")

            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)

        return None

    # -----------------------
    # PROFILE
    # -----------------------
    def get_profile(self, token):
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                r = requests.get(
                    f"{self.BASE_URL}/native/v1/me",
                    headers={
                        "authorization": f"Bearer {token}",
                        "app-version": "1.390.4",
                        "user-agent": "passculture.android"
                    },
                    timeout=30
                )
                if r.status_code == 200:
                    return r.json()
                if 400 <= r.status_code < 500:
                    return None
            except requests.exceptions.Timeout:
                print(f"Profile attempt {attempt}/{MAX_RETRIES} timed out")
            except Exception as e:
                print(f"Profile attempt {attempt}/{MAX_RETRIES} failed: {e}")

            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)

        return None

    # -----------------------
    # BOOKINGS
    # -----------------------
    def get_bookings(self, token):
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                r = requests.get(
                    f"{self.BASE_URL}/native/v2/bookings/ended",
                    headers={
                        "authorization": f"Bearer {token}",
                        "app-version": "1.390.4",
                        "user-agent": "passculture.android"
                    },
                    timeout=30
                )
                if r.status_code == 200:
                    return r.json()
                if 400 <= r.status_code < 500:
                    return None
            except requests.exceptions.Timeout:
                print(f"Bookings attempt {attempt}/{MAX_RETRIES} timed out")
            except Exception as e:
                print(f"Bookings attempt {attempt}/{MAX_RETRIES} failed: {e}")

            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)

        return None

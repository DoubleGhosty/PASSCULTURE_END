from fastapi import FastAPI
from pydantic import BaseModel
from passculture import PassCultureClient
from db import supabase

app = FastAPI()
client = PassCultureClient()

class LoginRequest(BaseModel):
    email: str
    password: str


# 1. LOGIN
@app.post("/login")
def login(data: LoginRequest):
    token = client.login(data.email, data.password)

    if not token:
        return {"error": "login_failed"}

    supabase.table("users").upsert({
        "email": data.email,
        "token": token
    }).execute()

    return {"token": token}


# 2. PROFILE
@app.get("/profile/{email}")
def profile(email: str):
    user = supabase.table("users").select("*").eq("email", email).execute()
    token = user.data[0]["token"]

    return client.get_profile(token)


# 3. BOOKINGS
@app.get("/bookings/{email}")
def bookings(email: str):
    user = supabase.table("users").select("*").eq("email", email).execute()
    token = user.data[0]["token"]

    return client.get_bookings(token)


@app.get("/health")
def health():
    return {"status": "ok"}
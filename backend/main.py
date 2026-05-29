from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from passculture import PassCultureClient
from db import supabase

app = FastAPI()

# CORS CONFIG
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://passculture-end.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    }, on_conflict="email").execute()

    return {"token": token}


# 2. PROFILE
@app.get("/profile/{email}")
def profile(email: str):
    user = supabase.table("users").select("*").eq("email", email).execute()

    if not user.data:
        return {"error": "user_not_found"}

    token = user.data[0]["token"]

    return client.get_profile(token)


# 3. BOOKINGS
@app.get("/bookings/{email}")
def bookings(email: str):
    user = supabase.table("users").select("*").eq("email", email).execute()

    if not user.data:
        return {"error": "user_not_found"}

    token = user.data[0]["token"]

    return client.get_bookings(token)


# HEALTH CHECK
@app.get("/health")
def health():
    return {"status": "ok"}
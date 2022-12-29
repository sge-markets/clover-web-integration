import aiohttp
from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def oauth_step1(client_id: str, employee_id: str, merchant_id: str, code: str):
    params = [
        ("client_id", client_id),
        ("code", code),
        ("client_secret", os.environ["CLOVER_SECRET"]),
    ]
    print(f"params:{params}")
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://sandbox.dev.clover.com/oauth/token", params=params
        ) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers["content-type"])

            html = await response.text()
            print("Body:", html, "...")

    return {}

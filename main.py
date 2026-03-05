import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

API_KEY = os.getenv("RAIN_API_KEY")
# ini auth
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

MY_LAT = -6.2369
MY_LONG = 106.853

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

res = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast",
    params=params
)

data = res.json()

will_rain = False

for forecast in data["list"]:
    weather_id = forecast["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
        break

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
    from_="whatsapp:+14155238886",
    body="It's going to rain today. Remember to bring an umbrella",
    to="whatsapp:+6287776161712"
    )

    print("Rain alert sent!")

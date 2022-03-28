import requests
from twilio.rest import Client
api_key = "api key of open weather"
weather_url = 'https://api.openweathermap.org/data/2.5/onecall'

account_sid = 'AC89adca6507be3948d27bdf7d3c30e346'
account_auth = "auth token of twilio"
parameters = {
    'lat' : 13.756331,
    'lon' : 100.501762,
    'appid' : api_key,
    'exclude':"current,minutely,daily"

}

response = requests.get(url=weather_url,params=parameters)
data = response.json()
will_rain = False
for i in range(0,11):
    if data['hourly'][i]['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, account_auth)

    message = client.messages \
        .create(
        body="It's going to RAIN.Bring UMBRELLA!!!",
        from_='twilio generated number',
        to='YOUR PHONE NUMBER'
    )
    print(message.status)


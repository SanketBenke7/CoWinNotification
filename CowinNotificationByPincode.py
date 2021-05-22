import requests
from datetime import date

#change pincode which you required
pincode = "400053"
today = date.today().strftime("%d-%m-%Y")
cowin_url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin" #?pincode={pincode}&date={today}"
PARAMS = {'pincode':pincode,'date':today}
HEADERS = {"content-type": "application/json", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

response = requests.get(url=cowin_url, params = PARAMS, headers=HEADERS)
data = response.json()

#replace with your own token id
token_id = "replace your token id here"
#replace group chat id where you want to send message
chat_id = "replace your chat id"

telegram_url = f"https://api.telegram.org/bot{token_id}/sendMessage"

for center in data["centers"]:
    for session in center["sessions"]:
        if session['available_capacity'] > 0:
            #you can change message format
            message = f"pincode: {center['pincode']}\naddress: {center['address']}\navailable_capacity: {session['available_capacity']}\navailable_capacity_dose1: {session['available_capacity_dose1']}\navailable_capacity_dose2: {session['available_capacity_dose2']}\ndate: {session['date']}\nmin_age_limit: {session['min_age_limit']}\nname: {center['name']}\nfee_type: {center['fee_type']}"
            telegram_params = {'chat_id': chat_id,'text':message}
            requests.get(url=telegram_url, params = telegram_params )

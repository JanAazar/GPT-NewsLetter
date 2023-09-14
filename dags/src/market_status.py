import requests
from src import auth

def get_market_status():
    api_key = auth.vantage_api_key
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = f'https://www.alphavantage.co/query?function=MARKET_STATUS&apikey={api_key}'
    try:
        r = requests.get(url)
        data = r.json()
        us_status = data["markets"][0]["current_status"]
        with open("dags//src//market_status.txt", "w") as file:
            file.write(us_status + "\n")
    except Exception as e:
        print(e)
        with open("dags//src//market_status.txt", "w") as file:
            file.write("closed" + "\n")


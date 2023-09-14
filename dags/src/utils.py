import datetime
import requests
from src.auth import vantage_api_key as api_key


def break_date(formatted_date):
    month = formatted_date[5:7]
    day = formatted_date[8:10]
    year = formatted_date[0:4]
    return f"{year}{month}{day}"

def get_date():
  
    current_datetime = datetime.datetime.now() - datetime.timedelta(hours=6)
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    return formatted_date

    # yesterday = current_datetime - datetime.timedelta(days=1)
    # return yesterday.strftime("%Y-%m-%d")
    

def get_ticker_data(tickers=["QQQ","SPY"]):
    
    
    data_dict = {
        "QQQ Open": 0.00,
        "QQQ Close": 0.00,
        "QQQ Highest": 0.00,
        "QQQ Lowest": 0.00,
        "SPY Open": 0.00,
        "SPY Close": 0.00,
        "SPY Highest": 0.00,
        "SPY Lowest": 0.00
    }

    for ticker in tickers:
    
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=60min&apikey={api_key}"    
        r = requests.get(url)
        r_json = r.json()

        highest=0.00
        lowest=100000.00
        open_price=0
        close_price=0

        cur_date = get_date()
        for key,value in r_json["Time Series (60min)"].items():
             if key[:10]==str(cur_date):
                 if key[11:]=="04:00:00":
                    open_price = float(value["1. open"])
                    
                    data_dict[f"{ticker} Open"] = open_price
                 if key[11:]=="19:00:00":
                    close_price = float(value["1. open"])
                    
                    data_dict[f"{ticker} Close"] = close_price
                 if float(value["2. high"])>highest:
                    highest = float(value["2. high"])
                 if float(value["3. low"])<lowest:
                    lowest = float(value["3. low"])

        data_dict[f"{ticker} Highest"] = highest
        data_dict[f"{ticker} Lowest"] = lowest

    # seperator = "\n"
    # data = seperator.join(data)
    return data_dict

letter_instructions = "The name of the newsletter is GPT-Letter. Do not add sincerely at the bottom. Create a newsletter in paragraph form and not bullet points or lists."
    
def get_receivers(file_name):
    with open(file_name, "r") as file:
        receivers = file.read()
    receivers = receivers.split("\n")
    return receivers

if __name__ == "__main__":
    get_ticker_data()
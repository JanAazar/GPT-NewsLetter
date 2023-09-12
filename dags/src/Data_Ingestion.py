import os
import requests
from src.auth import api_key
from src.auth import nyt_headline_api_key as story_api_key
from src.utils import break_date,get_date
from src.logger import logging

def get_articles():

    """
    This function takes in a date in the format of YYYYMMDD and returns a list of paths to the articles.
    """
    formatted_date = get_date()
    article_date = break_date(formatted_date)
    
    key = api_key
    keywords = ["Stock Market","Economy","Earnings","Bond Market","Commodities","Cryptocurrency","IPOs","Mergers and Acquisitions","Regulation","Stocks and Bonds","Wall Street"] 
    count = 1
    os.makedirs("dags//src//data//"+formatted_date, exist_ok=True)
    paths=[]
    for word in keywords:
        url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?&q={word}&facet_field=day_of_week&facet=true&begin_date={article_date}&sort=newest&api-key={key}"
 
        r = requests.get(url)

        try:
            for doc in r.json()["response"]["docs"]:
                with open(f"dags//src//data//{formatted_date}//article_{count}.txt", "w") as file:
                    paths.append(f"dags//src//data//{formatted_date}//article_{count}.txt")
                    file.write(doc['lead_paragraph'])
                count += 1
        except Exception as e:   
            pass
    
    logging.info(f"Articles Ingested using Search API")

    url = f"https://api.nytimes.com/svc/topstories/v2/business.json?api-key={story_api_key}"
    r = requests.get(url).json()["results"]
    for item in r:
        if item["subsection"] == "economy":
            with open(f"dags//src//data//{formatted_date}//article_{count}.txt", "w") as file:
                if item["abstract"] is not None:
                    file.write(item["abstract"])
                    paths.append(f"dags//src//data//{formatted_date}//article_{count}.txt")
            count += 1
    logging.info(f"Articles Ingested using Top Stories API")   
    return paths


# paths = get_articles()

if __name__ == "__main__":
    get_articles()

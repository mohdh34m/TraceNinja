import requests
import os
from dotenv import load_dotenv

load_dotenv()

def cli(target):
    api_key = os.getenv('RAPIDAPI_API_KEY')

    if not api_key:
        return []

    url = f"https://subdomain-finder3.p.rapidapi.com/v1/subdomain-finder/"

    querystring = {"domain":{target}}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "subdomain-finder3.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        return []

    data = response.json()["subdomains"]

    subdomains = []
    for item in data:
        subdomains.append(item["subdomain"])

    return list(subdomains)

if __name__ == '__main__':
    cli()
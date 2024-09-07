import requests
import os
from dotenv import load_dotenv
from rich import print as rprint

load_dotenv()

def fetch(target):
    api_key = os.getenv('SECURITY_TRAILS_API_KEY')

    if not api_key:
        return []

    url = f"https://api.securitytrails.com/v1/domain/{target}/subdomains"
    headers = {
        "APIKEY": api_key
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 401:
        rprint("[red1][ERROR] [SecurityTails]","Unauthorized access (401). Please check your API credentials or authentication token.")
        return []
    elif response.status_code == 429:
        rprint("[yellow1][WARNING] [SecurityTails]","Rate limit exceeded (429). You have reached the API request limit. Please wait and try again later.")
        return[]
    
    data = response.json()["subdomains"]

    subdomains = []
    for subdomain in data:
        subdomains.append(f"{subdomain}.{target}")

    return list(subdomains)

if __name__ == '__main__':
    fetch()
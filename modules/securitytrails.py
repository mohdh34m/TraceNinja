import requests
import os
from dotenv import load_dotenv

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

    if response.status_code != 200:
        return []

    data = response.json()["subdomains"]

    subdomains = []
    for subdomain in data:
        subdomains.append(f"{subdomain}.{target}")

    return list(subdomains)

if __name__ == '__main__':
    fetch()
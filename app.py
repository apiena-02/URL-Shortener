import requests
from dotenv import load_dotenv
import os

# Load API key once at the beginning
load_dotenv()
api_key = os.getenv('API_KEY')
api_url = 'https://cutt.ly/api/api.php'

def shorten_url(input_url):
    params = {
        'short': input_url,
        'key': api_key
    }

    response = requests.get(api_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Check API response status for URL shortening success
        if data['url']['status'] == 7:
            print("Shortened URL:", data['url']['shortLink'])
        else:
            print("Error:", data['url']['status'], "Please make sure the link entered is correct and try again!")
    else:
        print("Error:", response.status_code, "Please make sure the link entered is correct and try again!")

if __name__ == "__main__":
    input_url = input("Please enter a URL below: ")
    shorten_url(input_url)

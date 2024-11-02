import requests
import time
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

    # Measure response time
    start_time = time.time()
    response = requests.get(api_url, params=params)
    response_time = time.time() - start_time

    # Print the response time
    print("Response Time:", response_time)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Check API response status for URL shortening success
        if data['url']['status'] == 7:
            print("Shortened URL:", data['url']['shortLink'])
        elif data['url']['status'] == 1:
            print("Error: Invalid URL. Please enter a valid URL.")
        else:
            print("Error:", data['url']['status'], "Please try again!")
    else:
        print("Error:", response.status_code, "Please try again!")

if __name__ == "__main__":
    input_url = input("Please enter a URL below: ")
    shorten_url(input_url)

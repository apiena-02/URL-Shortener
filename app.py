import requests
from dotenv import load_dotenv
import os
load_dotenv()

# Function to check if a URL exists
def check_url_exists(url):
    
    # Try sending a HEAD request to check the URL status
    try:      
        response = requests.head(url) 
        
        # Check if the URL exists based on response status
        if response.status_code == 200:  
            return True    
        else:
            return False
        
    # Error occurred, URL may not exist or unreachable
    except Exception:
        return False

# Main function
def main():
    
    # API key and url for the URL shortening service
    api_key = os.getenv('API_KEY')
    api_url = 'https://cutt.ly/api/api.php'
    
    # Asking user to input a URL
    input_url = input("Please enter a URL below: ")
    
    # Checking if the entered URL exists
    if check_url_exists(input_url):
        
        # Parameters for the API request
        params = {
            'short' : input_url,
            'key' : api_key
        } 
        
        # Sending a GET request to shorten the URL
        response = requests.get(api_url, params=params)
        
        # Parsing response data as JSON
        data = response.json()
        
        # Checking if request was successful
        if response.status_code == 200:
            
            data = response.json()
            
            # Checking if URL was successfully shortened
            if data['url']['status'] == 7:
                print("Shortened URL:", data['url']['shortLink'])
            
            else:
                print("Error:", data['url']['status'], "Please try again!")
                
        else:
            print("Error:", response.status_code, "Please try again!")
            
    else:
        print("URL does not exist or is unreachable.")


if __name__ == "__main__":
    main()

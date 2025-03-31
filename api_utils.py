import requests

def authenticate_user(config):
    #Authenticate and get the user token.
    try:
        url = config["base_url"] + config["auth_endpoint"]
        credentials = {
            "username": config["username"],
            "password": config["password"]
        }


        response = requests.post(url, json=credentials)
        response.raise_for_status()
        data = response.json()
        return data.get("accessToken")
    
    except requests.RequestException as exception:
        print(f"Error fetching data from {url}: {exception}")
        return None

def fetch_data(url, headers=None):
    # Generic function to fetch data from the API.

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    
    except requests.RequestException as exception:
        print(f"Error fetching data from {url}: {exception}")
        return None
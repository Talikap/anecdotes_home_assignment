from api_utils import fetch_data

def collect_user_details(config, token):
    # Collect authenticated user details (E1).

    headers = {"Authorization": f"Bearer {token}"}
    user_url = config["base_url"] + config["user_details_endpoint"]
    user_details = fetch_data(user_url, headers)
    if user_details:
        print("E1: User Details Collected")
    else:
        print("E1: Failed to collect user details")
    return user_details



def collect_evidence(config, token):
    #Main function to collect all evidence.

    user_details = collect_user_details(config, token)

    return {
        "user_details": user_details,
    }

from api_utils import authenticate_user
from evidence_collector import collect_evidence
from utils import load_config
import os

def main():
    config = load_config("config.json")

    token = authenticate_user(config)
    if not token:
        print("Authentication failed. Exiting.")
        return

    collect_evidence(config, token)



if __name__ == "__main__":
    main()
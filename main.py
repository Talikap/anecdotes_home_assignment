from api_utils import authenticate_user
from evidence_collector import collect_evidence
from utils import load_config
from file_utils import save_to_file

def main():
    config = load_config("config.json")

    token = authenticate_user(config)
    if not token:
        print("Authentication failed. Exiting.")
        return

    evidences = collect_evidence(config, token)
    save_to_file(evidences,"output.txt")


if __name__ == "__main__":
    main()
import json


def save_to_file(data, filename):
    #Save data to a file in the current directory.
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")
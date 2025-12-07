from dotenv import load_dotenv
import os
import requests

load_dotenv()
cookie = os.getenv("COOKIE")

if cookie is None:
    raise ValueError("Missing required environment variable: COOKIE")

def download(year: int, day: int, output_file_path: str):
    response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", headers={"Cookie":"session="+cookie})

    response.raise_for_status()

    with open(output_file_path, "w") as file:
        file.write(response.text)

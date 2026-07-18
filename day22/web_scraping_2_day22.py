import requests
from bs4 import BeautifulSoup
import json

url = "https://archive.ics.uci.edu/ml/datasets.php"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

data = []

for table in soup.find_all("table"):
    data.append(table.get_text(" ", strip=True))

with open("uci_datasets.json", "w") as f:
    json.dump(data, f, indent=4)

print("JSON file created successfully!")
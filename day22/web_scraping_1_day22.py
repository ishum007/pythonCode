import requests
from bs4 import BeautifulSoup
import json

url = "http://www.bu.edu/president/boston-university-facts-stats/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

data = {}

for item in soup.find_all(["h2", "h3"]):
    heading = item.get_text(strip=True)
    content = []

    for sibling in item.find_next_siblings():
        if sibling.name in ["h2", "h3"]:
            break
        content.append(sibling.get_text(" ", strip=True))

    data[heading] = content

with open("bu_facts_stats.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Saved to bu_facts_stats.json")
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_(United_Nations)"

import requests
headers = {
    "User-Agent": "Mozilla/5.0 "
}
response = requests.get(url, headers=headers)
tables = pd.read_html(response.text)
df = tables[0]

df.to_json("countries.json", orient="records", indent=4)

print("Saved to countries.json")
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

tables = pd.read_html(response.text)

print("Tables found:", len(tables))

# The presidents table is usually the first table
presidents = tables[0]

presidents.to_json(
    "us_presidents.json",
    orient="records",
    indent=4
)

print("Saved as us_presidents.json")
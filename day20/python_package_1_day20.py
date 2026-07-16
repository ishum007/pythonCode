import requests
import re
from collections import Counter

url = "https://www.gutenberg.org/files/1112/1112.txt"

text = requests.get(url).text

# Convert to lowercase
text = text.lower()

# Extract only words
words = re.findall(r"\b[a-z']+\b", text)

# Count frequency
counter = Counter(words)

print("Top 10 Most Frequent Words:\n")

for word, count in counter.most_common(10):
    print(word, ":", count)
    
import requests
import statistics

url = "https://api.thecatapi.com/v1/breeds"

cats = requests.get(url).json()

weights = []
lifespans = []
countries = []
breeds = []

for cat in cats:

    # Weight
    weight = cat["weight"]["metric"]

    if "-" in weight:
        low, high = weight.split("-")
        avg = (float(low.strip()) + float(high.strip())) / 2
        weights.append(avg)

    # Lifespan
    life = cat["life_span"]

    if "-" in life:
        low, high = life.split("-")
        avg = (float(low.strip()) + float(high.strip())) / 2
        lifespans.append(avg)

    countries.append(cat["origin"])
    breeds.append(cat["name"])

print("Weight Statistics")

print("Minimum:", min(weights))
print("Maximum:", max(weights))
print("Mean:", statistics.mean(weights))
print("Median:", statistics.median(weights))
print("Standard Deviation:", statistics.stdev(weights))

print("\nLifespan Statistics")

print("Minimum:", min(lifespans))
print("Maximum:", max(lifespans))
print("Mean:", statistics.mean(lifespans))
print("Median:", statistics.median(lifespans))
print("Standard Deviation:", statistics.stdev(lifespans))

from collections import Counter

country_freq = Counter(countries)

print("\nCountry Frequency")

for country, count in country_freq.items():
    print(country, ":", count)

breed_freq = Counter(breeds)    
print("\nBreed Frequency")

for breed, count in breed_freq.items():
    print(breed, ":", count)
import requests
from collections import Counter

# Countries API
countries_api = "https://restcountries.com/v3.1/all"

countries_data = requests.get(countries_api).json()

print("Total Number of Countries:", len(countries_data))
print("\n10 Largest Countries:\n")
print("10 Most Spoken Languages:\n")
print("Total Number of Languages:\n")
print("10 Most Populated Countries:\n")
print("10 Least Populated Countries:\n")
print("10 Most Populated Countries in Asia:\n")
largest = sorted(
    countries_data,
    key=lambda x: x.get("area", 0),
    reverse=True
)

print("10 Largest Countries:\n")

for country in largest[:10]:
    print(country["name"]["common"], "-", country.get("area", 0))

# 2. 10 Most Spoken Languages
language_counter = Counter()

for country in countries_data:
    if "languages" in country:
        for language in country["languages"].values():
            language_counter[language] += 1

print("\n10 Most Spoken Languages:\n")

for language, count in language_counter.most_common(10):
    print(language, ":", count)

# 3. Total Number of Languages
all_languages = set()

for country in countries_data:
    if "languages" in country:
        all_languages.update(country["languages"].values())

print("\nTotal Number of Languages:", len(all_languages))

import requests
from bs4 import BeautifulSoup

url = "https://archive.ics.uci.edu/ml/datasets.php"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)

print("\nFirst 20 Links:\n")

links = soup.find_all("a")

for link in links[:20]:
    print(link.get_text(strip=True))



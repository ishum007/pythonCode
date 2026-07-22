import pandas as pd

# Read the hacker_news.csv file
df = pd.read_csv("../../data/hacker_news.csv")

# 1. Get the first five rows
print("First Five Rows:")
print(df.head())

# 2. Get the last five rows
print("\nLast Five Rows:")
print(df.tail())

# 3. Get the title column as a pandas Series
print("\nTitle Column:")
print(df["title"])

# 4. Count the number of rows and columns
print("\nNumber of Rows and Columns:")
print(df.shape)      # (rows, columns)

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 5. Filter the titles which contain Python
print("\nTitles Containing 'Python':")
python_titles = df[df["title"].str.contains("Python", case=False, na=False)]
print(python_titles)

# 6. Filter the titles which contain JavaScript
print("\nTitles Containing 'JavaScript':")
javascript_titles = df[df["title"].str.contains("JavaScript", case=False, na=False)]
print(javascript_titles)

# 7. Explore the data
print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe(include="all"))

print("\nMissing Values:")
print(df.isnull().sum())
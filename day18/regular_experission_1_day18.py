import re
from collections import Counter

paragraph = '''I love teaching. If you do not love teaching what else can you love.
I love Python if you do not love something which can give you all the
capabilities to develop an application what else can you love.'''

def most_frequent_words(text):
    # Remove punctuation
    words = re.findall(r'\b\w+\b', text)

    # Count words
    count = Counter(words)

    # Sort by frequency
    return sorted([(v, k) for k, v in count.items()], reverse=True)

print(most_frequent_words(paragraph))
import re

text = '''
The position of some particles on the horizontal x-axis are -12, -4,
-3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.
'''

# Extract integers
points = re.findall(r'-?\d+', text)

print(points)

# Convert to integers
numbers = list(map(int, points))

print(numbers)

# Distance between furthest points
distance = max(numbers) - min(numbers)

print("Distance =", distance)
import re

def is_valid_variable(variable):
    pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    return bool(re.match(pattern, variable))

print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))
import re
from collections import Counter

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;.
There $is nothing; &as& mo@re rewarding as educa@ting &and&
@emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting
tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    # Keep only letters and spaces
    cleaned = re.sub(r'[^A-Za-z\s]', '', text)
    return cleaned

def most_frequent_words(text):
    words = text.split()
    count = Counter(words)
    return count.most_common(3)

cleaned = clean_text(sentence)

print(cleaned)
print(most_frequent_words(cleaned))
import re
from collections import Counter

def clean_text(text):
    return re.sub(r'[^A-Za-z\s]', '', text)

def most_frequent_words(text):
    stop_words = {
        'and', 'as', 'to', 'be', 'is', 'a', 'am',
        'the', 'this', 'there', 'more'
    }

    words = [
        word for word in text.split()
        if word.lower() not in stop_words
    ]

    count = Counter(words)
    return count.most_common(3)

cleaned = clean_text(sentence)

print(cleaned)
print(most_frequent_words(cleaned))
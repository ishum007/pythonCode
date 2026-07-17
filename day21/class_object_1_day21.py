import math

class Statistics:

    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        data = sorted(self.data)
        n = len(data)

        if n % 2 == 0:
            return (data[n // 2 - 1] + data[n // 2]) / 2
        return data[n // 2]

    def mode(self):
        freq = {}
        for item in self.data:
            freq[item] = freq.get(item, 0) + 1

        mode = max(freq, key=freq.get)
        return (mode, freq[mode])

    def var(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / self.count()
        return round(variance, 1)

    def std(self):
        return round(math.sqrt(self.var()), 1)

    def freq_dist(self):
        freq = {}
        for item in self.data:
            freq[item] = freq.get(item, 0) + 1

        result = []
        for key, value in freq.items():
            percent = round(value * 100 / self.count(), 1)
            result.append((percent, key))

        result.sort(reverse=True)
        return result

    def describe(self):
        print("Count:", self.count())
        print("Sum:", self.sum())
        print("Min:", self.min())
        print("Max:", self.max())
        print("Range:", self.range())
        print("Mean:", round(self.mean()))
        print("Median:", self.median())
        print("Mode:", self.mode())
        print("Variance:", self.var())
        print("Standard Deviation:", self.std())
        print("Frequency Distribution:", self.freq_dist())


# ---------------- MAIN PROGRAM ----------------

ages = [
    31, 26, 34, 37, 27, 26, 32, 32, 26, 27,
    27, 24, 32, 33, 27, 25, 26, 38, 37, 31,
    34, 24, 33, 29, 26
]

data = Statistics(ages)
data.describe()
class PersonAccount:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    # Add income
    def add_income(self, description, amount):
        self.incomes[description] = amount

    # Add expense
    def add_expense(self, description, amount):
        self.expenses[description] = amount

    # Total income
    def total_income(self):
        return sum(self.incomes.values())

    # Total expense
    def total_expense(self):
        return sum(self.expenses.values())

    # Account balance
    def account_balance(self):
        return self.total_income() - self.total_expense()

    # Account information
    def account_info(self):
        print("First Name:", self.firstname)
        print("Last Name:", self.lastname)
        print("Incomes:", self.incomes)
        print("Expenses:", self.expenses)
        print("Total Income:", self.total_income())
        print("Total Expense:", self.total_expense())
        print("Account Balance:", self.account_balance())


# Driver Code
person = PersonAccount("Ishika", "Mahajan")

person.add_income("Salary", 50000)
person.add_income("Freelancing", 10000)

person.add_expense("Food", 5000)
person.add_expense("Rent", 12000)
person.add_expense("Shopping", 3000)

person.account_info()


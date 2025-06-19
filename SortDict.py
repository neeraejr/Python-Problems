# ✅ Problem 2: Sort a Dictionary by its Values (Descending Order)

data = {'apple': 50, 'banana': 20, 'cherry': 40}
data.items()
sorted_data = dict(sorted(data.items(), key = lambda x: x[1], reverse=True))
print(sorted_data)


import matplotlib.pyplot as plt
import pandas as pd

data = {
    "countries": ["UK", "China", "Italy", "Brazil", "USA"],
    "pop_2020": [66.7, 1426, 59.4, 208.6, 331.6],
    "pop_2024": [69.2, 1410, 58.9, 212.0, 340.1]}

DF = pd.DataFrame(data)

DF["percentage_change"] = 100 * (DF["pop_2024"] - DF["pop_2020"]) / (DF["pop_2020"])
print("population grow rate")
print(DF[["countries", "percentage_change"]])

sorted_DF = DF.sort_values(by="percentage_change", ascending=False)

print("\nsorted population grow rate")
print(sorted_DF[["countries", "percentage_change"]])

largest = sorted_DF.iloc[0]
smallest = sorted_DF.iloc[-1]

print(f"\nlargest increase: {largest["countries"]}: {largest["percentage_change"]:.2f}%")
print(f"\nsmallest increase: {smallest["countries"]}: {smallest["percentage_change"]:.2f}%")

plt.figure()
plt.bar(DF["countries"], DF["percentage_change"])
plt.xlabel("countries")
plt.ylabel("Population Change (%)")
plt.title("Population Change (2020–2024)")
plt.show()
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir(r"C:\Users\ZhuanZ\Documents\课件\IBI1\IBI_2025-26\IBI1_2025-26\Practical 10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

dalys_data.head(5)
dalys_data.info()
max_dalys = dalys_data["DALYs"].max()
min_dalys = dalys_data["DALYs"].min()
first_year = dalys_data["Year"].min()
most_recent_year = dalys_data["Year"].max()

print(dalys_data.iloc[0:10,2:4])
# 1998 reported the maximum DALYs for Afghanistan
zimbabwe_dalys = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]
print(zimbabwe_dalys)
# 1990 and 2019 were the first year and last year these data were collected, respectively.

recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
max_dalys_2019 = recent_data["DALYs"].max()
min_dalys_2019 = recent_data["DALYs"].min()

max_country = recent_data.loc[recent_data["DALYs"] == max_dalys_2019, "Entity"].iloc[0]
min_country = recent_data.loc[recent_data["DALYs"] == min_dalys_2019, "Entity"].iloc[0]

print(f"Country with maximum DALYs in 2019: {max_country}, with DALYs of {max_dalys_2019}")
print(f"Country with minimum DALYs in 2019: {min_country}, with DALYs of {min_dalys_2019}")

Singapore_data = dalys_data.loc[dalys_data["Entity"] == "Singapore"]
print("Singapore data from:", Singapore_data["Year"].min(), "to", Singapore_data["Year"].max())
print(f"DALYs in Singapore from 1990 to 2019")
plt.figure(figsize=(10, 6))
plt.plot(Singapore_data["Year"], Singapore_data["DALYs"], marker='o')
plt.title("DALYs in Singapore (1990-2019)")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.grid(True)
plt.show()

avg_dalys = dalys_data.groupby("Entity")["DALYs"].mean()

max_avg_country = avg_dalys.idxmax()
min_avg_country = avg_dalys.idxmin()

print("Highest average DALYs 1990-2019:", max_avg_country)
print("Lowest average DALYs 1990-2019:", min_avg_country)
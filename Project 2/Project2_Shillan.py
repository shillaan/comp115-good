import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "/Users/shillan/Desktop/coding/Project 2/BC census 2016 data.csv",
    encoding="latin1",
    engine="python"
)

df.columns = df.columns.str.strip()

print("DATA LOADED\n")
print(df.head())
print(df.columns)

# ------------------------
# Task1 
# ------------------------
print("\nTASK 1")

high_stress = df[df["shelt_rent_30plus_rate"] > 50]

print(high_stress[["chsa", "shelt_rent_30plus_rate"]])

# ------------------------
# Task2
# ------------------------
print("\nTASK 2")

region_avg = df.groupby("pha")["shelt_rent_30plus_rate"].mean()

print(region_avg)

# Graph
region_avg.plot(kind="bar")
plt.title("Shelter Cost Burden by Region")
plt.ylabel("% of renters spending 30%+ income")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
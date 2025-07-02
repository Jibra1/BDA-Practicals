import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
fruits = pd.read_table("C:/Users/kusha/OneDrive/Desktop/Chetna/fruit_data.txt")

# View first few rows
print(fruits.head())

# View unique fruit names
print(fruits['Fruit_Name'].unique())

# View shape of dataset
print(fruits.shape)

# Group by fruit name (optional check)
a = fruits.groupby("Fruit_Name").size()
print(a)

# Plot fruit type distribution
sns.countplot(x="Fruit_Name", data=fruits)
plt.title("Fruit Type Distribution")
plt.xlabel("Fruit Name")
plt.ylabel("Count")
plt.show()

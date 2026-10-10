import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
print("Loading penguin data...")
df = sns.load_dataset("penguins")

print("-------First Five Rows of Data---------")
print(df.head())

df = df.dropna()

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="species", palette="pastel")
plt.title("Number of Penguins by Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species",
    style="species",
    s=70,
)
plt.title("Bill length vs. Bill depth across species")
plt.xlabel('Bill length (mm)')
plt.ylabel('Bill depth (mm)')
plt.legend(title="Species")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x="species", y="body_mass_g", hue="sex", palette="muted")
plt.title("Body Mass Distribution by Species and Sex")
plt.xlabel("Species")
plt.ylabel("Body Mass (g)")
plt.legend(title="Sex")
plt.tight_layout()
plt.show()

print("\nGenerating pairplot... Close the plot windows to finish.")
sns.pairplot(data=df, hue="species", palette="bright", corner=True)
plt.suptitle("Pairwise Relationships of Penguin Characteristics", y=1.02)
plt.show()
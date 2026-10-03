import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load competitor data
df = pd.read_csv('competitor_data.csv')

# Create dashboard
sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))

plt.subplot(2,2,1)
sns.barplot(x='Platform', y='Avg_Price_PKR', data=df, palette='viridis')
plt.xticks(rotation=30)
plt.title('Pricing Comparison (PKR)')

plt.subplot(2,2,2)
sns.barplot(x='Platform', y='User_Rating', data=df, palette='magma')
plt.xticks(rotation=30)
plt.title('User Rating')

plt.subplot(2,2,3)
sns.barplot(x='Platform', y='Num_Courses', data=df, palette='cool')
plt.xticks(rotation=30)
plt.yscale('log')
plt.title('Num Courses (log scale)')

plt.tight_layout()
plt.savefig('benchmarking_dashboard.png')
plt.show()

print("Dashboard generated successfully")
print("\nInsight: Internee.pk is 100% Free with 4.8 rating - strong USP vs paid competitors")

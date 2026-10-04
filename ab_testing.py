# A/B Testing for Internee.pk Website Optimization
import pandas as pd

# Sample data for homepage test
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Bounce_Rate': [70, 65, 68, 40, 35, 38],
    'Conversion_Rate': [5, 6, 4, 12, 15, 13]
}

df = pd.DataFrame(data)
result = df.groupby('Group').mean()
print(result)
print("Conclusion: Design B is better - Lower Bounce, Higher Conversion")

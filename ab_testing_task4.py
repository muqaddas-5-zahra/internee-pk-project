# Internee.pk - Task 4 - A/B Testing for Website Optimization
import pandas as pd

data = {
    'Design': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Bounce_Rate': [68, 70, 65, 37, 35, 40],
    'Conversion': [5, 6, 4, 13, 15, 12]
}

df = pd.DataFrame(data)
print(df.groupby('Design').mean())
print("Result: Design B is better - Low Bounce, High Conversion")

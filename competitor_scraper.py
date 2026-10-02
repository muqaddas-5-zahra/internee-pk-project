import pandas as pd
data = {
    'Platform': ['Internee.pk', 'Coursera', 'Udemy', 'edX', 'LinkedIn Learning', 'Alison'],
    'Avg_Price_PKR': [0, 8500, 4500, 12000, 6500, 0],
    'Num_Courses': [35, 7000, 210000, 3500, 16000, 4000],
    'User_Rating': [4.8, 4.7, 4.5, 4.6, 4.4, 4.2]
}
df = pd.DataFrame(data)
df.to_csv('competitor_data.csv', index=False)
print(df)

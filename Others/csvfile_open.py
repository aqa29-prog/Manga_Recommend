# put csv data in two-dimensional array
def csvfile_open(file):
    import pandas as pd
    df = pd.read_csv(file, encoding='utf-8', dtype=object).values.tolist()

    return df


file = 'gamble_analysis.csv'
df = csvfile_open(file)
for synopsis in range(len(df)):
    print(df[synopsis][1])

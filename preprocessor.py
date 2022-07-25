import pandas as pd

def preprocess(df,region):
    # filter for summer olympics
    df = df[df['Season'] == 'Summer']
    # merg with region
    df = df.merge(region, on='NOC', how='left')
    # drop duplicates
    df.drop_duplicates(inplace=True)
    # coding for medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df
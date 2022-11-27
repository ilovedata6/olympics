import pandas as pd

def preprocess():
    df = pd.read_csv('athlete_events.csv')
    df_regions = pd.read_csv('noc_regions.csv')
    #filtering for summer olympics
    df = df[df['Season']=='Summer']
    # Merge with df_regions
    df = df.merge(df_regions,on="NOC",how='left')
    #dropping duplicates
    df.drop_duplicates(inplace=True)
    # One-Hot encoding the Medals Column
    df = pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)
    return df
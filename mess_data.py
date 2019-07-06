import random
import pandas as pd
import numpy as np

random.seed(2019)

def add_tall_people(df, frac=0.001):
    nanidx = df.sample(frac=frac).index
    df.iloc[nanidx, 10] = (pd.to_numeric(df.iloc[nanidx, 10].str.slice(0, 3)) + 100).astype(str) + ' cm'
    return df

def add_short_people(df, frac=0.001):
    nanidx = df.sample(frac=frac).index
    df.iloc[nanidx, 10] = (pd.to_numeric(df.iloc[nanidx, 10].str.slice(0, 3)) - 100).astype(str) + ' cm'
    return df


def add_heavy_people(df, frac=0.001):
    nanidx = df.sample(frac=frac).index
    df.iloc[nanidx, 11] = (pd.to_numeric(df.iloc[nanidx, 11].str.slice(0, 2)) + 105).astype(str) + ' kg'
    return df

def add_light_people(df, frac=0.001):
    nanidx = df.sample(frac=frac).index
    df.iloc[nanidx, 11] = (pd.to_numeric(df.iloc[nanidx, 11].str.slice(0, 2)) -50).astype(str) + ' kg'
    return df


def add_nan(df, frac = 0.1):
    nanidx = df.sample(frac=frac).index
    df.iloc[nanidx, :] = np.nan
    
    return df

def change_case(df, frac = 0.3):
    nanidx = df.sample(frac=frac).index
    df.iloc[nanidx, 1] = df.iloc[nanidx, 1].str.upper()
    
    nanidx = df.sample(frac=frac).index
    df.iloc[nanidx, 1] = df.iloc[nanidx, 1].str.lower()
    return df
  
  
def add_impossible_data(df, frac = 0.01):
    nanidx = df.sample(frac=frac/2).index
    df.iloc[nanidx, 10] = (pd.to_numeric(df.iloc[nanidx, 10].str.slice(0, 3)) - 400).astype(str) + ' cm'
    
    
    nanidx = df.sample(frac=frac/4).index
    df.iloc[nanidx, 11] = (pd.to_numeric(df.iloc[nanidx, 11].str.slice(0, 3)) - 400).astype(str) + ' kg'
    
    return df

def perform_modifs(df):
    df = add_tall_people(df)
    df = add_short_people(df)
    df = add_heavy_people(df)
    df = add_light_people(df)
    df = add_nan(df)
    df = change_case(df)
    df = add_impossible_data(df)
    return df

data = pd.read_csv('OGFullData.csv')
data = perform_modifs(data)

data.to_csv('FullData.csv', index=False)
from ucimlrepo import fetch_ucirepo
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


def glass_types_data(): 
  
    # fetch dataset 
    glass_identification = fetch_ucirepo(id=42) 
  
    # data (as pandas dataframes) 
    X = glass_identification.data.features 
    y = glass_identification.data.targets 
  
    # # metadata 
    # print(glass_identification.metadata) 
  
    # # variable information 
    # print(glass_identification.variables)

    # features of rows (glass samples)
    feature_names = glass_identification.variables[glass_identification.variables['role'] == 'Feature']['name'].tolist()
    # glass types for each row
    target_name = glass_identification.variables[glass_identification.variables['role'] == 'Target']['name'].values[0]

    #putting into dataframe using pandas
    df = pd.DataFrame(glass_identification.data.features, columns=feature_names)
    df[target_name] = glass_identification.data.targets

    return df, target_name


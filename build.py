import pandas as pd

def load_data():
    olympics_data = pd.read_csv("files/olympics.csv", skiprows =1)
    for column in olympics_data.columns:
        if '01' in column:
            olympics_data.rename(inplace=True, columns = {column:column.replace("01 !","Gold")})
        elif '02' in column:
            olympics_data.rename(inplace=True, columns = {column:column.replace("02 !","Silver")})
        elif '03'in column:
            olympics_data.rename(inplace=True, columns = {column:column.replace("03 !","Bronze")})
        else:
            pass

    country_names = [x.split('\xc2\xa0(')[0] for x in olympics_data.iloc[:,0]]
    olympics_data.set_index(pd.Series(country_names), inplace=True)
    olympics_data.iloc[:,0] = country_names
    olympics_data.drop(['Totals'], inplace= True)
    return olympics_data

def first_country(df):
    return df.iloc[0,:]

def gold_medal(df):
    return df.iloc[:,12].idxmax()

def biggest_difference_in_gold_medal(df):
    comparison_data = df.iloc[:,[0,5,10]]
    comparison_data['Difference'] = comparison_data.iloc[:,1] - comparison_data.iloc[:,2]
    return comparison_data.iloc[:,3].idxmax()

def get_points(df):
    df['Points'] = 3*df.iloc[:,12]+2*df.iloc[:,13]+df.iloc[:,14]
    return df.loc[:,'Points']

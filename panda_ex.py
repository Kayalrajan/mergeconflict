import pandas as pd
def fun(path):
    df=pd.read_csv(path).head(10)
    for columns in df.columns:
        if df[columns].isnull().sum()>0:
            print(columns)
        

fun('/Users/sarva/OneDrive/Desktop/Kayalvizhi/Python/Employee_Sample_1.txt')

import pandas as pd
path='C:/Users/sarva/OneDrive/Desktop/Kayalvizhi/Python/Employee_Sample.csv'
df=pd.read_csv(path,encoding='ANSI')
df.info()
df=df.assign(newcol=df[Exit date !='NaN'])
df.sample(5)
#df.describe()
#df.sample(10)

import pandas as pd

df=pd.read_csv('Name.csv')


#FINDING MAX AND MIN
p=df['ColumnName'].max()
q=df['ColumnName'].min()


print(q)

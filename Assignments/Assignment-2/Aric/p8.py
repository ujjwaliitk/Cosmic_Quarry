import pandas as pd 
df=pd.DataFrame({'Name':['Aric','Eric','Ariana','Selena','Lana'],'Course':['ME','CSE','CHE','AE','EE'],'Marks':[92,None,46,None,87]})
filled=df['Marks'].fillna(df['Marks'].mean())
print(filled)
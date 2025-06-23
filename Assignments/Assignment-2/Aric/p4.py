import pandas as pd 
df=pd.read_csv(r"C:\Users\SUNNY DAVID\Downloads\student_age_marks.csv")
df=df[df['Marks']>90]
print(df)
import matplotlib.pyplot as plt
import pandas as pd 
df=pd.read_csv(r"C:\Users\SUNNY DAVID\Downloads\student_age_marks.csv")
plt.hist(df['Marks'])
plt.show()
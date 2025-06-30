import matplotlib.pyplot as plt 
import pandas as pd 
df=pd.read_csv(r"C:\Users\SUNNY DAVID\Downloads\student_age_marks.csv")
plt.scatter(df['Marks'],df['Age'])
plt.title('Age vs Marks')
plt.xlabel('Marks')
plt.ylabel('Age')
plt.show()
import pandas as pd 
course=pd.DataFrame({'Name':['Aric','Eric','Ariana','Selena'],
                      'Course':['ME','CSE','CHE','AE']})
marks=pd.DataFrame({'Name':['Aric','Eric','Ariana','Selena'],'Marks':[92,98,78,87]})
new=pd.merge(course,marks,on='Name')
print(new)
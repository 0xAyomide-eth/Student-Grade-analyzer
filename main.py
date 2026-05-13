#import pandas, matplotlib and seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reading the csv file
df = pd.read_csv('student_scores.csv')
# get all courses and put them in a list
subject_cols = ['CSC202','MTH202','IFT212','MCT214']
#total and average
df['Total'] = df[subject_cols].sum(axis=1)
df['average'] = (df['Total']/len(subject_cols)).round(2)
#function to find point average
def pointavg(avg):
  if avg >= 90: return 5
  elif avg >= 80: return 4
  elif avg >= 70: return 3
  elif avg >= 60: return 2
  else: return 1
#function for grading
def grades(avg):
  if avg >= 90: return 'A'
  elif avg >= 80: return 'B'
  elif avg >= 70: return 'c'
  elif avg >= 60: return 'D'
  else: return 'failed'
#function for remark
def remark(msg):
  if msg >= 5: return "meggga win performance star!!"
  if msg >= 4: return "excellent performance!"
  elif msg>= 3: return "nice work"
  elif msg >= 2: return "good you can do better"
  else: return "poor performance"

#getting the grades for the student
df['grade'] = df['average'].apply(grades)
#getting the point average needed for remark
df['point_avg'] = df['average'].apply(pointavg)
#remark
df['remarks'] = df["point_avg"].apply(remark)
#student ranking
df["Rank"] = df["average"].rank(ascending=False, method="min").astype(int)
df = df.sort_values("Rank").reset_index(drop=True)
#result
result = df[["Rank", "Names", "Total", "average", "grade","point_avg","remarks"]]
print(result)

#barplot
sns.set_theme(style="whitegrid", context="talk")
sns.barplot(data=df, x="Names", y="average")
plt.show()

#scatterplot
scatterplt = sns.scatterplot(data=df, x="Names", y="average")
plt.show()

#displot
sns.displot(df["average"], kde=True) # kde=True adds a smooth trend line
plt.show()
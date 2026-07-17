import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("/home/melancholy/Downloads/Advertising.csv")
print(data.head())
print(data.shape)
print(data.isnull().sum())
print(data.info())
print(data.nunique())
print(data.nunique().sum())
print(data["Unnamed: 0"])
print(data.value_counts())

df = data.copy()
df.drop(columns =['Unnamed: 0'],inplace= True)

fig, axes = plt.subplots(2, 2, figsize=(15, 7), sharex=False)
sns.distplot(df["Sales"],color="red",ax=axes[0,0])

sns.distplot(df["TV"],color="blue",ax=axes[0,1])

sns.distplot(df["Radio"],color="orange",ax=axes[1,0])

sns.distplot(df["Newspaper"],color="purple",ax=axes[1,1])

plt.show()


jp1 = sns.jointplot(x="Newspaper",y="Sales",data = df,kind = "reg")
plt.show()
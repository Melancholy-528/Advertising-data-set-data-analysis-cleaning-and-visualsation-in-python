import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

#data exploration
data = pd.read_csv("/home/melancholy/Downloads/Advertising.csv")
print(data.head())
print(data.shape)
print(data.isnull().sum())
print(data.info())
print(data.nunique())
print(data.nunique().sum())
print(data["Unnamed: 0"])
print(data.value_counts())

#dropping needless columns
df = data.copy()
df.drop(columns =['Unnamed: 0'],inplace= True)

#distplot
fig, axes = plt.subplots(2, 2, figsize=(15, 7), sharex=False)
sns.distplot(df["Sales"],color="red",ax=axes[0,0])
sns.distplot(df["TV"],color="blue",ax=axes[0,1])
sns.distplot(df["Radio"],color="orange",ax=axes[1,0])
sns.distplot(df["Newspaper"],color="purple",ax=axes[1,1])
plt.show()

#joinplot1
jp1 = sns.jointplot(x="Newspaper",y="Sales",data = df,kind = "reg")
plt.show()

#joinplot2
jp1 = sns.jointplot(x="Radio",y="Sales",data = df,kind = "reg")
plt.show()

#heatmap
numeric_df = df.select_dtypes(include=["number"])
corr_matrix = numeric_df.corr()
hm1 = sns.heatmap(corr_matrix,cmap="coolwarm")
plt.show()

#pairplot
pp1 = sns.pairplot(data,height = 2,aspect = 1.45)
plt.show()
 
#pairplot2
pp2 = sns.pairplot(df,x_vars = ["TV","Radio","Newspaper"],y_vars="Sales",size = 5,aspect=1,kind = "reg")
plt.show()

#feature selection
features = ["TV","Radio","Newspaper"]
target = ["Sales"]

x_train,x_test,y_train,y_test = train_test_split(data[features],data[target],test_size=0.2,random_state=4000)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

RE=LinearRegression()
RE.fit(x_train,y_train)

pred = RE.predict(x_test)
pred = pd.DataFrame({'actual': y_test.values.ravel(),'predicted': pred.ravel()})
print(pred.head(10))

plt.figure(figsize=(14, 7))
plt.plot(y_test.values[:100],color = "blue",marker = "o",label = "actual")
plt.plot(pred.values[:100],color = "red",marker = "*",label = "predicted")
plt.title("actual v/s predicted")
plt.xlabel("actual val")
plt.ylabel("pred val")
plt.legend()
plt.grid()
plt.show()



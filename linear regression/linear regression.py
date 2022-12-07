from ast import increment_lineno
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
df= pd.read_csv("homeprices.csv") 
#plt.xlabel('areas')
#plt.ylabel('prices(US$)')
#plt.scatter(df.areas,df.prices,color='blue',marker='+')
new_df=df.drop('prices',axis='columns')
price=df.prices
reg=linear_model.LinearRegression()
reg.fit(new_df,price)
d=pd.read_csv("areas.csv")
p=reg.predict(d)
d['prices']=p
d.to_csv("prediction.csv",index=False)

import numpy as np
import pandas as pd

#
# sales = [0,5,155,0,518,0,1827,616,317,325]
# sales_series = pd.Series(sales,name="Sales")
# print(sales_series.index)
#
# product = ["coffee","banana","tea","coconut","sugar"]
# sales = [0,5,155,0,518]
# # series = pd.Series(range(5),name= "Test").astype("int")
# # series.name = "Daniel"
# # series.index=[10,20,30,40,50]
# # series_float = series.astype("bool")
#
# sales_series = pd.Series(sales,index=product,name="sale")
# print(sales_series["sugar"])
# # print(sales_series[2])
# print(sales_series.iloc[2:4])
# sales_series.index=[0,1,20,3,5]
#
# print(sales_series.reset_index(drop=True))
# print(sales_series.index)
# print(sales_series[sales_series != 5])

product = ["coffee","coffee","tea","coconut","sugar"]
sales = [0,np.NAN,155,0,518]
sales_series = pd.Series(sales,index=product,name="sale")
# print(sales_series.reset_index(drop=True).loc[0:2])
# mask = (sales_series > 0) & (sales_series.index == "coffee")
# print(sales_series.loc[mask])
# mask=(sales_series.eq(5))
# print(sales_series.eq(5))
# print(sales_series.loc[~sales_series.isin([0,5])])
# print(sales_series.loc[~sales_series.gt(5)])
#
# sales_series.index.isin(["coffee"])
# print(sales_series.index.isin(["coffee"]).sum())
# print(np.sum(sales_series.index.isin(["coffee"])))
# print(np.sum(~sales_series.index.isin(["coffee"])))
# print(~sales_series.index.isin(["coffee"]))
# print(sales_series.sort_values(ascending=False))
# print(sales_series.sort_index(ascending=False))
# sales_index = pd.Series(sales)
# print(sales_index + 2)
#
# print("$"+sales_index.astype("float").astype("string"))
sales_series2 = sales_series.add(1,fill_value=0).astype("int")
print(sales_series.add(sales_series2,fill_value=0)/2)
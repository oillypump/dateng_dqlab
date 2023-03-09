import pandas as pd
import numpy as np



# # Creating series from numpy array (1D)
# arr_series = np.array([1,2,3,4,5,6,6,7])
# ex_series = pd.Series(arr_series)
# print(ex_series)
# # Creating dataframe from numpy array (2D)
arr_df = np.array([[1,2,3,5],
                   [5,6,7,8],
                   ['a','b','9',10]])
df = pd.DataFrame(arr_df)
# print(ex_df)

ax = df.iloc[2,'a':'b'] = [11,12]
print(ax)
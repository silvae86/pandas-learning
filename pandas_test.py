#From https://www.youtube.com/watch?v=0UA49Ds1XXo

#brew install python3
#pip3 install pandas
#to run: python3 pandas.py

import pandas as pd
import numpy as np

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats)

# print(df.head())
#
# print("----------------------------")
#
# df.set_index('Day', inplace=True)
# print(df.tail(2))

#print(df['Visitors'])
#print(df.Visitors)
#print(df[['Bounce Rate','Visitors']])

#print(df[['Bounce Rate','Visitors']])
#print(np.array(df[['Bounce Rate','Visitors']]))

df2 = pd.DataFrame(np.array(df[['Bounce Rate','Visitors']]))
print(df2)

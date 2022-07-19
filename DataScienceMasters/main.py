import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

desired_width = 500

pd.set_option('display.width', desired_width)

np.set_printoptions(linewidth=desired_width)

pd.set_option('display.max_columns', 30)
# Get data and number of masters
data = pd.read_csv("Data_Science_Masters_US.csv")
print('Number of Masters in the US')
print(len(data.loc[data['TYPE'] == 'M']))
# print(data.dtypes)
# print(data.info)

# Masters in California and Florida
# Cali = data[(data['STATE'] == 'California') & (data['TYPE']=='M')]
# Florida =data.loc[(data['STATE'] == 'Florida') & (data['TYPE']=='M')]
# print('Number of Masters in California is: ')
# print(len(Cali))


x = str(input("Write the state you want to know information about:  "))
dm = data.loc[(data['STATE'] == x) & (data['TYPE'] == 'M') & (data['DELIVERY'] != 'Online')]

print(dm[['PROGRAM', 'CITY', 'SCHOOL']])
print('Number of Masters in ' + x + ' is: ')
print(len(x))


dm.to_csv(r'masters.csv', index=False)

# show 
# Cali.to_csv(r'Cali.csv', index=False)


# print(data.groupby("STATE",0,)['STATE'].count())

########################################################################################################

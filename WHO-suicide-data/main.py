import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
plt.style.use('seaborn-dark')
plt.rcParams['figure.figsize'] = (15, 10)

data = pd.read_csv("who_suicide_statistics.csv")
data.dropna(axis=0,inplace =True)
data.isnull().sum()

label_encoder = preprocessing.LabelEncoder()
data.sex = label_encoder.fit_transform(data.sex) 
data.age = label_encoder.fit_transform(data.age)

usa = data[data['country']=='United States of America']
usa_years = np.unique(usa.year)
russia = data[data['country']=='Russian Federation']
russia_years = np.unique(russia.year)

usa_list = []
usa_dict = {}
russia_list = []
russia_dict = {}

for i in usa_years:
    usa_sum = usa[usa['year'] == i]['suicides_no'].values.sum()
    usa_dict[i] = usa_sum

usa_list.append(usa_dict)
usa_years_df = pd.DataFrame(usa_list)
usa_years_df = np.transpose(usa_years_df)
usa_years_df.columns = ['Suicides']

russia_list = []
russia_dict = {}

for i in russia_years:
    russia_sum = russia[russia['year'] == i]['suicides_no'].values.sum()
    russia_dict[i] = russia_sum 

russia_list.append(russia_dict)
russia_years_df = pd.DataFrame(russia_list)
russia_years_df = np.transpose(russia_years_df)
russia_years_df.columns = ['Suicides'] 

plt.plot(usa_years_df, ls="-", lw=2)
plt.plot(russia_years_df, ls="--", lw=2)
plt.title('Number of suicides in the US and Russia')
plt.xlabel('Years')
plt.ylabel('Number of suicides')
plt.yticks([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000], ['10k', '20k', '30k', '40k', '50k', '60k', '70k', '80k'])
plt.legend(['USA', 'Russia'], loc='best')
plt.grid()
plt.show()

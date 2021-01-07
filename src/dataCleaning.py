import os
import pandas as pd 
from os import listdir

# data cleaning
data_base_oath = r'D:\UrbanGeo\PopData'
for i in listdir(r'D:\UrbanGeo\PopData'):
    data = pd.read_csv(os.path.join(data_base_oath, i), encoding='big5') 
    new_header = data.iloc[0] #grab the first row for the header
    data = data[1:] #take the data less the header row
    data.columns = new_header #set the header row as the df header
    data.to_csv(os.path.join(data_base_oath, i[0:i.index("年")]+'clean.csv'), encoding='utf8')

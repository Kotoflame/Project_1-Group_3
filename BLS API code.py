# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:33:44 2023

@author: RyanD
"""
import requests
import json
import pandas as pd

APIDataPath = '../Resources/API_Data/'
AnalyzedDataPath = '../Resources/Data_Analysis/'
FiguresPath = '../Resources/Figures/'

# In[1]:   BLS inputs

#For scraping BLS. First get the series you are interested in. Searchable at:  https://beta.bls.gov/dataQuery/find?st=0&r=20&s=popularity%3AD&fq=survey:[cu]&more=0
# you can view the series online at, for e.g.: https://beta.bls.gov/dataViewer/view/timeseries/CUUR0000SAF1

SaveName = f'{APIDataPath}BLS_data_01.csv'

from api_keys import BLS_key
BLSUrl = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'

Series1 = 'CUUR0000SAF1' #'Food in U.S. city average, all urban consumers, not seasonally adjusted'
Series2 = 'PCU484122484122P' #'PPI industry data for General freight trucking, long-distance LTL-Primary services, not seasonally adjusted'
Series3 =  'WPU3014' #'PPI Commodity data for Transportation services-Air transportation of freight, not seasonally adjusted'
Series4 =  'WPU3013' #'PPI Commodity data for Transportation services-Water transportation of freight, not seasonally adjusted'
Series5 = 'CUSR0000SETA' #'New and used motor vehicles in U.S. city average, all urban consumers, seasonally adjusted'

SeriesList = [Series1, Series2, Series3, Series4, Series5]
TitleList = ['CPI: Food',
             'PPI: Trucking', 
             'PPI: Air Freight',
             'PPI: Water Freight',
             'CPI: motor vehicles']
SeriesDict = {SeriesList[i] : TitleList[i] for i in range(len(SeriesList))}

StartYear = '2013'
EndYear = '2023'




# In[2]: request setup and place  


headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": SeriesList,"startyear":StartYear,
                   "endyear":EndYear,"registrationkey":BLS_key})
p = requests.post(BLSUrl, data=data, headers=headers)
json_data = json.loads(p.text)

# In[3]: dataframe formatting

BLS_Dataframe = pd.DataFrame({'SeriesID':[],
                              'Year':[],
                              'Period':[],
                              'Month':[],
                              'PPI/CPI':[],
    })

for result in json_data['Results']['series']:
    SeriesID = result['seriesID']
    for item in result['data'] :
        year = item['year']
        period = item['period']
        month = item['periodName']
        value = float(item['value'])
        
        BLS_Dataframe.loc[len(BLS_Dataframe.index)] = [SeriesID, year,period,month,value] 

# In[3]: dataframe formatting

BLS_Dataframe = BLS_Dataframe.replace({'SeriesID' : SeriesDict})
    
BLS_Dataframe.to_csv(SaveName)
    
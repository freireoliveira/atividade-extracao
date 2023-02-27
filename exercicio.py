import pandas as pd
import requests as re
from datetime import datetime as dt

day_dict = {
    1 : 'Monday',
    2 : 'Tuesday',
    3 : 'Wednesday',
    4 : 'Thursday',
    5 : 'Friday',
    6 : 'Saturday',
    7 : 'Sunday'
}

table = pd.DataFrame()

for year in range(2019, 2031):
  request = re.get(f'https://calendarific.com/api/v2/holidays/?&api_key=5513a9d46231145743590d899efdcae3df210c60&country=BR&year={year}')
  temp_table = pd.DataFrame(request.json()['response']['holidays'])
  colunas = ['name', 'date']
  temp_table = temp_table[~temp_table['name'].str.contains('Equinox', na = False)]
  temp_table = temp_table[~temp_table['name'].str.contains('Solstice', na = False)].reset_index(drop=True)
  temp_table = temp_table[colunas]
  temp_table['date'] = [dt.strptime(x['iso'], '%Y-%m-%d') for x in temp_table['date']]
  temp_table['weekday'] = [day_dict[temp_table['date'][i].isoweekday()] for i in range(len(temp_table))]
  temp_table.columns = ['Name', 'Date', 'Weekday']
  table = pd.concat([table,temp_table])
  
table = table.reset_index(drop=True)

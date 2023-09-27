import pandas as pd
from random import randint

# create list of dates
start_date = 231001
date_list = []
for i in range(31):
    date_list.append(start_date + i)


data_df = pd.DataFrame(columns=['date','max_emp','currently_working','currently_active',
                                'current_waiting_time','calls_at_9',
                                'calls_at_10',
                                'calls_at_11',
                                'calls_at_12',
                                'calls_at_13',
                                'calls_at_14',
                                'calls_at_15',
                                'calls_at_16'
                                ])

# define max employees here
max_emp = 18

# create mockup data per date in date_list and append to the data_df using pd.concat
for date in date_list:

    currently_working = randint(10,max_emp)
    currently_active = randint(9,currently_working)
    current_waiting_time = randint(0,5)

    data_dict = dict(date=[date],max_emp=[max_emp], currently_working=[currently_working], 
                currently_active=[currently_active], current_waiting_time=[current_waiting_time], 
                calls_at_9=[randint(90,150)],
                calls_at_10=[randint(90,150)],
                calls_at_11=[randint(90,150)],
                calls_at_12=[randint(90,150)],
                calls_at_13=[randint(90,150)],
                calls_at_14=[randint(90,150)],
                calls_at_15=[randint(90,150)],
                calls_at_16=[randint(90,150)],
                )

    data_df = pd.concat([data_df, pd.DataFrame(data_dict)])

# set index to date
data_df.set_index('date', inplace=True)

# export dataframe as csv
data_df.to_csv('data/testData_month_orig.csv')



import pandas as pd
import numpy as np
import csv
from datetime import datetime as dt
import openpyxl as xl

filename = dt.now().strftime("%d-%m-%Y.csv")
finalfile = dt.now().strftime("Final %d-%m-%Y.csv")

data = pd.read_csv(filename)

with open(finalfile,'w',newline='\n') as f:

    writer = csv.writer(f)
    
    col_name = ["Name","Date","In Time","Out Time"]

    writer.writerow(col_name)
    
    unq = data['Name'].unique()

    for i in unq:
        
        uniq = data[(data['Name'] == i)]        

        inDate = uniq.at[uniq.head(1).index.values[0], 'Date']
        inTime = uniq.at[uniq.head(1).index.values[0], 'Time']
        outTime = uniq.at[uniq.tail(1).index.values[0], 'Time']
        
        report = [i , inDate , inTime , outTime]
        writer.writerow(report)

from datetime import datetime
import pandas_datareader.data as web


start=datetime(2019,1,1)
end=datetime(2019,12,31)
df=web.get_data_yahoo('TSLA',start,end)
print(df)
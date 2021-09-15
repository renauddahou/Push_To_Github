#comparing QQQ, SPY, DIA stocks
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas_datareader.data as web 
import datetime as dt
from datetime import datetime
start = dt.datetime(2020,1,1)
end = dt.datetime.now()
QQQ = web.DataReader("QQQ",'yahoo',start,end)
SPY = web.DataReader("SPY",'yahoo',start,end)
DIA = web.DataReader('DIA','yahoo',start,end)
plt.plot(QQQ['Low'],label='QQQ Low')
plt.plot(DIA['Low'],label='DIA Low')
plt.plot(SPY['Low'],label='SPY Low')
plt.legend()
plt.show()
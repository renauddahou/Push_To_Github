#comparing cryptocurrencies
import pandas_datareader as web
import datetime as dt
import mplfinance as mpf
import matplotlib.pyplot as plt 
import seaborn as sns #creates a heatmap
currency = "USD"
metric = "Open"
start = dt.datetime(2021, 1, 1)
end = dt.datetime.now()
crypto = ['BTC','ETH','LTC']
colnames = []
first = True
for ticker in crypto:
    data = web.DataReader(f'{ticker}-{currency}',"yahoo",start, end)
    if first:
        combined = data[[metric]].copy()
        colnames.append(ticker)
        combined.columns = colnames
        first = False 
    else:
        combined = combined.join(data[metric])
        colnames.append(ticker)
        combined.columns = colnames
plt.yscale("Log")
for ticker in crypto:
   plt.plot(combined[ticker],label= ticker)
plt.legend(loc="upper right")
#combined = combined.pct_change().corr(method="pearson")
#sns.heatmap(combined, annot= True, cmap="coolwarm")
plt.show()
#cryptocurrencies: BTC, ETH, BTC-USD, USDT, ADA, XRP,BNB, LTC, and more
#mplfinance allows these graph types: 'candle', 'line', 'renko', 'pnf'.
#mplfinance allows plot moving averages using 'mav' keyword
#mplfinance allows display volume using 'volume' keyword
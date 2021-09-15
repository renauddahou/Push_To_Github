#Getting data using data reader
import pandas
import pandas_datareader.data as web
import datetime 
start = datetime.datetime(2021,1,1)
end = datetime.datetime.now()
palantir = web.DataReader("PLTR", 'yahoo', start, end)
#print(palantir)
palantir.to_csv("palantir.csv", index=False)
palantir_saved_file = pandas.read_csv("palantir.csv")
print(palantir_saved_file)
#amazon = web.DataReader("AMZN", 'yahoo', start, end) #D.R. syntax: (name=,source=,start=,end=)
#google = web.DataReader("GOOGL", 'yahoo', start, end)
#disney = web.DataReader("DIS", 'yahoo', start, end)
#print(amazon)
#turning data into csv files
#amazon.to_csv("amazon.csv", index=False)
#amazon_saved_file = pandas.read_csv("amazon.csv")
#print(amazon_saved_file)
#google.to_csv("google.csv", index=False)
#google_saved_file = pandas.read_csv("google.csv")
#print(google_saved_file)
#disney.to_csv("disney.csv", index=False)
#disney_saved_file = pandas.read_csv("disney.csv")
#print(disney_saved_file)
import matplotlib.pyplot as plt 
stocks = ['MSFT','AAPL','DIS','CAT']
shares = [1,3,7,9]
plt.bar(stocks,shares, color=['green','blue','orange','yellow'])
plt.title("Stocks")
plt.show()

cars = ['Lambo','Tesla','Porsche','Ferrari']
prices = [12000,14000,2000,30000]
#plt.pie(prices, labels=cars)
#plt.show()
#.bar() is how you create a bar graph. to create colors: use "color=[]" as parameter
#.pie() is how you create a pie graph
#'autopct=' allows you to add percentages to the pie chart. formatted as: '%f%'
#.scatter() is how you create a scatter plot
#.plot() just gives you a line graph
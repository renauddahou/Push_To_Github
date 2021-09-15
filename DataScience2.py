import pandas #pandas is a module in python
mydataset = {'cars':['BMW','Volvo','Ford'], 'passings':[3,7,2]}
myvar = pandas.DataFrame(mydataset) #DataFrame is a data set within pandas. its formatted as a table
print(myvar)
a = [1,7,2]
myvar1 = pandas.Series(a) #a series is in a DataFrame, 1D array holding data of any type
print(myvar1)
b = [2,4,6]
myvar2 = pandas.Series(b, index=["x","y","z"]) #use "index=" to create labels/also used to name indexes
print(myvar2)
calories = {"day 1":420,"day 2": 380, "day 3": 390} #create a series from a dictionary
myvar3 = pandas.Series(calories)
print(myvar3)
c = {'show': ['Glee', 'Greys','Scandal'],'time':[8,9,10]}
myvar4 = pandas.DataFrame(c)
print(myvar4.loc[0]) #use '.loc' to locate a row

#read csv from online resource:
titanic_data = pandas.read_csv(r'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
print(titanic_data.head()) #head() method gives first 5 rows of DataFrame
print(titanic_data.tail()) #tail() method gives last 5 row of the DataFrame 
print(titanic_data.info()) #gives information about the DataFrame

#write csv files. Here we are turning a DataFrame into a CSV:
cities = pandas.DataFrame([['San Jose', 'California'],['Atlanta','Georgia'],['Miami','Florida']], columns= ['City', 'State'])
cities.to_csv('cities.csv', index= False) #setting 'index=' to FALSE helps clean up data
cities_saved_file = pandas.read_csv('cities.csv')
print(cities_saved_file)

#Read JSON:
#JSON objects are in the same format as a python dictionary
data = { "Duration":{ "0":60,"1":60,"2":60,"3":45,"4":45,"5":60},"Pulse":{"0":110,"1":117,"2":103,"3":109,
"4":117,"5":102},"Maxpulse":{"0":130,"1":145,"2":135,"3":175,"4":148, "5":127},"Calories":{"0":409,"1":479,
"2":340,"3":282,"4":406,"5":300}}
df = pandas.DataFrame(data)
print(df) 
import matplotlib.pyplot as plt 
import numpy as np 
import sklearn
from sklearn import datasets, linear_model #Linear Regression: supervised learning
house_price = [245,312,279,308,199,219,405,324,319,255]
size = [1400,1600,1700,1875,1100,1550,2350,2450,1425,1700]
size2 = np.array(size).reshape((-1,1))
#print(size)
#print(size2)
regr = linear_model.LinearRegression()
regr.fit(size2,house_price)
#print("Coefficients: \n", regr.coef_)
#print("Intercept: \n", regr.intercept_)
def graph(formula, x_range): #formula obtained for the trained model
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x,y)
#plotting the prediction line:
graph('regr.coef_*x + regr.intercept_', range(1000, 2700))
plt.scatter(size, house_price, color='black')
plt.ylabel('house price')
plt.xlabel('size of house')
#plt.show()
#Unsupervised Learning: helps solve complex tasks
from sklearn.cluster import KMeans #KMeans Clustering Method
from matplotlib import style
x = [1,5,1.5,8,1,9]
y = [2,8,1.8,8,0.6,11]
plt.scatter(x,y)
#plt.show()
x1 = np.array([[1,2],[5,8],[1.5,1.8],[8,8],[1,0.6],[9,11]])
kmeans = KMeans(n_clusters=2)
kmeans.fit(x1)
#getting value of centroids and labels based on fitment:
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
#print(centroids)
#print(labels)
#plotting output:
colors = ['g','r','c','y']
for i in range(len(x1)):
    print("coordinate:",x1[i],"label:",labels[i])
    plt.plot(x1[i][0],x1[i][1], colors[labels[i]], markersize= 10)
plt.scatter(centroids[:,0], centroids[:,1], marker= 'x', s=150, linewidths=5, zorder=10)
plt.show()
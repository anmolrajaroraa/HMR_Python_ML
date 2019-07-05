#pip install pandas
import pandas as pd
#pip install matplotlib
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
dataset = pd.read_csv('SaratogaHouses.csv')
print(dataset.head())
fig = plot.figure()
axes3d = Axes3D(fig)
#print(dataset.columns)
x = dataset['livingArea']
y = dataset['price']
z = dataset['landValue']
axes3d.scatter(x,y,z)
plot.show()

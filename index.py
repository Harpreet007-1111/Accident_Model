import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

 # creating an array
numbers = np.array([1, 2, 3, 4, 5])
print("ID Array", numbers)

# creating a series using panda
series = pd.Series([1, 2, 3, 4, 5,])
print("Series: \n", series)

# # creating a dataframe using panda
record = {
    'Name': ["John", "Alice", "Charlie"],
    'Age': [23, 25, 28],
    'City': ["New York", 'Los Angeles', "Chicago"]
}
dataframe = pd.DataFrame(record)
print("Dataframe: \n", dataframe)

# creating graphs using matplotlib
even = [2, 4, 6, 8, 10]
prime = [2, 3, 5, 7, 11]
plt.plot(even, prime)
plt.xlabel('Odd Numbers')
plt.ylabel('Even Numbers')
plt.title('A Simple Graph of Even and Odd numbers')
plt.show()

# Ploting a graph using Seaborn
data = sns.load_dataset('iris')
sns.lineplot(data=data, x='sepal_length', y='sepal_width', hue='species')
plt.show()

# data mining using load iris
records = load_iris()
print("Features: ", records['feature_names'])
print('Target names: ', records['target_names'])
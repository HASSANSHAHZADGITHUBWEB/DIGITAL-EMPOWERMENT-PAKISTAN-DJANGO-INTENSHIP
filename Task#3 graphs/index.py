# NAME : MUHAMMAD HASSAN SHAHZAD

import pandas as pd
import matplotlib.pyplot as plt
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
data = pd.read_csv(url, names=names)
print(data.describe())

data.hist(figsize=(10, 10))
plt.show()

# scatter graph
#plt.scatter(data['sepal-length'], data['sepal-width'])
#plt.xlabel('Sepal Length')
#plt.ylabel('Sepal Width')
#plt.title('Sepal Length vs Sepal Width')
#plt.show()

# box plot
#data.boxplot(figsize=(10, 10))
#plt.show()

# pie chart
#class_counts = data['class'].value_counts()
#plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%')
#plt.title('Class Distribution')
#plt.show()
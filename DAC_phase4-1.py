
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
product=pd.read_csv("statsfinal.csv")
product


mean = np.mean(product)
mean


std_dev = np.std(product)
std_dev



from matplotlib import pyplot as plt
x = mean
y = std_dev
plt.plot(mean,std_dev)
plt.title("Line graph")
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()


sales_data = {
    'Product Q1': 2244.027367,
    'Product Q2': 1089.665243,
    'Product Q3': 1671.650501,
    'Product Q4':  497.331609,
}

product_names = list(sales_data.keys())
sales_values = list(sales_data.values())

plt.figure(figsize=(8, 8))
plt.pie(sales_values, labels=product_names, autopct='%1.1f%%', startangle=140)
plt.title('Product Sales Analysis')


plt.show()


plt.bar(mean, std_dev, color=['blue', 'red'])
plt.xlabel('mean')
plt.ylabel('std_dev')
plt.title('Mean and Standard Deviation')
plt.show()
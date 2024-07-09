import numpy as np
import matplotlib.pyplot as plt

data = np.array([10, 15, 20, 22, 25, 27, 29, 30, 31, 32, 33, 35, 40])

q1, median, q3 = np.percentile(data, [25, 50, 75])
iqr = q3 - q1
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

print(f"Q1: {q1}, Median: {median}, Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")

plt.boxplot(data)
plt.title('Boxplot of Data')
plt.xlabel('Data')
plt.ylabel('Values')
plt.grid(True)
plt.show()

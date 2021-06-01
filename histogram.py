from matplotlib import pyplot as plt
import numpy as np

nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
plt.hist(nums, bins=[0, 1, 2, 3])
plt.title("histogram of nums against bins")
plt.show()

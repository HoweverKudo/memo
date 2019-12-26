import numpy as np
import matplotlib.pyplot as plt

"""擬似コイン
"""
for j in range(5):
    vals = [sum(np.random.randint(0, 2, 10)) for i in range(100)]
    print(vals)
    plt.hist(vals)
    plt.grid(True)
    plt.show()


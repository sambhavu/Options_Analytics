import numpy as np
import matplotlib as mlp
from matplotlib import pyplot as plt
mlp.rcParams['font.family'] = 'serif'

K = 8000
S = np.linspace(7000,9000,100)

h = np.maximum(S-K,0)
plt.plot(S,h,lw = 2.5)
plt.ylabel('Value of European Call Option')
plt.xlabel('$S_t$ at Maturity')
plt.grid(True)
plt.show()

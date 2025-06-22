import matplotlib.pyplot as plt
import numpy as np
data=np.array([[0.1, 0.5, 0.9],[0.3, 0.7, 0.2],[0.8, 0.4, 0.6]])
plt.imshow(data,cmap='gray')
plt.show()
print("Pixel Values:",data)
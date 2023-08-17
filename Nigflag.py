#await micropip.install('numpy')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch

a=patch.Rectangle((0,9), width=10, height =3,facecolor='#008000')
b=patch.Rectangle((0,6), width=10, height =10, facecolor='#99f')
m,n=plt.subplots()
n.add_patch(a)
n.add_patch(b)
plt.axis('equal')
plt.show()
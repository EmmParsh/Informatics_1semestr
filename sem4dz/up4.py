import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')
print(df)
print(df['SepalWidthCm'])
print('listed widths: ', list(df['SepalWidthCm']))
x = [i for i in range(50)]
sl = list(df['SepalLengthCm'])
sw = list(df['SepalWidthCm'])
pl = list(df['PetalLengthCm'])
pw = list(df['PetalWidthCm'])
spec = list(df['Species'])
fig = plt.figure(figsize= (16,9))
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax1.plot(sl, sw, '.')
ax2.plot(sl, pl, '.')
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax3.plot(sl, pw, '.')
ax4.plot(sw, pl, '.')
ax5 = fig.add_subplot(325)
ax6 = fig.add_subplot(326)
ax5.plot(sw, pw, '.')
ax6.plot(pw, pl, '.')

ax1.set_xlabel('SepalLengthCm')
ax1.set_ylabel('SepalWidthCm')

ax2.set_xlabel('SepalLengthCm')
ax2.set_ylabel('PetalLengthCm')

ax3.set_xlabel('SepalLengthCm')
ax3.set_ylabel('PetalWidthCm')

ax4.set_xlabel('SepalWidthCm')
ax4.set_ylabel('PetalLengthCm')

ax5.set_xlabel('SepalWidthCm')
ax5.set_ylabel('PetalWidthCm')

ax6.set_xlabel('PetalWidthCm')
ax6.set_ylabel('PetalLengthCm')
plt.tight_layout()
plt.show()
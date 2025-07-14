import matplotlib
import pandas
import numpy as np
import pandas as pd
import sns as sns
from matplotlib import pyplot as plt

data=pd.read_csv('DISK CATDOG - Sheet1.csv')

categories=data['Image #']
values=data['Disk Read Speed']

plt.figure(figsize=(10,6))
plt.bar(categories,values,color='purple')

plt.xlabel('Images #')
plt.ylabel('Disk Read Speed')
plt.title('Test 1')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


mtcars = pd.read_csv('mtcars.csv')
'''1zad
mtcars.groupby('cyl')['mpg'].mean().plot.bar()
plt.show()
'''
'''2zad
mtcars.boxplot(by='cyl',column='wt')
plt.show()
'''
'''4zad
df = pd.DataFrame(data = mtcars);
df.plot.scatter(x = 'hp', y = 'qsec', s = 100);
plt.show()
'''
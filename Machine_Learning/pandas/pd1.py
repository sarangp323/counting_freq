
import os
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
print("PATH:", os.environ.get('PATH'))
import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
d = np.array(my_data)
print(pd.Series(data = my_data, index= labels))

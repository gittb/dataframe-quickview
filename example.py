import pandas as pd
from dataframe_quickview import quickview

data = {'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [3, 6, 9, 12, 15]}
df = pd.DataFrame(data)

df.quickview()
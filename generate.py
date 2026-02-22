import numpy as np
import pandas as pd

n = 1000000
data = {}

data['day_1_int_tang'] = np.arange(n)
data['day_2_int_giam'] = np.arange(n, 0, -1)
data['day_3_int_ngau_nhien'] = np.random.randint(0, n * 10, size=n)
data['day_4_int_ngau_nhien'] = np.random.randint(0, n * 10, size=n)
data['day_5_int_ngau_nhien'] = np.random.randint(0, n * 10, size=n)

data['day_6_float_ngau_nhien'] = np.random.rand(n)
data['day_7_float_ngau_nhien'] = np.random.rand(n)
data['day_8_float_ngau_nhien'] = np.random.rand(n)
data['day_9_float_ngau_nhien'] = np.random.rand(n)
data['day_10_float_ngau_nhien'] = np.random.rand(n)

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)
print("Xong")
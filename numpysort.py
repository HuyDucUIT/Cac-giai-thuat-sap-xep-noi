import pandas as pd
import numpy as np
import time

df = pd.read_csv('data.csv')
start2 = time.perf_counter()

for col in df.columns:
    arr = df[col].values
    start = time.perf_counter()
    np.sort(arr)
    end = time.perf_counter()
    print(f"{col}: {(end - start) * 1000:.2f} ms")

end2 = time.perf_counter()
print(f"Trung binh: {(end2 - start2) * 100:.2f} ms")
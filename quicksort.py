import pandas as pd
import time
import sys

sys.setrecursionlimit(2000000)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

df = pd.read_csv('data.csv')
start2 = time.perf_counter()

for col in df.columns:
    arr = df[col].values.tolist()
    start = time.perf_counter()
    quick_sort(arr)
    end = time.perf_counter()
    print(f"{col}: {(end - start) * 1000:.2f} ms")

end2 = time.perf_counter()
print(f"Trung binh: {(end2 - start2) * 100:.2f} ms")
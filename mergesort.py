import pandas as pd
import time

def merge(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    c.extend(a[i:])
    c.extend(b[j:])
    return c

def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2
    array1 = merge_sort(a[:mid])
    array2 = merge_sort(a[mid:])
    return merge(array1, array2)

df = pd.read_csv('data.csv')
start2 = time.perf_counter()

for col in df.columns:
    arr = df[col].values.tolist()
    start = time.perf_counter()
    merge_sort(arr)
    end = time.perf_counter()
    print(f"{col}: {(end - start) * 1000:.2f} ms")

end2 = time.perf_counter()
print(f"Trung binh: {(end2 - start2) * 100:.2f} ms")

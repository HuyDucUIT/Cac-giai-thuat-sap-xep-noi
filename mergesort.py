import pandas as pd
import time

def merge(a, b):
    c = []
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)
            
    while len(a) > 0:
        c.append(a[0])
        a.pop(0)
        
    while len(b) > 0:
        c.append(b[0])
        b.pop(0)
        
    return c

def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    
    mid = n // 2
    array1 = a[:mid]
    array2 = a[mid:]
    
    array1 = merge_sort(array1)
    array2 = merge_sort(array2)
    
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
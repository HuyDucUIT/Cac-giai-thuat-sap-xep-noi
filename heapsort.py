import pandas as pd
import time
import sys

sys.setrecursionlimit(2000000)

def heapify(A, n, i):
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and A[left] > A[largest]:
            largest = left
        if right < n and A[right] > A[largest]:
            largest = right
        
        if largest == i:
            break
        A[i], A[largest] = A[largest], A[i]
        i = largest

def build_max_heap(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

def heap_sort(A):
    build_max_heap(A)
    n = len(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)

df = pd.read_csv('data.csv')
start2 = time.perf_counter()

for col in df.columns:
    arr = df[col].values.tolist()
    start = time.perf_counter()
    heap_sort(arr)
    end = time.perf_counter()
    print(f"{col}: {(end - start) * 1000:.2f} ms")

end2 = time.perf_counter()
print(f"Trung binh: {(end2 - start2) * 100:.2f} ms")

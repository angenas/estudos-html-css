import random
import time

# Gera um vetor aleatório de 100.000 posições
vetor = [random.randint(1, 1000) for _ in range(100000)]

# Faz uma cópia do vetor original
vetor_copia = vetor.copy()

# Bubble Sort
t_inicio = time.time()
for i in range(len(vetor)):
    for j in range(i + 1, len(vetor)):
        if vetor[j] < vetor[i]:
            vetor[i], vetor[j] = vetor[j], vetor[i]
t_fim = time.time()
t_bubble = t_fim - t_inicio

# Restaura a cópia do vetor
vetor = vetor_copia.copy()

# Insertion Sort
t_inicio = time.time()
for i in range(1, len(vetor)):
    key = vetor[i]
    j = i - 1
    while j >= 0 and key < vetor[j]:
        vetor[j + 1] = vetor[j]
        j -= 1
    vetor[j + 1] = key
t_fim = time.time()
t_insertion = t_fim - t_inicio

# Restaura a cópia do vetor
vetor = vetor_copia.copy()

# Shell Sort
t_inicio = time.time()
gap = len(vetor) // 2
while gap > 0:
    for i in range(gap, len(vetor)):
        temp = vetor[i]
        j = i
        while j >= gap and vetor[j - gap] > temp:
            vetor[j] = vetor[j - gap]
            j -= gap
        vetor[j] = temp
    gap //= 2
t_fim = time.time()
t_shell = t_fim - t_inicio

# Restaura a cópia do vetor
vetor = vetor_copia.copy()

# Heap Sort
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

t_inicio = time.time()
n = len(vetor)
for i in range(n // 2 - 1, -1, -1):
    heapify(vetor, n, i)
for i in range(n - 1, 0, -1):
    vetor[i], vetor[0] = vetor[0], vetor[i]
    heapify(vetor, i, 0)
t_fim = time.time()
t_heap = t_fim - t_inicio

# Restaura a cópia do vetor
vetor = vetor_copia.copy()

# Selection Sort
t_inicio = time.time()
for i in range(len(vetor)):
    min_idx = i
    for j in range(i + 1, len(vetor)):
        if vetor[min_idx] > vetor[j]:
            min_idx = j
    vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]
t_fim = time
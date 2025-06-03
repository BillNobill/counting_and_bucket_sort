import random
import time

def countingSort(arr):
    if not arr:
        return []

    max_val = max(arr)
    counts = [0] * (max_val + 1)
    
    for num in arr:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    sorted_arr = [0] * len(arr)
    for num in reversed(arr):
        sorted_arr[counts[num] - 1] = num
        counts[num] -= 1

    return sorted_arr

tempo_inicial_all = time.time()
# Etapa 1: Gerar os números e salvar no arquivo
with open("../numeros_100mil_ordenados.txt", "w") as arquivo:
    numeros = list(range(1, 100001))
    random.shuffle(numeros)
    for numero in numeros:
        arquivo.write(f"{numero}\n")

# Etapa 2: Ler os números do arquivo para a lista
lista = []
with open("../numeros_100mil_ordenados.txt", "r") as arquivo:
    for linha in arquivo:
        lista.append(int(linha.strip()))

# Etapa 3: Ordenar a lista com Counting Sort
tempo_inicial_ordenamento = time.time()
lista = countingSort(lista) 
tempo_final_ordenamento = time. time()

## Etapa 4: (Opcional) Salvar a lista ordenada no arquivo
with open("../numeros_100mil_ordenados.txt", "w") as arquivo:
    for numero in lista:
        arquivo.write(f"{numero}\n")

tempo_final_all = time.time()
resultado_tempo_all = tempo_final_all - tempo_inicial_all
resultado_tempo_ordenamento = tempo_final_ordenamento - tempo_inicial_ordenamento
print(f"O resultado é de {lista[-1]}")
print(f"O tempo total é de {resultado_tempo_all:.10f}")
print(f"O tempo do ordenamento é de {resultado_tempo_ordenamento:.10f}")

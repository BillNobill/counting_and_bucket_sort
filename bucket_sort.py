import random
import time

def bucketSort(arr, bucket_size=1000):
    if len(arr) == 0:
        return []

    # Determinar o valor mínimo e máximo
    min_val = min(arr)
    max_val = max(arr)

    # Calcular o número de buckets
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    # Distribuir os elementos nos buckets
    for num in arr:
        bucket_index = (num - min_val) // bucket_size
        buckets[bucket_index].append(num)

    # Ordenar individualmente cada bucket e concatenar os resultados
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))  # usa sort interno do Python

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

# Etapa 3: Ordenar a lista com Bucket Sort
tempo_inicial_ordenamento = time.time()
lista = bucketSort(lista) 
tempo_final_ordenamento = time.time()

# Etapa 4: (Opcional) Salvar a lista ordenada no arquivo
with open("../numeros_100mil_ordenados.txt", "w") as arquivo:
    for numero in lista:
        arquivo.write(f"{numero}\n")

tempo_final_all = time.time()
resultado_tempo_all = tempo_final_all - tempo_inicial_all
resultado_tempo_ordenamento = tempo_final_ordenamento - tempo_inicial_ordenamento

print(f"O resultado é de {lista[-1]}")
print(f"O tempo total é de {resultado_tempo_all:.10f}")
print(f"O tempo do ordenamento é de {resultado_tempo_ordenamento:.10f}")

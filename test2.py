# n+1 = N + N-1

anterior = 0
proxima = 1
soma = 1

for n in range(0,51):
    print(anterior)
    soma = proxima + anterior
    anterior = proxima
    proxima = soma
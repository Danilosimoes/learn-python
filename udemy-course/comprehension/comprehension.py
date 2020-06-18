# [ expressão for item in list if conditional]
dobro_dos_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobro_dos_pares)

# versão normal
dobro_dos_pares = []
for i in range (17):
    if i % 2 == 0:
        dobro_dos_pares.append(i * 2)
print(dobro_dos_pares)

# expressão for item in lista
dobros = [i * 2 for i in range(1, 15)]
print(dobros)

# versão "normal"
dobros = []
for i in range(10):
    dobros.append(i * 2)
print(dobros)

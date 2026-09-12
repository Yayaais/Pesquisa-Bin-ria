primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

count = 0 #significa que o contador começará em zero

for n in primos: #passa por cada número da lista
    if n < 67:
        count += 1 #se for menor que 67 aumenta 1

print("A quantidade de números primos que são menores que 67 é: ", count)

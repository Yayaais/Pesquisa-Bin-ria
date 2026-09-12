lista = [
    (3, 'Ana'), (10, 'Bruno'), (15, 'Carlos'), (18, 'Daniela'), (19, 'Eduardo'),
    (28, 'Fernanda'), (33, 'Gustavo'), (35, 'Helena'), (43, 'Igor'), (48, 'Juliana'),
    (58, 'Kleber'), (83, 'Larissa'), (84, 'Marcos'), (86, 'Natália'), (97, 'Otávio'),
    (104, 'Patrícia'), (106, 'Rafael'), (115, 'Sabrina'), (120, 'Tiago'), (122, 'Vanessa'),
    (127, 'Amanda'), (143, 'Breno'), (147, 'Camila'), (149, 'Diego'), (151, 'Eliane'),
    (175, 'Fabiano'), (179, 'Gabriela'), (184, 'Henrique'), (187, 'Isabela'), (194, 'João'),
    (199, 'Karen'), (201, 'Leonardo'), (211, 'Mirela'), (213, 'Nicolas'), (232, 'Olívia'),
    (241, 'Pedro'), (244, 'Queila'), (246, 'Rodrigo'), (256, 'Simone'), (258, 'Túlio'),
    (259, 'Ursula'), (261, 'Victor'), (269, 'Wesley'), (273, 'Xênia'), (278, 'Yasmin'),
    (280, 'Zeca'), (288, 'Alana'), (291, 'Caio'), (292, 'Diana'), (294, 'Fábio')
]


numero_lista = 256

inicio = 0                   #inicio da lista
fim = len(lista) - 1         #quantidade de elementos - fim da lista
tentativas = 0

while inicio <= fim:
    meio = (inicio + fim) // 2  #elemento que está no meio da lista
    tentativas += 1

    if lista[meio][0] == numero_lista:       #verifica se o número do meio é 256
        print("Nome:", lista[meio][1])       #nome que foi encontrado
        print("Tentativas:", tentativas)     #número de tentativas
        break

    if numero_lista > lista[meio][0]:      #se 256 for maior que o número do meio, procura somente na metade da direita
        inicio = meio + 1
    else:                                  #do contrário procura somente na metade da esquerda
        fim = meio - 1


#achei difícil, um pouco confuso

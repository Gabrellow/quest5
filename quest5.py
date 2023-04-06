# Definindo a string
string = "exemplo"

# Convertendo a string para uma lista de caracteres
lista = list(string)

# Definindo os índices iniciais e finais para inverter a lista
inicio = 0
fim = len(lista) - 1

# Invertendo a lista de caracteres usando um loop while
while inicio < fim:
    # Trocando o caractere inicial pelo final
    lista[inicio], lista[fim] = lista[fim], lista[inicio]
    # Movendo os índices para a próxima posição
    inicio += 1
    fim -= 1

# Convertendo a lista de volta para uma string
string_invertida = "".join(lista)

# Imprimindo a string invertida
print(string_invertida)

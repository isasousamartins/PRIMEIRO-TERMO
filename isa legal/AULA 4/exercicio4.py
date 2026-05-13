#Exercicio 1 
# # 1. contador de produção (for)
# # Uma esteira processa 10 peças por ciclo.
#  Crie um progama que se um for para contar 1 a 100 e, para cada numero, imprima: 
# "Peça n x processada com sucesso". No final, exiba "Ciclo de produção"



# for peca in range(1, 11):
#     print(f"Peça n {ciclo} processada com sucesso"....)
# print("Ciclo de produção concluido")

#Exercicio 2
#Imagine a produção de frutas em uma feira. Desejo em uma feira. Desejo apresnetar as frutas banana, manga, melencia, abacaxi. Com  uma quantidade de 10 bananas, 5 mangas, 10 melancias e 13 abacaxis.

# for ban in range(1, 11):
#     print(f"A quantidade de {ban} são")

# for mang in range(1, 6 ):
#     print(f"A quantidade de {mang} são")

# for me in range(1, 11):
#     print(f"A quantidade de {me} são")

# for aba in range(1, 11):
#     print(f"A quantidade de {aba} são")

# total= ban+mang+me+aba

# Exercicio 3 
# Montar uma tabuada inicialmente pode ser usado por um valor fixo e depois a pergunta
print("tabuada")
tab= int(input("Digite qual tabuada você "))
for numero in range(1, 11):
    resultado= tab * numero
    print(f"{tab} x {numero} = {resultado}")
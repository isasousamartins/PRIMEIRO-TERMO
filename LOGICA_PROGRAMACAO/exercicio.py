# Exercícios de Programação Python: "O Caça-Erros"

# 1. O Problema da Idade
# ERRADO
# idade = input("Digite sua idade: ")
# if idade >= 18:
# print("Você é maior de idade.")

# Corrigido
# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade.")
    
# Melhorado
# idade = int(input("Digite sua idade: "))

# if idade >= 18:
#     print("Você é maior de idade.")
    
# else:
#     print("Você é menor de idade.")
#     anos_restantes = 18 - idade
#     print(f"Faltam {anos_restantes} anos para você atingir a maioridade.")

# 2. A Escrita Fiel
# # ERRADO
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

# Corrigido
# nome = "Mariana"
# print(f"Seja bem-vinda, {nome}!")

# Melhorado
# nome= (input("Qual o seu nome?"))
# print(f"Seja bem-vinda, {nome} ")

# 3. Falta de Espaço
#ERRADO
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

#Corrigido
# numero = 10
# if numero > 5:
#     print("O número é maior que cinco.")

# else:
#  print("O número é menor ou igual a cinco.")

# #Melhorado

# numero = int(input("Digite um número: "))

# if numero > 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")

# 4. Esquecimento Fatal
#ERRADO
# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso.")

#Corrigido
usuario = "aluno123"

if usuario == "aluno123":
    print("Login realizado com sucesso.")


#Melhorado
usuario = input("Digite o usuário: ")

if usuario == "aluno123":
    print("Login realizado com sucesso.")
else:
    print("Usuário incorreto.")

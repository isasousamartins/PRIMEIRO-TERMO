# Exercícios de Programação Python: "O Caça-Erros"

# # 1. O Problema da Idade
# # ERRADO
# # idade = input("Digite sua idade: ")
# # if idade >= 18:
# # print("Você é maior de idade.")

# # Corrigido
# # idade = int(input("Digite sua idade: "))
# # if idade >= 18:
# #     print("Você é maior de idade.")
    
# # Melhorado
# # idade = int(input("Digite sua idade: "))

# # if idade >= 18:
# #     print("Você é maior de idade.")
    
# # else:
# #     print("Você é menor de idade.")
# #     anos_restantes = 18 - idade
# #     print(f"Faltam {anos_restantes} anos para você atingir a maioridade.")

# # 2. A Escrita Fiel
# # # ERRADO
# # nome = "Mariana"
# # print("Seja bem-vinda, nome!")

# # Corrigido
# # nome = "Mariana"
# # print(f"Seja bem-vinda, {nome}!")

# # Melhorado
# # nome= (input("Qual o seu nome?"))
# # print(f"Seja bem-vinda, {nome} ")

# # 3. Falta de Espaço
# #ERRADO
# # numero = 10
# # if numero > 5:
# # print("O número é maior que cinco.")
# # else:
# # print("O número é menor ou igual a cinco.")

# #Corrigido
# # numero = 10
# # if numero > 5:
# #     print("O número é maior que cinco.")

# # else:
# #  print("O número é menor ou igual a cinco.")

# # #Melhorado

# # numero = int(input("Digite um número: "))

# # if numero > 5:
# #     print("O número é maior que cinco.")
# # else:
# #     print("O número é menor ou igual a cinco.")

# # 4. Esquecimento Fatal
# #ERRADO
# # usuario = "aluno123"
# # if usuario == "aluno123"
# # print("Login realizado com sucesso.")

# #Corrigido
# usuario = "aluno123"

# if usuario == "aluno123":
#     print("Login realizado com sucesso.")


# #Melhorado
# usuario = input("Digite o usuário: ")

# if usuario == "aluno123":
#     print("Login realizado com sucesso.")
# else:
#     print("Usuário incorreto.")

# # 4. Esquecimento Fatal

# # Errado
# usuario = "aluno123"

# if usuario == "aluno123"
#     print("Login realizado com sucesso.")

# # Corrigido
# usuario = "aluno123"

# if usuario == "aluno123":
#     print("Login realizado com sucesso.")

# # Melhorado
# usuario = input("Digite o usuário: ")

# if usuario == "aluno123":
#     print("Login realizado com sucesso.")
# else:
#     print("Usuário incorreto.")


# # 5. Atribuição vs. Comparação

# # Errado
# clima = "ensolarado"

# if clima = "chuvoso":
#     print("Leve um guarda-chuva!")

# # Corrigido
# clima = "ensolarado"

# if clima == "chuvoso":
#     print("Leve um guarda-chuva!")

# # Melhorado
# clima = input("Como está o clima? ")

# if clima == "chuvoso":
#     print("Leve um guarda-chuva!")
# else:
#     print("Aproveite o dia!")


# # 6. Misturando Alhos com Bugalhos

# # Errado
# pontos = 50

# print("Parabéns! Você fez " + pontos + " pontos.")

# # Corrigido
# pontos = 50

# print("Parabéns! Você fez", pontos, "pontos.")

# # Melhorado
# pontos = 50

# print(f"Parabéns! Você fez {pontos} pontos.")


# # 7. A Ordem dos Fatores

# # Errado
# nota = 9.5

# if nota >= 7:
#     print("Aprovado")

# elif nota >= 9:
#     print("Excelente")

# # Corrigido
# nota = 9.5

# if nota >= 9:
#     print("Excelente")

# elif nota >= 7:
#     print("Aprovado")

# # Melhorado
# nota = float(input("Digite a nota: "))

# if nota >= 9:
#     print("Excelente")
# elif nota >= 7:
#     print("Aprovado")
# else:
#     print("Reprovado")


# # 8. O Contador de 1 a 5

# # Errado
# for i in range(5):
#     print(i)

# # Corrigido
# for i in range(1, 6):
#     print(i)

# # Melhorado
# for i in range(1, 6):
#     print(f"Número: {i}")


# # 9. O Loop Eterno

# # Errado
# tentativas = 1

# while tentativas <= 3:
#     print("Tentando conectar...")

# # Corrigido
# tentativas = 1

# while tentativas <= 3:
#     print("Tentando conectar...")
#     tentativas += 1

# # Melhorado
# tentativas = 1

# while tentativas <= 3:
#     print(f"Tentativa {tentativas}")
#     tentativas += 1

# print("Limite de tentativas atingido.")


# # 10. A Senha Teimosa

# # Errado
# senha = ""

# while senha == "python123":
#     senha = input("Digite a senha secreta: ")

# print("Acesso concedido!")

# # Corrigido
# senha = ""

# while senha != "python123":
#     senha = input("Digite a senha secreta: ")

# print("Acesso concedido!")

# # Melhorado
# senha = ""

# while senha != "python123":
#     senha = input("Digite a senha secreta: ")

#     if senha != "python123":
#         print("Senha incorreta.")

# print("Acesso concedido!")
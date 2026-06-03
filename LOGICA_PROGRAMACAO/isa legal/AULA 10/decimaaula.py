# Tratamento de Erros e Depuração
#  try e execept são usados para lidar com erros forma controlada , evitando que o programa quebre. O código dentro do bloco try é executado normalmente, mas se ocorrer um erro, o controle é passadopra o bloco except, onde podemos lidar com a situação de forma apropriada

# try:
#     numero = int(input("Digite um número: "))
#     resultado = 10/numero
#     print("O resultado é:", resultado)

# except ValueError:
#     print("Erro: Você deve digitar um numero valido")

# except ZeroDivisionError:
#     print("Erro: Não é possivel dividir por zero.")

# except KeyboardInterrupt:
#     print("\n Programa interronpido")

# except Exception as erro:
#     print("Error inesperado:", erro)

# # Exercício 1 
# Escreva um programa que solicite ao usuario calcule a media de três numeros. O programa deve lidar com possiveis erros, como a entrada de valores não numéricos ou divisão por zero.

# try:
   
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     num3 = float(input("Digite o terceiro número: "))
    
#     media = (num1 + num2 + num3) / 3
#     print(f"O resultado da média é: {media}")

# except ValueError:
#     print("Erro: Entrada inválida. Você deve digitar apenas números.")

# except ZeroDivisionError:
#     print("Erro: Não é possível calcular a média se a soma resultar em divisão por zero.")

# except KeyboardInterrupt:
#     print("\nPrograma interrompido pelo usuário.")

# except Exception as erro:
#     print(f"Ocorreu um erro inesperado: {erro}")

# Explicação de def: A palavra-chava "def" é usada para definir uma função em Python. Uma função é um bloco de código reutilizave que ealiza uma tarefa especifica
# return: A palavra-chave "return" é usada para finalizar a execução de uma função e retomar um valor para o local onde a função foi chamada. O valor retornado pode ser usado posteriormente no codigo.

# def nome_da_função(parametro1, prametro2):
# # Corpo da função (codigo que sera esecutado)
# resultado = parametro1 + parametro2
# return resultado

#Exemplo 1 
# def saudacao(nome):
#     return f"Olá, {nome}!"
# print(saudacao("Isa"))
# # exemplo com input
# def saudacao(nome):
#     nome = input("Digite seu nome")
#     return f"Olá, {nome}!"
# print(saudacao("Isa"))

#  Exemplo 2: 
# def calcular_media(num1, num2, num3):
#     try:
#         media = (num1 + num2 + num3) / 3
#         return media
#     except TypeError:
#         return "Erro: Todos os valores devem ser numeros."
#     except ZeroDivisionError:
#         return "Erro: Não é possivel dividir por zero"
    
# print(calcular_media(10, 20, 30))

# # Exercicio 3
# def valores():
#     print("Digite Três valores:")
#     a = int(input("Digite o primeiro valor"))
#     b = int(input("Digite o segundo valor"))
#     c = int(input("Digite o terceiro valor"))
#     return a, b, c 
# print(f" o maior valor é {max(valores())}")

# # exemplo 4 
# # calcule o dobro de um numero fornecido pelo usuario, tratando erros de entrada invalida
# def calcular_dobro():
#     try:
#         valor_digitado = int(input("Digite o valor que deseja :)"))
#         total_dobro = valor_digitado * 2
#         return total_dobro
    
#     except ValueError:
#         print("Digite um numero valido")
#     print(f"O calculo é: {calcular_dobro}")
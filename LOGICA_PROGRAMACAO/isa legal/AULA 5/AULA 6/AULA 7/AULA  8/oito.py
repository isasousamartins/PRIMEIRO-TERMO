# Tratamento de Erros e Exceções
# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))
# resultado = valor1 / valor2
# print(f"O resultado da divisão é: {resultado}")
# O código acima pode gerar um erro de divisão por zero se o usuário digitar 0 para o segundo valor. Para tratar esse erro, podemos usar um bloco try-except:
# Exemplo 1: Tratamento de divisão por zero
# try:
#     valor1 = int(input("Digite o primeiro valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero.")

# # Exemplo 2: Tratamento de entrada inválida
# try:
#     valor1 = int(input("Digite o primeiro valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except ValueError:
#     print("Erro de valor: Por favor, digite um número inteiro válido.")


# Exemplo 3: Tratamento de múltiplas exceções
# try:
#     valor1 = int(input("Digite o primeiro valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Ocorreu um erro: {e}")
    
# Exemplo 4: Uso do bloco finally

# try:
#     valor1 = int(input("Digite o primeiro valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Erro de value: Por favor, digite um número inteiro válido. {e} ou Erro: Não é possível dividir por zero. {e}")
# finally:
#     print("Bloco finally executado.")


# Exercicio 1:
# Crie um algoritmo que pergunte o seu nome e trate erro ao inserir valores incorretos

# primeiro_nome = input("Digite seu primeiro nome: ")
# sobrenome = input("Digite seu sobrenome: ")
# try:
#     nome_completo = f"{primeiro_nome} {sobrenome}"
#     print(f"Olá, {nome_completo}!")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")

# Exercicio 1:
# Crie um algoritmo que pergunte o seu nome e trate erro ao inserir valores incorretos
# primeiro_nome = input("Digite seu primeiro nome: ")
# sobrenome = input("Digite seu sobrenome: ")
# try:
#     nome_completo = f"{primeiro_nome} {sobrenome}"
#     print(f"Olá, {nome_completo}!")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")

# Exemplo 5: TypeError
# try:
#     resultado = "5" + 10
# except TypeError as e:
#     print(f"Erro de tipo: {e}")

valor_hora = float(input("Valor da hora (R$): "))
entradas = 0
saidas = 0

while True:
    print("\n--- MENU DA CANCELA ---")
    opcao = input("1-Entrada | 2-Saída | 3-Relatório | 4-Sair\nEscolha: ")

    if opcao == "1":
        placa = input("Placa do veículo: ")
        tag = input("Possui TAG? (s/n): ")

        if tag == "s":
            print("TAG OK! Cancela aberta.")
        elif tag == "n":
            print("Ticket emitido! Cancela aberta.")
        else:
            print("ERRO: Opção inválida!")
        
        entradas = entradas + 1
        input("\nPressione ENTER para continuar...") # PAUSA

    elif opcao == "2":
        tempo = int(input("Horas de permanência: "))
        valor_pagar = tempo * valor_hora
        tag = input("Era TAG? (s/n): ")

        if tag == "s":
            print(f"Valor R${valor_pagar}: Cobrado na fatura.")
        else:
            print(f"Valor R${valor_pagar}: Pague e devolva o ticket.")
        
        saidas = saidas + 1
        print("Saída liberada!")
        input("\nPressione ENTER para continuar...") # PAUSA

    elif opcao == "3":
        print(f"\nRELATÓRIO: {entradas} Entradas e {saidas} Saídas.")
        input("\nPressione ENTER para continuar...") 

    elif opcao == "4":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
        input("\nPressione ENTER para tentar novamente...") # PAUSA





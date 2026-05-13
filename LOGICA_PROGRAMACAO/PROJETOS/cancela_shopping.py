# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código

preco_hora = float(input("Valor da hora (R$): "))
carros = []
tipos = []
total_arrecadado = 0.0
total_saidas = 0

programa_ativo = True

while programa_ativo:
    print("\n1-Entrada | 2-Saída | 3-Relatório | 4-Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        placa = input("Placa do veículo: ").upper()
        tipo = input("1-TAG | 2-TICKET: ")
        
        carros.append(placa)
        if tipo == "1":
            tipos.append("TAG")
        else:
            tipos.append("TICKET")
        print("Entrada liberada!")

    elif opcao == "2":
        placa = input("Placa para saída: ").upper()
        
        if placa in carros:
            indice = carros.index(placa)
            horas = int(input("Horas de permanência: "))
            valor = horas * preco_hora
            
            print(f"Valor a pagar: R$ {valor:.2f}")
            print(f"Forma de entrada: {tipos[indice]}")
            input("Pressione ENTER para confirmar o pagamento...")
            
            total_arrecadado = total_arrecadado + valor
            total_saidas = total_saidas + 1
            
            carros.pop(indice)
            tipos.pop(indice)
        else:
            print("Veículo não encontrado!")

    elif opcao == "3":
        print("\n--- RELATÓRIO DE FATURAMENTO ---")
        print(f"Total arrecadado: R$ {total_arrecadado:.2f}")
        print(f"Veículos que já saíram: {total_saidas}")
        print(f"Carros atualmente no pátio: {len(carros)}")

    elif opcao == "4":
        print("Sistema encerrado.")
        programa_ativo = False

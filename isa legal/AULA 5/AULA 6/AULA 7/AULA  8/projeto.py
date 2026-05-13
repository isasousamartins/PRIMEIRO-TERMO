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
# Revisão do código
# Configuração inicial
# valor_hora = float(input("Configuração: Informe o valor da hora (R$): "))
# placa = ""
# tipo_acesso = ""
# hora_entrada = 0 # Simulação de hora cheia para facilitar

# print("\n--- SISTEMA DE CANCELA ATIVO ---")

# while True:
#     print("\nEscolha uma opção:")
#     print("1 - Entrada de Veículo")
#     print("2 - Saída de Veículo")
#     print("3 - Sair do Sistema")
    
#     opcao = input("Opção: ")

#     if opcao == "1":
#         print("\n--- FICHA DE ENTRADA ---")
#         placa = input("Digite a placa do veículo: ")
#         tipo_acesso = input("Possui TAG? (sim/nao): ").lower()
#         hora_entrada = int(input("Hora de entrada ): "))
        
#         if tipo_acesso == "sim":
#             print(">> TAG detectada! Cancela liberada.")
#         else:
#             print(">> Pressione o botão para emitir o ticket...")
#             input("--- [ENTER PARA EMITIR TICKET] ---")
#             print(">> Ticket emitido! Cancela liberada.")
        
#         input("\nVeículo estacionado. Pressione ENTER para voltar ao menu...")

#     elif opcao == "2":
#         print("\n--- FICHA DE SAÍDA ---")
#         placa_saida = input("Confirme a placa para saída: ")
        
#         if placa_saida != placa:
#             print("Erro: Esta placa não consta no registro de entrada!")
#         else:
#             hora_saida = int(input("Hora de saída: "))
#             tempo = hora_saida - hora_entrada
            
#             if tempo <= 0:
#                 tempo = 1 # Valor mínimo cobrado
            
#             valor_total = tempo * valor_hora
            
#             print(f"\nResumo: Veículo {placa}")
#             print(f"Tempo de permanência: {tempo} hora(s)")
#             print(f"Valor por hora: R$ {valor_hora}")
#             print(f"VALOR TOTAL: R$ {valor_total}")

#             if tipo_acesso == "sim":
#                 print(">> Cobrança automática via TAG realizada.")
#             else:
#                 print(">> Aguardando pagamento do ticket no totem...")
#                 input("--- [ENTER APÓS PAGAMENTO E DEVOLUÇÃO DO TICKET] ---")
            
#             print(">> Cancela aberta! Boa viagem.")
#             # Limpa os dados para o próximo carro
#             placa = "" 
        
#         input("\nProcesso finalizado. Pressione ENTER para voltar ao menu...")

#     elif opcao == "3":
#         print("Desligando sistema...")
#         break
    
#     else:
#         print("Opção inválida! Tente novamente.")
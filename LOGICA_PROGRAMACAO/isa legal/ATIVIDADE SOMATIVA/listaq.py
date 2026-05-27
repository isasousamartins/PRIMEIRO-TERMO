# 1. Registro de veiculo
# print("Bem-vindo, ao registro de veiculos")
# modelo = input("Qual o modelo do veículo:? ")
# placa = input("Qual a placa:? ")
# print(f"Veículo {modelo} de placa {placa} registrado no sistema. Boa viagem!")

# # 2. Cálculo de Autonomia
# tanque = float(input("Capacidade do tanque (litros): "))
# consumo = float(input("Consumo médio (km/l): "))
# autonomia = tanque / consumo
# print(f"O veículo pode percorrer {autonomia} km com o tanque cheio.")

# 3. Conversor de Moeda
# usd = float(input("Valor do frete em USD: "))
# brl = usd * 5.00
# print(f"Valor em reais: R$ {brl}")

# 4. Média de Entregas
# t1 = float(input("Tempo da entrega 1 (h): "))
# t2 = float(input("Tempo da entrega 2 (h): "))
# t3 = float(input("Tempo da entrega 3 (h): "))
# media = (t1 + t2 + t3) / 3
# print(f"Média do tempo: {media} horas")


# # 5. Monitor de Carga
# peso = float(input("Peso da carga : "))
# if peso < 10:
#     print("Carga Leve")
# elif peso <= 25:
#   print("Carga padrão")
# else:
#  print("ALERTAAA: Excesso de Peso!")

# 6. Classificador de Destino
# print("insira o código de carga,")
# print("Digite N para REGIÃO NORTE")
# print("Digite S para REGIÃO SUL")
# print("E qualquer letra para REGIÃO INTERNACIONAL ")
# escolha=input("insere o código da carga.")

# if escolha== "n":
#     print("REGIÃO NORTE")
# elif escolha== "s":
#     print("REGIÃO SUL")
# else:
#     print("REGIÃO INTERNACIONAL")


#lower sera usado para maiusculo 
# upper minusculo


# 7. Liberação de Saída
# check = input("Checklist concluído? (concluido ou nao concluido): ")
# motorista = input("Motorista identificado? (sim/não): ")
# if check == "sim" and motorista == "sim":
#        print("Saída autorizada")
# else:
#      print("Saída não autorizada")


# # # 8. Cálculo de Atrasos
# total = int(input("Total de entregas: "))
# atrasos = int(input("Entregas com atraso: "))
# if atrasos > total * 0.1:
#    print("Necessário Otimizar Rotas")
# else:
#      print("Logística Eficiente")

# 9. Validaçõ de calibragem
# pressao = float(input("Pressão do pneu (PSI): "))
# if 100 <= pressao <= 110:
#      print("Dentro do padrão")
# elif pressao < 100:
#       print("Abaixo do recomendado")
# else:
#      print("Acima do recomendado")

# # 10. Contagem de Embarque (for)
# import time
# for i in range(5, 0, -1):
#     time.sleep(1)
#     print(i)
# print("Portão Trancado")


# # 11. Soma de Fretes (while)
# total_frete = 0
# while True:
#     valor = float(input("Digite o valor do frete (0 para parar): "))
#     if valor == 0:
#         break
#     total_frete += valor
# print(f"Total acumulado: R$ {total_frete:.2f}")

# # 12. Monitoramento de Frota
# maior = 0
# for i in range(5):
#     km = float(input(f"Quilometragem do veículo {i+1}: "))
#     if km > maior:
#         maior = km
# print(f"Maior quilometragem: {maior}")

#12 do Bruno
# print("Monitoramente")
# maior_km = 0
# for frota in range(1,6):
#     km= float(input(f"digite a quilomeragem do veiculo {frota}"))
#     if km > maior_km: 
#         maior_km = km

# 13. Sistema de Rastreamento
# tentativas = 3
# while tentativas > 0:
#     codigo = input("Digite o código de acesso: ")
#     if codigo == "track99":
#         print("Acesso Liberado")
#         break
#     else:
#         tentativas -= 1
#         print("Acesso Negado")
# if tentativas == 0:
#     print("Rastreamento Bloqueado")
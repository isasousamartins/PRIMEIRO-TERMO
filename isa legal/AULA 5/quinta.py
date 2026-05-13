#Revisão de conteúdo:
#print = "Função saida de dados para console"
# input = "Funçõ de entrada de daos console do usuario via teclado"
# if = "Estrutura de decisão para executar código condicionalmente"
# elif = "Combinação de else + if para verificar multiplas condigo quando a condição do if é falsa"
#  for = "laço de repetiçao para iterar sobre uma sequencia de elementos"
# while = "Laço de repetiçao para executar codigo enquanto uma condição for verdadeira"
# operaçoes matematica: +,-,*,/,//,%,**
# operadores de comparação: == , !=, >, <, <=,>=
# variavel = "Exempo de variavel para armazenardaos"
#print(variavel)

#Execicio 1: com print e input
# nome = input("Digite seu nome")
# print (f"Olá, {nome}! Bem-vindo á aula de Python para desenvolvimento de Sistemas!")

# # Exemplo 1: com print e input 
# nota = float (input("Digite a nota do aluno:"))
# if nota >= 7: 
#     print("Aluno aprovado!")
# elif nota >= 5: 
#     print ("Aluno em recuperação")
# else:
#     print("Aluno reprovado")

# #Exemplo 3: com for 
# materiais = ["metal", "plastico","vidro" ]
# for material in materiais:
#     print(f"Processando material: {material}.")
#     print(f"Material {material} processando com sucesso!")
# print ("Fim do processamento de materias")

# 2. O laço while (Repetiçoes indeterminadas)
# Use o white quando voce nao sabe quando vai parar . Ele deprnde de uma condição (como um sensor de segurança ou um botão de emergencia)
# Exemplo Monitor de temperatura (Loop infinito conrolado )
# Repete enquanto a temperatura estiver segura 
# import time 
# temperatura = 25
# while temperatura < 40:
#     print (f"Temperatura atual: {temperatura} °C. Sistema operando...")
#     time.sleep(1)
#     temperatura += 3 # simulando o aquecimento da máquina
#     print ("ALERTA! temperatura atingiu o limite. Desligando motor...")

# #Lista de temperaturas lidas pelo sensor por minuto
# leituras =[70, 75, 82, 98, 110.85,80]
# for temp in leituras:
#     print(f"CRITICO: {temp}°C detectado!Acionando parada de emergencia.")
#     break # O loop para aqui e NÃO Lê os proximos valores (85 e 80)
# print (f"Temperatura esta em {temp}°C. Operação normal.")
# print ("Sistema desligado. Aguardando manutenção")

# # Produção de peças com controle de material usando continue
# materiais = ["metas", "metal", "plastico", "metal", "vidro", "metal"]
# for peca in materiais:
#     if peca != "metais"
#     print(f"Aviso: Peça de {peca} detectada. Desviando para descarte... ")
#     continue # Pula o restente do codigo abaixo e vai para a proxima peça
# # Este codigo do roda se a peça for metal
# print (f"Processando peça de {peca}. Furando e polindo ...")
# print("Fim do lote de produçao")

#Exercicio 1
# Tente criar um codigo que conte 1 a 10, mas use o continue para não imprimir o numero 5 (simulando uma falha de sensor especifica no item 5)
# for sensor in range(1,11):
#     if sensor == 5:
#         print (f"Sensor n°{sensor} com falha ")
#         print(f"Sensor {sensor} sem falha")
#         continue
# print ("FiM! ;)")

#Exercicio 2
# Simule um semaforo com parada cada cor. Determine um tempo que deseja  para que quando mudar para tal cor ele represente uma pausa para cada cor. Use o Continue para pular a cor amarela(simulado um semafaro com defeito que nao acende a luz amrela)

# cores = ["Verde", "Amarelo", "Vermelho"]
# tempo_pausa = 3 
# print("Iniciando simulação de semáforo com defeito...")
# for cor in cores:
#     if cor == "Amarelo":
#         print(f"{cor} com falha")
#         continue
#     print(f"Sinal {cor} aceso. Aguardando {tempo_pausa} segundos...")
   
# print("finalizado.")

#Exemplo 3 - Soma de cargas de energia (for )
# #  Uma fabrica em 5 maquinas. Peças ao usuario (via input dentro do loop) o consumo em kWh de cada uma 5 maquinas. Ao final do loop, o programa deve exibir o consumo total da fabrica.

# consumo_total = 0
# for A in range(1, 6):
#     consumo = float(input(f"Digite o consumo da máquina {A} (em kWh): "))
#     consumo_total += consumo

# print(f"\nO consumo total da fábrica é: {consumo_total:.2f} kWh")

#Exemplo 4 - Identificador de Peças defeituosas (for + if)
#Percorra uma lista de medidas de peças:
#medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
#O padrao de qualidade aceita apenas pecas com exatamente 50.0 ou mais . 
# #Use um for para ler a lista e, para cada peca, digite se ela esta aprovda ou rejeitada

# pecas = [50.1, 49.8, 52.0, 50.0, 48.5 ]
# for medidas in pecas:
#     if medidas >= 50.0:
#         print(f"Peças com medida{medidas}mn: Aprovação")
#     else:
#         print(f"Peças com medida {medidas}mn: Rejeitada")
# print("Fim da avaliação de peças")

# Exercicio - uma balança industrial esta pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistema aceita variaçoes.
# Crie um progama que peça ao usuario o peso de cada saco (via input dentro do loop) e, para cada um , informe se ele está "Dentro do limite" (entre 48kg e 52kg) ou "Fora do limite ". No final ,exiba quantos sacos estao dentro do limite

# sacos_dentro = 0

# for i in range(1, 7):
#     peso = float(input(f"Digite o peso do saco {i} (kg): "))
#     if 48 <= peso <= 52:
#         print("Status: Dentro do limite")
#         sacos_dentro += 1
#     else:
#         print("Status: Fora do limite")
# print(f"\nTotal de sacos dentro do limite: {sacos_dentro}")

# # 1. O Laço 'for' (Repetição Determinadas)
# # Use o 'for' quanto você sabe exatamente quatas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças)
# # Exemplo; Relatoria de produção Diaria
# # Imagine que você tem uma meta produzir 5 lotes e quer numerar cada um:

# Exemplo 1 
# for lote in range (1, 6):
#     print(f"Processando lote número {lote}...")
#     print( "Qualidade verificada.[OK]")
#     print("Produção do dia finalizado!")
  # Exemplo 2
# for b in range(10):
#      print(f"Quantidade total {b} foi...")

#Exemplo 3 
# # Imagine o seguinte cenário, iremos produzir 20 disco de vinil
# for vinil in range (1, 21):
#      print(f"Produzir de {vinil}, disria")

# #Exemplo 4 
# pecas= ["Engrenagem", "Eixa", "Rolamento", "Parafunso", "Martelo", "Prego", "Chave de fenda"]
# itempeca= ["Cilindrica", "Dupla", "Crônica", "Prego", "Orelha"]
#  for item in pecas:
#      print(f"Item, e, estoque: {item} e [itempeca]")

# Exemplo 5
# Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção voce deseja e a partir da seleçao ele lista os produtos

doce= ["Bolo", "chocolate"]
salgado= ["Macarrao", "Arroz"]

print("Menu")

escolha= input("Escolha entre s ou d ")
if escolha == "d":
    print(f"Lista de doces disponiveis" )
    for lista in doce:
        print(lista)


elif escolha == "s":
    print("Lista de salgados disponiveis" )
    for lista in salgado:
        print(lista)

else: 
    print("Sua escolha esta errada seu bobão")





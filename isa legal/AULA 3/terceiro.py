#Lógicas e Decisãos 
#Se condição  verdadeira 
#Se  condição ainda verdadeira porém com criterios
#Senao condição falsa
#if elif e else 

#Exenplos 1 
print ("Verificar a idade")
idade = int (input("Digita sua idade"))

if idade >= 18:
    print("Você é maior de idade")
elif idade >=16:
    print("Você não é de maior porém pode votar")
else:
    print("Você não é de maior")
    
#Exemplo 2 
# Valores 
print(" Checar valores")
valor= int (input("Digite um valo"))

if valor >100: 
    print("Valores acima de 100")
    print("O valor é", valor + 1)
    
else:
    print("Valores abaixo de 100")
    print("O valor é", valor - 1)
    
    # Exemplo 3 
    # Criar um algoritimo que permita escolher a opção que deseja 
    print ("Menu de opição ")
    print ("Filme F e Série e X para sair")
    
    escolha =  input ("Digite uma opção")
    
if escolha == "F":
    print("Você escolheu Filmes")
    
elif escolha == "S":
    print("Você ecolheu Séries")
    
else: 
    print("Você saiu do programa")
    

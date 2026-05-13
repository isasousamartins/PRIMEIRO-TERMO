#Funções são blocos de código reutílizáveis.
# O "f" no Python, usado antes das aspas de uma string ( como f "texto {variável}"), indica que se trata de uma f-string (ou formatted string literal). Ele informa ao Python que a string contém expressoes entre chaves {} que devem ser avaliadas em tempo de execuçao e substituidas pelos valores reais.

def saudacao(nome):
    return f"Olá, {nome}!"

mensagem = saudacao("isa legal")
print (mensagem)

def age (idade):
    return f"sua idade é , {idade}!"
mensagem = age(16)
print(mensagem)

def boas_vindas(nome, cargo):
    print(f"Olá, {nome}! Você é {cargo}.")
    
boas_vindas("Anna", "Desenvolvedora")
boas_vindas("Isa", "Top")
boas_vindas("Bruno", "Professor legal")

# Conversões 
nome = input("Seu nome:")
idade = int(int("Sua idade: "))# Converte texto para inteiro
print(f"{nome} tem{idade} anos.")
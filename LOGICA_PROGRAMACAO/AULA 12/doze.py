import tkinter as tk
from tkinter import messagebox, ttk

def bemvindo():
    # .get() serve para buscar o texto da caixa
    nome_usuario = usuario_nome.get()
    idade_usaario = usuario_idade.get()
    paises_usuario = usuario_paises.get()

    if nome_usuario == "" and idade_usaario == "":
        messagebox.showwarning("Aviso", "Por favor digite seu nome e idade! :)")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá {nome_usuario}, logando no sistema! e sua idade é {idade_usaario}")

def janela_bemvindo():
    segunda_janela = tk.Toplevel(janela_bemvindo)
    segunda_janela.title("Segunda Janela")
    segunda_janela.geometry("400x400")

# Janela
janela_bemvindo = tk.Tk()
janela_bemvindo.title("Saudações do Usuário")
janela_bemvindo.geometry("600x500")

# Componentes
# Labels
lbl_mensagem_usuario = tk.Label(janela_bemvindo, text="Digite seu nome :)")
lbl_mensagem_usuario.grid(row=0, column=0, pady=10, padx=10)

lbl_mensagem_idade = tk.Label(janela_bemvindo, text="Digite sua idade :)")
lbl_mensagem_idade.grid(row=2, column=0, pady=10, padx=10)

lbl_mensagem_paises = tk.Label(janela_bemvindo, text="Paises :)")
lbl_mensagem_paises.grid(row=1, column=0, pady=10, padx=10)


lbl_segunda_janela = tk.Label(janela_bemvindo, text="Clique para abrir a segunda janela :)")
lbl_segunda_janela.grid(row=2, column=0, pady=10, padx=10)


# Entrys
usuario_nome = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
usuario_nome.grid(row=0,column=1,pady=10,padx=10)

usuario_idade = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
usuario_idade.grid(row=2,column=1,pady=10,padx=10)


usuario_paises = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
usuario_idade.grid(row=2,column=1,pady=10,padx=10)

# Componentes de ComboBox
combo_nivel = tk.ttk.Combobox(janela_bemvindo, values=["Brasil", "Marrocos", "Egito", "Escócia"], width=30)
combo_nivel.grid(row=1, column=1, pady=10, padx=10)

# Botão
btn_enviar_mensagem = tk.Button(janela_bemvindo, text="Enviar Mensagem", command=bemvindo, bg="#ccbb22" , fg="white")
btn_enviar_mensagem.grid(row=3, column=0, pady=20, padx=0)



btn_fechar_janela = tk.Button(janela_bemvindo, text="Fechar Janela", command=janela_bemvindo.destroy, bg="#cc228b" , fg="white")
btn_fechar_janela.grid(row=3, column=2, pady=30, padx=10)

btn_segunda_janela = tk.Button(janela_bemvindo, text="Abrir Segunda Janela", command=janela_bemvindo, bg="#22ccbe" , fg="white")
btn_segunda_janela.grid(row=3, column=1, pady=30, padx=10)



# Rodar interface
janela_bemvindo.mainloop()

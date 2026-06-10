import tkinter as tk
from tkinter import messagebox, ttk

def validar_emprestimo():
    try:
        # 1. Coleta dos dados digitados pelo usuário
        nome = usuario_nome.get().strip()
        livro_selecionado = combo_livros.get()
        
        # Validação se o nome foi preenchido
        if not nome:
            messagebox.showwarning("Aviso", "Por favor, digite seu nome.")
            return
            
        # Tratamento de erro: se o usuário esquecer de digitar os dias
        if not entry_dias.get():
            messagebox.showwarning("Aviso", "Por favor, digite a quantidade de dias.")
            return
        dias = int(entry_dias.get())

        # 2. Identificação do Perfil e da Categoria do livro
        perfil = var_perfil.get() 
        is_raro = "(Raros)" in livro_selecionado  # Identifica se o livro é raro pelo texto

        # 3. Aplicação das Regras de Negócio
        limite = 14 if perfil == 1 else 7

        # Regra 4: Restrição de Categoria (Livro Raro para Comunidade)
        if is_raro and perfil == 2:
            messagebox.showerror("EMPRÉSTIMO NEGADO", f"Olá {nome}!\n\nLivros raros são de uso exclusivo para Alunos.")
        
        # Regra 3: Cálculo da Taxa (Passou do limite do perfil)
        elif dias > limite:
            dias_extras = dias - limite
            taxa = dias_extras * 5
            messagebox.showwarning("APROVADO COM TAXA", f"Olá {nome}!\n\nEmpréstimo aprovado, mas com taxa.\nLimite do perfil: {limite} dias.\nDias extras: {dias_extras}\nValor total da taxa: R$ {taxa:.2f}")
        
        # Regra 2: Dentro do limite gratuito
        else:
            messagebox.showinfo("EMPRÉSTIMO APROVADO", f"Parabéns {nome}!\n\nEmpréstimo liberado com sucesso e 100% gratuito.")

    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números inteiros no campo de dias.")

# --- Configuração da Janela Principal ---
janela_bemvindo = tk.Tk()
janela_bemvindo.title("BIBLIOTECA DIGITAL")
janela_bemvindo.geometry("550x300")

# 1. Campo de Nome
lbl_mensagem_usuario = tk.Label(janela_bemvindo, text="Digite seu nome :)", font=("Arial", 10, "bold"))
lbl_mensagem_usuario.grid(row=0, column=0, pady=10, padx=10, sticky="w")

usuario_nome = tk.Entry(janela_bemvindo, font=("Arial", 12), width=30)
usuario_nome.grid(row=0, column=1, pady=10, padx=10)

# 2. Seleção de Livros (Seu Combobox)
lbl_livro = tk.Label(janela_bemvindo, text="Selecione o Livro:", font=("Arial", 10, "bold"))
lbl_livro.grid(row=1, column=0, pady=10, padx=10, sticky="w")

combo_livros = ttk.Combobox(janela_bemvindo, values=[
    "Dom Casmurro - Machado de Assis (comum)", 
    "1984 - George Orwell (comum)", 
    "Clean Code - Robert Martin (comum)", 
    "Os Lusíadas - Luís de Camões (Raros)"
], width=33, state="readonly")
combo_livros.current(0)
combo_livros.grid(row=1, column=1, pady=10, padx=10)

# 3. Seleção de Perfil (Radiobuttons)
lbl_perfil = tk.Label(janela_bemvindo, text="Seu Perfil:", font=("Arial", 10, "bold"))
lbl_perfil.grid(row=2, column=0, pady=10, padx=10, sticky="w")

var_perfil = tk.IntVar(value=1)
frame_perfil = tk.Frame(janela_bemvindo)
frame_perfil.grid(row=2, column=1, sticky="w", padx=10)

rb_aluno = tk.Radiobutton(frame_perfil, text="Aluno", variable=var_perfil, value=1)
rb_comunidade = tk.Radiobutton(frame_perfil, text="Comunidade", variable=var_perfil, value=2)
rb_aluno.pack(side="left", padx=5)
rb_comunidade.pack(side="left", padx=5)

# 4. Campo de Dias
lbl_dias = tk.Label(janela_bemvindo, text="Dias de Empréstimo:", font=("Arial", 10, "bold"))
lbl_dias.grid(row=3, column=0, pady=10, padx=10, sticky="w")

entry_dias = tk.Entry(janela_bemvindo, font=("Arial", 12), width=10)
entry_dias.grid(row=3, column=1, pady=10, padx=10, sticky="w")

# 5. Botões de Ação
btn_validar = tk.Button(janela_bemvindo, text="Validar Empréstimo", command=validar_emprestimo, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_validar.grid(row=4, column=1, pady=20, sticky="w", padx=10)

btn_fechar_janela = tk.Button(janela_bemvindo, text="Fechar Janela", command=janela_bemvindo.destroy, bg="#cc228b", fg="white")
btn_fechar_janela.grid(row=4, column=1, pady=20, sticky="e", padx=10)

# Rodar a interface gráfica
janela_bemvindo.mainloop()














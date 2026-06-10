# # 1.Registro de Operador:
# import tkinter as tk
# from tkinter import messagebox, ttk

# janela = tk.Tk()
# janela.title("Registro de Operador")
# janela.geometry("500x400")


# def bemvindo():
#     nome_usuario = usuario_nome.get()
#     turno_usuario = combo_nivel.get()

    
#     if nome_usuario == "" or turno_usuario == "":
        
#         messagebox.showwarning("Aviso", "Por favor, digite seu nome e selecione o turno! :)")
#     else:
        
#         messagebox.showinfo("Bem-Vindo", f"Operador {nome_usuario}, registrado no Turno {turno_usuario}. Boa jornada!")


# lbl_mensagem_usuario = tk.Label(janela, text="Digite seu nome")
# lbl_mensagem_usuario.grid(row=0, column=0, pady=10, padx=10)

# usuario_nome = tk.Entry(janela, font=("Arial", 12), width=20)
# usuario_nome.grid(row=0, column=1, pady=10, padx=10)

# lbl_mensagem = tk.Label(janela, text="Turno")
# lbl_mensagem.grid(row=1, column=0, pady=10, padx=10)

# combo_nivel = ttk.Combobox(janela, values=["A", "B", "C"], width=30)
# combo_nivel.grid(row=1, column=1, pady=10, padx=10)


# btn_clique_ativar = tk.Button(janela, text="Finalizar ", font=("Arial", 14), command=bemvindo)
# btn_clique_ativar.grid(row=3, column=1, padx=15, pady=15)


# btn_fechar_janela = tk.Button(janela, text="Fechar Janela", command=janela.destroy, bg="#c9258a" , fg="white")
# btn_fechar_janela.grid(row=3, column=2, pady=30, padx=10)

# janela.mainloop()


# #2. Cálculo de Produção:
# import tkinter as tk
# from tkinter import messagebox


# def calcular_producao():

#         pecas_por_hora = int(entry_pecas.get())
#         total_turno = pecas_por_hora * 8
#         lbl_resultado.config(
#             text=f"Produção estimada em 8h: {total_turno} peças", )

# janela = tk.Tk()
# janela.title("Cálculo de Produção")
# janela.geometry("450x250")


# lbl_instrucao = tk.Label(
#     janela, text="Quantidade de peças produzidas em 1 hora:", font=("Arial", 11)
# )
# lbl_instrucao.pack(pady=15)

# entry_pecas = tk.Entry(janela, font=("Arial", 12), width=15, justify="center")
# entry_pecas.pack(pady=5)

# btn_calcular = tk.Button(
#     janela,
#     text="Calcular Turno (8h)",
#     font=("Arial", 12 ),
#     command=calcular_producao,
# )
# btn_calcular.pack(pady=15)


# lbl_resultado = tk.Label(janela, text="", font=("Arial", 12 ))
# lbl_resultado.pack(pady=10)

# janela.mainloop()

# 3. Conversor de Unidade:




# # 4. Média de Qualidade:

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Média de Qualidade")
# janela.geometry("500x400")


# def calculo():
#     try:
  
#         nota1 = float(entry_nota1.get())
#         nota2 = float(entry_nota2.get())
#         nota3 = float(entry_nota3.get())

#         if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10):
#             messagebox.showwarning("Aviso", "As notas devem ser entre 0 e 10!")
#             return

#         media = (nota1 + nota2 + nota3) / 3


#         messagebox.showinfo("Resultado", f"A média de qualidade da peça é: {media:.2f}")

#     except ValueError:
       
#         messagebox.showerror("Erro", "Por favor, digite valores numéricos válidos nas três notas!")



# lbl_titulo = tk.Label(janela, text="Notas de inspeção de uma peça", font=("Arial", 12, ))
# lbl_titulo.grid(row=0, column=0, columnspan=2, pady=20, padx=20)


# entry_nota1 = tk.Entry(janela, font=("Arial", 12), width=20)
# entry_nota1.grid(row=1, column=1, pady=10, padx=10)

# entry_nota2 = tk.Entry(janela, font=("Arial", 12), width=20)
# entry_nota2.grid(row=2, column=1, pady=10, padx=10)

# entry_nota3 = tk.Entry(janela, font=("Arial", 12), width=20)
# entry_nota3.grid(row=3, column=1, pady=10, padx=10)


# lbl_nota1 = tk.Label(janela, text="Primeira nota (0 a 10)")
# lbl_nota1.grid(row=1, column=0, pady=10, padx=10)

# lbl_nota2 = tk.Label(janela, text="Segunda nota (0 a 10)")
# lbl_nota2.grid(row=2, column=0, pady=10, padx=10)

# lbl_nota3 = tk.Label(janela, text="Terceira nota (0 a 10)")
# lbl_nota3.grid(row=3, column=0, pady=10, padx=10)


# btn_calcular = tk.Button(janela, text="Calcular Média", font=("Arial", 11), command=calculo)
# btn_calcular.grid(row=4, column=0, columnspan=2, pady=20)

# janela.mainloop()











# # 5. Termostato Inteligente:

# # import tkinter as tk
# # from tkinter import messagebox  


# # def verificar_temperatura():
# #         temp = float(entry_temp.get())

# #         if temp < 40:
# #             messagebox.showinfo("Status", "Baixa carga")
# #         elif 40 <= temp <= 70:
# #             messagebox.showinfo("Status", "Normal")
# #         else:
            
# #             messagebox.showwarning("ALERTA", "ALERTA: Resfriamento Ativado!")

   


# # janela = tk.Tk()
# # janela.title("Termostato Inteligente:")
# # janela.geometry("400x400")


# # lbl_instrucao = tk.Label(
# #     janela, text="Digite a temperatura atual (°C):", font=("Arial", 12)
# # )
# # lbl_instrucao.pack(pady=15)

# # entry_temp = tk.Entry(janela, font=("Arial", 12), width=10, )
# # entry_temp.pack(pady=5)

# # btn_verificar = tk.Button(
# #     janela,
# #     text="Verificar Status",
# #     font=("Arial", 11),
# #     command=verificar_temperatura,
# # )
# # btn_verificar.pack(pady=15)

# # janela.mainloop()

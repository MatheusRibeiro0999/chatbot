import tkinter as tk
from tkinter import PhotoImage
from funcoes import modo_noturno, enviar_mensagem
from variaveis import llm_chain

#janela
root = tk.Tk()
root.title("Assistente Virtual")
root.geometry("800x600")
root.config(bg="white")

icon = PhotoImage(file='C:/Users/ribei/Documents/CODES/PYTHON/BOT ASSIST/images/LOGO.jpg')
root.iconphoto(True, icon)

background_image = PhotoImage(file="C:/Users/ribei/Documents/CODES/PYTHON/BOT ASSIST/images/banner.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#janela texto
chat_text = tk.Text(root, bg="#f0f0f0", fg="#000", font=("Arial", 12), bd=1)
chat_text.pack(expand=True, fill=tk.BOTH)

#entrada texto
user_input_entry = tk.Entry(root, width=50)
user_input_entry.pack(side=tk.LEFT, padx=10, pady=10)
user_input_entry.bind("<Return>", lambda event: enviar_mensagem(event, user_input_entry, chat_text, llm_chain, root))

#botão Enviar
send_button = tk.Button(root, text="Enviar", command=lambda: enviar_mensagem(None, user_input_entry, chat_text, llm_chain, root))
send_button.pack(side=tk.LEFT, padx=10, pady=10)

#botão Noturno
modo_escuro = tk.Button(root, text="Modo Escuro", command=lambda: modo_noturno(root, chat_text, user_input_entry, send_button, modo_escuro), bg="lightgray", fg="black")
modo_escuro.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
import tkinter as tk

def enviar_mensagem(event=None, user_input_entry=None, chat_text=None, llm_chain=None, root=None):
    user_input = user_input_entry.get().strip()
    if user_input:
        chat_text.insert(tk.END, f"Você: {user_input}\n")
        user_input_entry.delete(0, tk.END)

        if user_input.lower() == "sair":
            root.quit()
        
        response = llm_chain.run(input=user_input)
        chat_text.insert(tk.END, f"Assistente: {response}\n")
        
        chat_text.see(tk.END)

def modo_noturno(root, chat_text, user_input_entry, send_button, modo_escuro):
    if root["bg"] == "white":  
        root.config(bg="black")
        chat_text.config(bg="black", fg="white")
        user_input_entry.config(bg="gray20", fg="white")
        send_button.config(bg="gray20", fg="white")
        modo_escuro.config(bg="gray20", fg="white", text="Modo Claro")
    else:  
        root.config(bg="white")
        chat_text.config(bg="white", fg="black")
        user_input_entry.config(bg="white", fg="black")
        send_button.config(bg="lightgray", fg="black")
        modo_escuro.config(bg="lightgray", fg="black", text="Modo Escuro")
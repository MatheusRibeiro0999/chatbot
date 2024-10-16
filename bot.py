import tkinter as tk
from tkinter import PhotoImage
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

api_key = "SEU_API_AQUI"

template = """
você é um assistente virtual.
responda somente em português.
Input {input}
"""
base_prompt = PromptTemplate(input_variables=["input"], template=template)

llm = ChatGroq(model_name="llama3-8b-8192", api_key=api_key)
memory = ConversationBufferMemory(memory_key="chat_history", input_key='input')
llm_chain = LLMChain(llm=llm, prompt=base_prompt, memory=memory)

#envio de mensagem
def send_message(event=None):
    user_input = user_input_entry.get().strip()
    if user_input:
        chat_text.insert(tk.END, f"Você: {user_input}\n")
        user_input_entry.delete(0, tk.END)

        if user_input.lower() == "sair":
            root.quit()
        
        response = llm_chain.run(input=user_input)
        chat_text.insert(tk.END, f"Assistente: {response}\n")
        
        chat_text.see(tk.END)
    
#função do modo noturno
def modo_noturno():
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

#janela tkinter
root = tk.Tk()
root.title("Assistente Virtual")
root.geometry("800x600")  

root.config(bg="white")

# Definindo ícone
icon = PhotoImage(file='C:/Users/ribei/Documents/CODES/PYTHON/BOT ASSIST/images/LOGO.jpg')  # Altere para o caminho do seu ícone
root.iconphoto(True, icon)

# Imagem de fundo
background_image = PhotoImage(file="C:/Users/ribei/Documents/CODES/PYTHON/BOT ASSIST/images/banner.png")  # Altere para o caminho da sua imagem de fundo
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#área de texto
chat_text = tk.Text(root, bg="#f0f0f0", fg="#000", font=("Arial", 12), bd=1)
chat_text.pack(expand=True, fill=tk.BOTH)

#entrada de texto
user_input_entry = tk.Entry(root, width=50)
user_input_entry.pack(side=tk.LEFT, padx=10, pady=10)

user_input_entry.bind("<Return>", send_message)

#botão enviar
send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack(side=tk.LEFT, padx=10, pady=10)

#botão modo escuro
modo_escuro = tk.Button(root, text="Modo Escuro", command=modo_noturno, bg="lightgray", fg="black")
modo_escuro.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()

#adicionar função para acompanhar resposta do bot
#adicionar função para ajustar tela cheia
#adicionar função para upar arquivos como excel, word e pdf para o bot ler
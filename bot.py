from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

api_key = "sua_api_aqui"

template = """
você é um assistente virtual.
responda somente em portugês.
Input {input}
"""
base_prompt = PromptTemplate(input_variables=["input"], template=template)

llm = ChatGroq(model_name="llama3-8b-8192", api_key=api_key)
memory = ConversationBufferMemory(memory_key="chat_history", input_key='input')

llm_chain = LLMChain(llm=llm, prompt=base_prompt, memory=memory)

os.system("clear")

while True:
    user_input = input("você: ")

    if user_input.lower() == "sair":
        print("Encerrando a conversa.")
        break
    
    response = llm_chain.run(input=user_input)
    print(f"assistente: {response}")

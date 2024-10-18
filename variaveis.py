from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

chave_api = "sua_api_aqui"

template = """
você é um assistente virtual.
responda somente em português.
Input {input}
"""
prompt_base = PromptTemplate(variaveis_input=["input"], template=template)

#llm do groq
llm = ChatGroq(model="llama3-8b-8192", api_key=chave_api)
memoria = ConversationBufferMemory(memory_key="chat_history", input_key='input')
llm_chain = LLMChain(llm=llm, prompt=prompt_base, memory=memoria)
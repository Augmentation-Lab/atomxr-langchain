# from langchain.agents import load_tools
# from langchain.agents import initialize_agent
# from langchain.llms import OpenAI
# from langchain import OpenAI, SerpAPIWrapper, LLMChain
# from langchain.agents import ZeroShotAgent, Tool, AgentExecutor
# from langchain.chains.conversation.memory import ConversationBufferMemory

# search = SerpAPIWrapper()

# tools = [
#     Tool(
#         name = "Search",
#         func=search.run,
#         description="useful for when you need to answer questions about current events"
#     ), 
#     Tool(
#         name = "Documentation",
#         func=search.run,
#         description="useful for when you need to answer questions about AtomXR or CaineScript documentation, and general questions about AtomXR.",
#         return_direct=True
#     )
# ]

# prefix = """Have a conversation with a human, answering the following questions as best you can. You have access to the following tools:"""
# suffix = """Begin!"

# {chat_history}
# Question: {input}
# {agent_scratchpad}
# """

# # creates a prompt for ZeroShotAgent
# prompt = ZeroShotAgent.create_prompt(
#     tools, 
#     prefix=prefix, 
#     suffix=suffix,
#     input_variables=["input", "chat_history", "agent_scratchpad"]
# )
# memory=ConversationBufferMemory(memory_key="chat_history")

# print(prompt.template)

# llm_chain = LLMChain(
#     llm=OpenAI(temperature=0), 
#     prompt=prompt,
# )
# tool_names = [tool.name for tool in tools]
# agent = ZeroShotAgent(llm_chain=llm_chain, allowed_tools=tool_names)
# agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, memory=memory)
# agent_executor.run(input="Hi, I'm Bob")



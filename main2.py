from langchain.agents import Tool
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent
import faiss
from langchain.chains import VectorDBQAWithSourcesChain
import pickle
from langchain.agents import tool
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
os.environ['SERPAPI_API_KEY'] = os.getenv('SERPAPI_API_KEY')

# Load the LangChain.
index = faiss.read_index("docs.index")

with open("faiss_store.pkl", "rb") as f:
    store = pickle.load(f)

store.index = index

@tool
def documentation(query: str) -> str:
    """Searches the API for the query."""
    chain = VectorDBQAWithSourcesChain.from_llm(llm=OpenAI(temperature=0), vectorstore=store)
    result = chain({"question": query})
    return (f"Answer: {result['answer']} Sources: {result['sources']}")

@tool
def code(query: str) -> str:
    """Generates code based on query"""
    return "OnStart(CreateObject(\"Object\"))"

# define tools
search = SerpAPIWrapper()

tools = [
    Tool(
        name = "Current Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or the current state of the world"
    ),
    Tool(
        name = "Documentation",
        func= lambda query: documentation(query),
        description="useful for when you need to answer questions about AtomXR or CaineScript documentation, and general questions about AtomXR. Also good for asking about syntax of functions and methods.",
        return_direct=True
    ),
    Tool(
        name = "Code Generation",
        func= lambda query: code(query),
        description="Use this more than other tools if you are unsure if you should use a tool which tool to use. Code generation.",
    )
]
memory = ConversationBufferMemory(memory_key="chat_history")
llm=OpenAI(temperature=0)
agent_chain = initialize_agent(tools, llm, agent="conversational-react-description", verbose=True, memory=memory)

# while True:
#     print("AI: " + agent_chain.run(input=input("Human: ")))

with open('testcontext.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print("Prompt: " + line)
    print("AI: " + agent_chain.run(input=line))


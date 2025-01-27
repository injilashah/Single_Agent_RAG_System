from langchain.agents import create_openai_tools_agent
from langchain.agents import AgentExecutor
def create_agent(llm,tool,prompt,query):
    agent = create_openai_tools_agent(llm,tool,prompt)
    agent_executor = AgentExecutor(agent = agent, tools = tool, verbose = True)
    return agent_executor.invoke({"input":query})
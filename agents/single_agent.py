from email import message
from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langchain_core.messages import AnyMessage
from langgraph.graph import add_messages
from langchain_deepseek import ChatDeepSeek
from langchain_ollama import ChatOllama

class Contact(TypedDict):
    name: str
    email: str
    phone: str


class InputState(TypedDict):
    message: Annotated[list[AnyMessage], add_messages]

class OutputState(TypedDict):
    answer: str
    

class AgentState(InputState, OutputState):
    pass

def llm_node(state: InputState):
    """LLM node that takes a message and returns an answer."""
    # Use ChatDeepSeek or ChatOllama based on the input
    message = [
        {"role": "system", "content": "You are a helpful assistant."},
    ] + state["message"]


    # Get the answer from the LLM
    answer = ChatOllama(model="qwen3:4b").invoke(message)

    return {"answer": answer.content}

builder = StateGraph(AgentState, InputState)

builder.add_node("llm_node", llm_node)

builder.add_edge(START, "llm_node")
builder.add_edge("llm_node", END)

graph = builder.compile()

answer = graph.invoke({"message": "what's your name?"})
print(answer["answer"])

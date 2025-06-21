from typing import Annotated
from typing_extensions import TypedDict, Optional

from langgraph.graph import StateGraph, START, END
from langchain_core.messages import AnyMessage
from langgraph.graph import add_messages
from langchain_deepseek import ChatDeepSeek
from langchain_ollama import ChatOllama

from utils import save_graph

class Contact(TypedDict):
    name: str
    email: str
    phone: str


class InputState(TypedDict):
    message: Annotated[list[AnyMessage], add_messages]
    llm_answer: Optional[str]

class OutputState(TypedDict):
    answer: str
    
class AllMessages(InputState):
    ...

def llm_node(State: InputState):
    """LLM node that generates a response based on the input message."""
    # Use the ChatDeepSeek model to generate a response
    messages = [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
    ] + State['message']
    print(messages)
    print('---- ')
    print(State)
    # messages = [
    #     ("system","你是一位乐于助人的智能小助理",),
    #     ("human", State["message"])
    # ]
    chat_model = ChatDeepSeek(model="deepseek-chat")
    response = chat_model.invoke(messages)
    print(response.content)
    return {'answer':response.content}

graph = StateGraph(AllMessages, input=InputState, output=OutputState)

graph.add_node('llm', llm_node)

graph.add_edge(START, 'llm')
graph.add_edge('llm', END)

graph = graph.compile()

# a = graph.invoke({"message":"this is a test?"})
# a = graph.invoke("this is a test?")
# print(a# ...existing code...
a = graph.invoke({"message": [{"role": "user", "content": "this is a test?"}]})
print(a)
# ...existing code...)
# messages = [
#         {'role': 'system', 'content': 'You are a helpful assistant.'},
#     ]
# chat_model = ChatDeepSeek(model="deepseek-chat").invoke(messages)
# print(chat_model.content)
from IPython.display import Image, display

# save_graph(graph, "graph_single_agent.png")

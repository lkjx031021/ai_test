from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langchain_core.messages import AnyMessage
from langgraph.graph import add_messages
# from langchain_deepseek import DeepSeek
# from langchain_ollama import Ollama

class Contact(TypedDict):
    name: str
    email: str
    phone: str


class InputState(TypedDict):
    message: Annotated[list[AnyMessage], add_messages]
    
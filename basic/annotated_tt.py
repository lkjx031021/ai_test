from typing import Annotated
from langgraph.graph import add_messages

a = Annotated[int, "This is an integer", "This is another annotation"]
b = Annotated[dict[str, int], "This is a dictionary with string keys and integer values"]
c = Annotated[list[str], add_messages]

def ff(a: Annotated[int, "This is an integer", "This is another annotation"]) -> int:
    """Function that takes an annotated integer and returns it."""
    print(a)
    return a

def bb(b: Annotated[dict[str, int], "This is a dictionary with string keys and integer values"]) -> dict[str, int]:
    """Function that takes an annotated dictionary and returns it."""
    print(b)
    return b

ff(1)
bb({"key1": 1, "key2": 2,})
a = add_messages(["message1", "message2"], ["3ew"])
for i in a:
    print(i.content)


from pydantic import BaseModel, Field
from typing import Annotated

class User(BaseModel):
    # 必填字段，长度限制为2-50
    name: Annotated[str, Field(min_length=2, max_length=50)]
    # 可选字段，默认18，范围0-120
    age: Annotated[int, Field(default=18, ge=0, le=120)]

user = User(name="Ai", age=2599)  # 自动验证
# user = User(name="Bob")  # age默认为18
print(user)
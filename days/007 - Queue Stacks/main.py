from typing import Any

class EmptyStack(Exception):
    ...

class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, value: Any):
        self.stack.insert(0, value)

    def pop(self):
        if(len(self.stack) == 0):
            raise EmptyStack

        return self.stack.pop()
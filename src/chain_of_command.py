"""
Chain of Responsibility is a behavioral design pattern that lets you pass"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, List


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

class AbstractHandler(Handler):
    """An abstract class for handling requests. It also implements the next so it shoudl not be implemented in the subclasses"""
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        """Set the next handler in the chain"""
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request== "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class Handlers(Enum):
    MONKEY = MonkeyHandler
    SQUIRREL = SquirrelHandler



def build_chain_of_responsibility(handlers: List[Handlers]) -> Handler:
    """Build the chain of responsibility dinamically"""
    handler = None
    for handler_type in handlers:
        if handler is None:
            handler = handler_type.value()
            continue
        handler.set_next(handler_type.value())
    return handler

def client_code(handler: Handler, foods) -> None:
    for food in foods:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")

if __name__ == "__main__":
    handler = build_chain_of_responsibility([Handlers.MONKEY, Handlers.SQUIRREL])
    print("Chain: Monkey > Squirrel")
    client_code(handler, ["Nut", "Banana", "Cup of coffee"])
    print("\n")
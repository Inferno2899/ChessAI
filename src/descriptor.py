from typing import Any


class Descriptor:
    def __set_name__(self, owner: Any, name: str):
        self.name = "__" + name

    def __get__(self, instance: Any, owner: Any):
        return getattr(instance, self.name)

    def __set__(self, instance: Any, value: Any):
        setattr(instance, self.name, value)

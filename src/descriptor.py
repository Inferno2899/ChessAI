from typing import Any


class Descriptor:
    def __set_name__(self, owner: type[object], name: str) -> None:
        self.name = "__" + name

    def __get__(self, instance: object, owner: type[object]) -> Any:
        return getattr(instance, self.name)

    def __set__(self, instance: object, value: Any) -> None:
        setattr(instance, self.name, value)

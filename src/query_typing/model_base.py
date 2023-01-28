from dataclasses import dataclass
from typing import Type, TypeVar, Generic

@dataclass
class ModelBase:
    id: int

F = TypeVar('F', bound=ModelBase)

class QueryBase(Generic[F]):
    class NotFoundError(Exception):
        pass

    def __init__(self, models : list[F]) -> None:
        self.models  = models

    def all(self) -> list[F]:
        return self.models

    def get(self, id: int) -> F:
        for model in self.models:
            if model.id == id:
                return model

        raise self.NotFoundError()

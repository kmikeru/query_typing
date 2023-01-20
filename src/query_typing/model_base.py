from dataclasses import dataclass


@dataclass
class ModelBase:
    id: int


class QueryBase:
    class NotFoundError(Exception):
        pass

    def __init__(self, models):
        self.models = models

    def all(self):
        return self.models

    def get(self, id: int):
        for model in self.models:
            if model.id == id:
                return model

        raise self.NotFoundError()

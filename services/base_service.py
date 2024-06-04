class BaseService:
    def __init__(self, repository) -> None:
        self._repository = repository

    def get_list(self, schema):
        return self._repository.read_with_options(schema)

    def get_by_id(self, id: int):
        return self._repository.read_by_id(id)
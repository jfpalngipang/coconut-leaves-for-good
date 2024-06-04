from repository.alert_repo import AlertRepository
from services.base_service import BaseService

class AlertService(BaseService):
    def __init__(self, repository: AlertRepository):
        self.repository = repository
        super().__init__(repository)
from dependency_injector import containers, providers
from core.database import Database
from core.config import configs
from repository.alert_repo import AlertRepository
from services.alert_service import AlertService

class Container(containers.DeclarativeContainer):
    db = providers.Singleton(Database, db_url=configs.DATABASE_URI)

    alert_repository = providers.Factory(AlertRepository)

    alert_service = providers.Factory(AlertService, repository=alert_repository)
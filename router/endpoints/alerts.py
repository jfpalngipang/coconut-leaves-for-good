from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from services.alert_service import AlertService
from core.container import Container
from schema.alert_schema import GetAlerts

router =  APIRouter(prefix="/alerts", tags=["alerts"])

@router.get("/")
@inject
async def get_alerts(
    get_query: GetAlerts = Depends(),
    service: AlertService = Depends(Provide[Container.alert_service])
):
    return []
from fastapi import APIRouter

from router.endpoints.alerts import router as alert_router

routers = APIRouter()
router_list = [alert_router]

for r in router_list:
    routers.include_router(r)
from fastapi import FastAPI
import uvicorn
import os
# from models import Alert
from utils.class_object import singleton
from core.container import Container
from router.routes import routers
from core.config import configs

class AppCreator:
    def __init__(self):
        self.app = FastAPI(
            title=configs.PROJECT_NAME,
            version="0.0.1"
        )

        self.container = Container()
        self.db = self.container.db()

        self.app.include_router(routers)

# app = FastAPI()

app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
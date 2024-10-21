from fastapi import FastAPI
from api.routes import router

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

app.include_router(router)
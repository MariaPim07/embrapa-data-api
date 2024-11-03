import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import ValidationError

from api.routes import router

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
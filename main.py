from fastapi import FastAPI
from fastapi.responses import JSONResponse
from core.database import engine, Base
from models import *
from api.router import api_router
from core.security.auth_middleware import AuthMiddleware, PostAuthMiddleware


def init_db():  # initialize DB
    Base.metadata.create_all(bind=engine)
    print("Initialized  the DB Model")


app = FastAPI(name='Appointment Booking app')
app.add_middleware(AuthMiddleware)
app.add_middleware(PostAuthMiddleware)
app.include_router(api_router)


@app.on_event('startup')
def on_startup():
    init_db()


@app.get("/")
def health_check():
    return JSONResponse(status_code=200, content={
        "script": 'running'
    })


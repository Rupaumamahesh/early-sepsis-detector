from fastapi import FastAPI
from app.routes import report

app = FastAPI()

app.include_router(report.router)
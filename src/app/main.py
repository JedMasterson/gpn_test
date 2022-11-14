from fastapi import FastAPI
from src.app.routers import ping
from src.app.db import database
from src.app.routers import records
import uvicorn

app = FastAPI()


@app.on_event('startup')
async def startup():
    database.connect()


@app.on_event('shutdown')
async def shutdown():
    database.dispose()


app.include_router(ping.router)
app.include_router(records.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8075)

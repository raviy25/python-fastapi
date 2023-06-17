import os
import uvicorn
from fastapi import FastAPI
from routes import metacritics_games

PORT = os.getenv("SRV_PORT", 8000)


app = FastAPI()
app.include_router(metacritics_games.router)


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=PORT)

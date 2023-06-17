from fastapi import APIRouter
import urllib.parse
from typing import List

from starlette.responses import JSONResponse

from controller.metacritics_controller import games_controller
from fastapi.responses import JSONResponse


router = APIRouter(
    prefix="/games",
    tags=["games"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_games() -> List:
    return games_controller.get_all_games()


@router.get("/{title:path}")
async def read_game(title: str) -> JSONResponse:
    decoded_game_path = urllib.parse.unquote(title)
    print(f"Decoded game path{decoded_game_path}")
    if games_controller.get_game_by_title(decoded_game_path) == {}:
        return JSONResponse(status_code=404, content={"error": "Game not found"})
    return games_controller.get_game_by_title(decoded_game_path)

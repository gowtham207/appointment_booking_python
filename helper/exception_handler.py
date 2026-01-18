from typing import TypeVar, Callable, ParamSpec
from functools import wraps
from fastapi.responses import JSONResponse

ParamType = ParamSpec("P")
ReturnType = TypeVar("R")


def exception_handler(func: Callable[ParamType, ReturnType]) -> Callable[ParamType, ReturnType]:
    @wraps(func)
    def wrapper(*args: ParamType.args, **kwargs: ParamType.kwargs) -> ReturnType:
        try:
            return func(*args, **kwargs)
        except Exception as err:
            print(f"Error in login_user: {e}", flush=True)
            return JSONResponse(status_code=500, content={"message": "Internal Server Error"})
    return wrapper

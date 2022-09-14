from starlette.requests import Request

from fastapi.responses import JSONResponse


async def global_error_handler(
        request: Request,
        exc: Exception,
):
    print('eroor')
    return JSONResponse(content={"error": True}, status_code=500)

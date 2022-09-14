from fastapi import FastAPI
from aredis_om import get_redis_connection, Migrator

from endpoints import router
from errors import global_error_handler


async def startup():
    await Migrator().run()


def get_application():
    application = FastAPI()
    application.include_router(router)  # register endpoints
    application.add_event_handler("startup", startup)  # register event handler
    application.add_exception_handler(Exception, global_error_handler)  # register error handler
    return application


app = get_application()

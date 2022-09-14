from pydantic import BaseModel


class HistorySchema(BaseModel):
    link: str

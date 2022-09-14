from aredis_om import HashModel, Field


class HistoryModel(HashModel):
    link: str = Field(index=True)
    created_at: int = Field(index=True)

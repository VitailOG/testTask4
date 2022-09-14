from fastapi import APIRouter

from models import HistoryModel
from schemas import HistorySchema
from services import save_links, get_unique_domains

router = APIRouter()


@router.post('/')
async def add_route(data: list[HistorySchema] | HistorySchema):
    await save_links(data)
    return {"status": "ok"}


@router.get('/links', response_model=list[HistoryModel])
async def domains():
    s = await HistoryModel.find().all()
    return s


@router.get(
    '/links-filter'
)
async def domains_filter(f: int | None = None, t: int | None = None):
    return await get_unique_domains(f, t)

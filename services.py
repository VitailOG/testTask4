import re
import time

from operator import lt, gt

from models import HistoryModel
from schemas import HistorySchema


async def save_links(data: list[HistorySchema] | HistorySchema):
    if isinstance(data, list):
        for _ in data:
            e = _.dict() | {"created_at": int(round(time.time() * 100))}
            await HistoryModel(**e).save()
        return
    e = data.dict() | {"created_at": int(round(time.time() * 100))}
    await HistoryModel(**e).save()


async def get_list_links(_from: int | None = None, _to: int | None = None):
    params = ((_from, gt), (_to, lt))
    query = [func(HistoryModel.created_at, val) for val, func in params if val is not None]
    result = await HistoryModel.find(*query).all()
    return result


async def get_unique_domains(_from: int | None = None, _to: int | None = None):
    def domain_name(url):
        result = re.search(r'^((https|http)://)?(www.)?([\w.-]+)', url.link)
        return result.group(4)

    links = await get_list_links(_from, _to)
    links = set(map(domain_name, links))
    return links

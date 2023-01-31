from common.utils.request_api import request_api


async def get_match_detail(match_id):
    match_detail = await request_api('/matches', {'matchid': match_id})
    return match_detail

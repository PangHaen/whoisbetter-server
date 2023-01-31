from app.common.utils.request_api import request_api


async def get_userinfo_by_username(username):
    user_info = await request_api('/users', {'nickname': username})
    return user_info


async def get_match_by_access_id(access_id, match_type, offset, limit):
    match_list = await request_api(f'/users/{access_id}/matches',
                                   {'matchtype': match_type, 'offset': offset, 'limit': limit})
    return match_list

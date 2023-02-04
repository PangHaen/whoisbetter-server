import logging
from app.common.utils.fifa_api import users


async def get_userinfo(params):
    user_info = await users.get_userinfo_by_username(params)
    logging.info(f'user_info : {user_info}')
    return user_info


async def get_match_list(params):
    match_list = await users.get_match_by_access_id(params['accessId'], 40, 0, 100)
    logging.info(f'match_list : {match_list}')
    return match_list


def get_same_match(match_list_1, match_list_2):
    return list(set(match_list_1) & set(match_list_2))


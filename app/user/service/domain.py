from app.user.service import infra


async def get_user_infos(user_name, opponent_user_name):
    try:
        user_self = await infra.get_userinfo(user_name)
        opponent_user = await infra.get_userinfo(opponent_user_name)
        if 'message' in user_self or 'message' in opponent_user:
            raise Exception('존재 하지 않는 유저 명 입니다. 다시 입력해 주세요.')

        return {'user': user_self, 'opponent': opponent_user}
    except Exception as e:
        return e


async def get_user_match_lists(user_info, opponent_user_info):
    user_match_list = await infra.get_match_list(user_info)
    opponent_user_list = await infra.get_match_list(opponent_user_info)

    return {'user': user_match_list, 'opponent': opponent_user_list}


def get_same_match(match_list_1, match_list_2):
    return list(set(match_list_1) & set(match_list_2))

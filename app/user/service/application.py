from app.user.service import domain


async def get_user_match_list_detail(params):

    try:
        user_infos = await domain.get_user_infos(params['userName'], params['opponentUserName'])
        if type(user_infos) == 'string':
            raise Exception(user_infos)
    except Exception as e:
        return e


    user_match_lists = await domain.get_user_match_lists(user_infos['user'], user_infos['opponent'])

    matches_with_opponents = domain.get_same_match(user_match_lists['user'], user_match_lists['opponent'])



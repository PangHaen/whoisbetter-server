from fastapi import APIRouter
from pydantic import BaseModel
from app.router.user import service

router = APIRouter(prefix="/api/user")


class SelfRecord(BaseModel):
    userName: str


class RelativeRecord(SelfRecord):
    opponentUserName: str


# TODO 개인 한 명의 전적을 검색할 때 사용할 기능, 아직 구체화 되지 않음.
# @router.post('/search')
# async def search_user(self_record: SelfRecord):
#     return await service.search_userinfo(self_record)


@router.post('/search/relative')
async def search_two_user(relative_record: RelativeRecord):
    user_self = await service.get_userinfo(relative_record.userName)
    # opponent_user = service.get_userinfo(relative_record.opponentUserName)

    # user_match_list = await service.get_match_list(user_self)
    # opponent_match_list = await service.get_match_list(opponent_user)

    # result = service.get_same_match(user_match_list, opponent_match_list)

    return {"user" : user_self, "opponent": opponent_user}

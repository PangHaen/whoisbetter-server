from fastapi import APIRouter
from pydantic import BaseModel
from app.user import service

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
    # user_self = await service.get_userinfo(relative_record.userName)
    # opponent_user = await service.get_userinfo(relative_record.opponentUserName)
    #
    # user_match_list = await service.get_match_list(user_self)
    # opponent_match_list = await service.get_match_list(opponent_user)
    #
    # result = service.get_same_match(user_match_list, opponent_match_list)

    # return {"result": result}
    # TODO : str인건 맞는데 막 이상한 공격 들어오는건 알 수 없으니까 여기서 한 번 걸러 준다~ (입력 데이터 유효성 검증)
    # 다 통과 되면~ service.application으로 보내 준다.
from fastapi import APIRouter
from pydantic import BaseModel
from app.user.service import application

router = APIRouter(prefix="/api/user")


class SelfRecord(BaseModel):
    userName: str


class RelativeRecord(SelfRecord):
    opponentUserName: str


# TODO 개인 한 명의 전적을 검색할 때 사용할 기능, 아직 구체화 되지 않음.
# @router.post('/search')
# async def search_user(self_record: SelfRecord):
#     return await service.search_userinfo(self_record)

# TODO : str인건 맞는데 막 이상한 공격 들어오는건 알 수 없으니까 여기서 한 번 걸러 준다~ (입력 데이터 유효성 검증)
@router.post('/search/relative')
async def search_two_user(relative_record: RelativeRecord):
    user = relative_record.userName
    opponent = relative_record.opponentUserName

    try:
        user_matches_detail_list = await application.get_user_match_list_detail(
            {'userName': user, 'opponentUserName': opponent})
        if type(user_matches_detail_list) == 'string':
            raise Exception(user_matches_detail_list)

        return {'result': user_matches_detail_list}
    except Exception as e:
        return e



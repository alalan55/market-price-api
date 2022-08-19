import fastapi
from interface.IUser import User

router = fastapi.APIRouter()


@router.post("/user/register")
async def register_user(user: User):
    return {"user": []}

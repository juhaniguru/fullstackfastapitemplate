from pydantic import BaseModel


class UserRegisterReq(BaseModel):
    username: str
    password: str
    firstName: str
    lastName: str


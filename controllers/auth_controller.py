from fastapi import APIRouter

import models
from dtos.auth import UserRegisterReq

router = APIRouter()

"""

firstName = Column(String(45), nullable=False)
    lastName = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False, unique=True)
    role = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)

"""


@router.post('api/v1/auth/register')
async def register(req: UserRegisterReq, db: models.Db):
    user = models.User(
        lastName=req.lastName,
        firstName=req.firstName,
        email=req.username,
        password=req.password,
        role='student'
    )

    db.add(user)
    db.commit()


@router.post('api/v1/auth/login')
async def login():
    pass

from pydantic import BaseModel, EmailStr
from typing import Optional


class GetUser(BaseModel):
    email: EmailStr
    username: Optional[str]
    role: str

    class Config:
        orm_mode = True
        use_enum_values = True


class LoginUser(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
        use_enum_values = True


class RegisterUser(BaseModel):
    email: EmailStr
    username: Optional[str]
    password: str

    class Config:
        orm_mode = True
        use_enum_values = True
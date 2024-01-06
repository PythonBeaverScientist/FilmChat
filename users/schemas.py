import hashlib
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, PastDate
from secure import psw_context


class UserModel(BaseModel):
    user_name: str = Field(..., min_length=3, max_length=30)
    password: str = Field(...)
    email: EmailStr = Field(...)
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    birth_date: Optional[PastDate] = Field(default=None)

    def hash_user_psw(self) -> None:
        self.password = psw_context.hash(self.password)

from enum import Enum
from typing import Union, Optional

from pydantic import BaseModel


class ResponseSerializer(BaseModel):
    status: int
    message: Optional[str]
    data: Union[dict, list]


class CreateAccountSerializer(BaseModel):
    name: str
    value: float

class UpdateValueAccountSerializer(BaseModel):
    account: int
    value: float

class ConsultAccountSerializer(BaseModel):
    account: int


# class LikeDislike(str, Enum):
#     LIKE = 'like'
#     DISLIKE = 'dislike'


# class LikeDislikePhotoSerializer(BaseModel):
#     photo_id: int
#     action: LikeDislike

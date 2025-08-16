from pydantic.v1 import BaseModel


class NebulaUserAPIAuthorizationTokenResponseModel(BaseModel):
    token: str

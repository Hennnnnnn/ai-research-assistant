from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    email: str
    username: str

    model_config = {
        "from_attributes": True
    }
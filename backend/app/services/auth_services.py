from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.auth import RegisterRequest
from app.core.security import hash_password

def register_user(db: Session, request: RegisterRequest) -> User:
    user = User(
        email=request.email,
        username=request.username,
        hashed_password=hash_password(request.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException
from fastapi import status

from app.models.user import User
from app.schemas.auth import RegisterRequest
from app.core.security import hash_password
from app.core.security import verify_password

def authenticate_user(db: Session, email: str, password: str) -> User:
    statement = select(User).where(User.email == email)
    
    user = db.scalar(statement)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials"
        )
        
    if not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials"
        )
        
    return user

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


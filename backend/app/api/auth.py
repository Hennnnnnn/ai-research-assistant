from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.auth import RegisterRequest
from app.schemas.user import UserResponse
from app.services.auth_services import register_user

from app.schemas.auth import (
    LoginRequest,
    TokenResponse
)
from app.services.auth_services import authenticate_user
from app.core.security import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/register",
    response_model=UserResponse
)

def register(request: RegisterRequest, db: Session = Depends(get_db)):
    return register_user(db, request)

@router.post(
    "/login",
    response_model=TokenResponse
)

def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, request.email, request.password)
    
    token = create_access_token({"sub": str(user.id)})
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }

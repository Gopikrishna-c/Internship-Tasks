from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from jose import jwt, JWTError
from passlib.context import CryptContext

from sqlalchemy.orm import Session

from models.database import get_db
from models.schemas import UserRegister, UserLogin
from models.user import User


# ==================================================
# Password Configuration
# ==================================================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# ==================================================
# JWT Configuration
# ==================================================

SECRET_KEY = "your-secret-key-change-this"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


security = HTTPBearer()

router = APIRouter()


# ==================================================
# Test Authentication Route
# ==================================================

@router.get("/")
def test():

    return {
        "message": "Authentication Route Working"
    }


# ==================================================
# Password Verification
# ==================================================

def verify_password(
    plain_password: str,
    hashed_password: str
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# ==================================================
# Create JWT Access Token
# ==================================================

def create_access_token(
    data: dict
):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# ==================================================
# Register API
# ==================================================

@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    # Check existing email

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # Hash password

    hashed_password = pwd_context.hash(
        user.password
    )

    # Create user

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    # Save user

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {

        "message": "User registered successfully",

        "user_id": new_user.id,

        "username": new_user.username,

        "email": new_user.email
    }


# ==================================================
# Login API
# ==================================================

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    # Find user

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Verify password

    if not verify_password(
        user.password,
        existing_user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Create token

    access_token = create_access_token(
        data={
            "sub": existing_user.email
        }
    )

    return {

        "message": "Login successful",

        "user_id": existing_user.id,

        "username": existing_user.username,

        "email": existing_user.email,

        "access_token": access_token,

        "token_type": "bearer"
    }


# ==================================================
# Get Current Authenticated User
# ==================================================

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    try:

        # Decode JWT

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # Get email

        email = payload.get("sub")

        if email is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid authentication token"
            )

        # Find user

        user = db.query(User).filter(
            User.email == email
        ).first()

        if user is None:

            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return user

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )


# ==================================================
# Protected Profile API
# ==================================================

@router.get("/profile")
def profile(
    current_user: User = Depends(
        get_current_user
    )
):

    return {

        "message": "Protected API accessed successfully",

        "user_id": current_user.id,

        "username": current_user.username,

        "email": current_user.email
    }
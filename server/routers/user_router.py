from fastapi import Body, status,HTTPException
from fastapi.routing import APIRouter
from server.models.models1 import session
from server.models.models import User
from server.schemas import user_schemas
from server.utils import hash_helper

router = APIRouter(prefix="/user", tags=["User CRUD"])
@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user_data: user_schemas.GetUser = Body(...)):
    """
    Create a new user in the database.

    Args:
        user_data (user_schemas.GetUser): The user data including username, email, and password.

    Returns:
        User: The created user data.
    """
    # Hash the password
    hashed_password = hash_helper.hash(user_data.hashed_password)
    user_data.hashed_password = hashed_password

    # Create a new User object
    user = User(**user_data.model_dump())

    # Add the user to the session and commit the changes
    session.add(user)
    session.commit()
    session.refresh(user)

    return user

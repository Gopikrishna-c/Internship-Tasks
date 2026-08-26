from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.role import RoleSelection
from app.models.selected_role import SelectedRole

router = APIRouter(
    prefix="/role",
    tags=["Role Selection"]
)


@router.post("/select")
def select_role(
    data: RoleSelection,
    db: Session = Depends(get_db)
):

    # Old role delete
    db.query(SelectedRole).filter(
        SelectedRole.email == data.email
    ).delete()

    # Save one role
    selected = SelectedRole(
        email=data.email,
        role=data.selected_role
    )

    db.add(selected)
    db.commit()

    return {
        "message": "Role selected successfully",
        "selected_role": data.selected_role
    }


@router.get("/{email}")
def get_selected_role(
    email: str,
    db: Session = Depends(get_db)
):

    role = db.query(SelectedRole).filter(
        SelectedRole.email == email
    ).first()

    if not role:
        return {
            "email": email,
            "selected_role": None
        }

    return {
        "email": email,
        "selected_role": role.role
    }
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.contact import ContactCreate, ContactResponse
from app.services.contact_service import ContactService

router = APIRouter(prefix="/contacts", tags=["contacts"])
contact_service = ContactService()


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
def create_contact(
    payload: ContactCreate,
    db: Session = Depends(get_db),
) -> ContactResponse:
    return contact_service.create_contact(db, payload)


@router.get("/", response_model=list[ContactResponse])
def list_contacts(db: Session = Depends(get_db)) -> list[ContactResponse]:
    return contact_service.list_contacts(db)


@router.get("/{contact_id}", response_model=ContactResponse)
def get_contact(
    contact_id: int,
    db: Session = Depends(get_db),
) -> ContactResponse:
    return contact_service.get_contact(db, contact_id)

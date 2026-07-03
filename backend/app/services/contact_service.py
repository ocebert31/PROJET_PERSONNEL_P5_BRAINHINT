from __future__ import annotations

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.contact_repository import ContactRepository
from app.schemas.contact import ContactCreate, ContactResponse


class ContactService:
    def __init__(self, repository: ContactRepository | None = None) -> None:
        self.repository = repository or ContactRepository()

    def create_contact(self, db: Session, data: ContactCreate) -> ContactResponse:
        contact = self.repository.create(db, data)
        return ContactResponse.model_validate(contact)

    def list_contacts(self, db: Session) -> list[ContactResponse]:
        contacts = self.repository.get_all(db)
        return [ContactResponse.model_validate(contact) for contact in contacts]

    def get_contact(self, db: Session, contact_id: int) -> ContactResponse:
        contact = self.repository.get_by_id(db, contact_id)
        if contact is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Contact not found",
            )
        return ContactResponse.model_validate(contact)

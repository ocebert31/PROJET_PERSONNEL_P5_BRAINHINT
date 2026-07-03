from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.contact import Contact
from app.schemas.contact import ContactCreate


class ContactRepository:
    def create(self, db: Session, data: ContactCreate) -> Contact:
        contact = Contact(
            name=data.name,
            email=str(data.email),
            message=data.message,
        )
        db.add(contact)
        db.commit()
        db.refresh(contact)
        return contact

    def get_all(self, db: Session) -> list[Contact]:
        return list(db.scalars(select(Contact).order_by(Contact.created_at.desc())).all())

    def get_by_id(self, db: Session, contact_id: int) -> Contact | None:
        return db.get(Contact, contact_id)

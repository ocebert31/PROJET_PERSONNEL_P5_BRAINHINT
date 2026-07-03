from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from tests.factories.contact_factory import ContactCreateFactory, ContactFactory


def test_create_contact(client: TestClient) -> None:
    payload = ContactCreateFactory.build(
        name="Bertrand",
        email="bertrand@example.com",
        message="Hello BrainHint!",
    )

    response = client.post("/api/contacts/", json=payload.model_dump())

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload.name
    assert data["email"] == payload.email
    assert data["message"] == payload.message
    assert data["id"] == 1
    assert "created_at" in data


def test_list_contacts(client: TestClient, db_session: Session) -> None:
    ContactFactory.create_batch(2)

    response = client.get("/api/contacts/")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_contact(client: TestClient, db_session: Session) -> None:
    contact = ContactFactory.create(name="Alice", email="alice@example.com")

    response = client.get(f"/api/contacts/{contact.id}")

    assert response.status_code == 200
    assert response.json()["email"] == "alice@example.com"


def test_get_contact_not_found(client: TestClient) -> None:
    response = client.get("/api/contacts/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Contact not found"


def test_create_contact_validation_error(client: TestClient) -> None:
    response = client.post(
        "/api/contacts/",
        json={"name": "A", "email": "invalid", "message": "short"},
    )

    assert response.status_code == 422

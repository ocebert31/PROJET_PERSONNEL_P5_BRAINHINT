import factory
from factory.alchemy import SQLAlchemyModelFactory

from app.models.contact import Contact
from app.schemas.contact import ContactCreate


class ContactCreateFactory(factory.Factory):
    class Meta:
        model = ContactCreate

    name = factory.Faker("name")
    email = factory.Faker("email")
    message = factory.Faker("text", max_nb_chars=100)


class ContactFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Contact
        sqlalchemy_session_persistence = "commit"

    name = factory.Faker("name")
    email = factory.Faker("email")
    message = factory.Faker("text", max_nb_chars=100)

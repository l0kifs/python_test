import os

from peewee import MySQLDatabase, Model, CharField


def test_positive():
    assert 1==1


def test_negative():
    assert 1==2


def test_connect_db():
    db = MySQLDatabase(None)

    class BaseModel(Model):
        class Meta:
            database = db

    class Iban(BaseModel):
        iban = CharField(unique=True)
        swift = CharField()
        country_code = CharField()
        beneficiary_country = CharField()

    db.init('qa-tests',
            user='qa-tests',
            password=os.environ.get("PASS", ""),
            host=os.environ.get("HOST", ""),
            port=3306)

    iban = Iban.select().first()
    print('ibans =>', iban.swift)

    db.close()



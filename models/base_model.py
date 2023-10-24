"""Base model defining all common attributes/methods for other classes"""
import datetime
import uuid


class BaseModel:
    uuid.uuid4()
    created_at = datetime.datetime.now
    updated_at = datetime

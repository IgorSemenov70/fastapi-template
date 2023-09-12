from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID


@dataclass
class User:
    id: UUID = field(init=False)
    username: str | None
    first_name: str
    last_name: str
    created_at: datetime
    updated_at: datetime

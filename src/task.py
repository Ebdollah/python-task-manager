from dataclasses import dataclass
import json
import uuid
from typing import List

@dataclass
class Task:
    taskId: str
    taskName: str
    taskDesc: str
    markCompleted: bool = False

    @staticmethod
    def generate_short_uuid() -> str:
        return str(uuid.uuid4().int)


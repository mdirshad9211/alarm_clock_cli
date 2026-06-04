import json
import os
from typing import List, Dict


class AlarmRepository:

    def __init__(self, file_name: str = "alarms.json"):
        self.file_name = file_name

    def get_all_alarms(self) -> List[Dict]:

        if not os.path.exists(self.file_name):
            return []

        try:
            with open(self.file_name, "r") as file:
                return json.load(file)

        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_all_alarms(self, alarms: List[Dict]) -> None:

        with open(self.file_name, "w") as file:
            json.dump(alarms, file, indent=4)
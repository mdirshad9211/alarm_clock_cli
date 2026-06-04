import time
from datetime import datetime
from typing import List, Dict

from alarm_repository import AlarmRepository


class AlarmService:

    def __init__(self, repository: AlarmRepository):
        self.repository = repository

    def validate_time(self, alarm_time: str) -> bool:

        try:
            datetime.strptime(alarm_time, "%H:%M")
            return True
        except ValueError:
            return False

    def add_alarm(
        self,
        alarm_time: str,
        label: str
    ) -> None:

        if not self.validate_time(alarm_time):
            raise ValueError(
                "Invalid time format. Use HH:MM"
            )

        alarms = self.repository.get_all_alarms()

        next_alarm_id = (
            max(
                [alarm["alarm_id"] for alarm in alarms],
                default=0
            )
            + 1
        )

        new_alarm = {
            "alarm_id": next_alarm_id,
            "alarm_time": alarm_time,
            "label": label
        }

        alarms.append(new_alarm)

        self.repository.save_all_alarms(alarms)

    def list_alarms(self) -> List[Dict]:

        return self.repository.get_all_alarms()

    def delete_alarm(self, alarm_id: int) -> bool:

        alarms = self.repository.get_all_alarms()

        filtered_alarms = [
            alarm
            for alarm in alarms
            if alarm["alarm_id"] != alarm_id
        ]

        if len(filtered_alarms) == len(alarms):
            return False

        self.repository.save_all_alarms(
            filtered_alarms
        )

        return True

    def run_alarm_clock(self) -> None:

        print("Alarm clock started...")
        print("Press CTRL + C to stop")

        triggered_alarm_ids = set()

        try:

            while True:

                current_time = datetime.now().strftime(
                    "%H:%M"
                )

                alarms = (
                    self.repository.get_all_alarms()
                )

                for alarm in alarms:

                    if (
                        alarm["alarm_time"]
                        == current_time
                        and alarm["alarm_id"]
                        not in triggered_alarm_ids
                    ):

                        print("\n")
                        print("=" * 40)
                        print(
                            f"⏰ ALARM: {alarm['label']}"
                        )
                        print("=" * 40)
                        print("\n")

                        triggered_alarm_ids.add(
                            alarm["alarm_id"]
                        )

                time.sleep(1)

        except KeyboardInterrupt:

            print("\nAlarm clock stopped.")
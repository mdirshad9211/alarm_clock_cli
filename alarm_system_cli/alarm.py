from dataclasses import dataclass


@dataclass
class Alarm:
    alarm_id: int
    alarm_time: str
    label: str
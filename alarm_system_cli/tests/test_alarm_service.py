import os

from alarm_repository import AlarmRepository
from alarm_service import AlarmService


TEST_FILE = "test_alarms.json"


def cleanup():

    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_add_alarm():

    cleanup()

    repository = AlarmRepository(
        TEST_FILE
    )

    service = AlarmService(
        repository
    )

    service.add_alarm(
        "07:00",
        "Morning Workout"
    )

    alarms = (
        repository.get_all_alarms()
    )

    assert len(alarms) == 1

    cleanup()


def test_delete_alarm():

    cleanup()

    repository = AlarmRepository(
        TEST_FILE
    )

    service = AlarmService(
        repository
    )

    service.add_alarm(
        "07:00",
        "Workout"
    )

    result = service.delete_alarm(1)

    assert result is True

    cleanup()


def test_invalid_time():

    cleanup()

    repository = AlarmRepository(
        TEST_FILE
    )

    service = AlarmService(
        repository
    )

    try:

        service.add_alarm(
            "99:99",
            "Invalid"
        )

        assert False

    except ValueError:

        assert True

    cleanup()
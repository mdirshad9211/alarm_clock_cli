import argparse

from alarm_repository import AlarmRepository
from alarm_service import AlarmService


def main():

    repository = AlarmRepository()

    alarm_service = AlarmService(
        repository
    )

    parser = argparse.ArgumentParser(
        description="Alarm Clock CLI Application"
    )

    sub_parsers = parser.add_subparsers(
        dest="command"
    )

    add_parser = sub_parsers.add_parser(
        "add"
    )

    add_parser.add_argument(
        "--time",
        required=True,
        help="Alarm time in HH:MM format"
    )

    add_parser.add_argument(
        "--label",
        required=True,
        help="Alarm label"
    )

    sub_parsers.add_parser("list")

    delete_parser = sub_parsers.add_parser(
        "delete"
    )

    delete_parser.add_argument(
        "--id",
        required=True,
        type=int
    )

    sub_parsers.add_parser("run")

    args = parser.parse_args()

    if args.command == "add":

        try:

            alarm_service.add_alarm(
                args.time,
                args.label
            )

            print(
                "Alarm added successfully."
            )

        except ValueError as error:

            print(error)

    elif args.command == "list":

        alarms = (
            alarm_service.list_alarms()
        )

        if not alarms:

            print("No alarms found.")
            return

        print("\nSaved Alarms")
        print("-" * 50)

        for alarm in alarms:

            print(
                f"ID: {alarm['alarm_id']} | "
                f"Time: {alarm['alarm_time']} | "
                f"Label: {alarm['label']}"
            )

    elif args.command == "delete":

        is_deleted = (
            alarm_service.delete_alarm(
                args.id
            )
        )

        if is_deleted:
            print(
                "Alarm deleted successfully."
            )
        else:
            print(
                "Alarm not found."
            )

    elif args.command == "run":

        alarm_service.run_alarm_clock()

    else:

        parser.print_help()


if __name__ == "__main__":
    main()
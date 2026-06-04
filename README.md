# Alarm Clock CLI Application

A simple and maintainable command-line Alarm Clock application built with Python.

This project was developed as a take-home assignment with a focus on clean code, separation of concerns, maintainability, testing, and practical software engineering principles.

---

# Features

## Functional Features

* Add a new alarm
* List all saved alarms
* Delete an existing alarm
* Run the alarm scheduler
* Support multiple alarms
* Persistent storage using JSON
* Alarm labels for easier identification

## Engineering Features

* Clean and readable code
* Input validation
* Error handling
* Type hints
* Unit tests
* Separation of concerns
* SOLID principles where applicable
* DRY (Don't Repeat Yourself) principle
* Meaningful variable and function names

---

# AI-Assisted Planning Process

The assignment intentionally provided minimal requirements:

> Build an alarm clock as a Python CLI application.

Before implementation, AI was used to help refine requirements, identify edge cases, and validate design decisions.

## Questions Explored

* Should alarms persist after application restarts?
* Should multiple alarms be supported?
* How should alarms be stored?
* Should alarm labels be supported?
* How should invalid time inputs be handled?
* What architecture would keep the solution simple and maintainable?

## Decisions Made

* Multiple alarms are supported.
* Alarms persist between application runs.
* JSON is used as lightweight storage.
* Time validation is included.
* The application remains CLI-only.
* Simplicity was prioritized over unnecessary complexity.

## How AI Was Used

AI was used during the planning and design phase to:

* Refine ambiguous requirements
* Explore implementation approaches
* Identify edge cases
* Review architectural decisions
* Validate design tradeoffs

All final implementation decisions, code organization, testing strategy, and project structure were reviewed and adjusted manually.

---

# Assumptions

Since no detailed specification was provided, the following assumptions were made:

1. Users may create multiple alarms.
2. Alarm data should persist after application restart.
3. Alarm times follow 24-hour format (`HH:MM`).
4. JSON storage is sufficient for the scope of this assignment.
5. Terminal output is an acceptable notification mechanism.

---

# Project Structure

```text
alarm-clock-cli/

├── main.py
├── alarm.py
├── alarm_repository.py
├── alarm_service.py
├── alarms.json
├── requirements.txt

├── tests/
│   └── test_alarm_service.py

└── README.md
```

---

# Architecture

The project follows a simple layered structure to keep responsibilities separated and the code easy to maintain.

## Alarm Entity

**File:** `alarm.py`

Represents alarm-related data.

Responsibilities:

* Store alarm information
* Represent alarm objects

---

## Repository Layer

**File:** `alarm_repository.py`

Handles all storage-related operations.

Responsibilities:

* Read alarms from JSON
* Save alarms to JSON
* Isolate persistence logic

---

## Service Layer

**File:** `alarm_service.py`

Contains business logic.

Responsibilities:

* Create alarms
* Delete alarms
* Validate input
* Manage scheduler logic
* Coordinate alarm operations

---

## CLI Layer

**File:** `main.py`

Handles user interaction.

Responsibilities:

* Parse command-line arguments
* Execute user commands
* Display application output

---

# Design Decisions

## Why JSON Instead of a Database?

The assignment only required a CLI application.

Using JSON provides persistence while keeping the implementation lightweight and easy to understand.

## Why argparse?

`argparse` is part of Python's standard library and is a reliable solution for building command-line interfaces without additional dependencies.

## Why Separate Service and Repository Layers?

Separating business logic from storage logic improves:

* Maintainability
* Readability
* Testability

This allows changes to storage implementation without affecting business logic.

---

# SOLID Principles Applied

## Single Responsibility Principle (SRP)

Each component has one clear responsibility:

* `AlarmRepository` handles storage operations.
* `AlarmService` handles business logic.
* `main.py` handles command-line interaction.

## Dependency Inversion Principle (DIP)

`AlarmService` depends on `AlarmRepository` rather than performing file operations directly.

This improves maintainability and makes testing easier.

---

# DRY Principle

The DRY (Don't Repeat Yourself) principle is followed by:

* Centralizing storage operations in one repository
* Centralizing validation logic
* Reusing service methods
* Avoiding duplicated alarm-management code

---

# Error Handling

The application handles common error scenarios.

## Invalid Time Format

Example:

```bash
python main.py add --time 99:99 --label "Wake Up"
```

Output:

```text
Invalid time format. Use HH:MM
```

---

## Non-Existing Alarm

Example:

```bash
python main.py delete --id 100
```

Output:

```text
Alarm not found.
```

---

## Corrupted Storage File

If the JSON file becomes corrupted, the application safely returns an empty list instead of crashing.

---

# Installation

## Clone the Repository

```bash
git clone <repository-url>
```

## Navigate to the Project

```bash
cd alarm-clock-cli
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

## Add Alarm

```bash
python main.py add --time 07:00 --label "Morning Workout"
```

Output:

```text
Alarm added successfully.
```

---

## List Alarms

```bash
python main.py list
```

Output:

```text
Saved Alarms

ID: 1 | Time: 07:00 | Label: Morning Workout
ID: 2 | Time: 09:00 | Label: Team Meeting
```

---

## Delete Alarm

```bash
python main.py delete --id 1
```

Output:

```text
Alarm deleted successfully.
```

---

## Run Alarm Scheduler

```bash
python main.py run
```

Output:

```text
Alarm clock started...
Press CTRL + C to stop
```

When an alarm triggers:

```text
========================================
⏰ ALARM: Morning Workout
========================================
```

---

# Example Workflow

### Create an Alarm

```bash
python main.py add --time 07:00 --label "Morning Workout"
```

### View Saved Alarms

```bash
python main.py list
```

### Start the Scheduler

```bash
python main.py run
```

### Delete an Alarm

```bash
python main.py delete --id 1
```

---

# Running Tests

Execute all tests:

```bash
pytest
```

Expected output:

```text
3 passed
```

---

# Tradeoffs

To keep the solution aligned with the assignment requirements, the following tradeoffs were made.

## Included

* JSON persistence
* Input validation
* Unit tests
* Multiple alarm support
* Separation of concerns

## Not Included

* GUI
* Database
* Cloud storage
* Email notifications
* SMS notifications
* Recurring alarms
* Snooze functionality
* Dockerization

These features could be added later but were intentionally excluded to keep the implementation focused and maintainable.

---

# Future Improvements

If additional time were available, the following enhancements could be added.

## Functional Improvements

* Recurring alarms
* Snooze functionality
* Alarm editing
* Desktop notifications
* Sound notifications
* Time zone support

## Engineering Improvements

* SQLite storage
* Repository interface abstraction
* Structured logging
* Integration tests
* CI/CD pipeline
* Docker support
* Configuration management

---

# Testing Strategy

The project includes unit tests covering:

* Alarm creation
* Alarm deletion
* Time validation

The focus was on validating business logic independently from the command-line interface.

---

# Why This Design?

The primary goal was to balance:

* Simplicity
* Readability
* Maintainability
* Extensibility

The application intentionally avoids unnecessary complexity while still demonstrating practical software engineering practices.

The result is a lightweight, easy-to-understand CLI application that satisfies the assignment requirements and provides a solid foundation for future enhancements.

---

# Author Notes

This project was developed as part of a software engineering take-home assignment.

The implementation focuses on:

* Clean code
* Practical design decisions
* Maintainability
* Testing
* Documentation

while keeping the solution intentionally simple and aligned with the stated requirements.

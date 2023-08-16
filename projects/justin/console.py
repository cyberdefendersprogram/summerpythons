import os.path

from task import *


def _ask_y_or_n(prompt: str) -> bool:
    return input(prompt + " (y/n): ").lower() == "y"


def _create_task() -> Task:
    task_name = input("Enter the name of the task: ")
    task_execution_path = input("Enter the execution path of the task: ")
    return Task(task_name, os.path.expandvars(task_execution_path))


def _validate_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input!")


def _validate_console(condition: bool, message=""):
    if not condition:
        raise ConsoleError(message)


def _task_creation_process(tasks=None) -> list[Task]:
    if tasks is None:
        tasks = []
    while True:
        tasks.append(_create_task())

        if not _ask_y_or_n("Do you want to add another task?"):
            break

    return tasks


def _print_tasks(tasks: list[Task]):
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task.name} :: ({task.execution_path})")


class Console:
    def __init__(self, file_path: str):
        self.task_manager = TaskManager(file_path)
        self.operations = [
            ConsoleOperation("Create a task preset", self.create_task_preset),
            ConsoleOperation("Remove a task preset", self.remove_task_preset),
            ConsoleOperation("Edit a task preset", self.edit_task_preset),
            ConsoleOperation("Start a task preset", self.start_task_preset),
        ]

    def start(self):
        print("Welcome to the TaskPresets program!")

        while True:
            print("\nWhat do you want to do?")
            self._print_console_operations()

            choice = _validate_int_input("Enter your choice: ")

            print()

            try:
                if choice == len(self.operations) + 1:
                    return

                self.operations[choice - 1].function()
            except ConsoleError as error:
                print(error.message)

    def _print_console_operations(self):
        for i, operation in enumerate(self.operations):
            print(f"{i + 1}. {operation.name}")

        print(f"{len(self.operations) + 1}. Exit")

    def create_task_preset(self):
        tasks = _task_creation_process()

        focus_mode = _ask_y_or_n("Do you want to enable focus mode?")

        task_preset_name = input("Enter the name of the task preset: ")
        task_preset = TaskPreset(task_preset_name, tasks, focus_mode)

        self.task_manager.add_task_preset(task_preset)

    def remove_task_preset(self):
        task_preset = self._get_task_preset("Which task preset do you want to remove?")

        if _ask_y_or_n(f"Are you sure you want to remove the task preset '{task_preset.name}'?"):
            self.task_manager.remove_task_preset(task_preset)
            print(f"Successfully removed the task preset '{task_preset.name}'!")

    def edit_task_preset(self):
        task_preset = self._get_task_preset("Which task preset do you want to edit?")

        name = input(f"Enter the new name of the task preset or press enter to keep the name '{task_preset.name}': ")
        tasks = task_preset.tasks.copy()

        if _ask_y_or_n("Do you want to edit the tasks?"):
            tasks = _task_creation_process(tasks)

        focus_mode = _ask_y_or_n(f"Do you want to enable focus mode? (currently {task_preset.focus_mode})")

        self.task_manager.remove_task_preset(task_preset)
        self.task_manager.add_task_preset(TaskPreset(name if name else task_preset.name, tasks, focus_mode))

    def start_task_preset(self):
        task_preset = self._get_task_preset("Which task preset do you want to start?")
        task_preset.start_up()

    def _get_task_preset(self, prompt: str) -> TaskPreset:
        self._validate_task_preset_not_empty()

        print(prompt)
        self._list_task_presets()

        choice = input("Enter your choice: ")

        try:
            return self.task_manager.task_presets[int(choice) - 1]
        except ValueError:
            print("Invalid choice!")

    def _list_task_presets(self):
        for i, task_preset in enumerate(self.task_manager.task_presets):
            print(f"{i + 1}. {task_preset.name}")

    def _validate_task_preset_not_empty(self):
        _validate_console(len(self.task_manager.task_presets) > 0, "There are no task presets! Please create one first.")


class ConsoleError(Exception):

    def __init__(self, message: str):
        self.message = message


class ConsoleOperation:

    def __init__(self, name: str, function: callable):
        self.name = name
        self.function = function

    def __call__(self):
        self.function()
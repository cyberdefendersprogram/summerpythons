import os
import json
from dataclasses import dataclass


@dataclass
class Task:
    name: str
    execution_path: str

    def start_up(self):
        os.startfile(self.execution_path)


class TaskEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


@dataclass
class TaskPreset:
    name: str
    tasks: list[Task]
    focus_mode: bool = False

    def start_up(self):
        for task in self.tasks:
            task.start_up()

        if self.focus_mode:
            self.focus()

    def focus(self):
        pass

    def encode(self):
        return self.__dict__

    @staticmethod
    def decode(json_data: dict):
        return TaskPreset(json_data["name"], [Task(**task) for task in json_data["tasks"]], json_data["focus_mode"])


class TaskManager:
    def __init__(self, file_path: str):
        self.json_file_path = file_path
        self.task_presets: list[TaskPreset] = []
        self.load_task_presets()

    def load_task_presets(self):
        if os.path.exists(self.json_file_path):
            with open(self.json_file_path, "r") as file:
                self.task_presets = [TaskPreset.decode(task_preset) for task_preset in json.load(file)]
        else:
            self.task_presets = []

    def save_task_presets(self):
        with open(self.json_file_path, "w") as file:
            json.dump([task_preset.__dict__ for task_preset in self.task_presets], file, cls=TaskEncoder)

    def add_task_preset(self, task_preset: TaskPreset):
        self.task_presets.append(task_preset)
        self.save_task_presets()

    def remove_task_preset(self, task_preset: TaskPreset):
        self.task_presets.remove(task_preset)
        self.save_task_presets()
